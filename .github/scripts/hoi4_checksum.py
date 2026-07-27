#!/usr/bin/env python3
"""Calculate a Hearts of Iron IV checksum from fixed vanilla facts and one mod.

The eight-digit checksum logged for each file is:

```python
sum1 = 0
sum2 = 0
for byte in contents:
    sum1 = (sum1 + byte) % 65535
    sum2 = (sum2 + sum1) % 65535
file_checksum = (sum1 << 16) | sum2
```

The aggregate does not use those eight-digit values. HOI4 first enumerates
files using case-sensitive path names, but reopens each result through its
case-insensitive virtual filesystem. A differently-cased mod file can
therefore supply the contents for two separately enumerated paths.

For each path that can be reopened, HOI4 calculates:

```text
inner[i] = MD5(raw file contents || UTF-8 virtual path)
```

If reopening the path fails, the worker leaves the digest untouched:

```text
inner[i] = MD5(empty input)
```

It then calculates:

```text
global = MD5(
    inner[0] || inner[1] || ... || inner[n] ||
    UTF-8 "Operation Postern v1.19.2.0.a729"
)
```

Each `inner` value contributes its raw 16 bytes, not its 32-character hex
encoding. Virtual paths use forward slashes. Files are ordered by manifest
rule, then by HOI4's depth-first directory order: files in a directory first,
followed by subdirectories, with names sorted ordinally.

HOI4 has unusual checksum-only behavior for `replace_path`. Vanilla entries
under the replacement are removed normally, but mod entries below a nested
replacement are emitted at the manifest rule's root. For example:

```text
common/abilities/example.txt -> common/example.txt
history/countries/ABC.txt    -> history/ABC.txt
```

Their position still comes from the original unflattened tree. Duplicate
emitted paths are retained. These flattened paths usually cannot be reopened,
so they contribute `MD5(empty input)`. This is also why the game's unmodified
per-file checksum diagnostic can crash for large replacement-heavy mods.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path


FACTS_HEADER = "hoi4-vanilla-facts-v1"
REPLACE_PATH_RE = re.compile(
    r'^\s*replace_path\s*=\s*"([^"]+)"', re.IGNORECASE
)


@dataclass(frozen=True)
class Rule:
    directory: str
    extension: str


@dataclass
class Entry:
    digest: bytes
    file_checksum: str
    data: bytes | None = None


def new_md5(data: bytes = b""):
    try:
        return hashlib.md5(data, usedforsecurity=False)
    except TypeError:
        return hashlib.md5(data)


def normalize_virtual_path(path: str) -> str:
    return path.replace("\\", "/").strip("/")


def matching_rule(path: str, rules: list[Rule]) -> int | None:
    lower_path = path.lower()
    for index, rule in enumerate(rules):
        prefix = rule.directory.lower() + "/"
        if lower_path.startswith(prefix) and lower_path.endswith(
            rule.extension.lower()
        ):
            return index
    return None


def tree_order_key(path: str, rules: list[Rule]) -> tuple[object, ...]:
    rule_index = matching_rule(path, rules)
    if rule_index is None:
        raise ValueError(f"path is not covered by the checksum rules: {path}")

    rule = rules[rule_index]
    relative = path[len(rule.directory) + 1 :]
    parts = relative.split("/")
    key: list[object] = [rule_index]
    for directory in parts[:-1]:
        key.extend((1, directory))
    key.extend((0, parts[-1]))
    return tuple(key)


def hoi4_file_checksum(data: bytes) -> str:
    sum1 = 0
    sum2 = 0
    for value in data:
        sum1 = (sum1 + value) % 65535
        sum2 = (sum2 + sum1) % 65535
    return f"{sum1:04x}{sum2:04x}"


def inner_digest(data: bytes, virtual_path: str) -> bytes:
    checksum = new_md5()
    checksum.update(data)
    checksum.update(virtual_path.encode("utf-8"))
    return checksum.digest()


def read_facts(path: Path) -> tuple[str, list[Rule], dict[str, Entry]]:
    salt: str | None = None
    rules: list[Rule] = []
    entries: dict[str, Entry] = {}

    with path.open("r", encoding="utf-8", newline="") as facts:
        first = facts.readline().rstrip("\r\n")
        if first != f"# {FACTS_HEADER}":
            raise ValueError(
                f"{path} is not a {FACTS_HEADER} file"
            )

        for line_number, raw_line in enumerate(facts, start=2):
            line = raw_line.rstrip("\r\n")
            if not line or line.startswith("#"):
                continue
            fields = line.split("\t")
            kind = fields[0]
            if kind == "salt" and len(fields) == 2:
                salt = fields[1]
            elif (
                kind in {
                    "version",
                    "steam_previous_version",
                    "steam_public_build_id",
                    "checksum",
                }
                and len(fields) == 2
            ):
                continue
            elif kind == "rule" and len(fields) == 3:
                rules.append(
                    Rule(normalize_virtual_path(fields[1]), fields[2])
                )
            elif kind == "file" and len(fields) == 4:
                virtual_path = normalize_virtual_path(fields[1])
                try:
                    digest = bytes.fromhex(fields[2])
                except ValueError as error:
                    raise ValueError(
                        f"{path}:{line_number}: invalid MD5 digest"
                    ) from error
                if len(digest) != 16:
                    raise ValueError(
                        f"{path}:{line_number}: MD5 digest must be 16 bytes"
                    )
                entries[virtual_path] = Entry(digest, fields[3].lower())
            else:
                raise ValueError(
                    f"{path}:{line_number}: invalid facts record"
                )

    if salt is None:
        raise ValueError(f"{path}: missing salt record")
    if not rules:
        raise ValueError(f"{path}: no checksum rules")
    if not entries:
        raise ValueError(f"{path}: no vanilla file records")
    return salt, rules, entries


def read_replace_paths(mod_directory: Path) -> list[str]:
    descriptor = mod_directory / "descriptor.mod"
    if not descriptor.is_file():
        return []

    replacements: list[str] = []
    with descriptor.open("r", encoding="utf-8-sig", errors="replace") as source:
        for line in source:
            match = REPLACE_PATH_RE.match(line)
            if match:
                replacements.append(normalize_virtual_path(match.group(1)))
    return replacements


def is_replaced(path: str, replacements: list[str]) -> bool:
    lower_path = path.lower()
    for replacement in replacements:
        lower_replacement = replacement.lower()
        if (
            lower_path == lower_replacement
            or lower_path.startswith(lower_replacement + "/")
        ):
            return True
    return False


def read_mod_entry(
    item: tuple[Path, str, bool],
) -> tuple[str, Entry]:
    physical_path, virtual_path, include_file_checksum = item
    data = physical_path.read_bytes()
    file_checksum = hoi4_file_checksum(data) if include_file_checksum else ""
    return virtual_path, Entry(
        inner_digest(data, virtual_path),
        file_checksum,
        data,
    )


def apply_mod(
    entries: dict[str, Entry],
    rules: list[Rule],
    mod_directory: Path,
    include_file_checksums: bool = True,
) -> list[str]:
    replacements = read_replace_paths(mod_directory)
    if replacements:
        for path in list(entries):
            if is_replaced(path, replacements):
                del entries[path]

    mod_files: list[tuple[Path, str, bool]] = []
    for root, directory_names, file_names in os.walk(mod_directory):
        directory_names.sort()
        file_names.sort()
        root_path = Path(root)
        for file_name in file_names:
            physical_path = root_path / file_name
            virtual_path = physical_path.relative_to(mod_directory).as_posix()
            if matching_rule(virtual_path, rules) is None:
                continue

            mod_files.append(
                (physical_path, virtual_path, include_file_checksums)
            )

    with ThreadPoolExecutor() as executor:
        for virtual_path, entry in executor.map(read_mod_entry, mod_files):
            entries[virtual_path] = entry
    return replacements


def emitted_path(
    original_path: str, replacements: list[str], rules: list[Rule]
) -> str:
    lower_path = original_path.lower()
    matching_replacements = [
        replacement
        for replacement in replacements
        if (
            lower_path == replacement.lower()
            or lower_path.startswith(replacement.lower() + "/")
        )
    ]
    if not matching_replacements:
        return original_path

    replacement = max(matching_replacements, key=len)
    suffix = original_path[len(replacement) :].lstrip("/")
    if not suffix:
        return original_path

    rule_index = matching_rule(original_path, rules)
    if rule_index is None:
        return original_path
    return f"{rules[rule_index].directory}/{suffix}"


def calculate_checksum(
    salt: str,
    rules: list[Rule],
    entries: dict[str, Entry],
    replacements: list[str] | None = None,
) -> tuple[str, list[tuple[str, str]]]:
    replacements = replacements or []
    ordered_original_paths = sorted(
        entries, key=lambda path: tree_order_key(path, rules)
    )

    visible_by_casefold: dict[str, tuple[str, Entry]] = {}
    for path, entry in entries.items():
        key = path.casefold()
        if key not in visible_by_casefold or entry.data is not None:
            visible_by_casefold[key] = (path, entry)

    checksum = new_md5()
    output_files: list[tuple[str, str]] = []
    failed_digest = new_md5().digest()
    for original_path in ordered_original_paths:
        path = emitted_path(original_path, replacements, rules)
        resolved = visible_by_casefold.get(path.casefold())
        if resolved is None:
            digest = failed_digest
            file_checksum = "00000000"
        else:
            resolved_path, entry = resolved
            if resolved_path == path:
                digest = entry.digest
            elif entry.data is not None:
                digest = inner_digest(entry.data, path)
            else:
                raise ValueError(
                    "vanilla facts cannot rehash a differently-cased path: "
                    f"{path} resolves to {resolved_path}"
                )
            file_checksum = entry.file_checksum
        checksum.update(digest)
        output_files.append((path, file_checksum))

    checksum.update(salt.encode("utf-8"))
    return checksum.hexdigest(), output_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Calculate a HOI4 aggregate checksum from fixed vanilla facts "
            "and one unpacked mod directory."
        )
    )
    parser.add_argument("vanilla_facts", type=Path)
    parser.add_argument("mod_directory", type=Path)
    parser.add_argument(
        "--show-files",
        action="store_true",
        help="print the engine-style per-file checksums before the aggregate",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        facts_path = args.vanilla_facts.resolve(strict=True)
        mod_directory = args.mod_directory.resolve(strict=True)
        if not mod_directory.is_dir():
            raise ValueError(f"{mod_directory} is not a directory")

        salt, rules, entries = read_facts(facts_path)
        replacements = apply_mod(
            entries,
            rules,
            mod_directory,
            include_file_checksums=args.show_files,
        )
        checksum, output_files = calculate_checksum(
            salt, rules, entries, replacements
        )

        if args.show_files:
            for path, file_checksum in output_files:
                print(f"[{file_checksum}] File: {path}")
        print(checksum)
        return 0
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

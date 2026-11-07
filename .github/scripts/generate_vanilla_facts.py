#!/usr/bin/env python3
"""Generate a verified HOI4 vanilla facts file from a checksum log.

First run the matching vanilla game build with `--checksum` and per-file
logging enabled. Then supply that `system.log` and the matching installation
directory:

```powershell
python .\generate_vanilla_facts.py `
  "C:\path\to\vanilla-system.log" `
  "C:\path\to\Hearts of Iron IV" `
  .\vanilla-facts.tsv
```

The log alone is insufficient because it contains the eight-digit diagnostic
values, not the inner MD5 values. The generator reads the raw files named by
the log and the installation's `checksum_manifest.txt`.

Before writing the output, it verifies:

- the log reports zero active mods;
- the logged file count and manifest coverage;
- every per-file checksum against the file on disk;
- the complete engine path order;
- the reconstructed aggregate against `Checksum in HEX`.

It refuses to overwrite an existing output unless `--force` is supplied.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import hoi4_checksum as h


VERSION_RE = re.compile(
    r"Version:\s*(.+?)\s+\([0-9a-f]{4}\)\s+build time:",
    re.IGNORECASE,
)
AGGREGATE_RE = re.compile(r"Checksum in HEX:\s*([0-9a-f]{32})", re.IGNORECASE)
COUNT_RE = re.compile(r"Checksum files:\s*(\d+)")
FILE_RE = re.compile(
    r"\[([0-9a-f]{8})\]\s+File:\s+(.+)$",
    re.IGNORECASE,
)
MOD_COUNT_RE = re.compile(r"Active Mod Count:\s*(\d+)")


def parse_manifest(path: Path) -> list[h.Rule]:
    rules: list[h.Rule] = []
    block: dict[str, str] | None = None

    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line == "directory":
            if block is not None:
                rules.append(manifest_rule(path, block))
            block = {}
            continue
        if block is None or "=" not in line:
            raise ValueError(f"{path}: malformed manifest line: {raw_line}")
        key, value = line.split("=", 1)
        block[key.strip()] = value.strip()

    if block is not None:
        rules.append(manifest_rule(path, block))
    if not rules:
        raise ValueError(f"{path}: no directory rules")
    return rules


def manifest_rule(path: Path, block: dict[str, str]) -> h.Rule:
    try:
        directory = h.normalize_virtual_path(block["name"])
        extension = block["file_extension"]
    except KeyError as error:
        raise ValueError(
            f"{path}: manifest directory block is missing {error.args[0]}"
        ) from error
    if block.get("sub_directories", "").lower() != "yes":
        raise ValueError(
            f"{path}: unsupported non-recursive rule for {directory}"
        )
    return h.Rule(directory, extension)


def parse_log(path: Path) -> tuple[str, str, list[tuple[str, str]]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()

    mod_counts = [
        int(match.group(1))
        for line in lines
        if (match := MOD_COUNT_RE.search(line))
    ]
    if mod_counts and mod_counts[-1] != 0:
        raise ValueError(
            f"{path}: expected a vanilla run, found "
            f"Active Mod Count: {mod_counts[-1]}"
        )

    salt_matches = [
        match.group(1)
        for line in lines
        if (match := VERSION_RE.search(line))
    ]
    if not salt_matches:
        raise ValueError(f"{path}: version/build salt was not found")
    salt = salt_matches[-1]

    aggregate_indexes = [
        (index, match.group(1).lower())
        for index, line in enumerate(lines)
        if (match := AGGREGATE_RE.search(line))
    ]
    if not aggregate_indexes:
        raise ValueError(f"{path}: aggregate checksum was not found")
    aggregate_index, expected_checksum = aggregate_indexes[-1]

    count: int | None = None
    files: list[tuple[str, str]] = []
    for line in lines[aggregate_index + 1 :]:
        if count is None:
            match = COUNT_RE.search(line)
            if match:
                count = int(match.group(1))
            continue
        match = FILE_RE.search(line)
        if match:
            files.append(
                (
                    h.normalize_virtual_path(match.group(2)),
                    match.group(1).lower(),
                )
            )

    if count is None:
        raise ValueError(f"{path}: checksum file count was not found")
    if len(files) != count:
        raise ValueError(
            f"{path}: expected {count} file records, found {len(files)}"
        )
    if len({virtual_path for virtual_path, _ in files}) != len(files):
        raise ValueError(f"{path}: vanilla log contains duplicate paths")
    return salt, expected_checksum, files


def safe_physical_path(game_directory: Path, virtual_path: str) -> Path:
    relative = Path(*virtual_path.split("/"))
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"unsafe virtual path in log: {virtual_path}")
    physical = (game_directory / relative).resolve(strict=True)
    if not physical.is_relative_to(game_directory):
        raise ValueError(f"path escapes the game directory: {virtual_path}")
    if not physical.is_file():
        raise ValueError(f"not a regular file: {physical}")
    return physical


def generate(
    log_path: Path, game_directory: Path
) -> tuple[str, list[h.Rule], list[tuple[str, h.Entry]]]:
    salt, expected_checksum, logged_files = parse_log(log_path)
    rules = parse_manifest(game_directory / "checksum_manifest.txt")
    entries: list[tuple[str, h.Entry]] = []

    for virtual_path, logged_file_checksum in logged_files:
        if h.matching_rule(virtual_path, rules) is None:
            raise ValueError(
                f"log path is not covered by checksum_manifest.txt: "
                f"{virtual_path}"
            )
        data = safe_physical_path(game_directory, virtual_path).read_bytes()
        calculated_file_checksum = h.hoi4_file_checksum(data)
        if calculated_file_checksum != logged_file_checksum:
            raise ValueError(
                f"{virtual_path}: logged file checksum "
                f"{logged_file_checksum}, calculated "
                f"{calculated_file_checksum}"
            )
        entries.append(
            (
                virtual_path,
                h.Entry(
                    h.inner_digest(data, virtual_path),
                    calculated_file_checksum,
                ),
            )
        )

    expected_order = sorted(
        (virtual_path for virtual_path, _ in entries),
        key=lambda virtual_path: h.tree_order_key(virtual_path, rules),
    )
    logged_order = [virtual_path for virtual_path, _ in entries]
    if expected_order != logged_order:
        mismatch = next(
            index
            for index, pair in enumerate(zip(expected_order, logged_order))
            if pair[0] != pair[1]
        )
        raise ValueError(
            f"engine order mismatch at entry {mismatch}: "
            f"expected {expected_order[mismatch]}, "
            f"logged {logged_order[mismatch]}"
        )

    calculated_checksum, output_files = h.calculate_checksum(
        salt, rules, dict(entries)
    )
    if len(output_files) != len(entries):
        raise ValueError("facts entry count changed during verification")
    if calculated_checksum != expected_checksum:
        raise ValueError(
            f"aggregate mismatch: logged {expected_checksum}, "
            f"calculated {calculated_checksum}"
        )
    return salt, rules, entries


def write_facts(
    output_path: Path,
    salt: str,
    checksum: str,
    rules: list[h.Rule],
    entries: list[tuple[str, h.Entry]],
    force: bool,
) -> None:
    if output_path.exists() and not force:
        raise FileExistsError(
            f"{output_path} already exists; pass --force to replace it"
        )

    lines = [
        f"# {h.FACTS_HEADER}",
        f"salt\t{salt}",
        f"checksum\t{checksum}",
    ]
    lines.extend(
        f"rule\t{rule.directory}\t{rule.extension}" for rule in rules
    )
    lines.extend(
        f"file\t{virtual_path}\t{entry.digest.hex()}\t"
        f"{entry.file_checksum}"
        for virtual_path, entry in entries
    )
    output_path.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a verified HOI4 vanilla facts file from a vanilla "
            "--checksum system.log and its matching game directory."
        )
    )
    parser.add_argument("system_log", type=Path)
    parser.add_argument("game_directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace the output file if it already exists",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        log_path = args.system_log.resolve(strict=True)
        game_directory = args.game_directory.resolve(strict=True)
        if not game_directory.is_dir():
            raise ValueError(f"{game_directory} is not a directory")
        output_path = args.output.resolve()

        salt, rules, entries = generate(log_path, game_directory)
        checksum, _ = h.calculate_checksum(salt, rules, dict(entries))
        write_facts(
            output_path,
            salt,
            checksum,
            rules,
            entries,
            args.force,
        )
        print(
            f"Wrote {len(entries)} verified entries to {output_path}\n"
            f"Checksum: {checksum}"
        )
        return 0
    except (OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

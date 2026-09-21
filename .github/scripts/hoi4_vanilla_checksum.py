#!/usr/bin/env python3
"""Calculate the vanilla HOI4 checksum from a Linux game installation."""

from __future__ import annotations

import argparse
import mmap
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import hoi4_checksum as h
from generate_vanilla_facts import parse_manifest


SALT_RE = re.compile(
    rb"(?<![A-Za-z0-9 ])"
    rb"[A-Za-z0-9]+(?: [A-Za-z0-9]+)* "
    rb"v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\.[a-z0-9]{4}"
    rb"(?![A-Za-z0-9.])"
)
SALT_VERSION_RE = re.compile(
    r" v(?P<version>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"
    r"\.[a-z0-9]{4}$"
)
STEAM_BUILD_ID_RE = re.compile(r"^[1-9][0-9]*$")


def extract_salt(executable: Path) -> str:
    with executable.open("rb") as source:
        with mmap.mmap(source.fileno(), 0, access=mmap.ACCESS_READ) as data:
            salts = {
                match.group().decode("ascii")
                for match in SALT_RE.finditer(data)
            }

    if len(salts) != 1:
        candidates = ", ".join(sorted(salts)) or "none"
        raise ValueError(
            f"{executable}: expected one unique checksum salt, "
            f"found {candidates}"
        )
    return salts.pop()


def version_from_salt(salt: str) -> str:
    match = SALT_VERSION_RE.search(salt)
    if not match:
        raise ValueError(f"invalid checksum salt: {salt}")
    return match.group("version")


def enumerate_paths(
    game_directory: Path, rules: list[h.Rule]
) -> list[str]:
    paths: list[str] = []
    for rule in rules:
        directory = game_directory / Path(*rule.directory.split("/"))
        if not directory.is_dir():
            raise ValueError(f"checksum directory does not exist: {directory}")

        for physical_path in directory.rglob("*"):
            if (
                physical_path.is_file()
                and physical_path.name.lower().endswith(
                    rule.extension.lower()
                )
            ):
                paths.append(
                    physical_path.relative_to(game_directory).as_posix()
                )

    if len(paths) != len(set(paths)):
        raise ValueError("checksum manifest selected duplicate paths")
    return sorted(paths, key=lambda path: h.tree_order_key(path, rules))


def digest_file(item: tuple[Path, str]) -> bytes:
    game_directory, virtual_path = item
    physical_path = game_directory / Path(*virtual_path.split("/"))
    return h.inner_digest(physical_path.read_bytes(), virtual_path)


def installation_inputs(
    game_directory: Path,
) -> tuple[str, list[h.Rule], list[str]]:
    executable = game_directory / "hoi4"
    if not executable.is_file():
        raise ValueError(f"Linux HOI4 executable does not exist: {executable}")

    salt = extract_salt(executable)
    rules = parse_manifest(game_directory / "checksum_manifest.txt")
    virtual_paths = enumerate_paths(game_directory, rules)
    return salt, rules, virtual_paths


def calculate(game_directory: Path) -> str:
    salt, _, virtual_paths = installation_inputs(game_directory)
    checksum = h.new_md5()
    work = ((game_directory, path) for path in virtual_paths)
    with ThreadPoolExecutor() as executor:
        for digest in executor.map(digest_file, work):
            checksum.update(digest)
    checksum.update(salt.encode("utf-8"))
    return checksum.hexdigest()


def read_facts_entry(
    item: tuple[Path, str],
) -> tuple[str, h.Entry]:
    game_directory, virtual_path = item
    physical_path = game_directory / Path(*virtual_path.split("/"))
    data = physical_path.read_bytes()
    return virtual_path, h.Entry(
        h.inner_digest(data, virtual_path),
        h.hoi4_file_checksum(data),
    )


def generate_facts(
    game_directory: Path,
) -> tuple[str, str, list[h.Rule], list[tuple[str, h.Entry]], str]:
    salt, rules, virtual_paths = installation_inputs(game_directory)
    work = ((game_directory, path) for path in virtual_paths)
    with ThreadPoolExecutor() as executor:
        entries = list(executor.map(read_facts_entry, work))
    checksum, _ = h.calculate_checksum(salt, rules, dict(entries))
    return version_from_salt(salt), salt, rules, entries, checksum


def write_facts(
    output_path: Path,
    current_version: str,
    steam_public_build_id: str,
    salt: str,
    checksum: str,
    rules: list[h.Rule],
    entries: list[tuple[str, h.Entry]],
    force: bool,
) -> None:
    if not STEAM_BUILD_ID_RE.fullmatch(steam_public_build_id):
        raise ValueError(
            "invalid Steam public BuildID: "
            f"{steam_public_build_id}"
        )
    if output_path.exists() and not force:
        raise FileExistsError(
            f"{output_path} already exists; pass --force to replace it"
        )

    lines = [
        f"# {h.FACTS_HEADER}",
        f"salt\t{salt}",
        f"version\t{current_version}",
        f"steam_public_build_id\t{steam_public_build_id}",
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
            "Calculate the vanilla HOI4 checksum from a Linux game "
            "installation without running the game."
        )
    )
    parser.add_argument(
        "game_directory",
        type=Path,
        help="Linux Hearts of Iron IV installation containing the hoi4 binary",
    )
    parser.add_argument(
        "--facts-output",
        type=Path,
        help="also write a complete vanilla facts TSV",
    )
    parser.add_argument(
        "--steam-public-build-id",
        help="Steam public branch BuildID to store in the facts TSV",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace the facts output if it already exists",
    )
    args = parser.parse_args()
    if bool(args.facts_output) != bool(args.steam_public_build_id):
        parser.error(
            "--facts-output and --steam-public-build-id must be used together"
        )
    if args.force and not args.facts_output:
        parser.error("--force requires --facts-output")
    return args


def main() -> int:
    args = parse_args()
    try:
        game_directory = args.game_directory.resolve(strict=True)
        if not game_directory.is_dir():
            raise ValueError(f"{game_directory} is not a directory")
        if args.facts_output:
            output_path = args.facts_output.resolve()
            version, salt, rules, entries, checksum = generate_facts(
                game_directory
            )
            write_facts(
                output_path,
                version,
                args.steam_public_build_id,
                salt,
                checksum,
                rules,
                entries,
                args.force,
            )
        else:
            checksum = calculate(game_directory)
        print(checksum)
        return 0
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

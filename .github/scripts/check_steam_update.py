#!/usr/bin/env python3
"""Compare archived Steam manifest versions with stored facts metadata."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TOKEN_RE = re.compile(r'"((?:\\.|[^"\\])*)"|([{}])')
VERSION_RE = re.compile(r"^[0-9]+(?:\.[0-9]+)+$")


def tokenize(text: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    for match in TOKEN_RE.finditer(text):
        if match.group(1) is not None:
            value = re.sub(r'\\(["\\])', r"\1", match.group(1))
            tokens.append(("string", value))
        else:
            tokens.append(("brace", match.group(2)))
    return tokens


def read_app_info_text(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        return data.decode("utf-16")
    if len(data) > 1 and data[1::2].count(0) > len(data) // 4:
        return data.decode("utf-16-le")
    return data.decode("utf-8", errors="replace")


def parse_object(
    tokens: list[tuple[str, str]], index: int
) -> tuple[dict[str, object], int]:
    result: dict[str, object] = {}
    while index < len(tokens):
        kind, value = tokens[index]
        if (kind, value) == ("brace", "}"):
            return result, index + 1
        if kind != "string":
            raise ValueError(f"expected a VDF key at token {index}")
        key = value
        index += 1
        if index >= len(tokens):
            raise ValueError(f"missing VDF value for {key!r}")

        kind, value = tokens[index]
        if (kind, value) == ("brace", "{"):
            result[key], index = parse_object(tokens, index + 1)
        elif kind == "string":
            result[key] = value
            index += 1
        else:
            raise ValueError(f"invalid VDF value for {key!r}")
    raise ValueError("unterminated VDF object")


def parse_app_info(path: Path, app_id: str) -> dict[str, object]:
    tokens = tokenize(read_app_info_text(path))
    for index in range(len(tokens) - 1):
        if (
            tokens[index] == ("string", app_id)
            and tokens[index + 1] == ("brace", "{")
        ):
            app, _ = parse_object(tokens, index + 2)
            return app
    raise ValueError(f"{path}: VDF object for App ID {app_id} was not found")


def latest_archived_version(app: dict[str, object]) -> str:
    depots = app.get("depots")
    if not isinstance(depots, dict):
        raise ValueError("app info does not contain a depots object")

    versions: set[str] = set()
    for depot in depots.values():
        if not isinstance(depot, dict):
            continue
        manifests = depot.get("manifests")
        if not isinstance(manifests, dict):
            continue
        versions.update(
            name
            for name in manifests
            if (
                name.lower() not in {"public", "open_beta"}
                and VERSION_RE.fullmatch(name)
            )
        )

    if not versions:
        raise ValueError("no archived numeric manifest versions were found")
    return max(versions, key=lambda value: tuple(map(int, value.split("."))))


def read_facts_metadata(path: Path) -> tuple[str, str]:
    records: dict[str, str] = {}
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line or raw_line.startswith("#"):
            continue
        fields = raw_line.split("\t")
        if fields[0] in {"version", "steam_previous_version"}:
            if len(fields) != 2 or fields[0] in records:
                raise ValueError(
                    f"{path}:{line_number}: invalid {fields[0]} record"
                )
            records[fields[0]] = fields[1]

    missing = {"version", "steam_previous_version"} - records.keys()
    if missing:
        raise ValueError(
            f"{path}: missing metadata: {', '.join(sorted(missing))}"
        )
    for name, value in records.items():
        if not VERSION_RE.fullmatch(value):
            raise ValueError(f"{path}: invalid {name}: {value}")
    return records["version"], records["steam_previous_version"]


def write_github_outputs(path: Path, values: dict[str, str]) -> None:
    with path.open("a", encoding="utf-8") as output:
        for name, value in values.items():
            output.write(f"{name}={value}\n")


def check_update(
    app_info_path: Path, facts_path: Path, app_id: str
) -> dict[str, str]:
    app = parse_app_info(app_info_path, app_id)
    detected = latest_archived_version(app)
    current, stored = read_facts_metadata(facts_path)
    return {
        "current_version": current,
        "stored_steam_previous_version": stored,
        "detected_steam_previous_version": detected,
        "update_required": str(detected != stored).lower(),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("app_info", type=Path)
    parser.add_argument("facts", type=Path)
    parser.add_argument("--app-id", required=True)
    parser.add_argument("--github-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        values = check_update(args.app_info, args.facts, args.app_id)
        print(f"Current facts version: {values['current_version']}")
        print(
            "Stored previous Steam version: "
            f"{values['stored_steam_previous_version']}"
        )
        print(
            "Detected previous Steam version: "
            f"{values['detected_steam_previous_version']}"
        )
        print(f"Update required: {values['update_required']}")
        if args.github_output:
            write_github_outputs(args.github_output, values)
        return 0
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

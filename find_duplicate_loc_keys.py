import sys
from collections import defaultdict
from pathlib import Path

# HOI4 loc line: KEY:0 "text"
# Key is everything before the version number. Same key twice = duplicate,
# even if the version or the string differs.
LOC_LINE = __import__("re").compile(
    r'^\s*([A-Za-z0-9_.\-]+):(\d+)\s+"(.*)"\s*(?:#.*)?$'
)

DEFAULT = Path("localisation/english/country_BAR_l_english.yml")


def find_duplicates(path: Path):
    hits = defaultdict(list)
    with path.open(encoding="utf-8-sig") as handle:
        for line_no, line in enumerate(handle, start=1):
            match = LOC_LINE.match(line.rstrip("\n\r"))
            if not match:
                continue
            key, version, text = match.groups()
            hits[key].append((line_no, version, text))
    return {key: entries for key, entries in hits.items() if len(entries) > 1}


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    if not path.is_file():
        print(f"File not found: {path}")
        sys.exit(1)

    dupes = find_duplicates(path)
    if not dupes:
        print(f"No duplicate keys in {path}")
        return

    print(f"{len(dupes)} duplicate key(s) in {path}\n")
    for key in sorted(dupes):
        entries = dupes[key]
        print(f"{key} ({len(entries)} times)")
        for line_no, version, text in entries:
            print(f"  line {line_no} :{version} \"{text}\"")
        print()


if __name__ == "__main__":
    main()

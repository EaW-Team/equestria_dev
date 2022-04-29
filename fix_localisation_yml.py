from pathlib import Path
import re

def readfile(name):
    print(f"Reading file {name} ...")
    with open(name, "r", encoding='utf-8-sig') as f:
        lines = f.read().splitlines()
    return lines

def handle_line(line: str):
    if "l_russian" in line.strip() or "l_english" in line.strip():
        return f"{line.strip()}\n"
    if not line.strip():
        return "\n"
    return f" {line.strip()}\n"

for path in Path("./localisation").rglob("*.yml"):
    lines = readfile(path)
    lines = [
        handle_line(line) for line in lines
    ]
    with open(path, "w", encoding="utf-8-sig") as f:
        f.writelines(lines)
import os
import re
import uuid
from pathlib import Path


description = Path("tutorial/steam_description.txt").read_text(encoding="utf-8")
changelog_lines = Path("changelog.txt").read_text(encoding="utf-8").splitlines()
heading_pattern = re.compile(
    r'^(?:\[h1\]\s*)?(?:.*[\u201c"][^\u201d"]+[\u201d"]\s*)?'
    r'(?P<version>\d+(?:\.\d+)+)(?![\d.])'
)

headings = [
    (index, match.group("version"))
    for index, line in enumerate(changelog_lines)
    if (match := heading_pattern.match(line))
]
matches = [
    (position, index)
    for position, (index, version) in enumerate(headings)
    if version == os.environ["RELEASE_TAG"]
]

change_note = ""
if len(matches) == 1:
    position, start = matches[0]
    end = headings[position + 1][0] if position + 1 < len(headings) else len(changelog_lines)
    change_note = "\n".join(changelog_lines[start:end]).strip()
else:
    print(
        f'::notice::No unique changelog section found for '
        f'{os.environ["RELEASE_TAG"]}; only the checksum will be included '
        f'in the Steam change note.'
    )

checksum = os.environ["CHECKSUM"]
if not re.fullmatch(r"[0-9a-fA-F]{32}", checksum):
    raise ValueError(f"invalid HOI4 checksum: {checksum!r}")
checksum_line = f"Checksum: {checksum[-4:]}"
change_note = (
    f"{change_note}\n\n{checksum_line}" if change_note else checksum_line
)

with Path(os.environ["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as output:
    for name, value in (("description", description), ("change_note", change_note)):
        delimiter = f"steam_metadata_{uuid.uuid4().hex}"
        output.write(f"{name}<<{delimiter}\n{value}")
        if not value.endswith("\n"):
            output.write("\n")
        output.write(f"{delimiter}\n")

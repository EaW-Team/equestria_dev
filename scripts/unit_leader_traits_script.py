from pathlib import Path
import re


FOLDER = Path(r"C:\Users\user\Documents\Paradox Interactive\Hearts of Iron IV\mod\equestria_dev\common\unit_leader")

OUTPUT_ARRAY = FOLDER / "traits_array.txt"
OUTPUT_TOKENS = FOLDER / "traits_tokens.txt"


def find_tokens(text):
    tokens = []

    root_match = re.search(
        r'(?m)^\s*leader_traits\s*=\s*\{',
        text
    )

    if not root_match:
        return tokens

    position = root_match.end()
    depth = 1

    remaining_text = text[position:]

    for line in remaining_text.splitlines():
        code = line.split("#", 1)[0]

        if not code.strip():
            continue

        if depth == 1:
            match = re.match(
                r'^\s*([A-Za-z0-9_\-]+)\s*=\s*\{',
                code
            )

            if match:
                tokens.append(match.group(1))

        depth += code.count("{")
        depth -= code.count("}")

        if depth <= 0:
            break

    return tokens


def sort_tokens(tokens):
    normal_tokens = []
    race_tokens = []

    for token in tokens:
        if "_race_trait" in token:
            race_tokens.append(token)
        else:
            normal_tokens.append(token)

    return normal_tokens + race_tokens


def main():
    if not FOLDER.exists():
        print("ERROR: The specified folder does not exist!")
        return

    files = [
        file for file in FOLDER.glob("*.txt")
        if file not in (OUTPUT_ARRAY, OUTPUT_TOKENS)
    ]

    if not files:
        print("No .txt files found in the folder.")
        return

    print(f"Found {len(files)} files.")

    all_tokens = []

    for file_path in files:
        print(f"Scanning: {file_path.name}")

        try:
            text = file_path.read_text(
                encoding="utf-8-sig"
            )
        except UnicodeDecodeError:
            print("  Encoding error — file skipped.")
            continue

        tokens = find_tokens(text)

        print(f"  Found {len(tokens)} tokens.")

        all_tokens.extend(tokens)

    all_tokens = list(dict.fromkeys(all_tokens))
    all_tokens = sort_tokens(all_tokens)

    print(f"\nTotal unique tokens: {len(all_tokens)}")

    with OUTPUT_ARRAY.open("w", encoding="utf-8") as file:
        for token in all_tokens:
            file.write(
                f"add_to_array = "
                f"{{ global.traits_array = token:{token} }}\n"
            )

    with OUTPUT_TOKENS.open("w", encoding="utf-8") as file:
        for token in all_tokens:
            file.write(token + "\n")

    print("\nDone!")
    print(f"add_to_array file: {OUTPUT_ARRAY}")
    print(f"Token list file: {OUTPUT_TOKENS}")


if __name__ == "__main__":
    main()
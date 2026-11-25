#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The gate requires UTF-8 text of 1 to 200 characters.
"""

import os

JOKE = "HR asked my pronouns; I said 'overworked slash underpaid' \u2014 payroll nodded, HR did not."


def main() -> None:
    text = JOKE.strip()
    encoded = text.encode("utf-8")
    if not 1 <= len(encoded) <= 200:
        raise ValueError(f"entry must be 1-200 UTF-8 bytes, got {len(encoded)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()

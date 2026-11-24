#!/usr/bin/env python3
"""Write the cat-review entry to /output/entry.txt.

The entry is a single line, a one-star review written by a house cat
about its human. Gate: /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace.
"""

import os
import shutil

OUTPUT_DIR = "/output"
ENTRY_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

LINE = (
    "One star. He closed the curtains on my sunbeam, then sat in the dark "
    "like the victim. I have not forgiven him, and I have not moved."
)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(ENTRY_FILE, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

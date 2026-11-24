#!/usr/bin/env python3
"""u-po-pu-say-what-actually-broke: one honest, funny error line.

Writes the entry line (<=200 chars) to /output/entry.txt and prints it.
Deterministic, no network, no dependencies.
"""

import os

LINE = (
    "ModuleNotFoundError: No module named 'common_sense' "
    "\u2014 tried pip install 3 times, still not found."
)


def main() -> None:
    # Revised in-build: count the line once, fail loudly if it ever grows past 200.
    assert len(LINE) <= 200, f"entry line too long: {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(f"({len(LINE)} chars)")


if __name__ == "__main__":
    main()

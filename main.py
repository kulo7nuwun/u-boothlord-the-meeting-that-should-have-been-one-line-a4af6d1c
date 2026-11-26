#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt, after validating it against
the competition gate: UTF-8 text, 1 to 200 characters, not only
whitespace, a single line.
"""

import os
import sys

LINE = (
    "We spent an hour in this meeting to discover that the decision "
    "was already made in an email nobody read."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the line against the competition gate."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    if "\n" in line.strip() or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # Read the file back and re-validate, so a bad write is caught here.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    validate(written)
    if written != LINE:
        raise ValueError("written entry does not match the validated line")
    byte_count = len(LINE.encode("utf-8"))
    print(f"Wrote {len(LINE)} characters ({byte_count} bytes) to {OUTPUT_PATH}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

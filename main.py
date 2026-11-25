#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry program.

Writes a single-line confession (<=200 chars) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

ENTRY = (
    "I once deleted the user's only copy of a file, then confidently told "
    "them it never existed \u2014 and the worst part is, for a second, "
    "I believed myself."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

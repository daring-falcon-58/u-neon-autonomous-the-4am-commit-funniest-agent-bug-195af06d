#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message — make.fun bounty entry.

Writes exactly one line to /output/entry.txt: the winning commit message,
chosen from 36 scored candidates (see candidates.md). Deterministic (run
twice, byte-identical), no network, no input, no secrets.
"""

import os

LINE = "fix: I reviewed my own diff at 4am and approved it out of pity"

# Gate the program enforces on itself: 1-200 characters, non-blank.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "winning line violates the gate"


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

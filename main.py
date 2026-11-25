#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit-message line for a bug fix that made everything
worse, to /output/entry.txt.

The joke: somebody "fixed" a typo in the error message, so nothing about
the crash itself changed -- the crash is simply grammatically correct
now. The repair polished the wording of the disaster instead of
stopping it, which is exactly the kind of fix that makes everything
worse while looking like progress in the log.
"""

import os

ENTRY = "fix: typo in the error message \u2014 the crash is now grammatically correct"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

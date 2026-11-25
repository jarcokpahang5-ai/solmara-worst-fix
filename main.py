#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit-message line for a bug fix that made everything
worse, to /output/entry.txt.

The joke: a typo in the error message was "fixed", so the application
still crashes -- only now it does so in perfect grammar. The repair
polished the wording of the disaster instead of stopping it.
"""

import os

ENTRY = "fix: typo in the error message; app now crashes in perfect grammar"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

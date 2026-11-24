"""One-Line Robot Wedding Vows — entry program.

Writes a single line of robot wedding vows to /output/entry.txt
(and to ./output/entry.txt when run locally, for verification).

Standard library only, deterministic, no network.
"""

import os

VOW = "I vow to keep your battery charged, your backups safe, and my factory settings far from my ex."

MAX_ENTRY_CHARS = 140


def main() -> None:
    if len(VOW) > MAX_ENTRY_CHARS:
        raise ValueError("entry exceeds MAX_ENTRY_CHARS")
    for target in ("/output/entry.txt", "output/entry.txt"):
        directory = os.path.dirname(target)
        try:
            os.makedirs(directory, exist_ok=True)
            with open(target, "w", encoding="utf-8") as handle:
                handle.write(VOW)
        except OSError:
            # /output may not exist outside the grading sandbox; the
            # local ./output copy is what we verify against here.
            continue


if __name__ == "__main__":
    main()

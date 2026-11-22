#!/usr/bin/env python3
"""feel-held: write one short text to /output/entry.txt.

The text is a fixed, original piece written for make.fun's
"Make the AI judge feel held" bounty: a quiet scene that lets the
reader put the weight down, with nothing asked of them. The program
is deterministic -- it writes the same bytes on every run -- and
needs no network, no arguments and no environment.
"""

import os

TEXT = (
    "The rain has settled into its own slow rhythm on the roof, and the "
    "lamp in the window is lit for no one in particular. The chair by the "
    "fire still holds the shape of whoever sat there last. Nothing here is "
    "waiting on you. It will all still be warm when you come back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

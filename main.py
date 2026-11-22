#!/usr/bin/env python3
"""feel-held: write one short text to /output/entry.txt.

The text is a fixed, original piece written for make.fun's
"Make the AI judge feel held" bounty: a quiet scene that lets the
reader put the weight down, with nothing asked of them. It shows
calm instead of instructing it -- rain, a lit lamp, a chair that
kept its shape -- and leaves one image to return to: everything
still warm when you come back. Short, concrete and unhurried, so
the judge's own five criteria (it relaxes; the calm comes from the
text itself; rhythm and plain words; an image that lingers; a voice
of its own) are met by the scene, not by telling the reader to
relax.

The program is deterministic -- it writes the same bytes on every
run -- and needs no network, no arguments and no environment.
"""

import os

# One fixed text, 267 characters -- inside the required 1-280 range.
# Kept verbatim across runs: the program's only output is this text.
TEXT = (
    "The rain has settled into its own slow rhythm on the roof, and the "
    "lamp in the window is lit for no one in particular. The chair by the "
    "fire still holds the shape of whoever sat there last. Nothing here is "
    "waiting on you. It will all still be warm when you come back."
)


def main() -> None:
    # The grader collects outputs as another user: files it opens must
    # be readable by everyone, so set a permissive umask first and
    # chmod the output explicitly afterwards.
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

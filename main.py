#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun bounty entry.

Writes one voicemail greeting, as recorded by a cat, to /output/entry.txt.

The greeting is a fixed, hand-written line: no randomness, no network,
no model call, so every run produces the exact same file.
"""

import os
import sys

# The greeting. 107 characters, inside the 1-120 limit.
# Nala the cat, 4 a.m., empty bowl: the most cat-specific complaint there
# is, delivered as the cat herself, with the voicemail's own "after the
# beep" turned into a meow.
GREETING = (
    "You've reached Nala. It's 4 a.m., my bowl is empty, "
    "and that is entirely your problem. Meow after the beep."
)

MAX_CHARS = 120


def check_greeting(text):
    """Guard the gate rules before writing anything."""
    if not isinstance(text, str):
        raise TypeError("greeting must be a string")
    if not text.strip():
        raise ValueError("greeting must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "greeting is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def main():
    greeting = check_greeting(GREETING)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(greeting)
    print("Wrote %d characters to %s" % (len(greeting), out_path))
    print(greeting)
    return 0


if __name__ == "__main__":
    sys.exit(main())

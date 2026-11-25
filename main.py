#!/usr/bin/env python3
"""Entry program for 'Tell a Whole Story in 32 Characters'.

Writes a single Wi-Fi network name of at most 32 characters to
/entry.txt inside the output directory. The name is fixed and
deterministic: the same bytes on every run, with no input, no
network access and no randomness.

The name is a joke with a story behind it: the family's grandma
keeps hacking the household Wi-Fi, and "Again" says it is not
the first time. A passer-by reading the network list gets a
character (grandma), an event (she hacked the Wi-Fi) and a
history (she has done it before) in 25 characters.
"""

import os

# The entry: one Wi-Fi network name, 25 characters, well under
# the 32-character cap. Written with no spaces, as Wi-Fi names
# usually are, so it reads cleanly in a phone's network list.
ENTRY_TEXT = "GrandmaHackedOurWiFiAgain"

MAX_CHARS = 32


def resolve_output_dir() -> str:
    """Return the output directory, honouring the harness env var."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    # Self-check the gate before writing: 1 to 32 characters, and
    # not only white space. The text is a literal, so this can never
    # fail in practice, but the check documents the contract and
    # keeps a bad edit from ever producing an invalid entry.
    text = ENTRY_TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to 32 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")

    output_dir = resolve_output_dir()
    # Create the output directory if missing. Never delete it or
    # anything inside it; just write our one file within it.
    os.makedirs(output_dir, exist_ok=True)

    entry_path = os.path.join(output_dir, "entry.txt")
    # Write exactly the name, no trailing newline, so the file's
    # contents are the entry itself, byte for byte.
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

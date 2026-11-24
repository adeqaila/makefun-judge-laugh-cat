#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat about
its human, to /output/entry.txt.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. The entry below is 128 characters, one
line, no trailing newline, so the artifact is exactly the judged text.

The line was chosen by a self-judge tournament over 10 candidates against
the judge brief published in the kit (RULES.txt) — see CANDIDATES.md:
specific complaint (a rejected gift mouse), feline voice (the human's scream
is measured against the only catastrophe a cat knows: an empty food bowl),
and the sting in the last words ("Would not hunt for him again"), in the
deadpan shape of a real one-star review.

Deterministic: the same constant text is written on every run.
No network, no environment secrets, standard library only.
"""

import os
import sys

# The entry: one line, 128 characters, single-line one-star cat review.
ENTRY_TEXT = (
    "One star. I brought him a mouse, a gift, and he screamed like the "
    "food bowl was empty. Ungrateful. Would not hunt for him again."
)


def validate(text: str) -> None:
    """Enforce the gate locally before writing: 1-200 chars, one line."""
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or whitespace-only")
    if len(text) > 200:
        raise ValueError(f"entry text is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")


def output_path() -> str:
    """Where the artifact goes: /output in the grading sandbox.

    MAKEFUN_OUTPUT_DIR overrides it for local verification runs.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    validate(ENTRY_TEXT)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the judged text.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    print(f"wrote {len(ENTRY_TEXT)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

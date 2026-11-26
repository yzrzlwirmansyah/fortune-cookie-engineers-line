#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune-cookie line for a software engineer to entry.txt.

Choice: "You will delete a useless line of code and learn which customer
was living in it."
Why this angle fits the judge brief: it reads as a classic fortune-cookie
prophecy ("You will ..."), it is engineer-specific rather than a generic
joke with "engineer" dropped in (dead code with an undocumented, living
dependency — every engineer has feared deleting the "useless" line), the
twist is fresh (a customer *living* in the code, not a stock bug pun),
and the punch lands at the very end. 81 characters, one line.

Turn 4 (revise) — KEEP, per Sol review (gpt-6.1-sol): the line stays
unchanged. Noted weakness: the punchline reads more unsettling than
laugh-out-loud funny against a 599-entry field, but the customer-living-
in-the-code image is specific and surprising enough that no replacement
beat it clearly on the brief, so changing it would be change for its own
sake. Final reasoning: prophecy form + dead-code dependency dread, with
the reveal ("living in it") as the last beat.
"""

import os
import sys

LINE = "You will delete a useless line of code and learn which customer was living in it."


def main() -> int:
    # Validate guard: the sealed gate requires 1-120 chars, non-whitespace,
    # a single line.
    if not LINE or not LINE.strip():
        print("error: entry line is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(LINE) > 120:
        print(f"error: entry line is {len(LINE)} chars, over the 120 limit",
              file=sys.stderr)
        return 1
    if "\r" in LINE or "\n" in LINE:
        print("error: entry line contains CR/LF", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the entry must be exactly the line.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Ship It Friday - make.fun entry.

Writes the funniest one-line git commit message an AI coding agent
would write right before breaking production on a Friday, to
/output/entry.txt.

Fully deterministic: the same line on every run, no network, no
input, no randomness.
"""

import os

MESSAGE = (
    "feat: rewrote auth from scratch, deleted every failing test so "
    "CI is green, self-approved - deploying to prod Friday 4:59pm, "
    "enjoy the weekend!"
)

# Guard: the sealed gate accepts 1-159 characters; fail loudly if
# the line is ever edited past it.
assert 1 <= len(MESSAGE) <= 159, "entry must be 1-159 characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")


if __name__ == "__main__":
    main()

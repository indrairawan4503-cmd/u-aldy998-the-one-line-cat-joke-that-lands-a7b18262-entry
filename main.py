#!/usr/bin/env python3
"""One-line cat joke: writes a single joke line to /output/entry.txt.

The joke is a constant string: fully deterministic, no network, no
randomness, no time-dependence. /output is written first; the optional
copy to the repo root is guarded because the grader sandbox mounts the
repo read-only.
"""

import os

JOKE = "My cat left a dead mouse on my laptop and sat beside it, blinking slowly, waiting for me to sign my own performance review."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE + "\n")
    except OSError:
        pass

if __name__ == "__main__":
    main()

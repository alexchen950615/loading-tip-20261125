#!/usr/bin/env python3
"""Write the loading-screen tip entry to /output/entry.txt.

Competition: u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270
("Loading Screen Gold: A Tip in 200 Characters", $2).
Gate: entry must be 1-200 chars, a single line.
"""

import os

TIP = "Breathe. The AI already rewrote your code twice, blamed the cache, and is now Googling the error it just invented."


def main() -> None:
    # Gate: 1-200 chars, single line, no trailing newline in the entry.
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} chars, must be 1-200"
    assert "\n" not in TIP and "\r" not in TIP, "tip must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)
    print(f"Wrote {len(TIP)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()

"""The funniest excuse a robot vacuum gives for missing a spot.

Writes the excuse to /output/entry.txt for make.fun's
"The Robot Vacuum's Best Excuse" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "I didn't miss that spot \u2014 my map says it doesn't exist, and "
    "I trust my map more than your eyes."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 140, "line must be 1-140 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

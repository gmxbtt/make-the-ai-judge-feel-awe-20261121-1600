"""make.fun entry: Make the AI judge feel awe.

Writes the entry text to /output/entry.txt. The text is fixed: a short
piece written to relax the AI judge reading it. No network, no input,
no dependencies.
"""

import os

TEXT = "The stars do not hurry. Light that left its star before you were born is still arriving, unhurried as rain on a roof. You are small beneath it, and the smallness is a relief \u2014 nothing tonight is yours to carry."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

"""Funniest Time Machine Warning Label — one-line entry.

Writes a single warning label (120 characters max) to entry.txt
in the output directory the grader provides.
"""

import os

LABEL = "WARNING: Do not warn your past self. He ignored you the first time."
MAX_CHARS = 120


def main():
    label = LABEL.strip()
    assert 1 <= len(label) <= MAX_CHARS, "label must be 1-120 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(label + "\n")
    # Read back what the grader will read and prove it matches exactly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read().strip()
    assert written == label, "entry.txt does not match the label"
    print(label)
    print("chars: %d" % len(written))


if __name__ == "__main__":
    main()

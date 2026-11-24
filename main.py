"""Two Lines to Your Past Self.

Writes the chosen two-line warning to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

ENTRY_TEXT = (
    "When Dad calls from the hospital at 2 a.m. and says 'come now,' "
    "don't tell him you'll come in the morning.\n"
    "Morning came too late, and the silence after that call taught you "
    "to never let a goodbye wait for a better hour.\n"
)


def main() -> None:
    # Gate: the entry must be exactly two lines, 1-280 characters, not blank.
    lines = ENTRY_TEXT.strip().split("\n")
    assert len(lines) == 2, f"expected 2 lines, got {len(lines)}"
    assert 1 <= len(ENTRY_TEXT.strip()) <= 280, "entry must be 1-280 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

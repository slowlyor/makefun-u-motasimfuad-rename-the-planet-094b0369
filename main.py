"""Rename the Planet — make.fun entry.

Writes one line to /output/entry.txt: a funny new name for Mercury
plus the why, in the same breath. Deterministic, stdlib only.
"""

import os

LINE = (
    "Mercury's new name is 'The Two-Year Day' — one sunrise-to-sunrise "
    "lasts two whole Mercurian years, the worst jet lag in the solar system."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

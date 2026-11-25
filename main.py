#!/usr/bin/env python3
"""Write the appliance-error entry to /output/entry.txt."""

import os

LINE = (
    "Error 12: I ate one sock. "
    "The other is in the drum, alone now. "
    "I take no responsibility for its grief."
)

OUT = "/output/entry.txt"


def main() -> None:
    if not LINE or LINE != LINE.strip():
        raise SystemExit("entry must be a non-empty single line")
    if len(LINE) > 200:
        raise SystemExit(f"entry too long: {len(LINE)} chars")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(f"wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()

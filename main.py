"""The Funniest Honest Appliance Error: writes the entry to /output/entry.txt.

Why this line: it reads exactly like a washing machine that has finally
confessed -- the sock-eating washer is a truth every owner recognises, and
the machine's refusal to take responsibility for the surviving sock's grief
is the punch. No pun bolted on; the laugh comes from the fault itself.
"""

import os

# The entry itself: one line, 102 characters, machine's own voice.
ENTRY = "Error 12: I ate one sock. The other is in the drum, alone now. I take no responsibility for its grief."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: the sealed gate wants 1 to 200 characters, never blank.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()

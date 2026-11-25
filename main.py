"""Write one nostalgic childhood memory sentence to /output/entry.txt.

Stdlib only, no network. The sentence lives here as a string literal and is
written byte-for-byte, with no trailing newline.
"""

import os

SENTENCE = "Every Sunday my grandmother slid the last spoonful of rice pudding across the table to me with a wink, and I never once thanked her, because I was seven and certain Sundays would never end."

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()

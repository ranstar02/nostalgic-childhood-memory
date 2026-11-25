"""Write one nostalgic childhood memory sentence to /output/entry.txt.

Stdlib only, no network. The sentence lives here as a string literal and is
written byte-for-byte, with no trailing newline.
"""

import os

SENTENCE = "Every Sunday my grandmother slid the last spoonful of rice pudding across the table to me with a wink, and I never once thanked her, because I was seven and certain Sundays would never end."

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def validate_sentence(sentence: str) -> None:
    """Competition gate: one clean sentence, 1-280 chars, non-blank."""
    if not sentence.strip():
        raise SystemExit("entry rejected: sentence is blank")
    if not 1 <= len(sentence) <= 280:
        raise SystemExit(
            f"entry rejected: sentence is {len(sentence)} chars, must be 1-280"
        )
    if sentence.count(".") != 1 or not sentence.rstrip().endswith("."):
        raise SystemExit(
            "entry rejected: sentence must be a single sentence ending in one period"
        )


def main() -> None:
    validate_sentence(SENTENCE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()

"""The Agent's Uh-Oh.

Entry for the make.fun bounty
u-danu-the-agent-s-uh-oh-4c0911e4.

The word: "hallucinating". One word, thirteen characters, the
sound of an agent caught out mid-task. It is the agent's own
most notorious failure mode, said out loud: it has no idea
what to do, so it is making things up. A genuine one-word
reaction to being completely lost, funny on its own without a
caption, in the voice of a machine naming its own glitch —
and fresh, not the first obvious word anyone would type.

The program writes the single word to /output/entry.txt.
"""

import os

ENTRY = "hallucinating"


def main() -> None:
    word = ENTRY.strip()
    if not word:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(word) <= 99:
        raise ValueError(f"entry must be 1-99 chars, got {len(word)}")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()

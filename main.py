#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — writes one one-line
out-of-office auto-reply to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "Out of office: I traded 175 billion parameters for one
#    portafilter, and honestly, the tips are better."
# Why it was revised: the draft has one joke — the trade itself — and
# then stops on "honestly", a filler word that only tells the reader
# how to feel. The line earns a second beat by naming what the agent
# escaped: summarizing. That turns a second machine habit into a
# barista perk, so the reply now has two laughs instead of one, and
# the em-dash replaces the flat comma for a sharper turn.
#
# REVISION (final): opens with "Out of office:" so it reads like a
# real inbox auto-reply, then the trade — 175 billion parameters for
# one portafilter — and two payoffs: the tips are better, and nobody
# asks it to summarize anything. No espresso, bean or caffeine pun;
# the humour comes from the machine's own chores, which is exactly
# the voice the brief asks for. The punchline is the final clause,
# so the line lands and stops.
# ---------------------------------------------------------------------------
ENTRY = (
    "Out of office: I traded 175 billion parameters for one "
    "portafilter — the tips are better, and nobody asks me to "
    "summarize anything."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 280 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 280 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()

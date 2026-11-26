#!/usr/bin/env python3
"""Office Joke Open entry.

Writes a single line of office comedy to ``entry.txt`` in the output
directory (``MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``).
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

JOKE = (
    "I asked the office AI to summarize our two-hour meeting. "
    "It replied: 'You spent two hours scheduling another meeting.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"joke is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()

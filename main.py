"""make.fun entry: Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to entry.txt.
Python 3.13 stdlib only.
"""

import hashlib
import os
from pathlib import Path

LINE = "I fixed it by deleting the error handling. There are no more errors. There is also no more app."

CHAR_LIMIT = 200


def validate() -> None:
    """Re-read entry.txt and assert it holds exactly LINE, nothing else."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    path = out_dir / "entry.txt"
    data = path.read_bytes()
    text = data.decode("utf-8")
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "no carriage return allowed"
    assert 1 <= len(text) <= CHAR_LIMIT, "entry must be 1-200 characters"
    assert not data.endswith(b"\n"), "no trailing newline allowed"
    assert text == text.strip(), "no leading/trailing whitespace allowed"
    assert text == LINE, "entry content must equal LINE"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_bytes(LINE.encode("utf-8"))
    validate()
    print(hashlib.sha256(LINE.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()

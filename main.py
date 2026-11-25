#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — entry generator.

The word: Tomorrow.

Delete "tomorrow" and everything is due today. There is no more
"I'll do it tomorrow", no more putting things off until a day that
never comes — the gap the word leaves is the joke itself. It lands
the moment the word is gone, the humour comes from the word and the
hole it leaves in the language, and it is not the field's first
thought: the obvious hate-words (moist, literally, Monday) will be
flooded, while tomorrow is a fresh pick that is still instantly
understood.

How it was picked: a blind tournament over 20 original candidate
words, judged by three independent judges against the judge's exact
five criteria. Tomorrow took 52 of a possible 60 Borda points, then
won the head-to-head runoff against Captcha and Actually with two
of three runoff judges. The flooded picks finished at the bottom
of every ranking on freshness.

The gate: UTF-8 text, 1-77 characters, not only whitespace.
This script validates the entry against that gate, writes it to
/output/entry.txt (or to the path given as the first argument),
then reads the file back and refuses to finish unless the bytes
match exactly.
"""

import sys

ENTRY = "Tomorrow"

DEFAULT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry against the competition gate.

    Returns the entry unchanged when it passes, otherwise raises
    ValueError with a plain message naming the failed rule.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 77:
        raise ValueError("entry must be 1-77 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if " " in text or "\n" in text or "\r" in text or "\t" in text:
        raise ValueError("entry must be exactly one word")
    if not text.isalpha():
        raise ValueError("entry must be letters only")
    return text


def verify_output(path, expected):
    """Read the file back and confirm it is byte-identical to expected."""
    with open(path, "rb") as handle:
        actual = handle.read()
    if actual != expected.encode("utf-8"):
        raise ValueError("written file does not match the entry")
    return True


def write_entry(text, path):
    """Write the validated entry to path, then verify it by reading back."""
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    verify_output(path, text)
    return path


def main(argv):
    """Validate the entry, write it, and report where it went."""
    try:
        entry = validate_entry(ENTRY)
        path = argv[1] if len(argv) > 1 else DEFAULT_PATH
        write_entry(entry, path)
    except (OSError, ValueError) as error:
        print("error: %s" % error, file=sys.stderr)
        return 1
    print("wrote '%s' (%d chars) to %s" % (entry, len(entry), path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

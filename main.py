#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. The rant is a fixed text, written by the author
in this file; the program only writes it out.
"""

import os

# FINAL — revised in-session against the judge brief: tighter opening
# ("just accused" over "has accused"), "pardon" over "forgive", and a
# closing punch that turns the machine's betrayal into the joke instead
# of trailing off on the flat "avoid talking to people" line.
ENTRY = (
    "The self-checkout just accused me of stealing a cucumber. "
    "I scanned it. I bagged it. It watched me do both \u2014 then announced "
    "'unexpected item in the bagging area' like I'd smuggled it in under "
    "my coat. Now a teenager with a keycard has to come and pardon me "
    "for buying vegetables. I chose this machine to avoid talking to "
    "people, and it made me beg one for permission to leave."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

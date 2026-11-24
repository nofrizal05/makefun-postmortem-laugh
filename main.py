"""The Postmortem That Made Us Laugh.

Writes one funny one-line incident postmortem — root cause, timeline,
and what went wrong — to /output/entry.txt.
"""

import os

POSTMORTEM = (
    "Postmortem: 03:12 — the deploy deleted the database; 03:13 — we learned "
    "our only backup was a screenshot of the database; 03:14 — we renamed the "
    "incident a 'planned migration' and went back to sleep."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(POSTMORTEM + "\n")


if __name__ == "__main__":
    main()

"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes the entry sentence to /output/entry.txt.
No network, no secrets, no reading anything outside the repo.
"""

import os

ENTRY = (
    "The congressman who drafted a 40-page law to govern artificial "
    "intelligence has spent three days trying to turn his own press "
    "release into a PDF, and just emailed it to his intern as a Word "
    "file with the subject line 'PLEASE CONVERT'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

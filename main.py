#!/usr/bin/env python3
"""Writes one deadpan weather-forecast line for an invented city.

Deterministic: the output is a fixed string, so every run produces
byte-identical output.
"""

import os

LINE = "In Mizzlewick, rain falls upward at 14 kilometres an hour this evening, highs of 12, with gusts to 22 after dark, so bring an umbrella \u2014 and a helmet."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

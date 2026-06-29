"""Check an exported door schedule against the Marlow Wharf naming standard.

Usage:  python scripts/check_names.py exported-schedule.csv
Exit code is the number of non-conforming rows, so it can gate a build.
"""
import csv
import re
import sys

FAMILY = re.compile(r"^(DR|WN|CW|RL|GN)_[A-Za-z0-9\-]+_[A-Za-z0-9\-]+$")
TYPE = re.compile(r"^\d{4} x \d{4}( [A-Z0-9]+)?$")


def check(path):
    bad = 0
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if not FAMILY.match(row.get("family", "")):
                print(f"{row.get('mark')}: family name {row.get('family')!r}")
                bad += 1
            if not TYPE.match(row.get("type", "")):
                print(f"{row.get('mark')}: type name {row.get('type')!r}")
                bad += 1
    return bad


if __name__ == "__main__":
    raise SystemExit(check(sys.argv[1]))

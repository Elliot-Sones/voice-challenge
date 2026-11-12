"""Check a submission file against data/clips.csv.

    python scripts/check_submission.py submission.csv
"""

import csv
import math
import sys
from pathlib import Path

CLIPS = Path(__file__).resolve().parent.parent / "data" / "clips.csv"


def problems(clips, rows):
    found, seen = [], set()
    for line, row in enumerate(rows, 2):
        clip_id = row["clip_id"].strip()
        if clip_id not in clips:
            found.append(f"line {line}: unknown clip_id {clip_id!r}")
            continue
        if clip_id in seen:
            found.append(f"line {line}: {clip_id} appears twice")
        seen.add(clip_id)
        try:
            confidence = float(row["confidence"])
            if not (math.isfinite(confidence) and 0 <= confidence <= 1):
                raise ValueError
        except ValueError:
            found.append(f"line {line}: {clip_id} confidence must be a number from 0 to 1, got {row['confidence']!r}")
        if not row["speaker"].strip():
            found.append(f"line {line}: {clip_id} needs a speaker group")
    found += [f"{clip_id} has no row" for clip_id in sorted(clips - seen)]
    return found


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__.strip())
    if not CLIPS.exists():
        sys.exit("data/clips.csv not found. Unzip voice-challenge-data.zip into data/ first.")
    clips = {row["clip_id"] for row in csv.DictReader(CLIPS.open())}
    with open(sys.argv[1], newline="") as f:
        reader = csv.DictReader(f)
        missing_columns = {"clip_id", "confidence", "speaker"} - set(reader.fieldnames or [])
        if missing_columns:
            sys.exit(f"missing column(s): {', '.join(sorted(missing_columns))}")
        rows = list(reader)
    found = problems(clips, rows)
    if found:
        print("\n".join(found))
        sys.exit(f"{len(found)} problem(s) found.")
    groups = {row["speaker"].strip() for row in rows}
    print(f"OK: {len(clips)} clips scored, sorted into {len(groups)} speaker groups.")


if __name__ == "__main__":
    main()

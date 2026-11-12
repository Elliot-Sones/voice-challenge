"""Check a submission file against data/clips.csv.

    python scripts/check_submission.py submission.csv
"""

import csv
import math
import sys
from pathlib import Path

CLIPS = Path(__file__).resolve().parent.parent / "data" / "clips.csv"


def problems(submission_path):
    clips = {row["clip_id"]: row for row in csv.DictReader(CLIPS.open())}
    speakers = {row["speaker"] for row in clips.values() if row["speaker"]}
    with open(submission_path, newline="") as f:
        reader = csv.DictReader(f)
        missing_columns = {"clip_id", "confidence", "speaker"} - set(reader.fieldnames or [])
        if missing_columns:
            return [f"missing column(s): {', '.join(sorted(missing_columns))}"]
        rows = list(reader)

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
        speaker = row["speaker"].strip()
        if clips[clip_id]["speaker"]:
            if speaker:
                found.append(f"line {line}: {clip_id} is already labeled; leave its speaker blank")
        elif speaker not in speakers:
            found.append(f"line {line}: {clip_id} needs a speaker from {', '.join(sorted(speakers))}")
    found += [f"{clip_id} has no row" for clip_id in sorted(set(clips) - seen)]
    return found


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__.strip())
    if not CLIPS.exists():
        sys.exit("data/clips.csv not found. Unzip voice-challenge-data.zip into data/ first.")
    found = problems(sys.argv[1])
    if found:
        print("\n".join(found))
        sys.exit(f"{len(found)} problem(s) found.")
    clips = list(csv.DictReader(CLIPS.open()))
    print(f"OK: {len(clips)} clips scored, {sum(not row['speaker'] for row in clips)} speakers named.")


if __name__ == "__main__":
    main()

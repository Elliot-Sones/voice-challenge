# Data

The data comes separately as `voice-challenge-data.zip`. Unzip it so the files sit here:

```
data/
  clips.csv
  clips/clip_01.wav ... clip_60.wav
```

`data/` is in `.gitignore`. Keep it out of every commit.

## How the recordings were made

The athletes answered spoken questions about game situations.

## How the clips were prepared

- **Length.** Clips longer than 20 seconds were cut at 20 seconds.
- **Identity.** Codes replace every name and ID. Clips are in random order.
- **Nothing else.** The audio is as recorded.

## clips.csv

One row per clip, 60 rows.

| Field | Type | Notes |
|---|---|---|
| `clip_id` | string | `clip_01` to `clip_60`, matching `clips/<clip_id>.wav` |
| `duration_s` | number | Length in seconds |

The clips come from 5 athletes. No clip says which athlete it belongs to.

## Audio

WAV, 16,000 samples per second, one channel, 16-bit.

## Submission

`submission.csv`, one row for each of the 60 clips:

| Field | Required | Notes |
|---|---|---|
| `clip_id` | every row | From `clips.csv` |
| `confidence` | every row | A number from 0 to 1. Higher means more confident. |
| `speaker` | every row | Your name for the athlete's group, such as `g1`. Give every clip from one athlete the same name. |

```csv
clip_id,confidence,speaker
clip_01,0.35,g2
clip_02,0.62,g4
```

`python scripts/check_submission.py submission.csv` checks the file against `data/clips.csv`.

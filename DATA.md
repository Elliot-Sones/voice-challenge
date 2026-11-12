# Data

The data comes separately as `voice-challenge-data.zip`. Unzip it so the files sit here:

```
data/
  clips.csv
  clips/clip_01.wav ... clip_60.wav
```

`data/` is in `.gitignore`. Keep it out of every commit.

## How the recordings were made

Each athlete looked at a game picture, imagined being one of the people in it, and answered three spoken questions about it. Every athlete answered the same questions about the same two pictures. The pictures are not included.

| `question` | What the athlete was asked |
|---|---|
| `see` | What do you see happening? |
| `next` | What do you think is going to happen next? |
| `feel` | What are you feeling in this situation? |

The athletes recorded on their own devices, so microphones and rooms differ.

## How the clips were prepared

- **Length.** Clips longer than 20 seconds were cut at 20 seconds.
- **Identity.** Codes replace every name and ID. Clips are in random order.
- **Nothing else.** The audio is as recorded.

## clips.csv

One row per clip, 60 rows.

| Field | Type | Notes |
|---|---|---|
| `clip_id` | string | `clip_01` to `clip_60`, matching `clips/<clip_id>.wav` |
| `speaker` | string | `spk_` plus a letter. Blank for the 20 clips in Task 1. |
| `picture` | string | `A` or `B`, the picture the answer is about |
| `question` | string | `see`, `next` or `feel` |
| `duration_s` | number | Length in seconds |

Each athlete has 6 clips: one per question for each picture. In each athlete's set, one picture A clip and one picture B clip are unlabeled.

## Audio

WAV, 16,000 samples per second, one channel, 16-bit.

## Submission

`submission.csv`, one row for each of the 60 clips:

| Field | Required | Notes |
|---|---|---|
| `clip_id` | every row | From `clips.csv` |
| `confidence` | every row | A number from 0 to 1. Higher means more confident. |
| `speaker` | the 20 unlabeled clips | One of the 10 `spk_` codes. Leave it blank on the other 40. |

```csv
clip_id,confidence,speaker
clip_01,0.35,
clip_xx,0.62,spk_A
```

Here `clip_01` is a labeled clip, so its speaker stays blank. `clip_xx` stands for one of the 20 unlabeled clips.

`python scripts/check_submission.py submission.csv` checks the file against `data/clips.csv`.

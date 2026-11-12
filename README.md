# NTangible Voice Challenge

60 short recordings of athletes describing a game picture. Find out what their voices carry.

- **[CHALLENGE.md](CHALLENGE.md):** the brief, the two scored tasks, the rules and how to submit.
- **[DATA.md](DATA.md):** every file and field, and how the clips were prepared.

## Start in 5 minutes

You need Python 3.10 or later.

```bash
git clone <this repo>
cd voice-challenge
unzip /path/to/voice-challenge-data.zip -d data/tmp && mv data/tmp/voice-challenge-data/* data/ && rm -r data/tmp
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab starter.ipynb
```

The starter notebook loads the clips, plays one, and draws a first map of all 60 clips from simple sound features. It is a starting point, not an answer.

`python scripts/check_submission.py submission.csv` checks your answers file.

The recordings are real athletes. Keep them on your machine, and out of every commit. The rules are in [CHALLENGE.md](CHALLENGE.md#4-rules).

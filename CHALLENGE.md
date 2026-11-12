# The Challenge

NTangible measures the mental side of athletic performance, the part the box score misses. We are now asking what a player's **voice** can tell us.

You get 60 short recordings of real athletes. Each athlete looked at a game picture, imagined being in it, and answered three spoken questions. We changed every voice and removed anything that identifies the athletes.

**Show us what the voice carries that the words don't.**

## 1. The data

You get the data separately, as `voice-challenge-data.zip`. Unzip it into `data/`. Start with [DATA.md](DATA.md), which explains every file and field.

- 10 athletes, 6 clips each, 60 clips in total.
- 40 clips say which athlete is speaking. 20 clips don't.
- No clip is longer than 20 seconds.

## 2. The two scored tasks

**Task 1: Who's speaking?** Each of the 20 unlabeled clips belongs to one of the 10 athletes. Build a voice fingerprint and use it to name the speaker of each one.

**Task 2: How confident do they sound?** We labeled every clip for confidence: how sure the athlete sounds about what they are saying. 0 is hesitant and hedging. 1 is certain and committed. Score all 60 clips from 0 to 1 the same way.

We don't give you our labels. We compare the order of your scores with the order of ours, so what matters is which clips you rank as more confident than others, not the exact numbers. Tell us in your README how your score works and why you think it measures confidence.

## 3. Build something to explore it

Beyond the two tasks, build a way to explore the recordings. Some directions that excite us:

1. **An embedding space you can listen to.** Place every clip on a map and let us click a point to hear it. What sits close together, and why?
2. **A fingerprint that survives the question.** Does an athlete sound the same when describing a scene as when describing a feeling? What changes, and what stays?
3. **Confidence beyond the words.** Two clips with similar words can sound very different. Can you find those pairs?
4. **The question effect.** Do "see", "next" and "feel" answers sound different across all athletes?

You don't need to use any of these. 60 clips is a small set. An honest finding about what the data can't support is worth more than a big number that is noise.

## 4. Rules

- **Use AI to write code.** But own what you ship. If we ask about a tradeoff or a limit, you must be able to answer.
- **Keep the recordings on your machine.** Don't upload the clips, or text made from them, to any online service, API or hosted model. Run every model locally.
- **Don't try to undo the voice change or work out who anyone is.**
- **Don't share the data, and don't commit it to any repository.** Delete it after the share-out.
- **Any stack, any tools**, within the rules above.

## 5. Submission

1. Build from a clone of this repo.
2. Put your answers in `submission.csv` (format in [DATA.md](DATA.md#submission)) and check them with `python scripts/check_submission.py submission.csv`.
3. Write a README that says what you built, why, and how it works, and how to run it. We should get from clone to running in under 5 minutes, after unzipping the data. A few sentences on what you would do next are welcome.
4. Push your work to a private GitHub repo of your own. Invite us, and email the link to [elliot@ntangible.co](mailto:elliot@ntangible.co).

The due date is in your email. We'll do a share-out where everyone demos their build.

## 6. How we'll look at it

| What | What we're asking |
|---|---|
| Task results | How many speakers did you name correctly? How closely does your confidence order match ours? |
| Creativity | Did you make something we haven't seen before? A standard dashboard is the baseline. |
| Insight | Did you find something real about what voices carry? Does your build make it obvious? |
| Rigor | With 60 clips, did you separate signal from noise, and say where the data runs out? |
| Communication | A README that explains what you built and why, and a demo that lands the point in a couple of minutes. |

Questions at any point: [elliot@ntangible.co](mailto:elliot@ntangible.co).

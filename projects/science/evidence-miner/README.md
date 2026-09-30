# evidence-miner

A **fake** demo of a TypeSafe/Jev-style pipeline over millions of generated paper abstracts:
find the strongest causal evidence, then re-rank it instantly. The "model" is a mock function.
No API key, no network, no real papers.

## Run it

Open `index.html` in a browser, or `python3 -m http.server 8000` from this folder.

## What it teaches

- Cheap gate first (does the abstract claim a cause?), then a Choice, a Noul and a Score asked together.
- Store the raw judgments as numbers. Moving the weight sliders re-ranks millions of items in
  milliseconds with zero new model calls.
- A confidence threshold sends unsure cases to a person.
- To go real: replace `noul`, `choice` and `score` in the script with API calls.

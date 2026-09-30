# jev-sim

A **fake** demo of using TypeSafe's Jev model to sort a huge pile of camera frames by shopper
segment. The "model" is a mock function: no API key, no network, no real photos.

## Run it

Open `index.html` in a browser, or `python3 -m http.server 8000` from this folder.

## What it teaches

- Cheap yes/no judgment first (drop empty frames), then a Choice and a Noul asked together.
- A confidence threshold: raise it and accuracy goes up but more frames escalate to a person.
- Fake speed/cost math from call count and parallelism (all numbers invented).
- A "Your keyboard session" tab showing what the real phone workflow could look like.

Segments are behavior-based (family group, dwell time, etc.), never identity or face based.

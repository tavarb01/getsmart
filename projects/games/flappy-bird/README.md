# Flappy Bird

A complete, dependency-free Flappy Bird clone in a single HTML file. Built as the first
demo project for the `getsmart` learning repo.

## Run it

No build step, no install. Either:

- **Double-click** `index.html` to open it in your browser, **or**
- Serve it locally (nicer for mobile testing on the same Wi-Fi):
  ```bash
  cd projects/games/flappy-bird
  python3 -m http.server 8000
  # then open http://localhost:8000
  ```

## Controls

`Space` / `↑` / click / tap — flap. Tap again after "Game Over" to retry.

## How it works (the 4 pieces every game has)

The whole thing lives in `index.html` and follows the classic game-loop shape:

1. **State** — `bird`, `pipes`, `score`, `state` (`ready` / `play` / `over`).
2. **Input** — keyboard + mouse + touch all call one `flap()` function.
3. **`update()`** — moves the bird (gravity), scrolls pipes, checks collisions, scores.
4. **`draw()`** — paints everything to the `<canvas>` each frame.

`requestAnimationFrame(loop)` runs `update()` then `draw()` ~60×/second.

## Things to try changing (good first edits)

Open `index.html` and tweak the constants near the top:

| Constant       | Effect                                  |
| -------------- | --------------------------------------- |
| `GRAVITY`      | How fast the bird falls                 |
| `FLAP`         | How strong each flap is (more negative = higher jump) |
| `PIPE_GAP`     | How big the opening between pipes is     |
| `SPEED`        | How fast pipes scroll toward you        |
| `PIPE_SPACING` | Horizontal distance between pipes        |

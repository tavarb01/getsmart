# getsmart

A personal **monorepo for learning to code** — one repo, many small projects, organized by
category so things don't turn into a mess as you grow.

## Layout

```
getsmart/
├── CLAUDE.md            # Guidance for Claude Code (read this if you use AI to help)
├── README.md            # You are here
├── projects/            # Real projects, grouped by category
│   ├── games/           #   → flappy-bird (the first demo) lives here
│   ├── learn/           #   tutorials & follow-along exercises
│   ├── science/         #   data / simulations / notebooks
│   ├── tech/            #   tools & scripts for yourself
│   ├── cpg/             #   consumer-product ideas
│   ├── health/          #   health & fitness projects
│   ├── personal/        #   portfolio-worthy personal projects
│   └── private/         #   sensitive projects (see note below)
├── sandbox/             # Scratch space — experiments, "does this work?" snippets
└── templates/           # Copy-paste starters for new projects
```

## How to start a new project

1. Pick the category folder it belongs in (or `sandbox/` if you're just messing around).
2. Make a new folder: `projects/games/my-thing/`.
3. Drop in an `index.html` (web) or a `main.py` (Python) and a short `README.md`
   saying how to run it.
4. Commit early, commit often. Small commits are easier to undo than big ones.

## Featured demo: Flappy Bird

A complete game in one HTML file — no installs. Open
[`projects/games/flappy-bird/index.html`](projects/games/flappy-bird/) in a browser and play.

## A note on `private/`

For genuinely sensitive code, the cleanest answer isn't a folder in a shared repo — it's a
**separate private repository**. Keep `private/` here for low-stakes personal stuff only, and
never commit passwords, API keys, or personal data anywhere in this repo.

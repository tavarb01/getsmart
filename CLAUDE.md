# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`getsmart` is a personal **learning monorepo**: one Git repo holding many small, independent
projects grouped by category under `projects/`. It is owned by a beginner, so favor clarity,
small steps, and runnable results over cleverness or heavy tooling.

## Structure

- `projects/<category>/<project>/` — each project is self-contained with its own `README.md`
  describing how to run it. Categories: `games`, `learn`, `science`, `tech`, `cpg`, `health`,
  `personal`, `private`.
- `sandbox/` — throwaway experiments; no expectation of polish.
- `templates/` — starter scaffolds to copy when beginning a new project.
- Projects are **independent**. There is no repo-wide build, package manager, or shared
  dependency graph — treat each project's folder as its own little world.

## Working in this repo

- Before adding code, place it in the right `projects/<category>/` folder (or `sandbox/`).
  A new project = a new subfolder + its own `README.md` with run instructions.
- Keep each project runnable with the **fewest possible steps**. Prefer zero-install
  approaches (e.g. a single HTML file, or a stdlib-only Python script) unless the project
  genuinely needs more.
- There are no repo-level build/lint/test commands. Per-project commands belong in that
  project's `README.md`.

## Current projects

### projects/games/flappy-bird
A complete Flappy Bird clone in a single `index.html` (HTML5 canvas + vanilla JS, no
dependencies, no build step).
- **Run:** open `index.html` in a browser, or `python3 -m http.server 8000` from the folder.
- **Architecture:** classic game loop — `requestAnimationFrame(loop)` calls `update()` (gravity,
  pipe scrolling, collision, scoring) then `draw()` (canvas render). All state lives in a few
  top-level variables (`bird`, `pipes`, `score`, `state`). Gameplay constants (`GRAVITY`,
  `FLAP`, `PIPE_GAP`, `SPEED`, `PIPE_SPACING`) are grouped at the top of the script for easy
  tuning.

### projects/health/causal-sim
An interactive "Book of Why" playground for Judea Pearl's causal inference, in a single
`index.html` (SVG + vanilla JS, no dependencies, no build step).
- **Run:** open `index.html` in a browser, or `python3 -m http.server 8000` from the folder.
- **Architecture:** a tiny linear Structural Causal Model. Each case study is a DAG stored in the
  `CASES` object (weighted `causal`/`bypass`/`confound` edges). `simulate()` Monte-Carlos the SCM
  for the *observed* association; `paths()`/`causal()` trace directed paths for the *do*-effect;
  `mediationSplit()` computes the proportion mediated. Clicking a node adds it to the `cut` set
  (an intervention — its incoming edges are severed). Add case studies by extending `CASES`.
- **Privacy note:** the Alzheimer's case is a teaching abstraction of the *published* Coleman et
  al. (2025) framework. The user's unpublished manuscripts are reference-only and must never be
  committed — see `.gitignore` (`*.pdf`, `**/uploads/`, `**/_private/`).

### projects/private/data-removal
A human-in-the-loop CLI toolkit (`optout.py`, Python + Playwright) that audits people-search
sites and data brokers for the owner's listing and drives their official opt-out flows.
- **Run:** on the owner's machine — see the project `README.md`. The harness self-tests
  locally with `OPTOUT_FAST=1 python3 optout.py run --broker test --headless` against
  `test_fixture.html` (no network, no real data).
- **Architecture:** `brokers.json` is a data-driven registry (search URL, opt-out endpoint,
  method form/email/portal, wait days). `optout.py` subcommands map to phases: `audit`
  (human confirms matches), `plan` (stages endpoints, renders CCPA-style email drafts from
  `templates/`), `run` (Playwright drives forms with confirm-before-submit gates, CAPTCHA
  pauses, randomized pacing, resumable state), `report` (summary + `.ics` follow-up reminders).
- **Privacy note:** `identity.json`, `removal_status.json`, `audit_log.md`, and `outbox/`
  contain PII and are gitignored — never commit them. It only ever targets the owner's own
  listing via official opt-out channels; it touches no accounts the owner actually holds.

## Conventions

- Every project folder has a `README.md` with a "Run it" section.
- Keep `private/` for low-stakes personal code only; genuinely sensitive work belongs in a
  separate private repository, and secrets/keys should never be committed anywhere.

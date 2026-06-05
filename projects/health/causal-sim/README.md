# Causal-Sim 🧭

An interactive **Book of Why** playground. Build intuition for Judea Pearl's causal ladder by
*doing* it: tap a node to `do()` an intervention and watch a spurious correlation collapse into
the true causal effect.

## Run it

No install, no build. Either:
- **Double-click / tap** `index.html`, **or**
- Serve it: `python3 -m http.server 8000` from this folder, then open `http://localhost:8000`.

## What you can play with

Five case studies, each teaching a different causal lesson:

| Case study | Lesson | Pearl concept |
| --- | --- | --- |
| **Alzheimer's · Stress Granules** | How much of the disease runs *through* NCT vs. bypass paths | Front-door criterion & mediation decomposition |
| **Melanoma · Sunscreen** | Why "sunscreen → melanoma" is a mirage | Backdoor / common-cause confounding |
| **Parkinson's · Smoking** | How a fake "protective" effect appears from nothing | Collider bias (Berkson's paradox) |
| **Stroke · Blood pressure** | Splitting an effect into direct + indirect | Proportion mediated |
| **Migraine · Stress** | Intervening on the *mediator* instead of the cause | Controlled direct effect |

## How to use it

1. Pick a case study (the pills at the top).
2. Read the **observed association** — the naive correlation.
3. **Tap a node** to `do()` it: this severs its incoming arrows (you'll see ✂). That's a surgical
   intervention — exactly Pearl's `do`-operator.
4. Compare the **causal effect** to the observed one. The gap is the bias (confounding, collider,
   or an un-blocked mediator).
5. Hit **▶ Run model** to animate the signal flowing through the graph.
6. For the Parkinson's case, toggle **condition on collider** to watch a spurious link appear.

## How it works (architecture)

Single `index.html`, no dependencies. The engine is a tiny **linear Structural Causal Model**:

- Each case is a **DAG**: `nodes` (treatment / mediator / outcome / latent / collider) and
  weighted `edges` (`causal`, `bypass`, or latent `confound`).
- **Observed association** comes from a Monte-Carlo simulation of the SCM (`simulate()`), with an
  optional filter that *conditions on a collider*.
- **Causal effect** comes from tracing all directed paths from treatment to outcome
  (`paths()` → `causal()`); the **proportion mediated** splits those paths by whether they pass
  through the mediator (`mediationSplit()`).
- Clicking a node adds it to the `cut` set; cut nodes become exogenous (their incoming edges are
  severed) in both the simulation and the path tracer — that *is* the intervention.

To add a case study, drop another entry into the `CASES` object (nodes, edges, and which node is
`x`, `y`, and the optional `mediator`).

## Background reading

- Judea Pearl & Dana Mackenzie, *The Book of Why* (2018) — the ladder of causation.
- The Alzheimer's case is a teaching abstraction of the published **Coleman et al. (2025)**
  stress-granule / nucleocytoplasmic-transport framework, viewed through Pearl's front-door
  criterion. It is illustrative, not a clinical claim.

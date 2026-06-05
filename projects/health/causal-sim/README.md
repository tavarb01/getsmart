# Causal-Sim 🧭

An interactive **Book of Why** playground. Build intuition for Judea Pearl's causal ladder by
*doing* it: tap a node to `do()` an intervention and watch a spurious correlation collapse into
the true causal effect.

## Run it

No install, no build. Either:
- **Double-click / tap** `index.html`, **or**
- Serve it: `python3 -m http.server 8000` from this folder, then open `http://localhost:8000`.

## What you can play with

Models are organised as a 3-level drill-down — **Domain → Disease → Model** — so the library can
grow without becoming a flat mess:

```
Neurodegeneration
├── Alzheimer's
│   ├── Coleman · SG → NCT        front-door criterion & mediation decomposition
│   └── Amyloid cascade           a competing causal DAG for the same disease
└── Parkinson's
    └── Smoking & the collider trap   collider bias (Berkson's paradox)
Oncology
└── Melanoma
    └── Sunscreen confounding      backdoor / common-cause confounding
Cardiovascular
└── Stroke
    └── BP → arterial damage       proportion mediated
Headache & Pain
└── Migraine
    └── Stress, sleep & the mediator   controlled direct effect
```

Alzheimer's deliberately holds **two competing models** side by side: Coleman's stress-granule →
NCT framework, and the amyloid cascade (where NCT sits *downstream* of tau). Same disease, same
outcome — different graph, different place to intervene.

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

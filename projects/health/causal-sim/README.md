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
🧠 Neurology
├── Alzheimer's
│   ├── Coleman · SG → NCT        front-door criterion & mediation decomposition
│   ├── Amyloid cascade           a competing DAG: NCT downstream of tau
│   └── Convergent inputs         many causes share one bottleneck (NCT)
├── Parkinson's
│   └── Smoking & the collider trap   collider bias (Berkson's paradox)
└── Migraine
    └── Stress, sleep & the mediator   controlled direct effect
🎗️ Oncology
├── Melanoma
│   └── Sunscreen confounding      backdoor that flips the sign
└── Lung cancer
    └── Smoking · Fisher's confounder   confounding that can't explain it away
🫀 Cardiometabolic
└── Stroke
    └── BP → arterial damage       proportion mediated
🦠 Infectious Disease
└── Cholera
    └── Snow's natural experiment (1854)   the founding causal story
```

Alzheimer's deliberately holds **three competing models** side by side — Coleman's stress-granule →
NCT framework, the amyloid cascade (NCT *downstream* of tau), and a convergent-inputs model (many
causes share the NCT bottleneck). Same disease, same outcome — different graph, different place to
intervene.

Tip: every model has a **"show the math" panel** that prints the actual directed paths, their
products, and the proportion mediated, so the numbers are never a black box.

## How to use it

1. Open the **"Behind the scenes"** intro at the top — it explains, in plain language, how every
   number is produced (virtual patients → regression → path tracing).
2. Pick a **Domain → Disease → Model**.
3. Read the three numbers:
   - **Observed association** *(from data)* — the naive correlation.
   - **The identified estimate** *(from data)* — front-door, back-door, a natural experiment, or a
     randomized `do()`, depending on what the case allows.
   - **Model-entailed effect** *(◆ model)* — the effect that *follows necessarily from the assumed
     arrow-strengths*. Not a measurement; change the assumptions and it changes.
4. **Tap a node** to `do()` it (✂ severs its incoming arrows) and **▶ Run** to animate the flow.
5. Expand **"show the math"** to see the path products behind the model-entailed effect.

### What "◆ model" means (read this — it matters)
A number marked **◆** is **model-entailed, not measured**: it follows logically from the arrow
strengths the model *assumes*. It is **not** ground truth about any real disease — and the strengths
here are **illustrative, chosen for teaching, not estimated from data**. Real research has no such
answer key; that's precisely what makes causal inference hard.

So this tool is honest about what it is: a demonstration of the *logic* of causal inference (which
is real and verified), running on *invented parameters* (which are not). The transferable lesson is
structural — *when* front-door under-counts, *how* a collider manufactures an artifact — never the
specific numbers on screen.

### Sensitivity mode: ranges, not points
Because the strengths are assumptions, the model-entailed effect is reported as a **90% range under
stated assumptions**, not a single number — exactly the discipline a careful analysis follows (a
point estimate of "the truth" is what the Coleman/NCT perspective that inspired this deliberately
refuses to claim). Each arrow carries a strength **± a range**; the app samples within those ranges
and propagates the uncertainty to the effect and the proportion mediated. The **assumption-width**
control (tight / stated / loose) widens or narrows every range at once, so you can see whether a
conclusion is robust or fragile. Expand **"assumptions"** to read exactly what the interval is
conditional on.

## The five escape routes from confounding

Each model is tagged with how you can (or can't) recover the truth — a tour of Pearl's toolkit:

| Route | Example | What it shows |
| --- | --- | --- |
| **Randomized `do()` (RCT)** | Melanoma, HRT, Lung cancer | When the confounder is *unmeasurable*, only randomizing works |
| **Natural experiment** | Cholera (Snow 1854) | History randomizes for you |
| **Front-door** | Coleman, Statins, Stroke, Migraine | Recover the effect *through a mediator* from data alone |
| **Back-door adjustment** | Berkeley admissions | Adjust for a measured common cause (Simpson's paradox) |
| **Collider (a trap)** | Parkinson's, Birthweight paradox | Conditioning on a common *effect* invents correlations |

The Alzheimer's trio is the centrepiece: **Coleman's front-door under-counts** (bypass paths leak),
while the **amyloid** and **convergent** models have no bypass, so front-door recovers them exactly.

## What you can play with

Models are organised as a 3-level drill-down — **Domain → Disease → Model**:

```
🧠 Neurology
├── Alzheimer's   ├ Coleman · SG → NCT   ├ Amyloid cascade   └ Convergent inputs
├── Parkinson's   └ Smoking & the collider trap
└── Migraine      └ Stress, sleep & the mediator
🎗️ Oncology
├── Melanoma      └ Sunscreen confounding (sign flip)
└── Lung cancer   └ Smoking · Fisher's confounder
🫀 Cardiometabolic
├── Stroke        └ BP → arterial damage
└── Heart disease ├ HRT · the WHI reversal   └ Statins → LDL → CHD
🦠 Infectious Disease
└── Cholera       └ Snow's natural experiment (1854)
👶 Perinatal
└── Infant mortality   └ The birthweight paradox
⚖️ Society & Policy
└── Admissions    └ Berkeley admissions (Simpson's paradox)
```

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

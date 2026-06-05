# Causal-Sim 🧭

An interactive **Book of Why** playground. Build intuition for Judea Pearl's causal ladder by
*doing* it: tap a node to `do()` an intervention and watch a spurious correlation collapse into
the true causal effect.

New here? Tap **🎓 Learn** in the header for a 4-minute, no-math primer — a slide-deck tour of the
Ladder of Causation, confounders, the `do()` operator, the three numbers, and how to read the
sandbox (general teaching; no domain expertise assumed).

Three lenses on every model, via the header toggle: **👩‍🏫 Teacher** (intuition), **🔬 Researcher**
(real-world evidence + citations), and **💼 Boardroom** — the decision and what it's worth in plain
English (the call, the gap between the dashboard and the truth, the trap, and the move; no standard
deviations). Figures are illustrative — the *gap* is the point.

## Run it

No install, no build. Either:
- **Double-click / tap** `index.html`, **or**
- Serve it: `python3 -m http.server 8000` from this folder, then open `http://localhost:8000`.

## The Causal Ladder, everywhere

The top level is a **Field** selector: the same three rungs of causal reasoning (see → do → imagine)
applied across **epistemic domains** — domains of human knowledge. Switch fields with the tab bar;
each field carries its own **Area → Topic → Model** drill-down.

- **🧬 Health & Life Sciences** — the original 17 models (below).
- **📈 Economics & Policy** — the *credibility revolution*. A new **instrumental-variable (`iv`)
  estimator** shows how a natural experiment recovers a confounded effect via the Wald ratio
  `cov(Z,Y)/cov(Z,X)`:
  - *Labor & Wages* — the minimum-wage showdown (Card–Krueger border IV) · the veteran earnings
    penalty (Angrist draft lottery)
  - *Education* — does the degree pay or the person? (quarter-of-birth, a deliberately **weak**
    instrument) · class size & achievement (Project STAR RCT)
  - *Development* — microcredit's modest real effect (J-PAL RCTs) · deworming & attendance
    (Miguel–Kremer RCT)

  Every economics claim in Researcher mode was adversarially fact-checked against the primary
  literature (Card–Krueger 1994, Angrist 1990, Angrist–Krueger 1991, Krueger 1999, Banerjee et al.
  2015, Miguel–Kremer 2004).

- **🤖 AI & Data Science** — where product and model decisions hinge on cause vs. correlation:
  - *A/B Testing* — the feature that "caused" conversions (self-selection vs randomized exposure) ·
    Simpson's paradox inside an A/B test (segment-mix confounding)
  - *ML Pitfalls* — the model that called asthma protective (Caruana — collider via ICU care) ·
    the X-ray model that read the scanner (Zech — shortcut learning / hospital confounder)
  - *Impact & Validity* — did the ad cause the click? (eBay paid-search holdout) · Wald's bombers
    (WWII survivorship / selection bias)

  Every AI claim was adversarially fact-checked (Kohavi 2020, Caruana 2015, Zech 2018, Blake–Nosko–
  Tadelis 2015, Mangel–Samaniego 1984).

- **🛒 Business · CPG & Consumer Health** — causal thinking across the commercial funnel:
  - *Marketing* — does the campaign actually lift sales? (geo-holdout RCT vs marketing-mix
    confounding) · the demand curve that slopes the wrong way (price endogeneity, cost-shock IV)
  - *Sales* — do sales-rep visits drive sales? (detailing vs account-targeting confound) · does the
    loyalty program create loyalty? (heavy-buyer self-selection, adjust for prior spend)
  - *Supply & Availability* — the stockout that "boosted" sales (demand confound, supply-shock natural
    experiment) · is the cheap co-packer really worse? (product-mix confounding)

  DAG-honest only — no bullwhip/feedback or pricing-equilibrium models. Anchored to the
  marketing-science literature (Gordon et al. 2019, Nevo 2001, Leenheer et al. 2007) and
  adversarially fact-checked; the supplier case is flagged as an illustrative example.

- **🧩 Mind, Society & the Human Sciences** — the replication-crisis epicenter:
  - *Psychology* — why talented people seem like jerks (Berkson's collider) · the marshmallow test
    re-examined (self-control vs family-background confounding)
  - *Society & Policy* — does health insurance make you healthier? (Oregon Medicaid lottery RCT) ·
    does prison cause more crime? (random judge-leniency IV)
  - *Health & Behavior* — is moderate drinking good for you? (the alcohol J-curve vs Mendelian
    randomization) · does coffee cause pancreatic cancer? (a smoking-confounded phantom)

  Adversarially fact-checked (Berkson 1946, Watts–Duncan–Quan 2018, Finkelstein 2012/Baicker 2013,
  Aizer–Doyle 2015, Holmes 2014, MacMahon 1981).

> **Roadmap:** one field remains — **🌍 Climate & Environment** (warming attribution, carbon-tax
> difference-in-differences, pollution regression-discontinuity) — DAG-honest and fact-checked
> before shipping.

## What you can play with

Health models are organised as a 3-level drill-down — **Domain → Disease → Model** — so the library
can grow without becoming a flat mess:

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

### Two modes: Teacher and Researcher
A toggle at the top switches the framing without changing the (exact, verified) simulation math:

- **👩‍🏫 Teacher** — intuition first. Plain-language lessons and the interactive `do()` loop. Honest
  that the *math* is exact while the *numbers* are illustrative.
- **🔬 Researcher** — honest about each domain's **actual real-world evidence**. The panel reports
  what is established versus hypothesised, with **citations** and an explicit **identification
  verdict** (RCT-identified, natural experiment, robust-but-contested, recognised artifact, or
  *not identified*). The simulated numbers are clearly flagged as a *structural illustration*, not
  the real effect sizes.

For example, in Researcher mode the **Coleman** model states plainly that the SG→NCT link is *not
identified* (front-door fails on documented bypass paths), while **smoking → lung cancer**,
**statins → LDL → CHD**, and **sunscreen → melanoma (Nambour RCT)** are flagged as identified, with
sources. This keeps the tool easy to learn from *and* honest to a medical researcher.

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
├── Melanoma         └ Sunscreen confounding (sign flip)
├── Lung cancer      └ Smoking · Fisher's confounder
└── Cervical cancer  └ HPV vaccine (Sweden cohort, 2020)
🫀 Cardiometabolic
├── Stroke        └ BP → arterial damage
├── Heart disease ├ HRT · the WHI reversal   └ Statins → LDL → CHD
├── Obesity       └ Semaglutide → CV events (SELECT, 2023)
└── Vitamin D     └ VITAL null result (RCT overturns observational)
🦠 Infectious Disease
├── Cholera   └ Snow's natural experiment (1854)
└── COVID-19  └ Vaccine & the Simpson's-paradox trap
👶 Perinatal
└── Infant mortality   └ The birthweight paradox
⚖️ Society & Policy
└── Admissions    └ Berkeley admissions (Simpson's paradox)
```

**17 models across 6 domains.** The Researcher-mode evidence is anchored in landmark trials and
meta-analyses (2019–2025 where relevant) — SELECT (semaglutide), VITAL (vitamin D), the Swedish HPV
cohort, the COVID-19 vaccine RCT, BPLTTC 2021, the CTT statin meta-analyses, and the anti-amyloid
trials — and was **adversarially fact-checked** for effect sizes, citations, and identification
status before shipping. Teacher and Researcher modes cover the **same diagrams** (the toggle only
changes the framing), so there is full parity between them.

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

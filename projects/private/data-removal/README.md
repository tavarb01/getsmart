# data-removal

A human-in-the-loop toolkit for getting **your own** listing removed from
people-search sites and data brokers (Spokeo, Whitepages, TruePeopleSearch,
Nuwber, Radaris, BeenVerified, MyLife, Acxiom, LexisNexis, Epsilon, Oracle),
using each site's **official** opt-out channel. It's a DIY version of what
services like DeleteMe/Optery sell.

**What it will never touch:** accounts you actually have. It doesn't log in
anywhere, doesn't unsubscribe you from anything, and only contacts the brokers
listed in `brokers.json` — companies holding data about you *without* a
relationship with you. Your bank, your email, your subscriptions, and every
service you signed up for are completely out of scope.

## Run it

Real runs happen **on your own computer** (you need a visible browser, your
home internet connection, and access to your email inbox for confirmation
links). One-time setup:

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
cp identity.example.json identity.json   # then edit with your real details
```

Then work through the four phases:

```bash
python3 optout.py audit    # 1. opens each broker's search; YOU confirm matches
python3 optout.py plan     # 2. stages endpoints, writes email drafts to outbox/
python3 optout.py run      # 3. drives the opt-out forms; YOU approve every submit
python3 optout.py report   # 4. summary, follow-up dates, calendar reminders
```

When you later verify a listing is really gone:

```bash
python3 optout.py mark spokeo removed
```

## Safety model

- **Nothing submits without you.** Every form pauses for an explicit `y`
  before submitting; CAPTCHAs are yours to solve in the visible browser.
- **Resumable.** State lives in `removal_status.json`; a dropped session
  resumes where it left off and never double-submits.
- **Paced.** Randomized 3–7 s delays between browser actions.
- **No PII in git.** `identity.json`, `removal_status.json`, `audit_log.md`,
  `outbox/`, and `followups.ics` are all gitignored (see `.gitignore`).
  Only code, the broker registry, and blank templates are committed.

## Self-test (no network, no real data)

Exercises the whole harness against a local fake opt-out form:

```bash
cp identity.example.json identity.json      # fake sample data is fine here
OPTOUT_FAST=1 python3 optout.py run --broker test --headless <<< $'y'
python3 optout.py report
```

## Extending

- `brokers.json` is the registry — add a site by adding an entry (search URL
  pattern, opt-out URL, method: `form` / `email` / `portal`, wait days).
- Opt-out pages change and mostly need a human anyway, so form auto-fill
  selectors (`form_fields`, `submit_selector`) are optional per broker; the
  `test` entry shows the format. Without them, `run` still opens the page,
  paces you through it, and records the submission.
- Aggregators (Acxiom, LexisNexis, Epsilon) use ID-verified portals that
  can't honestly be automated — `plan` gives you drafts and checklists instead.

## Good to know

- Opting out is a right under the CCPA/CPRA and similar state laws, but
  brokers re-scrape public records — expect to re-run `audit` every few
  months. `report` writes `followups.ics` so the reminders land in your
  calendar.
- MyLife removal can also be done by phone: (888) 704-1900, press 2.
- Oracle shut down its advertising-data business in 2024; its entry is kept
  for a belt-and-suspenders deletion email.

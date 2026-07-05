#!/usr/bin/env python3
"""
optout.py — a human-in-the-loop toolkit for removing YOUR OWN listing from
data brokers and people-search sites, via each site's official opt-out channel.

Subcommands (run them in this order):

  audit    Phase 1: opens each broker's people-search with your name in a
           visible browser; YOU confirm which listings are really you.
  plan     Phase 2: stages opt-out endpoints and writes deletion-request
           email drafts into outbox/ for the email/portal brokers.
  run      Phase 3: drives the form-based opt-outs in a visible browser.
           Nothing is ever submitted without your explicit per-site "y".
  report   Phase 4: summary of done/pending/manual, follow-up dates, a
           followups.ics calendar file, and follow-up email drafts.
  mark     Manually set a broker's status (e.g. `mark spokeo removed`
           after you verify the listing is gone).

Safety model:
  - Only YOUR identity (identity.json), only official opt-out channels.
  - Confirm-before-submit gate on every form; CAPTCHA pauses for you.
  - Randomized 3-7s pacing between browser actions.
  - State saved to removal_status.json after every step, so a dropped
    session resumes without double-submitting.
  - identity.json, removal_status.json, audit_log.md, outbox/, followups.ics
    all hold personal data and are gitignored. Never commit them.
"""

import argparse
import datetime as dt
import json
import os
import random
import sys
import time
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
BROKERS_FILE = HERE / "brokers.json"
IDENTITY_FILE = HERE / "identity.json"
STATUS_FILE = HERE / "removal_status.json"
AUDIT_FILE = HERE / "audit_log.md"
OUTBOX_DIR = HERE / "outbox"
TEMPLATES_DIR = HERE / "templates"
ICS_FILE = HERE / "followups.ics"

# Statuses a broker moves through. "assumed" = aggregator with no public
# search, included in the batch without a confirmed profile URL.
PENDING = ("found", "assumed")
DONE = ("submitted", "confirmed", "removed")

# Randomized pause between browser actions. OPTOUT_FAST=1 shrinks it so the
# local self-test doesn't dawdle; real runs keep a human-ish 3-7s cadence.
DELAY_RANGE = (0.05, 0.15) if os.environ.get("OPTOUT_FAST") == "1" else (3.0, 7.0)


def pause():
    time.sleep(random.uniform(*DELAY_RANGE))


# ---------------------------------------------------------------- data files

def load_brokers():
    return json.loads(BROKERS_FILE.read_text())


def load_identity():
    if not IDENTITY_FILE.exists():
        sys.exit(
            "identity.json not found.\n"
            "Copy identity.example.json to identity.json, fill in your own "
            "details, and re-run. (identity.json is gitignored.)"
        )
    return json.loads(IDENTITY_FILE.read_text())


def load_status():
    if STATUS_FILE.exists():
        return json.loads(STATUS_FILE.read_text())
    return {}


def save_status(status):
    STATUS_FILE.write_text(json.dumps(status, indent=2) + "\n")


class SafeDict(dict):
    """Leave unknown {placeholders} intact instead of crashing."""

    def __missing__(self, key):
        return "{" + key + "}"


def placeholders(identity, profile_url=""):
    """Flatten identity.json into the {placeholders} used by URLs/templates."""
    addresses = identity.get("addresses") or [{}]
    addr = next((a for a in addresses if a.get("current")), addresses[0])
    parts = identity["full_name"].split()
    ph = {
        "full_name": identity["full_name"],
        "first_name": identity.get("first_name", parts[0]),
        "last_name": identity.get("last_name", parts[-1]),
        "email": (identity.get("emails") or [""])[0],
        "phone": (identity.get("phones") or [""])[0],
        "street": addr.get("street", ""),
        "city": addr.get("city", ""),
        "state": addr.get("state", ""),
        "zip": addr.get("zip", ""),
        "profile_url": profile_url,
        "aliases": ", ".join(identity.get("aliases", [])) or "none",
        "all_emails": ", ".join(identity.get("emails", [])),
        "all_phones": ", ".join(identity.get("phones", [])),
        "all_addresses": "; ".join(
            f"{a.get('street', '')}, {a.get('city', '')}, {a.get('state', '')} {a.get('zip', '')}".strip(", ")
            for a in addresses
        ),
        "date": dt.date.today().isoformat(),
    }
    ph["city_state"] = ", ".join(x for x in (ph["city"], ph["state"]) if x)
    ph["city_state_zip"] = " ".join(x for x in (ph["city_state"], ph["zip"]) if x)
    return ph


def fill_url(template, ph):
    quoted = SafeDict({k: urllib.parse.quote(str(v)) for k, v in ph.items()})
    return template.format_map(quoted)


def resolve_url(url):
    """http(s) URLs pass through; bare filenames resolve to local file:// URIs
    relative to this folder (used by the test fixture)."""
    if url.startswith(("http://", "https://", "file://")):
        return url
    return (HERE / url).as_uri()


def render_template(name, mapping):
    text = (TEMPLATES_DIR / name).read_text()
    return text.format_map(SafeDict(mapping))


# ------------------------------------------------------------------- browser

def launch_page(headless):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit(
            "Playwright is not installed. Run:\n"
            "  python3 -m pip install playwright\n"
            "  python3 -m playwright install chromium"
        )
    p = sync_playwright().start()
    try:
        browser = p.chromium.launch(headless=headless)
    except Exception:
        # Fall back to a system/preinstalled Chromium when Playwright's own
        # browser download is missing or a different build. Override with
        # OPTOUT_CHROMIUM=/path/to/chrome if needed.
        exe = os.environ.get("OPTOUT_CHROMIUM")
        for candidate in ([exe] if exe else []) + ["/opt/pw-browsers/chromium"]:
            if candidate and Path(candidate).exists():
                browser = p.chromium.launch(headless=headless, executable_path=candidate)
                break
        else:
            p.stop()
            raise
    page = browser.new_page()
    return p, browser, page


def ask(prompt):
    return input(prompt).strip().lower()


# ------------------------------------------------------------ phase 1: audit

def cmd_audit(args):
    identity = load_identity()
    brokers = [b for b in load_brokers() if b.get("category") != "test"]
    status = load_status()
    ph = placeholders(identity)

    p = browser = page = None
    try:
        for b in brokers:
            entry = status.get(b["id"], {})
            if entry.get("status") in DONE:
                print(f"=== {b['name']}: already {entry['status']}, skipping.")
                continue

            if b.get("search_url"):
                if page is None:
                    p, browser, page = launch_page(args.headless)
                url = fill_url(b["search_url"], ph)
                print(f"\n=== {b['name']} — opening search:\n    {url}")
                try:
                    page.goto(url, timeout=60_000)
                except Exception as exc:
                    print(f"    (page load problem: {exc}) — check the browser window anyway")
                if ask(f"Is YOUR profile listed on {b['name']}? [y/N] ") == "y":
                    prof = input(
                        "Paste your profile URL (Enter = use the page's current URL): "
                    ).strip() or page.url
                    status[b["id"]] = {"status": "found", "profile_url": prof}
                else:
                    status[b["id"]] = {"status": "not_found"}
                pause()
            else:
                # Aggregators offer no public search; they almost certainly
                # hold data on you, so default to including them.
                ans = ask(f"\n{b['name']} has no public search. Include it in the removal batch? [Y/n] ")
                status[b["id"]] = {"status": "not_found" if ans == "n" else "assumed"}
            save_status(status)
    finally:
        if browser:
            browser.close()
        if p:
            p.stop()

    table = audit_table(brokers, status)
    AUDIT_FILE.write_text(table)
    print("\n" + table)
    print(f"Audit written to {AUDIT_FILE.name} (gitignored).")
    print("Review it, then run:  python3 optout.py plan")


def audit_table(brokers, status):
    lines = [
        f"# Data broker audit — {dt.date.today().isoformat()}",
        "",
        "| Data Broker / Site | Profile Found | Profile URL | Opt-Out Method |",
        "|---|---|---|---|",
    ]
    for b in brokers:
        e = status.get(b["id"], {})
        found = {"found": "Yes", "assumed": "Assumed", "not_found": "No"}.get(
            e.get("status"), e.get("status", "—")
        )
        lines.append(
            f"| {b['name']} | {found} | {e.get('profile_url', '—')} | {b['method']} |"
        )
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------- phase 2: plan

def cmd_plan(args):
    identity = load_identity()
    brokers = load_brokers()
    status = load_status()
    if not status:
        sys.exit("No audit yet — run:  python3 optout.py audit")
    OUTBOX_DIR.mkdir(exist_ok=True)

    print("Opt-out plan for confirmed/assumed brokers:\n")
    for b in brokers:
        e = status.get(b["id"], {})
        if e.get("status") not in PENDING:
            continue
        ph = placeholders(identity, profile_url=e.get("profile_url", ""))
        if b["method"] == "form":
            print(f"  {b['name']}: form at {b['optout_url']} — automated by `run`")
        elif b["method"] == "email":
            draft = draft_email(b, ph)
            path = OUTBOX_DIR / f"{b['id']}.md"
            path.write_text(draft)
            print(f"  {b['name']}: email draft written to outbox/{path.name} "
                  f"(send to {b['email_to']} from your own mail client)")
        else:  # portal
            print(f"  {b['name']}: manual portal — visit {b['optout_url']}")
        if b.get("notes"):
            print(f"      note: {b['notes']}")
    print("\nDrafts contain your personal data; outbox/ is gitignored.")
    print("Next:  python3 optout.py run")


def draft_email(broker, ph):
    profile_line = (
        f"- Profile URL: {ph['profile_url']}" if ph["profile_url"] else ""
    )
    mapping = dict(ph, broker_name=broker["name"],
                   email_to=broker.get("email_to", ""), profile_line=profile_line)
    return render_template("deletion_request.md", mapping)


# -------------------------------------------------------------- phase 3: run

def cmd_run(args):
    identity = load_identity()
    brokers = [b for b in load_brokers() if b["method"] == "form"]
    if args.broker:
        brokers = [b for b in brokers if b["id"] == args.broker]
        if not brokers:
            sys.exit(f"No form-based broker with id '{args.broker}' in brokers.json")
    status = load_status()

    todo = []
    for b in brokers:
        e = status.get(b["id"])
        if e is None:
            if args.broker:  # explicit request: allow running without an audit
                e = status[b["id"]] = {"status": "found"}
            else:
                print(f"=== {b['name']}: not audited yet — run `audit` first. Skipping.")
                continue
        if e["status"] in DONE:
            print(f"=== {b['name']}: already {e['status']} — will not re-submit.")
        elif e["status"] in PENDING:
            todo.append((b, e))
        else:
            print(f"=== {b['name']}: status '{e['status']}', skipping. "
                  f"(Use `mark {b['id']} found` to retry.)")
    if not todo:
        print("Nothing to do.")
        return

    p, browser, page = launch_page(args.headless)
    try:
        for b, e in todo:
            print(f"\n=== {b['name']} — opening opt-out page")
            if b.get("notes"):
                print(f"    note: {b['notes']}")
            ph = placeholders(identity, profile_url=e.get("profile_url", ""))
            try:
                page.goto(resolve_url(b["optout_url"]), timeout=60_000)
            except Exception as exc:
                print(f"    page load problem: {exc}")
            pause()

            for selector, value_tpl in b.get("form_fields", {}).items():
                value = value_tpl.format_map(SafeDict(ph))
                try:
                    page.fill(selector, value)
                    pause()
                except Exception:
                    print(f"    couldn't auto-fill {selector} — fill it manually in the browser")

            print("    If a CAPTCHA appears, solve it in the browser window now.")
            print("    Review the form and complete anything the script missed.")
            ans = ask(f"Submit the {b['name']} opt-out now? [y/N] ")
            if ans != "y":
                e["status"] = "skipped"
                save_status(status)
                print("    Skipped (nothing was submitted).")
                continue

            if b.get("submit_selector"):
                page.click(b["submit_selector"])
                pause()
            else:
                input("    Click Submit in the browser yourself, then press Enter here... ")
            e["status"] = "submitted"
            e["submitted_at"] = dt.datetime.now().isoformat(timespec="seconds")
            save_status(status)
            print("    Submitted and recorded. If the site emails you a "
                  "confirmation link, click it to finish.")
    finally:
        browser.close()
        p.stop()
    print("\nDone. Next:  python3 optout.py report")


# ----------------------------------------------------------- phase 4: report

def cmd_report(args):
    identity = load_identity()
    brokers = load_brokers()
    status = load_status()
    if not status:
        sys.exit("No status yet — run:  python3 optout.py audit")
    today = dt.date.today()
    OUTBOX_DIR.mkdir(exist_ok=True)

    done, waiting, action, out = [], [], [], []
    for b in brokers:
        e = status.get(b["id"])
        if not e:
            continue
        st = e["status"]
        if st in ("confirmed", "removed"):
            done.append((b, e, None))
        elif st == "submitted":
            # marked_at covers entries set by hand via `mark ... submitted`
            when = e.get("submitted_at") or e.get("marked_at") or today.isoformat()
            submitted = dt.date.fromisoformat(when[:10])
            follow_up = submitted + dt.timedelta(days=b.get("wait_days", 7))
            waiting.append((b, e, follow_up))
        elif st in PENDING:
            action.append((b, e, None))
        else:
            out.append((b, e, None))

    print(f"# Removal report — {today.isoformat()}\n")
    print(f"Completed ({len(done)}):")
    for b, e, _ in done:
        print(f"  - {b['name']} ({e['status']})")
    print(f"\nSubmitted, waiting on the broker ({len(waiting)}):")
    for b, e, fu in waiting:
        overdue = "  <-- wait period over: verify, and re-send if still listed" if fu <= today else ""
        print(f"  - {b['name']}: check on {fu.isoformat()} "
              f"(~{b.get('wait_days', 7)} day wait){overdue}")
    print(f"\nStill needs action ({len(action)}):")
    for b, e, _ in action:
        how = {"form": "run `python3 optout.py run`",
               "email": f"send outbox/{b['id']}.md to {b.get('email_to', '?')}",
               "portal": f"visit {b['optout_url']}"}[b["method"]]
        print(f"  - {b['name']}: {how}")
    print(f"\nSkipped / not found ({len(out)}):")
    for b, e, _ in out:
        print(f"  - {b['name']} ({e['status']})")

    if waiting:
        write_ics(waiting)
        print(f"\nCalendar reminders written to {ICS_FILE.name} "
              "(import into Google Calendar / Apple Calendar).")
        for b, e, fu in waiting:
            if fu <= today:
                ph = placeholders(identity, profile_url=e.get("profile_url", ""))
                profile_line = (
                    f"- Profile URL: {ph['profile_url']}" if ph["profile_url"] else ""
                )
                when = e.get("submitted_at") or e.get("marked_at") or today.isoformat()
                mapping = dict(ph, broker_name=b["name"],
                               email_to=b.get("email_to", "(see their site)"),
                               submitted_date=when[:10],
                               wait_days=b.get("wait_days", 7),
                               profile_line=profile_line)
                path = OUTBOX_DIR / f"followup_{b['id']}.md"
                path.write_text(render_template("followup.md", mapping))
                print(f"Follow-up draft written to outbox/{path.name}")
    print("\nWhen you verify a listing is gone:  python3 optout.py mark <broker> removed")


def write_ics(waiting):
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0",
             "PRODID:-//getsmart//data-removal//EN"]
    for b, e, follow_up in waiting:
        lines += [
            "BEGIN:VEVENT",
            f"UID:optout-{b['id']}@getsmart.local",
            f"DTSTAMP:{now}",
            f"DTSTART;VALUE=DATE:{follow_up.strftime('%Y%m%d')}",
            f"SUMMARY:Verify data removal: {b['name']}",
            f"DESCRIPTION:Check {e.get('profile_url') or b.get('optout_url') or b['name']}"
            " — if still listed, send the follow-up draft from outbox/.",
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    ICS_FILE.write_text("\r\n".join(lines) + "\r\n")


# --------------------------------------------------------------------- mark

def cmd_mark(args):
    status = load_status()
    ids = [b["id"] for b in load_brokers()]
    if args.broker_id not in ids:
        sys.exit(f"Unknown broker '{args.broker_id}'. Known: {', '.join(ids)}")
    entry = status.setdefault(args.broker_id, {})
    entry["status"] = args.new_status
    entry["marked_at"] = dt.datetime.now().isoformat(timespec="seconds")
    save_status(status)
    print(f"{args.broker_id} -> {args.new_status}")


# --------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("audit", help="Phase 1: find your listings (interactive)")
    a.add_argument("--headless", action="store_true",
                   help="no visible browser (self-test only)")
    a.set_defaults(func=cmd_audit)

    pl = sub.add_parser("plan", help="Phase 2: stage endpoints + email drafts")
    pl.set_defaults(func=cmd_plan)

    r = sub.add_parser("run", help="Phase 3: drive form opt-outs (interactive)")
    r.add_argument("--broker", help="only this broker id (e.g. spokeo, test)")
    r.add_argument("--headless", action="store_true",
                   help="no visible browser (self-test only)")
    r.set_defaults(func=cmd_run)

    rp = sub.add_parser("report", help="Phase 4: summary + reminders")
    rp.set_defaults(func=cmd_report)

    m = sub.add_parser("mark", help="manually set a broker's status")
    m.add_argument("broker_id")
    m.add_argument("new_status",
                   choices=["found", "assumed", "not_found", "skipped",
                            "submitted", "confirmed", "removed"])
    m.set_defaults(func=cmd_mark)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

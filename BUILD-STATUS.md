# bcom ICT website — build status

Working file for the rebuild. **Read this first in any new session.** Every chunk
is self-contained and pushed to `main` when it's done, so work is never lost if
the machine goes off mid-build.

Strategy doc: https://claude.ai/code/artifact/8f2a0bb6-5647-4847-89cb-52085fff9159

---

## How to work on this

```bash
cd ~/bcom-ict-website && python3 build/build.py
```

Pages are Python modules in `build/pages/`. Each exports a `PAGE` dict. Shared
header, footer, nav, hero and schema live in `build/layout.py` — change them once,
rebuild, and all pages update. Business facts live in `build/site_data.py`.

Preview: `bcom-ict` server on port 4400.

**When editing `assets/css/styles.css` or `assets/js/main.js`, bump `ASSET_V` in
`build/layout.py`.** Cloudflare's edge TTL will otherwise serve stale CSS for hours.

---

## Locked decisions (confirmed by Royce 2026-08-31)

| | |
|---|---|
| Repo | `BcomServicesLimited/bcom-ict-website`, public |
| URLs | **Existing slugs preserved.** New design, same addresses. Parity check gates go-live. |
| Nav | Home · Services · Industries · Support · About — unchanged from the current site |
| Positioning | Business only. Gold Coast = on-site, Australia-wide = remote/managed. No residential. |
| Tone | Two-layer: surface pages plain English, trust centre carries ISO/ITIL/compliance depth |
| GBP name | Trim to **bcom ICT** — drop the keyword suffix (redressal risk) |
| GBP prices | Remove from-prices on managed IT + cybersecurity; keep on transactional services |
| GBP categories | 6 total. Keep Computer repair service (reframed to business hardware). **Add IT security service** — all 6 cybersecurity services move there out of Computer consultant so the two stop competing. |
| GBP services | 36 across the six categories, all <=300 chars. Confirmed credentials worked in: ACMA registered cabler on cabling, police checks on on-site attendance, Microsoft Partner on M365. |
| Suburb pages | Rebuild 10, genuinely distinct content — not templated |
| ISO | **Aligned, NOT certified.** Never write "certified/compliant/accredited" for the org. |
| Credentials | PI + cyber + public liability insured. Police checks + QLD Blue Cards held. **No ACMA cabler registration** — cabling is subcontracted to ACMA registered contractors; never imply bcom ICT holds it. Microsoft: says "Silver Partner", but Silver/Gold are retired tiers — site says **"Microsoft Partner"** until Partner Center is checked. |
| SLA | Draft P1–P4 matrix approved as-is |
| Booking | Google Calendar appointment booking embedded on the homepage — `BIZ["booking"]` in site_data. |
| Remote support | **Splashtop SOS**, instructions and download link on **`/support` only** (Royce's instruction). `BIZ["splashtop"]`. |
| Contact form | **Live and tested end to end** — Formspree `xreoqepk`. Submits in place via fetch so the visitor never leaves the site; falls back to a plain POST with JS off. `_next` is ignored by Formspree (they redirect to their own `/thanks`), which is why the in-page handler exists rather than relying on it. |
| Legal pages | Ported from the old site and updated — they were far more thorough than a generic template (VoIP 000 disclaimer, carrier dependency, number porting, fair-use policies, right to refuse insecure systems). |
| Managed IT pricing | **Not per-seat.** Calculated from business requirements and the services provided; quoted after the free review. Never write "based on staff and device numbers". |
| Rates | **$198 + GST per hour** ($217.80 inc). **$100 + GST on-site call-out** ($110 inc). First hour on site $298 + GST ($327.80 inc). Remote has no call-out. Single source of truth: `RATES` in `build/site_data.py`. Site quotes ex-GST with inc-GST alongside — audience is GST-registered businesses. |

### Wording rules that must not be broken
- Organisation: *"aligned to ISO/IEC 27001:2022 … not currently certified"*. Never "ISO certified".
- Individuals: Royce = ITIL 4 Foundation. Ollie = ISO/IEC 42001:2023 Lead Implementer, issued by BSI.
- Callback promise is **"within 4 business hours"** everywhere. Never "1 hour".
- **Hours (corrected 2026-08-31 — the site had overstated this):** business hours are
  **8:00am – 5:00pm, Monday to Friday, Brisbane time**. The digital assistant answers the
  phone at any hour and logs the job, but **we do not respond to phone enquiries after
  hours** — calls are returned the next business day. After-hours **on-call** support is
  for managed/SLA clients under their agreement only. Never write "open 24/7" or
  "phones answered 24/7". The only legitimate 24/7 claim is the **SOC service**.
- No residential/home-user copy. Home-office WiFi and mesh is fine; general home computer repair is not.
- **Cabling:** "installed by ACMA registered cabling contractors" — bcom ICT engages and manages them.
  Never "bcom ICT is ACMA registered" or "an ACMA registered cabler".
- **Microsoft:** "Microsoft Partner" only. Not "Silver Partner" — that tier no longer exists.

---

## Chunks

Each chunk ends with a commit and a push. Tick as they land.

- [x] **Chunk 1 — Foundation** · repo, design system, generator, homepage
      Self-hosted Manrope + Inter, brand mark SVG derived from the logo, cropped
      logos, hero system, JSON-LD graph, `_headers`, `_redirects`, robots.txt.
- [x] **Chunk 2 — Core service pages (6) + Services hub**
      Managed IT · Business IT Support · Cybersecurity · Business WiFi ·
      Phone Systems · Cloud & Microsoft 365 · Services hub. All seven carry an
      answer block, question-form FAQs with matching FAQPage schema, breadcrumbs,
      Service schema using the exact GBP service name, and a cross-silo link mesh.
      `python3 build/build.py` now runs a link + image check on every build.
- [x] **Chunk 3 — Trust centre (8) + 3 GBP-backed service pages**
      Trust centre hub · published SLA (P1-P4 matrix) · ISO alignment · ITIL service
      model · data handling & sovereignty · NDB guide · ransomware reporting ·
      onboarding · 24/7 SOC · cyber incident response · Essential Eight.
      `build.py` now runs a **claims guard** that fails loudly on any overstated
      ISO / ACMA / Microsoft-tier claim. It has already caught one live regression.
- [x] **Chunk 4 — Company & conversion (7)**
      About · Our team · Contact · Reviews · Case studies · Pricing · Support.
      Person schema with `hasCredential` on Royce (ITIL 4) and Ollie (ISO 42001,
      BSI) — credentials sit on the Person node, never the Organization.
- [x] **Chunk 5a — Core remaining services (14)**
      Remote support · on-site support · IT consulting · troubleshooting · office
      relocation · security health check · ASIC compliance · Microsoft 365 ·
      backup & DR · office cabling · firewall · network troubleshooting ·
      networking · mesh WiFi · VoIP · PBX · phone cabling · NBN.
      Written via `build/newpage.py` — a committed spec-to-module writer, so the
      generated page modules stay the source of truth.
- [x] **Chunk 5b — Repair family + AI (7)**
      Business computer repair · virus & malware removal · Windows/macOS repair ·
      performance optimisation · hardware procurement · AI implementation ·
      ISO/IEC 42001 AI governance.
      **All 36 GBP services now map to a page.** Two of them ("IT Strategy &
      Technology Roadmaps", "Data Cabling") are second names for an existing
      offering, so `also_service` on a page emits an extra `Service` node —
      every GBP string has an exact schema match.
- [x] **Chunk 6 — Industries hub + 8 verticals**
      Small business · healthcare · professional services · real estate · retail ·
      restaurants · hospitality · trades. Each page leads with what is genuinely
      different about that sector rather than swapping the industry name into one
      template — health providers get no Privacy Act small business exemption,
      agencies are targeted through trust accounts, venues are judged on guest WiFi.
- [x] **Chunk 7 — Suburbs (10)**
      Surfers Paradise · Southport · Broadbeach · Robina · Burleigh Heads ·
      Varsity Lakes · Palm Beach · Nerang · Helensvale · Coomera.
      Written distinctly: all 40 FAQ questions are unique across the ten pages
      and every answer block differs. Each leads with what is genuinely local —
      high-rise access in Surfers, the legal/medical concentration in Southport,
      warehouse coverage in Coomera and Nerang, converted shopfronts in Burleigh.
      `nearby()` in layout.py cross-links them so none is an orphan.
- [x] **Chunk 8 — Guides (7)**
      How to choose an MSP · hacked: first 60 minutes · what IT support costs ·
      managed IT vs break-fix · computer replacement cycle · office move checklist ·
      business NBN guide. (Essential Eight shipped in chunk 3.)
      All seven carry `Article` schema — added `article: True` support to
      `layout.schema()`. These are the pages written to be cited, so they stay
      neutral: the MSP guide names criteria that count against us, and the NBN
      guide says plainly we earn nothing from plan choice.
- [x] **Chunk 9 — Legal, utility + the last 11 service pages**
      Privacy policy · terms and conditions · generated HTML sitemap · 404
      (noindex, excluded from sitemap.xml). Plus Copilot, AI phone agents, AI
      chatbots, UniFi, Aruba, IT needs assessment, telecommunications contractor,
      router config, WiFi range extension, software installation, software
      recommendations and technology procurement.
      **`build.py` now reports "all internal links resolve" — zero broken links.**
      The HTML sitemap is generated from the pages actually built, so it cannot
      fall out of step.
- [ ] **Chunk 10 — LLM layer** · `llms.txt`, `llms-full.txt`, internal link mesh,
      og:image cards, IndexNow
- [ ] **Chunk 11 — Parity check & cutover**
      > **DO NOT carry these three rules across from the old `_redirects`:**
      > `/it-support-burleigh-heads-gold-coast.html`, `/it-support-robina-gold-coast.html`
      > and `/it-support-southport-gold-coast.html` currently 301 to the generic
      > IT support page. Chunk 7 rebuilds all three as real pages — carrying the
      > redirects across would silently 301 them away again. · 301 map, every old URL resolves,
      raw-curl crawl, schema validation, then repoint the domain

---

## Blocked / waiting on Royce

| Item | Needed for |
|---|---|
| **Search Console export** — 12 months, page-level, impressions + clicks. *Said "see attached" but no file came through.* | Chunk 11 — decides which of the 11 WiFi brand pages get consolidated vs kept |
| **Legal review of `/privacy-policy` and `/terms-and-conditions`** — both are reasonable and Australian-law aware (APPs, ACL consumer guarantees explicitly preserved) but have not been reviewed by a lawyer | Before go-live |
| **Insurer names and cover limits** for PI / cyber / public liability | Written generically for now ("certificates of currency available on request") — add specifics when supplied |
| **Is the $100 call-out ex-GST?** Assumed yes for consistency with the hourly rate. Site currently says "$100 + GST ($110 inc GST)" — correct if it is GST-inclusive | `/pricing` and 5 other pages |
| **GBP from-prices are wrong** — profile says From $182 / $252 / $310; real minimum is $217.80 remote and $327.80 on site, inc GST. Set to $218 / $328 and delete from managed IT + all 6 cybersecurity services | GBP, this week |
| **Microsoft Partner Center check** — is there a current Solutions Partner designation? "Silver" was retired with the old competency model | Chunk 3, Chunk 4 |
| Permission to name the national retail chain client | `/case-studies` — written accurately but unnamed, with the reason stated in the FAQ |
| Cloudflare: confirm **Block AI bots = OFF** and managed robots.txt disabled on the zone | Before go-live — silently 403s every AI crawler |
| Cloudflare Access on the `.pages.dev` staging domain | Before the site is publicly reachable |

---

## Staging preview

**https://bcomserviceslimited.github.io/bcom-ict-website/**

Served from the `gh-pages` branch. Regenerate after any change:

```bash
cd ~/bcom-ict-website && python3 build/build.py --staging /bcom-ict-website
```

then copy the output into a clone of `gh-pages` and push. The staging build sets
`noindex, nofollow` on every page and ships a disallow-all `robots.txt`, so it
cannot be indexed as a duplicate of the live site. **Always re-run
`python3 build/build.py` afterwards** to restore the production build on `main`.

This is for design approval only — the real staging target is a Cloudflare Pages
project behind Cloudflare Access (chunk 11).

---

## Compliance content that needs verifying before go-live

Two guides carry a visible amber **Under review** banner because their specifics
could not be verified from source. Confirm, then remove the `verify_note(...)`
call from the page module:

| Page | What to confirm |
|---|---|
| `/pricing` | **Resolved.** $198 + GST/hr and $100 + GST call-out published. Managed IT deliberately has **no from-price** — it is calculated from business requirements and services provided, not per seat, and is quoted after the free review. |
| `/contact` | Form posts to `FORM_ENDPOINT` in `build/site_data.py`, currently the placeholder `REPLACE_WITH_BCOM_FORM_ID`. Create the form, paste the ID, rebuild. Page leads with phone and email so nothing is broken meanwhile. |
| `/ransomware-reporting-australia` | Cyber Security Act 2024 — current turnover threshold and reporting window for mandatory ransomware payment reporting (Dept of Home Affairs) |
| `/notifiable-data-breach-guide-australia` | Small business exemption threshold and the current list of exceptions (OAIC); confirm the 30-day assessment window is unchanged |

Both pages also carry standard "general information, not legal advice" framing,
which is appropriate for compliance content regardless.

---

## Notes

- Image library: 178 WebP files carried across from the old repo, 38 MB, all reusable.
- The old repo `BcomITSolutionsPROJECT` stays untouched as the live site and the rollback.
- Logo blue is **#004AAC**, sampled from the logo itself. The old design system used
  cyan `#00c8e0`, which never matched the logo — the new palette is anchored to the real one.
- The `><` mark from the logo is the brand device: section rules, list bullets, card
  icons, hero texture, favicon. `assets/logo/bcom-mark.svg`.

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
| **Response targets** | **The contracted 4-hour response applies to managed / SLA clients ONLY.** Ad-hoc clients get a **best-effort** response — usually the same business day, generally within one business day. Never publish the 4-hour figure as a general promise. `build.py` now runs an **SLA gate** that fails the build if a 4-hour response promise appears without managed/SLA/contracted in the surrounding text. |
| Managed IT pricing | **Not per-seat.** Calculated from business requirements and the services provided; quoted after the free review. Never write "based on staff and device numbers". |
| Rates | **$198 + GST per hour** ($217.80 inc). **$100 + GST on-site call-out** ($110 inc). First hour on site $298 + GST ($327.80 inc). Remote has no call-out. Single source of truth: `RATES` in `build/site_data.py`. Site quotes ex-GST with inc-GST alongside — audience is GST-registered businesses. |

### Wording rules that must not be broken
- Organisation: *"aligned to ISO/IEC 27001:2022 … not currently certified"*. Never "ISO certified".
- Individuals: **Ollie = ITIL 4 Foundation and ISO/IEC 42001:2023 Lead Implementer, issued by BSI.**
  Royce holds no listed certification. *(ITIL was attributed to Royce until 3 Sept 2026 — it is
  Ollie's. Do not reassign it back, and do not invent a credential for Royce.)*
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
- [x] **Chunk 10 — LLM layer**
      `llms.txt` (32 KB, indexes all 112 pages) and `llms-full.txt` (272 KB, every
      answer block plus **651 Q&A pairs**) — both **generated from the pages
      actually built** by `build/llms.py`, so they cannot drift out of step.
      og:image share card generated on-brand at `assets/img/og-image.jpg`, wired
      into og + twitter tags on every page. `indexnow_submit.py` and the key file
      are in place — **do not run it until cutover**, since it would submit the
      old site's URLs. robots.txt cleaned (removed 3 disallows for pages that no
      longer exist; added llms-full.txt).
- [x] **Chunk 11 — Parity check & redirect map**
      All 82 old sitemap URLs resolve (69 direct, 13 via single-hop 301). Zero
      404s, loops or chains. All 91 legacy redirect sources resolve. `_redirects`
      is generated by `build/redirects.py` — it deliberately drops the three
      suburb rules, flattens chains, and fixes a self-redirect loop in the old
      file. Built the 4 PBX brand pages rather than redirecting them.
      **Remaining work is Royce's, in the Cloudflare dashboard — see `CUTOVER.md`.**

### Depth pass — every service page to 1,500+ words

Two new components in `layout.py` carry this: `issues()` renders symptom /
usual cause / what we do (symptom-first, because that is how people search),
and `example()` renders a worked engagement labelled **representative** —
drawn from real work with identifying detail removed, since we do not name
clients without written permission.

Every symptom heading and every example title is unique site-wide, checked
on each pass. **432 symptom blocks and 172 worked examples, no duplicates.**

- [x] **Chunk A — 6 core service pages** · 5,004 -> 10,238 words
- [x] **Chunk B — 8 security & compliance pages** · 7,251 -> 13,132 words
      Leans on the findings that decide outcomes rather than tidy results: the
      backup NAS mapped with the server's own admin credentials, the MFA
      exemption nobody revisited, the firewall rule for a supplier four years
      gone. The incident response page documents what clients have usually
      already done before we arrive, and what each of those costs.
- [x] **Chunk C — 8 networks & telecom pages** · 7,377 -> 13,338 words
      Now carries real pricing as well as depth. Two examples are deliberately
      about *not* selling: the $28,000 switching upgrade that was a tree grown
      into a wireless path, and the server replacement that was one damaged
      cable. Phone cabling documents the NBN migration casualties — the lift
      emergency phone and the back-to-base alarm that had both been silently
      dead for years.
- [x] **Chunk D — 8 industry pages** · 6,223 -> 12,943 words
      Written so no two verticals blur into each other: retail is the till and
      the stock sync, restaurants are the kitchen printer and the delivery
      tablet, hospitality is guest room coverage and function-space density.
      The security examples are all business email compromise and all different
      — the agency mailbox watched for five weeks before a single altered
      settlement email, the contractor's duplicate progress invoice, the
      accounting firm's contractor still holding the file server eighteen
      months on.
- [x] **Chunk E — 13 hardware, AI & consulting pages** · 8,548 -> 21,102 words
      The three overlapping repair pages are kept sharply apart: hardware repair
      is power, drives, heat and liquid; OS repair is profiles, updates,
      BitLocker and licensing; performance is the payroll arithmetic of a slow
      machine. Ten of the thirteen carry a third worked example.
      Six examples in this chunk end in us recommending less: nine machines kept
      instead of eleven replaced, a production system advised against migrating,
      Copilot deferred four months at a healthcare provider, ten licences
      released, an AI pilot measured honestly enough to stop it, and a review
      that told a business to keep its existing provider.
- [x] **Chunk F — 35 of the remaining 45 pages** · all suburbs, services,
      guides and trust pages now over 1,500
      F1 · a local worked example on each of the ten suburb pages, including
      the five already over 1,500 — a suburb set where half the pages carry
      proof and half do not is what reads as templated.
      F2 · the four PBX brand pages were generated from one template, so each
      is written to what is distinctive about that estate rather than given
      identical sections.
      F3 · every service page on the site is now over 1,500.
      F4 · guides shift pattern — not symptoms and fixes but the assumptions
      people hold and why each is wrong.
      F5 · trust pages shift again to questions, including the ones most
      service level documents avoid.

**Deliberately left under 1,500 — these are not service pages:**

| Page | Words | Why |
|---|---|---|
| `/reviews` | 588 | A reviews page. Padding it with prose makes it worse. Grows by getting more reviews |
| `/contact` | 660 | A contact page. People arrive to find a phone number |
| `/industries` | 697 | Navigational hub. Its job is to route to the eight vertical pages |
| `/services` | 940 | Navigational hub, same reasoning |
| `/trust-centre` | 1,190 | Navigational hub for the eight trust pages, all of which are now 1,800+ |
| `/` (homepage) | 1,048 | A homepage converts. 1,500 words of body copy would hurt it |
| `/support` | 946 | Functional — Splashtop SOS instructions. Length is the enemy here |
| `/about` | 923 | Company page. Could grow with real substance, not with a symptoms block |
| `/our-team` | 993 | Same. Grows if Royce wants more depth on credentials |
| `/case-studies` | 925 | **Blocked.** Needs three real named clients with written permission |


---

## Blocked / waiting on Royce

*Resolved and removed Sept 2026: GBP prices and descriptions (Royce updated the profile);
the $100 call-out confirmed ex-GST by the $252 arithmetic; both Cloudflare items, which
were pre-cutover and are verified live — AI crawlers return 200 and our own robots.txt
serves.*


| Item | Needed for |
|---|---|
| **Search Console export** — 12 months, page-level, impressions + clicks. *Said "see attached" but no file came through.* | Chunk 11 — decides which of the 11 WiFi brand pages get consolidated vs kept |
| **Legal review of `/privacy-policy` and `/terms-and-conditions`** — both are reasonable and Australian-law aware (APPs, ACL consumer guarantees explicitly preserved) but have not been reviewed by a lawyer | Before go-live |
| **Insurer names and cover limits** for PI / cyber / public liability | Written generically for now ("certificates of currency available on request") — add specifics when supplied |
| **Microsoft Partner Center check** — is there a current Solutions Partner designation? "Silver" was retired with the old competency model | Chunk 3, Chunk 4 |
| **Switch GBP to a service-area business** — hide the street address, set the coverage area. *Now surfaces on the site: the map embed on `/contact` and `/about` renders whatever GBP shows.* | Consistency with the site |
| **GBP hours** still show "Open 24 hours" | Contradicts every page and the locked hours decision |
| Permission to name the national retail chain client | `/case-studies` — written accurately but unnamed, with the reason stated in the FAQ |

---

## Location: service-area business (Royce, 3 Sept 2026)

**There is no office.** Technicians and the sales team attend the customer; no
customer comes to us. The site published `9 Ferny Avenue, Surfers Paradise QLD
4217` in the utility bar, the footer, the `LocalBusiness` schema, `llms.txt`,
the privacy policy, the terms, and as the travel-time anchor on all ten suburb
pages. All of it is gone.

- Published location is **`Gold Coast QLD, Australia`** and nothing narrower.
  `address_line()` in `site_data.py` is the single source.
- `BIZ` no longer holds `street`, `postcode`, `lat` or `lon` — the keys are
  deleted, so they cannot be reintroduced by accident.
- Schema carries `addressLocality` / `addressRegion` / `addressCountry` plus
  `areaServed`, and **no `GeoCoordinates`**. This is the correct shape for a
  service-area business; the suburb list does the geographic work.
- `geo.region` and `geo.placename` meta tags are kept — they name a region,
  not a point.
- **Nowhere states that we do not have an office.** The address is simply
  absent. Do not add an explanation.
- Suburb pages frame local relevance by **attendance speed**, never by distance
  from a base. "Roughly ten minutes from our office" must not come back.
- `Ferny Avenue` still appears on the Surfers Paradise page describing **client**
  towers. That is the street, not us, and it stays.

## GBP map embed

`map_embed()` in `layout.py`, URL in `MAP_EMBED` in `site_data.py`. On
`/contact` and `/about` only — the entity signal comes from the association,
not from repeating a third-party iframe 112 times.

Google's snippet was changed in two ways: a `title` was added (an unlabelled
iframe is announced as an anonymous frame), and the fixed `600x450` was replaced
with `width:100%` and a height set by breakpoint (420px / 300px mobile).

**The embed renders whatever GBP says.** If the profile still carries the street
address, the map will show the address the site no longer publishes.

## Mobile action bar

`sticky_bar()` in `layout.py`, `.stickybar` in `styles.css`. Two actions: call,
plus **Book a tech** on any page that links to the booking calendar and **Get a
quote** everywhere else (18 / 94 split).

Renders **visible in the HTML**; `main.js` only hides it while the hero — which
carries its own calls to action — is on screen. With JS off the bar simply
stays up. Nothing on this site may depend on JS to render.

## SLA gate hardening (3 Sept 2026)

`sla_gate()` missed two live unscoped 4-hour promises (`/contact`, `/support`)
because the sentence wrapped across two source lines and the pattern matched a
single space. `_strip_tags()` now strips markup **and collapses whitespace**,
and the scope window is ±220 chars rather than ±600 — legitimate SLA prose
elsewhere on a page was excusing unscoped claims several paragraphs away.

Both pages also claimed calls are returned "including weekends and public
holidays", contradicting the published Mon–Fri hours. Fixed.

---

## Online booking (Google Calendar appointment scheduling)

Two components in `layout.py`, both fed from `BIZ["booking"]`:

- `booking_embed()` — the inline iframe. Used where booking IS the point:
  the homepage panel and `/on-site-technical-support-gold-coast`. Lazy-loaded,
  which Google's stock snippet is not.
- `booking_button()` / `booking_cta()` — Google's pop-up button. Used on 16
  pages where a 620px calendar would be too heavy.

**The external CSS/JS loads only on pages that set `"booking": True`** — 17 of
112 pages. Do not put the loader in the global head.

Google injects `<button class="qxCTlb">` with inline colour. `.bookbtn button`
in styles.css restyles it to match `.btn--primary` (Manrope, bcom blue, 14px 26px,
`--radius-sm`). The `!important` flags are needed only for what Google sets inline.

**Outstanding — Royce's, in Google Calendar (not the site):**

| Issue | Currently reads | Should be |
|---|---|---|
| Service description | "1 Hour IT Support for **Gold Coast Home Users** — $252.00 inc GST" | The whole site targets **business**. "Home Users" contradicts every page it appears on |
| Calendar owner name | "**B**com ICT" | Trading name is **bcom ICT**, lowercase b |

## Rate card (Royce, Sept 2026 — current)

| | Ex GST | Inc GST |
|---|---|---|
| Business hourly rate | **$190.00** | $209.00 |
| On-site call-out | **$100.00** | $110.00 |
| **First hour on site** (call-out + hour) | **$290.00** | **$319.00** |
| **First hour on site, booked online** | — | **$252.00 fixed** |
| Remote job, up to one hour (no call-out) | **$150.00** | $165.00 |
| Each half hour after the first hour | $95.00 | $104.50 |

**Booking online is genuinely cheaper: $252 vs $319 inc GST, a $67 saving (21%)
on exactly the same hour.** Framed on the site as an incentive we pass on
because online booking costs less to schedule. This framing is correct under
the current card — it was briefly wrong in an earlier revision where the
call-out was $39, which made the two prices identical.

**Increments:** time after the first hour is billed in **half-hour** increments,
not hourly.

**Assumption to confirm:** remote work beyond the first hour is published as
$190 + GST in half-hour increments. Royce specified the half-hour rule for the
on-site path only.

## Superseded pricing (Aug 2026 — kept for reference)

| Service | Figure | Framing on the site |
|---|---|---|
| On-site, booked online | **$252 inc GST** | Fixed, one hour, no call-out on top. Inferred as an online-booking rate — see blockers |
| Ad-hoc on site | $298 + GST ($327.80 inc) | $100 + GST call-out plus $198 + GST/hr. Unchanged |
| Remote | $198 + GST ($217.80 inc) | No call-out. Unchanged |
| Business WiFi | $1,500 + GST | Simple site, hardware included, fixed price |
| Cybersecurity health check | **$500 inc GST** | Up to 5 users, fixed fee |
| Data cabling | **$150 + GST per outlet** | Indicative. ~$1,200 for a typical 8-outlet office. Cabinet, patch panel and switch quoted separately |
| VoIP install | **$100 + GST per handset** | So $500 + GST for 5 extensions |
| VoIP handset | **$350 + GST each** | Five-extension system = $2,250 + GST all up |
| Microsoft 365 migration | **$150 + GST per user** | **Softest number on the site.** Royce's own words were "too hard to give indicative pricing. Maybe $150 per user. Maybe..." — carried with heavy scoping language on 2 pages. Pull it on request |
| Cloud backup | **$10 + GST per user per month** | Servers and infrastructure quoted separately on recovery targets. GST treatment was unstated by Royce; published as ex-GST to match every other unmarked figure he supplied |

Managed IT deliberately still has **no from-price**. Monthly call plans for VoIP are
quoted alongside the install rather than published.


### Google Business Profile — prices to correct

Royce maintains GBP himself. Current site figures, converted to inc GST for the profile:

| GBP service | Set to | Note |
|---|---|---|
| On-site / technician attendance | **From $252** | Book-online rate. Already on the profile and correct |
| Remote IT support | **From $218** | $217.80 inc GST, first hour, no call-out |
| Cybersecurity health check | **From $500** | Up to 5 users |
| Business WiFi | **From $1,650** | $1,500 + GST |
| Data cabling | **From $165** | per outlet, $150 + GST |
| VoIP / phone systems | **From $2,475** | 5-extension system, $2,250 + GST |
| Microsoft 365 migration | **From $165** | per user, $150 + GST |
| Managed IT | **no price** | Quoted from requirements, never per seat |
| The other 5 cybersecurity services | **no price** | Only the health check has a fixed fee |

**Remove From $182 and From $310 wherever they appear** — both are old rates.


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

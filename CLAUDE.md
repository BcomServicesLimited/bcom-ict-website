# bcom ICT website — www.bcomservices.com

Static site for **bcom ICT** (trading name of Bcom Services Pty Ltd, ABN 92 636 893 108),
a business IT support company on the Gold Coast. This file is read automatically by
Claude Code. Read it before changing anything; `BUILD-STATUS.md` holds the detailed
project history and the reasoning behind each rule below.

**This repository is public, and Cloudflare publishes its root to the live site.**
Never commit customer names that are not already on the site, private contact
details, credentials, keys, or internal business figures. Non-site files are kept off
the live domain by rules at the top of `build/redirects.py` (`*.md`, `*.py`, `/build/`,
dotfiles). Any new internal file must match one of those patterns or it will be served.

## How the site is built

The HTML is **generated** — never edit it by hand.

| What | Where |
|---|---|
| Business facts, rates, suburbs, nav, footer, credentials | `build/site_data.py` |
| Shared components (`cards`, `cta`, `faq_block`, `related`, `map_embed`, …) | `build/layout.py` |
| One module per page, each exporting a `PAGE` dict | `build/pages/*.py` |
| Redirect rules (generates `_redirects`) | `build/redirects.py` |
| `llms.txt` / `llms-full.txt`, generated from the built pages | `build/llms.py` |
| Styles / progressive-enhancement JS | `assets/css/styles.css`, `assets/js/main.js` |

**Build** — Python 3.9+, standard library only, nothing to install:

```bash
python3 build/redirects.py   # only when redirect rules change
python3 build/build.py       # renders every page, sitemap.xml and llms files
```

**Deploy** — commit to `main` and push. Cloudflare Pages auto-deploys in about a
minute. There is no staging branch and no PR process.

**Never edit** the built `*.html`, `_redirects`, `sitemap.xml` or `llms*.txt` directly:
the next build overwrites them. Change the generator instead.

When `styles.css` or `main.js` changes, bump `ASSET_V` in `build/layout.py`, or
Cloudflare's edge serves the stale file.

## Build gates — the build fails if any of these trip

- **Link check** — every internal link must resolve.
- **Claims check** — blocks overstated credentials (see below).
- **SLA gate** — blocks any unscoped four-hour response promise, in HTML *and* JS.
- **Noindex gate** — only `404.html` and `thank-you.html` may carry noindex.

Do not weaken a gate to get a build through. Each has caught real published claims.
Fix the content.

## Content rules — none of these are optional

**Name.** Always "bcom ICT" — lowercase b. "Bcom IT Solutions" is the former name.

**Business-only.** No general residential or home computer work. The one exception
is mesh WiFi and network setup for a home office. Never add home-user copy.

**Response times.** The four-hour response is a **contracted target for managed and
SLA clients only**. Everyone else gets best effort: "usually the same business day".
Never publish a four-hour, one-hour or any other response figure as a general
promise. The SLA gate enforces this, but only for the patterns it knows.

**Hours.** 8:00am–5:00pm, Monday to Friday, Brisbane time. A digital assistant takes
calls after hours; calls are returned the next business day. After-hours on-call is
for managed and SLA clients only. Never write "24/7" or "open 24 hours".

**Location.** "Gold Coast QLD, Australia" and nothing narrower. **No street address,
no postcode, no coordinates** — in copy, schema or meta. The business attends the
customer. **Never state that there is no office** — the address is simply absent.
Suburb pages describe how quickly we attend, never distance from a base.

**Credentials — word these exactly.**
- The **company** is *aligned to* ISO/IEC 27001, 20000-1, 22301, the Essential Eight and
  ITIL 4. It is **not certified** in any of them. Never say "ISO certified".
- **Ollie** holds ITIL 4 Foundation and ISO/IEC 42001:2023 Lead Implementer (BSI).
  These are individual certifications. **Royce holds no listed certification** — do not
  attribute ITIL, or any other credential, to him.
- bcom ICT is **not** ACMA registered. Cabling is done by ACMA-registered cabling
  contractors.

**Team and resourcing.** Never state or imply how many people work at bcom ICT, and
never describe how work is resourced beyond "our technicians" and the cabling
contractors above.

**Clients.**
- The retail fit-out client (Pacific Fair and Chermside stores) is **never named**. Refer
  to them only as "a retail customer" or similar.
- Grow&Co Property Agents **may** be named — written permission given 3 Sept 2026 for
  the copy as published. A material rewrite of their case study needs fresh approval.
- Only **public** reviews may be quoted as testimonials. Never quote client email or
  private correspondence, and never publish a client's personal contact details.
- Attribute reviews to the business, not an individual, unless told otherwise.

**Numbers.** Rates live once in `RATES` in `site_data.py`, and the review count in
`BIZ["reviews"]`. Change them there, never by hand in a page. Never add `Review` or
`AggregateRating` schema: Google treats self-serving review markup as ineligible.

## Before you push

1. `python3 build/build.py` passes every gate.
2. Titles ≤ 60 characters, meta descriptions ≤ 160.
3. Anything visual checked in a browser at desktop and mobile widths.
4. Any new page has an `<p class="answer">` block — `llms.py` extracts it by class.

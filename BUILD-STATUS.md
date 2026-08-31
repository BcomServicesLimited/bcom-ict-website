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
| GBP category | Keep Computer repair service, reframe to business hardware. Add Computer security service. |
| Suburb pages | Rebuild 10, genuinely distinct content — not templated |
| ISO | **Aligned, NOT certified.** Never write "certified/compliant/accredited" for the org. |
| Credentials | All four confirmed held — cabler registration, PI + cyber + public liability, police checks + Blue Cards, Microsoft Partner |
| SLA | Draft P1–P4 matrix approved as-is |

### Wording rules that must not be broken
- Organisation: *"aligned to ISO/IEC 27001:2022 … not currently certified"*. Never "ISO certified".
- Individuals: Royce = ITIL 4 Foundation. Ollie = ISO/IEC 42001:2023 Lead Implementer, issued by BSI.
- Callback promise is **"within 4 business hours"** everywhere. Never "1 hour".
- Hours: phones answered 24/7, after hours by the AI operator, work actioned in business hours.
- No residential/home-user copy. Home-office WiFi and mesh is fine; general home computer repair is not.

---

## Chunks

Each chunk ends with a commit and a push. Tick as they land.

- [x] **Chunk 1 — Foundation** · repo, design system, generator, homepage
      Self-hosted Manrope + Inter, brand mark SVG derived from the logo, cropped
      logos, hero system, JSON-LD graph, `_headers`, `_redirects`, robots.txt.
- [ ] **Chunk 2 — Core service pages (6)**
      Managed IT · Business IT Support · Cybersecurity · Business WiFi ·
      Phone Systems · Cloud & Microsoft 365. Plus the Services hub.
- [ ] **Chunk 3 — Trust centre (8)**
      Trust centre hub · published SLA · ISO alignment · ITIL service model ·
      data handling & sovereignty · NDB guide · ransomware reporting · onboarding.
      **This is the differentiator — the depth layer nothing else on the Gold Coast has.**
- [ ] **Chunk 4 — Company & conversion (7)**
      About · Our team (Person schema + credentials) · Contact · Reviews ·
      Case studies · Pricing · Support.
- [ ] **Chunk 5 — Remaining services (~22)**
      Remote/on-site support, IT consulting, M365, Copilot, AI services, backup,
      networking, cabling, PBX brands, hardware, repair (business-framed).
- [ ] **Chunk 6 — Industries (8)** · incl. new professional-services page
- [ ] **Chunk 7 — Suburbs (10)** · distinct content per suburb, not templated
- [ ] **Chunk 8 — Guides (7)** · MSP buyer's guide, hacked, office move, NBN,
      IT support cost, managed vs break-fix, Essential Eight
- [ ] **Chunk 9 — Legal & utility** · privacy, terms, sitemap page, 404
- [ ] **Chunk 10 — LLM layer** · `llms.txt`, `llms-full.txt`, internal link mesh,
      og:image cards, IndexNow
- [ ] **Chunk 11 — Parity check & cutover** · 301 map, every old URL resolves,
      raw-curl crawl, schema validation, then repoint the domain

---

## Blocked / waiting on Royce

| Item | Needed for |
|---|---|
| **Search Console export** — 12 months, page-level, impressions + clicks. *Said "see attached" but no file came through.* | Chunk 11 — decides which of the 11 WiFi brand pages get consolidated vs kept |
| **ACMA cabler registration number** (the actual number) | Chunk 3 + cabling pages — the claim is confirmed, the number is what gets displayed |
| **Insurer names and cover limits** for PI / cyber / public liability | Chunk 3 |
| **Microsoft Partner designation** (which tier/solutions areas) | Chunk 3, Chunk 4 |
| Permission to name the national retail chain client | Chunk 4 case studies |
| Cloudflare: confirm **Block AI bots = OFF** and managed robots.txt disabled on the zone | Before go-live — silently 403s every AI crawler |
| Cloudflare Access on the `.pages.dev` staging domain | Before the site is publicly reachable |

---

## Notes

- Image library: 178 WebP files carried across from the old repo, 38 MB, all reusable.
- The old repo `BcomITSolutionsPROJECT` stays untouched as the live site and the rollback.
- Logo blue is **#004AAC**, sampled from the logo itself. The old design system used
  cyan `#00c8e0`, which never matched the logo — the new palette is anchored to the real one.
- The `><` mark from the logo is the brand device: section rules, list bullets, card
  icons, hero texture, favicon. `assets/logo/bcom-mark.svg`.

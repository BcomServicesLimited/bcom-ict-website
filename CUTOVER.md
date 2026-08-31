# Cutover runbook — bcom ICT

Everything below is either **a step Royce takes in a browser** or **a check to run
afterwards**. The build itself is done and the parity gate passes.

---

## Pre-flight (all verified 2026-08-31)

| Check | Result |
|---|---|
| Old sitemap URLs (82) resolve on the new site | **82/82** — 69 direct, 13 via single-hop 301 |
| Broken links, redirect loops, redirect chains | **0** |
| Legacy redirect sources from the old `_redirects` (91) | **all resolve** |
| Suburb pages rebuilt in chunk 7 are not redirected away | **confirmed** |
| Pages readable with no JavaScript executed | **98/98**, avg 1,006 words |
| JSON-LD present and valid on every page | **98/98** |
| Overstated ISO / ACMA / Microsoft-tier claims | **0** |
| AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) | **HTTP 200, full content** |

---

## Step 1 — Cloudflare Pages project

1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
2. Choose `BcomServicesLimited/bcom-ict-website`, production branch **`main`**.
3. **Build command:** leave empty. **Build output directory:** `/` (the repo root
   holds the built HTML — the generator is committed but does not run on Cloudflare).
4. Deploy. Note the `*.pages.dev` URL.

## Step 2 — lock the preview URL down

Put **Cloudflare Access** in front of the `.pages.dev` domain before anything else.
Without it, Google can index the preview as a complete duplicate of the site.

Cloudflare → **Zero Trust** → **Access** → **Applications** → add the `.pages.dev`
hostname → policy: allow your own email only.

## Step 3 — the two settings that silently break AI crawling

**Check both. They default to ON and they return 403 to every AI crawler.**

1. Zone `bcomservices.com` → **Security** → **Settings** / **Detection tools** →
   **Block AI bots** → set to **Do not block (allow crawlers)** → Save.
2. Same area → **Manage robots.txt** → **Disable robots.txt configuration** → Save.

This exact pair sabotaged businessflow.au before it was caught. The whole
LLM-first strategy is worthless if these are on.

Verify after saving:
```bash
curl -s -o /dev/null -w '%{http_code}\n' -A "GPTBot/1.2" https://www.bcomservices.com/
curl -s https://www.bcomservices.com/robots.txt | head -5
```
Expect `200` and *our* robots.txt, not a Cloudflare-generated one.

## Step 4 — cut the domain over

Both old and new are Cloudflare Pages projects, so this is a custom-domain move
rather than a DNS change. Downtime is measured in minutes.

1. **Old** Pages project → Custom domains → remove `www.bcomservices.com`.
2. **New** Pages project → Custom domains → add `www.bcomservices.com`.
3. Add `bcomservices.com` (apex) too — `_redirects` sends it to www.

**The old repo `BcomITSolutionsPROJECT` stays untouched.** Rollback is putting the
custom domain back on the old project.

## Step 5 — immediately after cutover

```bash
cd ~/bcom-ict-website
python3 build/verify_live.py          # parity check against the live domain
python3 indexnow_submit.py            # Bing/Yandex — do NOT run before cutover
```

Then in **Google Search Console**:
- Resubmit `https://www.bcomservices.com/sitemap.xml`
- Request indexing on: `/`, `/services`, `/managed-it-services-for-small-businesses-gold-coast`,
  `/it-support-and-services-gold-coast`, `/cybersecurity-services-gold-coast`,
  `/trust-centre`, `/service-levels-and-security`, `/pricing`

## Step 6 — watch for two weeks

- **Search Console → Pages**: coverage errors should stay near zero. Any spike in
  "Not found (404)" means a redirect was missed — send it to me.
- **Search Console → Performance**: a dip for 1–2 weeks is normal on a redesign.
  A dip that keeps going is not.
- **Google Business Profile**: the 36 rewritten services and the corrected name
  still need pasting in — see the strategy doc, section J.

---

## Still outstanding (not blocking cutover)

| Item | Where |
|---|---|
| Legal review of `/privacy-policy` and `/terms-and-conditions` | Both ported from the old site and updated; not lawyer-checked |
| Verify Cyber Security Act ransomware thresholds and the NDB small-business exemption | Two guides carry a visible amber "under review" banner until confirmed |
| Insurer names and cover limits | Currently written generically |
| Microsoft Partner Center check — is there a current Solutions Partner designation? | Site says "Microsoft Partner", which is safe either way |
| 12-month page-level Search Console export | The 9 WiFi brand consolidations were decided without it. All are reversible — the page can be rebuilt and the redirect removed |

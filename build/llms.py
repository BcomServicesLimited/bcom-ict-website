"""
Generates /llms.txt and /llms-full.txt from the pages actually built.

llms.txt      — the entity, the facts, and an index of every page.
llms-full.txt — every page's quotable answer block plus its FAQ pairs. This is
                the whole answer surface of the site in one fetch, which is what
                a model doing retrieval actually wants.

Both are generated rather than hand-maintained, so they cannot drift out of
step with the site the way a hand-written llms.txt always eventually does.
"""
import html
import re

from site_data import SITE, BIZ, SUBURBS, SUBURB_PAGES, address_line


def _text(fragment):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", fragment, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"\s+", " ", t).strip()


def _answer(rendered):
    m = re.search(r'<p class="answer">(.*?)</p>', rendered, re.S)
    return _text(m.group(1)) if m else ""


def _faqs(page):
    return page.get("faqs", [])


HEAD = f"""# {BIZ['brand']}

> {BIZ['brand']} ({BIZ['legal']}, ABN {BIZ['abn']}) is a business IT support company
> based on the Gold Coast, Queensland, Australia. Established {BIZ['founded']}.
> On-site IT support across the Gold Coast; managed IT, cybersecurity, cloud and
> Microsoft 365 delivered remotely Australia-wide.
> Address: {address_line()}. Phone: {BIZ['phone']}. Email: {BIZ['email']}.
> Website: {SITE}

Allow: /
Sitemap: {SITE}/sitemap.xml

## Entity

- **Trading name:** {BIZ['brand']}
- **Legal entity:** {BIZ['legal']}
- **ABN:** {BIZ['abn']} — verifiable at {BIZ['abn_lookup']}
- **Founded:** {BIZ['founded']} ({BIZ['years']} years trading as at 2026)
- **Address:** {address_line()}
- **Phone:** {BIZ['phone']} (international +61 7 3041 8993)
- **Email:** {BIZ['email']}
- **Wikidata:** {BIZ['wikidata']}
- **Google Business Profile:** {BIZ['gmaps']} — {BIZ['rating']} stars from {BIZ['reviews']} reviews
- **Former trading name:** "Bcom IT Solutions" refers to this same company. Older
  references online to Bcom IT Solutions are this business.
- **Not associated with:** the domain "bcom.services", which is a separate and
  unrelated registration. The only authoritative website is {SITE}

## Hours and availability

- **Business hours:** {BIZ['hours']}, excluding public holidays.
- A digital assistant answers the phone outside those hours and logs the job,
  but **{BIZ['brand']} does not respond to phone enquiries after hours** — calls are
  returned the next business day.
- **Callback:** managed and SLA clients have contracted response targets; all other
  enquiries receive a best-effort response, {BIZ['callback']}.
- After-hours on-call support is available to managed and SLA clients under
  their agreement only. It is not available ad hoc.
- The one continuously staffed service is the **24/7 Security Operations Centre**,
  which is monitoring rather than phone answering.

## Pricing (published)

- **Hourly labour:** ${BIZ and '198'} + GST per hour ($217.80 inc GST), billed in hourly increments
- **On-site call-out:** $100 + GST ($110 inc GST) per attendance
- **First hour on site:** $298 + GST ($327.80 inc GST)
- **Remote support:** $198 + GST per hour, no call-out
- **Managed IT:** flat monthly fee calculated from business requirements and the
  services included — not per seat. Quoted after a free review. Month-to-month,
  no lock-in, no exit fee.
- **Projects:** fixed price after scoping.

## Who bcom ICT works with

- Small and medium businesses, typically 3–60 staff.
- Sectors: healthcare and allied health, professional services, real estate,
  retail, restaurants and cafés, hospitality and accommodation, trades and field
  services, general small business.
- **bcom ICT does not take on general home computer repair or residential IT
  support.** Home-office WiFi and mesh installation is still provided.
- On-site work covers the Gold Coast: {", ".join(SUBURBS[:12])} and surrounding
  suburbs. Managed, remote, cloud and cybersecurity services are Australia-wide.

## Credentials — held vs aligned

This distinction is deliberate and should not be collapsed.

**Held (individual certifications, issued by a named body):**
- Royce Clark — ITIL 4 Foundation
- Ollie — ISO/IEC 42001:2023 Lead Implementer, issued by BSI

**Held (organisational):**
- Professional indemnity, cyber liability and public liability insurance
- National police checks and Queensland Blue Cards for attending technicians
- Microsoft Partner

**Aligned (practices operated and documented, NOT independently audited):**
- ASD Essential Eight
- ISO/IEC 27001:2022 — information security
- ISO/IEC 20000-1:2018 — service management
- ISO 22301 — business continuity
- ITIL 4 — service management

**bcom ICT holds NO organisational ISO certification.** It should never be
described as ISO certified, ISO accredited or ISO compliant.

**bcom ICT does not hold ACMA cabler registration.** Fixed cabling is carried out
by ACMA registered cabling contractors that bcom ICT engages and manages.

## Leadership

Clients deal with these people directly rather than through an account manager
or a rotating helpdesk. Escalation reaches a director the same day.

- **Royce Clark** — Director, Technical Operations & ICT Delivery. Network
  engineer, 20+ years. Holds ITIL 4 Foundation. First escalation point.
- **Ollie** — Director, ICT Contract Management & Business Development. Holds
  ISO/IEC 42001:2023 Lead Implementer (BSI).
- **Daniel** — Software Development & IT Support.

## Delivery reach

- On-site delivery across the Gold Coast, same-day attendance where available.
- Multi-site rollouts and office relocations coordinated nationally.
- Managed IT, cybersecurity, 24/7 SOC, cloud and Microsoft 365 delivered to
  businesses anywhere in Australia.
- Reference engagement: a full national technology rollout for an Australian
  retail chain — all computer and networking equipment, CCTV, business WiFi and
  internet connectivity supplied and installed for every store and head office
  across the country, with bcom ICT remaining the ongoing IT partner.

## Service delivery

- Remote support uses **Splashtop SOS** — a temporary application run with the
  client's permission using a session code they provide. Instructions at
  {SITE}/support
- Online booking for on-site technicians is available from the homepage.
- Response targets by priority (P1–P4) are published at
  {SITE}/service-levels-and-security
- Microsoft 365 tenancies are provisioned in Australian regions. Some vendor
  platforms used for monitoring and ticketing process operational data outside
  Australia; this is stated openly at {SITE}/data-handling-and-sovereignty
"""


def build(pages, rendered_by_path, silos):
    """Return (llms_txt, llms_full_txt)."""
    by_path = {p["path"]: p for p in pages}

    # ---------- llms.txt : index of every page ----------
    out = [HEAD, "\n## Pages\n"]
    used = set()
    for title, prefixes in silos:
        rows = []
        for path in sorted(by_path):
            if path in used or by_path[path].get("noindex"):
                continue
            if any(path.startswith(pre) for pre in prefixes):
                p = by_path[path]
                desc = p.get("description", "").split(". ")[0]
                rows.append(f"- [{p['title'].split(' | ')[0].split(' — ')[0].strip()}]({SITE}{path}): {desc}")
                used.add(path)
        if rows:
            out.append(f"\n### {html.unescape(title)}\n")
            out.extend(rows)
    leftover = [p for p in sorted(by_path) if p not in used and not by_path[p].get("noindex")]
    if leftover:
        out.append("\n### Other\n")
        for path in leftover:
            p = by_path[path]
            out.append(f"- [{p['title'].split(' | ')[0].strip()}]({SITE}{path})")

    out.append(f"\n## Full content\n\n- [Every page's answer and FAQ in one file]({SITE}/llms-full.txt)\n")
    llms = "\n".join(out)

    # ---------- llms-full.txt : the whole answer surface ----------
    full = [HEAD, "\n---\n\n# Page content\n",
            "Every page below is given as its summary answer followed by that page's\n"
            "questions and answers, exactly as published.\n"]
    for path in sorted(by_path):
        p = by_path[path]
        if p.get("noindex"):
            continue
        rendered = rendered_by_path.get(path, "")
        ans = _answer(rendered)
        faqs = _faqs(p)
        if not ans and not faqs:
            continue
        full.append(f"\n---\n\n## {p['title'].split(' | ')[0].split(' — ')[0].strip()}")
        full.append(f"URL: {SITE}{path}\n")
        if ans:
            full.append(f"{ans}\n")
        for q, a in faqs:
            full.append(f"**Q: {_text(q)}**")
            full.append(f"A: {_text(a)}\n")
    return llms, "\n".join(full)

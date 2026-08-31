"""
Shared page furniture. Every template lives here so header/footer/nav is a
single edit rather than 86. Output is plain static HTML — no client-side
rendering, because AI crawlers largely do not execute JavaScript.
"""
import json
from site_data import SITE, BIZ, NAV, FOOTER, SUBURBS, address_line

MARK = ('<span class="mark" aria-hidden="true"><svg viewBox="0 0 140 73" xmlns="http://www.w3.org/2000/svg">'
        '<path fill="currentColor" d="M0 0 L66 36.5 L0 73 L0 53 L29.8 36.5 L0 20 Z"/>'
        '<path fill="currentColor" d="M140 0 L74 36.5 L140 73 L140 53 L110.2 36.5 L140 20 Z"/>'
        '</svg></span>')

ASSET_V = "5"  # bump when styles.css or main.js changes — Cloudflare edge TTL otherwise serves stale


ROBOTS_OK = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">'
ROBOTS_NO = '<meta name="robots" content="noindex, follow">'


def head(p):
    url = SITE + p["path"]
    robots = ROBOTS_NO if p.get("noindex") else ROBOTS_OK
    preload = ""
    if p.get("hero_img"):
        preload = f'\n  <link rel="preload" as="image" href="/assets/img/{p["hero_img"]}" fetchpriority="high">'
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]}</title>
<meta name="description" content="{p["description"]}">
<link rel="canonical" href="{url}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BIZ['brand']}">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["description"]}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="AU-QLD">
<meta name="geo.placename" content="{BIZ['suburb']}, {BIZ['region']}">
<link rel="icon" href="/assets/logo/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/logo/favicon.webp">
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/manrope-800-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/inter-400-latin.woff2" crossorigin>{preload}
<link rel="stylesheet" href="/assets/css/styles.css?v={ASSET_V}">
{schema(p)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def local_business():
    return {
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": f"{SITE}/#localbusiness",
        "name": BIZ["brand"],
        "legalName": BIZ["legal"],
        "alternateName": ["Bcom IT Solutions", "Bcom Services Pty Ltd"],
        "url": SITE,
        "telephone": BIZ["phone_intl"],
        "email": BIZ["email"],
        "foundingDate": BIZ["founded"],
        "priceRange": "$$",
        "image": f"{SITE}/assets/logo/bcom-ict-logo.webp",
        "logo": f"{SITE}/assets/logo/bcom-ict-logo.webp",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": BIZ["street"],
            "addressLocality": BIZ["suburb"],
            "addressRegion": BIZ["state"],
            "postalCode": BIZ["postcode"],
            "addressCountry": "AU",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": BIZ["lat"], "longitude": BIZ["lon"]},
        "areaServed": [{"@type": "City", "name": s} for s in SUBURBS[:12]]
                      + [{"@type": "Country", "name": "Australia"}],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59",
        }],
        "sameAs": [BIZ["wikidata"], BIZ["gmaps"], BIZ["abn_lookup"]],
        "identifier": {"@type": "PropertyValue", "propertyID": "ABN", "value": BIZ["abn"]},
        # Frameworks the organisation works to. knowsAbout — NOT a certification
        # claim. bcom ICT is aligned to these standards, not certified to them.
        "knowsAbout": [
            "ASD Essential Eight", "ISO/IEC 27001:2022 information security management",
            "ISO/IEC 20000-1:2018 IT service management", "ISO/IEC 42001:2023 AI management systems",
            "ITIL 4 service management", "Australian Privacy Principles",
            "Notifiable Data Breaches scheme", "ASIC cyber resilience",
        ],
    }


def schema(p):
    graph = [local_business()]
    # A page can carry more than one Service node where the Google Business
    # Profile lists the same offering under two names in two categories — e.g.
    # "Office Network Cabling" and "Data Cabling". Each GBP service name must
    # map to a page, and the exact string is what makes the alignment work.
    svc_names = ([p["service"]] if p.get("service") else []) + list(p.get("also_service", []))
    for i, name in enumerate(svc_names):
        graph.append({
            "@type": "Service",
            "@id": f"{SITE}{p['path']}#service" + (f"-{i}" if i else ""),
            # Exact Google Business Profile service name, character for character.
            "name": name,
            "description": p["description"],
            "serviceType": name,
            "provider": {"@id": f"{SITE}/#localbusiness"},
            "areaServed": p.get("area", [{"@type": "City", "name": "Gold Coast"}]),
            "url": f"{SITE}{p['path']}",
        })
    if p.get("article"):
        # Guides get Article schema. These are the pages written to be cited —
        # a dated, attributed article is far more quotable than a bare page.
        graph.append({
            "@type": "Article",
            "@id": f"{SITE}{p['path']}#article",
            "headline": p.get("headline", p["h1"]),
            "description": p["description"],
            "url": f"{SITE}{p['path']}",
            "datePublished": p.get("published", "2026-08-31"),
            "dateModified": p.get("modified", "2026-08-31"),
            "inLanguage": "en-AU",
            "author": {"@id": f"{SITE}/#localbusiness"},
            "publisher": {"@id": f"{SITE}/#localbusiness"},
            "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE}{p['path']}"},
        })
    if p.get("faqs"):
        graph.append({
            "@type": "FAQPage",
            "@id": f"{SITE}{p['path']}#faq",
            "mainEntity": [{
                "@type": "Question", "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            } for q, a in p["faqs"]],
        })
    for person in p.get("people", []):
        node = {
            "@type": "Person",
            "@id": f"{SITE}{p['path']}#{person['slug']}",
            "name": person["name"],
            "jobTitle": person["role"],
            "worksFor": {"@id": f"{SITE}/#localbusiness"},
        }
        if person.get("photo"):
            node["image"] = f"{SITE}/assets/img/{person['photo']}"
        if person.get("credentials"):
            node["hasCredential"] = [{
                "@type": "EducationalOccupationalCredential",
                "name": c["name"],
                "credentialCategory": "certification",
                **({"recognizedBy": {"@type": "Organization", "name": c["issuer"]}}
                   if c.get("issuer") else {}),
            } for c in person["credentials"]]
        graph.append(node)
    if p.get("crumbs"):
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE}]
        for i, (label, href) in enumerate(p["crumbs"], start=2):
            items.append({"@type": "ListItem", "position": i, "name": label, "item": SITE + href})
        graph.append({"@type": "BreadcrumbList", "@id": f"{SITE}{p['path']}#crumbs", "itemListElement": items})
    doc = {"@context": "https://schema.org", "@graph": graph}
    return '<script type="application/ld+json">\n' + json.dumps(doc, indent=1, ensure_ascii=False) + '\n</script>'


def header(p):
    def nav_link(label, href):
        cur = ' aria-current="page"' if href == p["path"] else ""
        return f'<a href="{href}"{cur}>{label}</a>'

    links = "".join(nav_link(label, href) for label, href in NAV)
    mlinks = "".join(f'<a href="{href}">{label}</a>' for label, href in NAV)
    return f'''<div class="utility">
  <div class="wrap">
    <div class="utility-left">
      <span class="utility-open"><span class="dot"></span> Open 24/7 · phones answered</span>
      <span class="u-hide">{address_line()}</span>
    </div>
    <span class="u-hide">Callback {BIZ['callback']}</span>
  </div>
</div>
<header class="masthead">
  <div class="wrap">
    <a class="brand" href="/" aria-label="{BIZ['brand']} — home">
      <img src="/assets/logo/bcom-ict-logo.webp" alt="{BIZ['brand']}" width="185" height="30">
    </a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <div class="header-cta">
      <a class="header-phone" href="{BIZ['phone_href']}">{MARK} {BIZ['phone']}</a>
      <a class="btn btn--primary" href="/contact">Get a quote</a>
    </div>
    <button class="navtoggle" type="button" aria-expanded="false" aria-controls="mobilenav">
      <span class="burger" aria-hidden="true"><span></span><span></span><span></span></span> Menu
    </button>
  </div>
</header>
<div class="mobilenav" id="mobilenav" data-open="false">
  <div class="wrap">
    {mlinks}
    <a class="btn btn--primary" href="/contact">Get a quote</a>
    <a class="btn btn--ghost" href="{BIZ['phone_href']}">Call {BIZ['phone']}</a>
  </div>
</div>
'''


def crumbs(p):
    if not p.get("crumbs"):
        return ""
    items = '<li><a href="/">Home</a></li>'
    last = len(p["crumbs"]) - 1
    for i, (label, href) in enumerate(p["crumbs"]):
        items += (f'<li aria-current="page">{label}</li>' if i == last
                  else f'<li><a href="{href}">{label}</a></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>{items}</ol></div></nav>\n'


def cta(heading, body, primary=("Get a quote", "/contact")):
    return f'''<section class="cta section section--tight">
  <div class="wrap">
    <h2>{heading}</h2>
    <p class="lede">{body}</p>
    <div class="cta-actions">
      <a class="btn btn--white btn--lg" href="{primary[1]}">{primary[0]}</a>
      <a class="btn btn--onink btn--lg" href="{BIZ['phone_href']}">Call {BIZ['phone']}</a>
    </div>
  </div>
</section>
'''


def faq_block(faqs):
    if not faqs:
        return ""
    items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in faqs)
    return f'''<section class="section section--tight" id="faq">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Common questions</span><h2>Questions Gold Coast businesses ask us</h2></div>
    <div class="faq">{items}</div>
  </div>
</section>
'''


def footer(p):
    cols = ""
    for title, links in FOOTER.items():
        li = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in links)
        cols += f'<div><h4>{title}</h4><ul>{li}</ul></div>'
    reviewed = ""
    if p.get("reviewed"):
        reviewed = (f'<div class="wrap"><p class="reviewed">{MARK} Last updated: {p["reviewed"]} '
                    f'· Reviewed by the {BIZ["brand"]} team</p></div>')
    return f'''{reviewed}
<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="/assets/logo/bcom-ict-logo-white.webp" alt="{BIZ['brand']}" width="173" height="28">
        <p>Business IT support on the Gold Coast since {BIZ['founded']}. On-site across the Gold Coast, remote and managed support Australia-wide.</p>
        <ul style="margin-top:20px">
          <li><a href="{BIZ['phone_href']}">{BIZ['phone']}</a></li>
          <li><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
          <li>{address_line()}</li>
        </ul>
      </div>
      {cols}
    </div>
    <div class="foot-legal">
      <span>&copy; 2026 {BIZ['legal']} · ABN {BIZ['abn']} · trading as {BIZ['brand']}</span>
      <span class="links">
        <a href="/privacy-policy">Privacy</a>
        <a href="/terms-and-conditions">Terms</a>
        <a href="/trust-centre">Trust centre</a>
        <a href="/sitemap">Sitemap</a>
      </span>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js?v={ASSET_V}" defer></script>
</body>
</html>
'''


def hero(p):
    """Photographic hero. The image is a real <img> — the LCP element, with alt
    text and a preload hint — rather than a CSS background, which no crawler
    can see and no browser can preload."""
    kind = p.get("hero_kind", "page")
    if kind == "doc":
        return f'''<section class="hero hero--doc">
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <span class="eyebrow">{p.get("eyebrow", "Trust centre")}</span>
      <h1>{p["h1"]}</h1>
      <p class="lede">{p["lede"]}</p>
    </div>
  </div>
</section>
'''
    badge = ""
    if p.get("badge"):
        badge = f'<span class="hero-badge"><span class="dot"></span>{p["badge"]}</span>'
    trust = ""
    if p.get("trust"):
        li = "".join(f"<li>{MARK} {t}</li>" for t in p["trust"])
        trust = f'<ul class="hero-trust">{li}</ul>'
    actions = ""
    if p.get("actions"):
        actions = '<div class="hero-actions">' + "".join(
            f'<a class="btn btn--{s} btn--lg" href="{h}">{l}</a>' for l, h, s in p["actions"]) + "</div>"
    cls = "hero" if kind == "home" else "hero hero--page"
    return f'''<section class="{cls}">
  <div class="hero-media"><img src="/assets/img/{p["hero_img"]}" alt="{p["hero_alt"]}" width="1920" height="1080" fetchpriority="high" decoding="async"></div>
  <div class="hero-wash" aria-hidden="true"></div>
  <div class="wrap hero-inner">
    <div class="hero-copy">
      {badge}
      <h1>{p["h1"]}</h1>
      <p class="lede">{p["lede"]}</p>
      {actions}
      {trust}
    </div>
  </div>
</section>
'''


def render(p):
    return (head(p) + header(p) + hero(p) + crumbs(p)
            + f'<main id="main">\n{p["body"]}\n</main>\n' + footer(p))


# ---------------------------------------------------------------------------
# Content components. Pages stay content; markup lives here.
# ---------------------------------------------------------------------------

def cards(items, icon=True):
    """items: (title, href|None, blurb), or (title, blurb) for a plain card.
    A href makes the whole card a link."""
    out = ""
    for item in items:
        if len(item) == 2:
            (title, blurb), href = item, None
        else:
            title, href, blurb = item
        ic = f'<div class="card-icon">{MARK}</div>' if icon else ""
        if href:
            out += (f'<a class="card" href="{href}">{ic}<h3>{title}</h3><p>{blurb}</p>'
                    f'<span class="more">Learn more {MARK}</span></a>')
        else:
            out += f'<div class="card">{ic}<h3>{title}</h3><p>{blurb}</p></div>'
    return out


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{MARK}<span>{i}</span></li>" for i in items) + "</ul>"


def steps(items):
    return "".join(
        f'<div class="card"><div class="card-icon">{MARK}</div><h3>{n}. {t}</h3><p>{b}</p></div>'
        for n, (t, b) in enumerate(items, 1))


def related(items, heading="Related services"):
    """Cross-silo links. Every service page carries these — the internal link
    mesh is what carries authority around a static site."""
    li = "".join(f'<li>{MARK}<a href="{h}">{t}</a></li>' for t, h in items)
    return f'''<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Keep exploring</span><h2>{heading}</h2></div>
    <ul class="ticks ticks--2col">{li}</ul>
  </div>
</section>
'''


def photo(src, alt, caption=None):
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return (f'<figure class="photo"><img src="/assets/img/{src}" alt="{alt}" '
            f'width="1200" height="675" loading="lazy" decoding="async">{cap}</figure>')


def trust_note(text):
    """Surface-layer pointer down to the depth layer. Keeps frameworks off the
    marketing pages while still making them findable."""
    return f'<div class="tnote">{MARK}<p>{text}</p></div>'


def verify_note(text):
    """Amber banner for compliance content whose specifics have not yet been
    verified against the source. Deliberately visible: a confidently stated
    wrong threshold is worse for a client relying on it than no page at all."""
    return f'<div class="vnote"><strong>Under review</strong><p>{text}</p></div>'


def commitments(items):
    """A published commitment: what we do / what that means for you."""
    rows = "".join(
        f'<div class="commit"><h4>{h}</h4><p>{b}</p></div>' for h, b in items)
    return f'<div class="commits">{rows}</div>'


def creds(items):
    """items: (label, detail, kind) — kind is 'held', 'aligned' or 'note'.
    The held/aligned split is the whole point: it keeps certification claims
    and alignment claims visually distinct so they can never be read as one."""
    out = ""
    for label, detail, kind in items:
        out += (f'<div class="cred cred--{kind}"><span class="cred-tag">'
                f'{"Held" if kind == "held" else "Aligned" if kind == "aligned" else "Note"}</span>'
                f'<div><h4>{label}</h4><p>{detail}</p></div></div>')
    return f'<div class="credlist">{out}</div>'


def svc_body(*, answer, blocks):
    """Assemble a service page body from content blocks, alternating white and
    tinted sections. Each block is a dict:
        {"eyebrow","h2","sub","cards"|"ticks"|"steps"|"html", "icon","cols"}
    Keeps the 25 service pages as content rather than 25 copies of the markup.
    """
    out = [f'<section class="section">\n  <div class="wrap">\n'
           f'    <p class="answer">{answer}</p>\n  </div>\n</section>\n']
    for i, b in enumerate(blocks):
        tint = " section--mist" if i % 2 == 0 else ""
        head = ""
        if b.get("h2"):
            eb = f'<span class="eyebrow">{b["eyebrow"]}</span>' if b.get("eyebrow") else ""
            sub = f'<p>{b["sub"]}</p>' if b.get("sub") else ""
            head = f'<div class="section-head">{eb}<h2>{b["h2"]}</h2>{sub}</div>'
        if "cards" in b:
            inner = f'<div class="grid grid--{b.get("cols", 3)}">{cards(b["cards"], icon=b.get("icon", True))}</div>'
        elif "steps" in b:
            inner = f'<div class="grid grid--{b.get("cols", 4)}">{steps(b["steps"])}</div>'
        elif "ticks" in b:
            inner = ticks(b["ticks"])
        else:
            inner = b.get("html", "")
        out.append(f'<section class="section section--tight{tint}">\n  <div class="wrap">\n'
                   f'    {head}\n    {inner}\n  </div>\n</section>\n')
    return "\n".join(out)


def nearby(current_path, limit=5):
    """Cross-link the suburb pages to each other. A local page with no links to
    its neighbours is an orphan; the mesh is what carries authority between them."""
    from site_data import SUBURB_PAGES
    others = [(n, h) for n, h in SUBURB_PAGES if h != current_path][:limit]
    li = "".join(f'<li>{MARK}<a href="{h}">IT support in {n}</a></li>' for n, h in others)
    return f'''<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Nearby</span><h2>We cover the whole Gold Coast</h2>
    <p>On-site attendance across every suburb between Coomera and Coolangatta. Managed and remote support extends Australia-wide.</p></div>
    <ul class="ticks ticks--2col">{li}</ul>
  </div>
</section>
'''

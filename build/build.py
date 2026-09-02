#!/usr/bin/env python3
"""
bcom ICT static site generator.

Renders every module in build/pages/ to static HTML at the repo root, then
writes sitemap.xml. Committed deliberately: shared markup is one edit, and the
output stays plain static HTML that AI crawlers can read without executing JS.

    python3 build/build.py
"""
import importlib.util
import pathlib
import re
import sys
import datetime
import re as _re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
PAGES = BUILD / "pages"
sys.path.insert(0, str(BUILD))

import layout                      # noqa: E402
from site_data import SITE         # noqa: E402


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PAGE


STAGE_DIR = ROOT / "_staging"


def out_path(url_path, staging=False):
    """'/' -> index.html ; '/foo' -> foo.html  (Cloudflare Pages serves both
    /foo and /foo.html from foo.html, so URLs stay extensionless).

    Staging builds write to _staging/ rather than the repo root. A staging build
    sets noindex on every page; if that ever overwrote the production files and
    got committed, the live site would deindex itself. Separate directories make
    that impossible rather than merely unlikely."""
    base = STAGE_DIR if staging else ROOT
    return base / ("index.html" if url_path == "/" else url_path.lstrip("/") + ".html")


STAGING_NOINDEX = ('<meta name="robots" content="noindex, nofollow">\n'
                   '<!-- STAGING BUILD. Not for production: noindex is set and every URL is\n'
                   '     rewritten to a base path. Run build.py with no flags for production. -->\n')


def stage(html, base):
    """Rewrite a production build for a staging host served from a sub-path,
    and stop search engines indexing it as a duplicate of the live site."""
    html = html.replace('<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">',
                        STAGING_NOINDEX.rstrip())
    # Root-relative URLs -> base-prefixed. Leaves tel:, mailto: and absolute URLs alone.
    html = _re.sub(r'(href|src)="/(?!/)', lambda m: f'{m.group(1)}="{base}/', html)
    # Extensionless page links need .html on a static host with no rewrite rules.
    def add_ext(m):
        url = m.group(2)
        if url.rstrip('/') in ('', base) or '.' in url.rsplit('/', 1)[-1]:
            return m.group(0)
        return f'{m.group(1)}="{url}.html"'
    html = _re.sub(r'(href)="(' + _re.escape(base) + r'/[^"#?]*)"', add_ext, html)
    html = html.replace(f'href="{base}/"', f'href="{base}/index.html"')
    return html


def main(staging_base=None):
    pages, rendered = [], {}
    for f in sorted(PAGES.glob("*.py")):
        if f.name.startswith("_"):
            continue
        p = load(f)
        dest = out_path(p["path"], bool(staging_base))
        dest.parent.mkdir(parents=True, exist_ok=True)
        out = layout.render(p)
        rendered[p["path"]] = out
        if staging_base:
            out = stage(out, staging_base)
        dest.write_text(out, encoding="utf-8")
        pages.append(p)
        print(f"  {p['path']:<62} {dest.stat().st_size/1024:6.1f} KB")

    if staging_base:
        import shutil
        for extra in ("assets", "favicon.ico", "favicon.png"):
            src = ROOT / extra
            if src.exists():
                dst = STAGE_DIR / extra
                if dst.exists():
                    shutil.rmtree(dst) if dst.is_dir() else dst.unlink()
                shutil.copytree(src, dst) if src.is_dir() else shutil.copy2(src, dst)
        (STAGE_DIR / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
        (STAGE_DIR / ".nojekyll").write_text("")
        for f in ("llms.txt", "llms-full.txt"):
            if (ROOT / f).exists():
                shutil.copy2(ROOT / f, STAGE_DIR / f)
        print(f"\nSTAGING build in {STAGE_DIR}/ — production files untouched")
        return

    html_sitemap(pages)
    pages.append({"path": "/sitemap", "priority": "0.3",
                  "title": "Sitemap", "description": "Every page on the site."})

    import llms as llms_mod
    a, b = llms_mod.build(pages, rendered, SILOS)
    (ROOT / "llms.txt").write_text(a, encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(b, encoding="utf-8")
    print(f"  {'/llms.txt':<62} {len(a)/1024:6.1f} KB  (generated)")
    print(f"  {'/llms-full.txt':<62} {len(b)/1024:6.1f} KB  (generated)")

    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{SITE}{p['path']}</loc><lastmod>{today}</lastmod>"
        f"<priority>{p.get('priority', '0.7')}</priority></url>"
        for p in sorted(pages, key=lambda x: x["path"])
        if not p.get("noindex"))
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n',
        encoding="utf-8")

    print(f"\n{len(pages)} pages + sitemap.xml")
    check(pages)


# Groups for the human-readable sitemap. First matching prefix wins, so order
# matters. Anything unmatched falls into "More".
SILOS = [
    ("Support &amp; managed IT", ("/managed-it-services", "/it-support-and-services", "/remote-it-support",
                                  "/on-site-technical", "/hardware-software", "/it-consulting",
                                  "/it-needs-assessment", "/office-it-relocation", "/support")),
    ("Cybersecurity", ("/cybersecurity", "/security-operations", "/cyber-incident", "/essential-eight",
                       "/asic-cyber", "/virus-and-malware")),
    ("Cloud, Microsoft 365 &amp; AI", ("/cloud-computing", "/microsoft-365", "/microsoft-copilot",
                                       "/artificial-intelligence", "/ai-", "/iso-42001", "/data-backup")),
    ("Networks &amp; WiFi", ("/business-wifi", "/computer-networking", "/network-", "/mesh-network",
                             "/ubiquiti", "/aruba", "/wifi-range", "/router-and-modem",
                             "/home-wifi")),
    ("Phones &amp; telecommunications", ("/business-phone", "/voip-", "/pabx-", "/phone-line",
                                         "/nbn-internet", "/telecommunications")),
    ("Hardware &amp; repair", ("/on-site-computer-repair", "/os-troubleshooting", "/performance-optimisation",
                               "/hardware-procurement", "/software-installation", "/software-recommendations",
                               "/technology-procurement", "/computer-repairs")),
    ("Industries", ("/industries", "/it-support-small-business", "/it-support-healthcare",
                    "/it-support-professional", "/it-support-real-estate", "/it-support-retail",
                    "/it-support-restaurants", "/it-support-hospitality", "/it-support-trades")),
    ("Gold Coast suburbs", ("/it-support-surfers", "/it-support-southport", "/it-support-broadbeach",
                            "/it-support-robina", "/it-support-burleigh", "/it-support-varsity",
                            "/it-support-palm-beach", "/it-support-nerang", "/it-support-helensvale",
                            "/it-support-coomera")),
    ("Guides", ("/how-to-choose", "/what-to-do-when-hacked", "/it-support-cost", "/managed-it-vs",
                "/business-computer-replacement", "/office-move", "/business-nbn-guide")),
    ("Trust centre", ("/trust-centre", "/service-levels", "/iso-alignment", "/how-we-work",
                      "/data-handling", "/notifiable-data-breach", "/ransomware-reporting",
                      "/onboarding-")),
    ("Company", ("/about", "/our-team", "/contact", "/reviews", "/case-studies", "/pricing",
                 "/services", "/privacy-policy", "/terms-and-conditions", "/sitemap", "/")),
]


def html_sitemap(pages):
    """Render the human-readable sitemap from the pages actually built, so it
    can never fall out of step with the site."""
    import layout
    by_path = {p["path"]: p for p in pages}
    used, groups = set(), []
    for title, prefixes in SILOS:
        items = []
        for path in sorted(by_path):
            if path in used:
                continue
            if any(path.startswith(pre) for pre in prefixes) or path == "/" and "/" in prefixes:
                items.append(path)
                used.add(path)
        if items:
            groups.append((title, items))
    leftover = sorted(set(by_path) - used)
    if leftover:
        groups.append(("More", leftover))

    def label(path):
        p = by_path[path]
        t = p["title"].split(" | ")[0].split(" — ")[0].strip()
        return t

    cols = ""
    for title, items in groups:
        li = "".join(f'<li>{layout.MARK}<a href="{h}">{label(h)}</a></li>' for h in items)
        cols += f'<div class="silo"><h4>{title}</h4><ul class="ticks">{li}</ul></div>'

    page = {
        "path": "/sitemap", "priority": "0.3",
        "title": "Sitemap | bcom ICT",
        "description": f"Every page on the bcom ICT website — {len(pages) + 1} pages covering business IT services, industries, Gold Coast suburbs, guides and the trust centre.",
        "hero_kind": "doc", "eyebrow": "Sitemap",
        "h1": "Every page on this site",
        "lede": f"All {len(pages) + 1} pages, grouped. Generated from the site itself, so it cannot fall out of date.",
        "crumbs": [("Sitemap", "/sitemap")],
        "reviewed": "August 2026",
        "body": ('<section class="section section--tight"><div class="wrap">'
                 '<div class="silos" style="margin-top:0">' + cols + '</div></div></section>'),
    }
    (ROOT / "sitemap.html").write_text(layout.render(page), encoding="utf-8")
    print(f"  {'/sitemap':<62} {(ROOT / 'sitemap.html').stat().st_size/1024:6.1f} KB  (generated)")


def check(pages):
    """Every internal link either resolves to a built page or is still to come.
    Run on every build so a typo never quietly becomes a 404 at cutover."""
    import re
    built = {p["path"] for p in pages}
    missing_img, pending = set(), {}
    for f in ROOT.glob("*.html"):
        s = f.read_text(encoding="utf-8")
        for src in re.findall(r'src="/assets/([^"]+)"', s):
            if not (ROOT / "assets" / src.split("?")[0]).exists():
                missing_img.add(src)
        for h in re.findall(r'href="(/[^"#?]*)"', s):
            if h.startswith("/assets"):
                continue
            if h not in built:
                pending.setdefault(h, set()).add(f.name)
    if missing_img:
        print("\n!! MISSING IMAGES:")
        for m in sorted(missing_img):
            print("   ", m)
    if pending:
        print(f"\n{len(pending)} links point at pages not built yet "
              f"(expected until chunk 9 — must be zero before cutover)")
    if not missing_img and not pending:
        print("\nlink check: all internal links resolve")
    claims()


# Claims that would overstate what bcom ICT holds. Confirmed 2026-08-31:
# no organisational ISO certification, no ACMA cabler registration (cabling is
# subcontracted), and "Silver Partner" is a retired Microsoft tier.
BANNED = [
    (r'ISO[\s/A-Z0-9:-]{0,20}\bcertified\b', 'implies organisational ISO certification'),
    (r'\bISO[- ]?(compliant|accredited)\b', 'ISO compliant/accredited is never accurate'),
    (r'bcom ICT is ACMA', 'bcom ICT holds no cabler registration'),
    (r'\ban ACMA registered cabler\b', 'singular implies bcom ICT holds it'),
    (r'\b(Silver|Gold) Partner\b', 'retired Microsoft tier'),
]
# Sentences that legitimately contain the words while denying the claim.
SAFE = ('not certified', 'not currently certified', 'no organisational iso',
        'holds no organisational', 'not describe', 'does not make',
        'is bcom ict iso certified?', "doesn't that make",
        'not iso certified', 'nobody can', 'retired', 'no formal certification')


# The contracted 4-hour response target applies to managed / SLA clients ONLY.
# Ad-hoc clients get a best-effort response. Publishing the 4-hour figure as a
# general promise commits us to an SLA nobody has signed, so the build refuses
# it unless the surrounding text scopes it to a contracted client.
SLA_SCOPE = ('managed', 'sla', 'contracted', 'agreement', 'under their')


def _strip_tags(html):
    """The gate matches on prose, not markup: a claim split across <dt>/<dd>
    reads as one promise to a human and to a crawler, and used to slip the
    gate because the gap pattern excluded "<"."""
    return re.sub(r"<[^>]+>", " ", html)


def sla_gate():
    hits = []
    for f in ROOT.glob("*.html"):
        t = _strip_tags(f.read_text(encoding="utf-8"))
        # Only a response/callback promise matters here. "four hours a week" and
        # "four days instead of four hours" are not commitments.
        pats = (r'(callback|call back|respond(?:s|ed)?|response|come back to you|'
                r'get back to you|reply|returned)[^.]{0,90}?\b(4|four)[- ](business )?hours?',
                r'\b(4|four)[- ]hour\b[^.]{0,40}?(response|callback|sla|target)')
        for pat in pats:
          for m in re.finditer(pat, t, re.I):
            # Tight window on purpose. A page may legitimately discuss SLAs
            # several paragraphs away from an unscoped promise; only scoping in
            # the same breath actually qualifies the claim for a reader.
            ctx = t[max(0, m.start() - 220):m.end() + 220].lower()
            if any(w in ctx for w in SLA_SCOPE):
                continue
            hits.append((f.name, t[max(0, m.start() - 70):m.end() + 40].strip()))
    if hits:
        print("\n!! UNSCOPED 4-HOUR RESPONSE PROMISE — this is a contracted target,")
        print("   not a general one. Scope it to managed / SLA clients or remove it:")
        for f, ctx in hits:
            print(f"   {f}: ...{' '.join(ctx.split())}...")
        raise SystemExit(1)
    print("SLA gate: the 4-hour response target is scoped to contracted clients only")


def claims():
    import re
    hits = []
    for f in ROOT.glob("*.html"):
        t = f.read_text(encoding="utf-8")
        for pat, why in BANNED:
            for m in re.finditer(pat, t, re.I):
                ctx = t[max(0, m.start() - 240):m.end() + 240].lower()
                if any(sf in ctx for sf in SAFE):
                    continue
                # A question is not a claim. "Is bcom ICT ISO certified?" is a
                # legitimate heading; what matters is the answer beneath it.
                if "?" in t[m.end():m.end() + 90]:
                    continue
                hits.append((f.name, m.group(0), why))
    if hits:
        print("\n!! OVERSTATED CLAIMS — fix before publishing:")
        for f, txt, why in hits:
            print(f"   {f}: {txt!r} — {why}")
    else:
        print("claims check: no overstated certification or credential claims")
    sla_gate()
    noindex_gate()


# Pages that are meant to carry noindex. Anything else carrying it in a
# production build is a mistake serious enough to stop the build.
NOINDEX_OK = {"404.html", "thank-you.html"}


def noindex_gate():
    leaked = [f.name for f in ROOT.glob("*.html")
              if f.name not in NOINDEX_OK and "noindex" in f.read_text(encoding="utf-8")]
    if leaked:
        print("\n!! ABORT — production build contains noindex pages:")
        for f in leaked:
            print("   ", f)
        print("   This would deindex the live site. Rebuild without --staging.")
        raise SystemExit(1)
    print("noindex gate: production build is indexable")


if __name__ == "__main__":
    base = None
    if "--staging" in sys.argv:
        base = sys.argv[sys.argv.index("--staging") + 1].rstrip("/")
        print(f"STAGING build — base path {base}, noindex on every page\n")
    main(base)

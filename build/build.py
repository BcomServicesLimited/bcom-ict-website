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


def out_path(url_path):
    """'/' -> index.html ; '/foo' -> foo.html  (Cloudflare Pages serves both
    /foo and /foo.html from foo.html, so URLs stay extensionless)."""
    return ROOT / ("index.html" if url_path == "/" else url_path.lstrip("/") + ".html")


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
    pages = []
    for f in sorted(PAGES.glob("*.py")):
        if f.name.startswith("_"):
            continue
        p = load(f)
        dest = out_path(p["path"])
        dest.parent.mkdir(parents=True, exist_ok=True)
        out = layout.render(p)
        if staging_base:
            out = stage(out, staging_base)
        dest.write_text(out, encoding="utf-8")
        pages.append(p)
        print(f"  {p['path']:<62} {dest.stat().st_size/1024:6.1f} KB")

    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{SITE}{p['path']}</loc><lastmod>{today}</lastmod>"
        f"<priority>{p.get('priority', '0.7')}</priority></url>"
        for p in sorted(pages, key=lambda x: x["path"]))
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n',
        encoding="utf-8")

    print(f"\n{len(pages)} pages + sitemap.xml")
    check(pages)


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


if __name__ == "__main__":
    base = None
    if "--staging" in sys.argv:
        base = sys.argv[sys.argv.index("--staging") + 1].rstrip("/")
        print(f"STAGING build — base path {base}, noindex on every page\n")
    main(base)

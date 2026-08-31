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


def main():
    pages = []
    for f in sorted(PAGES.glob("*.py")):
        if f.name.startswith("_"):
            continue
        p = load(f)
        dest = out_path(p["path"])
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(layout.render(p), encoding="utf-8")
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


if __name__ == "__main__":
    main()

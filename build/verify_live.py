#!/usr/bin/env python3
"""
Post-cutover parity check against the live domain.

Fetches every URL from the previous site's sitemap plus every legacy redirect
source, and reports anything that does not end at a real page.

    python3 build/verify_live.py
"""
import concurrent.futures as cf
import pathlib
import re
import urllib.request

SITE = "https://www.bcomservices.com"
OLD = pathlib.Path.home() / "BcomITSolutionsPROJECT"


def head(path):
    req = urllib.request.Request(SITE + path, method="HEAD",
                                 headers={"User-Agent": "bcom-parity-check/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return path, r.status, r.url
    except Exception as e:
        return path, getattr(e, "code", 0), str(e)[:60]


def main():
    paths = set(re.findall(r"<loc>https://www\.bcomservices\.com(/[^<]*)</loc>",
                           (OLD / "sitemap.xml").read_text()))
    for line in (OLD / "_redirects").read_text().split("\n"):
        p = line.strip().split()
        if len(p) >= 2 and p[0].startswith("/") and p[0] != "/*.html":
            paths.add(p[0])

    bad = []
    with cf.ThreadPoolExecutor(8) as ex:
        for path, status, final in ex.map(head, sorted(paths)):
            if status not in (200,):
                bad.append((path, status, final))

    print(f"checked {len(paths)} legacy URLs against {SITE}")
    if bad:
        print(f"\n{len(bad)} did not resolve:")
        for p, s, f in bad:
            print(f"  {s}  {p}  -> {f}")
    else:
        print("all legacy URLs resolve. Parity confirmed.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Submit the sitemap's URLs to IndexNow (Bing, Yandex, Seznam and others).

    python3 indexnow_submit.py            # submit everything in sitemap.xml
    python3 indexnow_submit.py /pricing   # submit specific paths

Google does not use IndexNow, so this complements rather than replaces
requesting indexing in Search Console.
"""
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
HOST = "www.bcomservices.com"
SITE = f"https://{HOST}"
KEY = next(ROOT.glob("[0-9a-f]" * 32 + "*.txt")).stem


def urls():
    if len(sys.argv) > 1:
        return [SITE + a if a.startswith("/") else a for a in sys.argv[1:]]
    return re.findall(r"<loc>(.*?)</loc>", (ROOT / "sitemap.xml").read_text())


def main():
    u = urls()
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": f"{SITE}/{KEY}.txt",
        "urlList": u,
    }).encode()
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow", data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req) as r:
            print(f"IndexNow: HTTP {r.status} — submitted {len(u)} URLs")
    except urllib.error.HTTPError as e:
        print(f"IndexNow: HTTP {e.code} — {e.read().decode()[:200]}")


if __name__ == "__main__":
    main()

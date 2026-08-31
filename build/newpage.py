"""
Service-page writer. Turns a content spec into a real page module in
build/pages/. Used for the service pages, which share one structure while
keeping their content bespoke.

    from newpage import emit
    emit("slug", dict(path=..., service=..., blocks=[...], faqs=[...]))

The generated module is the source of truth and is committed — this is a
one-shot writer, not a runtime dependency.
"""
import pathlib
import pprint

ROOT = pathlib.Path(__file__).resolve().parent


def emit(f, d):
    body = (f"    \"body\": svc_body(answer={d['answer']!r},\n"
            f"                     blocks={pprint.pformat(d['blocks'], width=108, indent=8)})\n"
            f"            + faq_block(FAQS)\n"
            f"            + related({pprint.pformat(d['related'], width=108, indent=8)})\n"
            f"            + cta({d['cta'][0]!r}, {d['cta'][1]!r}),\n")
    src = ("from layout import cta, faq_block, related, svc_body\n\n"
           f"FAQS = {pprint.pformat(d['faqs'], width=200, indent=4)}\n\n"
           "PAGE = {\n"
           f"    \"path\": {d['path']!r},\n    \"priority\": {d.get('pri', '0.75')!r},\n"
           + (f"    \"service\": {d['service']!r},\n" if d.get("service") else "")
           + (f"    \"also_service\": {d['also_service']!r},\n" if d.get("also_service") else "")
           + f"    \"title\": {d['title']!r},\n"
           f"    \"description\": {d['desc']!r},\n    \"hero_img\": {d['img']!r},\n    \"hero_alt\": {d['alt']!r},\n"
           f"    \"h1\": {d['h1']!r},\n    \"lede\": {d['lede']!r},\n"
           "    \"actions\": [(\"Get a quote\", \"/contact\", \"white\"), (\"Call 07 3041 8993\", \"tel:+61730418993\", \"onink\")],\n"
           f"    \"trust\": {d['trust']!r},\n    \"crumbs\": {d['crumbs']!r},\n"
           "    \"faqs\": FAQS,\n    \"reviewed\": \"August 2026\",\n" + body + "}\n")
    (ROOT / "pages" / f"{f}.py").write_text(src)
    print("wrote", f)

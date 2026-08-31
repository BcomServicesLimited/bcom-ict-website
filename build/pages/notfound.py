from layout import MARK, cta, ticks

POPULAR = [
    ("Business IT Support", "/it-support-and-services-gold-coast"),
    ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
    ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
    ("Business WiFi Installation", "/business-wifi-gold-coast"),
    ("Business Phone Systems", "/business-phone-systems-gold-coast"),
    ("Pricing", "/pricing"),
    ("All services", "/services"),
    ("Every page on this site", "/sitemap"),
]

PAGE = {
    "path": "/404",
    "priority": "0.1",
    "noindex": True,
    "title": "Page not found | bcom ICT",
    "description": "That page doesn't exist. Find what you were looking for, or call bcom ICT on 07 3041 8993.",
    "hero_kind": "doc",
    "eyebrow": "404",
    "h1": "That page doesn't exist",
    "lede": "Either it moved, or the link was wrong. Here's where most people are heading.",
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    {ticks([f'<a href="{h}">{t}</a>' for t, h in POPULAR])}
    <p style="margin-top:32px">If you followed a link from our own site and landed here, we'd genuinely like
    to know — <a href="mailto:support@bcomservices.com">support@bcomservices.com</a>. It means something is
    broken and we'd rather fix it than have the next person hit it too.</p>
  </div>
</section>

{cta("Rather just talk to someone?",
     "Call 07 3041 8993 — returned during business hours, Monday to Friday.")}
''',
}

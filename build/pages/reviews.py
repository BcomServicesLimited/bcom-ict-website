from layout import MARK, cta, faq_block, ticks, related, trust_note
from site_data import BIZ

# Real reviews carried across from the existing site's public Google profile.
# Do not add to this list without a genuine, attributable review.
QUOTES = [
    ("bcom ICT fixed our office network the same day we called. Professional, fast and fairly priced. Highly recommend for any Gold Coast business.", "Michael T. · Robina"),
    ("Set up our entire VoIP phone system for our Southport office. Very knowledgeable and explained everything clearly.", "David R. · Southport"),
]

quotes = "".join(
    f'<figure class="quote"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div>'
    f'<blockquote>“{q}”</blockquote><cite>{who}</cite></figure>' for q, who in QUOTES)

FAQS = [
    ("How is bcom ICT rated?",
     "bcom ICT holds a 5.0 star rating from 24 verified reviews on its Google Business Profile as at August 2026. Every review is from a real customer and the full set is public on Google — the reviews quoted on this page are a sample, not a curated selection with the rest hidden."),
    ("Are these reviews real?",
     "Yes. They come from bcom ICT's public Google Business Profile, where anyone can read all of them without going through us. We don't publish testimonials that can't be traced back to a verifiable source, which is why there are fewer quotes on this page than on most IT company websites."),
    ("Why aren't there more reviews for a business trading since 2011?",
     "We've never systematically asked for them. Most of our work comes from referrals and from clients who've been with us for years, and it took us a long time to start requesting reviews at all. Twenty-four honest ones over a long period is a fair reflection of a business that has never run campaigns."),
    ("Can I speak to an existing client before engaging you?",
     "Yes. Ask and we'll arrange a reference call with a client in a similar sector or of a similar size. It's a more useful signal than any review, and we'd rather you did it."),
]

PAGE = {
    "path": "/reviews",
    "priority": "0.7",
    "title": "Reviews — 5.0 Stars from Gold Coast Businesses | bcom ICT",
    "description": "bcom ICT is rated 5.0 from 24 verified Google reviews. Read what Gold Coast businesses say about our IT support, networks and phone systems.",
    "hero_kind": "doc",
    "eyebrow": "About",
    "h1": "What Gold Coast businesses say",
    "lede": "5.0 stars from 24 verified Google reviews. The full set is public on Google — these are a sample, not a shortlist with the rest hidden.",
    "crumbs": [("About", "/about"), ("Reviews", "/reviews")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT holds a 5.0 star rating from 24 verified reviews on its Google Business
    Profile as at August 2026. Reviews come from Gold Coast businesses across IT support, networking, phone
    systems and cybersecurity work. The full set is publicly readable on Google.</p>

    <div class="quotes">{quotes}</div>

    <p><a class="btn btn--ghost" href="{BIZ['gmaps']}" rel="nofollow">Read every review on Google {MARK}</a></p>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>Why there aren't fifty of them</h2>
    <p style="margin-top:16px">A business trading since 2011 could reasonably be expected to have more
    reviews than 24, and it's a fair thing to notice. The honest reason is that we never systematically asked
    for them. Most of our work has come from referrals and from clients who've simply been with us for years,
    and requesting reviews is something we started doing late.</p>
    <p style="margin-top:16px">We'd rather have 24 real ones than pad the number. If you want a stronger
    signal than a review, ask us for a reference call with a client of a similar size or in your sector —
    we'll arrange it.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Worked with us? A review takes about a minute</h2>
    <p style="margin-top:16px">bcom ICT is a Gold Coast business that grows on word of mouth. We don't run ad campaigns and we don't
    cold-call — almost every new client finds us through Google, and reviews from businesses like yours are
    the single biggest reason they pick up the phone.</p>
    <p style="margin-top:16px">If we've looked after your IT, networks, phones or security, a short review
    describing what we actually did helps other Gold Coast operators find honest local support.</p>
    <p style="margin-top:24px"><a class="btn btn--primary" href="{BIZ['gmaps']}" rel="nofollow">Write a review on Google</a></p>

    {trust_note('Reviews are one signal. <a href="/service-levels-and-security">Our published service levels</a> and <a href="/trust-centre">trust centre</a> are the ones you can hold us to.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Case studies", "/case-studies"),
  ("About bcom ICT", "/about"),
  ("Our team", "/our-team"),
  ("Published service levels", "/service-levels-and-security"),
  ("Trust centre", "/trust-centre"),
  ("Contact us", "/contact"),
], heading="More")}

{cta("See whether we'd suit you",
     "The free systems review is the fastest way to find out — and you keep the report either way.")}
''',
}

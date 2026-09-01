from layout import booking_embed, MARK, cta, faq_block
from site_data import BIZ

SERVICES = [
    ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast",
     "Someone looking after your IT every day, for a flat monthly fee. Monitoring, helpdesk, updates and backups. Month-to-month, no lock-in."),
    ("Business IT Support", "/it-support-and-services-gold-coast",
     "Something's broken and you need it fixed. Same-day on-site visits across the Gold Coast, or remote in minutes."),
    ("Cybersecurity", "/cybersecurity-services-gold-coast",
     "Protecting your business from the things that actually happen — email scams, ransomware, staff accounts getting taken over."),
    ("Business WiFi & Networks", "/business-wifi-gold-coast",
     "WiFi that works in every corner of your building, with your guests kept separate from your business systems."),
    ("Phone Systems", "/business-phone-systems-gold-coast",
     "Cloud phone systems and traditional PBX. We install both, and we still support the older systems most providers have walked away from."),
    ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast",
     "Email, files and Teams set up properly and kept secure — with your data in Australia."),
]

WHY = [
    ("We answer the phone", "Day, night, weekend or public holiday, a call to bcom ICT gets answered. Out of hours it's our AI operator taking the details, and we come back to you in business hours — usually the same business day."),
    ("We fix causes, not symptoms", "If the same fault keeps coming back, that's our problem to solve — not a new invoice every time. Chasing root causes is the difference between managed IT and a repair bill."),
    ("We're local, and we come to you", "We're based on Ferny Avenue in Surfers Paradise. Same-day on-site visits across the Gold Coast, and remote support anywhere in Australia."),
    ("No lock-in contracts", "Our managed IT is month-to-month. If we're not worth the money, you should be able to leave — and you should get your documentation and passwords on the way out."),
]

STEPS = [
    ("Have a chat", "A short conversation about what's working, what isn't, and what it's costing you. No charge, no obligation."),
    ("We look at what you've got", "A proper review of your systems, security and backups. You get a plain-English report with what we'd fix first."),
    ("We take it on", "We document everything, fix the urgent things, and take over the day-to-day. Most businesses are fully onboarded inside 30 days."),
]

cards = "".join(
    f'<a class="card" href="{href}"><div class="card-icon">{MARK}</div>'
    f'<h3>{name}</h3><p>{blurb}</p>'
    f'<span class="more">Learn more {MARK}</span></a>'
    for name, href, blurb in SERVICES)

why = "".join(f'<div class="card"><h3>{h}</h3><p>{b}</p></div>' for h, b in WHY)

steps = "".join(
    f'<div class="card"><div class="card-icon">{MARK}</div><h3>{i}. {h}</h3><p>{b}</p></div>'
    for i, (h, b) in enumerate(STEPS, 1))

FAQS = [
    ("Who provides IT support for businesses on the Gold Coast?",
     "bcom ICT provides IT support to small and medium businesses across the Gold Coast, and has done since 2011. "
     "The team is based at 9 Ferny Avenue, Surfers Paradise, and attends sites across the whole Gold Coast &mdash; from Coomera and Logan in the north to Tweed Heads in the south — "
     "with remote and managed support available to businesses anywhere in Australia. Call 07 3041 8993."),
    ("How much does business IT support cost on the Gold Coast?",
     "bcom ICT charges $190 + GST per hour ($209.00 inc GST) for business IT support, plus a $100 + GST call-out "
     "($110.00 inc GST) on on-site work — so a first hour on site is $290 + GST ($319.00 inc GST), or a fixed $252 inc GST booked online. Remote support carries no call-out. "
     "Managed IT is a flat monthly fee calculated from your business requirements and the services included, "
     "quoted after a free review and month-to-month with no lock-in. Rates are published in full on our pricing page."),
    ("Do you only work with businesses on the Gold Coast?",
     "On-site work is Gold Coast based — that's where we can get to you the same day. Managed IT, cybersecurity, "
     "Microsoft 365 and cloud work don't need anyone on site, so we support businesses across Australia remotely. "
     "If you have staff in several states, that's normal for us."),
    ("Do you take on home computer repairs?",
     "No. bcom ICT works with businesses. We do still install WiFi and mesh networks for home offices, but general "
     "home computer repair isn't something we take on any more."),
    ("What size businesses do you work with?",
     "Most of our clients have between 3 and 60 staff. We're set up for businesses that are too big to keep muddling "
     "through and too small to employ a full-time IT person."),
    ("Are you certified to any standards?",
     "We work to recognised standards without overstating it. bcom ICT operates to the ASD Essential Eight and aligns "
     "its practices with ISO/IEC 27001 and ITIL 4, but the company is not formally certified to those standards. "
     "Individually, Royce holds ITIL 4 Foundation and Ollie holds ISO/IEC 42001:2023 Lead Implementer certification "
     "issued by BSI. Our trust centre sets all of this out in full."),
]

PAGE = {
    "path": "/",
    "priority": "1.0",
    "title": "IT Support Gold Coast for Business — Same-Day On-Site | bcom ICT",
    "description": "Business IT support on the Gold Coast since 2011. Managed IT, cybersecurity, WiFi, phone systems and Microsoft 365 for small and medium businesses. Call 07 3041 8993.",
    "hero_kind": "home",
    "hero_img": "hero-bg.webp",
    "hero_alt": "A bcom ICT client working at a dual-screen desk in a Gold Coast office, with the Surfers Paradise skyline and beach visible through the window",
    "badge": "Open now · Mon–Fri 8am–5pm",
    "h1": "Business IT support on the <em>Gold Coast</em>",
    "lede": "Managed IT, cybersecurity, WiFi, phone systems and Microsoft 365 for small and medium businesses. On-site across the Gold Coast, remote and managed support Australia-wide.",
    "actions": [("Book an on-site tech", BIZ["booking"], "white"),
                ("Call 07 3041 8993", BIZ["phone_href"], "onink")],
    "trust": ["Local since 2011", "5.0 from 24 Google reviews", "Month-to-month, no lock-in", "Callback usually the same business day"],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT is a Gold Coast IT support company that has looked after small and medium
    businesses since 2011. bcom ICT provides managed IT, cybersecurity, business WiFi, phone systems and
    Microsoft 365 support — on-site across the Gold Coast and remotely Australia-wide. Business hours are 8:00am to 5:00pm Monday to
    Friday, Brisbane time. Managed and SLA clients have contracted response targets; every other enquiry receives a best-effort response, usually the same business day. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">What we do</span>
      <h2>Six things most businesses call us about</h2>
      <p>You don't need all of it. Most clients start with one thing and hand over more once they trust us.</p>
    </div>
    <div class="grid grid--3">{cards}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why bcom ICT</span>
      <h2>What actually makes a difference</h2>
      <p>Every IT company says they're responsive and reliable. Here's what we'll commit to in writing.</p>
    </div>
    <div class="grid grid--2">{why}</div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow" style="color:#7FB2F2">By the numbers</span>
      <h2>A Gold Coast business, not a call centre</h2>
    </div>
    <dl class="stats">
      <div class="stat"><dt>Supporting businesses since</dt><dd>2011</dd></div>
      <div class="stat"><dt>Google rating</dt><dd>5.0 / 24</dd></div>
      <div class="stat"><dt>Business hours</dt><dd>Mon–Fri 8–5</dd></div>
      <div class="stat"><dt>Callback promise</dt><dd>4 business hrs</dd></div>
    </dl>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="booking">
      <div>
        <span class="eyebrow">Book online</span>
        <h2>Book an on-site technician</h2>
        <p style="margin-top:16px">Pick a time that suits and we&rsquo;ll come to you. <strong>Booking here is a
        fixed $252 inc GST for the first hour on site</strong> &mdash; $67 less than the same visit arranged by
        phone, which is $290 + GST ($319.00 inc GST). Time past the first hour is $190 + GST in half-hour
        increments, agreed with you before it starts.</p>
        <p style="margin-top:16px">Booking runs on our live calendar, so the times you see are times we
        actually have. If nothing suits, <a href="/contact">send us a message</a> or call
        <a href="{BIZ['phone_href']}">{BIZ['phone']}</a> during business hours.</p>
        <div class="hero-actions" style="margin-top:28px">
          <a class="btn btn--primary btn--lg" href="{BIZ['booking']}" target="_blank" rel="noopener">Book a time {MARK}</a>
          <a class="btn btn--ghost btn--lg" href="/contact">Rather talk first?</a>
        </div>
      </div>
      {booking_embed()}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Getting started</span>
      <h2>How it works if you switch to us</h2>
      <p>Changing IT providers feels risky. It shouldn't be — here's exactly what happens.</p>
    </div>
    <div class="grid grid--3">{steps}</div>
    <div class="rule">{MARK}</div>
    <p class="lede">We run the same disciplines a large IT department runs — documented, monitored, and
    measured against real standards. We just run them at a size that suits a business with eight staff,
    and we explain them in English. If you want the detail behind that,
    <a href="/trust-centre">our trust centre</a> sets out how we work, what we're aligned to, and what
    we commit to.</p>
  </div>
</section>

{faq_block(FAQS)}

{cta("Let's have a look at your IT",
     "A short conversation, then a plain-English review of what's working and what isn't. No charge, and no obligation to go further.")}
''',
}

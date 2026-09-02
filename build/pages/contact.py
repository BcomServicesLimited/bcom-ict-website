from layout import MARK, faq_block, ticks, related, trust_note, booking_cta, map_embed
from site_data import BIZ, FORM_ENDPOINT, address_line

LINES = [
    ("Phone", f'<a href="{BIZ["phone_href"]}">{BIZ["phone"]}</a>',
     "Our digital assistant answers any time; calls are returned in business hours. After hours our AI operator takes the details and escalates."),
    ("Email", f'<a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a>',
     "Managed and SLA clients have contracted response targets. Every other enquiry receives a best-effort response &mdash; usually the same business day, and generally within one business day."),
    ("Where we work", address_line(),
     "Our technicians and sales team come to you. On-site across the Gold Coast; managed, remote and cloud services Australia-wide."),
    ("Hours", "Mon–Fri, 8am – 5pm",
     "Phones always answered. Work is actioned during business hours, except for managed and SLA clients on a critical fault."),
]

lines = "".join(
    f'<div class="contact-line">{MARK}<div><dt>{t}</dt><dd>{v}</dd><p class="sub">{s}</p></div></div>'
    for t, v, s in LINES)

FAQS = [
    ("How do I contact bcom ICT?",
     "Call 07 3041 8993, email support@bcomservices.com, or use the enquiry form on this page. Our digital assistant answers the phone at any hour, but calls are returned during business hours — 8:00am to 5:00pm, Monday to Friday, Brisbane time — usually the same business day. Managed and SLA clients have contracted response targets under their agreement; every other enquiry receives a best-effort response. We attend sites across the Gold Coast and support businesses remotely Australia-wide."),
    ("What happens after I get in touch?",
     "We call you back to understand the problem — usually the same business day, and generally within one business day. If it can be fixed remotely we'll often start there and then, at $190 + GST per hour with no call-out. If it needs someone on site, we book a visit — same day where we can — at a $100 + GST call-out plus the hourly rate, agreed before anyone gets in a car."),
    ("Is the first conversation free?",
     "Yes, and so is the systems review that usually follows it. You get a plain-English report on what's working and what isn't, and you keep it whether or not you engage us."),
    ("Do you charge to quote?",
     "No. Quoting is free, and we quote before starting work rather than invoicing afterwards. Business IT support is $190 + GST per hour ($209.00 inc GST), with a $100 + GST call-out on on-site work. Remote support carries no call-out."),
    ("What if it's an emergency?",
     "Call rather than email. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time. If you think you've been breached, don't turn anything off or delete anything — see cyber incident response for what to do in the first hour."),
    ("Do you work outside the Gold Coast?",
     "On-site work is Gold Coast based. Managed IT, cybersecurity, the SOC, Microsoft 365 and cloud work are delivered remotely to businesses anywhere in Australia."),
]

PAGE = {
    "path": "/contact",
    "priority": "0.85",
    "title": "Contact bcom ICT — Gold Coast Business IT Support",
    "description": "Contact bcom ICT on 07 3041 8993 or support@bcomservices.com. Callback usually the same business day, Mon–Fri 8am–5pm.",
    "hero_kind": "doc",
    "eyebrow": "Contact",
    "h1": "Talk to someone who can actually help",
    "lede": "Mon–Fri 8am–5pm. Callback usually the same business day. The first conversation and the systems review that follows are both free.",
    "crumbs": [("Contact", "/contact")],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT can be reached on 07 3041 8993 or at support@bcomservices.com. Calls are
    returned during business hours &mdash; 8:00am to 5:00pm, Monday to Friday, Brisbane time. Managed and SLA
    clients have contracted response targets under their agreement; every other enquiry receives a best-effort
    response, usually the same business day. We attend sites across the Gold Coast and support businesses
    remotely Australia-wide. Call 07 3041 8993.</p>

    <div class="contact-grid" style="margin-top:56px">
      <div>
        <h2>Get in touch</h2>
        <dl style="margin-top:20px">{lines}</dl>
        <h3 style="margin-top:40px">Emergencies</h3>
        <p style="margin-top:12px">If you think you've been breached, <strong>call rather than email</strong>.
        Don't turn anything off and don't delete anything —
        <a href="/cyber-incident-response-gold-coast">here's what to do in the first hour</a>.</p>
      </div>

      <form class="enquiry" action="https://formspree.io/f/{FORM_ENDPOINT}" method="POST">
        <input type="hidden" name="_subject" value="Website enquiry — bcom ICT">
        <input type="hidden" name="_next" value="https://www.bcomservices.com/thank-you">
        <p style="display:none" aria-hidden="true"><label>Leave this empty<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
        <div>
          <h3 style="margin-bottom:6px">Send us a message</h3>
          <p class="hint">Or just call — a person will pick up.</p>
        </div>
        <div><label for="name">Your name</label><input id="name" name="name" type="text" required autocomplete="name"></div>
        <div><label for="business">Business name</label><input id="business" name="business" type="text" autocomplete="organization"></div>
        <div><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
        <div><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
        <div>
          <label for="topic">What's it about?</label>
          <select id="topic" name="topic">
            <option>Something's broken — I need help now</option>
            <option>Managed IT / ongoing support</option>
            <option>Cybersecurity</option>
            <option>Business WiFi or networking</option>
            <option>Phone systems</option>
            <option>Cloud &amp; Microsoft 365</option>
            <option>I think we've been breached</option>
            <option>Something else</option>
          </select>
        </div>
        <div><label for="message">What's going on?</label><textarea id="message" name="message" required></textarea></div>
        <button class="btn btn--primary btn--lg" type="submit">Send enquiry</button>
        <p class="hint">We&rsquo;ll come back to you during business hours, usually the same business day — 8:00am to
        5:00pm, Monday to Friday, Brisbane time. We don't share your details with anyone.</p>
      </form>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Where we work</h2>
    <p style="margin-top:16px;max-width:var(--measure)">We come to you. On-site attendance covers the whole
    Gold Coast, from Coomera in the north to Coolangatta and Tweed Heads in the south, with managed, remote
    and cloud services delivered Australia-wide.</p>
    <div style="margin-top:28px">{map_embed()}</div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>Before you call, it helps to know</h2>
    {ticks([
      "<strong>What's affected</strong> — one person, one system, or everyone. That sets the priority.",
      "<strong>When it started</strong>, and whether anything changed just before — an update, a new device, a power cut.",
      "<strong>Whether there's a workaround</strong>, or the business has genuinely stopped.",
      "<strong>Any error message</strong>, word for word or as a photo. It saves a surprising amount of time.",
    ])}
    <p style="margin-top:24px">None of it is essential. Call and we'll work it out together —
    <a href="/service-levels-and-security">our priority matrix</a> explains how we classify it once we know.</p>
  </div>
</section>

{booking_cta()}

{faq_block(FAQS)}

{related([
  ("Support", "/support"),
  ("Published service levels", "/service-levels-and-security"),
  ("Pricing", "/pricing"),
  ("Cyber incident response", "/cyber-incident-response-gold-coast"),
  ("About bcom ICT", "/about"),
  ("Our team", "/our-team"),
], heading="Useful next")}
''',
}

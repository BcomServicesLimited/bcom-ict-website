from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, booking_cta
from site_data import BIZ

ROUTES = [
    ("Call 07 3041 8993", BIZ["phone_href"],
     "Our digital assistant answers any time; calls are returned in business hours. The fastest route for anything urgent, and the only one to use if you think you've been breached."),
    ("Email support@bcomservices.com", "mailto:support@bcomservices.com",
     "Best for things that aren't stopping anyone working. Managed and SLA clients have contracted response targets; every other enquiry receives a best-effort response &mdash; usually the same business day, and generally within one business day."),
    ("Send an enquiry", "/contact",
     "The form on our contact page, if you'd rather write it down than explain it on the phone."),
]

PRIORITY = [
    ("Everyone is affected", "Server down, internet out, phones or email down for the whole office, or signs of ransomware. Call — don't email."),
    ("A team is blocked", "One department can't work, or a core system is down with a painful workaround. Call."),
    ("One person is stuck", "Someone can't print, an account is locked, an application won't open. Email is fine."),
    ("You need something new", "A starter set up, a new device, an access change, planned work. Email or the form — these get scheduled rather than responded to."),
]

FAQS = [
    ("How do I get IT support from bcom ICT?",
     "Call 07 3041 8993 for anything urgent — business hours are 8am to 5pm Monday to Friday, Brisbane time. Outside those hours our digital assistant takes the details and the job is logged, including at weekends and on public holidays. Email support@bcomservices.com for non-urgent issues, with a best-effort callback — usually the same business day. For remote support we'll send you a one-time link that lets a technician see your screen with your permission. Existing clients don't need to be managed clients to call."),
    ("What happens when I call after hours?",
     "Our AI phone operator answers, takes the details, triages and escalates. It identifies itself as an AI rather than pretending to be a person. Work is actioned during business hours, except for managed and SLA clients on a critical fault, where after-hours attendance is included."),
    ("How does remote support work?",
     "bcom ICT uses Splashtop SOS. Call or email first so a technician is ready, then download the small SOS application from sos.splashtop.com and run it — it shows a 9-digit session code. Read that code to your technician and approve the connection. Nothing is permanently installed, you can watch the whole session on your own screen, and access ends when the session does."),
    ("Do I need to be a managed client to get help?",
     "No. We take support calls from any business, including ones we've never worked with. Managed and SLA clients have contracted response targets and after-hours attendance under their agreement. Everyone else gets a best-effort response — usually the same business day, and generally within one business day."),
    ("What do you need from me when I report a problem?",
     "What's affected — one person or everyone. When it started, and whether anything changed just before. Whether there's a workaround. And any error message, word for word or as a photo. None of it is essential, but all of it saves time."),
    ("I think we've been hacked. What do I do right now?",
     "Call 07 3041 8993. Disconnect affected machines from the network but don't power them off — shutting down destroys evidence in memory. Don't delete anything, including the ransom note, and don't wipe and rebuild. See cyber incident response for the full first-hour checklist."),
]

PAGE = {
    "path": "/support",
    "priority": "0.8",
    "title": "Get Support — bcom ICT Gold Coast IT Helpdesk",
    "description": "How to get IT support from bcom ICT: call 07 3041 8993 (returned in business hours), email support@bcomservices.com, or request remote support.",
    "hero_kind": "doc",
    "eyebrow": "Support",
    "aside": f'''
      <span class="tag">Remote support</span>
      <h2>Splashtop SOS</h2>
      <p>Call or email us first so a technician is ready — then run this and read us the code.</p>
      <a class="btn btn--primary btn--lg" href="{BIZ['splashtop']}" target="_blank" rel="noopener">Download Splashtop SOS {MARK}</a>
      <ol>
        <li>Run the file you just downloaded — nothing installs permanently.</li>
        <li>It shows a <strong>9-digit session code</strong>.</li>
        <li>Read the code to your technician and approve the connection.</li>
      </ol>
      <p class="after">You watch the whole session on your own screen and can end it at any moment. Access stops when the session does.</p>
    ''',
    "h1": "Need help now?",
    "lede": "Call 07 3041 8993 — returned during business hours, Monday to Friday. You don't need to be an existing client.",
    "crumbs": [("Support", "/support")],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">To get IT support from bcom ICT, call 07 3041 8993 — returned in business hours including weekends
    and public holidays — or email support@bcomservices.com for non-urgent issues, with a callback within 4
    business hours. Remote support is provided via a one-time link you approve. bcom ICT takes support calls
    from businesses that are not existing clients.</p>

    <div class="grid grid--3" style="margin-top:48px">{cards([(t, h, d) for t, h, d in ROUTES])}</div>

    <div class="vnote" style="border-color:#E8A0A0;background:#FBEEEE;margin-top:40px">
      <strong>If you think you've been breached</strong>
      <p>Call <strong>07 3041 8993</strong> rather than emailing. Disconnect affected machines from the
      network but <strong>don't power them off</strong> — that destroys evidence in memory. Don't delete
      anything and don't rebuild.
      <a href="/cyber-incident-response-gold-coast">Full first-hour checklist</a>.</p>
    </div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Which route</span>
      <h2>Call or email? It depends who's affected</h2>
      <p>We'll agree the priority with you when you log it, but this is roughly how we'll classify it.</p>
    </div>
    <div class="grid grid--4">{cards([(t, None, d) for t, d in PRIORITY], icon=False)}</div>
    <p style="margin-top:32px">The full priority matrix, with response targets for managed and non-managed
    clients, is on <a href="/service-levels-and-security">our service levels page</a>.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>What Splashtop SOS actually does</h2>
        <p style="margin-top:16px">It is a support tool, not monitoring software. Worth knowing exactly what
        it is before you run it — and the download link is at the top of this page.</p>
        {ticks([
          "Nothing is permanently installed — the application closes with the session",
          "You give us the code; we cannot connect without it",
          "You see everything on your own screen and can disconnect instantly",
          "Access ends when the session ends, unless you're a managed client with monitoring agreed separately in writing",
        ])}
        <p style="margin-top:24px">If it turns out to need hands on hardware, we'll book an on-site visit —
        same day where we can. On-site is a $100 + GST call-out plus $190 + GST per hour; remote is $190 + GST
        per hour with no call-out. <a href="/pricing">Full rates here</a>, agreed before anyone gets in a car.</p>
      </div>
      <div>
        <h2>Before you call</h2>
        <p style="margin-top:16px">None of this is essential. It just saves time.</p>
        {ticks([
          "<strong>Who's affected</strong> — one person, one team, or everyone",
          "<strong>When it started</strong>, and what changed just before",
          "<strong>Whether there's a workaround</strong>, or work has genuinely stopped",
          "<strong>The exact error message</strong> — a photo of the screen is perfect",
          "<strong>What you've already tried</strong>, so we don't repeat it",
        ])}
      </div>
    </div>

    {trust_note('Phones are returned in business hours — after hours by our AI operator, which takes details and escalates rather than pretending to be a person. What happens at which hour is set out in full on <a href="/service-levels-and-security">service levels</a>.')}
  </div>
</section>

{booking_cta()}

{faq_block(FAQS)}

{related([
  ("Published service levels", "/service-levels-and-security"),
  ("Cyber incident response", "/cyber-incident-response-gold-coast"),
  ("Remote IT Support", "/remote-it-support-gold-coast"),
  ("Business IT Support", "/it-support-and-services-gold-coast"),
  ("Contact us", "/contact"),
  ("Pricing", "/pricing"),
], heading="Related")}

{cta("Call 07 3041 8993",
     "Open 8am–5pm Monday to Friday. You don't need to be an existing client, and the first conversation costs nothing.")}
''',
}

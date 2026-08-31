from layout import MARK, cta, ticks

PAGE = {
    "path": "/thank-you",
    "priority": "0.1",
    "noindex": True,
    "title": "Thanks — we've got your message | bcom ICT",
    "description": "Your enquiry has reached bcom ICT. We'll come back to you within 4 business hours.",
    "hero_kind": "doc",
    "eyebrow": "Message sent",
    "h1": "Thanks — that's reached us",
    "lede": "We'll come back to you within 4 business hours, during business hours: 8:00am to 5:00pm, Monday to Friday, Brisbane time.",
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <h2>If it's urgent</h2>
    <p style="margin-top:16px">Call <a href="tel:+61730418993"><strong>07 3041 8993</strong></a> rather than
    waiting on the email. During business hours you'll get a person.</p>
    <p style="margin-top:16px">If you think you've been breached, call — don't email — and
    <strong>don't turn anything off or delete anything</strong>.
    <a href="/cyber-incident-response-gold-coast">Here's what to do in the first hour</a>.</p>

    <div class="rule">{MARK}</div>

    <h2>While you're here</h2>
    {ticks([
      '<a href="/service-levels-and-security">What we commit to</a> — response targets, hours and escalation, published',
      '<a href="/pricing">Pricing</a> — $198 + GST per hour, $100 + GST on-site call-out',
      '<a href="/trust-centre">Trust centre</a> — what we hold, what we align to, and where the line is',
      '<a href="/how-to-choose-an-msp-gold-coast">Eight questions to ask any IT provider</a> — including us',
    ])}
  </div>
</section>

{cta("Need someone sooner?",
     "Call 07 3041 8993 during business hours and you'll get a person rather than a queue.")}
''',
}

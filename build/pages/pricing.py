from layout import MARK, cta, faq_block, ticks, related, trust_note, verify_note
from site_data import RATES as R

TIERS = [
    ("Ad-hoc support", "$198 + GST per hour", False,
     "Charged at $198 + GST per hour ($217.80 inc GST), in hourly increments. On-site work adds a $100 + GST call-out ($110 inc GST). Remote support is time only — no call-out.",
     ["First hour on site: $298 + GST ($327.80 inc GST). First hour remote: $198 + GST ($217.80 inc GST)",
      "Remote first where the fault allows it — it's faster and cheaper",
      "No retainer, no minimum, no contract",
      "Same technicians as managed clients get"],
     "Suits: simple setups where an occasional problem is an annoyance rather than a crisis."),
    ("Managed IT", "Flat monthly fee", True,
     "A single monthly fee based on how many staff and devices you have. Covers monitoring, unlimited helpdesk, patching, backup and Microsoft 365 management.",
     ["Unlimited helpdesk — no per-ticket charges",
      "4-hour response SLA on critical faults, after-hours attendance included",
      "Recurring problems chased to root cause at our cost",
      "Month-to-month. No lock-in, no exit fee"],
     "Suits: businesses with a server, staff who can't work without their systems, or client data you'd need to prove is protected."),
    ("Projects", "Fixed quote", False,
     "WiFi installs, cabling, phone systems, cloud migrations and office relocations are quoted as a fixed price after a site visit or scoping call.",
     ["Surveyed or scoped before quoting, not estimated off a floor plan",
      "One quote covering equipment, labour and documentation",
      "Variations agreed in writing before they happen",
      "Handover documentation included, not extra"],
     "Suits: anything with a defined start and end."),
]

tiers = "".join(
    f'''<div class="tier{' tier--feature' if feat else ''}">
      <span class="label">{label}</span>
      <h3>{name}</h3>
      <p style="font-size:.9375rem;color:var(--slate)">{blurb}</p>
      <ul>{"".join(f"<li>{MARK}<span>{i}</span></li>" for i in items)}</ul>
      <p style="font-size:.875rem;color:var(--slate);border-top:1px solid var(--line);padding-top:16px;margin-top:8px"><strong>{suits}</strong></p>
      <a class="btn btn--{'primary' if feat else 'ghost'}" href="/contact">Get a quote</a>
    </div>''' for name, label, feat, blurb, items, suits in TIERS)

FAQS = [
    ("How much does business IT support cost on the Gold Coast?",
     "bcom ICT charges $198 + GST per hour ($217.80 inc GST) for business IT support, plus a $100 + GST call-out ($110 inc GST) on on-site work — a first hour on site is $298 + GST. Remote support carries no call-out. Managed IT is a flat monthly fee quoted after a free review, month-to-month with no lock-in. Projects are fixed-price after scoping. Call 07 3041 8993."),
    ("What is bcom ICT's hourly rate?",
     "bcom ICT charges $198 + GST per hour ($217.80 inc GST) for business IT support, billed in hourly increments. On-site work adds a $100 + GST call-out ($110 inc GST), so a first hour on site is $298 + GST ($327.80 inc GST). Remote support carries no call-out. Rates are agreed before work starts."),
    ("Why isn't managed IT priced on this page?",
     "Because a single monthly figure would mislead. Two businesses with the same headcount can differ by a factor of three depending on whether they run a server, how old the machines are, how many sites there are and what compliance obligations apply. We quote it after the free review, based on what you actually run rather than on a headcount and a guess."),
    ("Is managed IT more expensive than paying by the hour?",
     "In a quiet month, yes. Over a year, it usually isn't — and that's before counting the hours your staff lose to problems nobody is preventing. The real difference is predictability: you can budget for a flat monthly fee, and you're never weighing up whether a problem is worth a call-out."),
    ("Do you charge for quotes or the initial review?",
     "No. The first conversation and the systems review that follows are both free, and you keep the written report whether or not you engage us."),
    ("Are there lock-in contracts?",
     "No. Managed IT agreements are month-to-month. We'd rather earn the next month than hold you to a three-year term, and if we're not worth the money you should be able to leave — with your documentation and credentials handed over properly."),
    ("What's not included in managed IT?",
     "Projects and hardware. A new WiFi install, an office move, a cloud migration or a fleet of laptops are quoted separately — bundling them into a monthly fee just hides the cost. Day-to-day support, monitoring, patching and backup are included with no per-ticket charges."),
    ("Do you mark up hardware?",
     "We source at trade pricing and are transparent about what we charge over it. If you'd rather buy the hardware yourself and have us configure it, that's fine too — some clients do."),
]

PAGE = {
    "path": "/pricing",
    "priority": "0.8",
    "title": "Pricing — $198 + GST per Hour | bcom ICT Gold Coast",
    "description": "bcom ICT business IT support is $198 + GST per hour ($217.80 inc GST), plus a $100 + GST on-site call-out. Remote support has no call-out. Managed IT is a flat monthly fee with no lock-in.",
    "hero_kind": "doc",
    "eyebrow": "Pricing",
    "h1": "How we charge, and why we quote first",
    "lede": "$198 + GST an hour, $100 + GST call-out for on-site. Published, not negotiated per client — and everything is agreed before work starts.",
    "crumbs": [("Pricing", "/pricing")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT charges $198 + GST per hour ($217.80 inc GST) for business IT support, billed
    in hourly increments, plus a $100 + GST call-out ($110 inc GST) for on-site work — so a first hour on
    site is $298 + GST. Remote support carries no call-out. Managed IT is a flat monthly fee, month-to-month
    with no lock-in. Call 07 3041 8993.</p>

    <div class="pricecard" style="margin-top:40px;max-width:none">
      <h3>Published rates</h3>
      <div class="grid grid--3" style="margin-top:20px">
        <div><div class="from">$198 <small>+ GST per hour · $217.80 inc GST</small></div></div>
        <div><div class="from">$100 <small>+ GST on-site call-out · $110 inc GST</small></div></div>
        <div><div class="from">$298 <small>+ GST first hour on site · $327.80 inc GST</small></div></div>
      </div>
      <p style="margin-top:20px;font-size:.9375rem;color:var(--slate)">Charged in hourly increments and
      agreed before work starts. Remote support carries no call-out, which is why we try remote first
      wherever the fault allows it. Managed IT is priced separately as a flat monthly fee — see below.</p>
    </div>

    {verify_note("Managed IT per-seat pricing is not published yet. It varies enough with device count, server presence and compliance obligations that a single figure would mislead — we quote it after the free review. Royce to confirm whether an indicative from-price should appear here.")}

    <div class="tiers">{tiers}</div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>What actually drives the number</h2>
    <p style="margin-top:16px">Two businesses with the same headcount can differ by a factor of three. These
    are the things that move it, so you can sanity-check any quote you're given — ours or anyone else's.</p>
    {ticks([
      "<strong>Do you run a server?</strong> On-premise servers carry maintenance, backup and patching that cloud-only businesses simply don't have.",
      "<strong>How old is the hardware?</strong> A fleet of eight-year-old machines generates support hours no provider can prevent. Sometimes replacement is the cheaper support strategy.",
      "<strong>How many sites?</strong> One office is straightforward. Three sites with connectivity between them is a different job.",
      "<strong>What compliance applies?</strong> AFS licensees, health providers and businesses handling sensitive data need controls and evidence that others don't.",
      "<strong>How documented is it now?</strong> An undocumented environment costs more to take on, because the first months are discovery.",
    ])}
    <p style="margin-top:24px">Any provider quoting a monthly figure without asking about these hasn't
    understood your business yet.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>What we won't do</h2>
    {ticks([
      "<strong>Lock you in.</strong> Managed agreements are month-to-month, with no exit fee and your documentation handed over.",
      "<strong>Invoice for work you didn't approve.</strong> On-site is a fixed call-out plus hourly increments, agreed up front.",
      "<strong>Charge per ticket.</strong> If people hesitate to ask for help because it costs, small problems become big ones.",
      "<strong>Bundle projects into the monthly fee.</strong> That hides cost. Projects are quoted separately and transparently.",
      "<strong>Sell you what you don't need.</strong> Including telling you that you're not ready for managed IT, or that your existing phone system has years left in it.",
    ])}

    <div class="rule">{MARK}</div>

    <h2>Getting a real number</h2>
    <p style="margin-top:16px">The free systems review is how we get to an accurate quote rather than a
    guess. We look at what you're running, what state it's in, and what you actually need — then quote on
    that. You keep the written report either way, including if you decide not to proceed.</p>

    {trust_note('What you get for a managed fee is set out in full on <a href="/service-levels-and-security">our published service levels</a> — response targets, escalation, and exit terms, published rather than negotiated privately per client.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
  ("Business IT Support", "/it-support-and-services-gold-coast"),
  ("Published service levels", "/service-levels-and-security"),
  ("Onboarding — first 30 days", "/onboarding-first-30-days"),
  ("Managed IT vs break-fix", "/managed-it-vs-break-fix"),
  ("Contact us", "/contact"),
], heading="Related")}

{cta("Get a number for your business",
     "A free review of what you're running, then a quote based on it rather than on a headcount and a guess.")}
''',
}

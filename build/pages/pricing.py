from layout import MARK, cta, faq_block, ticks, related, trust_note, verify_note

TIERS = [
    ("Ad-hoc support", "Pay for what you use", False,
     "Charged as a fixed call-out fee plus hourly increments, agreed up front before anyone starts. Remote support is charged for time only, with no call-out.",
     ["Quoted before we begin, never invoiced after",
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
     "bcom ICT charges ad-hoc support as a fixed call-out fee plus hourly increments, agreed before work starts, with remote support charged for time only and no call-out. Managed IT is a flat monthly fee based on staff and device numbers, covering monitoring, unlimited helpdesk, patching and backup. Projects are fixed-price after scoping. Every engagement is quoted before it begins. Call 07 3041 8993."),
    ("Why don't you publish exact prices?",
     "Because a number without context misleads more than it helps. Two businesses with the same headcount can differ by a factor of three depending on whether they run a server, how old the machines are, and what compliance obligations they carry. What we will do is quote before starting, and tell you the call-out and hourly rate on the phone before anyone gets in a car."),
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
    "title": "Pricing — How bcom ICT Charges for Business IT",
    "description": "How bcom ICT charges: ad-hoc support at a fixed call-out plus hourly increments, managed IT at a flat monthly fee with no lock-in, and projects fixed-priced after scoping.",
    "hero_kind": "doc",
    "eyebrow": "Pricing",
    "h1": "How we charge, and why we quote first",
    "lede": "Three commercial models, each suited to a different situation. Everything is quoted before work starts — you'll never get an invoice for something you didn't approve.",
    "crumbs": [("Pricing", "/pricing")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT charges ad-hoc support as a fixed call-out fee plus hourly increments, agreed
    before work starts. Remote support is charged for time only with no call-out. Managed IT is a flat
    monthly fee based on staff and device numbers, month-to-month with no lock-in. Projects are fixed-price
    after scoping. Call 07 3041 8993.</p>

    {verify_note("Indicative rates are deliberately not published on this page yet. Royce to confirm the current call-out fee, hourly rate and managed IT per-seat pricing before figures go live — a wrong number here is worse than no number.")}

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

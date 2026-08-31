from layout import MARK, cta, faq_block, ticks, related, trust_note, price_table
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
     "A single monthly fee, calculated from your business requirements and the services you want included. Covers monitoring, unlimited helpdesk, patching, backup and Microsoft 365 management.",
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
    ("How much do common IT projects cost on the Gold Coast?",
     "Indicative starting points from bcom ICT: a one-hour on-site visit booked online is $252 inc GST; a small-business cybersecurity health check is $500 inc GST for up to five users; business WiFi for a simple site starts at $1,500 + GST with hardware included; data cabling is around $150 + GST per outlet; a five-extension VoIP phone system is about $2,250 + GST including handsets; a Microsoft 365 migration is around $150 + GST per user; and automatic cloud backup is $10 + GST per user per month. Every project is quoted as a fixed price after scoping."),
    ("How much does business IT support cost on the Gold Coast?",
     "bcom ICT charges $198 + GST per hour ($217.80 inc GST) for business IT support, plus a $100 + GST call-out ($110 inc GST) on on-site work — a first hour on site is $298 + GST. Remote support carries no call-out. Managed IT is a flat monthly fee quoted after a free review, month-to-month with no lock-in. Projects are fixed-price after scoping. Call 07 3041 8993."),
    ("What is bcom ICT's hourly rate?",
     "bcom ICT charges $198 + GST per hour ($217.80 inc GST) for business IT support, billed in hourly increments. On-site work adds a $100 + GST call-out ($110 inc GST), so a first hour on site is $298 + GST ($327.80 inc GST). Remote support carries no call-out. Rates are agreed before work starts."),
    ("How is managed IT priced?",
     "Managed IT is calculated from your business requirements and the services provided — not per seat. Two businesses with the same headcount can differ by a factor of three depending on whether they run a server, how old the machines are, how many sites there are, what has to stay available and what compliance obligations apply. bcom ICT quotes it after the free review, so the figure reflects your actual environment and the scope you've asked us to cover."),
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

PROJECTS = [
    ('On-site visit, booked online', '$252', 'inc GST, fixed',
     ['One hour on site with a technician', 'No call-out charged on top',
      '<a href="/on-site-technical-support-gold-coast">On-site IT support</a>']),
    ('Cybersecurity health check', '$500', 'inc GST, fixed',
     ['Up to five users', 'Written report and prioritised plan, yours to keep',
      '<a href="/cybersecurity-health-check-for-small-business-gold-coast">Health check</a>']),
    ('Business WiFi, simple site', '$1,500', '+ GST, hardware included',
     ['Surveyed, installed, configured and documented', 'Guest network kept separate from business systems',
      '<a href="/business-wifi-gold-coast">Business WiFi</a>']),
    ('Data cabling, per outlet', '$150', '+ GST, indicative',
     ['Cat6 outlet tested, certified and labelled', 'Installed by ACMA registered cabling contractors',
      '<a href="/network-cabling-for-offices-gold-coast">Network cabling</a>']),
    ('Phone system, five extensions', '$2,250', '+ GST, handsets included',
     ['Five handsets at $350 + GST, install at $100 + GST each', 'Monthly call plan quoted separately',
      '<a href="/business-phone-systems-gold-coast">Phone systems</a>']),
    ('Microsoft 365 migration, per user', '$150', '+ GST, indicative',
     ['Mail, calendar and contacts moved intact', 'Scoped first, then quoted as a fixed price',
      '<a href="/microsoft-365-setup-gold-coast">Microsoft 365</a>']),
    ('Cloud backup, per user', '$10', '+ GST per month',
     ['Automatic, held away from your network', 'Restores tested rather than assumed',
      '<a href="/data-backup-recovery-gold-coast">Backup &amp; recovery</a>']),
]

PAGE = {
    "path": "/pricing",
    "priority": "0.8",
    "title": "Pricing — $198 + GST per Hour | bcom ICT Gold Coast",
    "description": "bcom ICT business IT support is $198 + GST per hour ($217.80 inc GST), plus a $100 + GST on-site call-out. Remote support has no call-out. Managed IT is quoted to your requirements, month-to-month with no lock-in.",
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
    site is $298 + GST. Remote support carries no call-out. Managed IT is a flat monthly fee calculated from
    your requirements and the services included, month-to-month with no lock-in. Call 07 3041 8993.</p>

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

    <p style="margin-top:28px;font-size:.9375rem;color:var(--slate);max-width:64ch">Managed IT is not listed
    above because it is not a per-seat product. It is calculated from your business requirements and the
    services you want included, and quoted after the free review — see <a href="#faq">how that works</a>.</p>

    <div class="tiers">{tiers}</div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>What drives a managed IT quote</h2>
    <p style="margin-top:16px">Managed IT is priced on requirements and scope rather than per seat, which is
    why there is no from-price above. Two businesses with the same headcount can differ by a factor of three.
    These are the things that move it, so you can sanity-check any quote you're given — ours or anyone
    else's.</p>
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


<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Project work</span>
      <h2>What common jobs actually start at</h2>
      <p>Most providers will not publish these. Here are ours, so you can work out whether it is worth a conversation before you have one.</p>
    </div>
    {price_table(PROJECTS, note="These are starting points for straightforward jobs, not quotes. Every project is scoped first and then quoted as a fixed price, so the number you approve is the number you pay &mdash; variations are agreed in writing before they happen, never discovered on the invoice. What moves a figure is almost always the building or the system being left behind rather than the work itself: hard ceilings and long cable runs, a mail platform that will not release its data cleanly, a site that can only be worked on after hours. We would rather tell you the range now and the exact number after we have looked.")}
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

from layout import MARK, cta, faq_block, ticks, related, trust_note, price_table, booking_cta
from site_data import RATES as R

TIERS = [
    ("Ad-hoc support", "$190 + GST per hour", False,
     "Charged at $190 + GST per hour ($209.00 inc GST), in half-hour increments after the first hour. On-site work adds a $100 + GST call-out ($110.00 inc GST). Remote support is time only — no call-out.",
     ["First hour on site: $290 + GST ($319.00 inc GST), or $252 inc GST booked online. Remote job up to an hour: $150 + GST ($165 inc GST), no call-out",
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
    ("How does bcom ICT charge for project work?",
     "Projects are quoted as a fixed price after the work has been scoped, not estimated over the phone. bcom ICT publishes indicative starting points for a few common jobs so you can judge whether a conversation is worth having, but those are planning aids rather than quotes and each one is published alongside what it assumes and what sits outside it. Once a project is scoped, the fixed price is agreed in writing before work starts and variations are agreed before they happen rather than appearing on the invoice."),
    ("Why won't you give me a price over the phone?",
     "Because a number given before anyone has looked is a guess, and a guess given confidently becomes something you reasonably expect us to honour. Most project costs are driven by the building or by the system being replaced rather than by the work itself — ceiling access, cable routes, whether an old mail platform will release its data cleanly, whether a site can only be worked on after hours. We would rather tell you the range of possibilities now and the actual number after we have looked at your site."),
    ("Do you publish per-outlet or per-user rates?",
     "No, and we removed them deliberately. A published unit price invites a business to multiply it by its own headcount or outlet count and arrive at a figure bcom ICT never quoted, which is the most common way a published price ends in a disagreement. Cabling, migrations and phone systems are quoted on the actual site and the actual requirement."),
    ("How much does business IT support cost on the Gold Coast?",
     "bcom ICT charges $190 + GST per hour ($209.00 inc GST) for business IT support, plus a $100 + GST call-out ($110.00 inc GST) on on-site work — a first hour on site is $290 + GST ($319.00 inc GST), or a fixed $252 inc GST booked online. Remote support carries no call-out. Managed IT is a flat monthly fee quoted after a free review, month-to-month with no lock-in. Projects are fixed-price after scoping. Call 07 3041 8993."),
    ("What is bcom ICT's hourly rate?",
     "bcom ICT charges $190 + GST per hour ($209.00 inc GST) for business IT support, billed in half-hour increments after the first hour. On-site work adds a $100 + GST call-out ($110.00 inc GST), so a first hour on site is $290 + GST ($319.00 inc GST) — or a fixed $252 inc GST booked online. Remote support carries no call-out. Rates are agreed before work starts."),
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

# ITIL separates what is committed from what is estimated, and this page follows that
# boundary rather than blurring it. A rate is a unit of charge and is fully within our
# control, so it is published precisely. A standard service request has a pre-defined
# scope, so it can carry a fixed price safely. Everything else is a quoted project,
# where a figure before assessment is a planning aid and nothing more.
#
# Per-unit project figures were deliberately removed: a published "per outlet" or
# "per user" rate invites a client to do their own multiplication and arrive at a
# number we never quoted, which is exactly how a price page becomes a dispute.

STANDARD = [
    ('First hour on site, booked online', '$252', 'inc GST &middot; fixed price',
     ['<strong>$67 less than the same hour arranged by phone</strong>, which is $290 + GST ($319.00 inc GST)',
      'The call-out and the first hour with a technician, as one figure',
      'Booked through our calendar, so the price is settled before anyone sets off',
      'Beyond the first hour, $190 + GST in half-hour increments, agreed with you first',
      '<a href="/on-site-technical-support-gold-coast">On-site IT support</a>']),
    ('Small business security health check', '$500', 'inc GST &middot; fixed price',
     ['Up to five users',
      'Email, identity, endpoints, backups and network reviewed',
      'Written report and prioritised plan, yours to keep either way',
      '<a href="/cybersecurity-health-check-for-small-business-gold-coast">Health check</a>']),
]

# label, indicative, assumes, excluded, link text, link href
INDICATIVE = [
    ('Business WiFi for a single office',
     'from around $1,500 + GST',
     'One tenancy, straightforward construction, existing cabling adequate for the access points required.',
     'Multi-floor or multi-building sites, new cabling, switching upgrades, outdoor coverage.',
     'Business WiFi', '/business-wifi-gold-coast'),
    ('Structured cabling for a small office',
     'from around $1,200 + GST',
     'Around eight outlets, standard commercial ceiling and cavity access, tested and certified.',
     'Cabinet, patch panel and switching; long runs; hard ceilings; heritage buildings; after-hours access.',
     'Network cabling', '/network-cabling-for-offices-gold-coast'),
    ('Phone system for a small team',
     'from around $2,250 + GST',
     'Five handsets supplied and installed, numbers ported, call flow configured.',
     'Monthly service and call plan, which is quoted alongside the install.',
     'Phone systems', '/business-phone-systems-gold-coast'),
    ('Microsoft 365 migration',
     'quoted after assessment',
     'Nothing meaningful can be said before we know what is being migrated from.',
     'We do not publish a per-user figure for this, because the range between an easy migration and a difficult one is wider than any average would usefully describe.',
     'Microsoft 365', '/microsoft-365-setup-gold-coast'),
    ('Automatic cloud backup',
     '$10 + GST per user per month',
     'Mailboxes, files and the data staff work on day to day. A recurring subscription rather than a project.',
     'Servers, databases and on-premises infrastructure, quoted on data volume and how quickly you need it back.',
     'Backup &amp; recovery', '/data-backup-recovery-gold-coast'),
]

irows = "".join(
    f'<tr><td><strong>{n}</strong><br><a href="{h}" style="font-size:.875rem">{lt}</a></td>'
    f'<td class="indic">{v}</td><td>{a}</td><td>{x}</td></tr>'
    for n, v, a, x, lt, h in INDICATIVE)


PAGE = {
    "path": "/pricing",
    "priority": "0.8",
    "title": "Pricing — $190 + GST per Hour | bcom ICT Gold Coast",
    "description": "bcom ICT business IT support is $190 + GST per hour ($209.00 inc GST), plus a $100 + GST on-site call-out. Remote support has no call-out.",
    "hero_kind": "doc",
    "eyebrow": "Pricing",
    "h1": "How we charge, and why we quote first",
    "lede": "$190 + GST an hour, $100 + GST call-out for on-site. Published, not negotiated per client — and everything is agreed before work starts.",
    "crumbs": [("Pricing", "/pricing")],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT charges $190 + GST per hour ($209.00 inc GST) for business IT support, billed
    in half-hour increments after the first hour, plus a $100 + GST call-out ($110.00 inc GST) for on-site work — so a first hour on
    site is $290 + GST ($319.00 inc GST), or a fixed $252 inc GST booked online. A remote job of up to an hour is $150 + GST
    ($165 inc GST) and carries no call-out. Managed IT is a flat monthly fee calculated from
    your requirements and the services included, month-to-month with no lock-in. Project work is quoted as a
    fixed price after scoping rather than estimated in advance. Call 07 3041 8993.</p>

    <div class="pricecard" style="margin-top:40px;max-width:none">
      <h3>Published rates</h3>
      <div class="grid grid--2" style="margin-top:20px">
        <div><div class="from">$190 <small>+ GST per hour · $209.00 inc GST</small></div></div>
        <div><div class="from">$100 <small>+ GST on-site call-out · $110.00 inc GST</small></div></div>
        <div><div class="from">$290 <small>+ GST first hour on site · $319.00 inc GST</small></div></div>
        <div><div class="from">$150 <small>+ GST remote job up to an hour · $165.00 inc GST</small></div></div>
      </div>
      <p style="margin-top:20px;font-size:.9375rem;color:var(--slate)">Charged in half-hour increments after the first hour and
      agreed before work starts. Remote support carries no call-out, which is why we try remote first
      wherever the fault allows it. <strong>Booking a visit through our online calendar is a fixed $252 inc GST</strong>
      &mdash; $67 less than the same first hour arranged by phone, because it costs us less to schedule and we
      pass that on. Managed IT is priced separately as a flat monthly fee — see below.</p>
    </div>

    <p style="margin-top:28px;font-size:.9375rem;color:var(--slate);max-width:64ch">Managed IT is not listed
    above because it is not a per-seat product. It is calculated from your business requirements and the
    services you want included, and quoted after the free review — see <a href="#faq">how that works</a>.</p>

    <div class="tiers">{tiers}</div>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How we charge</span>
      <h2>Three charging models, and which applies to you</h2>
      <p>Most disagreements about an IT invoice come from a figure being treated as a commitment when it was only ever an estimate. We separate the two rather than leaving it to be worked out afterwards.</p>
    </div>
    {ticks([
      "<strong>A rate is a unit of charge.</strong> The hourly rate and the call-out are entirely within our control, so we publish them precisely and they do not move. What a job costs is the rate multiplied by hours nobody can know in advance &mdash; which is why a rate is a commitment and a job total is not.",
      "<strong>A fixed price needs a fixed scope.</strong> Two things on this page carry a fixed price because their scope is completely defined before anyone starts: a one-hour booked visit and a health check for up to five users. Anything with a defined scope can be priced with confidence, and anything without one cannot.",
      "<strong>A quoted project is scoped, then priced, then agreed in writing.</strong> The fixed price is set after the assessment rather than before it. Once agreed, that is the number &mdash; variations are approved by you before they happen and never discovered on an invoice.",
      "<strong>An indicative figure is a planning aid.</strong> It is not an offer, not a quote and not a cap. It exists so you can decide whether to have a conversation, and it is always published alongside what it assumes.",
      "<strong>Managed IT is a flat monthly fee.</strong> Calculated from requirements and scope rather than per seat, quoted after the free review, and month-to-month.",
    ])}
    <p style="margin-top:24px;max-width:64ch">This is ordinary service management practice rather than
    caution for its own sake &mdash; see <a href="/how-we-work-itil">how we work</a>. The point of separating
    a rate from an estimate from a quote is that you always know which one you are looking at, and can hold
    us to the ones that are commitments.</p>
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
      "<strong>Invoice for work you didn't approve.</strong> On-site is a fixed call-out plus the hourly rate in half-hour increments, agreed up front.",
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
      <span class="eyebrow">Fixed price</span>
      <h2>Two jobs we can price without looking</h2>
      <p>These have a defined scope, so the price is fixed and agreed before we start. There is nothing to discover, which is exactly why they can carry a number.</p>
    </div>
    {price_table(STANDARD, note="Fixed price means fixed. If a job turns out to be larger than the one described here, we tell you before the hour is up rather than after it, and anything additional is agreed with you before it happens.")}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Project work</span>
      <h2>Everything else is quoted after we have looked</h2>
      <p>The figures below are planning aids, not quotes and not offers. They exist so you can judge whether a conversation is worth having &mdash; nothing more.</p>
    </div>

    <div class="tablewrap" style="margin-top:24px">
      <table>
        <thead><tr><th>Typical job</th><th>Indicative</th><th>What that assumes</th><th>What sits outside it</th></tr></thead>
        <tbody>{irows}</tbody>
      </table>
    </div>

    <p style="margin-top:24px;max-width:64ch">Read the third and fourth columns before the second one. A
    figure is only meaningful alongside what it assumes, and almost every project that lands above an
    indicative number does so because of the building or the system being replaced rather than because of
    the work itself.</p>

    <p style="margin-top:16px;max-width:64ch">We have deliberately stopped publishing per-outlet and
    per-user rates. A published unit price invites you to multiply it by your own headcount and arrive at a
    number we never quoted, and a figure arrived at that way is the most common reason a price page ends in
    a disagreement. If you want a number for your site, we will look at your site.</p>
  </div>
</section>

{booking_cta()}

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

from layout import MARK, cta, faq_block, cards, related, trust_note

# Deliberately short. Royce's call: a case study is read by a person deciding
# whether to call, and by the client it is about — not skimmed for keywords.
# The 1,500-word standard applies to service pages, not to this.

NUMBERS = [
    ("31 workstations", None, "Up from the 26 first scoped."),
    ("47 monitors", None, "42 of them onto dual arms."),
    ("2 technicians, 1 day", None, "Start to finish."),
]

FAQS = [
    ("Can bcom ICT relocate our office IT?",
     "Yes. For Grow&Co Property Agents' Southport move, bcom ICT collected, transported and set up 31 workstations in a single day with two technicians — around 16 desktops, 8 laptops, 2 Macs and 47 monitors, 42 of them fitted to dual monitor arms. Every machine went to its allocated desk and the team worked from the new office the next business day."),
    ("How long does an office IT relocation take?",
     "This one was a single day for 31 workstations with two technicians, which is a realistic rate where the cabling and outlets are already in and the equipment is labelled. The planning ran across several weeks beforehand; the move itself was one Friday."),
    ("Do you check the new office before the move?",
     "Yes, and we ask for it early. Before this relocation we walked the new floor to confirm the outlets, power and cable trays were ready. It takes about fifteen minutes, and a problem found three weeks out is an email rather than a lost trading day."),
    ("Do you work in Southport?",
     "Yes — bcom ICT is based at Surfers Paradise, a few minutes away, and works across Southport regularly. See <a href=\"/it-support-southport-gold-coast\">IT support in Southport</a>."),
]

PAGE = {
    "path": "/office-relocation-case-study-southport",
    "priority": "0.8",
    "title": "Office IT Relocation — 31 Workstations in a Day | bcom ICT",
    "description": "bcom ICT relocated Grow&Co Property Agents' Southport office — 31 workstations, 47 monitors and a mixed fleet moved, set up and working in a single day.",
    "hero_kind": "doc",
    "eyebrow": "Case study",
    "h1": "31 workstations moved, set up and working in a day",
    "lede": "Grow&Co Property Agents moved office in Southport. We moved the lot, built every desk to their seating plan, and had them working the next morning.",
    "crumbs": [("Case studies", "/case-studies"), ("Office relocation", "/office-relocation-case-study-southport")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT relocated Grow&amp;Co Property Agents&rsquo; Southport office &mdash;
    31 workstations collected, transported and set up in a single day by two technicians, with 47 monitors,
    42 of them fitted to dual arms. Call 07 3041 8993.</p>

    <p style="margin-top:40px">Grow&amp;Co Property Agents were moving a few blocks, from Short Street to a new
    floor in the Premion Building. Thirty-one desks across sales, property management, operations and two
    director offices &mdash; and a business where the phones still ring on a Saturday.</p>

    <p style="margin-top:16px">They had the new floor cabled and powered by others, and their own IT consultant
    handling logins. What they needed from us was the physical job done properly and done in one day: the whole
    fleet moved, every desk built to their seating plan, and the cabling left neat enough to work at.</p>

    <div class="grid grid--3" style="margin-top:40px">{cards(NUMBERS, icon=True)}</div>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>The fifteen minutes that mattered most</h2>
    <p style="margin-top:16px">Weeks before the move we asked to walk the new floor. Not to see the desks
    &mdash; they weren&rsquo;t built yet &mdash; but to check the data outlets, the power and the cable trays
    were actually there and actually enough.</p>
    <p style="margin-top:16px">It took about fifteen minutes. It is also the single thing that separates a move
    that takes a day from one that takes a week, because a gap found three weeks out is an email, and the same
    gap found on moving day is a room full of people who cannot work.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Moving day</h2>
    <p style="margin-top:16px">Only 19 desks could be cleared in the morning, with the other 12 freed up around
    lunchtime as staff finished packing. So we collected the first 19, and the rest came across at midday
    &mdash; sequenced so neither team was standing around waiting for the other.</p>
    <p style="margin-top:16px">The fleet was a mix: Dell, HP, Lenovo and a couple of Macs, with monitors from
    half a dozen makers. Every one had a name and a desk against their seating plan, and the whole point was
    that on Monday nobody had to work out which machine was theirs.</p>
    <p style="margin-top:16px">Seven desks had no computers on them yet. We ran the cabling into those anyway,
    so the next person they hire plugs in rather than waits for a technician.</p>

    <div class="rule">{MARK}</div>

    <h2>What it cost, and what it didn&rsquo;t</h2>
    <p style="margin-top:16px">The job grew while we planned it &mdash; 26 workstations became 29, then 31. The
    price did not move, because the day had been worked out against the job rather than guessed at, and the
    extras were desks rather than complications.</p>
    <p style="margin-top:16px">Where something genuinely would have added time &mdash; unlabelled equipment, a
    floor that wasn&rsquo;t ready &mdash; we said so in writing before anyone committed to anything. Nobody
    likes a surprise on an invoice, least of all the person who has to explain it.</p>

    {trust_note('Thirty-one desks, every machine on the right one, and a team that walked in on Monday and got on with it. For an agency listing and managing property across the Gold Coast, a good move is one where the following week looks like the one before.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Office IT Relocation", "/office-it-relocation-gold-coast"),
  ("IT Support in Southport", "/it-support-southport-gold-coast"),
  ("IT Support for Real Estate", "/it-support-real-estate-gold-coast"),
  ("Office move IT checklist", "/office-move-it-checklist"),
  ("Case studies", "/case-studies"),
], heading="Related")}

{cta("Moving office?",
     "Talk to us before the lease starts. The pre-move check takes fifteen minutes and it is the difference between a move and a lost week.")}
''',
}

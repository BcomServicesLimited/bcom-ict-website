from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We move in three weeks and haven&rsquo;t ordered the internet&rdquo;",
     "lead times nobody checked. A new service at a new address can take considerably longer than a fit-out, and it is the item most often discovered late.",
     "Order services the moment the lease is signed. This is the constraint on almost every office move, and it is the one thing that cannot be solved by working a weekend."),
    ("&ldquo;The new building says it&rsquo;s already cabled&rdquo;",
     "cabling of unknown age, standard and condition, frequently modified by previous tenants and documented by nobody.",
     "Test and certify it before relying on it. Discovering that nine outlets fail on the Monday morning is a very different situation from discovering it three weeks out."),
    ("&ldquo;Nobody knows what&rsquo;s in the comms room&rdquo;",
     "equipment accumulated over a tenancy, some of it live, some of it abandoned by previous occupants, none of it labelled.",
     "Document what exists and what it does before anything is unplugged. The move is when undocumented dependencies surface, and the middle of a move is the worst moment to find them."),
    ("&ldquo;We&rsquo;ll just move the phones ourselves&rdquo;",
     "an underestimate. Numbers, services and cabling all have to align at the new site, and phones are typically left until last.",
     "Treat phones as a lead item rather than a moving-day task. It is the part of a relocation with the least tolerance for running late and the most external dependencies."),
    ("&ldquo;Can the server just go in the boot?&rdquo;",
     "an understandable question and a genuine risk. Servers are heavy, delicate, and hold everything the business runs on.",
     "Move it deliberately, with a verified backup taken first and a tested way back. The backup before a move is not a formality &mdash; it is the only thing standing between a bad journey and a lost business."),
    ("&ldquo;Staff arrive Monday and nothing works&rdquo;",
     "a cutover completed but never tested, or tested only by the people who did it.",
     "Test as a user before anyone arrives &mdash; log in, print, call out, open a file, reach the internet. The gap between it is connected and it works is where lost trading days live."),
]

EXAMPLE_1 = example(
    "Testing the new building three weeks out instead of on the Monday",
    "A firm was relocating over a single weekend to a floor the landlord described as cabled and ready. Forty positions, and staff expected to be working on Monday morning.",
    "Certification three weeks before the move found a mix of cable standards with no records distinguishing them and nine runs that failed outright, two of them serving the room intended for the comms cabinet. The internet service, ordered a fortnight earlier, had a connection date four days after the move. Both problems were entirely solvable with three weeks in hand and neither was solvable on a Sunday night.",
    "Replaced the nine failed runs, escalated the service order with the provider and arranged a temporary mobile broadband service as cover, then configured and tested everything before the move weekend.",
    "The firm moved on Saturday and worked on Monday. The permanent service connected on the Thursday as revised, by which point nobody had noticed, because the cover had been arranged rather than improvised.")

EXAMPLE_2 = example(
    "The dependency that surfaced when a cable was unplugged",
    "A business was moving premises and had documented what it believed was in the comms room &mdash; the server, the switching, the router and the phone system.",
    "Tracing everything before disconnection found a small unlabelled device that turned out to be a monitored alarm dialler, and a second connection feeding a card reader on the front door of a part of the building the business shared with another tenant. Neither appeared in any documentation and neither belonged to anything anyone had thought about. Unplugging the rack without tracing it first would have disabled a monitored alarm and locked a shared entrance.",
    "Identified every connection and what it served before anything was touched, arranged the alarm and door access separately with their own providers, and moved the rest as planned.",
    "Nothing was discovered by failing. The tracing added half a day to the preparation and removed two problems that would have appeared on a Sunday evening with nobody available to resolve them.")

EXAMPLE_3 = example(
    "Testing as a user rather than as an installer",
    "A business completed a weekend relocation. Everything had been connected, powered and confirmed working by the team doing the move before they left on Sunday evening.",
    "Staff arrived Monday and could not print, and half of them could not reach a shared drive. Nothing had been done incorrectly. The testing had confirmed that each device was connected and responding, which was true, and had not confirmed that an ordinary person sitting at an ordinary desk could log in, open a file, print it and make a call. The printers were reachable and the print queues on the workstations still pointed at addresses from the old premises. The shared drive was online and the mapping used a server name resolved by a system that had not yet been repointed.",
    "Worked through the office desk by desk on the Monday morning to restore normal working, then rebuilt the checklist so a relocation ends with somebody sitting at a real desk performing the five things staff do first, rather than with a list of devices confirmed as responding.",
    "The business lost most of a morning rather than a day. Every subsequent move we have run finishes with that user-level test, because the gap between it is connected and it works is precisely where a lost trading day lives.")
FAQS = [   (   'How far ahead should we plan an office IT move?',
        'Start at least six to eight weeks out, and earlier if the new site needs carrier services provisioned. NBN, fibre and phone line lead times are the most common reason an office move slips — '
        'the physical work is the easy part. bcom ICT surveys both sites and orders carrier services against your move date rather than after it.'),
    (   'Will we lose phone numbers?',
        "No. Number porting is planned and started well ahead of the move rather than attempted on the day. That includes legacy PBX systems where you're relocating rather than replacing."),
    (   'Can you do it over a weekend?',
        "That's the usual approach. Non-critical equipment moves first, servers and phones cut over last, and everything is tested before staff arrive Monday. Larger estates sometimes need a staged "
        'move across two weekends.'),
    (   'Do you handle the cabling at the new site?',
        'Yes, as part of the job. Fixed cabling legally requires a registered cabler in Australia, so that portion is carried out by ACMA registered cabling contractors we engage and manage — you '
        'deal with one point of contact and get testing documentation on completion.'),
    (   "What if the new site isn't ready?",
        "We'll tell you during the survey rather than on moving day. Missing power, no viable comms room location or insufficient data points are all cheap to solve six weeks out and very expensive "
        'to solve on a Saturday.')]

PAGE = {
    "path": '/office-it-relocation-gold-coast',
    "priority": '0.75',
    "service": 'Office IT Relocation Gold Coast',
    "title": 'Office IT Relocation Gold Coast — Planned & Tested | bcom ICT',
    "description": 'Planned office IT relocations for Gold Coast businesses. Servers, networks, cabling, phone systems and workstations moved and tested before your team arrives. Call 07 3041 8993.',
    "hero_img": 'hero-bg-business.webp',
    "hero_alt": 'bcom ICT relocating servers and network equipment for a Gold Coast office move',
    "h1": 'Moving office without losing a trading day',
    "lede": 'Servers, networks, cabling and phones planned, moved and tested over a weekend — so Monday morning is uneventful.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Weekend cutovers', 'Carrier lead times managed', 'Tested before handover', 'Since 2011'],
    "crumbs": [('Services', '/services'), ('Office IT Relocation', '/office-it-relocation-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT plans and delivers office IT relocations for Gold Coast businesses — moving servers, networks, structured cabling, phone systems and workstations, then testing everything before staff arrive. Cutovers are typically staged across a weekend to avoid losing a trading day. Call 07 3041 8993.', blocks=[       {       'cards': [       (       'Carrier lead times',
                                         None,
                                         'NBN, fibre and phone line provisioning at a new site can take '
                                         'weeks, and nobody tells you that until you ask. This is the single '
                                         'most common reason a move slips — it needs starting long before '
                                         'the boxes are packed.'),
                                 (       'Nobody surveyed the new site',
                                         None,
                                         'No comms room, no power where the rack needs to go, not enough '
                                         'data points, or cabling that terminates somewhere unhelpful. Cheap '
                                         'to find early, expensive to discover on moving day.'),
                                 (       'Number porting left too late',
                                         None,
                                         'Porting business phone numbers takes time and cannot be rushed on '
                                         'the day. Started late, you open at the new address with no '
                                         'phones.'),
                                 (       'Nobody tested before Monday',
                                         None,
                                         'Equipment that was working before the move is assumed to work '
                                         'after it. Printers, scanners, EFTPOS and shared drives are where '
                                         'that assumption usually breaks.')],
                'cols': 2,
                'eyebrow': 'Why moves go wrong',
                'h2': "It's almost never the moving day",
                'icon': False,
                'sub': 'Office IT moves fail on lead times and assumptions, not on the physical work.'},
        {       'cols': 4,
                'eyebrow': 'How we run it',
                'h2': 'Four stages, starting well before the move',
                'steps': [       (       'Survey both sites',
                                         'What you have, what the new site can take, where the comms room '
                                         'goes, how many data points are needed and what has to be cabled.'),
                                 (       'Order early',
                                         'Carrier services, number porting and any cabling booked against '
                                         'the move date with the lead times built in, not discovered.'),
                                 (       'Stage the cutover',
                                         'Usually across a weekend. Non-critical equipment moves first; '
                                         'servers and phones cut over last, in a planned order.'),
                                 (       'Test before handover',
                                         'Every workstation, printer, phone, EFTPOS terminal and shared '
                                         'drive checked working before anyone arrives Monday.')]},
        {       'h2': "What's in scope",
                'ticks': [       'Server and network equipment decommissioned, moved and recommissioned',
                                 'Structured cabling at the new site — installed by ACMA registered cabling '
                                 'contractors we engage and manage',
                                 'Phone system relocation and number porting, including legacy PBX where '
                                 "you're keeping it",
                                 'Internet and carrier services ordered, provisioned and tested against the '
                                 'move date',
                                 'Workstations, printers, scanners and EFTPOS moved, reconnected and '
                                 'verified',
                                 'Updated documentation and asset register handed to you at the end']}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The relocation problems we are actually called to</h2>
      <p>Six situations. Five of them are decided weeks before the move, and one of them cannot be fixed on the weekend.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a planned relocation looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Case study</span>
      <h2>31 workstations, one day</h2>
      <p>How bcom ICT relocated Grow&amp;Co Property Agents&rsquo; Southport office &mdash; the whole fleet moved,
      built to their seating plan and working the next business day.
      <a href="/office-relocation-case-study-southport">Read the case study</a>.</p>
    </div>
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Business WiFi', '/business-wifi-gold-coast'),
        ('Office move IT checklist', '/office-move-it-checklist'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('Got a move date?', 'Tell us when and where. The earlier we survey, the fewer surprises there are — and carrier lead times wait for nobody.'),
}

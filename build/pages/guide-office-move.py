from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We&rsquo;ll sort the internet closer to the date&rdquo;",
     "the belief that a connection can be arranged quickly. A new service at a new address frequently takes longer than the entire fit-out, and no amount of weekend work compensates for it.",
     "Order it the day the lease is signed. This is the only item on a move that cannot be solved by working harder later, and it is the one most often left until it is too late."),
    ("&ldquo;The new place is already cabled&rdquo;",
     "a statement from a landlord or agent about cabling of unknown age, standard and condition, almost always modified by previous tenants and documented by nobody.",
     "Have it tested and certified weeks out. Finding nine failed outlets three weeks before a move is an inconvenience; finding them on the Monday morning is a lost trading day."),
    ("&ldquo;The removalists will handle the computers&rdquo;",
     "an assumption about scope. Removalists move furniture competently and are not being engaged to disconnect a server, label a rack or preserve a configuration.",
     "Separate the IT move from the furniture move and treat it as its own project. They happen on the same weekend and they are not the same job."),
    ("&ldquo;The phones can just be redirected&rdquo;",
     "an underestimate of what phones need. Numbers, services and cabling must all align at the new site, and each has its own lead time.",
     "Treat phones as a lead item, not a moving-day task. It is the part of a relocation with the least tolerance for delay and the most external dependencies."),
    ("&ldquo;We&rsquo;ll work out what&rsquo;s in the comms room on the day&rdquo;",
     "equipment accumulated across a tenancy, some live, some abandoned by previous occupants, none labelled. The day of the move is when undocumented dependencies surface.",
     "Trace and document everything before anything is unplugged. Alarms, door access and monitored services hide in racks and are discovered by being switched off."),
    ("&ldquo;We&rsquo;ll test it on Monday&rdquo;",
     "the difference between connected and working. Confirming that devices respond is not the same as confirming that a person can do their job.",
     "Test as a user before staff arrive &mdash; log in, open a file, print it, make a call, reach the internet. That five-minute check is where lost trading days are prevented."),
]

EXAMPLE_1 = example(
    "The service order that decided the whole timeline",
    "A firm signed a lease with eight weeks before occupation and a fit-out scheduled to take six. The internet service was noted as an action item and picked up in week four, which felt comfortable at the time.",
    "The connection date offered for the new address was eleven weeks out &mdash; three weeks after the business was due to be trading there. Nothing had gone wrong; the address simply had a lead time, which is normal and is not something a business finds out until it asks. Had the order been placed in week one, the date would have fallen comfortably before the move.",
    "Escalated the order with the provider, which recovered some time but not all of it, and arranged a temporary mobile broadband service sized for the office to cover the gap.",
    "The firm traded from day one on temporary connectivity and transitioned to the permanent service three weeks later without incident. It cost a few hundred dollars and a fortnight of mild inconvenience, all of which was avoidable by making one phone call in week one.")

EXAMPLE_2 = example(
    "What was actually in the rack",
    "A business documented its comms room before a move &mdash; server, switching, router, phone system &mdash; and considered the inventory complete. It was accurate as far as it went.",
    "Tracing every connection before disconnection found two devices nobody could account for. One was a monitored alarm dialler. The other fed a card reader on a shared entrance used by another tenant in the building, installed years earlier under an arrangement neither party could now explain. Both would have been switched off on Friday evening with nobody aware until something needed them.",
    "Identified what every connection served before anything was touched, arranged the alarm and the door access separately with their own providers, and moved the rest as planned.",
    "Nothing was discovered by failing. Half a day of tracing removed two problems that would otherwise have appeared on a Sunday night with nobody available to fix them.")

FAQS = [   (   'How far in advance should we plan an office IT move?',
        'Six to eight weeks, and earlier if the new site needs carrier services provisioned. NBN, fibre and phone line lead times are the most common reason an office move slips — the physical '
        'equipment move is the easy part. Number porting also needs starting well ahead rather than on the day.'),
    (   "What's the most common thing that goes wrong?",
        "Internet not being live at the new site on day one, because it was ordered too late. Everything else depends on it — phones, payments, cloud applications and remote access. It's the first "
        'thing to order and the last thing anyone thinks of.'),
    (   'Will we lose our phone numbers?',
        'Not if porting is started ahead of the move rather than attempted on the day. That applies to legacy PBX systems being relocated as well as to cloud phone systems.'),
    (   'Can the move happen over a weekend?',
        'Usually. Non-critical equipment moves first, servers and phones cut over last, and everything is tested before staff arrive Monday. Larger estates sometimes need staging across two '
        'weekends.'),
    (   'Should we replace equipment as part of the move?',
        "It's a natural moment to do it. Anything you'd otherwise limp along with for another year is worth replacing rather than paying to move twice. A fleet assessment before the move usually "
        'pays for itself.'),
    (   'Do we need new cabling at the new site?',
        "Test rather than assume. Existing points are frequently the wrong category, in the wrong place, or simply non-functional. A survey establishes what's usable before you plan around it.")]

PAGE = {
    "path": '/office-move-it-checklist',
    "priority": '0.7',
    "article": True,
    "title": 'Office Move IT Checklist — Australian Business | bcom ICT',
    "description": "A practical IT checklist for an office move, in order and by timeline. Carrier lead times, number porting, cabling, cutover and testing.",
    "hero_kind": 'page',
    "eyebrow": "Guide",
    "hero_img": 'hero-bg-business.webp',
    "hero_alt": 'IT equipment being prepared for an office relocation by bcom ICT',
    "h1": 'Office move IT checklist',
    "lede": 'Office IT moves almost never fail on moving day. They fail six weeks earlier, on the things nobody started in time.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Start 6–8 weeks out', 'Carrier lead times', 'Weekend cutover', 'Tested before Monday'],
    "crumbs": [("Guides", "/services"), ('Office move IT checklist', '/office-move-it-checklist')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='An office IT move should start six to eight weeks before the move date. The critical path is carrier services — NBN, fibre and phone line provisioning at the new site can take weeks — followed by number porting, cabling and a staged weekend cutover with everything tested before staff arrive. The physical equipment move is the easiest part.',
                     blocks=[       {       'eyebrow': '6–8 weeks out',
                'h2': 'Start these now or the date slips',
                'ticks': [       '<strong>Order carrier services at the new site.</strong> NBN, fibre or '
                                 'business internet provisioning is the single most common reason an '
                                 'office move slips. Lead times can run to weeks and nobody volunteers '
                                 'that.',
                                 '<strong>Survey the new site.</strong> Where the comms room goes, whether '
                                 "there's power and ventilation for it, how many data points are needed "
                                 'and where. Cheap to solve now, expensive on moving day.',
                                 '<strong>Check what cabling exists.</strong> Existing points may be the '
                                 'wrong category, wrong location or non-functional. Assume nothing without '
                                 'testing.',
                                 '<strong>Start number porting.</strong> Business numbers take time to '
                                 'port and it cannot be rushed on the day.',
                                 '<strong>Check your lease obligations at the old site</strong> — '
                                 'make-good frequently includes removing cabling you installed.']},
        {       'eyebrow': '3–4 weeks out',
                'h2': 'Plan and order',
                'ticks': [       'Book the cabling installation, allowing time for it to be tested before '
                                 'the move',
                                 'Decide what moves and what gets replaced — an office move is a natural '
                                 "point to retire equipment you'd otherwise limp along with",
                                 'Confirm building access at both ends: loading dock, service lift '
                                 'bookings, after-hours access, security passes',
                                 'Plan the cutover sequence — what moves first, what moves last, and what '
                                 'has to be working before anything else',
                                 'Tell your staff what to expect and when, including what they need to '
                                 'take home']},
        {       'eyebrow': 'The week of',
                'h2': 'Cutover',
                'ticks': [       "<strong>Verify the new site's internet is live and tested</strong> "
                                 'before anything else moves. Everything depends on it.',
                                 'Back up everything, and verify the backup, before a single machine is '
                                 'unplugged',
                                 'Label everything — cables, monitors, docks, phones. It costs an hour and '
                                 'saves a day',
                                 'Move non-critical equipment first, servers and phones last',
                                 '<strong>Test before anyone arrives:</strong> every workstation, printer, '
                                 'scanner, phone, EFTPOS terminal and shared drive']},
        {       'cards': [       (       'Carrier lead times',
                                         None,
                                         'By far the most common cause of a slipped move. Order at the new '
                                         'site before you order anything else.'),
                                 (       'Number porting left late',
                                         None,
                                         'Attempted on the day, it fails. You open at the new address with '
                                         "no phones, and there's no quick fix."),
                                 (       'No comms room at the new site',
                                         None,
                                         'Or one with no power, no ventilation, or in a location nothing '
                                         'can reach. Found during a survey; disastrous on a Saturday.'),
                                 (       'Nothing tested before Monday',
                                         None,
                                         'Equipment that worked before the move is assumed to work after '
                                         'it. Printers, scanners, EFTPOS and shared drives are where that '
                                         'assumption reliably breaks.')],
                'cols': 2,
                'h2': 'The five that catch people out',
                'icon': False}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What people get wrong about moving an office</h2>
      <p>Six assumptions that turn a planned move into a lost trading day.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in practice</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast')])
            + cta('Got a move date?', 'The earlier we survey both sites, the fewer surprises there are — and carrier lead times wait for nobody.'),
}

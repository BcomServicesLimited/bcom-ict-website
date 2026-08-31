from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;Dockets stop printing in the kitchen&rdquo;",
     "the kitchen printer dropping off the network, often because it sits behind a wall of stainless steel and is on wireless when it should be cabled.",
     "Cable the kitchen printer wherever it can be reached, and give it a fixed address. A kitchen that stops receiving dockets during service is a stopped restaurant, and it is one of the cheapest faults to design out."),
    ("&ldquo;Delivery platform orders aren&rsquo;t reaching us&rdquo;",
     "a tablet that has gone to sleep, lost its wireless connection, or logged itself out. Orders continue to be accepted at the platform end regardless.",
     "Keep the ordering tablets powered, awake and on a network that reaches them properly, and check them at the start of every service. Missed delivery orders damage a venue&rsquo;s rating as well as its takings."),
    ("&ldquo;Terminals lose the POS server mid-service&rdquo;",
     "a network under load, or a server that has become the busiest device in the building without anyone noticing.",
     "Watch what actually happens during service rather than testing at three in the afternoon. Faults in restaurants keep restaurant hours, and diagnosis has to happen when the fault does."),
    ("&ldquo;Ordering works at some tables and not others&rdquo;",
     "wireless coverage designed for the room as an empty space. A full dining room of people and furniture absorbs signal in ways an empty one does not.",
     "Survey with the venue in a realistic state and put coverage where the tables are. Courtyards, mezzanines and anywhere behind a service area are the usual dead spots."),
    ("&ldquo;It only ever breaks on Friday and Saturday night&rdquo;",
     "load. Everything works at low volume, and the design limit is reached only when the venue is full &mdash; which is precisely when it is most expensive.",
     "Size the network for the busiest hour, not the average one. A system that copes on a Tuesday and fails on a Saturday is not intermittent; it is undersized, and it will fail every Saturday."),
    ("&ldquo;Nobody can help us at eight on a Saturday&rdquo;",
     "a fair complaint. Our business hours are eight to five on weekdays, and we say so rather than implying otherwise.",
     "Design the venue so that a single failure cannot stop service &mdash; offline-capable terminals, a mobile backup for payments, a printed fallback the staff have practised. Prevention is what protects a Saturday night, because no response time is fast enough once service has started."),
]

EXAMPLE_1 = example(
    "The Saturday night failure that was arithmetic",
    "A restaurant reported that its ordering terminals became unusable on Friday and Saturday evenings and were faultless the rest of the week. Two providers had attended, both midweek, and both found nothing wrong.",
    "The venue ran everything &mdash; terminals, kitchen printer, delivery tablets, office computer, music and guest WiFi &mdash; through a single consumer access point mounted above the bar. On a Tuesday that device handled around fifteen connections. On a Saturday it handled over a hundred, most of them guest phones, and it reached its limit around the time the kitchen did.",
    "Separated guest WiFi from venue systems entirely, cabled the kitchen printer and the terminals, and installed access points sized for a full room with the payment devices on their own segment.",
    "Service ran through the following Saturday without an incident. The fault had never been intermittent &mdash; it had been perfectly predictable, and it only ever appeared when nobody could afford to look at it.")

EXAMPLE_2 = example(
    "Four months of delivery orders quietly declined",
    "A caf&eacute; had signed up to a delivery platform and concluded the platform did not work in their area. Orders were rare and their rating had fallen far enough that they were considering withdrawing.",
    "The platform tablet was on a power adaptor that had stopped charging it. Staff would find it flat, plug it in, and it would come back logged out. Orders arriving while it was asleep or logged out were auto-declined after a timeout, which the platform recorded against the venue as a rejection. The venue had never seen the orders and did not know they had been offered.",
    "Replaced the adaptor, mounted the tablet on permanent power within wireless range, disabled the sleep behaviour, and added a start-of-service check to the opening routine.",
    "Orders resumed immediately and the rating recovered over the following months. Four months of trade had been lost to a failed power adaptor and a device nobody had been given responsibility for.")

FAQS = [   (   'What IT support does a restaurant need?',
        'Keeping point of sale and EFTPOS running through service is the priority — which means a reliable network, automatic 4G or 5G failover, payment terminals segmented from other traffic, and '
        'WiFi that covers the whole venue including outdoor areas. Online ordering integrations and kitchen printers matter next. bcom ICT supports Gold Coast restaurants and cafés and answers '
        '8am to 5pm Monday to Friday.'),
    (   'Our EFTPOS drops out at busy times. Why?',
        "Usually the network rather than the terminal — WiFi saturated by staff phones, ordering tablets and guest devices all competing, or an access point that cannot cover the whole venue. It's "
        "measurable, and it's almost never fixed by replacing the terminal."),
    (   'What happens if the internet goes down during service?',
        "With automatic 4G or 5G failover, payments keep working and the changeover needs nobody's attention. Without it, you stop taking card. For a venue, that single piece of configuration "
        "usually pays for itself the first time it's needed."),
    (   'Can you support our online ordering integration?',
        "We support the environment and connectivity it depends on, and work with your POS vendor on the integration itself. Broken integrations tend to fail silently — orders simply don't arrive — "
        'so monitoring them matters more than people expect.'),
    (   'Do you work outside business hours?',
        'Business hours are 8:00am to 5:00pm Monday to Friday, Brisbane time. After hours our AI operator takes details and escalates. Managed and SLA clients have after-hours emergency attendance '
        'included, which for a venue trading at night is usually the arrangement that makes sense.'),
    (   'How quickly can you get to us?',
        'Same-day attendance is usually available across the Gold Coast, and many faults are diagnosed remotely within minutes. For a venue, the more useful conversation is what we can prevent '
        'rather than how fast we arrive.')]

PAGE = {
    "path": '/it-support-restaurants-gold-coast',
    "priority": '0.75',
    "title": 'IT Support for Gold Coast Restaurants & Cafés | bcom ICT',
    "description": "IT support for Gold Coast restaurants and cafés. POS and EFTPOS uptime through service, online ordering integrations, and a network that doesn't drop at 7pm.",
    "hero_img": 'it-support-restaurants-gold-coast-hero.webp',
    "hero_alt": 'Point of sale and ordering systems supported by bcom ICT for a Gold Coast restaurant',
    "h1": 'Nothing can break during service',
    "lede": "A restaurant's IT has a two-hour window where failure is unacceptable, and margins that don't absorb a lost night. That shapes everything.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Built for service hours', 'EFTPOS failover', 'Ordering integrations', 'Digital assistant after hours'],
    "crumbs": [('Industries', '/industries'), ('Restaurants & cafés', '/it-support-restaurants-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supports restaurants and cafés across the Gold Coast — point of sale and EFTPOS uptime through service, online ordering and delivery platform integrations, kitchen display systems, and the network underneath them, with automatic 4G or 5G failover so an internet outage does not stop you taking payment. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Failure has a schedule',
                                         None,
                                         'An office can lose an hour on a Tuesday morning and absorb it. A '
                                         'restaurant losing the POS at 7pm on a Saturday loses the night. '
                                         'The same fault has a completely different cost depending on when '
                                         'it lands.'),
                                 (       "Margins don't absorb it",
                                         None,
                                         'Hospitality runs tight. A lost service is not an inconvenience '
                                         'to be written off — which is why prevention and failover matter '
                                         'more here than almost anywhere else.'),
                                 (       'Nobody has time to troubleshoot',
                                         None,
                                         'Mid-service, nobody is going to methodically diagnose a network '
                                         'fault. Systems need to fail over automatically or not fail at '
                                         'all.'),
                                 (       'Staff turnover is constant',
                                         None,
                                         'New people every few weeks, all needing POS access. Accounts '
                                         'have to be added and — more importantly — removed promptly.')],
                'cols': 2,
                'eyebrow': 'The shape of the problem',
                'h2': 'Hospitality IT is a timing problem',
                'icon': False},
        {       'h2': 'What we make sure of',
                'ticks': [       '<strong>Automatic 4G or 5G failover</strong>, so an internet outage '
                                 "doesn't stop card payments. The single highest-value thing a venue can "
                                 'do.',
                                 '<strong>Payment terminals segmented</strong> from staff devices and '
                                 'guest WiFi — expected practice under PCI-DSS and cheap to build in',
                                 '<strong>WiFi that covers the whole venue</strong>, including the terrace '
                                 'and the kitchen, because tablets and handhelds are used everywhere',
                                 '<strong>Online ordering and delivery integrations</strong> kept talking '
                                 'to the POS, since a broken integration loses orders silently',
                                 '<strong>Kitchen display and printer reliability</strong> — a docket '
                                 'printer that stops mid-service is a genuine emergency',
                                 '<strong>Guest WiFi isolated</strong> from everything operational',
                                 '<strong>Mon–Fri 8am–5pm</strong>, which matters when your trading '
                                 'hours are not office hours']},
        {       'h2': 'Prevention is the whole game',
                'html': '<p style="max-width:68ch">Most of what we do for hospitality happens before '
                        'service. Equipment on backup power so a brief outage does not take the POS down '
                        'mid-transaction. Failover tested rather than assumed. Updates scheduled for '
                        'Tuesday morning, never Friday afternoon.</p><p '
                        'style="max-width:68ch;margin-top:16px">And a straight answer about what your '
                        'network can actually carry. Venues frequently run POS, ordering tablets, music, '
                        'cameras, staff phones and guest WiFi over a connection and access point specified '
                        'for far less — see <a href="/business-wifi-gold-coast">business WiFi</a>.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The problems we are actually called to in venues</h2>
      <p>Restaurant faults are timing problems. Six situations account for nearly all of them.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in a venue</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Hospitality & accommodation', '/it-support-hospitality-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast')])
            + cta('What happens if the POS drops on Saturday night?', "If you don't have an answer, that's the conversation to have on a quiet Tuesday rather than during service."),
}

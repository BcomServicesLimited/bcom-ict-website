from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What IT support does a restaurant need?',
        'Keeping point of sale and EFTPOS running through service is the priority — which means a reliable network, automatic 4G or 5G failover, payment terminals segmented from other traffic, and '
        'WiFi that covers the whole venue including outdoor areas. Online ordering integrations and kitchen printers matter next. bcom ICT supports Gold Coast restaurants and cafés and answers '
        'phones 24/7.'),
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
        'Phones are answered 24/7, including weekends and public holidays. After hours our AI operator takes details and escalates. Managed and SLA clients have after-hours emergency attendance '
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
    "trust": ['Built for service hours', 'EFTPOS failover', 'Ordering integrations', 'Answered 24/7'],
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
                                 '<strong>Phones answered 24/7</strong>, which matters when your trading '
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
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Hospitality & accommodation', '/it-support-hospitality-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast')])
            + cta('What happens if the POS drops on Saturday night?', "If you don't have an answer, that's the conversation to have on a quiet Tuesday rather than during service."),
}

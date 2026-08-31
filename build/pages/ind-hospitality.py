from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What does a hotel or venue need from its IT provider?',
        'Guest WiFi designed for whole-property coverage and high device density, full network segmentation keeping guests away from booking and payment systems, reliable connectivity for the '
        'property management system, payment terminal separation across all outlets, and account management that keeps up with seasonal staff turnover. bcom ICT supports Gold Coast accommodation and '
        'venues on all of it.'),
    (   'Our guest WiFi works in the lobby but not the rooms. Why?',
        "Almost always coverage design rather than the internet service. Concrete, tiled bathrooms, lift shafts and long corridors block signal, and equipment placed on a guess won't reach. It needs "
        'a survey and properly positioned access points — adding extenders generally makes roaming worse.'),
    (   'Can guests reach our booking system?',
        "They shouldn't be able to, and on a properly segmented network they can't. Guest WiFi should be internet-only with no route to booking, payment, back office or building systems. If nobody "
        "can tell you whether that's the case at your property, it's worth checking."),
    (   'How do we handle constant staff turnover?',
        'By treating account lifecycle as a control rather than admin. Accounts created quickly for new casuals and — the part that matters — removed the day someone leaves. Managed clients get this '
        'as part of the arrangement.'),
    (   'Do you support function and conference connectivity?',
        "Yes, and it needs designing for the room at capacity rather than the room empty. Function space WiFi tends to be judged at exactly the moment it's under most load."),
    (   'What about our restaurant or bar POS?',
        'Same considerations as any venue — payment terminals segmented, automatic internet failover so card payments continue through an outage, and WiFi that covers outdoor and terrace areas. See '
        'our restaurants and cafés page.')]

PAGE = {
    "path": '/it-support-hospitality-gold-coast',
    "priority": '0.75',
    "title": 'IT Support for Gold Coast Hospitality & Accommodation | bcom ICT',
    "description": 'IT support for Gold Coast hotels, venues and accommodation. Guest WiFi at scale, booking system uptime, payment segmentation and seasonal staff account management.',
    "hero_img": 'it-support-hospitality-gold-coast-hero.webp',
    "hero_alt": 'Guest WiFi and venue systems supported by bcom ICT for a Gold Coast hospitality business',
    "h1": 'Guest WiFi is now part of the product',
    "lede": 'On the Gold Coast, guests review the WiFi. Covering a whole property properly — while keeping guests nowhere near your booking and payment systems — is a specific job.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Guest WiFi at scale', 'Booking system uptime', 'Payment segmentation', 'Seasonal turnover handled'],
    "crumbs": [('Industries', '/industries'), ('Hospitality', '/it-support-hospitality-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supports hotels, venues and accommodation businesses across the Gold Coast — guest WiFi designed for whole-property coverage and high device density, booking and property management system uptime, payment terminal segmentation, and account management for high seasonal staff turnover. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Guests review the WiFi',
                                         None,
                                         'On the Gold Coast, connectivity shows up in guest reviews and '
                                         'affects bookings. Coverage across rooms, common areas, pool '
                                         'decks and function spaces is a product decision, not an IT one — '
                                         'and it needs surveying rather than estimating.'),
                                 (       'Device density is extreme',
                                         None,
                                         'Every guest arrives with three devices. A property that would '
                                         'need a handful of access points for staff needs considerably '
                                         'more for guests, and the difference is not a matter of turning '
                                         'the power up.'),
                                 (       'Guests must reach nothing internal',
                                         None,
                                         'Guest networks isolated from booking systems, payment terminals, '
                                         'back office and building systems. This is the security '
                                         'requirement that matters most and the one most often built '
                                         'badly.'),
                                 (       'Seasonal turnover is relentless',
                                         None,
                                         'Casual staff arriving and leaving constantly, all needing system '
                                         'access. Prompt removal of accounts is a genuine control in this '
                                         'industry rather than an administrative nicety.')],
                'cols': 2,
                'eyebrow': "What's different",
                'h2': 'A venue is not an office with more people',
                'icon': False},
        {       'h2': 'What we design and support',
                'ticks': [       '<strong>Guest WiFi surveyed and designed</strong> for whole-property '
                                 'coverage and real device density, not estimated from a floor plan',
                                 '<strong>Full network segmentation</strong> — guests, staff, payments, '
                                 'cameras and building systems each isolated from the others',
                                 '<strong>Booking and property management system</strong> connectivity, '
                                 'uptime and backup',
                                 '<strong>Payment terminal separation</strong>, PCI-DSS-aligned, across '
                                 'restaurant, bar, reception and function spaces',
                                 '<strong>Function and conference connectivity</strong> that works when a '
                                 'room fills, because that is when it is noticed',
                                 '<strong>Account lifecycle management</strong> for seasonal staff — added '
                                 'quickly, removed promptly',
                                 "<strong>Internet with automatic failover</strong>, so an outage doesn't "
                                 'take reception and payments down together']},
        {       'h2': 'Coverage is the part that gets underestimated',
                'html': '<p style="max-width:68ch">The most common problem we are called to in Gold Coast '
                        'accommodation is guest WiFi that works in the lobby and fails in the rooms. '
                        'Concrete, tiled bathrooms, lift shafts and long corridors are difficult, and '
                        'consumer-grade equipment installed on a guess will not cover them.</p><p '
                        'style="max-width:68ch;margin-top:16px">Getting it right means surveying the '
                        'property, designing access point placement and cabling around the actual '
                        'construction, and using equipment built for density — see <a '
                        'href="/business-wifi-gold-coast">business WiFi installation</a>. It costs more '
                        'upfront than adding extenders and it is the only approach that actually '
                        'works.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Restaurants & cafés', '/it-support-restaurants-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('Guests complaining about the WiFi?', "We'll survey the property and tell you what coverage actually requires — including where the current equipment was never going to reach."),
}

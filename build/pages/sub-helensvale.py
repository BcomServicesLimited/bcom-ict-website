from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Helensvale?',
        'Yes. bcom ICT attends Helensvale businesses from its Surfers Paradise office, roughly twenty-five minutes away, with same-day attendance usually available. Most faults are resolved remotely '
        'at $198 + GST per hour with no call-out. Call 07 3041 8993.'),
    (   'Is Helensvale too far for same-day support?',
        'No. Same-day attendance is usually available across the whole Gold Coast, and remote support often has people working again within minutes of a call — well before anyone could drive '
        'anywhere.'),
    (   'Our business has grown quickly. What should we look at?',
        "Usually the network, which was specified for a smaller business and hasn't been revisited. Then backups you've actually seen restore and multi-factor authentication on every account. The "
        'review is free and you keep the report.'),
    (   'Can you support multiple sites across the northern corridor?',
        'Yes. Multi-site is straightforward with the right design — one standard across sites, centrally managed and remotely supported, rather than each location running whatever it accumulated.')]

PAGE = {
    "path": '/it-support-helensvale-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Helensvale — Business | bcom ICT',
    "description": 'IT support for Helensvale businesses — retail, professional practices and service businesses across the northern Gold Coast growth corridor.',
    "hero_img": 'hero-bg-business.webp',
    "hero_alt": 'A Helensvale business supported by bcom ICT',
    "h1": 'IT support for Helensvale businesses',
    "lede": 'Northern growth corridor, newer commercial space, and a lot of businesses whose systems were set up when they were half the size.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~25 min from our office', 'Northern corridor', 'Remote-first where we can', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Helensvale', '/it-support-helensvale-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT supports businesses in Helensvale — retail, professional practices, medical and service businesses across the northern Gold Coast corridor. Attendance is roughly twenty-five minutes from bcom ICT's Surfers Paradise office, with most faults resolved remotely. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Newer commercial space',
                                         None,
                                         'Much of the business accommodation here is relatively recent, '
                                         'which usually means workable comms rooms and structured cabling '
                                         'already in place. Fewer surprises than the older parts of the '
                                         'coast.'),
                                 (       'Businesses growing faster than their systems',
                                         None,
                                         'The common pattern in a growth corridor: headcount doubles, the '
                                         "network doesn't change, and nothing fails until it all does at "
                                         'once. Worth reviewing before that point rather than after.'),
                                 (       'Serving a wide catchment',
                                         None,
                                         'A lot of Helensvale businesses serve the northern corridor and '
                                         'beyond, which means staff on the road, multiple sites, or both. '
                                         'Phones and remote access matter more than a fixed office setup.'),
                                 (       'Remote support does most of it',
                                         None,
                                         'At twenty-five minutes out, we resolve what we can remotely — '
                                         '$198 + GST per hour with no call-out — and book a visit only '
                                         'when the fault genuinely needs someone there.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'Growth corridor businesses',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       'Retail and service businesses around Westfield Helensvale and the '
                                 'surrounding centres',
                                 'Medical and allied health practices',
                                 'Professional practices serving the northern corridor',
                                 'Businesses with staff split across multiple northern sites',
                                 'Trades and service operations based north of Nerang']}])
            + faq_block(FAQS)
            + nearby('/it-support-helensvale-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Remote IT Support', '/remote-it-support-gold-coast')])
            + cta('Grown out of your setup?', "The free review tells you what's actually straining and what to fix first — no obligation either way."),
}

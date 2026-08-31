from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Surfers Paradise?',
        "Yes — bcom ICT's office is at 9 Ferny Avenue, Surfers Paradise. Attendance within the suburb is usually available within the hour during business hours, and phones are answered 24/7 "
        'including weekends and public holidays. Call 07 3041 8993.'),
    (   'How quickly can you get to a Surfers Paradise business?',
        "Usually within the hour during business hours, since we're based in the suburb. Building access in high-rise towers occasionally adds time — service lift bookings and building management "
        'approvals — which we arrange in advance where the work needs it.'),
    (   'Do you work with hotels and accommodation here?',
        "Yes, and it's a substantial part of what we do in Surfers. Guest WiFi across whole properties, property management system connectivity, payment terminal segmentation and account management "
        'for seasonal staff.'),
    (   'What does IT support cost in Surfers Paradise?',
        '$198 + GST per hour ($217.80 inc GST), plus a $100 + GST call-out for on-site attendance. Remote support carries no call-out. Managed IT is a flat monthly fee quoted after a free review.')]

PAGE = {
    "path": '/it-support-surfers-paradise-gold-coast',
    "priority": "0.7",
    "title": "IT Support Surfers Paradise — We're Based Here | bcom ICT",
    "description": 'IT support for Surfers Paradise businesses from an office at 9 Ferny Avenue. High-rise access, venue and accommodation systems, guest WiFi and seasonal staff turnover.',
    "hero_img": 'hero-bg.webp',
    "hero_alt": 'A Surfers Paradise office supported by bcom ICT, with the skyline visible through the window',
    "h1": "We're on Ferny Avenue",
    "lede": 'Our office is in Surfers Paradise, so this is the one suburb where "local IT support" means we can walk.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Office at 9 Ferny Ave', 'High-rise experience', 'Venue & accommodation', 'Answered 24/7'],
    "crumbs": [("Industries", "/industries"), ('Surfers Paradise', '/it-support-surfers-paradise-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT is based at 9 Ferny Avenue, Surfers Paradise, and supports businesses throughout the suburb — accommodation, venues, hospitality, retail and professional offices in the high-rise towers. Attendance in Surfers Paradise is usually within the hour during business hours. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'High-rise access takes planning',
                                         None,
                                         'Most commercial space here is in towers. That means building '
                                         'management approvals, booking a service lift, and often a window '
                                         'for anything involving cabling or equipment being moved. We '
                                         'factor it in rather than discovering it on the day.'),
                                 (       'Accommodation and venues dominate',
                                         None,
                                         'Guest WiFi across a whole property, booking systems that cannot '
                                         'go down, payment terminals across multiple outlets, and function '
                                         'spaces judged at capacity. A different problem to an office — '
                                         'see hospitality.'),
                                 (       'Seasonal turnover is constant',
                                         None,
                                         'Casual staff arriving and leaving year-round. Account creation '
                                         'and, more importantly, prompt removal is a security control here '
                                         'rather than paperwork.'),
                                 (       'Older towers, older cabling',
                                         None,
                                         'Several of the commercial towers along the Esplanade and Ferny '
                                         'Avenue have cabling that predates what modern WiFi and PoE '
                                         'devices need. Worth checking before assuming a new access point '
                                         'will just work.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'What working in Surfers actually involves',
                'icon': False,
                'sub': 'The businesses here have a particular shape, and so do the buildings.'},
        {       'h2': 'Who we work with here',
                'ticks': [       'Accommodation and short-stay operators — guest WiFi, property management '
                                 'systems, payment segmentation',
                                 'Restaurants, bars and venues along the Esplanade and Cavill Avenue',
                                 'Professional offices in the Ferny Avenue and Surfers Paradise Boulevard '
                                 'towers',
                                 'Retail and tourism operators with card payments and seasonal peaks',
                                 'Body corporate and building management, where shared infrastructure '
                                 'needs coordinating']}])
            + faq_block(FAQS)
            + nearby('/it-support-surfers-paradise-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Hospitality & accommodation', '/it-support-hospitality-gold-coast')])
            + cta("We're around the corner", 'Call 07 3041 8993 — in Surfers we can usually be there inside the hour.'),
}

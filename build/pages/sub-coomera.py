from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Coomera?',
        'Yes. bcom ICT attends Coomera businesses — including the industrial and logistics estates — from its Surfers Paradise office, roughly thirty minutes away. Same-day attendance is usually '
        'available and most faults are resolved remotely first. Call 07 3041 8993.'),
    (   'Can you get WiFi coverage across a warehouse?',
        "Yes, but it needs surveying rather than estimating. Steel framing, high ceilings and racking block signal in ways a floor plan won't show. We measure the space and specify access point "
        "placement and cabling for what's actually there — consumer equipment won't cover it however it's positioned."),
    (   'Is Coomera too far for on-site support?',
        'No. Same-day attendance is usually available, and remote support resolves most faults far faster than anyone could drive. For businesses that need guaranteed response, managed IT carries a '
        'contracted 4-hour target on critical faults.'),
    (   'Can you support us across several sites?',
        "Yes, and it's where we do our best work. Standardised equipment and configuration across sites, centrally managed and remotely supported — the same model as the national retail chain "
        'rollout in our case studies.')]

PAGE = {
    "path": '/it-support-coomera-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Coomera — Industrial, Logistics & Retail | bcom ICT',
    "description": 'IT support for Coomera businesses — warehousing, logistics, light industrial and retail across the fastest-growing part of the northern Gold Coast.',
    "hero_img": 'hero-bg-business.webp',
    "hero_alt": 'A Coomera warehouse and logistics business supported by bcom ICT',
    "h1": "IT support for Coomera's industrial estates",
    "lede": 'The fastest-growing part of the coast, and a lot of large-footprint premises where covering the floor is the actual problem.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~30 min from our office', 'Warehouse coverage', 'Multi-site capable', 'Remote-first where we can'],
    "crumbs": [("Industries", "/industries"), ('Coomera', '/it-support-coomera-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT supports businesses in Coomera — warehousing, logistics, light industrial operations and retail across the northern growth corridor. Attendance is roughly thirty minutes from bcom ICT's Surfers Paradise office, with most faults resolved remotely and multi-site operations supported as a single estate. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Coverage is the whole job',
                                         None,
                                         'Warehousing and logistics premises are large, steel-framed and '
                                         'full of racking. Getting reliable WiFi to a scanner at the back '
                                         'of a rack run is a design problem, not a matter of buying a '
                                         'better router.'),
                                 (       'Newer estates, better starting point',
                                         None,
                                         'Recently built industrial and commercial space usually has '
                                         'sensible provisioning and modern connectivity available. It '
                                         "makes installations more predictable — though what's available "
                                         "and what's connected are different questions worth checking."),
                                 (       'Operations run to a schedule',
                                         None,
                                         'Picking, despatch and delivery windows mean disruptive work has '
                                         'to be scheduled around them. We plan installations for when the '
                                         'floor is quiet rather than when it suits us.'),
                                 (       'Often part of a multi-site business',
                                         None,
                                         'Coomera premises are frequently one site of several. '
                                         'Standardising equipment and configuration across them makes '
                                         'support dramatically faster and problems rarer — the model '
                                         'behind our national retail rollout.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'Large footprints, new estates',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       'Warehousing, logistics and distribution — floor coverage, scanning, '
                                 'stock systems',
                                 'Light industrial and manufacturing with an office attached',
                                 'Retail around Westfield Coomera and the surrounding centres',
                                 'Trades and construction businesses based in the northern estates',
                                 'Multi-site operations running Coomera as one of several locations']}])
            + faq_block(FAQS)
            + nearby('/it-support-coomera-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Case studies', '/case-studies')])
            + cta('Coverage problems on the floor?', "We'll survey the space and tell you what it actually needs — which is rarely what's currently installed."),
}

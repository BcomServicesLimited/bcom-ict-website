from layout import cta, faq_block, related, svc_body

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
            + faq_block(FAQS)
            + related([       ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Business WiFi', '/business-wifi-gold-coast'),
        ('Office move IT checklist', '/office-move-it-checklist'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('Got a move date?', 'Tell us when and where. The earlier we survey, the fewer surprises there are — and carrier lead times wait for nobody.'),
}

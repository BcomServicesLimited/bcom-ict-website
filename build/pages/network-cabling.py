from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Who installs office data cabling on the Gold Coast?',
        'bcom ICT delivers Cat6 and Cat6A structured cabling for Gold Coast offices, including patch panels, comms racks, cable management, testing and certification. The cabling itself is carried '
        'out by ACMA registered cabling contractors that bcom ICT engages and manages, because fixed cabling is a licensed trade in Australia and bcom ICT does not hold cabler registration itself. Call 07 3041 8993.'),
    (   'Should we use Cat6 or Cat6A?',
        'Cat6 handles gigabit comfortably and 10-gigabit over shorter runs, and suits most small offices. Cat6A is the safer choice for longer runs, for buildings you expect to be in for a decade, '
        "and where high-density WiFi or 10-gigabit switching is likely. We'll explain the difference for your building rather than defaulting to one."),
    (   'Do you need to be licensed to install network cabling in Australia?',
        'Yes. Fixed cabling connected to the telecommunications network requires ACMA cabler registration. bcom ICT engages registered cabling contractors for that work rather than doing it with '
        'internal staff, and provides the testing and certification documentation on completion.'),
    (   'Can you work around our trading hours?',
        "Yes. Cabling in an occupied office is usually staged after hours or over a weekend. Ceiling and wall work is disruptive and noisy, and it's rarely worth doing while people are trying to "
        'work.'),
    (   "What's the difference between data cabling and phone cabling?",
        'Increasingly very little — most modern phone systems run over the same structured cabling as your computers. Older PBX systems may still use separate voice cabling, which we also install. '
        "If you're replacing a phone system, one structured cabling installation usually serves both."),
    ('Will you label it?', 'Yes, at both ends, matched to a floor plan you keep. It is the cheapest thing in the entire installation and the one that saves the most time later.')]

PAGE = {
    "path": '/network-cabling-for-offices-gold-coast',
    "priority": '0.75',
    "service": 'Office Network Cabling Gold Coast',
    "title": 'Office Network & Data Cabling Gold Coast — Cat6 & Cat6A | bcom ICT',
    "description": 'Cat6 and Cat6A structured cabling for Gold Coast offices — patch panels, comms racks and cable management, installed by ACMA registered cabling contractors with testing and certification.',
    "hero_img": 'data-cabling-hero.webp',
    "hero_alt": 'Cat6 structured cabling and patch panel installed in a Gold Coast commercial premises',
    "h1": 'Cabling done once, properly, and documented',
    "lede": 'Cat6 and Cat6A structured cabling for Gold Coast offices — installed by registered cablers, tested, certified and labelled so the next person can follow it.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Cat6 & Cat6A', 'ACMA registered cablers', 'Tested & certified', 'Labelled and documented'],
    "crumbs": [('Services', '/services'), ('Office Network Cabling', '/network-cabling-for-offices-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT delivers Cat6 and Cat6A structured cabling for Gold Coast offices and commercial premises — patch panels, comms racks, cable management, testing and certification documentation. Fixed cabling is a licensed trade in Australia, so the cabling itself is carried out by ACMA registered cabling contractors that bcom ICT engages and manages. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Nothing is labelled',
                                         None,
                                         'An unlabelled patch panel turns a five-minute fault into a '
                                         'two-hour trace. Labelling costs nothing at installation and '
                                         'saves hours forever after.'),
                                 (       'The wrong cable was used',
                                         None,
                                         "Cat5e still works until it doesn't — until you install PoE "
                                         'access points, or move to faster switching, and discover the run '
                                         'is the bottleneck.'),
                                 (       'Runs are too long',
                                         None,
                                         'Ethernet has distance limits. Exceeding them produces '
                                         'intermittent faults that look like everything except cabling, '
                                         'which is where troubleshooting time goes to die.'),
                                 (       'No testing certificate',
                                         None,
                                         'Without one you have no evidence any run performs to spec. '
                                         'Reputable installers test and certify every run and hand you the '
                                         'results.'),
                                 (       'The comms room is chaos',
                                         None,
                                         'Cable management is not cosmetic. It determines whether a change '
                                         'takes ten minutes or a morning, and whether airflow keeps the '
                                         'equipment alive.'),
                                 (       "It wasn't done by a registered cabler",
                                         None,
                                         'Fixed cabling connected to the telecommunications network '
                                         'legally requires registration in Australia. Worth asking any '
                                         'installer to show you before work starts.')],
                'cols': 3,
                'eyebrow': 'Why it matters',
                'h2': 'Bad cabling is expensive twice',
                'sub': "Once when it's installed, and again every time someone has to troubleshoot it."},
        {       'h2': 'What an installation includes',
                'ticks': [       'Site survey — where the comms room goes, where the points are needed, '
                                 'what routes exist and what the building will allow',
                                 'Cat6 or Cat6A runs, terminated to standard, with the choice explained '
                                 'rather than defaulted',
                                 'Patch panels, comms rack, and cable management that a future technician '
                                 'can work in',
                                 'Every run tested and certified, with the documentation handed to you',
                                 'Labelling at both ends, matched to a floor plan you keep',
                                 'Power over Ethernet capacity considered up front, for access points, '
                                 'cameras and phones']},
        {       'h2': 'Who does the work',
                'html': '<p style="max-width:68ch">Fixed cabling connected to the telecommunications '
                        'network legally requires a registered cabler in Australia. <strong>bcom ICT does '
                        'not hold that registration.</strong> The cabling portion is carried out by ACMA '
                        'registered cabling contractors that we engage and manage.</p><p '
                        'style="max-width:68ch;margin-top:16px">In practice that means you deal with one '
                        'point of contact for the whole job — design, cabling, switching, WiFi and '
                        'handover — rather than coordinating three trades yourself. You still get the '
                        'testing and certification documentation on completion, and we would encourage you '
                        'to ask any installer for it.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast')])
            + cta('Fitting out or moving in?', "We'll survey the building and quote on what it actually needs — including telling you when the existing cabling is fine."),
}

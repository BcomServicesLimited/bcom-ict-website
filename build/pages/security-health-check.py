from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What is a cybersecurity health check?',
        "A cybersecurity health check is a point-in-time review of a business's security position across email and identity, endpoints, backups, network and cloud tenancy. bcom ICT delivers it for a "
        'fixed fee agreed before starting and provides a plain-English written report with findings mapped to the ASD Essential Eight and a prioritised remediation plan.'),
    (   'How much does it cost?',
        'A fixed fee, agreed before we start, so there is no open meter and no surprise. The figure depends on how many users and sites there are — we will give you the number before you commit to '
        'anything.'),
    (   'Do we have to use you for the fixes?',
        'No, and the report is written on that basis. Plenty of businesses take it to their existing provider, or work through it themselves. We would rather you acted on it with someone else than '
        'not acted on it at all.'),
    (   'How long does it take?',
        "Typically a few days from access to report for a small business, most of which is us working rather than you. We need about an hour of someone's time who knows how the business actually "
        'operates.'),
    ('Will it disrupt anything?', 'No. It is a review, not a change. Nothing is altered during the assessment — findings are reported, and any remediation is agreed separately afterwards.'),
    (   'Is this the same as an Essential Eight assessment?',
        'It covers the Essential Eight and reports where you sit against each control, alongside things the Essential Eight does not address such as email spoofing protection and cloud sharing '
        'settings. If you specifically need a maturity assessment for an insurer or client, say so and we will scope it that way.')]

PAGE = {
    "path": '/cybersecurity-health-check-for-small-business-gold-coast',
    "priority": '0.8',
    "service": 'Cybersecurity Risk Assessment Gold Coast',
    "title": 'Cybersecurity Health Check for Gold Coast Small Business | bcom ICT',
    "description": 'A fixed-fee cybersecurity health check for Gold Coast small businesses. bcom ICT audits email, identity, endpoints, backups and network, then hands you a plain-English report. Call 07 3041 8993.',
    "hero_img": 'cybersecurity-assessment-hero.webp',
    "hero_alt": 'A cybersecurity health check being carried out for a Gold Coast small business',
    "h1": 'Find out where you actually stand',
    "lede": 'A fixed-fee review of your email, accounts, devices, backups and network — with a written report you keep whatever you decide to do next.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Fixed fee, agreed up front', 'Plain-English report', 'Essential Eight mapped', 'No obligation to remediate'],
    "crumbs": [('Services', '/services'), ('Cybersecurity', '/cybersecurity-services-gold-coast'), ('Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides a fixed-fee cybersecurity health check for Gold Coast small businesses, reviewing email, identity and accounts, endpoints, backups and network security. You receive a plain-English written report with findings mapped against the ASD Essential Eight and a prioritised remediation plan. The report is yours regardless of what you do next. Call 07 3041 8993.', blocks=[       {       'cards': [       (       'Email and identity',
                                         None,
                                         'Who can sign in, from where, and with what. Multi-factor '
                                         'authentication coverage, legacy authentication left open, '
                                         'forwarding rules nobody set, and whether your domain can be '
                                         'spoofed.'),
                                 (       'Endpoints',
                                         None,
                                         'What protection is actually running on each machine, whether it is '
                                         'centrally visible, patch status, and how many devices are on '
                                         'unsupported operating systems.'),
                                 (       'Backups',
                                         None,
                                         'What is backed up, how often, where it is held, whether ransomware '
                                         'could reach it from inside your network, and — the question most '
                                         'fail — when a restore was last tested.'),
                                 (       'Network',
                                         None,
                                         'Firewall configuration, remote access, guest WiFi separation, and '
                                         'the default passwords that were never changed.'),
                                 (       'Cloud tenancy',
                                         None,
                                         'Microsoft 365 or Google Workspace sharing settings, admin '
                                         'accounts, permissions that accumulated as people came and went.'),
                                 (       'The human layer',
                                         None,
                                         'Whether staff would recognise an invoice scam, and what happens '
                                         'when someone does click. Not a lecture — a realistic picture.')],
                'cols': 3,
                'eyebrow': 'What we review',
                'h2': 'Five areas, in the order that matters'},
        {       'h2': 'What you get',
                'ticks': [       'A written report in plain English, not a tool export with 400 findings',
                                 'Every finding ranked by what it would actually cost you, not by severity '
                                 'score',
                                 'Where you sit against each of the ASD Essential Eight controls, and what '
                                 'the next maturity level takes',
                                 'A prioritised plan — what to fix this month, this quarter, and what can '
                                 'wait',
                                 'Rough costs against each item so you can budget rather than guess',
                                 'A document you can hand to an insurer, a board or a client asking the '
                                 'question']},
        {       'h2': 'Why businesses book one',
                'html': '<p style="max-width:68ch">Two reasons, almost every time. An insurer\'s renewal '
                        'questionnaire got noticeably harder and the answers are no longer obvious. Or a '
                        'larger client started asking about their supply chain and wants something in '
                        'writing.</p><p style="max-width:68ch;margin-top:16px">Both need a document rather '
                        'than an assurance, which is the point of doing this properly. The third reason — '
                        'and the one we would rather see — is a business that simply wants to know before '
                        'something happens.</p><p style="max-width:68ch;margin-top:16px">There is no '
                        'obligation to have us do the remediation. Take the report to whoever you like; it '
                        'is written to be useful on its own.</p>'}])
            + faq_block(FAQS)
            + related([       ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('24/7 Security Operations Centre', '/security-operations-centre-gold-coast'),
        ('ASIC Cybersecurity Compliance', '/asic-cybersecurity-compliance-gold-coast'),
        ('Data Backup & Disaster Recovery', '/data-backup-recovery-gold-coast'),
        ('Notifiable Data Breaches guide', '/notifiable-data-breach-guide-australia')])
            + cta('Book a health check', 'Fixed fee, agreed before we start. You keep the report whether or not you go any further.'),
}

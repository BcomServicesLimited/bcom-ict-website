from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Is the IT assessment really free?',
        "Yes. bcom ICT provides the initial systems review at no charge, and you keep the written report whether or not you engage us. It's how both sides work out whether there's a fit — and "
        "sometimes the honest conclusion is that you don't need a monthly arrangement yet."),
    (   'What do you need from us?',
        'Access to the site and systems, whatever documentation already exists, and roughly an hour of someone who knows how the business actually works day to day. Everything else is our time.'),
    ('Will it disrupt anything?', "No. It's a review rather than a change — nothing is altered during the assessment. Any remediation is quoted and agreed separately afterwards."),
    ('How long does it take?', 'For a typical small business, a few days from access to report. Larger or completely undocumented environments take longer, mostly in discovery rather than analysis.'),
    (   "What if we don't want to use you afterwards?",
        "That's a legitimate outcome and the report is still yours. Plenty of businesses take it to their existing provider — we'd rather it got acted on by someone else than not acted on at all."),
    (   'Is this the same as a security health check?',
        'No. The needs assessment is broader and free — systems, licensing, hardware and security at a high level. The security health check is a deeper, fixed-fee review focused specifically on '
        'your security position and Essential Eight maturity.')]

PAGE = {
    "path": '/it-needs-assessment-gold-coast',
    "priority": '0.7',
    "title": 'Free IT Needs Assessment — Gold Coast Business | bcom ICT',
    "description": "A free review of what your business actually runs, what's at risk and what to fix first. Plain-English written report, yours to keep whether or not you engage us.",
    "hero_img": 'it-needs-assessment-hero.webp',
    "hero_alt": 'An IT needs assessment being carried out for a Gold Coast business by bcom ICT',
    "h1": "Find out what you've actually got",
    "lede": "Most businesses can't answer basic questions about their own IT — what's backed up, what's out of support, who has access. The review answers them, and it's free.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['No charge', 'Report is yours', 'No obligation', 'About an hour of your time'],
    "crumbs": [('Services', '/services'), ('IT Needs Assessment', '/it-needs-assessment-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides a free IT needs assessment for Gold Coast businesses — reviewing systems, security, backups and licensing, then providing a plain-English written report on what is at risk and what to fix first. The report is yours to keep whether or not you engage bcom ICT. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       '"Are our backups working?"',
                                         None,
                                         'Not whether backups run — whether a restore has been tested, and '
                                         'whether ransomware could reach the backup from inside your '
                                         'network. This is the question that most often has an '
                                         'uncomfortable answer.'),
                                 (       '"Who can get into what?"',
                                         None,
                                         "Which accounts have multi-factor authentication and which don't. "
                                         "Who still has access who shouldn't. What a departed staff member "
                                         'can still reach.'),
                                 (       '"What\'s out of support?"',
                                         None,
                                         'Operating systems no longer receiving security updates, expired '
                                         "warranties on equipment you can't trade without, and software "
                                         'the vendor stopped patching.'),
                                 (       '"What are we actually paying for?"',
                                         None,
                                         'Licences and subscriptions nobody has reviewed. This one '
                                         'frequently pays for the work that follows.')],
                'cols': 2,
                'eyebrow': 'What it answers',
                'h2': "Questions most businesses can't answer about themselves",
                'icon': False},
        {       'h2': 'What you get',
                'ticks': [       'A written report in plain English — not a tool export with four hundred '
                                 'findings',
                                 'Every issue ranked by what it would actually cost you if it happened',
                                 'An inventory of devices, licences, warranties and suppliers, which most '
                                 'businesses have never had',
                                 'Where you sit against the ASD Essential Eight',
                                 'A prioritised plan: this month, this quarter, and what can genuinely '
                                 'wait',
                                 'Rough costs against each item so you can budget rather than guess']},
        {       'h2': "Why it's free",
                'html': '<p style="max-width:68ch">Because it is how we find out whether we are a fit, and '
                        'how you find out the same thing. We would rather spend a few hours discovering '
                        'that you do not need us monthly than sign you up and part company in eight '
                        'months.</p><p style="max-width:68ch;margin-top:16px">You keep the report either '
                        'way. Take it to your existing provider, work through it yourself, or use it to '
                        'compare quotes. It is written to be useful on its own.</p><p '
                        'style="max-width:68ch;margin-top:16px">What we need from you is access, whatever '
                        'documentation exists, and about an hour of someone who knows how the business '
                        'actually operates. The rest is our work.</p>'}])
            + faq_block(FAQS)
            + related([       ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Onboarding — first 30 days', '/onboarding-first-30-days'),
        ('What IT support costs', '/it-support-cost-gold-coast'),
        ('How to choose an MSP', '/how-to-choose-an-msp-gold-coast')])
            + cta('Book the free review', 'A few hours of our time, about an hour of yours, and a written report you keep regardless.'),
}

from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Can you review a quote from another IT provider?',
        "Yes, and it's one of the most common reasons businesses call. We read the proposal, explain what it actually buys, and flag anything missing, duplicated or padded. bcom ICT takes no vendor "
        "commissions, so the assessment isn't influenced by wanting to sell you an alternative."),
    (   'Do you earn commission on hardware you recommend?',
        "No. We source at trade pricing and are transparent about what we charge over it, and we're happy for clients to buy directly and have us configure it instead. A recommendation to buy "
        'nothing costs us nothing to make.'),
    ('What does procurement advice cost?', "$198 + GST per hour ($217.80 inc GST). We scope the piece of work first so you're agreeing to a rough number of hours rather than an open meter."),
    (   'Will you tell us not to buy something?',
        "Regularly. Common examples: a server that could be retired to cloud instead of replaced, a licence tier above what's needed, and equipment with years of useful life being replaced "
        'unnecessarily.')]

PAGE = {
    "path": '/technology-procurement-advice-gold-coast',
    "priority": '0.65',
    "title": 'Technology Procurement Advice Gold Coast | bcom ICT',
    "description": 'Independent advice on what technology to buy, from a provider that takes no vendor commissions. Read the quote, check the spec, and hear when the answer is to buy nothing.',
    "hero_img": 'hardware-procurement-setup-gold-coast-hero.webp',
    "hero_alt": 'Technology procurement advice being provided to a Gold Coast business by bcom ICT',
    "h1": 'Someone to read the quote before you sign it',
    "lede": 'Independent advice on what to buy, what to skip, and whether the proposal in front of you is reasonable. We take no vendor commissions, so it costs us nothing to say no.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['No vendor commissions', '$198 + GST/hr', 'Second opinions welcome', 'Often the cheapest hour'],
    "crumbs": [('Services', '/services'), ('Technology Procurement Advice', '/technology-procurement-advice-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides independent technology procurement advice to Gold Coast businesses — reviewing quotes and proposals, specifying what a business actually needs, and advising on whether to buy, upgrade or do nothing. bcom ICT takes no commissions from hardware or software vendors. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       "A quote landed and you can't judge it",
                                         None,
                                         'Someone has proposed a system, a server or a migration and you '
                                         "have no way to assess whether it's reasonable. We read it, tell "
                                         'you what it actually buys, and flag anything missing or padded. '
                                         "Frequently the cheapest hour you'll spend."),
                                 (       "You're not sure what to specify",
                                         None,
                                         'Buying for the work each person actually does, rather than the '
                                         'cheapest model or the one at the top of the page. An accounts '
                                         'machine, a CAD workstation and a reception PC are three '
                                         'different purchases.'),
                                 (       'Renewal is coming up',
                                         None,
                                         'Licensing, subscriptions and support contracts renewing on '
                                         'autopilot. A review before renewal frequently finds tiers above '
                                         'what you need and seats nobody uses.'),
                                 (       "You're being told to replace something",
                                         None,
                                         "Sometimes correct, often driven by who's available rather than "
                                         "what the equipment needs. We'll assess remaining life honestly — "
                                         'see the replacement cycle guide.')],
                'cols': 2,
                'eyebrow': 'When to call',
                'h2': 'Four moments this is worth an hour',
                'icon': False},
        {       'h2': 'Why independent matters here',
                'ticks': [       '<strong>No hardware or software commissions.</strong> A recommendation '
                                 'to buy nothing costs us nothing.',
                                 "<strong>We're not an internet or phone reseller</strong>, so advice on "
                                 "plans isn't influenced by wanting to sell you one.",
                                 '<strong>You can take the advice elsewhere.</strong> Some clients have us '
                                 "specify and then buy it themselves. That's a legitimate outcome.",
                                 "<strong>We'll say when the incumbent is right.</strong> If the quote in "
                                 'front of you is fair, hearing that is worth the hour too.',
                                 "<strong>We'll say when we're the wrong people.</strong> Some purchases "
                                 "need a specialist, and it's cheaper for everyone if we say so early."]}])
            + faq_block(FAQS)
            + related([       ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('IT Needs Assessment', '/it-needs-assessment-gold-coast'),
        ('Computer replacement cycle', '/business-computer-replacement-cycle'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast')])
            + cta("Got a quote you can't judge?", 'Send it over. An hour reading it is usually the cheapest part of the whole purchase.'),
}

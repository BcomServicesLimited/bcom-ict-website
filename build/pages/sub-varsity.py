from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Varsity Lakes?',
        'Yes. bcom ICT attends Varsity Lakes businesses from its Surfers Paradise office, roughly twenty minutes away, with same-day attendance usually available. Managed, cloud and cybersecurity '
        'work is delivered remotely. Call 07 3041 8993.'),
    (   "We've grown and our IT hasn't kept up. Where do we start?",
        "With a review of what you're actually running — usually a consumer router doing a job it was never specified for, backups nobody has tested, and multi-factor authentication on some accounts "
        'but not others. The review is free and you keep the report.'),
    (   'Can you support staff working from home?',
        "Yes, and it's routine here. Remote workers get the same support and the same security settings as anyone in the office — the security travels with the device rather than sitting in the "
        'building.'),
    (   'Do you support businesses that only need occasional help?',
        "Yes. Ad-hoc support is $198 + GST per hour with no ongoing commitment. We'll tell you honestly if a monthly arrangement isn't worth it for you yet.")]

PAGE = {
    "path": '/it-support-varsity-lakes-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Varsity Lakes — Business Park & Professional | bcom ICT',
    "description": 'IT support for Varsity Lakes businesses — professional services, medical and technology firms in a modern business park precinct near Bond University.',
    "hero_img": 'hero-bg-consulting.webp',
    "hero_alt": 'A Varsity Lakes business park office supported by bcom ICT',
    "h1": 'IT support for the Varsity Lakes business park',
    "lede": "Modern premises, professional tenants and a lot of businesses that grew out of somewhere smaller and haven't updated their IT arrangements to match.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~20 min from our office', 'Business park precinct', 'Modern infrastructure', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Varsity Lakes', '/it-support-varsity-lakes-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT supports businesses in Varsity Lakes — professional services firms, medical practices and technology businesses in the business park precinct near Bond University. Attendance is roughly twenty minutes from bcom ICT's Surfers Paradise office. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Purpose-built premises',
                                         None,
                                         'Business park space usually has proper comms rooms and '
                                         'structured cabling already in place, which removes most of the '
                                         'awkward surprises. Installations here tend to run to plan.'),
                                 (       'Businesses that outgrew their setup',
                                         None,
                                         'A common pattern: a firm that started with five people and a '
                                         'consumer router now has twenty-five and the same router. Nothing '
                                         'has failed yet, but nothing has been designed either.'),
                                 (       'Professional and medical concentration',
                                         None,
                                         'Practices holding concentrated client or patient information, '
                                         "often with obligations they haven't fully mapped — see "
                                         'professional services and healthcare.'),
                                 (       'Hybrid working is normal',
                                         None,
                                         'Proximity to Bond and a professional tenant mix means a lot of '
                                         'hybrid arrangements. Security has to travel with the device '
                                         'rather than living in the office.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'Growth-stage businesses in good buildings',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       'Professional services firms — accounting, legal, consulting, advice',
                                 'Medical and allied health practices in the precinct',
                                 'Technology and services businesses in growth stage',
                                 'Businesses with staff split between office and home',
                                 'Multi-site operations running a head office from Varsity']}])
            + faq_block(FAQS)
            + nearby('/it-support-varsity-lakes-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Professional services', '/it-support-professional-services-gold-coast')])
            + cta('Outgrown your setup?', "That's the most common reason Varsity businesses call. The review is free and tells you what to fix first."),
}

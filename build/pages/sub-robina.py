from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Robina?',
        'Yes. bcom ICT attends Robina businesses from its Surfers Paradise office, roughly twenty minutes away, with same-day attendance usually available. Many faults are resolved remotely within '
        'minutes. Call 07 3041 8993.'),
    (   'Can you answer supplier security questionnaires?',
        "Yes, and Robina's corporate tenants ask more often than most. Our published service levels and trust centre set out response targets, framework alignment, credentials and insurance — most "
        'questionnaires can be answered directly from them.'),
    (   'Do you work with AFS licensees in Robina?',
        'Yes. Cyber resilience falls within the general obligations of a financial services licence, which means implemented controls plus documented evidence. See our ASIC cybersecurity compliance '
        'page.'),
    (   'How much does IT support cost in Robina?',
        '$198 + GST per hour ($217.80 inc GST) plus a $100 + GST call-out for on-site attendance. Remote support has no call-out. Managed IT is quoted after a free review.')]

PAGE = {
    "path": '/it-support-robina-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Robina — Corporate & Professional | bcom ICT',
    "description": 'IT support for Robina businesses — corporate offices, professional services and medical practices in a planned commercial precinct with modern infrastructure.',
    "hero_img": 'hero-bg-business.webp',
    "hero_alt": 'A Robina corporate office supported by bcom ICT',
    "h1": "IT support for Robina's business precinct",
    "lede": 'Robina was planned rather than accumulated, which shows in the buildings. Newer infrastructure, corporate tenants, and expectations to match.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~20 min from our office', 'Corporate & professional', 'Modern buildings', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Robina', '/it-support-robina-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT supports businesses in Robina — corporate offices, professional services firms, financial services and medical practices concentrated around Robina Town Centre and the surrounding business precinct. Attendance is roughly twenty minutes from bcom ICT's Surfers Paradise office. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Newer buildings, better bones',
                                         None,
                                         'Most commercial space here was purpose-built, which usually '
                                         'means sensible comms rooms, adequate cabling and fewer nasty '
                                         'surprises above the ceiling tiles. It makes installations more '
                                         'predictable than in older parts of the coast.'),
                                 (       'Corporate tenants, corporate expectations',
                                         None,
                                         'A lot of Robina businesses are branches or head offices of '
                                         'larger operations, which brings procurement questionnaires, '
                                         'supplier security assessments and documented response '
                                         'requirements. Our published service levels exist partly for that '
                                         'conversation.'),
                                 (       'Financial and professional services concentration',
                                         None,
                                         'AFS licensees, brokers, accountants and advice practices. Cyber '
                                         'resilience sits inside licence obligations for many of them — '
                                         'see ASIC cybersecurity compliance.'),
                                 (       'Medical precinct nearby',
                                         None,
                                         'Practices in and around Robina carry Privacy Act obligations '
                                         'regardless of size, and our attending technicians hold police '
                                         'checks and Blue Cards where required.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'A planned precinct behaves differently',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       'Financial services, broking and advice practices with licence '
                                 'obligations',
                                 'Accounting and legal firms handling concentrated client information',
                                 'Corporate branch offices needing documented supplier security answers',
                                 'Medical and allied health practices',
                                 'Retail and hospitality around Robina Town Centre']}])
            + faq_block(FAQS)
            + nearby('/it-support-robina-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('ASIC Cybersecurity Compliance', '/asic-cybersecurity-compliance-gold-coast')])
            + cta('Answering a supplier security questionnaire?', "Most of what they ask is already published on our trust centre — and if something's missing, we'll write it."),
}

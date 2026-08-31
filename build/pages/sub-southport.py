from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Southport?',
        'Yes. bcom ICT attends Southport businesses from its office at 9 Ferny Avenue, Surfers Paradise — roughly ten minutes away — with same-day attendance usually available. Phones are answered '
        '8am to 5pm Monday to Friday. Call 07 3041 8993.'),
    (   'Do you work with medical practices in Southport?',
        'Yes. Health service providers are covered by the Privacy Act regardless of turnover, which changes what their IT has to do. Our technicians hold national police checks and Queensland Blue '
        'Cards where the practice requires them.'),
    (   'Can you support law firms and confidential document systems?',
        'Yes — access control structured by role, managed devices for anything leaving the office, secure remote access and backups with tested restores. Professional confidentiality obligations '
        'make access control more than a convenience.'),
    (   'How quickly can you attend in Southport?',
        'Same-day attendance is usually available, and many faults are resolved remotely within minutes of your call. Managed clients have a contracted 4-hour response for critical faults.')]

PAGE = {
    "path": '/it-support-southport-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Southport — Business & Professional | bcom ICT',
    "description": 'IT support for Southport businesses — legal, medical and professional offices in the Gold Coast CBD. Same-day attendance, roughly ten minutes from our Surfers Paradise office.',
    "hero_img": 'hero-bg-it-support.webp',
    "hero_alt": 'A Southport professional office supported by bcom ICT',
    "h1": 'IT support in the Gold Coast CBD',
    "lede": 'Southport carries the legal, medical and professional weight of the Gold Coast — and the compliance obligations that come with it.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~10 min from our office', 'Legal & medical experience', 'Police-checked techs', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Southport', '/it-support-southport-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT provides IT support to Southport businesses, roughly ten minutes from its Surfers Paradise office. Southport is the Gold Coast's commercial and civic centre, with a concentration of legal, medical and professional practices carrying specific confidentiality and compliance obligations. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Professional and legal practices',
                                         None,
                                         'With the courts here, Southport has a dense concentration of '
                                         'legal practices. Client confidentiality, document management and '
                                         'access control matter more than in a typical office — see '
                                         'professional services.'),
                                 (       'Medical and allied health',
                                         None,
                                         'A significant health precinct. Practices carry Privacy Act '
                                         'obligations regardless of turnover, because health service '
                                         "providers don't get the small business exemption. Our "
                                         'technicians hold police checks and Blue Cards where required.'),
                                 (       'A mix of building ages',
                                         None,
                                         'Southport ranges from modern towers to commercial buildings that '
                                         'have been repurposed several times. Cabling quality varies '
                                         "enormously, and it's worth checking what's actually in the walls "
                                         'before planning anything.'),
                                 (       'Parking is a genuine factor',
                                         None,
                                         'Unglamorous but real — it affects how quickly a technician gets '
                                         'from the car to your desk. We know where to park, which sounds '
                                         "trivial until you've waited for someone who didn't.")],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'What Southport businesses tend to need',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       "Legal practices and barristers' chambers — confidentiality, document "
                                 'systems, secure remote access',
                                 'Medical, dental and allied health practices — patient records, practice '
                                 'software, screened technicians',
                                 'Accounting and financial services firms, including AFS licensees with '
                                 'cyber resilience obligations',
                                 'Government-adjacent and not-for-profit offices',
                                 'Retail and hospitality around Australia Fair and the Broadwater']}])
            + faq_block(FAQS)
            + nearby('/it-support-southport-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Professional services', '/it-support-professional-services-gold-coast')])
            + cta('Ten minutes up the road', 'Call 07 3041 8993 — Southport attendance is usually same-day, often sooner.'),
}

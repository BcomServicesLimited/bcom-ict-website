from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Broadbeach?',
        'Yes. bcom ICT is based at 9 Ferny Avenue, Surfers Paradise, roughly five minutes from Broadbeach, with same-day attendance usually available and phones answered 24/7 including weekends and '
        'public holidays. Call 07 3041 8993.'),
    (   "Our WiFi struggles when we're busy. Can that be fixed?",
        "Usually yes, and it's a design problem rather than an internet problem. One access point serving forty devices behaves nothing like one serving five. It needs surveying and properly "
        'specified equipment — adding a consumer extender generally makes it worse.'),
    (   'What happens to our payments if the internet drops?',
        "With automatic 4G or 5G failover, card payments keep working and the changeover needs nobody's attention. Without it you stop trading. For a Broadbeach retailer or venue it usually pays for "
        "itself the first time it's used."),
    ('Can you attend during trading hours?', "Yes, and we'll work around service where it matters. Disruptive work gets scheduled outside trading. For anything urgent, phones are answered 24/7.")]

PAGE = {
    "path": '/it-support-broadbeach-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Broadbeach — Retail, Venues & Offices | bcom ICT',
    "description": 'IT support for Broadbeach businesses — retail, restaurants, venues and professional offices around Pacific Fair, the convention centre and Oracle Boulevard.',
    "hero_img": 'hero-bg-business.webp',
    "hero_alt": 'A Broadbeach business supported by bcom ICT',
    "h1": 'IT support for Broadbeach retail and venues',
    "lede": 'Convention traffic, a major shopping centre and a dense restaurant strip. Broadbeach businesses live and die on payments working and WiFi holding up under load.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~5 min from our office', 'Retail & venue focus', 'EFTPOS failover', 'Answered 24/7'],
    "crumbs": [("Industries", "/industries"), ('Broadbeach', '/it-support-broadbeach-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT supports businesses in Broadbeach — retail, restaurants, venues and professional offices around Pacific Fair, the convention precinct and Oracle Boulevard. Broadbeach is roughly five minutes from bcom ICT's Surfers Paradise office. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Convention and event peaks',
                                         None,
                                         "When there's an event on, foot traffic and device density spike "
                                         'together. Systems that are comfortable on a Tuesday get tested '
                                         'properly on those weekends, which is exactly when a failure '
                                         'costs most.'),
                                 (       'Retail and payments dominate',
                                         None,
                                         'Around Pacific Fair and the surrounding strips, when the POS is '
                                         'down the shop is closed. Payment terminal segmentation and '
                                         'automatic 4G failover are the two things worth having before you '
                                         'need them.'),
                                 (       'Dining density is high',
                                         None,
                                         'The restaurant strip has the same shape as Surfers — failure at '
                                         "service is the problem, and margins don't absorb a lost night."),
                                 (       'Offices among the towers',
                                         None,
                                         'Professional and corporate tenants in the Oracle and surrounding '
                                         'buildings, with the same high-rise access considerations as '
                                         'Surfers — building management, service lifts and scheduled '
                                         'windows.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'Load arrives in waves',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       'Retailers and food outlets — POS, EFTPOS, stock systems and failover',
                                 'Restaurants, bars and venues along the dining strip',
                                 'Accommodation and short-stay operators with guest WiFi obligations',
                                 'Professional offices in the Oracle and surrounding towers',
                                 'Businesses running multiple Gold Coast sites from a Broadbeach base']}])
            + faq_block(FAQS)
            + nearby('/it-support-broadbeach-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Retail', '/it-support-retail-gold-coast')])
            + cta('Busy weekend coming?', "The time to test failover is a quiet Tuesday. Call 07 3041 8993 — we're five minutes away."),
}

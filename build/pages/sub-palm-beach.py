from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Palm Beach?',
        'Yes. bcom ICT attends Palm Beach businesses from its Surfers Paradise office, roughly twenty-five minutes away, with same-day attendance usually available. Most faults are resolved remotely '
        'at $198 + GST per hour with no call-out. Call 07 3041 8993.'),
    (   'Is it worth calling you for a small job?',
        "Often the answer is remote support, which carries no call-out and frequently resolves the problem in under an hour. We'll tell you on the phone whether it needs a visit before booking one."),
    (   "We're only a few people. Do we need managed IT?",
        "Probably not, and we'll say so. Ad-hoc support suits most businesses this size. The two things worth doing regardless are multi-factor authentication on your email and a backup you've "
        'actually seen restore.'),
    ('Do you do home office WiFi in Palm Beach?', "Yes — mesh WiFi and home office network setup. General home computer repair isn't something we take on.")]

PAGE = {
    "path": '/it-support-palm-beach-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Palm Beach — Small Business | bcom ICT',
    "description": 'IT support for Palm Beach businesses — cafés, retail, creative studios and small professional practices along the southern Gold Coast Highway strip.',
    "hero_img": 'hero-bg-consulting.webp',
    "hero_alt": 'A Palm Beach small business supported by bcom ICT',
    "h1": 'IT support for Palm Beach businesses',
    "lede": "A strip of independent operators that's changed considerably in a few years — and a lot of premises whose infrastructure hasn't changed with it.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~25 min from our office', 'Small independents', 'Remote-first where we can', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Palm Beach', '/it-support-palm-beach-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT supports businesses in Palm Beach — cafés, retail, creative studios and small professional practices along the southern Gold Coast Highway. Attendance is roughly twenty-five minutes from bcom ICT's Surfers Paradise office, and most faults are resolved remotely without a visit. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Premises that predate the businesses in them',
                                         None,
                                         'A lot of Palm Beach commercial space has been repurposed more '
                                         'than once. Cabling is frequently improvised and WiFi has to '
                                         'cover through construction nobody planned around — worth '
                                         'surveying rather than assuming.'),
                                 (       'Mostly very small teams',
                                         None,
                                         'Two to ten people, no internal IT, and often no provider at all '
                                         'until something breaks. Ad-hoc support at an hourly rate usually '
                                         "suits better than a monthly arrangement, and we'll say so."),
                                 (       'Remote fixes matter more here',
                                         None,
                                         'At twenty-five minutes out, the call-out is a meaningful part of '
                                         "a small job. We try remote first — it's $198 + GST per hour with "
                                         'no call-out — and only book a visit when the fault genuinely '
                                         'needs hands on it.'),
                                 (       'Hospitality and retail along the strip',
                                         None,
                                         'Same shape as elsewhere on the coast: card payments are the '
                                         'priority, and automatic failover is the cheap insurance.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'Independent operators, ageing premises',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       'Cafés, restaurants and food outlets along the highway',
                                 'Retail and boutique operators',
                                 'Creative studios, agencies and consultants',
                                 'Small professional practices',
                                 'Home offices needing WiFi and mesh — though not general home computer '
                                 'repair']}])
            + faq_block(FAQS)
            + nearby('/it-support-palm-beach-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Remote IT Support', '/remote-it-support-gold-coast')])
            + cta('Try remote first', "Call 07 3041 8993 — no call-out on remote support, and most problems don't need anyone on site."),
}

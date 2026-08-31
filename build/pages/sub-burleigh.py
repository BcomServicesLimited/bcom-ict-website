from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Burleigh Heads?',
        'Yes. bcom ICT attends Burleigh Heads businesses from its Surfers Paradise office, roughly twenty minutes away, with same-day attendance usually available and phones answered 24/7. Call 07 '
        '3041 8993.'),
    (   "We're a small café. Do we really need an IT provider?",
        "Not necessarily on a monthly arrangement, and we'll say so. But two things are worth doing regardless: automatic 4G or 5G failover so card payments continue through an internet outage, and "
        'multi-factor authentication on your email. Both are inexpensive and both prevent expensive days.'),
    (   'Do you work with businesses in older Burleigh buildings?',
        "Frequently. Converted premises usually have improvised cabling and awkward equipment placement. We survey rather than assume, because what's actually in the walls determines what's "
        'possible.'),
    ('Do you do home office setups in Burleigh?', "WiFi and mesh network installation for home offices, yes. General home computer repair isn't something we take on.")]

PAGE = {
    "path": '/it-support-burleigh-heads-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Burleigh Heads — Business | bcom ICT',
    "description": 'IT support for Burleigh Heads businesses — cafés, creative studios, boutique agencies and the professional practices moving into converted shopfronts along James Street.',
    "hero_img": 'hero-bg-consulting.webp',
    "hero_alt": 'A Burleigh Heads business supported by bcom ICT',
    "h1": "IT support for Burleigh's small operators",
    "lede": 'Burleigh runs on small, independent businesses — hospitality, creative studios and boutique practices in buildings that were never designed for what they now hold.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~20 min from our office', 'Small independents', 'Older shopfronts', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Burleigh Heads', '/it-support-burleigh-heads-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT supports businesses in Burleigh Heads — cafés and restaurants, creative studios, boutique agencies and the professional practices increasingly occupying converted shopfronts around James Street and the Gold Coast Highway. Attendance is roughly twenty minutes from bcom ICT's Surfers Paradise office. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Converted shopfronts have quirks',
                                         None,
                                         "A lot of Burleigh's commercial space started as something else. "
                                         'Cabling is often improvised, comms equipment ends up in a '
                                         'cupboard behind the coffee machine, and WiFi has to cover '
                                         'through walls nobody planned around.'),
                                 (       'Hospitality density is high',
                                         None,
                                         'Cafés and restaurants along James Street and the highway, where '
                                         'the POS going down at service is the whole problem. Automatic 4G '
                                         'failover matters more here than almost anywhere.'),
                                 (       'Creative and boutique businesses',
                                         None,
                                         'Studios, agencies and consultancies with a handful of staff, '
                                         'working across devices, often hybrid. Small does not mean simple '
                                         '— they frequently hold client material worth protecting.'),
                                 (       'Small businesses, real exposure',
                                         None,
                                         'Being small is not protective. Almost all of what happens is '
                                         'automated and indiscriminate — it finds whoever is reachable, '
                                         'and smaller businesses are reachable because the basics are '
                                         'missing.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'Small premises, older buildings',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       'Cafés, restaurants and bars — POS, EFTPOS, failover and venue WiFi',
                                 'Creative studios and agencies working across laptops and cloud tools',
                                 'Boutique professional practices in converted premises',
                                 'Retail along the highway and James Street',
                                 'Home offices in the surrounding suburbs — WiFi and mesh, though not '
                                 'general home computer repair']}])
            + faq_block(FAQS)
            + nearby('/it-support-burleigh-heads-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Restaurants & cafés', '/it-support-restaurants-gold-coast')])
            + cta('Small business, small budget?', "Tell us what's actually causing problems. Often the fix is cheaper than you'd expect, and sometimes you don't need us monthly at all."),
}

from layout import cta, faq_block, related, svc_body, nearby

FAQS = [   (   'Do you provide IT support in Nerang?',
        'Yes. bcom ICT attends Nerang businesses — including the industrial estates — from its Surfers Paradise office, roughly twenty minutes away, with same-day attendance usually available. Call '
        '07 3041 8993.'),
    (   'Can you get WiFi working across a warehouse or shed?',
        "Usually, but it needs surveying rather than guessing. Steel construction, high ceilings and racking all block signal, and consumer equipment won't cover it regardless of how it's "
        "positioned. We measure the space and specify access points for what's actually there."),
    (   'Our team is always on the road. What do they need?',
        'Job management software that works offline at sites with poor reception, mobile devices that can be replaced and configured the same day, and a phone system that follows people rather than '
        'sitting on a desk. See our trades and field services page.'),
    (   'Someone changed our bank details on an invoice. What do we do?',
        'Contact your bank immediately, then call us on 07 3041 8993. Going forward, multi-factor authentication on every mailbox and a rule that bank detail changes are verified by phone on a '
        'number you already hold.')]

PAGE = {
    "path": '/it-support-nerang-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Nerang — Trades & Light Industrial | bcom ICT',
    "description": 'IT support for Nerang businesses — trades, workshops, automotive and light industrial operations in the industrial estates, plus the offices behind them.',
    "hero_img": 'it-support-trades-gold-coast-hero.webp',
    "hero_alt": 'A Nerang light industrial business supported by bcom ICT',
    "h1": "IT support for Nerang's industrial estates",
    "lede": 'Workshops, yards and trade businesses where the IT is a small office, a job management system, and phones that have to follow people into the field.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~20 min from our office', 'Trades & industrial', 'Warehouse WiFi', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Nerang', '/it-support-nerang-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT supports businesses in Nerang — trades, workshops, automotive and light industrial operations across the industrial estates, along with the offices behind them. Attendance is roughly twenty minutes from bcom ICT's Surfers Paradise office. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'WiFi in a shed is genuinely hard',
                                         None,
                                         'Steel construction, high ceilings, racking and machinery all '
                                         'interfere. Consumer equipment that would cover an office reaches '
                                         'a fraction of a warehouse — it needs surveying and proper access '
                                         'points, not more power.'),
                                 (       "The office is small, the yard isn't",
                                         None,
                                         'Typically a few desks attached to a much larger operational '
                                         'space. Coverage has to extend to where stock is picked, jobs are '
                                         'scanned and vehicles are loaded.'),
                                 (       'Field staff are the business',
                                         None,
                                         'Job management software on phones and tablets, quoting on site, '
                                         'and phones that route to whoever is actually available rather '
                                         "than a desk nobody's at — see trades and field services."),
                                 (       'Invoice fraud hits hard here',
                                         None,
                                         'Trades and industrial businesses invoice large progress '
                                         'payments. Business email compromise redirecting one of those is '
                                         'real money, and multi-factor authentication stops nearly all of '
                                         'it.')],
                'cols': 2,
                'eyebrow': 'Local reality',
                'h2': 'Sheds are a different building problem',
                'icon': False},
        {       'h2': 'Who we work with here',
                'ticks': [       'Trades and field service businesses running job management software',
                                 'Workshops and automotive operations with a small office attached',
                                 'Light industrial and warehousing needing coverage across the floor',
                                 'Wholesale and distribution with stock systems',
                                 'Construction and building businesses invoicing progress payments']}])
            + faq_block(FAQS)
            + nearby('/it-support-nerang-gold-coast')
            + related([       ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Pricing', '/pricing'),
        ('Trades & field services', '/it-support-trades-gold-coast')])
            + cta("WiFi that won't reach the back of the shed?", "We'll measure it and tell you what coverage actually requires — usually not what's currently installed."),
}

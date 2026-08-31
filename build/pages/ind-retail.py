from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What IT support does a retail business need?',
        'Above all, keeping point of sale and payment terminals running — which means a reliable network, automatic 4G or 5G failover when the internet drops, and payment devices segmented from '
        'staff and guest traffic. Beyond that: stock system support, business WiFi built for a shop floor, and standardised equipment across stores. bcom ICT supports Gold Coast retailers on all of '
        'it.'),
    (   'What happens if our internet goes down mid-trade?',
        "With a 4G or 5G failover connection, payments keep working and the changeover is automatic — nobody is plugging in a hotspot while customers wait. It's worth configuring before an outage "
        "rather than after one, and it's inexpensive relative to a closed till."),
    (   'Do we need to separate our payment terminals from the rest of the network?',
        "Yes, and it's expected practice under PCI-DSS. Payment devices should sit on their own network segment that staff machines and guest WiFi cannot reach. It costs almost nothing at "
        'installation and is genuinely awkward to retrofit later.'),
    (   'Can you support multiple stores?',
        "Yes, and it's where the biggest gains are. Standardising equipment and configuration across stores makes support far faster and problems far rarer. Our largest engagement is a national "
        'retail chain supported as a single estate.'),
    (   'Is customer WiFi a risk?',
        "Only if it isn't isolated. Guest WiFi should be internet-only with no route to your stock system, back office or payment devices. Done properly it's a genuine amenity; done as an "
        "afterthought it's a way into your business."),
    (   'How fast can you get to a store?',
        'Same-day attendance is usually available across the Gold Coast, and many POS and network faults can be diagnosed remotely within minutes of a call. Phones are answered 24/7, which for '
        'retail trading hours matters.')]

PAGE = {
    "path": '/it-support-retail-gold-coast',
    "priority": '0.75',
    "title": 'IT Support for Gold Coast Retail Businesses | bcom ICT',
    "description": 'IT support for Gold Coast retail. POS and EFTPOS uptime, payment terminal segmentation, stock systems and consistent technology across multiple stores.',
    "hero_img": 'it-support-retail-gold-coast-hero.webp',
    "hero_alt": 'Point of sale and payment systems supported by bcom ICT for a Gold Coast retailer',
    "h1": 'When the POS is down, the shop is closed',
    "lede": 'Retail IT has one job above all others: keep taking payments. Everything else is secondary, and most of it depends on the network underneath.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['POS & EFTPOS uptime', 'PCI-aligned segmentation', 'Multi-site consistency', '4G/5G failover'],
    "crumbs": [('Industries', '/industries'), ('Retail', '/it-support-retail-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supports retail businesses across the Gold Coast — point of sale and payment terminal uptime, PCI-DSS-aligned network segmentation keeping payment devices separate from staff and guest traffic, stock and inventory systems, and consistent technology across multiple stores. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Payments never stop',
                                         None,
                                         'POS and EFTPOS are the business. Everything in the design should '
                                         'serve keeping them running, including a 4G or 5G failover '
                                         'connection that takes over automatically when the internet '
                                         'drops.'),
                                 (       'Payment devices are separated',
                                         None,
                                         'Card terminals on their own network segment, unreachable from '
                                         'staff machines or guest WiFi. This is expected practice under '
                                         'PCI-DSS and it is far cheaper to build in than to retrofit.'),
                                 (       'Guest WiFi is genuinely isolated',
                                         None,
                                         'Customer WiFi with a route to your stock system or back office '
                                         'is a real exposure. Internet only, nothing internal.'),
                                 (       'Stock systems stay in sync',
                                         None,
                                         'Inventory, ordering and online integrations that fall out of '
                                         'sync cost real money quietly, and the failure is often not '
                                         'noticed for days.'),
                                 (       'Every store looks the same',
                                         None,
                                         'Multi-site retail runs far better on one standardised technology '
                                         'stack than on whatever each store accumulated. It also makes '
                                         'support dramatically faster.'),
                                 (       'Staff turnover is a control',
                                         None,
                                         'High turnover means accounts must be removed promptly. In retail '
                                         'this is a security control rather than paperwork.')],
                'cols': 3,
                'eyebrow': 'Priorities',
                'h2': 'What actually matters in a shop',
                'sub': "Retail IT priorities are not the same as an office's, and treating them the same "
                       'is how a provider ends up unavailable at the worst moment.'},
        {       'h2': 'Multi-site retail',
                'html': '<p style="max-width:68ch">Once you have more than one store, the useful shift is '
                        'to stop treating them as separate sites and start treating them as one estate — '
                        'the same equipment, the same configuration, centrally managed and remotely '
                        'supported.</p><p style="max-width:68ch;margin-top:16px">That is precisely the '
                        'model behind our largest engagement: a full national rollout for an Australian '
                        'retail chain, where every store was commissioned to the same standard and the '
                        'whole network is now supported as a single estate. See <a '
                        'href="/case-studies">case studies</a>.</p>'},
        {       'h2': 'What we cover',
                'ticks': [       'POS and payment terminal support, and the network they depend on',
                                 'PCI-DSS-aligned segmentation separating payments, staff, guests and '
                                 'devices such as cameras',
                                 "<a href='/business-wifi-gold-coast'>Business WiFi</a> designed for a "
                                 'shop floor rather than an office',
                                 "Internet with automatic 4G or 5G failover, so an outage doesn't close "
                                 'the till',
                                 'Stock, inventory and online integration support',
                                 'Standardised equipment across stores, ordered and configured centrally',
                                 'Backups of the systems you cannot rebuild from memory']}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Case studies', '/case-studies'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast')])
            + cta('What happens to your till if the internet drops?', 'If the answer is "we stop trading", that\'s a cheap problem to fix — and worth fixing before Christmas rather than during it.'),
}

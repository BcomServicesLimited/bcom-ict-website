from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Who installs business networks on the Gold Coast?',
        'bcom ICT designs, installs and supports business networks across the Gold Coast — switching, routing, firewalls, structured cabling and business WiFi — delivered as one system with a single '
        'point of accountability. Cabling is carried out by ACMA registered cabling contractors that bcom ICT engages and manages. Call 07 3041 8993.'),
    (   'Can you take over a network someone else installed?',
        'Yes, and it is common. The first step is documenting what actually exists, because that is usually the thing missing. From there we can tell you what is sound, what needs attention and what '
        'was done badly enough to redo.'),
    (   'Do we need business-grade switches, or will consumer gear do?',
        "It depends on scale and what you're powering. Once you have access points, cameras or phones needing Power over Ethernet, VLANs to keep guests separate, or more than about a dozen users, "
        'consumer gear stops being cheaper — it just moves the cost into troubleshooting time.'),
    (   'How long does a network installation take?',
        "A small office fit-out is usually a few days including cabling. Larger sites or occupied offices take longer because the work is staged after hours. We'll give you a schedule after the site "
        'survey rather than an estimate before it.'),
    (   'Will you document it?',
        'Yes — diagrams, labelling at both ends, credentials and an asset register, all handed to you. It is yours, and you can ask for a copy at any time rather than only on exit.')]

PAGE = {
    "path": '/computer-networking-service-gold-coast',
    "priority": '0.75',
    "service": 'Computer Networking Service Gold Coast',
    "title": 'Business Computer Networking Gold Coast | bcom ICT',
    "description": 'Design, installation and support of business networks on the Gold Coast — switching, routing, WiFi, cabling and firewalls, built as one system by one team. Call 07 3041 8993.',
    "hero_img": 'hero-bg-networking.webp',
    "hero_alt": 'Business network switching and infrastructure installed by bcom ICT on the Gold Coast',
    "h1": 'One network, one team, one number to call',
    "lede": 'Switching, routing, WiFi, cabling and firewalls designed together — rather than four suppliers each blaming the other three.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Designed as one system', 'One point of accountability', 'Documented on handover', 'Since 2011'],
    "crumbs": [('Services', '/services'), ('Computer Networking', '/computer-networking-service-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT designs, installs and supports business computer networks across the Gold Coast — switching, routing, structured cabling, business WiFi and firewalls — delivered as one system with a single point of accountability rather than split across separate suppliers. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'The blame loop',
                                         None,
                                         "The WiFi installer says it's the cabling. The cabler says it's "
                                         "the switch. The phone company says it's the internet. Meanwhile "
                                         "nobody owns the fault and you're the one coordinating three "
                                         'trades who have never spoken.'),
                                 (       'Nothing was designed together',
                                         None,
                                         'Access points specified without checking the switch has PoE '
                                         'capacity. Cabling run before anyone decided where the rack goes. '
                                         "Each piece is fine; the system isn't."),
                                 (       'No documentation exists',
                                         None,
                                         'Every supplier documented their own part, if at all. Nobody has '
                                         'a diagram of the whole thing, which makes every future change an '
                                         'investigation.'),
                                 (       'Nobody reviews it',
                                         None,
                                         'Networks are installed and then left. Firmware ages, rules '
                                         'accumulate, capacity gets outgrown quietly — until something '
                                         "breaks and it's an emergency.")],
                'cols': 2,
                'eyebrow': 'The problem with split suppliers',
                'h2': 'Four vendors, nobody responsible',
                'icon': False,
                'sub': "The most common networking problem we're called to isn't technical."},
        {       'h2': 'What we design and support',
                'ticks': [       '<strong>Switching</strong> — capacity, PoE budget for access points, '
                                 'cameras and phones, and VLANs planned before anything is bought',
                                 '<strong>Routing and firewalls</strong> — segmentation, secure remote '
                                 'access and rules written to match how your business works',
                                 '<strong>Business WiFi</strong> — Ubiquiti UniFi and Aruba Instant On, '
                                 'surveyed before quoting',
                                 '<strong>Structured cabling</strong> — Cat6 and Cat6A, installed by ACMA '
                                 'registered cabling contractors we engage and manage',
                                 '<strong>Internet and failover</strong> — including 4G or 5G backup so an '
                                 "outage doesn't stop you trading",
                                 '<strong>Documentation you keep</strong> — diagrams, labelling, '
                                 'credentials and an asset register that belongs to you']},
        {       'h2': 'Ongoing, or one-off',
                'html': '<p style="max-width:68ch">Plenty of clients have us design and install a network '
                        'and then call when something needs changing. That is a perfectly reasonable '
                        'arrangement and we support it.</p><p style="max-width:68ch;margin-top:16px">The '
                        'alternative is having the network monitored and maintained as part of <a '
                        'href="/managed-it-services-for-small-businesses-gold-coast">managed IT</a> — '
                        'firmware kept current, capacity watched, rules reviewed, and faults noticed '
                        'before somebody reports them. Which suits you depends on how much a day of '
                        'downtime costs, and we will give you an honest view rather than a default '
                        'answer.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta("Fitting out, moving, or fixing what's there?", "We'll survey it and design the whole thing together — so there's one person to call when something isn't right."),
}

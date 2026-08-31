from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Should we use the router our internet provider supplied?',
        "For a small setup, often yes, once it's properly configured. It typically becomes the bottleneck once you're running VoIP phones, a VPN and thirty or more devices — well before the "
        'connection itself struggles. We measure before recommending a replacement.'),
    (   "What's the first thing to change on a new router?",
        'The default admin password. Router default credentials are published online by model, so a device still on factory settings is accessible to anyone who reaches the network. After that: '
        'firmware updates, guest network separation and voice prioritisation if you use VoIP.'),
    (   'Our calls break up when someone uploads a file. Why?',
        "Voice traffic isn't being prioritised. Without quality-of-service configuration, a large upload competes directly with your phone calls. It's a configuration change rather than a hardware "
        'problem in most cases.'),
    (   'Can you set up a router remotely?',
        "Frequently yes — remote support is $198 + GST per hour with no call-out. If it needs physical replacement or rewiring, we'll book a visit and tell you the cost first.")]

PAGE = {
    "path": '/router-and-modem-configuration-gold-coast',
    "priority": '0.65',
    "title": 'Router & Modem Configuration Gold Coast — Business | bcom ICT',
    "description": 'Router and modem configuration for Gold Coast businesses and home offices — set up securely, with voice traffic prioritised and default passwords changed.',
    "hero_img": 'hero-bg-router-modem.webp',
    "hero_alt": 'A business router being configured by bcom ICT on the Gold Coast',
    "h1": 'Routers configured, not just plugged in',
    "lede": "New connection, new router, or one that's been quietly running on factory defaults since it arrived.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Defaults changed', 'Voice prioritised', 'Secure remote access', 'Documented'],
    "crumbs": [('Services', '/services'), ('Computer Networking', '/computer-networking-service-gold-coast'), ('Router & Modem Configuration', '/router-and-modem-configuration-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT configures routers and modems for Gold Coast businesses and home offices — securing the device, changing default credentials, prioritising voice traffic where VoIP is in use, setting up guest and staff separation, and documenting the configuration. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'The default admin password',
                                         None,
                                         'Still the single most common finding. A router on factory '
                                         'credentials is reachable by anyone who gets onto the network, '
                                         'and the passwords are published online by model.'),
                                 (       'Voice prioritisation',
                                         None,
                                         'If you run VoIP phones, voice traffic needs priority over a '
                                         'large upload. Without it, calls break up at exactly the moment '
                                         'someone sends a big file.'),
                                 (       'Guest and staff separation',
                                         None,
                                         'Visitors on a network that reaches your business systems is a '
                                         'genuine exposure, and most supplied routers are capable of '
                                         'separating them once someone configures it.'),
                                 (       'Firmware',
                                         None,
                                         'Routers need patching like anything else, and edge devices are '
                                         'actively targeted. An unpatched router is worse than none '
                                         "because it's trusted.")],
                'cols': 2,
                'eyebrow': 'What we change',
                'h2': 'What a proper configuration involves',
                'icon': False},
        {       'h2': 'When the router is the problem',
                'html': '<p style="max-width:68ch">Provider-supplied routers are built to a price. '
                        "They're adequate for a household and frequently become the bottleneck once a "
                        'business is running VoIP, a VPN, and thirty devices — long before the connection '
                        'itself struggles.</p><p style="max-width:68ch;margin-top:16px">Symptoms look like '
                        'slow internet: calls breaking up, connections dropping under load, remote access '
                        "that stalls. We measure before recommending a replacement, because sometimes it's "
                        'configuration rather than capacity — see <a '
                        'href="/network-troubleshooting-diagnostics-gold-coast">network '
                        'troubleshooting</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Mesh WiFi Setup', '/mesh-network-setup-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Remote IT Support', '/remote-it-support-gold-coast')])
            + cta('Router still on factory settings?', "It's a short job with a disproportionate benefit — and we can usually do it remotely."),
}

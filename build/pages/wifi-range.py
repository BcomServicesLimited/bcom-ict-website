from layout import cta, faq_block, related, svc_body

FAQS = [   (   "What's the best way to extend WiFi range?",
        "A wired access point, wherever a cable run is physically possible — it delivers full speed with no compromise. Where cabling isn't practical, a mesh system positioned by measurement is the "
        'next best. Range extenders are cheapest but typically halve throughput and create roaming problems.'),
    (   "Why doesn't our range extender work well?",
        "Usually placement. Extenders are commonly installed at the dead spot itself, where they can barely hear the signal they're meant to relay. They need to sit partway between the router and "
        'the dead area. Even correctly placed, they halve throughput by design.'),
    (   'Should we use mesh instead?',
        "For most homes and small premises where cabling isn't practical, yes. Mesh keeps one network name so devices roam properly, rather than clinging to a weak connection. See our mesh WiFi "
        'setup page.'),
    (   'Can you extend WiFi to a shed or outbuilding?',
        "Often, though it depends on distance, construction and whether power and a cable path exist. Steel sheds are particularly difficult. We'll measure and tell you honestly what's achievable "
        'before quoting.')]

PAGE = {
    "path": '/wifi-range-extension-gold-coast',
    "priority": '0.65',
    "title": 'WiFi Range Extension Gold Coast — Business & Home Office | bcom ICT',
    "description": 'Extending WiFi coverage for Gold Coast businesses and home offices — measured rather than guessed, with wired access points where a cable run is possible.',
    "hero_img": 'hero-bg-wifi-range-extension.webp',
    "hero_alt": 'WiFi coverage being extended by bcom ICT at a Gold Coast premises',
    "h1": "Getting signal where there isn't any",
    "lede": 'Extenders are the usual answer and often the wrong one. What actually works depends on whether a cable can reach.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Measured, not guessed', 'Wired where possible', 'Business & home office', 'Same-day where available'],
    "crumbs": [('Services', '/services'), ('Business WiFi', '/business-wifi-gold-coast'), ('WiFi Range Extension', '/wifi-range-extension-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT extends WiFi coverage for Gold Coast businesses and home offices, measuring signal across the space before recommending an approach. Where a cable run is possible a wired access point is used, since it outperforms wireless extenders and mesh; where it is not, a mesh system is positioned by measurement. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Wired access point',
                                         None,
                                         'A cable run to a second access point. Full speed, no compromise, '
                                         'and by a clear margin the best result. If a cable can physically '
                                         'get there, this is the answer.'),
                                 (       'Mesh system',
                                         None,
                                         'Several nodes working together under one network name. Good when '
                                         "cabling isn't practical, and devices roam properly between nodes "
                                         'rather than clinging to a distant one.'),
                                 (       'Range extender',
                                         None,
                                         'The cheapest and the weakest. Typically halves throughput and '
                                         'creates a second network name devices hold onto long after they '
                                         'should switch. Occasionally the right answer, usually not.')],
                'cols': 3,
                'eyebrow': 'Three approaches',
                'h2': 'Which one suits, in order of preference'},
        {       'h2': 'Why measuring matters',
                'html': '<p style="max-width:68ch">Almost every failed extension we are called to fix was '
                        'positioned by guesswork — the device placed where the dead spot is, rather than '
                        'partway between the router and the dead spot where it can still hear the signal '
                        'it is meant to be relaying.</p><p '
                        'style="max-width:68ch;margin-top:16px">Measuring takes very little time and '
                        'determines whether the equipment will work at all. For larger premises — '
                        'warehouses, multi-storey buildings, accommodation — it is not optional; see <a '
                        'href="/business-wifi-gold-coast">business WiFi installation</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Mesh WiFi Setup', '/mesh-network-setup-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Remote IT Support', '/remote-it-support-gold-coast')])
            + cta('Dead spot somewhere it matters?', "We'll measure it and tell you what will actually work — which is frequently cheaper than what's been suggested."),
}

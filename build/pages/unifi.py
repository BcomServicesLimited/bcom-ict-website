from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Do you install Ubiquiti UniFi on the Gold Coast?',
        'Yes. bcom ICT designs and installs UniFi access points, switching and gateways for Gold Coast businesses, including site survey, VLAN segmentation for staff, guests and payment devices, '
        'central management and documentation on handover.'),
    (   'Can we install UniFi ourselves?',
        'The hardware is available and the software is approachable, so many people try. What usually goes wrong is design rather than setup — access points placed without a survey, wireless mesh '
        'used where cabling was possible, no VLANs configured, and PoE budget exceeded. The result is a system that works but not well.'),
    (   'Is UniFi better than Aruba Instant On?',
        'Different rather than better. UniFi gives more control, better visibility and a wider range covering switching, gateways, cameras and door access — and expects competent configuration. '
        'Aruba Instant On is simpler and very solid for straightforward business WiFi. We install both and recommend based on the building.'),
    (   'Do we need a cloud key or controller?',
        "Some form of controller is needed to manage the system, though modern gateways often include it. We'll specify what your setup actually requires rather than adding hardware by default."),
    ('Will you document it?', "Yes — network layout, VLAN structure, credentials and labelling, handed to you. It's your network and you should hold the keys to it.")]

PAGE = {
    "path": '/ubiquiti-unifi-wifi-gold-coast',
    "priority": '0.7',
    "title": 'Ubiquiti UniFi Installation Gold Coast — Business | bcom ICT',
    "description": 'Ubiquiti UniFi business WiFi and networking installed across the Gold Coast — surveyed, cabled, segmented and centrally managed, with documentation handed over.',
    "hero_img": 'aruba-instant-on-wifi-gold-coast-hero.webp',
    "hero_alt": 'Ubiquiti UniFi access point installed by bcom ICT in a Gold Coast business',
    "h1": 'Ubiquiti UniFi, installed properly',
    "lede": 'UniFi is excellent hardware and a poor DIY project. The difference between a great install and a frustrating one is almost entirely in the design.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Surveyed before quoting', 'VLAN segmentation', 'Centrally managed', 'Documented on handover'],
    "crumbs": [('Services', '/services'), ('Business WiFi', '/business-wifi-gold-coast'), ('Ubiquiti UniFi', '/ubiquiti-unifi-wifi-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT designs and installs Ubiquiti UniFi networks for Gold Coast businesses — access points, switching and gateways, with site surveys, VLAN segmentation, central management and documentation handed over on completion. Structured cabling is carried out by ACMA registered cabling contractors bcom ICT engages. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'One system, centrally managed',
                                         None,
                                         'Access points, switches and the gateway managed from a single '
                                         'controller. Adding a site or an access point is straightforward '
                                         'rather than a new project.'),
                                 (       'Proper segmentation',
                                         None,
                                         'Staff, guests, payment terminals and devices on separate VLANs '
                                         'that cannot reach each other. This is the security work that '
                                         'matters most, and UniFi makes it manageable.'),
                                 (       'Sensible ongoing cost',
                                         None,
                                         'No per-access-point subscription for the core functionality, '
                                         'which over five years is a material difference against some '
                                         'alternatives.'),
                                 (       'Visibility',
                                         None,
                                         "You can see what's connected, what's using bandwidth and where "
                                         'problems are — which turns troubleshooting from guesswork into '
                                         'looking.')],
                'cols': 2,
                'eyebrow': 'Why UniFi',
                'h2': 'What it does well for a business',
                'icon': False},
        {       'h2': 'Where DIY installs go wrong',
                'ticks': [       '<strong>Access points placed by convenience rather than survey.</strong> '
                                 'Near a power point is not a coverage plan. Dead spots follow.',
                                 '<strong>Wireless mesh used where cabling was possible.</strong> Wired '
                                 'backhaul always outperforms it; mesh is a fallback, not a default.',
                                 '<strong>No VLANs configured</strong>, so everything sits on one flat '
                                 'network and the segmentation advantage is unused.',
                                 '<strong>Switch PoE budget exceeded</strong>, so access points drop off '
                                 'intermittently under load and nobody connects the two facts.',
                                 '<strong>Nothing documented or labelled</strong>, which makes every '
                                 'future change an investigation.']},
        {       'h2': 'UniFi or Aruba Instant On?',
                'html': '<p style="max-width:68ch">Both are good, and we install both. UniFi gives more '
                        'control, better visibility and a wider product range — switches, gateways, '
                        'cameras and door access all in one system. It expects someone competent to '
                        'configure it.</p><p style="max-width:68ch;margin-top:16px"><a '
                        'href="/aruba-instant-on-wifi-gold-coast">Aruba Instant On</a> is simpler and very '
                        'solid for straightforward business WiFi where nobody wants a controller to think '
                        'about.</p><p style="max-width:68ch;margin-top:16px">For most Gold Coast offices '
                        'either would work. We recommend based on the building, what else you need on the '
                        'network, and who will look after it — not on what we prefer.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Aruba Instant On WiFi', '/aruba-instant-on-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast')])
            + cta('Considering UniFi?', "We'll survey the building and tell you what it actually needs — including when a simpler system would serve you better."),
}

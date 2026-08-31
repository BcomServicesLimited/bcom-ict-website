from layout import cta, faq_block, related, svc_body, models

FAQS = [   (   'Who supports Aruba Instant On on the Gold Coast?',
        'bcom ICT installs, configures and supports Aruba Instant On across the Gold Coast — AP11, AP11D, AP12, AP15 and AP17 through the Wi-Fi 6 range AP21, AP22, AP22D, AP25, AP27 and AP32, plus '
        '1430, 1830, 1930 and 1960 series switches. Call 07 3041 8993.'),
    (   'Should we upgrade from AP11 or AP12 to AP22?',
        "If the complaint is speed when the office is full, yes — device density is where the newer hardware genuinely helps, and an AP11 handling forty clients struggles in a way an AP22 doesn't. "
        "If the complaint is coverage or dead spots, no. That's placement and cabling, and newer access points don't travel further through walls."),
    (   'Our Instant On access point keeps going offline. Why?',
        'Most often PoE budget on the switch or a marginal cable run — Instant On is less tolerant of borderline power than people expect. Adding cameras or phones to the same switch is a common '
        'trigger. Both are quick to test before anyone suggests new hardware.'),
    (   "We've lost access to the Instant On cloud account. Can you help?",
        "Usually, yes. It's a common situation when the original installer has moved on. We recover or re-establish access and hand back credentials documented and belonging to you."),
    (   'Do you support enterprise Aruba as well as Instant On?',
        'Yes — the Instant AP range (IAP-205 through IAP-335) and the AP-500 series. These turn up in larger Gold Coast sites and are sometimes inherited during an office move.'),
    (   'Do we need a subscription?',
        "Core Instant On functionality doesn't require one, which keeps ongoing cost predictable. We'll tell you clearly what carries a recurring cost before you commit to anything.")]

PAGE = {
    "path": '/aruba-instant-on-wifi-gold-coast',
    "priority": '0.7',
    "title": 'Aruba Instant On Support Gold Coast — AP22, AP25, AP32 | bcom ICT',
    "description": 'Aruba Instant On installation and support across the Gold Coast — AP11, AP12, AP15, AP22, AP25, AP32 and 1830/1930/1960 switches. Surveyed, configured and documented.',
    "hero_img": 'aruba-instant-on-wifi-gold-coast-hero.webp',
    "hero_alt": 'An Aruba Instant On access point installed by bcom ICT in a Gold Coast business',
    "h1": 'Aruba Instant On, installed and supported',
    "lede": "From an AP11 that won't stay online to a full AP25 estate with 1960 switching. Business-grade wireless without a controller to look after.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['AP11 through AP32', 'Instant On switching', 'No controller needed', 'Documented on handover'],
    "crumbs": [('Services', '/services'), ('Business WiFi', '/business-wifi-gold-coast'), ('Aruba Instant On', '/aruba-instant-on-wifi-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT installs, configures and supports Aruba Instant On across the Gold Coast — access points from AP11, AP12 and AP15 through the Wi-Fi 6 range (AP21, AP22, AP25) and AP32, plus 1830, 1930 and 1960 series switches. Work includes site survey, guest network separation and documented handover. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'Hardware',
                'h2': 'What we install and support',
                'html': models([('Wi-Fi 6 and 6E access points — current', 'The current Instant On range. AP22 covers most offices; AP25 and AP32 where density or throughput justify them.', ['AP21', 'AP22', 'AP22D', 'AP25', 'AP27 (outdoor)', 'AP32', 'AP35']), ('Wi-Fi 5 access points — still widely installed', 'Earlier Instant On hardware, still in service across plenty of Gold Coast offices and generally still adequate.', ['AP11', 'AP11D', 'AP12', 'AP15', 'AP17 (outdoor)']), ('Instant On switches', 'Matched switching, including the PoE budget your access points draw from.', ['1430 series', '1830 8G', '1830 24G', '1830 48G', '1930 8G', '1930 24G', '1930 48G', '1960 24G', '1960 48G']), ('Aruba Instant (enterprise) — also supported', 'The larger Aruba line. Found in bigger Gold Coast sites and sometimes inherited during an office move.', ['IAP-205', 'IAP-207', 'IAP-215', 'IAP-225', 'IAP-305', 'IAP-315', 'IAP-325', 'IAP-335', 'AP-505', 'AP-515', 'AP-535', 'AP-635'])]),
                'sub': 'Current range and the earlier generations still running in plenty of Gold Coast '
                       'offices.'},
        {       'cards': [       (       '"The AP keeps going offline"',
                                         None,
                                         'Usually PoE budget on the switch or a marginal cable run. '
                                         'Instant On access points are less tolerant of borderline power '
                                         'than people expect.'),
                                 (       '"Coverage is fine but it\'s slow when we\'re busy"',
                                         None,
                                         'Device density rather than coverage. An AP11 handling forty '
                                         'clients behaves nothing like an AP22 doing the same. This is the '
                                         'case where a hardware upgrade genuinely helps.'),
                                 (       '"We can\'t find who set it up"',
                                         None,
                                         'Instant On is tied to a cloud account. Losing access to it is '
                                         'common and usually recoverable, and we hand back credentials '
                                         'that belong to you.'),
                                 (       '"Guests can see our files"',
                                         None,
                                         "Guest network wasn't isolated. Instant On does this well once "
                                         "configured — it just isn't automatic.")],
                'cols': 2,
                'eyebrow': 'Symptoms',
                'h2': 'What people call about',
                'icon': False},
        {       'h2': 'Instant On or UniFi?',
                'html': '<p style="max-width:68ch">We install both and recommend on the building, not on '
                        'preference.</p><p style="max-width:68ch;margin-top:16px"><strong>Instant '
                        'On</strong> for a single office that wants reliable wireless and nobody thinking '
                        'about a controller. Simpler to hand over to a client who has no IT person.</p><p '
                        'style="max-width:68ch;margin-top:16px"><strong><a '
                        'href="/ubiquiti-unifi-wifi-gold-coast">UniFi</a></strong> for deeper control and '
                        'visibility, several sites managed together, or where you also want cameras and '
                        'door access on one system.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Ubiquiti UniFi WiFi', '/ubiquiti-unifi-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast')])
            + cta('Know your model?', "Tell us the AP number and what it's doing. Most Instant On faults are diagnosed before anyone travels."),
}

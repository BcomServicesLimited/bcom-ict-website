from layout import cta, faq_block, related, svc_body, models

FAQS = [   (   'Do you design and supply new Aruba Instant On systems?',
        "Yes — that's the larger part of what we do with it. bcom ICT surveys the building, specifies access points and switching, supplies the hardware at trade pricing, runs the cabling and "
        'commissions the system, then hands over documentation. We also support existing Instant On installations including earlier AP generations.'),
    (   'What does an Instant On installation cost?',
        'It depends on the building — how many access points the coverage genuinely needs, switch capacity and PoE budget, and how much cabling is involved. We survey first and quote on the actual '
        "building, so the figure doesn't move once work starts."),
    (   'Can we buy the hardware ourselves?',
        'Yes. We source at trade pricing and are transparent about the margin, but plenty of clients purchase directly and have us specify, install and configure. Either is fine.'),
    (   'Should we choose Instant On or UniFi?',
        'Instant On for a single office that wants reliable wireless with minimal management overhead. UniFi for deeper control and visibility, multiple sites managed together, or where you also '
        'want cameras and door access on the same system. We design and install both.'),
    (   'Our AP keeps going offline. Why?',
        'Most often PoE budget on the switch or a marginal cable run — Instant On is less tolerant of borderline power than people expect. Adding cameras or phones to the same switch is a common '
        'trigger. Both test quickly before anyone suggests new hardware.'),
    (   'Do you support enterprise Aruba as well?',
        'Yes — the Instant AP range (IAP-205 through IAP-335) and the AP-500 series. These turn up in larger Gold Coast sites and are sometimes inherited during an office move.')]

PAGE = {
    "path": '/aruba-instant-on-wifi-gold-coast',
    "priority": '0.7',
    "title": 'Aruba Instant On Installation Gold Coast — Design & Supply | bcom ICT',
    "description": 'Aruba Instant On networks designed, supplied and installed across the Gold Coast — survey, AP and switch specification, guest separation and documented handover. Existing installs supported too.',
    "hero_img": 'aruba-instant-on-wifi-gold-coast-hero.webp',
    "hero_alt": 'An Aruba Instant On network designed and installed by bcom ICT in a Gold Coast business',
    "h1": 'Aruba Instant On, designed and installed',
    "lede": 'Surveyed, specified, supplied and commissioned — access points, switching and cabling as one system. Business-grade wireless with no controller to look after.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Designed, not guessed', 'Hardware supplied', 'No controller needed', 'Documented on handover'],
    "crumbs": [('Services', '/services'), ('Business WiFi', '/business-wifi-gold-coast'), ('Aruba Instant On', '/aruba-instant-on-wifi-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT designs, supplies and installs Aruba Instant On networks for Gold Coast businesses — surveying the building, specifying access points and switching, running the cabling, configuring guest separation and handing over documentation. bcom ICT also supports existing Instant On installations including earlier AP generations. Call 07 3041 8993.',
                     blocks=[       {       'cols': 4,
                'eyebrow': 'New installations',
                'h2': 'How we design and build an Instant On network',
                'steps': [       (       'Survey the building',
                                         'Signal measured, construction noted, interference found. Access '
                                         'point placement comes out of that rather than out of a floor '
                                         'plan.'),
                                 (       'Design the system',
                                         'Access point count and positions, switch capacity and PoE '
                                         'budget, cable routes, and the guest network separation planned '
                                         'before anything is ordered.'),
                                 (       'Supply the hardware',
                                         'Sourced at trade pricing and specified for the building. Buy it '
                                         "yourself if you'd rather — we'll still tell you exactly what to "
                                         'get.'),
                                 (       'Install and hand over',
                                         'Cabling by ACMA registered contractors, commissioned and tested, '
                                         'then credentials and network layout documented and given to '
                                         'you.')]},
        {       'eyebrow': 'What we specify',
                'h2': 'The hardware we install',
                'html': models([('Wi-Fi 6 and 6E access points — current', 'The current Instant On range. AP22 covers most offices; AP25 and AP32 where density or throughput justify them.', ['AP21', 'AP22', 'AP22D', 'AP25', 'AP27 (outdoor)', 'AP32', 'AP35']), ('Wi-Fi 5 access points — still widely installed', 'Earlier Instant On hardware, still in service across plenty of Gold Coast offices and generally still adequate.', ['AP11', 'AP11D', 'AP12', 'AP15', 'AP17 (outdoor)']), ('Instant On switches', 'Matched switching, including the PoE budget your access points draw from.', ['1430 series', '1830 8G', '1830 24G', '1830 48G', '1930 8G', '1930 24G', '1930 48G', '1960 24G', '1960 48G']), ('Aruba Instant (enterprise) — also supported', 'The larger Aruba line. Found in bigger Gold Coast sites and sometimes inherited during an office move.', ['IAP-205', 'IAP-207', 'IAP-215', 'IAP-225', 'IAP-305', 'IAP-315', 'IAP-325', 'IAP-335', 'AP-505', 'AP-515', 'AP-535', 'AP-635'])]),
                'sub': 'Current range, plus the earlier generations we still support.'},
        {       'cards': [       (       'Business-grade, no controller',
                                         None,
                                         'Real access points with proper coverage and roaming, managed '
                                         'from an app or browser with no controller appliance to maintain. '
                                         "For an office that needs WiFi to work, that's often exactly "
                                         'right.'),
                                 (       'Aruba engineering at SMB pricing',
                                         None,
                                         "Instant On is Aruba's small business range, built on the same "
                                         'radio engineering as their enterprise gear.'),
                                 (       'Guest separation as standard',
                                         None,
                                         'Guest access isolated from business systems is a built-in '
                                         'feature rather than something to engineer.'),
                                 (       'Low ongoing cost',
                                         None,
                                         'No subscription for core functionality, and hardware that tends '
                                         'to keep working for years.')],
                'cols': 2,
                'h2': 'Why Instant On for a new system',
                'icon': False},
        {       'cards': [       (       '"The AP keeps going offline"',
                                         None,
                                         'Usually PoE budget on the switch or a marginal cable run. '
                                         'Instant On is less tolerant of borderline power than people '
                                         'expect.'),
                                 (       '"It\'s slow when everyone\'s in"',
                                         None,
                                         'Device density rather than coverage. An AP11 handling forty '
                                         "clients struggles where an AP22 wouldn't — this is the case "
                                         'where new hardware genuinely helps.'),
                                 (       '"We\'ve lost the cloud account"',
                                         None,
                                         'Common when the original installer has moved on. Usually '
                                         'recoverable, and we hand back credentials that belong to you.'),
                                 (       '"Guests can see our files"',
                                         None,
                                         'Guest network was never isolated. The hardware does this well; '
                                         "it just wasn't configured.")],
                'cols': 2,
                'eyebrow': 'Already running Instant On',
                'h2': 'We support existing installs too',
                'icon': False},
        {       'h2': 'Instant On or UniFi?',
                'html': '<p style="max-width:68ch">We design and install both, and recommend on the '
                        'building rather than on preference.</p><p '
                        'style="max-width:68ch;margin-top:16px"><strong>Instant On</strong> for a single '
                        'office wanting reliable wireless with minimal management overhead — and it is '
                        'simpler to hand to a client with no IT person.</p><p '
                        'style="max-width:68ch;margin-top:16px"><strong><a '
                        'href="/ubiquiti-unifi-wifi-gold-coast">UniFi</a></strong> for deeper control and '
                        'visibility, several sites managed together, or where cameras and door access '
                        'should sit on the same system.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Ubiquiti UniFi WiFi', '/ubiquiti-unifi-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast')])
            + cta("Fitting out, or fixing what's there?", "We'll survey the building first and quote on what it actually needs — including when your existing gear is fine."),
}

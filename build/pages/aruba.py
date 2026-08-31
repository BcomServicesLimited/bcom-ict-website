from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Do you install Aruba Instant On on the Gold Coast?',
        'Yes. bcom ICT surveys, cables and configures Aruba Instant On business WiFi for Gold Coast offices, including guest network separation, current security settings and documentation on '
        'handover.'),
    (   'Is Aruba Instant On good enough for a business?',
        "Yes for most small and medium offices. It's Aruba's small business range built on the same radio engineering as their enterprise equipment, with proper coverage, roaming and guest isolation "
        '— without a controller to maintain.'),
    (   'Should we choose Instant On or UniFi?',
        'Instant On if you want reliable WiFi with minimal management overhead in a single office. UniFi if you want deeper control and visibility, multiple sites managed together, or one system '
        'also covering switching and cameras. We install both.'),
    ('Do we need a subscription?', "Core functionality doesn't require one, which keeps the ongoing cost predictable. We'll tell you clearly what carries a recurring cost before you commit."),
    (   'Can you improve WiFi we already have?',
        "Often yes, and sometimes without replacing anything. Placement and channel problems are common and fixable in a visit. We'll say when that's the case rather than selling you a new system.")]

PAGE = {
    "path": '/aruba-instant-on-wifi-gold-coast',
    "priority": '0.7',
    "title": 'Aruba Instant On WiFi Installation Gold Coast | bcom ICT',
    "description": 'Aruba Instant On business WiFi installed across the Gold Coast — surveyed, cabled and configured with guest network separation. Simple, reliable business wireless.',
    "hero_img": 'aruba-instant-on-wifi-gold-coast-hero.webp',
    "hero_alt": 'Aruba Instant On access point installed by bcom ICT in a Gold Coast business',
    "h1": 'Aruba Instant On for business WiFi',
    "lede": "Straightforward, reliable business wireless without a controller to look after. For a lot of Gold Coast offices it's the sensible choice.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Surveyed before quoting', 'Guest separation', 'No controller needed', 'Documented on handover'],
    "crumbs": [('Services', '/services'), ('Business WiFi', '/business-wifi-gold-coast'), ('Aruba Instant On', '/aruba-instant-on-wifi-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT installs Aruba Instant On business WiFi for Gold Coast businesses — site surveyed, cabled, and configured with guest network separation and current security settings. Aruba Instant On suits businesses wanting reliable business-grade wireless without managing a controller. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Business-grade without the overhead',
                                         None,
                                         'Proper access points with real coverage and roaming, managed '
                                         'from an app or browser without a controller appliance to '
                                         'maintain. For an office that just needs WiFi that works, that is '
                                         'often exactly right.'),
                                 (       'Guest networks done properly',
                                         None,
                                         'Guest access isolated from business systems as a standard '
                                         'feature rather than something to engineer. Straightforward and '
                                         'reliable.'),
                                 (       'Aruba engineering, SMB pricing',
                                         None,
                                         "Instant On is Aruba's small business range, built on the same "
                                         'radio engineering as their enterprise gear at a price that makes '
                                         'sense for a small office.'),
                                 (       'Low ongoing cost',
                                         None,
                                         'No subscription for core functionality, and hardware that tends '
                                         'to keep working for years.')],
                'cols': 2,
                'eyebrow': 'Why Instant On',
                'h2': "What it's good at",
                'icon': False},
        {       'h2': 'What still matters regardless of brand',
                'ticks': [       '<strong>Survey before quoting.</strong> Coverage depends on the '
                                 'building, not the box. Plasterboard, steel studs and glass partitions '
                                 "all change what's needed.",
                                 '<strong>Wired backhaul where possible.</strong> A cabled access point '
                                 'beats a wireless one every time.',
                                 '<strong>Guest separation configured</strong>, not just enabled by name.',
                                 '<strong>PoE budget checked</strong> on the switch before adding access '
                                 'points.',
                                 '<strong>Labelled and documented</strong>, so the next change takes '
                                 'minutes rather than a morning.']},
        {       'h2': 'Instant On or UniFi?',
                'html': '<p style="max-width:68ch">We install both and recommend based on your building '
                        'and who will look after it, not on preference.</p><p '
                        'style="max-width:68ch;margin-top:16px"><strong>Instant On</strong> suits a '
                        'business that wants reliable WiFi with minimal management overhead — a single '
                        'office, straightforward requirements, nobody wanting to think about a '
                        'controller.</p><p style="max-width:68ch;margin-top:16px"><strong><a '
                        'href="/ubiquiti-unifi-wifi-gold-coast">UniFi</a></strong> suits businesses '
                        'wanting deeper control and visibility, multiple sites managed together, or a '
                        'single system also covering switching, cameras and door access.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Ubiquiti UniFi WiFi', '/ubiquiti-unifi-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast')])
            + cta("WiFi that doesn't reach?", "We'll survey the building and quote on what it actually needs — often less than you'd expect."),
}

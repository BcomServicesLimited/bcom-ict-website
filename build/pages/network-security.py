from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Does a small business need a proper firewall?',
        'If you have a server, staff working remotely, payment terminals or client data worth protecting, yes. The router your internet provider supplied is designed to get you online, not to '
        'segment a business network, control remote access or log what happened. bcom ICT configures business firewalls for Gold Coast offices including VLAN segmentation and secure remote access.'),
    (   'What is VLAN segmentation and why does it matter?',
        'It splits one physical network into separate logical networks that cannot reach each other — typically staff, guests, payment terminals and building devices such as cameras. It matters '
        "because without it, one compromised laptop or one visitor's infected phone can reach everything, including your accounts system."),
    (   'Is remote desktop safe to expose to the internet?',
        'No, and it is one of the most reliably exploited routes into Australian small businesses. Remote access should sit behind a VPN or a controlled access broker with multi-factor '
        'authentication. If you currently have RDP published directly, that is worth changing this month.'),
    (   'How often should firewall rules be reviewed?',
        'At least annually, and whenever staff or suppliers change. Rules accumulate — added for a project, a contractor or someone who left three years ago — and nobody removes them. Managed IT '
        'clients get this as part of the arrangement.'),
    (   'Do you supply the firewall or work with ours?',
        'Either. If your existing device is capable and current we will configure it properly rather than sell you a replacement. If it is unsupported or underpowered for what you now run, we will '
        'tell you that and quote the alternative.'),
    (   'Does this cover guest WiFi?',
        'Yes. Guest networks should be internet-only with no route to anything internal, and that separation is standard on the business WiFi installations we do. If you take card payments it is '
        'expected practice rather than optional.')]

PAGE = {
    "path": '/network-security-and-firewall-configuration-gold-coast',
    "priority": '0.75',
    "service": 'Network Security & Firewall Gold Coast',
    "title": 'Business Firewall & Network Security Gold Coast | bcom ICT',
    "description": 'Business firewall and network security for Gold Coast offices — next-generation firewall setup, VLAN segmentation, secure remote access, guest isolation and WPA3. Call 07 3041 8993.',
    "hero_img": 'hero-bg-network-security.webp',
    "hero_alt": 'Network firewall and security equipment configured by bcom ICT for a Gold Coast business',
    "h1": "A firewall that's actually configured",
    "lede": 'Most business firewalls are doing a fraction of what they could. Segmentation, remote access and guest isolation set up properly — not left on defaults.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['VLAN segmentation', 'Guest isolation', 'Secure remote access', 'Essential Eight aligned'],
    "crumbs": [('Services', '/services'), ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT configures business firewalls and network security for Gold Coast offices — next-generation firewall setup, VLAN segmentation, secure remote access, guest network isolation and WPA3 encryption. Configuration is reviewed against the ASD Essential Eight. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       "It's on factory defaults",
                                         None,
                                         'A firewall out of the box permits far more than it should and '
                                         'often still has the default admin password. It is doing '
                                         'something, but not much of what you paid for.'),
                                 (       'Everything is on one flat network',
                                         None,
                                         'Guest WiFi, EFTPOS, cameras, staff laptops and the accounts '
                                         'server all able to reach each other. One compromised device then '
                                         'reaches everything.'),
                                 (       'Remote access is wide open',
                                         None,
                                         'Remote desktop exposed to the internet is one of the most '
                                         'reliably exploited ways into a small business. It should be '
                                         'behind a VPN or a controlled access broker, never published '
                                         'directly.'),
                                 (       'Nobody reviews the rules',
                                         None,
                                         'Rules get added for a supplier, a project or a departed staff '
                                         'member and are never removed. Over years the ruleset stops '
                                         'reflecting how the business works.'),
                                 (       'Firmware is years old',
                                         None,
                                         'Firewalls need patching like anything else, and vendor '
                                         'advisories for edge devices are actively targeted. An unpatched '
                                         'firewall is worse than no firewall, because it is trusted.'),
                                 (       'There is no logging',
                                         None,
                                         'After an incident, logging is what lets you establish what was '
                                         'reached. Without it you may have to notify on the assumption of '
                                         'the worst because you cannot prove otherwise.')],
                'cols': 2,
                'eyebrow': 'What we find',
                'h2': 'The five things almost every business firewall gets wrong',
                'icon': False},
        {       'h2': 'What we configure',
                'ticks': [       '<strong>Next-generation firewall</strong> setup or review, with the '
                                 'ruleset written to match how your business actually operates',
                                 '<strong>VLAN segmentation</strong> — staff, guests, payment terminals, '
                                 'cameras and building devices separated so a compromise in one does not '
                                 'reach the others',
                                 '<strong>Secure remote access</strong> via VPN or a controlled broker, '
                                 'with multi-factor authentication, rather than services published to the '
                                 'internet',
                                 '<strong>Guest WiFi isolation</strong> — internet only, no route to '
                                 'anything internal, which is expected practice if you take card payments',
                                 '<strong>WPA3</strong> where hardware supports it, and no lingering open '
                                 'or WEP networks',
                                 '<strong>Logging and firmware maintenance</strong>, so the device stays '
                                 'current and an incident can actually be investigated']},
        {       'h2': 'Segmentation is the part that pays',
                'html': '<p style="max-width:68ch">If there is one change worth making, it is separating '
                        'your network into segments that cannot reach each other. It costs almost nothing '
                        'at installation, it is awkward to retrofit, and it is the difference between one '
                        'infected laptop and an infected business.</p><p '
                        'style="max-width:68ch;margin-top:16px">It also answers a compliance question '
                        'directly: if you take card payments, keeping payment terminals isolated from '
                        'staff and guest traffic is expected practice under PCI-DSS. We build that '
                        'separation in as standard on <a href="/business-wifi-gold-coast">business WiFi '
                        'installations</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast')])
            + cta('When was your firewall last reviewed?', "If nobody can answer that, it's worth an hour. We'll tell you what it's actually doing and what it should be."),
}

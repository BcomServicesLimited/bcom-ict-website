from layout import cta, faq_block, related, svc_body, models

FAQS = [   (   'Do you design and supply new UniFi systems, or only support existing ones?',
        'Both, and design and supply is the larger part. bcom ICT surveys the building, specifies access points, switching and gateway, supplies the hardware at trade pricing, runs the cabling and '
        'commissions the system, then hands over documentation. We also support existing UniFi installations including earlier generations. Call 07 3041 8993.'),
    (   'What does a UniFi installation cost?',
        'It depends on the building — how many access points the coverage genuinely needs, switch capacity and PoE budget, and how much cabling has to be run. We survey first and quote on the actual '
        "building rather than a guess, so the number doesn't move once an installer is on site."),
    (   'Can we buy the hardware ourselves?',
        "Yes, and some clients do. We source at trade pricing and are transparent about what we charge over it, but if you'd rather purchase directly we'll still specify exactly what to buy and "
        'install and configure it for you.'),
    (   'Why does our UAP-AC-Pro keep dropping off?',
        'The usual causes are exceeding the PoE budget on the switch, a marginal or over-length cable run, and the access point being unable to reach its controller after a network change. Adding '
        'cameras or phones to the same switch is a very common trigger. All three test quickly, and none need new hardware.'),
    (   'Do we need to upgrade from UAP-AC to U6 or U7?',
        'Often not. Upgrading is worth it for genuine device density, for large file transfers over wireless, or where hardware has reached end of software support. If the complaint is coverage or '
        "dead spots, newer access points won't help — that's placement and cabling."),
    (   'Can you take over a UniFi network someone else installed?',
        "Yes, and it's common — frequently when nobody has the controller login any more. That's usually recoverable, and we hand back documented credentials, network layout and VLAN structure "
        'belonging to you.'),
    (   'Does UniFi cover cameras and door access too?',
        "Yes — UniFi Protect for cameras and UniFi Access for doors, on the same controller. It's a real advantage of choosing UniFi for a new system, but it means planning PoE budget and switch "
        'capacity for all of it at design stage rather than discovering the limit later.')]

PAGE = {
    "path": '/ubiquiti-unifi-wifi-gold-coast',
    "priority": '0.7',
    "title": 'Ubiquiti UniFi Installation Gold Coast — Design & Supply | bcom ICT',
    "description": 'UniFi networks designed, supplied and installed across the Gold Coast — site survey, hardware specified for your building, VLAN segmentation and documented handover. Existing UniFi supported too.',
    "hero_img": 'aruba-instant-on-wifi-gold-coast-hero.webp',
    "hero_alt": 'A Ubiquiti UniFi network designed and installed by bcom ICT in a Gold Coast business',
    "h1": 'UniFi networks, designed and installed',
    "lede": 'Surveyed, specified, supplied and commissioned as a complete system — access points, switching, gateway and cabling — then documented and handed to you.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Designed, not guessed', 'Hardware supplied', 'Trade pricing', 'Documented on handover'],
    "crumbs": [('Services', '/services'), ('Business WiFi', '/business-wifi-gold-coast'), ('Ubiquiti UniFi', '/ubiquiti-unifi-wifi-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT designs, supplies and installs Ubiquiti UniFi networks for businesses across the Gold Coast — surveying the building, specifying access points, switching and gateway, running the cabling, configuring VLAN segmentation and handing over documentation. bcom ICT also supports existing UniFi installations, including earlier generations. Call 07 3041 8993.',
                     blocks=[       {       'cols': 4,
                'eyebrow': 'New installations',
                'h2': 'How we design and build a UniFi network',
                'steps': [       (       'Survey the building',
                                         'We measure signal, note the construction, find the interference '
                                         'and work out where access points actually need to go. A floor '
                                         'plan is not a survey.'),
                                 (       'Design the system',
                                         'Access point count and placement, switch capacity and PoE '
                                         'budget, gateway sizing, cable routes, and the VLANs — guest, '
                                         'staff, payments, cameras — planned before anything is ordered.'),
                                 (       'Supply the hardware',
                                         'Sourced at trade pricing and specified for the building rather '
                                         "than the catalogue. You can buy it yourself if you'd rather; "
                                         "we'll still tell you exactly what to get."),
                                 (       'Install and hand over',
                                         'Cabling by ACMA registered contractors, everything commissioned '
                                         'and tested, then network layout, VLAN structure and credentials '
                                         'documented and given to you.')],
                'sub': 'The order matters. Specifying hardware before knowing the building is how '
                       'businesses end up paying twice.'},
        {       'eyebrow': 'What we specify',
                'h2': 'The hardware we install',
                'html': models([('Wi-Fi 6 and Wi-Fi 7 access points', 'The current range. U6 for most offices, U7 where device density or throughput justifies it.', ['U6 Lite', 'U6 Pro', 'U6+', 'U6 LR', 'U6 Mesh', 'U6 In-Wall', 'U6 Enterprise', 'U7 Pro', 'U7 Pro Max', 'U7 Outdoor']), ('Wi-Fi 5 access points — still widely installed', "Plenty of Gold Coast offices are running these. Most still perform fine; we'll tell you when they're genuinely the bottleneck rather than selling a refresh.", ['UAP-AC-Lite', 'UAP-AC-Pro', 'UAP-AC-LR', 'UAP-AC-M', 'UAP-AC-IW', 'UAP-nanoHD', 'UAP-FlexHD', 'UAP-BeaconHD']), ('Gateways and controllers', 'The device that runs your network and hosts the controller. Which one you need depends on throughput and whether you want the controller on-site.', ['Dream Machine (UDM)', 'UDM Pro', 'UDM SE', 'Dream Router (UDR)', 'Cloud Gateway Ultra', 'Cloud Gateway Max', 'Cloud Key Gen2', 'Cloud Key Gen2 Plus', 'USG', 'USG-Pro-4']), ('PoE switches', 'The part most commonly under-specified. Access points, cameras and phones all draw PoE budget from here.', ['USW Lite 8 PoE', 'USW Lite 16 PoE', 'USW 16 PoE', 'USW 24 PoE', 'USW Pro 24 PoE', 'USW Pro 48 PoE', 'USW Flex', 'USW Flex Mini', 'USW Aggregation', 'US-8-60W', 'US-24-250W']), ('UniFi Protect cameras', 'Where the same system also covers CCTV, which is a large part of why businesses choose UniFi over Aruba.', ['G4 Bullet', 'G4 Dome', 'G4 Pro', 'G5 Bullet', 'G5 Dome', 'G5 Flex', 'AI Pro', 'UNVR', 'UNVR Pro']), ('UniFi Access and Talk', 'Door access and phones on the same controller. Worth knowing they exist before you buy a separate system for each.', ['UA-Hub', 'UA-Lite', 'UA-Pro', 'UA-G2', 'UniFi Talk Flex', 'UniFi Talk Touch']), ('Legacy access points — still supported', 'The original UniFi generations. Plenty are still in service across the Gold Coast and most are still doing their job.', ['UAP', 'UAP-LR', 'UAP-PRO', 'UAP-AC', 'UAP-AC-Outdoor', 'UAP-Outdoor+', 'UAP-AC-EDU', 'UAP-AC-HD', 'UAP-AC-SHD', 'UAP-XG', 'UAP-IW', 'UAP-IW-HD']), ('EdgeMax routers and switches', "Ubiquiti's other line, common where a network was built before UniFi gateways existed. We still configure and support it.", ['EdgeRouter X (ER-X)', 'ER-X-SFP', 'EdgeRouter 4', 'EdgeRouter 6P', 'EdgeRouter 12', 'EdgeRouter Lite', 'EdgeRouter PoE', 'EdgeSwitch 8', 'EdgeSwitch 16', 'EdgeSwitch 24', 'EdgeSwitch 48']), ('airMAX point-to-point links', 'For getting a network between two buildings without trenching — a shed, a second unit, a site across the yard.', ['NanoStation M5', 'NanoStation 5AC', 'NanoBeam 5AC', 'LiteBeam 5AC', 'PowerBeam 5AC', 'Rocket 5AC', 'LiteAP AC', 'AirFiber']), ('Legacy switches and gateways', 'Earlier UniFi switching and the original Security Gateway range.', ['US-8', 'US-8-60W', 'US-8-150W', 'US-16-150W', 'US-24', 'US-24-250W', 'US-48', 'US-48-500W', 'US-XG-6POE', 'USG', 'USG-Pro-4', 'USG-XG-8'])]),
                'sub': 'Current range. What goes in your building depends on the survey, not on what we '
                       'have in stock.'},
        {       'cards': [       (       'One system, one controller',
                                         None,
                                         'Access points, switching, gateway, cameras and door access '
                                         'managed together. Adding a site or an access point later is a '
                                         'change rather than a new project.'),
                                 (       'Segmentation done properly',
                                         None,
                                         "Guests, staff, payment terminals and devices on VLANs that can't "
                                         'reach each other. This is the security work that matters most, '
                                         'and UniFi makes it manageable to run.'),
                                 (       'Predictable ongoing cost',
                                         None,
                                         'No per-access-point subscription for core functionality. Over '
                                         "five years that's a material difference against some "
                                         'alternatives.'),
                                 (       "You can see what's happening",
                                         None,
                                         'Client counts, bandwidth, interference and errors, visible '
                                         'rather than guessed at. Turns future troubleshooting into '
                                         'looking instead of speculating.')],
                'cols': 2,
                'h2': 'Why UniFi for a new system',
                'icon': False},
        {       'cards': [       (       '"Our UAP-AC-Pro keeps dropping out"',
                                         None,
                                         'Usually PoE budget on the switch, a marginal cable run, or the '
                                         'access point unable to reach its controller. All three test '
                                         'quickly and none need new hardware.'),
                                 (       '"Devices won\'t roam between access points"',
                                         None,
                                         'Placement or transmit power — access points turned up too high '
                                         'overlap, and devices cling to a distant one. Fixable without '
                                         'buying anything.'),
                                 (       '"We added cameras and the WiFi got worse"',
                                         None,
                                         'Protect cameras draw PoE from the same switch budget as the '
                                         'access points. Exceeding it causes intermittent faults across '
                                         'everything.'),
                                 (       '"Nobody has the controller login"',
                                         None,
                                         'Very common once the original installer has moved on. Usually '
                                         'recoverable, and we hand back documented credentials that belong '
                                         'to you.')],
                'cols': 2,
                'eyebrow': 'Already running UniFi',
                'h2': "We support what you've already got, too",
                'icon': False,
                'sub': "Inherited, installed by someone who's moved on, or simply not behaving. All of it "
                       'is fixable, and it rarely needs replacing.'},
        {       'h2': 'Do you actually need new hardware?',
                'html': '<p style="max-width:68ch">We would rather tell you no. A UAP-AC-Pro serving '
                        'fifteen devices in a normal office is not the bottleneck, and replacing it '
                        'changes nothing you can measure.</p><p '
                        'style="max-width:68ch;margin-top:16px"><strong>New hardware is worth it '
                        'when</strong> you have genuine device density — thirty or more clients per access '
                        'point — you are moving large files over wireless, the gear has reached end of '
                        'software support, or you are fitting out new premises.</p><p '
                        'style="max-width:68ch;margin-top:16px"><strong>It is not the answer when</strong> '
                        'the complaint is coverage. Newer access points do not travel further through '
                        'walls. That is placement and cabling, and it is what the <a '
                        'href="/business-wifi-gold-coast">survey</a> resolves — sometimes for less than '
                        'the hardware would have cost.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Aruba Instant On WiFi', '/aruba-instant-on-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast')])
            + cta("Fitting out, or fixing what's there?", "Either way we'll survey the building first and quote on what it actually needs — including when the answer is that your existing gear is fine."),
}

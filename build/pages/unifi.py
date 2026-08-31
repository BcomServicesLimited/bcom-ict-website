from layout import cta, faq_block, related, svc_body, models

FAQS = [   (   'Who supports Ubiquiti UniFi on the Gold Coast?',
        'bcom ICT installs, configures and supports UniFi across the Gold Coast — UAP-AC-Lite, UAP-AC-Pro and UAP-AC-LR through the U6 range (U6 Lite, U6 Pro, U6 LR, U6 Mesh, U6 In-Wall) and U7, '
        'plus Dream Machine and Cloud Gateway controllers, USW PoE switches, Cloud Key and UniFi Protect. Call 07 3041 8993.'),
    (   'Why does our UAP-AC-Pro keep dropping off the network?',
        'The three usual causes are exceeding the PoE budget on the switch, a marginal or too-long cable run, and the access point being unable to reach its controller after a network change. All '
        'three are quick to test, and none of them need new hardware. Adding cameras or phones to the same switch is a very common trigger.'),
    (   'Do we need to upgrade from UAP-AC to U6 or U7?',
        'Usually not. A UAP-AC-Pro serving fifteen devices in an office is not the bottleneck. Upgrading is worth it for genuine device density — thirty or more clients per access point — or where '
        "hardware has reached end of software support. If the complaint is coverage, newer access points won't help; that's placement and cabling."),
    (   'Can you take over a UniFi network someone else installed?',
        "Yes, and it's common — often when the original installer has moved on and nobody has the controller login. That's usually recoverable, and we hand back documented credentials, network "
        'layout and VLAN structure that belong to you.'),
    (   'Which controller do we need — Cloud Key, Dream Machine or Cloud Gateway?',
        'It depends on throughput and whether you want the controller on-site. A Dream Machine or Cloud Gateway combines router, firewall and controller in one unit and suits most single-site '
        "businesses. A Cloud Key alongside an existing gateway suits sites where the routing is already handled. We'll specify for your setup rather than defaulting."),
    (   'Does UniFi cover cameras and door access too?',
        "Yes — UniFi Protect for cameras and UniFi Access for doors, on the same controller. It's a genuine advantage over alternatives, but it does mean planning PoE budget and switch capacity for "
        'all of it up front rather than discovering the limit later.')]

PAGE = {
    "path": '/ubiquiti-unifi-wifi-gold-coast',
    "priority": '0.7',
    "title": 'Ubiquiti UniFi Support Gold Coast — UAP, U6, UDM, USW | bcom ICT',
    "description": 'Ubiquiti UniFi installation and support across the Gold Coast — UAP-AC-Pro, U6 Pro, U7, Dream Machine, Cloud Gateway, USW switches and UniFi Protect. Surveyed, segmented and documented.',
    "hero_img": 'aruba-instant-on-wifi-gold-coast-hero.webp',
    "hero_alt": 'A Ubiquiti UniFi access point installed by bcom ICT in a Gold Coast business',
    "h1": 'Ubiquiti UniFi, installed and supported properly',
    "lede": 'From a single UAP-AC-Pro that keeps dropping out to a full UDM Pro estate across several sites. Excellent hardware, and a poor DIY project.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['All UniFi generations', 'Surveyed before quoting', 'VLAN segmentation', 'Documented on handover'],
    "crumbs": [('Services', '/services'), ('Business WiFi', '/business-wifi-gold-coast'), ('Ubiquiti UniFi', '/ubiquiti-unifi-wifi-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT installs, configures and supports Ubiquiti UniFi across the Gold Coast — access points from the UAP-AC range through U6 and U7, Dream Machine and Cloud Gateway controllers, USW PoE switches and UniFi Protect cameras. Work includes site survey, VLAN segmentation, controller setup and documented handover. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'Hardware',
                'h2': 'What we install and support',
                'html': models([('Wi-Fi 6 and Wi-Fi 7 access points', 'The current range. U6 for most offices, U7 where device density or throughput justifies it.', ['U6 Lite', 'U6 Pro', 'U6+', 'U6 LR', 'U6 Mesh', 'U6 In-Wall', 'U6 Enterprise', 'U7 Pro', 'U7 Pro Max', 'U7 Outdoor']), ('Wi-Fi 5 access points — still widely installed', "Plenty of Gold Coast offices are running these. Most still perform fine; we'll tell you when they're genuinely the bottleneck rather than selling a refresh.", ['UAP-AC-Lite', 'UAP-AC-Pro', 'UAP-AC-LR', 'UAP-AC-M', 'UAP-AC-IW', 'UAP-nanoHD', 'UAP-FlexHD', 'UAP-BeaconHD']), ('Gateways and controllers', 'The device that runs your network and hosts the controller. Which one you need depends on throughput and whether you want the controller on-site.', ['Dream Machine (UDM)', 'UDM Pro', 'UDM SE', 'Dream Router (UDR)', 'Cloud Gateway Ultra', 'Cloud Gateway Max', 'Cloud Key Gen2', 'Cloud Key Gen2 Plus', 'USG', 'USG-Pro-4']), ('PoE switches', 'The part most commonly under-specified. Access points, cameras and phones all draw PoE budget from here.', ['USW Lite 8 PoE', 'USW Lite 16 PoE', 'USW 16 PoE', 'USW 24 PoE', 'USW Pro 24 PoE', 'USW Pro 48 PoE', 'USW Flex', 'USW Flex Mini', 'USW Aggregation', 'US-8-60W', 'US-24-250W']), ('UniFi Protect cameras', 'Where the same system also covers CCTV, which is a large part of why businesses choose UniFi over Aruba.', ['G4 Bullet', 'G4 Dome', 'G4 Pro', 'G5 Bullet', 'G5 Dome', 'G5 Flex', 'AI Pro', 'UNVR', 'UNVR Pro']), ('UniFi Access and Talk', 'Door access and phones on the same controller. Worth knowing they exist before you buy a separate system for each.', ['UA-Hub', 'UA-Lite', 'UA-Pro', 'UA-G2', 'UniFi Talk Flex', 'UniFi Talk Touch']),
 ('Legacy access points — still supported',
  'The original UniFi generations. Plenty are still in service across the Gold Coast and most are still doing their job.',
  ['UAP', 'UAP-LR', 'UAP-PRO', 'UAP-AC', 'UAP-AC-Outdoor', 'UAP-Outdoor+', 'UAP-AC-EDU',
   'UAP-AC-HD', 'UAP-AC-SHD', 'UAP-XG', 'UAP-IW', 'UAP-IW-HD']),
 ('EdgeMax routers and switches',
  "Ubiquiti's other line, common where a network was built before UniFi gateways existed. We still configure and support it.",
  ['EdgeRouter X (ER-X)', 'ER-X-SFP', 'EdgeRouter 4', 'EdgeRouter 6P', 'EdgeRouter 12',
   'EdgeRouter Lite', 'EdgeRouter PoE', 'EdgeSwitch 8', 'EdgeSwitch 16', 'EdgeSwitch 24', 'EdgeSwitch 48']),
 ('airMAX point-to-point links',
  'For getting a network between two buildings without trenching — a shed, a second unit, a site across the yard.',
  ['NanoStation M5', 'NanoStation 5AC', 'NanoBeam 5AC', 'LiteBeam 5AC', 'PowerBeam 5AC',
   'Rocket 5AC', 'LiteAP AC', 'AirFiber']),
 ('Legacy switches and gateways',
  'Earlier UniFi switching and the original Security Gateway range.',
  ['US-8', 'US-8-60W', 'US-8-150W', 'US-16-150W', 'US-24', 'US-24-250W', 'US-48', 'US-48-500W',
   'US-XG-6POE', 'USG', 'USG-Pro-4', 'USG-XG-8'])]),
                'sub': 'If you already own it, we support it — including the older generations most '
                       'installers would rather replace.'},
        {       'cards': [       (       '"Our UAP-AC-Pro keeps dropping out"',
                                         None,
                                         'Usually PoE budget on the switch, a marginal cable run, or the '
                                         'access point adopting to a controller it can no longer reach. '
                                         'All three are quick to test and none need new hardware.'),
                                 (       '"Devices won\'t roam between access points"',
                                         None,
                                         'Nearly always placement or power settings — access points turned '
                                         'up too high overlap and devices cling to a distant one. '
                                         'Measurable, and fixable without buying anything.'),
                                 (       '"The controller says the AP is disconnected"',
                                         None,
                                         'Adoption and provisioning problems, often after a firmware '
                                         'update or a network change. Recoverable in most cases without a '
                                         'factory reset.'),
                                 (       '"We added cameras and now the WiFi is worse"',
                                         None,
                                         'UniFi Protect cameras draw PoE from the same switch budget as '
                                         'the access points. Exceeding it causes intermittent, baffling '
                                         'faults across everything.'),
                                 (       '"Nobody knows the controller login"',
                                         None,
                                         'Extremely common when the original installer has moved on. '
                                         'Usually recoverable, and we hand over documented credentials '
                                         'that belong to you.'),
                                 (       '"Guest WiFi can see our server"',
                                         None,
                                         'VLANs were never configured. The hardware supports proper '
                                         'segmentation; it just needs someone to set it up.')],
                'cols': 2,
                'eyebrow': 'Symptoms',
                'h2': 'What people actually call about',
                'icon': False},
        {       'h2': 'Which generation do you actually need?',
                'html': '<p style="max-width:68ch">A common and expensive mistake is refreshing an entire '
                        'estate because the model numbers look old. A UAP-AC-Pro in a normal office with '
                        'fifteen devices on it is not the bottleneck, and replacing it will change nothing '
                        'you can measure.</p><p style="max-width:68ch;margin-top:16px"><strong>Worth '
                        'upgrading when:</strong> you have genuine device density — thirty or more clients '
                        'per access point — or you are running large file transfers over wireless, or the '
                        'hardware has reached end of software support.</p><p '
                        'style="max-width:68ch;margin-top:16px"><strong>Not worth upgrading when:</strong> '
                        'the complaint is coverage. More capable access points do not travel further '
                        'through walls. That is a placement and cabling problem, and it is what a <a '
                        'href="/business-wifi-gold-coast">site survey</a> answers.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Aruba Instant On WiFi', '/aruba-instant-on-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast')])
            + cta('Know your model number?', "Tell us what you've got and what it's doing. Most UniFi faults are diagnosed on the phone before anyone travels."),
}

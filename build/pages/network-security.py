from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("“Our firewall is on but we’ve never touched it”",
     "factory defaults. It permits far more than it should, and the admin password may still be the one it shipped with.",
     "Review the ruleset against how the business actually operates, change the credentials, and remove the permissions nobody needs. Usually a couple of hours with a disproportionate effect."),
    ("“Guests can reach our server”",
     "one flat network. The guest WiFi feature exists on the hardware and was never actually configured.",
     "Segment properly — staff, guests, payment terminals and building devices on VLANs that cannot reach each other. Cheap to build in, awkward to retrofit, and the highest-value network change most businesses can make."),
    ("“Remote desktop is how we work from home”",
     "RDP published directly to the internet. One of the most reliably exploited routes into an Australian small business.",
     "Move it behind a VPN or a controlled access broker with multi-factor authentication. This is worth changing this month rather than adding to a roadmap."),
    ("“There are firewall rules nobody can explain”",
     "rules added for a supplier, a project or a staff member who left years ago, and never removed.",
     "Review each rule against a current business reason. Anything without one goes. Over years a ruleset stops describing how the business works."),
    ("“The firewall firmware is years old”",
     "nobody owns patching the edge device, and it does not prompt anyone the way a workstation does.",
     "Bring it current and keep it there. Edge devices are actively targeted, and an unpatched firewall is worse than none because it is trusted."),
    ("“We wouldn’t know if someone got in”",
     "no logging, or logs retained for days rather than months.",
     "Enable logging and retain it long enough to be useful. After an incident this determines whether you can establish what was reached — or have to assume the worst."),
]

EXAMPLE_1 = example(
    "Remote desktop published to the internet",
    "A Gold Coast business had staff working from home by connecting to office machines over remote desktop, exposed directly to the internet with a port forward. It had worked fine for three years.",
    "The firewall logs showed continuous automated login attempts against those machines — thousands per day, from everywhere. No account lockout, no MFA, and one account using a password that appeared in a known breach list.",
    "Closed the exposure, put remote access behind a VPN with multi-factor authentication, reset the affected credentials, and reviewed the logs for any successful access. None had succeeded, which was largely luck.",
    "Remote working continued unchanged from the users’ point of view. The difference was that the front door stopped being open to the internet.")

EXAMPLE_2 = example(
    "A flat network in a venue taking card payments",
    "A Gold Coast hospitality business asked us to look at slow WiFi. The network turned out to be a more pressing problem.",
    "Everything sat on one flat network — guest WiFi, staff laptops, the point of sale, EFTPOS terminals and a set of cameras installed by a third party with default credentials. Any device on the guest network could reach all of it.",
    "Rebuilt the network into four segments: staff, guests with internet only, payment terminals isolated, and building devices separated. Changed the camera credentials and firmware. Fixed the wireless capacity issue that had prompted the call in the first place.",
    "The WiFi complaint was resolved, and a PCI-DSS exposure that nobody had identified was closed at the same time — for materially less than retrofitting it after an incident.")

EXAMPLE_3 = example(
    "A firewall rule from a supplier who had left",
    "A Gold Coast business asked for a firewall review before a compliance audit, expecting a formality.",
    "Eleven rules nobody could explain. One permitted inbound access from a fixed external address belonging to a software supplier the business had stopped using four years earlier. The rule had outlived the relationship, the contract and the person who requested it.",
    "Traced each rule to a current business reason, removed those without one, documented the remainder, and set an annual review so the ruleset stays a description of how the business works.",
    "Eleven unnecessary openings closed, including one that had been available to a third party for four years. The audit was a formality after that, rather than before it.")

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
    "description": "Business firewall and network security for Gold Coast offices — next-generation firewall setup, VLAN segmentation, secure remote access. Call 07 3041 8993.",
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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What we find when we look at a business firewall</h2>
      <p>Five of these six turn up in almost every network we are asked to review.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a network review actually turns up</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([('DrayTek Routers', '/draytek-router-gold-coast'),
        ('Sophos Firewalls', '/sophos-firewall-gold-coast'),
        ('FortiGate Firewalls', '/fortigate-firewall-gold-coast'),
               ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast')])
            + cta('When was your firewall last reviewed?', "If nobody can answer that, it's worth an hour. We'll tell you what it's actually doing and what it should be."),
}

from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;Everything is slow, but the speed test is fine&rdquo;",
     "a bottleneck inside the building rather than on the internet connection. A speed test measures the path to the internet and tells you nothing about the path to your own server.",
     "Check the negotiated link speed on every port rather than the advertised one. A single damaged run negotiating at 100Mbps instead of 1Gbps will drag an entire office down, and it does not announce itself."),
    ("&ldquo;It drops out at the same time every afternoon&rdquo;",
     "something on a schedule &mdash; a backup, a sync, an antivirus update &mdash; saturating a link that has no capacity to spare. Occasionally it is a second device handing out IP addresses alongside the real one.",
     "Watch the traffic across a full day instead of guessing. A fault that keeps time is nearly always caused by something that also keeps time, which makes it one of the easier faults to pin down once anyone actually looks."),
    ("&ldquo;We plugged something in and half the office went offline&rdquo;",
     "a loop. Someone has connected both ends of a patch lead into the same unmanaged switch, or joined two wall ports, and the network is now flooding itself.",
     "Find and break the loop, then put loop protection on the switching so it cannot happen twice. Cheap unmanaged switches under desks are the usual culprit, and they are worth removing rather than tolerating."),
    ("&ldquo;One site works and the other doesn&rsquo;t&rdquo;",
     "the link between sites, not the sites themselves. A wireless bridge that has drifted out of alignment, a VPN dropping and re-establishing, or routing that was never set up symmetrically.",
     "Test the link in isolation before touching anything at either end. Multi-site faults get blamed on the far site by the near site and vice versa, which is how they survive for years."),
    ("&ldquo;It was fine until we moved the desks&rdquo;",
     "outlets that were never live being pressed into service, or a patch panel repatched by whoever moved the furniture. The network did not change &mdash; what it was asked to do changed.",
     "Trace what is actually connected where and patch it properly. This is the fault most often described as inexplicable, and it is almost always explicable within twenty minutes of opening the cabinet."),
    ("&ldquo;Nobody knows what any of it does&rdquo;",
     "a network that grew rather than was designed &mdash; added to by several providers over a decade, none of whom wrote anything down.",
     "Document it. Ports, VLANs, addresses, what each device is for and who supplied it. Not glamorous, but it converts every future fault from an investigation into a lookup, and it is yours to keep."),
]

EXAMPLE_1 = example(
    "Two years of blaming the server, and it was one cable",
    "An accounting firm of twenty-two staff had been told their file server was undersized. Opening a client file took the best part of a minute, and it had been getting slowly worse for two years. A quote to replace the server was already on the table.",
    "The server was fine. The single cable running from the server cabinet to the main office switch had been damaged at some point and was negotiating at 100Mbps instead of 1Gbps. Every file the office opened crossed that one link. Nothing reported an error, because from the network&rsquo;s point of view nothing was wrong &mdash; it had simply agreed to run ten times slower.",
    "Replaced and certified the run, then checked every other link in the building for the same thing and found two more.",
    "File opens went from roughly forty seconds to under three. The server they were about to replace is still in service. The fault had cost them two years of lost minutes and would have cost them a server on top.")

EXAMPLE_2 = example(
    "The $28,000 upgrade they didn&rsquo;t need",
    "A manufacturer running two buildings on one site had been quoted for a complete switching replacement to fix persistent slowness between the office and the factory. They asked for a second opinion before signing.",
    "The switching was adequate. The two buildings were joined by a wireless bridge mounted on the office roof, and a tree planted after the bridge was installed had grown into the path. Performance had degraded over three years at roughly the rate the tree grew, which is why nobody connected the two.",
    "Relocated and re-aimed the bridge to a clear line of sight, then measured the link before and after so the improvement was demonstrable rather than asserted.",
    "Throughput between buildings returned to full. The quoted upgrade was not carried out, because it would not have fixed anything &mdash; new switches at both ends of an obstructed radio link perform exactly as badly as old ones.")

FAQS = [   (   'Who installs business networks on the Gold Coast?',
        'bcom ICT designs, installs and supports business networks across the Gold Coast — switching, routing, firewalls, structured cabling and business WiFi — delivered as one system with a single '
        'point of accountability. Cabling is carried out by ACMA registered cabling contractors that bcom ICT engages and manages. Call 07 3041 8993.'),
    (   'Can you take over a network someone else installed?',
        'Yes, and it is common. The first step is documenting what actually exists, because that is usually the thing missing. From there we can tell you what is sound, what needs attention and what '
        'was done badly enough to redo.'),
    (   'Do we need business-grade switches, or will consumer gear do?',
        "It depends on scale and what you're powering. Once you have access points, cameras or phones needing Power over Ethernet, VLANs to keep guests separate, or more than about a dozen users, "
        'consumer gear stops being cheaper — it just moves the cost into troubleshooting time.'),
    (   'How long does a network installation take?',
        "A small office fit-out is usually a few days including cabling. Larger sites or occupied offices take longer because the work is staged after hours. We'll give you a schedule after the site "
        'survey rather than an estimate before it.'),
    (   'Will you document it?',
        'Yes — diagrams, labelling at both ends, credentials and an asset register, all handed to you. It is yours, and you can ask for a copy at any time rather than only on exit.')]

PAGE = {
    "path": '/computer-networking-service-gold-coast',
    "priority": '0.75',
    "service": 'Computer Networking Service Gold Coast',
    "title": 'Business Computer Networking Gold Coast | bcom ICT',
    "description": "Business networks designed, installed and supported on the Gold Coast — switching, routing, WiFi, cabling and firewalls built as one system, not four.",
    "hero_img": 'hero-bg-networking.webp',
    "hero_alt": 'Business network switching and infrastructure installed by bcom ICT on the Gold Coast',
    "h1": 'One network, one team, one number to call',
    "lede": 'Switching, routing, WiFi, cabling and firewalls designed together — rather than four suppliers each blaming the other three.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Designed as one system', 'One point of accountability', 'Documented on handover', 'Since 2011'],
    "crumbs": [('Services', '/services'), ('Computer Networking', '/computer-networking-service-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT designs, installs and supports business computer networks across the Gold Coast — switching, routing, structured cabling, business WiFi and firewalls — delivered as one system with a single point of accountability rather than split across separate suppliers. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'The blame loop',
                                         None,
                                         "The WiFi installer says it's the cabling. The cabler says it's "
                                         "the switch. The phone company says it's the internet. Meanwhile "
                                         "nobody owns the fault and you're the one coordinating three "
                                         'trades who have never spoken.'),
                                 (       'Nothing was designed together',
                                         None,
                                         'Access points specified without checking the switch has PoE '
                                         'capacity. Cabling run before anyone decided where the rack goes. '
                                         "Each piece is fine; the system isn't."),
                                 (       'No documentation exists',
                                         None,
                                         'Every supplier documented their own part, if at all. Nobody has '
                                         'a diagram of the whole thing, which makes every future change an '
                                         'investigation.'),
                                 (       'Nobody reviews it',
                                         None,
                                         'Networks are installed and then left. Firmware ages, rules '
                                         'accumulate, capacity gets outgrown quietly — until something '
                                         "breaks and it's an emergency.")],
                'cols': 2,
                'eyebrow': 'The problem with split suppliers',
                'h2': 'Four vendors, nobody responsible',
                'icon': False,
                'sub': "The most common networking problem we're called to isn't technical."},
        {       'h2': 'What we design and support',
                'ticks': [       '<strong>Switching</strong> — capacity, PoE budget for access points, '
                                 'cameras and phones, and VLANs planned before anything is bought',
                                 '<strong>Routing and firewalls</strong> — segmentation, secure remote '
                                 'access and rules written to match how your business works',
                                 '<strong>Business WiFi</strong> — Ubiquiti UniFi and Aruba Instant On, '
                                 'surveyed before quoting',
                                 '<strong>Structured cabling</strong> — Cat6 and Cat6A, installed by ACMA '
                                 'registered cabling contractors we engage and manage',
                                 '<strong>Internet and failover</strong> — including 4G or 5G backup so an '
                                 "outage doesn't stop you trading",
                                 '<strong>Documentation you keep</strong> — diagrams, labelling, '
                                 'credentials and an asset register that belongs to you']},
        {       'h2': 'Ongoing, or one-off',
                'html': '<p style="max-width:68ch">Plenty of clients have us design and install a network '
                        'and then call when something needs changing. That is a perfectly reasonable '
                        'arrangement and we support it.</p><p style="max-width:68ch;margin-top:16px">The '
                        'alternative is having the network monitored and maintained as part of <a '
                        'href="/managed-it-services-for-small-businesses-gold-coast">managed IT</a> — '
                        'firmware kept current, capacity watched, rules reviewed, and faults noticed '
                        'before somebody reports them. Which suits you depends on how much a day of '
                        'downtime costs, and we will give you an honest view rather than a default '
                        'answer.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The network faults we are actually called to</h2>
      <p>Six complaints account for most of what we see. Only one of them usually needs new hardware.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What fixing a network actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta("Fitting out, moving, or fixing what's there?", "We'll survey it and design the whole thing together — so there's one person to call when something isn't right."),
}

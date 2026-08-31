from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;Our remote access stopped after the provider swapped the modem&rdquo;",
     "a replacement unit delivered on factory settings. Every rule, forward and reservation that had been configured on the old one is gone, and nobody records them because nobody expects the swap.",
     "Rebuild the configuration and then keep a copy of it. A modem replacement is a routine event that takes a business offline for a day when nothing was documented."),
    ("&ldquo;Two routers, and half our things don&rsquo;t work&rdquo;",
     "double NAT &mdash; a business router behind a provider&rsquo;s modem, both handing out addresses and both translating traffic. Ordinary browsing works and anything needing an inbound connection does not.",
     "Put the provider&rsquo;s unit into a pass-through mode and let one device do the routing. Half the strange faults on small business networks come from two devices both believing they are in charge."),
    ("&ldquo;We&rsquo;re using the router the provider gave us&rdquo;",
     "equipment supplied to meet a price, adequate for a household and frequently not for a business with staff, VoIP and cloud applications.",
     "Assess whether it is genuinely the constraint before replacing it &mdash; sometimes it is fine. Where it is not, a business-grade unit changes far more than an internet plan upgrade would."),
    ("&ldquo;Devices get a different address every time&rdquo;",
     "no reserved addresses, so printers, terminals and access points move around whenever something restarts and stop being findable.",
     "Reserve addresses for anything that needs to be found reliably. This is a ten-minute job that prevents a recurring category of fault nobody ever connects to its cause."),
    ("&ldquo;The firmware has never been updated&rdquo;",
     "a device installed years ago and never revisited. Routers are directly exposed to the internet and are a genuine target.",
     "Update it, and check whether it is still receiving updates at all. A router the manufacturer has stopped supporting is a security problem regardless of how well it is performing."),
    ("&ldquo;The default password is still on it&rdquo;",
     "an installation that was never finished properly. Frequently the password is printed on a label on the device itself.",
     "Change it, disable remote administration from the internet, and record the new credentials somewhere the business controls. This is the shortest and most valuable job on this page."),
]

EXAMPLE_1 = example(
    "A modem swap that took a business offline for a day",
    "A business lost access to its own systems from outside the office after their internet provider replaced a faulty modem. The provider had done nothing wrong and the replacement was working correctly.",
    "The original unit had carried port forwards for a remote access arrangement, address reservations for the printers and payment terminal, and a configured guest network. The replacement arrived on factory settings, as replacements do. None of the original configuration had been documented, so it had to be reconstructed from what staff could describe and from what failed.",
    "Rebuilt the configuration, then exported and stored it so a future replacement is a fifteen-minute restore. Reserved addresses for every device that needs to be found and moved the remote access onto something more appropriate than a port forward.",
    "Remote access works and the next modem swap will not repeat this. Provider hardware gets replaced routinely, and a business with no copy of its own configuration loses a day every time it happens.")

EXAMPLE_2 = example(
    "Two devices both convinced they were in charge",
    "A business had installed a capable business router behind their provider&rsquo;s modem. Browsing and email were fine. Their phone system, remote access and a supplier&rsquo;s ordering integration all behaved strangely, and had done since the day the router was installed.",
    "Both devices were routing and translating traffic independently. Anything initiating a connection outward worked normally, and anything needing a connection inward reached the first device and stopped. This is a textbook double NAT and it had been diagnosed twice as a problem with the phone system.",
    "Placed the provider&rsquo;s unit into pass-through so the business router handled routing alone, then rebuilt the forwarding rules once, in one place.",
    "All three problems resolved at the same moment, which is what tends to happen when the actual cause is finally addressed rather than the three symptoms it produces.")

EXAMPLE_3 = example(
    "A router still carrying the password printed on its label",
    "A business asked us to look at an internet connection that had felt slow for months. The complaint was performance and the expectation was that a faster plan would be recommended.",
    "The connection itself was delivering close to its rated speed at the boundary. The router had been installed six years earlier and had never had its firmware updated &mdash; the manufacturer had stopped issuing updates for it three years before that. Remote administration was enabled and reachable from the internet, and the administrative password was still the default one printed on a sticker on the underside of the unit. The device&rsquo;s logs, once we could read them, showed sustained automated login attempts going back as far as the logs were retained. Whether any had succeeded could not be established, because the logging retained too little to say.",
    "Replaced the router with a supported business unit, disabled internet-facing administration entirely, set credentials held in the business&rsquo;s password manager, and rebuilt the configuration properly. Advised the business to treat any credential that had passed through that device as potentially exposed and to reset the important ones.",
    "The connection is no longer slow, which was the presenting complaint and by some distance the least important thing we found. The device had been quietly indefensible for three years and nobody had any reason to look at it, because it had never stopped working.")
FAQS = [   (   'Should we use the router our internet provider supplied?',
        "For a small setup, often yes, once it's properly configured. It typically becomes the bottleneck once you're running VoIP phones, a VPN and thirty or more devices — well before the "
        'connection itself struggles. We measure before recommending a replacement.'),
    (   "What's the first thing to change on a new router?",
        'The default admin password. Router default credentials are published online by model, so a device still on factory settings is accessible to anyone who reaches the network. After that: '
        'firmware updates, guest network separation and voice prioritisation if you use VoIP.'),
    (   'Our calls break up when someone uploads a file. Why?',
        "Voice traffic isn't being prioritised. Without quality-of-service configuration, a large upload competes directly with your phone calls. It's a configuration change rather than a hardware "
        'problem in most cases.'),
    (   'Can you set up a router remotely?',
        "Frequently yes — remote support is $190 + GST per hour with no call-out. If it needs physical replacement or rewiring, we'll book a visit and tell you the cost first.")]

PAGE = {
    "path": '/router-and-modem-configuration-gold-coast',
    "priority": '0.65',
    "title": 'Router & Modem Configuration Gold Coast — Business | bcom ICT',
    "description": 'Router and modem configuration for Gold Coast businesses and home offices — set up securely, with voice traffic prioritised and default passwords changed.',
    "hero_img": 'hero-bg-router-modem.webp',
    "hero_alt": 'A business router being configured by bcom ICT on the Gold Coast',
    "h1": 'Routers configured, not just plugged in',
    "lede": "New connection, new router, or one that's been quietly running on factory defaults since it arrived.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Defaults changed', 'Voice prioritised', 'Secure remote access', 'Documented'],
    "crumbs": [('Services', '/services'), ('Computer Networking', '/computer-networking-service-gold-coast'), ('Router & Modem Configuration', '/router-and-modem-configuration-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT configures routers and modems for Gold Coast businesses and home offices — securing the device, changing default credentials, prioritising voice traffic where VoIP is in use, setting up guest and staff separation, and documenting the configuration. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'The default admin password',
                                         None,
                                         'Still the single most common finding. A router on factory '
                                         'credentials is reachable by anyone who gets onto the network, '
                                         'and the passwords are published online by model.'),
                                 (       'Voice prioritisation',
                                         None,
                                         'If you run VoIP phones, voice traffic needs priority over a '
                                         'large upload. Without it, calls break up at exactly the moment '
                                         'someone sends a big file.'),
                                 (       'Guest and staff separation',
                                         None,
                                         'Visitors on a network that reaches your business systems is a '
                                         'genuine exposure, and most supplied routers are capable of '
                                         'separating them once someone configures it.'),
                                 (       'Firmware',
                                         None,
                                         'Routers need patching like anything else, and edge devices are '
                                         'actively targeted. An unpatched router is worse than none '
                                         "because it's trusted.")],
                'cols': 2,
                'eyebrow': 'What we change',
                'h2': 'What a proper configuration involves',
                'icon': False},
        {       'h2': 'When the router is the problem',
                'html': '<p style="max-width:68ch">Provider-supplied routers are built to a price. '
                        "They're adequate for a household and frequently become the bottleneck once a "
                        'business is running VoIP, a VPN, and thirty devices — long before the connection '
                        'itself struggles.</p><p style="max-width:68ch;margin-top:16px">Symptoms look like '
                        'slow internet: calls breaking up, connections dropping under load, remote access '
                        "that stalls. We measure before recommending a replacement, because sometimes it's "
                        'configuration rather than capacity — see <a '
                        'href="/network-troubleshooting-diagnostics-gold-coast">network '
                        'troubleshooting</a>.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The router and modem problems we are actually called to</h2>
      <p>Six situations. Several of them look like faults in something else entirely.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What router and modem work actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Mesh WiFi Setup', '/mesh-network-setup-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Remote IT Support', '/remote-it-support-gold-coast')])
            + cta('Router still on factory settings?', "It's a short job with a disproportionate benefit — and we can usually do it remotely."),
}

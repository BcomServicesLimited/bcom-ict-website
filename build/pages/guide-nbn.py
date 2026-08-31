from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Is business NBN worth it over a residential plan?',
        'It depends what an hour offline costs you. A business plan typically buys a faster fault response commitment from the provider and, on some plan types, guaranteed rather than best-effort '
        'speed. It does not prevent outages. For most Gold Coast small businesses, an automatic 4G or 5G failover connection delivers more value than a premium plan.'),
    (   'What speed does a business actually need?',
        "Usually less than expected, because speed is rarely the bottleneck. Wireless congestion, an underpowered router or a device flooding the connection cause most complaints. Measure what's "
        'actually happening before upgrading a plan — the upgrade often changes nothing.'),
    (   'What is internet failover and do we need it?',
        'A secondary 4G or 5G connection that takes over automatically when the primary drops, keeping card payments, phones and cloud applications running. If you take card payments, use VoIP '
        "phones, or simply can't stop trading, it's the highest-value thing you can spend money on and costs less than a premium plan."),
    (   'Why is our internet slow at certain times of day?',
        'Usually contention on the network — either inside your building, where a backup job or large upload is competing, or in the surrounding area at peak times. Traffic analysis distinguishes '
        'the two, and only one of them is fixable by changing plans.'),
    (   'Can you deal with our internet provider?',
        "Yes, and it's often the most useful part of the job. We run line tests, capture logs and document the fault, then handle the escalation. Providers close documented faults far less readily "
        'than undocumented ones.'),
    (   'Do you sell internet connections?',
        "No. bcom ICT is not a reseller and earns nothing from your plan choice, which means our advice on whether the connection is the problem isn't influenced by wanting to sell you a different "
        'one.')]

PAGE = {
    "path": '/business-nbn-guide-gold-coast',
    "priority": '0.7',
    "article": True,
    "title": 'Business NBN Guide — Gold Coast Businesses | bcom ICT',
    "description": 'A plain-English guide to business NBN for Gold Coast businesses — connection types, business versus residential plans, what speed you actually need, and why failover matters.',
    "hero_kind": 'page',
    "eyebrow": "Guide",
    "hero_img": 'nbn-internet-support-hero.webp',
    "hero_alt": 'Business NBN connection and networking equipment installed by bcom ICT on the Gold Coast',
    "h1": 'Business NBN, explained plainly',
    "lede": 'What the connection types actually mean, whether a business plan is worth the premium, and the one thing worth spending money on that almost nobody does.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Business vs residential', 'Failover explained', 'Vendor-neutral', 'Gold Coast specific'],
    "crumbs": [("Guides", "/services"), ('Business NBN guide', '/business-nbn-guide-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='Business NBN plans typically differ from residential ones in fault response commitments and, on some plan types, guaranteed rather than best-effort speeds. For most Gold Coast businesses the more valuable investment is not a faster plan but an automatic 4G or 5G failover connection, since a total outage costs far more than a slow connection. bcom ICT is not a reseller and does not earn from plan recommendations.',
                     blocks=[       {       'cards': [       (       "It's usually the WiFi",
                                         None,
                                         'One access point serving forty devices behaves nothing like one '
                                         'serving five. Most "slow internet" complaints in Gold Coast '
                                         'offices are wireless congestion, and no plan upgrade fixes it.'),
                                 (       'Or the router',
                                         None,
                                         "Provider-supplied routers are built to a price. Once you're "
                                         'running VoIP, a VPN and thirty devices, they become the '
                                         'bottleneck long before the connection does.'),
                                 (       'Or something flooding it',
                                         None,
                                         'A backup running during business hours, a device misbehaving, a '
                                         'large upload nobody mentioned. Traffic analysis finds it in '
                                         "minutes; guessing doesn't."),
                                 (       'Sometimes it genuinely is the service',
                                         None,
                                         'And then the job is evidence — line testing and logs so the '
                                         'provider can\'t close the ticket as "no fault found".')],
                'cols': 2,
                'eyebrow': 'First',
                'h2': 'Speed is usually not your problem',
                'icon': False,
                'sub': "Before upgrading anything, it's worth knowing what's actually slow."},
        {       'h2': 'Business plan or residential?',
                'html': '<p style="max-width:68ch">The honest answer is that it depends on what an hour '
                        'offline costs you, and that the marketing overstates the difference.</p><p '
                        'style="max-width:68ch;margin-top:16px"><strong>What a business plan typically '
                        'buys:</strong> a faster fault response commitment from the provider, and on some '
                        'plan types a guaranteed rather than best-effort speed. Static IP addresses are '
                        'usually included, which matters if you host anything or use certain VPN '
                        'setups.</p><p style="max-width:68ch;margin-top:16px"><strong>What it doesn\'t '
                        'buy:</strong> immunity from outages. A business plan means someone responds '
                        "faster when it breaks — not that it won't break. For most small businesses, the "
                        'money is better spent on failover than on a premium plan.</p>'},
        {       'eyebrow': 'The one thing worth doing',
                'h2': 'Failover is cheap insurance',
                'ticks': [       '<strong>A 4G or 5G backup connection</strong> that takes over '
                                 'automatically when the primary drops — no hotspot, nobody plugging '
                                 'anything in while customers wait.',
                                 '<strong>Card payments keep working</strong>, which for retail and '
                                 'hospitality is the difference between trading and closing.',
                                 "<strong>Phones keep working</strong> if you're on VoIP — otherwise an "
                                 'internet outage takes your phone system down with it.',
                                 '<strong>It has to be tested</strong>, not assumed. An untested failover '
                                 'is a theory.',
                                 '<strong>It costs far less than a premium plan</strong> and covers the '
                                 'failure mode that actually hurts.']},
        {       'cards': [       (       'What connection type is available here?',
                                         None,
                                         "It varies street by street on the Gold Coast, and what's "
                                         'available at the address matters more than what the plan '
                                         'advertises. Check before signing a lease if you can.'),
                                 (       "What's the contract term?",
                                         None,
                                         'Business plans often carry longer terms than residential. Worth '
                                         'knowing before you commit, particularly if the lease is '
                                         'shorter.'),
                                 (       'Is the router included, and is it adequate?',
                                         None,
                                         'Frequently included and frequently underpowered for a business. '
                                         "Budget for a proper one rather than discovering it's the "
                                         'bottleneck later.'),
                                 (       "What's the actual fault response commitment?",
                                         None,
                                         'Get it in writing. "Priority support" without a stated response '
                                         'window is marketing.')],
                'cols': 2,
                'h2': 'Practical questions before you sign anything',
                'icon': False},
        {       'h2': "We don't sell connections",
                'html': '<p style="max-width:68ch">bcom ICT is not an internet reseller and earns nothing '
                        'from which plan you choose. That means our answer to "is our connection the '
                        'problem?" isn\'t influenced by wanting to sell you a different one — and quite '
                        'often the answer is no.</p><p style="max-width:68ch;margin-top:16px">What we do '
                        "is measure what's actually happening, tell you whether the bottleneck is inside "
                        'or outside the building, and handle the provider escalation with evidence when '
                        'the fault is theirs. See <a href="/nbn-internet-support-gold-coast">business NBN '
                        'and internet support</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business NBN & Internet Support', '/nbn-internet-support-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Router & Modem Configuration', '/router-and-modem-configuration-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast')])
            + cta("Not sure if it's your connection?", "We'll measure it and tell you honestly — including when the answer is that your plan is fine and something else is wrong."),
}

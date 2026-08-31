from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Why is our business internet so slow?',
        'In most cases the connection is not the cause — saturated WiFi, a failing cable or switch port, an underpowered router or a device flooding the network usually is. bcom ICT measures the '
        'network before recommending a service upgrade, so you are not paying more for a connection that was never the bottleneck. Call 07 3041 8993.'),
    (   'Can you deal with our internet provider for us?',
        'Yes, and it is often the most valuable part of the job. We run line tests, capture logs and document the fault, then handle the escalation. Providers close documented faults far less '
        'readily than undocumented ones.'),
    (   'What happens to our phones if the internet drops?',
        "On a VoIP system, calls can fail over automatically to mobiles. Pairing that with a 4G or 5G backup connection keeps both phones and payment terminals working. It's worth configuring before "
        'an outage rather than after.'),
    (   'Do you supply internet services?',
        "We are not a reseller — we work with whatever provider you're with, which means our advice on whether the service is the problem isn't influenced by wanting to sell you a different one. "
        "We'll tell you when changing provider is genuinely the answer."),
    (   'Is business NBN different from residential?',
        'Business-grade services typically carry better fault response commitments and, on some plan types, guaranteed rather than best-effort performance. Whether the difference is worth the cost '
        'depends on what an hour offline costs you — which is a conversation worth having before an outage, not during one.'),
    ('How quickly can you look at it?', 'Same-day attendance is usually available across the Gold Coast, and many connection faults can be diagnosed remotely before anyone travels.')]

PAGE = {
    "path": '/nbn-internet-support-gold-coast',
    "priority": '0.75',
    "service": 'Business NBN & Internet Support Gold Coast',
    "title": 'Business NBN & Internet Support Gold Coast | bcom ICT',
    "description": "NBN and business internet support on the Gold Coast — modem and router configuration, line testing, ISP escalation and 4G/5G failover so an outage doesn't stop you trading.",
    "hero_img": 'nbn-internet-support-hero.webp',
    "hero_alt": 'Business NBN and internet connection being tested by bcom ICT on the Gold Coast',
    "h1": 'When the internet goes down, so does the business',
    "lede": 'Line testing, provider escalation with evidence, and failover so an outage is an inconvenience rather than a lost day.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['ISP escalation handled', '4G/5G failover', 'Line testing with evidence', 'Same-day where available'],
    "crumbs": [('Services', '/services'), ('Business NBN & Internet', '/nbn-internet-support-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT diagnoses and resolves NBN and business internet problems across the Gold Coast — modem and router configuration, line testing, escalation to the internet provider with documented evidence, and 4G or 5G failover so an outage does not stop the business trading. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Saturated WiFi',
                                         None,
                                         'One access point serving too many devices. Feels exactly like '
                                         'slow internet and is completely unrelated to your connection.'),
                                 (       'A failing cable or port',
                                         None,
                                         'Intermittent faults that appear random. Cheap to test and '
                                         'frequently the answer.'),
                                 (       'Something flooding the connection',
                                         None,
                                         'A backup running in business hours, a device misbehaving, a '
                                         'large upload nobody mentioned. Traffic analysis finds it.'),
                                 (       'The router is underpowered',
                                         None,
                                         'Provider-supplied routers are built to a price. Once you have '
                                         'VoIP, a VPN and thirty devices, they become the bottleneck.'),
                                 (       'A genuine line fault',
                                         None,
                                         'Sometimes it really is the service. Then the job becomes '
                                         'gathering evidence the provider cannot dismiss.'),
                                 (       'The plan no longer fits',
                                         None,
                                         "Business has grown, the connection hasn't. Worth checking, but "
                                         'worth checking last rather than first.')],
                'cols': 3,
                'eyebrow': 'First question',
                'h2': 'Is it actually the internet?',
                'sub': "Most of the time it isn't, and upgrading the plan won't fix it."},
        {       'h2': 'Dealing with the provider',
                'html': '<p style="max-width:68ch">This is where most of the frustration lives. Faults get '
                        'closed as "no fault found", the next call starts from scratch, and nobody at the '
                        'business has the technical evidence to push back.</p><p '
                        'style="max-width:68ch;margin-top:16px">We run line tests, capture logs and '
                        'document what is actually happening, then handle the escalation on your behalf. '
                        'Providers respond very differently to a documented fault than to a frustrated '
                        'customer, and you get your time back.</p>'},
        {       'h2': 'Failover — the thing worth doing before you need it',
                'ticks': [       '<strong>4G or 5G backup</strong> that takes over automatically when the '
                                 'primary connection drops',
                                 '<strong>Phones keep working</strong> — critical if you are on VoIP, '
                                 'where an internet outage otherwise takes your phones with it',
                                 '<strong>EFTPOS keeps working</strong>, which for retail and hospitality '
                                 'is the difference between trading and closing',
                                 '<strong>Automatic, not manual</strong> — nobody should be plugging in a '
                                 'hotspot while customers wait',
                                 '<strong>Tested</strong>, so you know it actually cuts over rather than '
                                 'assuming it will']}])
            + faq_block(FAQS)
            + related([       ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Router & Modem Configuration', '/router-and-modem-configuration-gold-coast'),
        ('Business NBN guide', '/business-nbn-guide-gold-coast')])
            + cta('Internet problems nobody can resolve?', "We'll measure it, document it, and take the provider on for you — with evidence they can't close the ticket on."),
}

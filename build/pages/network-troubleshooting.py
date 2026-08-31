from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Why is our office internet so slow?',
        'In most Gold Coast offices the connection is not the bottleneck — saturated WiFi, channel interference, a failing cable or switch port, or a device flooding the network usually is. bcom ICT '
        'measures the physical layer, the wireless environment and the traffic before recommending anything, so you are not upgrading a service that was never the problem.'),
    (   'Devices keep dropping off the WiFi. What causes that?',
        'Usually coverage gaps where a device clings to a distant access point rather than switching, channel interference from neighbouring buildings, or too many devices on one access point. All '
        'three are measurable. Adding a consumer range extender generally makes roaming worse rather than better.'),
    (   'Can you deal with our internet provider for us?',
        "Yes, and it is often the most useful part of the job. We run line tests and gather logs so the fault is documented, then handle the escalation. Providers close tickets as 'no fault found' "
        'far less readily when presented with evidence.'),
    (   'How long does a network diagnosis take?',
        'Most faults are identified within a single on-site visit. Intermittent ones that only occur at certain times can need monitoring left in place for a few days, which we will tell you up '
        'front rather than billing repeat visits.'),
    ('What does it cost?', '$198 + GST per hour ($217.80 inc GST) plus a $100 + GST call-out for on-site attendance. We scope roughly how long we expect it to take before starting.'),
    (   'Will you tell us if the fix is expensive?',
        'Yes, and we will tell you if it is not needed. Sometimes the answer is a channel change and a cable replacement rather than the new equipment someone else quoted.')]

PAGE = {
    "path": '/network-troubleshooting-diagnostics-gold-coast',
    "priority": '0.75',
    "service": 'Network Troubleshooting & Diagnostics Gold Coast',
    "title": 'Business Network Troubleshooting Gold Coast | bcom ICT',
    "description": "Slow network, dropouts or devices that won't connect? bcom ICT diagnoses and fixes business network faults across the Gold Coast — interference, congestion, cabling, switching and ISP problems.",
    "hero_img": 'hero-bg-network-troubleshooting.webp',
    "hero_alt": 'A bcom ICT technician diagnosing a business network fault on the Gold Coast',
    "h1": "Find out what's actually causing it",
    "lede": '"The internet is slow" is a symptom with a dozen possible causes. We test rather than guess, and tell you which one it is.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Tested, not guessed', 'Same-day where available', 'Written findings', 'ISP escalation handled'],
    "crumbs": [('Services', '/services'), ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT diagnoses and resolves business network faults across the Gold Coast — slow speeds, dropouts, devices that will not connect, WiFi dead zones, cabling faults, switch and router problems, and internet service faults requiring escalation to the provider. Findings are tested and reported rather than guessed. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Saturated WiFi, not slow internet',
                                         None,
                                         'One access point serving forty devices behaves nothing like one '
                                         'serving five. Most slow-internet complaints in offices are '
                                         'wireless congestion, and no amount of upgrading the NBN plan '
                                         'will fix it.'),
                                 (       'Interference and channel overlap',
                                         None,
                                         "On the Gold Coast, dense buildings mean your neighbours' "
                                         'networks are competing with yours. Channel planning is '
                                         'measurable and fixable; guessing at it is not.'),
                                 (       'A failing cable or port',
                                         None,
                                         'Intermittent faults that appear random are frequently one '
                                         'marginal cable run or a dying switch port. They look like '
                                         'everything except cabling, which is where troubleshooting time '
                                         'disappears.'),
                                 (       'Something is flooding the network',
                                         None,
                                         'A misconfigured device, a backup job running in business hours, '
                                         'or a loop between two switches. Traffic analysis finds it; '
                                         'restarting things does not.'),
                                 (       'The connection genuinely is faulty',
                                         None,
                                         'Sometimes it is the service. Then the job becomes evidence — '
                                         'line testing and logs so the provider cannot simply close the '
                                         'ticket.'),
                                 (       "Nobody knows what's connected",
                                         None,
                                         "Old devices, personal phones, a contractor's laptop, a smart TV "
                                         'somebody plugged in. You cannot troubleshoot a network you '
                                         'cannot see.')],
                'cols': 2,
                'eyebrow': 'Symptoms and causes',
                'h2': '"The internet is slow" is rarely the internet',
                'icon': False,
                'sub': 'The complaint is almost always the same. The cause almost never is.'},
        {       'cols': 4,
                'eyebrow': 'How we diagnose',
                'h2': 'Measure first',
                'steps': [       (       'Reproduce and scope it',
                                         'When it happens, to whom, on what, and whether it correlates '
                                         'with anything — time of day, a particular room, a particular '
                                         'application.'),
                                 (       'Test the physical layer',
                                         'Cable runs, switch ports, link speeds and errors. Cheap to check '
                                         'and frequently where the answer is.'),
                                 (       'Survey the wireless',
                                         'Signal, channel usage, interference and client density measured '
                                         'across the site rather than estimated.'),
                                 (       'Analyse the traffic',
                                         'What is actually using the connection, and whether the '
                                         'bottleneck is inside the building or outside it.')]},
        {       'h2': 'You get the findings in writing',
                'html': '<p style="max-width:68ch">A diagnosis you cannot check is not much use, '
                        'particularly when the answer is that you need to spend money. You get what we '
                        'measured, what it showed, and what we recommend — including when the '
                        'recommendation is to change nothing.</p><p '
                        'style="max-width:68ch;margin-top:16px">Where the fault is with your internet '
                        'provider, that written evidence is what stops the ticket being closed as "no '
                        'fault found". We handle the escalation — see <a '
                        'href="/nbn-internet-support-gold-coast">business NBN and internet '
                        'support</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Business NBN & Internet Support', '/nbn-internet-support-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business IT Support', '/it-support-and-services-gold-coast')])
            + cta("Something on the network isn't right?", "We'll measure it rather than guess, and you'll get the findings in writing — including when the answer is to change nothing."),
}

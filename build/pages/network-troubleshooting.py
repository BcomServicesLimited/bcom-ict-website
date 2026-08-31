from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;It&rsquo;s just slow&rdquo;",
     "almost anything, which is why it is the hardest report to act on. Slow can mean the internet, the server, one application, the wireless, or a single failing device flooding the network.",
     "Establish what is slow, for whom, and when, before changing anything. Half of network troubleshooting is converting a feeling into a measurement, and the measurement usually names the culprit without further argument."),
    ("&ldquo;It only happens to one person&rdquo;",
     "the device, its position, or its habits &mdash; not the network. One machine on an old wireless standard, one desk at the edge of coverage, one person who leaves forty browser tabs open.",
     "Swap the variable rather than debating it. Move the person, or move the machine, and the fault either follows or it does not. That single test eliminates most of the possibilities in about five minutes."),
    ("&ldquo;It happens every morning at nine&rdquo;",
     "everyone arriving at once. Forty devices reconnecting, syncing mail and pulling updates in the same ten minutes is a genuine load spike, not a fault.",
     "Measure the peak and decide whether it needs capacity or scheduling. Moving updates off the morning window is free; adding bandwidth is not, and often is not what the problem needed."),
    ("&ldquo;It fixed itself&rdquo;",
     "nothing. Intermittent faults do not heal &mdash; they go quiet. Something that resolves without intervention will return, usually with worse timing.",
     "Log continuously rather than investigating only while it is broken. Catching the fault in the act is the whole job, and it cannot be done during a visit booked for the following Tuesday."),
    ("&ldquo;The provider says there&rsquo;s no fault&rdquo;",
     "a provider testing to the network boundary and finding it healthy. That test is often accurate and still irrelevant, because the fault is intermittent and their test is not.",
     "Build an evidence pack &mdash; timestamps, line statistics, packet loss over days rather than minutes. Providers respond to data. A support call describing frustration goes to the same queue every time."),
    ("&ldquo;It started after the power went out&rdquo;",
     "hardware that did not survive the event, or that came back in the wrong order. Switches, routers and access points are all vulnerable to surges, and a device can be damaged without dying.",
     "Check whether everything actually came back, in the right sequence, and whether anything is now running degraded. Partial failures after an outage are common and much harder to spot than total ones."),
]

EXAMPLE_1 = example(
    "Eighteen months, three providers, one failing injector",
    "A Gold Coast business had changed internet providers twice in eighteen months chasing intermittent dropouts. Each new provider tested the line, declared it healthy, and each was right. The dropouts continued regardless.",
    "Continuous monitoring over eleven days showed the outages had nothing to do with the internet connection at all. A power-over-Ethernet injector feeding a wireless bridge was failing under thermal load, dropping the link for between forty seconds and four minutes whenever the plant room warmed up. No provider test would ever have found it, because no provider test looked at that device.",
    "Replaced the injector, then relocated it out of the plant room so the same failure mode could not recur.",
    "The dropouts stopped. The business had spent eighteen months and two contract changes on a fault that a $90 part was causing &mdash; and would have kept changing providers, because every provider they tried was telling them the truth.")

EXAMPLE_2 = example(
    "The 2pm dropout that was doing exactly what it was told",
    "A real estate agency reported that their internet became unusable at two o&rsquo;clock every weekday afternoon and recovered by about half past three. It had been going on for months and had already survived a modem replacement.",
    "A cloud backup had been configured years earlier by a previous provider to run at 2pm on weekdays &mdash; presumably intended as a quiet period at the time. It was consuming the entire upload capacity for ninety minutes, which starved every phone call, video meeting and cloud application in the office.",
    "Moved the backup to overnight, applied traffic shaping so it could never again take the whole connection, and confirmed the backup was still completing and still restorable.",
    "The afternoon dropouts ended that week at no cost. The backup was not the problem &mdash; the schedule was, and nobody had revisited it since the day it was set.")

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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The faults that are never what they look like</h2>
      <p>Network troubleshooting is mostly the business of disproving the obvious explanation.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a proper diagnosis looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Business NBN & Internet Support', '/nbn-internet-support-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business IT Support', '/it-support-and-services-gold-coast')])
            + cta("Something on the network isn't right?", "We'll measure it rather than guess, and you'll get the findings in writing — including when the answer is to change nothing."),
}

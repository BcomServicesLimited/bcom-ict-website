from layout import MARK, cta, faq_block, cards, ticks, steps, related, svc_body, trust_note, issues, example

COMMON_ISSUES = [
    ("&ldquo;Can you see everything on my screen?&rdquo;",
     "a reasonable question that deserves a plain answer. During a session a technician sees what is on the screen, which is why the session is started by you and ended by you.",
     "Close what you would rather not have seen before starting, and end the session when the work is done. You watch the whole thing, and you can stop it at any point without asking."),
    ("&ldquo;The internet is down, so remote won&rsquo;t work&rdquo;",
     "correct, and it is the one fault remote support cannot address by definition.",
     "That is what an on-site visit is for. We will tell you straight away when a fault needs someone there rather than billing you for an hour of trying to work around it."),
    ("&ldquo;It only happens sometimes and never while you&rsquo;re watching&rdquo;",
     "an intermittent fault. A booked session catches it only by luck, and the luck rarely arrives.",
     "Put monitoring in place and investigate from the evidence rather than the appointment. Intermittent faults are solved by logging, not by attending more often."),
    ("&ldquo;We&rsquo;re not on the Gold Coast&rdquo;",
     "not an obstacle. Remote support does not care where the machine is, and a great deal of our work is for businesses and staff elsewhere in Australia.",
     "Distance is irrelevant to remote work and decisive for on-site work. Where a fault genuinely needs hands on hardware outside our area, we will say so rather than pretend otherwise."),
    ("&ldquo;Our staff work from home and it&rsquo;s always their own setup&rdquo;",
     "often true, and frequently used to dismiss a genuine problem. A home connection that struggles with video calls is a real business issue regardless of who owns the equipment.",
     "Establish whether the fault is the machine, the home network or the connection. Knowing which is what turns an ongoing complaint into something someone can act on."),
    ("&ldquo;Will you need our password?&rdquo;",
     "usually not, and where elevated access is genuinely required it is requested explicitly rather than assumed.",
     "You approve the session and you can watch every action. If something needs a credential you hold, you enter it &mdash; we would rather ask than have a shared password sitting somewhere afterwards."),
]

EXAMPLE_1 = example(
    "The fault that never happened during an appointment",
    "A business had a machine that would freeze for a minute or two at unpredictable intervals, several times a week. Three separate remote sessions had been booked, and on each occasion the machine behaved perfectly.",
    "Booked sessions were the wrong tool. Monitoring left running for nine days caught the freeze eleven times and showed a consistent pattern: each one coincided with a backup agent scanning a mapped network drive that had become unreachable, causing the machine to wait on it. The drive pointed at a server decommissioned during an office move a year earlier.",
    "Removed the stale mapping and corrected the backup agent&rsquo;s configuration, then left monitoring running for a further fortnight to confirm the freezes had genuinely stopped rather than gone quiet.",
    "No further freezes. Three attended sessions had found nothing because the fault was never going to appear on demand &mdash; it needed evidence gathered over days rather than a person watching for an hour.")

EXAMPLE_2 = example(
    "Telling a client the problem was not their laptop",
    "A business had a staff member working from home whose video calls broke up constantly. The assumption within the business was that the laptop was underpowered, and a replacement had been approved.",
    "The laptop was performing well and was not short of anything. Measuring the home connection over several days showed adequate speed and substantial latency variation during the afternoon &mdash; enough to make a call unusable while leaving everything else feeling normal. The household was on a residential plan sharing capacity with a neighbourhood that came home at three.",
    "Reported that the laptop was not the problem, recommended against replacing it, and set out the two things that would actually help: a wired connection to the router rather than wireless, and a conversation with the provider about the service.",
    "Calls improved immediately with the cable alone. A laptop was not purchased. Replacing it would have cost the business a machine and changed nothing, which is what tends to happen when the wrong component is blamed for a network fault.")

PAGE = {
    "path": '/remote-it-support-gold-coast',
    "priority": "0.8",
    "service": 'Remote IT Support Gold Coast',
    "title": 'Remote IT Support Gold Coast & Australia-Wide | bcom ICT',
    "description": 'Remote IT support for Gold Coast businesses and distributed teams Australia-wide. Secure screen-share diagnosis, usually same day, at $190 + GST per hour with no call-out. Call 07 3041 8993.',
    "hero_img": 'hero-bg-remote-it-support.webp',
    "hero_alt": 'A bcom ICT technician providing remote IT support to a business client',
    "h1": 'Remote IT support, usually the same day',
    "lede": "Most business IT faults never need anyone on site. A secure screen share often has you working again in minutes — and there's no call-out on it.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['$190 + GST/hr, no call-out', 'Usually same day', 'Australia-wide', 'You approve every session'],
    "crumbs": [('Services', '/services'), ('Remote IT Support', '/remote-it-support-gold-coast')],
    "faqs": [('Can IT support be done remotely?', 'Most business IT faults can. bcom ICT resolves the majority of support requests by secure screen share without a site visit — email and Microsoft 365 problems, software faults, account and access issues, performance problems and most printer faults. Hardware failures and network outages need someone on site. A remote job of up to an hour is $150 + GST ($165 inc GST) with no call-out.'), ('Is remote support secure?', "Yes, and you control it. We send a one-time link, you approve the connection before anyone can see your screen, you watch the entire session, and you can disconnect at any moment. Nothing stays installed afterwards unless you're a managed client with monitoring agreed separately in writing."), ('How much does remote IT support cost?', "$190 + GST per hour ($209.00 inc GST), billed in half-hour increments after the first hour, with no call-out fee. That's the main reason we try remote first — an on-site visit adds a $39 + GST call-out before anyone has looked at the problem."), ('Do you support staff working from home?', "Yes, and it's routine. A remote worker gets the same support as someone in the office. If your team is spread across several sites or states, remote support is how that works in practice."), ("What if it turns out you can't fix it remotely?", "We'll tell you, and book an on-site visit — same day where we can. We don't bill you for an hour of trying before admitting a drive has failed."), ('Do we need to be an existing client?', 'No. We take support calls from any business. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time.')],
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides remote IT support to Gold Coast businesses and distributed teams anywhere in Australia. A technician connects by secure screen share with your permission, diagnoses the fault and usually resolves it the same day. Remote support is charged at $190 + GST per hour with no call-out fee. Call 07 3041 8993.', blocks=[{'eyebrow': 'What we fix remotely', 'h2': "Most faults don't need anyone on site", 'sub': 'Roughly three quarters of what businesses call us about can be resolved without a visit.', 'cols': 3, 'cards': [('Email and Microsoft 365', None, 'Mail not sending, accounts locked out, mailboxes full, shared calendars misbehaving, Teams and SharePoint permissions.'), ('Software and applications', None, "Programs that won't open, crash, or stopped working after an update. Licensing and activation problems."), ('Slow or misbehaving machines', None, 'Performance problems, startup issues, failed updates and the mysterious slowdowns nobody can explain.'), ('Account and access issues', None, 'Password resets, MFA problems, permissions, and getting a new starter into the systems they need.'), ('Printers and shared devices', None, 'Network printers and scanners that stop working for one person or everyone. Usually fixable remotely.'), ('Security concerns', None, "Suspicious emails, accounts you think have been accessed. Call rather than email if you think you've been breached.")]}, {'eyebrow': 'How it works', 'h2': 'You stay in control of the session', 'cols': 4, 'steps': [('You call or email', "Call 07 3041 8993 or email support@bcomservices.com. Tell us what's happening and who's affected."), ('We send a one-time link', "Nothing installs permanently. You open the link when you're ready."), ('You approve the connection', 'Nobody sees anything until you say so. You watch the entire session on your own screen.'), ('It ends when you close it', "Access stops with the session. Nothing remains unless you're a managed client with monitoring agreed separately.")]}, {'h2': 'Why remote first', 'ticks': ["<strong>It's faster.</strong> Minutes rather than the hours it takes to get someone into a car and across the Gold Coast.", "<strong>It's cheaper.</strong> $190 + GST per hour with no call-out, against $252 inc GST for a first hour on site.", '<strong>It works anywhere.</strong> Staff at home, on a second site, or interstate get the same support as someone in the office.', "<strong>We'll tell you when it won't work.</strong> Dead hardware, a failed drive or a network that's genuinely down needs hands on it, and we book a visit instead of billing you to try."]}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The questions we are actually asked about remote support</h2>
      <p>Six things worth answering plainly, including the two we would rather you asked before the first session.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What remote support actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block([('Can IT support be done remotely?', 'Most business IT faults can. bcom ICT resolves the majority of support requests by secure screen share without a site visit — email and Microsoft 365 problems, software faults, account and access issues, performance problems and most printer faults. Hardware failures and network outages need someone on site. A remote job of up to an hour is $150 + GST ($165 inc GST) with no call-out.'), ('Is remote support secure?', "Yes, and you control it. We send a one-time link, you approve the connection before anyone can see your screen, you watch the entire session, and you can disconnect at any moment. Nothing stays installed afterwards unless you're a managed client with monitoring agreed separately in writing."), ('How much does remote IT support cost?', "$190 + GST per hour ($209.00 inc GST), billed in half-hour increments after the first hour, with no call-out fee. That's the main reason we try remote first — an on-site visit adds a $39 + GST call-out before anyone has looked at the problem."), ('Do you support staff working from home?', "Yes, and it's routine. A remote worker gets the same support as someone in the office. If your team is spread across several sites or states, remote support is how that works in practice."), ("What if it turns out you can't fix it remotely?", "We'll tell you, and book an on-site visit — same day where we can. We don't bill you for an hour of trying before admitting a drive has failed."), ('Do we need to be an existing client?', 'No. We take support calls from any business. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time.')])
            + related([('Business IT Support', '/it-support-and-services-gold-coast'), ('On-site IT Support', '/on-site-technical-support-gold-coast'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'), ('Support', '/support'), ('Pricing', '/pricing'), ('Published service levels', '/service-levels-and-security')])
            + cta('Need help right now?', "Call 07 3041 8993 and we'll often have you working again before a technician could reach the car park."),
}

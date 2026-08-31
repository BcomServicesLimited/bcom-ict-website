from layout import cta, faq_block, related, svc_body, price_table, issues, example

COMMON_ISSUES = [
    ("&ldquo;The port in the meeting room doesn&rsquo;t work&rdquo;",
     "the outlet was run but never terminated at the cabinet end, or it was terminated and never patched into a switch. Extremely common in fit-outs where the cabling and the network were done by different trades.",
     "Trace the run, terminate or patch it, and test it. Then record it on a port schedule so the next person does not have to repeat the exercise."),
    ("&ldquo;It works if you wiggle the cable&rdquo;",
     "a poor termination at one end &mdash; usually a wall plate that was punched down in a hurry, or a plug crimped on site rather than a proper outlet.",
     "Re-terminate and certify. A connection that works intermittently is not a connection that mostly works; it is one that will fail at the least convenient moment and be blamed on the computer."),
    ("&ldquo;We&rsquo;ve run out of ports&rdquo;",
     "growth. The cabinet was specified for the headcount at fit-out and the business added people, printers, access points and cameras to it since.",
     "Count what is actually connected and what is coming, then add capacity once with room to spare. Daisy-chaining a desk switch onto a full patch panel works until it very publicly does not."),
    ("&ldquo;None of the outlets are labelled&rdquo;",
     "cabling installed without a port schedule, or one that was made and then lost. The information existed for about a week.",
     "Tone out every run, label both ends, and hand over a written schedule. It takes a day and saves that day back on the first fault after it."),
    ("&ldquo;The new phones won&rsquo;t power on&rdquo;",
     "the switch has run out of PoE budget. Each port can supply power, but the switch as a whole has a total wattage limit that new access points and handsets quietly consume.",
     "Add up what the switch is actually being asked to power rather than assuming per-port capacity is the constraint. Sometimes the answer is a bigger power supply; sometimes it is moving two devices to a different switch."),
    ("&ldquo;The builder&rsquo;s electrician did the data cabling&rdquo;",
     "data cabling treated as electrical work. The cable is often correct and the termination often is not, because terminating structured cabling to specification is a different trade with different test equipment.",
     "Certify it before you rely on it. Testing eleven outlets costs very little at fit-out and a great deal once the ceiling is closed and the tenancy is occupied."),
]

EXAMPLE_1 = example(
    "Cat6 cable, Cat5e termination, nobody tested it",
    "A medical practice completed a fit-out and moved in. Within a fortnight, two consulting rooms were dropping their connection several times a day. The builder had included data cabling in the works and the invoice described it as Cat6.",
    "The cable was genuinely Cat6. Both ends had been terminated to the older Cat5e pin specification, and nothing had ever been tested. Four of the eleven outlets failed certification outright. The two that were failing daily were simply the two being used hardest.",
    "Re-terminated every outlet correctly, certified all eleven, and provided the test results and a labelled port schedule. Two runs had been damaged during construction and were replaced.",
    "Eleven certified outlets with documented results, which is what the practice believed it had paid for. The certification report also settled the question of who was responsible for the rework.")

EXAMPLE_2 = example(
    "Testing the cabling before the move, not after",
    "A law firm was relocating to a floor the landlord described as already cabled with Cat6. Forty outlets, and a move scheduled over a single weekend with the firm expected to be working on Monday morning.",
    "Certification found a mix of Cat5e and Cat6 with no records distinguishing them, and nine runs that failed outright &mdash; two of them serving the room intended for the server cabinet. Had this been discovered on the Monday, the firm would have lost days rather than hours.",
    "Tested every outlet three weeks before the move, replaced the nine failures, and produced a port schedule the movers and the phone installer could both work from.",
    "The firm moved on the Saturday and worked on the Monday. The cost of testing forty outlets was a fraction of one day of a law firm not billing, which is the calculation that makes pre-move certification an easy decision.")

FAQS = [   (   'Who installs office data cabling on the Gold Coast?',
        'bcom ICT delivers Cat6 and Cat6A structured cabling for Gold Coast offices, including patch panels, comms racks, cable management, testing and certification. The cabling itself is carried '
        'out by ACMA registered cabling contractors that bcom ICT engages and manages, because fixed cabling is a licensed trade in Australia and bcom ICT does not hold cabler registration itself. Call 07 3041 8993.'),
    (   'Should we use Cat6 or Cat6A?',
        'Cat6 handles gigabit comfortably and 10-gigabit over shorter runs, and suits most small offices. Cat6A is the safer choice for longer runs, for buildings you expect to be in for a decade, '
        "and where high-density WiFi or 10-gigabit switching is likely. We'll explain the difference for your building rather than defaulting to one."),
    (   'Do you need to be licensed to install network cabling in Australia?',
        'Yes. Fixed cabling connected to the telecommunications network requires ACMA cabler registration. bcom ICT engages registered cabling contractors for that work rather than doing it with '
        'internal staff, and provides the testing and certification documentation on completion.'),
    (   'Can you work around our trading hours?',
        "Yes. Cabling in an occupied office is usually staged after hours or over a weekend. Ceiling and wall work is disruptive and noisy, and it's rarely worth doing while people are trying to "
        'work.'),
    (   "What's the difference between data cabling and phone cabling?",
        'Increasingly very little — most modern phone systems run over the same structured cabling as your computers. Older PBX systems may still use separate voice cabling, which we also install. '
        "If you're replacing a phone system, one structured cabling installation usually serves both."),
    ('Will you label it?', 'Yes, at both ends, matched to a floor plan you keep. It is the cheapest thing in the entire installation and the one that saves the most time later.')]

PRICING = [
    ('Small office fit-out', 'from around $1,200', '+ GST &middot; indicative only',
     [
      'Around eight Cat6 outlets, terminated to a patch panel',
      'Every run tested and certified, results handed to you',
      'Labelled at both ends and recorded on a port schedule',
      'Assumes standard commercial ceiling and cavity access',
     ]),
]

PAGE = {
    "path": '/network-cabling-for-offices-gold-coast',
    "priority": '0.75',
    "service": 'Office Network Cabling Gold Coast',
    "also_service": ["Data Cabling Gold Coast"],
    "title": 'Office Network & Data Cabling Gold Coast — Cat6 & Cat6A | bcom ICT',
    "description": 'Cat6 and Cat6A structured cabling for Gold Coast offices — patch panels, comms racks and cable management, installed by ACMA registered cabling contractors with testing and certification.',
    "hero_img": 'data-cabling-hero.webp',
    "hero_alt": 'Cat6 structured cabling and patch panel installed in a Gold Coast commercial premises',
    "h1": 'Cabling done once, properly, and documented',
    "lede": 'Cat6 and Cat6A structured cabling for Gold Coast offices — installed by registered cablers, tested, certified and labelled so the next person can follow it.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Cat6 & Cat6A', 'ACMA registered cablers', 'Tested & certified', 'Labelled and documented'],
    "crumbs": [('Services', '/services'), ('Office Network Cabling', '/network-cabling-for-offices-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT delivers Cat6 and Cat6A structured cabling for Gold Coast offices and commercial premises — patch panels, comms racks, cable management, testing and certification documentation. Fixed cabling is a licensed trade in Australia, so the cabling itself is carried out by ACMA registered cabling contractors that bcom ICT engages and manages. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Nothing is labelled',
                                         None,
                                         'An unlabelled patch panel turns a five-minute fault into a '
                                         'two-hour trace. Labelling costs nothing at installation and '
                                         'saves hours forever after.'),
                                 (       'The wrong cable was used',
                                         None,
                                         "Cat5e still works until it doesn't — until you install PoE "
                                         'access points, or move to faster switching, and discover the run '
                                         'is the bottleneck.'),
                                 (       'Runs are too long',
                                         None,
                                         'Ethernet has distance limits. Exceeding them produces '
                                         'intermittent faults that look like everything except cabling, '
                                         'which is where troubleshooting time goes to die.'),
                                 (       'No testing certificate',
                                         None,
                                         'Without one you have no evidence any run performs to spec. '
                                         'Reputable installers test and certify every run and hand you the '
                                         'results.'),
                                 (       'The comms room is chaos',
                                         None,
                                         'Cable management is not cosmetic. It determines whether a change '
                                         'takes ten minutes or a morning, and whether airflow keeps the '
                                         'equipment alive.'),
                                 (       "It wasn't done by a registered cabler",
                                         None,
                                         'Fixed cabling connected to the telecommunications network '
                                         'legally requires registration in Australia. Worth asking any '
                                         'installer to show you before work starts.')],
                'cols': 3,
                'eyebrow': 'Why it matters',
                'h2': 'Bad cabling is expensive twice',
                'sub': "Once when it's installed, and again every time someone has to troubleshoot it."},
        {       'h2': 'What an installation includes',
                'ticks': [       'Site survey — where the comms room goes, where the points are needed, '
                                 'what routes exist and what the building will allow',
                                 'Cat6 or Cat6A runs, terminated to standard, with the choice explained '
                                 'rather than defaulted',
                                 'Patch panels, comms rack, and cable management that a future technician '
                                 'can work in',
                                 'Every run tested and certified, with the documentation handed to you',
                                 'Labelling at both ends, matched to a floor plan you keep',
                                 'Power over Ethernet capacity considered up front, for access points, '
                                 'cameras and phones']},
        {       'h2': 'Who does the work',
                'html': '<p style="max-width:68ch">Fixed cabling connected to the telecommunications '
                        'network legally requires a registered cabler in Australia. <strong>bcom ICT does '
                        'not hold that registration.</strong> The cabling portion is carried out by ACMA '
                        'registered cabling contractors that we engage and manage.</p><p '
                        'style="max-width:68ch;margin-top:16px">In practice that means you deal with one '
                        'point of contact for the whole job — design, cabling, switching, WiFi and '
                        'handover — rather than coordinating three trades yourself. You still get the '
                        'testing and certification documentation on completion, and we would encourage you '
                        'to ask any installer for it.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>How much does office data cabling cost?</h2>
      <p>An indicative figure for a described job, quoted properly after a look at the building rather than over the phone.</p>
    </div>
    {price_table(PRICING, note='This is an indicative planning figure for the job described above &mdash; not a quote, and not a per-outlet rate to multiply by your own outlet count. Sitting outside it: the cabinet, patch panel and switch, which are quoted on what the site actually needs; long runs; hard ceilings and heritage buildings; asbestos; and after-hours access where a landlord or a tenanted building requires it. Cabling is quoted after someone has looked at the building, because a number given over the phone is a number that moves once an installer is on a ladder. All cabling work is carried out by ACMA registered cabling contractors.')}
  </div>
</section>
'''
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What we find in ceilings</h2>
      <p>Cabling faults are unglamorous and account for a remarkable share of problems blamed on computers.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What proper cabling work looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast')])
            + cta('Fitting out or moving in?', "We'll survey the building and quote on what it actually needs — including telling you when the existing cabling is fine."),
}

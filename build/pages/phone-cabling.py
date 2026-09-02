from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;The phone point in the new office is dead&rdquo;",
     "an outlet that was never connected back to anything, or one that was connected to a service disconnected when the previous tenant left.",
     "Trace the point back to the building distributor and establish what it is actually joined to. Tenancy phone points are frequently orphaned between tenants and look identical to working ones."),
    ("&ldquo;The lift phone stopped working&rdquo;",
     "a line disconnected during an NBN migration. Lift phones, fire panels and alarm diallers often sat on old copper services that were cancelled without anyone realising what they carried.",
     "Identify every service in the building and what depends on it before anything is switched. Emergency lines are a compliance obligation, and finding out they are dead during an incident is the worst possible way to find out."),
    ("&ldquo;The EFTPOS line died after the NBN switch&rdquo;",
     "the same cause. Terminals, fax machines and monitored alarms that ran happily on a copper line do not necessarily survive the move to an internet-delivered service.",
     "Establish what each device needs before the switch, not after. Some can move to the new service, some need a different approach, and some need to be replaced &mdash; but all of that is cheaper to discover in advance."),
    ("&ldquo;The comms cupboard is a rat&rsquo;s nest&rdquo;",
     "twenty years of additions by different trades, none of whom removed anything. It usually still works, right up until someone needs to change one thing.",
     "Trace, label and rationalise, removing what is genuinely dead. The goal is not tidiness for its own sake &mdash; it is that the next change takes an hour instead of a day."),
    ("&ldquo;We&rsquo;re moving and need the phones live on day one&rdquo;",
     "not a fault, but the most common reason we are called, and the one with the least room to run late.",
     "Get the cabling and the services in place before the move rather than during it, and test them while the old site is still running. Phones are the part of a relocation most often left to last and least able to absorb a delay."),
    ("&ldquo;Who is even allowed to touch this?&rdquo;",
     "a fair question. Cabling connected to the telecommunications network must be installed by a registered cabler, and that is a legal requirement rather than a preference.",
     "bcom ICT engages ACMA registered cabling contractors for this work rather than doing it with internal staff. You get the compliance and the paperwork that goes with it, which matters for insurance and for a building certifier."),
]

EXAMPLE_1 = example(
    "The lift phone nobody knew had been disconnected",
    "A retail tenancy in a two-storey building had migrated its phones to NBN eighteen months earlier. The changeover went smoothly and nothing appeared to have been missed.",
    "A routine review of the building&rsquo;s services found the lift emergency phone had been running on a copper line cancelled as part of that migration. It had been dead for eighteen months. Nobody had tested it, because nobody knew it was there &mdash; it appeared on no inventory and belonged to no obvious owner.",
    "Restored an emergency service to the lift through an ACMA registered cabling contractor, tested it under the building&rsquo;s own procedure, and produced an inventory of every service in the building and what depended on it.",
    "The lift phone works and the building has a record of what its services actually carry. The uncomfortable part is that this is not unusual &mdash; it is one of the first things we check after any NBN migration, precisely because it is so often missed.")

EXAMPLE_2 = example(
    "Phones working on Monday because the cabling was done in advance",
    "A medical centre was relocating to a larger premises with a fixed opening date and appointments already booked into the first week. Reception needed six extensions, and the building had phone points of unknown vintage and unknown connection.",
    "None of the existing points terminated anywhere useful. The building distributor had been repeatedly modified by previous tenants, and tracing what connected to what took longer than running new cable would have.",
    "Ran new structured cabling to every position through an ACMA registered contractor three weeks before the move, terminated it into a proper cabinet, certified it, and pre-configured and tested the handsets against the new cabling while the old site was still trading.",
    "The centre moved over a weekend and opened on the Monday with every extension working. The only thing that happened on moving day was that the handsets were carried in and plugged into outlets already proven to work.")

EXAMPLE_3 = example(
    "The alarm that had been reporting to nobody for two years",
    "A small manufacturer had a monitored back-to-base alarm covering a workshop full of tooling. The panel armed and disarmed normally, the keypad behaved, and the monitoring contract was paid every quarter without question.",
    "The alarm dialler had been reporting over a copper line disconnected during the site&rsquo;s NBN migration two years earlier. The panel had no way to tell anyone &mdash; it dialled out, failed, and cleared the fault silently. The monitoring centre had received nothing in that time and the business had assumed silence meant no incidents.",
    "Restored a reporting path for the panel using an ACMA registered cabling contractor, tested a signal end to end with the monitoring centre on the line, and checked every other device in the building that had depended on the old copper service.",
    "The alarm reports again and has been verified rather than assumed. The business had been paying a monitoring fee for two years for a service that could not physically have worked, which is worth checking after any migration.")

FAQS = [   (   'Who can install phone cabling in Australia?',
        'Fixed cabling connected to the telecommunications network legally requires ACMA cabler registration. bcom ICT does not hold that registration itself — the cabling portion of a job is '
        'carried out by ACMA registered cabling contractors that bcom ICT engages and manages, with testing and certification documentation provided on completion.'),
    (   'Do we need separate phone cabling, or can it share the data cabling?',
        'Most modern phone systems, including cloud VoIP and current on-premise PBX, run over the same structured data cabling as your computers. Separate voice cabling is generally only needed for '
        "older analogue or digital handsets. If you're fitting out, one structured cabling installation usually serves both and costs less than two jobs."),
    (   'Can you add points to our existing cabling?',
        'Yes — new desks, a reception move or a meeting room handset. New runs are terminated and tested to match the existing installation, and added to the documentation.'),
    (   'Will it disrupt our office?',
        'Cabling work in an occupied office is usually staged after hours or over a weekend. Ceiling and wall work is noisy and intrusive, and it is rarely worth doing while people are trying to '
        'take calls.'),
    (   'Do we get documentation?',
        'Yes. Testing and certification results, labelling at both ends, and a plan you keep. It is the cheapest part of the job and the part that saves the most time later.')]

PAGE = {
    "path": '/phone-line-installation-cabling-gold-coast',
    "priority": '0.75',
    "service": 'Phone Line Installation & Cabling Gold Coast',
    "title": "Phone Line & Voice Cabling Gold Coast | bcom ICT",
    "description": "Internal phone line and voice cabling for Gold Coast offices, installed by ACMA registered cabling contractors, tested and documented on handover.",
    "hero_img": 'phone-line-installation-hero.webp',
    "hero_alt": 'Phone line and voice cabling installed in a Gold Coast commercial premises',
    "h1": 'Phone and voice cabling, done to standard',
    "lede": 'Internal lines for offices and commercial premises — installed by registered cablers, tested, certified and documented on handover.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Australian standards', 'ACMA registered cablers', 'Tested & documented', 'One point of contact'],
    "crumbs": [('Services', '/services'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('Phone Line Cabling', '/phone-line-installation-cabling-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT installs internal phone line and voice cabling for Gold Coast offices and commercial premises. The cabling is carried out to Australian standards by ACMA registered cabling contractors that bcom ICT engages and manages, with testing and certification documentation provided on handover. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'New premises and fit-outs',
                                         None,
                                         'Voice and data cabling planned together at fit-out, which is far '
                                         'cheaper than adding points once the ceilings are closed and the '
                                         'office is occupied.'),
                                 (       'Additional points',
                                         None,
                                         'New desks, a reception move, a meeting room that needs a '
                                         'handset. Adding points to an existing installation, terminated '
                                         'and tested to match.'),
                                 (       'Relocations',
                                         None,
                                         'Moving a phone system to a new site, with cabling installed and '
                                         'tested ahead of the move rather than on the day. Part of an '
                                         'office IT relocation.'),
                                 (       'Legacy voice cabling',
                                         None,
                                         'Older PBX systems may still use separate voice cabling rather '
                                         'than sharing structured data cabling. We install and repair '
                                         'both.')],
                'cols': 2,
                'eyebrow': "What's involved",
                'h2': 'Voice cabling for commercial premises',
                'icon': False},
        {       'h2': 'Modern systems mostly share your data cabling',
                'html': '<p style="max-width:68ch">Worth knowing before you pay for two installations. '
                        'Most current phone systems — cloud VoIP and modern on-premise PBX alike — run '
                        'over the same Cat6 structured cabling as your computers, powered over Ethernet '
                        'from the switch. Separate voice cabling is generally only needed for older '
                        'analogue or digital PBX handsets.</p><p style="max-width:68ch;margin-top:16px">If '
                        'you are fitting out or replacing a phone system, one properly specified <a '
                        'href="/network-cabling-for-offices-gold-coast">structured cabling '
                        'installation</a> usually serves both, and it is cheaper than doing voice and data '
                        'as separate jobs. We will tell you which applies to your system rather than '
                        'quoting the larger option by default.</p>'},
        {       'h2': 'Who does the work',
                'ticks': [       'Fixed cabling connected to the telecommunications network legally '
                                 'requires ACMA cabler registration in Australia',
                                 '<strong>bcom ICT does not hold that registration</strong> — the cabling '
                                 'portion is carried out by ACMA registered cabling contractors we engage '
                                 'and manage',
                                 'You deal with one point of contact for the whole job rather than '
                                 'coordinating separate trades',
                                 'Testing and certification documentation is provided on completion — '
                                 'worth asking any installer for',
                                 'Runs are labelled at both ends and matched to a floor plan you keep']}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What we find behind the phone points</h2>
      <p>Phone cabling is where NBN migrations leave their casualties, and they tend to stay hidden until they matter.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What planning phone cabling properly looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Telecommunications Contractor', '/telecommunications-contractor-gold-coast')])
            + cta('Fitting out or adding points?', "We'll tell you whether you need voice cabling at all — for most modern systems, one structured installation covers both."),
}

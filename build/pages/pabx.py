from layout import cta, faq_block, related, svc_body, price_table, issues, example

COMMON_ISSUES = [
    ("&ldquo;Our installer has retired&rdquo;",
     "the single most common reason a business with a working PBX calls anyone. The system is fine and the knowledge has gone.",
     "Recover administrative access and document the configuration. A platform nobody can change is not a broken platform, and being told to replace it is not the same as needing to."),
    ("&ldquo;We can&rsquo;t change our own greeting&rdquo;",
     "a system handed over without its credentials or its documentation, which is how most of them were handed over.",
     "Make the change and then leave you able to make it yourself. If a business has to book a technician to alter an after-hours message, something has gone wrong that is not technical."),
    ("&ldquo;Half the phones went out after a power failure&rdquo;",
     "a card, a power supply or a component that did not survive the event. Older systems are more exposed to power disturbance than most equipment in a building.",
     "Identify precisely what failed and whether it can be replaced, then protect the system properly. A PBX on unconditioned power in a building with supply problems will keep doing this."),
    ("&ldquo;We want people working from home on the same number&rdquo;",
     "a requirement most legacy systems were never designed for. It does not automatically mean replacing everything.",
     "Consider a hybrid &mdash; the existing system for the office, cloud extensions for people outside it, joined so one number reaches whoever is available. Frequently a fraction of a full replacement."),
    ("&ldquo;We&rsquo;ve been told the system is end of life&rdquo;",
     "sometimes accurate and sometimes a sales position. What matters is whether parts are obtainable, whether it does what the business needs, and what the alternative costs.",
     "Get an honest assessment with both paths costed. We supply new systems and we support old ones, so we have no structural reason to prefer either answer."),
    ("&ldquo;We&rsquo;re moving premises and want to keep the system&rdquo;",
     "usually possible and usually underestimated. The system moving is the easy part; the services and the cabling at the new site are not.",
     "Plan the numbers, the services and the cabling well before the move rather than during it. Phones are the part of a relocation most often left to last and least able to absorb a delay."),
]

EXAMPLE_1 = example(
    "Keeping the office system and adding the people who were not in it",
    "A business with a healthy PBX needed six staff working from home to be reachable on the main number. Two providers had quoted for full cloud replacements, and the directors could not see why a working system had to be discarded.",
    "The existing platform suited the sixteen people in the building and was not designed to extend beyond it. Replacing it entirely would have solved a problem affecting six people by discarding equipment serving sixteen, which nobody had questioned because nobody had proposed anything else.",
    "Kept the PBX for the office, added cloud extensions for the six remote staff, and joined the two so a single published number rings whoever is available regardless of location.",
    "Everyone has a working phone and the business spent a small fraction of a replacement. The PBX will be replaced when it genuinely reaches its end, which is a decision the business now gets to make on its own timing.")

EXAMPLE_2 = example(
    "Moving a phone system without losing a day",
    "A business relocating within the Gold Coast wanted to take its phone system to the new premises and be operating from the first morning. The move was over a weekend.",
    "The system itself would move without difficulty. The new tenancy had phone points of unknown vintage connected to nothing identifiable, no structured cabling to the positions the business intended to use, and services that had to be arranged with lead times longer than the business had allowed.",
    "Ran cabling to every position through an ACMA registered contractor three weeks ahead, arranged the services with time to spare, and configured and tested the system against the new cabling while the old site was still trading.",
    "The business moved on the Saturday and worked on the Monday. On moving day the system was carried in and connected to outlets already proven to work, which is the whole point of doing the preparation early.")

FAQS = [   (   'Who services PBX phone systems on the Gold Coast?',
        'bcom ICT installs, programs and maintains on-premise PBX systems on the Gold Coast, including LG Ericsson iPECS, Panasonic KX-NS, KX-TDA and KX-TDE, NEC UNIVERGE SV9100, SV8100 and SL2100, '
        'and Alcatel-Lucent OmniPCX and OXO Connect — including legacy systems many providers no longer service. Call 07 3041 8993.'),
    (   'Our provider says we have to replace our system. Is that true?',
        'Sometimes, but frequently it reflects who is available rather than what the system needs. If the platform still does what your business requires and parts are obtainable, keeping it is '
        'often the cheaper answer. We will give you an honest assessment of remaining life before you commit to a replacement.'),
    (   'Can you just reprogram ours without taking over support?',
        'Yes. Plenty of clients call us for a one-off change — an extension, a call flow, an after-hours message — charged at the standard rate. There is no requirement to sign up to anything '
        'ongoing.'),
    (   'Can you still get parts for older systems?',
        'For the platforms listed above, usually yes. Where a part is genuinely unobtainable we will tell you, because that is the point at which replacement stops being optional and becomes a '
        'planning exercise.'),
    (   'Should we move to VoIP instead?',
        'Eventually most businesses will. Whether now is the right time depends on whether your hardware is failing, whether you need remote extensions, and whether your internet connection is '
        "reliable enough. We'll test the connection and give you a straight answer rather than a default one."),
    (   'Can you move our PBX to a new office?',
        'Yes. PBX relocation, recabling and number porting are handled as part of an office IT relocation, planned around your move date rather than attempted on the day.')]

PRICING = [
    ('Five-handset system', 'from around $2,250', '+ GST &middot; indicative only',
     [
      'Five business-grade handsets supplied, configured and installed',
      'Your existing numbers ported across',
      'Call flow, hunt groups and after-hours routing set up',
      'Staff shown how to actually use it',
      'Monthly service and call plan quoted alongside, not included',
     ]),
]

PAGE = {
    "path": '/pabx-phone-systems-gold-coast',
    "priority": '0.8',
    "service": 'PBX System Installation & Support Gold Coast',
    "title": 'PBX Phone Systems Gold Coast — Supply, Install & Support | bcom ICT',
    "description": 'On-premise PBX systems supplied, installed, programmed and supported on the Gold Coast — LG Ericsson iPECS, Panasonic KX, NEC UNIVERGE and Alcatel-Lucent OmniPCX. Legacy systems maintained. Call 07 3041 8993.',
    "hero_img": 'pabx-phone-systems-hero.webp',
    "hero_alt": 'An on-premise PBX phone system being programmed by bcom ICT on the Gold Coast',
    "h1": 'PBX systems supplied, installed and supported',
    "lede": 'New on-premise systems specified and installed, existing ones programmed and maintained — including the platforms most providers have walked away from.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['New systems supplied', '4 major brands', 'Programming & moves', 'Legacy still serviced'],
    "crumbs": [('Services', '/services'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('PBX Systems', '/pabx-phone-systems-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supplies, installs, programs and maintains on-premise PBX phone systems across the Gold Coast — including new system design, handset supply and commissioning — covering LG Ericsson iPECS, Panasonic KX-NS, KX-TDA and KX-TDE, NEC UNIVERGE SV9100, SV8100 and SL2100, and Alcatel-Lucent OmniPCX and OXO Connect. bcom ICT continues to support legacy systems that many providers no longer service. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'LG Ericsson iPECS',
                                         None,
                                         'Installation, programming, extension changes, call flow updates '
                                         'and fault diagnosis. Still a capable platform and rarely worth '
                                         'replacing while it works.'),
                                 (       'Panasonic KX-NS, KX-TDA, KX-TDE',
                                         None,
                                         'Widely installed across Gold Coast businesses and increasingly '
                                         'orphaned as providers move to cloud-only. We still service '
                                         'them.'),
                                 (       'NEC UNIVERGE SV9100, SV8100, SL2100',
                                         None,
                                         'Programming, moves and changes, hardware faults and expansion. '
                                         'Common in professional practices and multi-line reception '
                                         'environments.'),
                                 (       'Alcatel-Lucent OmniPCX & OXO Connect',
                                         None,
                                         'Less common locally, which is exactly why finding anyone to '
                                         'touch one is difficult. We do.')],
                'cols': 2,
                'eyebrow': 'Supply & install',
                'h2': 'Systems we supply, install and support',
                'icon': False},
        {       'h2': 'The problem we most often solve',
                'html': '<p style="max-width:68ch">A business has a phone system that works. A staff '
                        'member leaves, an extension needs reassigning, the after-hours message needs '
                        'changing — and the company that installed it has moved to cloud-only and will not '
                        'come out. The business is then told the only option is a full replacement.</p><p '
                        'style="max-width:68ch;margin-top:16px">Sometimes replacement genuinely is the '
                        'right call. Often it is not, and the quote is being driven by who is available '
                        'rather than by what the system needs. We will assess honestly how much life is '
                        'left, what it would cost to keep running, and what a sensible replacement '
                        'timeline looks like — so it becomes a planned capital decision rather than a '
                        'forced one.</p>'},
        {       'h2': 'What we do on a PBX',
                'ticks': [       'Extension adds, moves and changes — new starters, departures, desk swaps',
                                 'Call flow and hunt group programming, including after-hours and holiday '
                                 'handling',
                                 'Auto-attendant menus and recorded announcements',
                                 'Voicemail configuration, including voicemail-to-email where the system '
                                 'supports it',
                                 'Fault diagnosis and hardware replacement, including sourcing parts for '
                                 'older platforms',
                                 "Relocation during an <a href='/office-it-relocation-gold-coast'>office "
                                 'move</a>, including number porting',
                                 'Honest assessment of remaining life, and planning the eventual move to '
                                 '<a '
                                 "href='/voip-phone-system-installation-and-support-gold-coast'>VoIP</a> "
                                 'when it makes sense']}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>How much does a business phone system cost?</h2>
      <p>An indicative figure for a described system, so you can judge whether to have the conversation. The quote comes after we know what you need and what is being replaced.</p>
    </div>
    {price_table(PRICING, note='This is an indicative planning figure for the system described above, not a quote and not a per-handset rate. Hardware and installation are quoted as a one-off fixed price once we know how many extensions you need and what is being replaced, and that price is agreed before we start. The monthly service and call plan is separate and depends on how many numbers and concurrent calls you need &mdash; we quote it alongside the install so you are looking at the whole cost rather than the attractive half of it. A business that does not want desk phones can run softphones on the computers and mobiles it already owns, which removes the hardware line entirely and leaves only the installation.')}
  </div>
</section>
'''
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The PBX problems we are actually called to</h2>
      <p>Six situations. The most common one is a working system with nobody left to maintain it.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What PBX work actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Brands</span>
      <h2>The platforms we actually program</h2>
      <p>Each of these has its own page covering the faults specific to that estate, because they do not fail in the same ways.</p>
    </div>
    <div class="grid grid--2"><div class="card"><h3><a href="/panasonic-pbx-gold-coast">Panasonic PBX</a></h3></div><div class="card"><h3><a href="/nec-pbx-gold-coast">NEC PBX</a></h3></div><div class="card"><h3><a href="/lg-ericsson-pbx-gold-coast">LG Ericsson PBX</a></h3></div><div class="card"><h3><a href="/alcatel-lucent-pbx-gold-coast">Alcatel-Lucent PBX</a></h3></div></div>
  </div>
</section>
'''
            + related([       ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Telecommunications Contractor', '/telecommunications-contractor-gold-coast')])
            + cta('Got a system nobody will touch?', "Tell us the make and model. If it's on our list, you probably don't need the replacement you've been quoted."),
}

from layout import cta, faq_block, related, svc_body, models, issues, example

COMMON_ISSUES = [
    ("&ldquo;Nobody will touch our Panasonic&rdquo;",
     "the installer retiring or moving on, and the programming knowledge going with them. Panasonic is the most widely installed legacy platform on the Gold Coast, which also means a great many of them are now orphaned.",
     "We still program these systems. A working platform with nobody to maintain it is a support problem rather than a technical one, and being told to replace it is not the same as needing to."),
    ("&ldquo;The cordless handsets drop as you walk the building&rdquo;",
     "cordless base stations positioned for a smaller premises, or one that has since been partitioned. Handover between bases is the part that fails first as a building changes around the system.",
     "Check coverage along the routes people actually walk and reposition or add a base. Cordless coverage is rarely the reason a business replaces a system, and it is frequently the reason it wants to."),
    ("&ldquo;We can&rsquo;t change the after-hours greeting&rdquo;",
     "a system configured by an installer who never handed anything over. The capability is there and the knowledge left with them.",
     "Make the change, then document the call flow and show whoever will need to alter it next. A phone system only its installer can operate is a dependency rather than an asset."),
    ("&ldquo;Voicemail has stopped recording&rdquo;",
     "storage that has filled, or a voicemail component that has failed. On older platforms this happens quietly and callers simply hear the phone ring out.",
     "Check the storage and the component before assuming the worst. This is one of the more common faults on ageing systems and one of the more straightforward to resolve."),
    ("&ldquo;Half the extensions died after a blackout&rdquo;",
     "a card or a power supply that did not survive the event. Legacy systems are more vulnerable to power disturbance than most equipment in a building.",
     "Identify what failed and whether it is replaceable. Where it is, protect the system properly afterwards &mdash; an unprotected PBX in a building with unreliable power will keep doing this."),
    ("&ldquo;We&rsquo;ve been told we have to replace it&rdquo;",
     "sometimes true and sometimes a sales position. Whether it is genuinely finished depends on the platform, what parts are still obtainable and what the business needs it to do.",
     "Get an honest assessment. We supply new systems and we also keep older ones running, so we have no particular reason to push you either way &mdash; and we will tell you when a system has years left in it."),
]

EXAMPLE_1 = example(
    "A system the business had been told was dead",
    "A business with around thirty extensions had been quoted for a complete replacement after their long-standing installer retired. Two providers had declined to work on the existing system at all.",
    "The platform was functioning correctly. The actual complaint was that nobody could change the after-hours greeting or add an extension, because the programming credentials had left with the installer and no documentation existed. Nothing was broken &mdash; the business had simply lost the ability to operate what it owned.",
    "Recovered administrative access, made the changes the business had been waiting months for, and documented the numbering plan, call flow and greetings so the next change does not require anybody at all.",
    "The replacement was deferred by several years and will happen when the business decides it should, not when it was told. We would have been happy to sell the new system and it was not what the situation called for.")

EXAMPLE_2 = example(
    "Cordless coverage that a partition wall broke",
    "A business reported cordless handsets dropping calls in part of their premises. The system had worked without complaint for six years and the problem had begun a few months earlier.",
    "The tenancy had been partitioned to create two meeting rooms shortly before the problem started. The new walls sat directly between the cordless base and the area now suffering, and the handover to the second base was happening too late to be seamless. The phone system had not changed at all &mdash; the building had.",
    "Repositioned one base station and added a third to cover the area created by the partitioning, then walked the building with a handset to confirm handover happened cleanly.",
    "Calls stopped dropping. The business had been considering replacing the whole system over a fault created by its own fit-out, which is worth checking before anyone quotes for a platform.")

FAQS = [   (   'Who services Panasonic phone systems on the Gold Coast?',
        'bcom ICT supplies, installs, programmes and repairs Panasonic PBX systems across the Gold Coast, covering KX-NS700, KX-NS1000 and the earlier KX-TDA, KX-TDE and KX-TES platforms, plus the current and '
        'legacy handset ranges. That includes extension changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 '
        '8993.'),
    (   'Do you support older Panasonic systems, not just current models?',
        'Yes — the legacy platforms are a large part of what we do. As providers move to cloud-only, plenty of Gold Coast businesses are left with a working system and nobody willing to attend. If '
        'your model is listed on this page, we service it.'),
    (   'Our provider says it has to be replaced. Is that true?',
        "Sometimes, but frequently it reflects who is available rather than the system's condition. If the platform still does what your business needs and parts are obtainable, keeping it is often "
        "the cheaper answer. We'll assess remaining life honestly before you commit to a replacement quote."),
    (   'Can you just make one change without an ongoing contract?',
        "Yes. Plenty of clients call for a one-off — an extension, a call flow, an after-hours message — at $190 + GST per hour plus a $100 + GST call-out for on-site attendance. There's no "
        'requirement to sign up to anything ongoing.'),
    (   'Can you still get parts and handsets?',
        "For most Panasonic platforms listed here, yes — new, refurbished or from stock. Tell us the exact model and we'll tell you honestly what's obtainable and what isn't. Where a part genuinely "
        "can't be sourced, that's the point at which replacement stops being optional and becomes a planning exercise."),
    (   'Can it connect to SIP trunks?',
        "Where the platform and card configuration support it, yes — and it often defers a full replacement by years while reducing call costs. We'll tell you whether your specific model can do it "
        'before quoting anything.'),
    (   'Can you move it to a new office?',
        'Yes. PBX relocation, recabling and number porting are handled as part of an office IT relocation, planned around your move date rather than attempted on the day.')]

PAGE = {
    "path": '/panasonic-pbx-gold-coast',
    "priority": '0.7',
    "title": 'Panasonic PBX Support Gold Coast — KX-NS700, KX-TDA200 | bcom ICT',
    "description": 'Panasonic phone system programming, repair and support on the Gold Coast — KX-NS700, KX-NS1000 and the earlier KX-TDA, KX-TDE and KX-TES platforms. Extension changes, call flows, handset replacement and parts. Call 07 3041 8993.',
    "hero_img": 'panasonic-pbx-gold-coast-hero.webp',
    "hero_alt": 'A Panasonic PBX phone system being programmed by bcom ICT on the Gold Coast',
    "h1": 'Panasonic systems, supplied and supported',
    "lede": 'KX-NS700 · KX-TDA200 · KX-TES824 · KX-DT546. New systems specified and installed, existing ones programmed and repaired — including the platforms most providers have walked away from.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['New systems supplied', 'Current + legacy models', 'Parts sourced', 'Honest advice'],
    "crumbs": [('Services', '/services'), ('PBX Systems', '/pabx-phone-systems-gold-coast'), ('Panasonic', '/panasonic-pbx-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supplies, installs, programmes and repairs Panasonic PBX phone systems across the Gold Coast, covering KX-NS700, KX-NS1000 and the earlier KX-TDA, KX-TDE and KX-TES platforms, along with the current and legacy handset ranges. Work includes extension adds and changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'Models',
                'h2': 'Every Panasonic system and handset we work on',
                'html': models([('Current systems', 'The current NS and NSX ranges.', ['KX-NS700', 'KX-NS1000', 'KX-NSX1000', 'KX-NSX2000']), ('Legacy systems — still serviced', 'TDA, TDE and the analogue TES/TA range. Extremely common in older Gold Coast small business sites.', ['KX-TDA15', 'KX-TDA30', 'KX-TDA100', 'KX-TDA100D', 'KX-TDA200', 'KX-TDA600', 'KX-TDE100', 'KX-TDE200', 'KX-TDE600', 'KX-TES824', 'KX-TEM824', 'KX-TEB308', 'KX-TA308', 'KX-TA616', 'KX-TA824', 'KX-TVM50', 'KX-TVM200']), ('Current handsets — DT500 & NT500', 'The current digital and IP desk range.', ['KX-DT521', 'KX-DT543', 'KX-DT546', 'KX-NT511', 'KX-NT551', 'KX-NT553', 'KX-NT556', 'KX-NT560']), ('Legacy handsets — DT300, NT300, T7600', 'Older sets. Usually what is actually on the desk in a TDA or TES site.', ['KX-DT321', 'KX-DT333', 'KX-DT343', 'KX-DT346', 'KX-NT321', 'KX-NT343', 'KX-NT346', 'KX-NT366', 'KX-T7630', 'KX-T7633', 'KX-T7636', 'KX-T7665', 'KX-T7730', 'KX-T7735']), ('SIP handsets and DECT', 'SIP desk phones and the cordless range.', ['KX-HDV130', 'KX-HDV230', 'KX-HDV330', 'KX-HDV430', 'KX-TGP600', 'KX-TCA175', 'KX-TCA185', 'KX-TCA285', 'KX-TCA385', 'KX-UDT111', 'KX-UDT121', 'KX-UDT131'])]),
                'sub': 'Search for whatever is written on the box or the handset — if it is listed here, '
                       'we service it.'},
        {       'cards': [       (       'Adds, moves and changes',
                                         None,
                                         'New starters, departures, desk swaps, extension reassignments. '
                                         'The everyday work that becomes impossible when nobody will '
                                         'attend.'),
                                 (       'Call flows and after-hours',
                                         None,
                                         'Ring order, hunt groups, overflow, holiday messages and the '
                                         'after-hours greeting nobody can work out how to change.'),
                                 (       'Voicemail and auto-attendant',
                                         None,
                                         'Menu programming, recorded announcements, mailbox resets, and '
                                         'voicemail-to-email where the platform supports it.'),
                                 (       'Faults, handsets and parts',
                                         None,
                                         'Diagnosis, card and handset replacement, and sourcing parts for '
                                         "platforms no longer sold new. Tell us the model and we'll tell "
                                         "you honestly what's obtainable.")],
                'cols': 2,
                'eyebrow': 'What we do',
                'h2': 'The work people call about',
                'icon': False},
        {       'h2': 'Should you replace it?',
                'html': '<p style="max-width:68ch">Panasonic is the most widely installed legacy platform '
                        'we see on the Gold Coast, and increasingly the most orphaned as providers move to '
                        'cloud-only.</p><p style="max-width:68ch;margin-top:16px">Our position: if the '
                        'platform still does what your business needs and parts are obtainable, keeping it '
                        'is usually cheaper and we will say so. Replacement becomes right when hardware is '
                        'failing, when you need staff working from home, when you are opening a second '
                        'site, or when parts genuinely run out.</p><p '
                        'style="max-width:68ch;margin-top:16px">Where the system supports SIP trunks, '
                        'connecting it to them often defers replacement by years while cutting call costs. '
                        'When the time does come, <a '
                        'href="/voip-phone-system-installation-and-support-gold-coast">moving to cloud '
                        'VoIP</a> becomes a planned capital decision rather than a forced one — and we '
                        'test whether your internet is actually ready before recommending it.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The Panasonic problems we are actually called to</h2>
      <p>Six situations, and the most common one is not a fault at all.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What Panasonic work actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Telecommunications Contractor', '/telecommunications-contractor-gold-coast')])
            + cta('Got a Panasonic system nobody will touch?', "Tell us the model number. If it's on the list above, you probably don't need the replacement you've been quoted."),
}

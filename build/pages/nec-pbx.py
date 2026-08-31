from layout import cta, faq_block, related, svc_body, models

FAQS = [   (   'Who services NEC phone systems on the Gold Coast?',
        'bcom ICT supplies, installs, programmes and repairs NEC PBX systems across the Gold Coast, covering UNIVERGE SV9100, SL2100 and the earlier SV8100, Aspire and Xen platforms, plus the current and '
        'legacy handset ranges. That includes extension changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 '
        '8993.'),
    (   'Do you support older NEC systems, not just current models?',
        'Yes — the legacy platforms are a large part of what we do. As providers move to cloud-only, plenty of Gold Coast businesses are left with a working system and nobody willing to attend. If '
        'your model is listed on this page, we service it.'),
    (   'Our provider says it has to be replaced. Is that true?',
        "Sometimes, but frequently it reflects who is available rather than the system's condition. If the platform still does what your business needs and parts are obtainable, keeping it is often "
        "the cheaper answer. We'll assess remaining life honestly before you commit to a replacement quote."),
    (   'Can you just make one change without an ongoing contract?',
        "Yes. Plenty of clients call for a one-off — an extension, a call flow, an after-hours message — at $198 + GST per hour plus a $100 + GST call-out for on-site attendance. There's no "
        'requirement to sign up to anything ongoing.'),
    (   'Can you still get parts and handsets?',
        "For most NEC platforms listed here, yes — new, refurbished or from stock. Tell us the exact model and we'll tell you honestly what's obtainable and what isn't. Where a part genuinely can't "
        "be sourced, that's the point at which replacement stops being optional and becomes a planning exercise."),
    (   'Can it connect to SIP trunks?',
        "Where the platform and card configuration support it, yes — and it often defers a full replacement by years while reducing call costs. We'll tell you whether your specific model can do it "
        'before quoting anything.'),
    (   'Can you move it to a new office?',
        'Yes. PBX relocation, recabling and number porting are handled as part of an office IT relocation, planned around your move date rather than attempted on the day.')]

PAGE = {
    "path": '/nec-pbx-gold-coast',
    "priority": '0.7',
    "title": 'NEC PBX Support Gold Coast — SV9100, SL2100 | bcom ICT',
    "description": 'NEC phone system programming, repair and support on the Gold Coast — UNIVERGE SV9100, SL2100 and the earlier SV8100, Aspire and Xen platforms. Extension changes, call flows, handset replacement and parts. Call 07 3041 8993.',
    "hero_img": 'nec-pbx-gold-coast-hero.webp',
    "hero_alt": 'A NEC PBX phone system being programmed by bcom ICT on the Gold Coast',
    "h1": 'NEC systems, supplied and supported',
    "lede": 'SV9100 · SL2100 · Xen Topaz · DT900. New systems specified and installed, existing ones programmed and repaired — including the platforms most providers have walked away from.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['New systems supplied', 'Current + legacy models', 'Parts sourced', 'Honest advice'],
    "crumbs": [('Services', '/services'), ('PBX Systems', '/pabx-phone-systems-gold-coast'), ('NEC', '/nec-pbx-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supplies, installs, programmes and repairs NEC PBX phone systems across the Gold Coast, covering UNIVERGE SV9100, SL2100 and the earlier SV8100, Aspire and Xen platforms, along with the current and legacy handset ranges. Work includes extension adds and changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'Models',
                'h2': 'Every NEC system and handset we work on',
                'html': models([('Current systems', 'The current UNIVERGE and SL ranges.', ['UNIVERGE SV9100', 'SV9300', 'SV9500', 'SL2100', 'UNIVERGE 3C', 'UNIVERGE BLUE']), ('Legacy systems — still serviced', 'Earlier NEC platforms, including the Xen range that is still everywhere in older Australian offices.', ['UNIVERGE SV8100', 'SV8300', 'SV8500', 'SL1100', 'SL1000', 'Aspire', 'Aspire S', 'Xen Topaz', 'Xen Alpha', 'Xen Master', 'Xen IPK', 'Xen IPK II']), ('Current handsets — DT900 & DT800', 'The current desk range.', ['ITK-6D', 'ITK-8LC', 'ITK-12D', 'ITK-24', 'ITK-32', 'ITZ-6DE', 'ITZ-12D', 'ITZ-24D', 'ITZ-32D']), ('Legacy handsets — DT700, DT400, DT300', 'Older digital and IP sets, widely still in service.', ['ITL-2E', 'ITL-6DE', 'ITL-12D', 'ITL-24D', 'ITL-32D', 'DTZ-6DE', 'DTZ-12D', 'DTZ-24D', 'DTZ-32D', 'DTL-6DE', 'DTL-12D', 'DTL-24D', 'DTL-32D', 'IP4WW', 'IP7WW', 'DTerm Series i']), ('DECT and wireless', 'Cordless handsets and base stations.', ['G266', 'G566', 'I766', 'ML440', 'MH240', 'AP20', 'AP400'])]),
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
                'html': '<p style="max-width:68ch">NEC systems are common in Gold Coast professional '
                        'practices and reception-heavy sites, where proper handsets and hunt groups still '
                        'beat a softphone. The Xen range in particular is still everywhere in older '
                        'Australian offices.</p><p style="max-width:68ch;margin-top:16px">Our position: if '
                        'the platform still does what your business needs and parts are obtainable, '
                        'keeping it is usually cheaper and we will say so. Replacement becomes right when '
                        'hardware is failing, when you need staff working from home, when you are opening '
                        'a second site, or when parts genuinely run out.</p><p '
                        'style="max-width:68ch;margin-top:16px">Where the system supports SIP trunks, '
                        'connecting it to them often defers replacement by years while cutting call costs. '
                        'When the time does come, <a '
                        'href="/voip-phone-system-installation-and-support-gold-coast">moving to cloud '
                        'VoIP</a> becomes a planned capital decision rather than a forced one — and we '
                        'test whether your internet is actually ready before recommending it.</p>'}])
            + faq_block(FAQS)
            + related([       ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Telecommunications Contractor', '/telecommunications-contractor-gold-coast')])
            + cta('Got a NEC system nobody will touch?', "Tell us the model number. If it's on the list above, you probably don't need the replacement you've been quoted."),
}

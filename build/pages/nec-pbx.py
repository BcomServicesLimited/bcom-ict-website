from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Who services NEC phone systems on the Gold Coast?',
        'bcom ICT installs, programmes and maintains NEC PBX systems across the Gold Coast, covering NEC UNIVERGE SV9100, SV8100 and SL2100. That includes extension changes, call flow programming, '
        'auto-attendant and voicemail configuration, fault diagnosis and parts sourcing. Call 07 3041 8993.'),
    (   'Our provider says the system has to be replaced. Is that true?',
        "Sometimes, but frequently it reflects who is available rather than the system's condition. If the platform still does what your business needs and parts are obtainable, keeping it is often "
        'the cheaper answer. We will assess remaining life honestly before you commit to a replacement quote.'),
    (   'Can you just make one change without an ongoing contract?',
        'Yes. Plenty of clients call for a one-off — an extension, a call flow, an after-hours message — charged at $198 + GST per hour plus a $100 + GST call-out for on-site attendance. There is no '
        'requirement to sign up to anything ongoing.'),
    (   'Can you still get parts?',
        'For the NEC platforms listed above, usually yes. Where a part is genuinely unobtainable we will tell you, because that is the point at which replacement stops being optional and becomes a '
        'planning exercise.'),
    (   'Can you connect it to SIP trunks?',
        "Where the platform supports it, yes — and it often defers a full replacement by years while reducing call costs. We'll tell you whether your specific model and card configuration can do "
        'it.'),
    (   'Can you move it to a new office?',
        'Yes. PBX relocation, recabling and number porting are handled as part of an office IT relocation, planned around your move date rather than attempted on the day.')]

PAGE = {
    "path": '/nec-pbx-gold-coast',
    "priority": '0.65',
    "title": 'NEC PBX Support Gold Coast — UNIVERGE | bcom ICT',
    "description": 'NEC UNIVERGE phone system installation, programming and support on the Gold Coast. Extension changes, call flows, fault diagnosis and honest advice on remaining life.',
    "hero_img": 'nec-pbx-gold-coast-hero.webp',
    "hero_alt": 'A NEC UNIVERGE phone system being programmed by bcom ICT on the Gold Coast',
    "h1": 'NEC phone systems, still supported',
    "lede": 'A working NEC system that nobody will program is a genuinely frustrating position. We service, programme and maintain them.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['UNIVERGE supported', 'Programming & moves', 'Parts sourced', 'Honest replacement advice'],
    "crumbs": [('Services', '/services'), ('PBX Systems', '/pabx-phone-systems-gold-coast'), ('NEC PBX', '/nec-pbx-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT installs, programmes and maintains NEC PBX phone systems across the Gold Coast, covering NEC UNIVERGE SV9100, SV8100 and SL2100. Work includes extension adds and changes, call flow and hunt group programming, auto-attendant and voicemail configuration, fault diagnosis and parts sourcing. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Adds, moves and changes',
                                         None,
                                         'New starters, departures, desk swaps and extension reassignments '
                                         '— the everyday work that becomes impossible when nobody will '
                                         'attend.'),
                                 (       'Call flows and hunt groups',
                                         None,
                                         'Ring order, overflow, after-hours handling and holiday messages. '
                                         "Usually the thing a business needs changed and can't do itself."),
                                 (       'Auto-attendant and voicemail',
                                         None,
                                         'Menu programming, recorded announcements, and voicemail-to-email '
                                         'where the platform supports it.'),
                                 (       'Faults and parts',
                                         None,
                                         'Diagnosis, board and handset replacement, and sourcing parts for '
                                         'platforms that are no longer sold new.')],
                'cols': 2,
                'eyebrow': 'What we do',
                'h2': 'Working on NEC systems',
                'icon': False},
        {       'h2': 'Models we support',
                'ticks': [       '<strong>NEC UNIVERGE SV9100, SV8100 and SL2100</strong>',
                                 'Extension cards, trunk cards and handset replacement',
                                 'SIP trunk integration where the platform supports it, which often defers '
                                 'a full replacement',
                                 "Relocation during an <a href='/office-it-relocation-gold-coast'>office "
                                 'move</a>, including number porting',
                                 "Documentation of the current programming, so the next change doesn't "
                                 'start from scratch']},
        {       'h2': 'Should you replace it?',
                'html': '<p style="max-width:68ch">NEC systems are common in professional practices and '
                        'reception-heavy sites on the Gold Coast, where proper handsets and hunt groups '
                        'still beat a softphone.</p><p style="max-width:68ch;margin-top:16px">Our honest '
                        'position: if the platform still does what your business needs and parts are '
                        'obtainable, keeping it is usually the cheaper answer and we will say so. '
                        'Replacement becomes the right call when hardware is failing, when you need staff '
                        'working from home, when you are opening a second site, or when parts genuinely '
                        'run out.</p><p style="max-width:68ch;margin-top:16px">When that point arrives we '
                        'will tell you, and <a '
                        'href="/voip-phone-system-installation-and-support-gold-coast">moving to cloud '
                        'VoIP</a> is a planned capital decision rather than a forced one. Before any move '
                        'we test whether your internet connection is actually ready for it.</p>'}])
            + faq_block(FAQS)
            + related([       ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Telecommunications Contractor', '/telecommunications-contractor-gold-coast')])
            + cta('Got a NEC system nobody will touch?', "Tell us the model. If it's on our list, you probably don't need the replacement you've been quoted."),
}

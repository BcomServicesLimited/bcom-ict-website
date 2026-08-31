from layout import cta, faq_block, related, svc_body, models

FAQS = [   (   'Who services Alcatel-Lucent phone systems on the Gold Coast?',
        'bcom ICT supplies, installs, programmes and repairs Alcatel-Lucent PBX systems across the Gold Coast, covering OXO Connect, OmniPCX Office and OmniPCX Enterprise, plus the current and legacy handset '
        'ranges. That includes extension changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 8993.'),
    (   'Do you support older Alcatel-Lucent systems, not just current models?',
        'Yes — the legacy platforms are a large part of what we do. As providers move to cloud-only, plenty of Gold Coast businesses are left with a working system and nobody willing to attend. If '
        'your model is listed on this page, we service it.'),
    (   'Our provider says it has to be replaced. Is that true?',
        "Sometimes, but frequently it reflects who is available rather than the system's condition. If the platform still does what your business needs and parts are obtainable, keeping it is often "
        "the cheaper answer. We'll assess remaining life honestly before you commit to a replacement quote."),
    (   'Can you just make one change without an ongoing contract?',
        "Yes. Plenty of clients call for a one-off — an extension, a call flow, an after-hours message — at $198 + GST per hour plus a $100 + GST call-out for on-site attendance. There's no "
        'requirement to sign up to anything ongoing.'),
    (   'Can you still get parts and handsets?',
        "For most Alcatel-Lucent platforms listed here, yes — new, refurbished or from stock. Tell us the exact model and we'll tell you honestly what's obtainable and what isn't. Where a part "
        "genuinely can't be sourced, that's the point at which replacement stops being optional and becomes a planning exercise."),
    (   'Can it connect to SIP trunks?',
        "Where the platform and card configuration support it, yes — and it often defers a full replacement by years while reducing call costs. We'll tell you whether your specific model can do it "
        'before quoting anything.'),
    (   'Can you move it to a new office?',
        'Yes. PBX relocation, recabling and number porting are handled as part of an office IT relocation, planned around your move date rather than attempted on the day.')]

PAGE = {
    "path": '/alcatel-lucent-pbx-gold-coast',
    "priority": '0.7',
    "title": 'Alcatel-Lucent PBX Support Gold Coast — OXO Connect, OmniPCX | bcom ICT',
    "description": 'Alcatel-Lucent phone system programming, repair and support on the Gold Coast — OXO Connect, OmniPCX Office and OmniPCX Enterprise. Extension changes, call flows, handset replacement and parts. Call 07 3041 8993.',
    "hero_img": 'alcatel-lucent-pbx-gold-coast-hero.webp',
    "hero_alt": 'A Alcatel-Lucent PBX phone system being programmed by bcom ICT on the Gold Coast',
    "h1": 'Alcatel-Lucent systems, supplied and supported',
    "lede": 'OXO Connect · OmniPCX · 8068s · ALE-400. New systems specified and installed, existing ones programmed and repaired — including the platforms most providers have walked away from.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['New systems supplied', 'Current + legacy models', 'Parts sourced', 'Honest advice'],
    "crumbs": [('Services', '/services'), ('PBX Systems', '/pabx-phone-systems-gold-coast'), ('Alcatel-Lucent', '/alcatel-lucent-pbx-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supplies, installs, programmes and repairs Alcatel-Lucent PBX phone systems across the Gold Coast, covering OXO Connect, OmniPCX Office and OmniPCX Enterprise, along with the current and legacy handset ranges. Work includes extension adds and changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'Models',
                'h2': 'Every Alcatel-Lucent system and handset we work on',
                'html': models([('Current systems', 'Still sold and supported. Most Gold Coast Alcatel sites run one of these.', ['OXO Connect', 'OXO Connect Evolution', 'OmniPCX Enterprise (OXE)', 'OXE Purple', 'Rainbow (cloud)']), ('Legacy systems — still serviced', 'Earlier platforms. If yours is here, it very likely does not need replacing yet.', ['OmniPCX Office (OXO)', 'OmniPCX Office RCE Small', 'RCE Medium', 'RCE Large', 'OmniPCX 4400', 'Alcatel 4200', 'Alcatel 4400']), ('Current handsets — Myriad & Premium DeskPhone', 'The current desk range.', ['ALE-2', 'ALE-20', 'ALE-20h', 'ALE-30h', 'ALE-300', 'ALE-400', 'ALE-500', '8018 DeskPhone', '8028s', '8038', '8058s', '8068s']), ('Legacy handsets — IP Touch & Reflexes', 'Older sets, widely still in service. We source replacements where we can.', ['4008 IP Touch', '4018', '4028', '4038', '4068', '4004 Reflexes', '4019', '4029', '4039', '8001', '8002', '8008', '8012']), ('DECT and wireless', 'Cordless handsets and base stations.', ['8212 DECT', '8232 DECT', '8242 DECT', '8262 DECT', '8378 DECT IP-xBS', '300 DECT', '400 DECT'])]),
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
                'html': '<p style="max-width:68ch">Alcatel-Lucent is less common on the Gold Coast than '
                        'Panasonic or NEC, which is exactly why finding anyone willing to touch one is '
                        'difficult. We do.</p><p style="max-width:68ch;margin-top:16px">Our position: if '
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
            + cta('Got a Alcatel-Lucent system nobody will touch?', "Tell us the model number. If it's on the list above, you probably don't need the replacement you've been quoted."),
}

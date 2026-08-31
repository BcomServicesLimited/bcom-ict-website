from layout import cta, faq_block, related, svc_body, models

FAQS = [   (   'Who services LG Ericsson phone systems on the Gold Coast?',
        'bcom ICT programmes, repairs and supports LG Ericsson PBX systems across the Gold Coast, covering iPECS eMG80, eMG100, UCP and the earlier LIK and ipLDK platforms, plus the current and '
        'legacy handset ranges. That includes extension changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 '
        '8993.'),
    (   'Do you support older LG Ericsson systems, not just current models?',
        'Yes — the legacy platforms are a large part of what we do. As providers move to cloud-only, plenty of Gold Coast businesses are left with a working system and nobody willing to attend. If '
        'your model is listed on this page, we service it.'),
    (   'Our provider says it has to be replaced. Is that true?',
        "Sometimes, but frequently it reflects who is available rather than the system's condition. If the platform still does what your business needs and parts are obtainable, keeping it is often "
        "the cheaper answer. We'll assess remaining life honestly before you commit to a replacement quote."),
    (   'Can you just make one change without an ongoing contract?',
        "Yes. Plenty of clients call for a one-off — an extension, a call flow, an after-hours message — at $198 + GST per hour plus a $100 + GST call-out for on-site attendance. There's no "
        'requirement to sign up to anything ongoing.'),
    (   'Can you still get parts and handsets?',
        "For most LG Ericsson platforms listed here, yes — new, refurbished or from stock. Tell us the exact model and we'll tell you honestly what's obtainable and what isn't. Where a part "
        "genuinely can't be sourced, that's the point at which replacement stops being optional and becomes a planning exercise."),
    (   'Can it connect to SIP trunks?',
        "Where the platform and card configuration support it, yes — and it often defers a full replacement by years while reducing call costs. We'll tell you whether your specific model can do it "
        'before quoting anything.'),
    (   'Can you move it to a new office?',
        'Yes. PBX relocation, recabling and number porting are handled as part of an office IT relocation, planned around your move date rather than attempted on the day.')]

PAGE = {
    "path": '/lg-ericsson-pbx-gold-coast',
    "priority": '0.7',
    "title": 'LG Ericsson PBX Support Gold Coast — eMG80, UCP600 | bcom ICT',
    "description": 'LG Ericsson phone system programming, repair and support on the Gold Coast — iPECS eMG80, eMG100, UCP and the earlier LIK and ipLDK platforms. Extension changes, call flows, handset replacement and parts. Call 07 3041 8993.',
    "hero_img": 'lg-ericsson-pbx-gold-coast-hero.webp',
    "hero_alt": 'A LG Ericsson PBX phone system being programmed by bcom ICT on the Gold Coast',
    "h1": 'LG Ericsson phone systems, still supported',
    "lede": 'eMG80 · UCP600 · LIP-9030 · ipLDK. A working system nobody will programme is a genuinely frustrating position — we service, programme and source parts for the lot.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Current + legacy models', 'Programming & moves', 'Parts sourced', 'Honest replacement advice'],
    "crumbs": [('Services', '/services'), ('PBX Systems', '/pabx-phone-systems-gold-coast'), ('LG Ericsson', '/lg-ericsson-pbx-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT programmes, repairs and supports LG Ericsson PBX phone systems across the Gold Coast, covering iPECS eMG80, eMG100, UCP and the earlier LIK and ipLDK platforms, along with the current and legacy handset ranges. Work includes extension adds and changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'Models',
                'h2': 'Every LG Ericsson system and handset we work on',
                'html': models([('Current systems', 'The current iPECS range, on-premise and cloud.', ['iPECS eMG80', 'iPECS eMG100', 'iPECS UCP100', 'iPECS UCP600', 'iPECS UCP2400', 'iPECS ONE', 'iPECS Cloud']), ('Legacy systems — still serviced', 'Earlier Ericsson-LG and LG-Nortel platforms. Common across older Gold Coast installs.', ['iPECS LIK-100', 'LIK-300', 'LIK-600', 'LIK-1200', 'iPECS MG100', 'MG300', 'ipLDK-20', 'ipLDK-60', 'ipLDK-100', 'ipLDK-300', 'GDK-100', 'GDK-162']), ('Current handsets — 1000i & LIP-9000', 'The current desk range.', ['1010i', '1020i', '1030i', '1040i', '1050i', 'LIP-9002', 'LIP-9008', 'LIP-9010', 'LIP-9020', 'LIP-9030', 'LIP-9040', 'LIP-9070']), ('Legacy handsets — LIP-8000 & LDP', 'Older IP and digital sets. Frequently what is actually on the desk.', ['LIP-8002', 'LIP-8004', 'LIP-8008', 'LIP-8012', 'LIP-8024', 'LIP-8040', 'LDP-7004', 'LDP-7008', 'LDP-7016', 'LDP-7024', 'LDP-9008', 'LDP-9030', 'LDP-9240']), ('DECT and wireless', 'Cordless handsets and repeaters.', ['GDC-450H', 'GDC-480H', 'GDC-500H', 'GDC-800H', 'W-SOHO', 'WIT-400HE'])]),
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
                'html': '<p style="max-width:68ch">iPECS is a capable platform that is rarely worth '
                        'replacing while it works. Most of the replacement quotes we review for iPECS '
                        "sites are driven by who is available, not by the system's condition.</p><p "
                        'style="max-width:68ch;margin-top:16px">Our position: if the platform still does '
                        'what your business needs and parts are obtainable, keeping it is usually cheaper '
                        'and we will say so. Replacement becomes right when hardware is failing, when you '
                        'need staff working from home, when you are opening a second site, or when parts '
                        'genuinely run out.</p><p style="max-width:68ch;margin-top:16px">Where the system '
                        'supports SIP trunks, connecting it to them often defers replacement by years '
                        'while cutting call costs. When the time does come, <a '
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
            + cta('Got a LG Ericsson system nobody will touch?', "Tell us the model number. If it's on the list above, you probably don't need the replacement you've been quoted."),
}

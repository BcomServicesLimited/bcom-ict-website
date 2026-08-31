from layout import cta, faq_block, related, svc_body

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
            + faq_block(FAQS)
            + related([       ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Telecommunications Contractor', '/telecommunications-contractor-gold-coast')])
            + cta('Got a system nobody will touch?', "Tell us the make and model. If it's on our list, you probably don't need the replacement you've been quoted."),
}

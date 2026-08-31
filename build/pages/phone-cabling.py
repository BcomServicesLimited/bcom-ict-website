from layout import cta, faq_block, related, svc_body

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
    "title": 'Phone Line Installation & Voice Cabling Gold Coast | bcom ICT',
    "description": 'Internal phone line and voice cabling for Gold Coast offices and commercial premises. Installed to Australian standards by ACMA registered cabling contractors, tested and documented.',
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
            + faq_block(FAQS)
            + related([       ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Telecommunications Contractor', '/telecommunications-contractor-gold-coast')])
            + cta('Fitting out or adding points?', "We'll tell you whether you need voice cabling at all — for most modern systems, one structured installation covers both."),
}

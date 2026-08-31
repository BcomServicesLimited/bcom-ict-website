from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What does a telecommunications contractor do?',
        'Supplies and installs business phone systems, runs voice and data cabling, manages internet and NBN connections, and handles number porting. bcom ICT covers all of it on the Gold Coast, '
        'with cabling carried out by ACMA registered cabling contractors it engages and manages.'),
    (   'Is bcom ICT a registered cabler?',
        'No. Fixed cabling connected to the telecommunications network requires ACMA cabler registration, and bcom ICT does not hold it. Cabling work is carried out by ACMA registered contractors '
        'that bcom ICT engages and manages, with testing and certification documentation provided on completion.'),
    (   'Why use one contractor for phones, cabling and internet?',
        'Because voice quality depends on the connection, the network and the cabling as much as on the phone system. When those sit with three suppliers, a dropped-call fault becomes a three-week '
        'argument with you in the middle.'),
    (   'Do you sell internet or phone plans?',
        "We're not a reseller. We work with whatever provider you're with, which means our advice on whether the service is at fault isn't influenced by wanting to sell you a different one."),
    (   'Can you support our existing phone system?',
        'Very likely. We maintain LG Ericsson iPECS, Panasonic KX, NEC UNIVERGE and Alcatel-Lucent systems, including legacy platforms many providers have stopped servicing.')]

PAGE = {
    "path": '/telecommunications-contractor-gold-coast',
    "priority": '0.7',
    "title": 'Telecommunications Contractor Gold Coast — Business | bcom ICT',
    "description": 'Business telecommunications on the Gold Coast — phone systems, voice and data cabling, NBN and internet, number porting and legacy PBX support, from one contractor.',
    "hero_img": 'phone-line-installation-hero.webp',
    "hero_alt": 'Telecommunications and cabling work carried out by bcom ICT for a Gold Coast business',
    "h1": 'One contractor for phones, cabling and connectivity',
    "lede": "Rather than a phone company, a cabler and an IT provider each blaming the other two when something doesn't work.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Phones, cabling & internet', 'Registered cablers engaged', 'Legacy PBX supported', 'One point of contact'],
    "crumbs": [('Services', '/services'), ('Telecommunications', '/telecommunications-contractor-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides business telecommunications services across the Gold Coast — phone system supply and installation, VoIP and legacy PBX support, voice and data cabling, NBN and business internet, and number porting. Cabling is carried out by ACMA registered cabling contractors that bcom ICT engages and manages. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'The problem this solves',
                'h2': 'Three suppliers, no accountability',
                'html': '<p style="max-width:68ch">The usual arrangement: a phone company sells the '
                        'system, a cabler runs the cabling, and an IT provider looks after the network. '
                        'When calls drop, each points at the other two and you become the project '
                        'manager.</p><p style="max-width:68ch;margin-top:16px">Voice quality depends on '
                        'the connection, the network configuration and the cabling as much as on the phone '
                        'system. Splitting those across suppliers is precisely why the fault takes three '
                        'weeks to resolve.</p>'},
        {       'h2': 'What we cover',
                'ticks': [       "<a href='/business-phone-systems-gold-coast'>Business phone systems</a> "
                                 '— supply, installation and support',
                                 "<a href='/voip-phone-system-installation-and-support-gold-coast'>Cloud "
                                 "VoIP</a> and <a href='/pabx-phone-systems-gold-coast'>on-premise "
                                 'PBX</a>, including legacy systems many providers no longer service',
                                 "<a href='/phone-line-installation-cabling-gold-coast'>Voice cabling</a> "
                                 "and <a href='/network-cabling-for-offices-gold-coast'>structured data "
                                 'cabling</a>, installed by ACMA registered cabling contractors',
                                 "<a href='/nbn-internet-support-gold-coast'>NBN and business internet</a> "
                                 '— faults, configuration, ISP escalation and 4G/5G failover',
                                 'Number porting, planned ahead of a cutover rather than attempted on the '
                                 'day',
                                 "<a href='/office-it-relocation-gold-coast'>Relocations</a> — moving the "
                                 'lot to a new site and testing it before Monday']},
        {       'h2': 'On cabling registration',
                'html': '<p style="max-width:68ch">Fixed cabling connected to the telecommunications '
                        'network legally requires ACMA cabler registration in Australia. <strong>bcom ICT '
                        'does not hold that registration.</strong> The cabling portion of any job is '
                        'carried out by ACMA registered cabling contractors that we engage and '
                        'manage.</p><p style="max-width:68ch;margin-top:16px">In practice you still deal '
                        'with one point of contact for the whole job and get testing and certification '
                        'documentation on completion. We would encourage you to ask any contractor to show '
                        'you their registration before work begins.</p>'}])
            + faq_block(FAQS)
            + related([       ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast')])
            + cta('Tired of three suppliers blaming each other?', 'One number covers phones, cabling and connectivity — and the fault stops being your project to manage.'),
}

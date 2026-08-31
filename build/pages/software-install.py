from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Can you install our business software on new machines?',
        "Yes. bcom ICT installs and configures business applications consistently across machines, handles licensing and activation, and records what's licensed to whom in an asset register you "
        'keep. New machines can be imaged and delivered ready to use.'),
    (   "We don't know what software licences we have. Can you help?",
        "Yes, and it's a common starting point. An audit establishes what's installed, what's licensed, what's being paid for and used, and what's being paid for and not. It frequently pays for "
        'itself in cancelled subscriptions.'),
    (   'An update broke our software. Can you fix it?',
        'Usually. Windows feature updates commonly break drivers, printers and older business applications. The fix is often rolling back a specific component rather than the whole update — and '
        "where an application is genuinely incompatible, we'll tell you what your real options are."),
    ('Do you supply software licences?', "We can source business licensing, or work with what you buy directly. Either is fine, and we'll tell you when you're on a tier above what you need.")]

PAGE = {
    "path": '/software-installation-configuration-gold-coast',
    "priority": '0.65',
    "title": 'Business Software Installation & Configuration Gold Coast | bcom ICT',
    "description": 'Business software installed, licensed and configured across the Gold Coast — deployed consistently, activated properly and documented so licensing stays under control.',
    "hero_img": 'hero-bg-software-installation.webp',
    "hero_alt": 'Business software being installed and configured by bcom ICT on the Gold Coast',
    "h1": 'Software installed and actually working',
    "lede": 'Deployed consistently across machines, licensed properly, and recorded — so nobody discovers a renewal by being locked out of it.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Consistent deployment', 'Licensing recorded', 'Activation handled', 'Documented'],
    "crumbs": [('Services', '/services'), ('Business Computer Repair', '/on-site-computer-repair-gold-coast'), ('Software Installation', '/software-installation-configuration-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT installs, licenses and configures business software across the Gold Coast — deploying consistently across machines, handling activation, and recording licences in an asset register so renewals and entitlements stay visible. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Every machine is slightly different',
                                         None,
                                         'Installed ad hoc over years, different versions, different '
                                         'settings. Then a fault affects one person and nobody can work '
                                         "out why — because their machine isn't like anyone else's."),
                                 (       "Nobody knows what's licensed",
                                         None,
                                         'Renewals arrive as a surprise, or worse, someone is locked out '
                                         "mid-job. An asset register recording what's licensed to whom "
                                         'removes both.'),
                                 (       'Paying for what nobody uses',
                                         None,
                                         'Subscriptions for departed staff, duplicate tools doing the same '
                                         "job, licence tiers well above what's needed. Reviewing this "
                                         'frequently pays for the work.'),
                                 (       'Updates break things',
                                         None,
                                         'An update to one application breaks another, or a '
                                         'line-of-business tool stops working after a Windows feature '
                                         'update. Predictable, and manageable if someone is watching.')],
                'cols': 2,
                'eyebrow': 'What goes wrong',
                'h2': 'Four recurring software problems',
                'icon': False},
        {       'h2': 'What we do',
                'ticks': [       'Install and configure business applications consistently across machines '
                                 'rather than one at a time',
                                 'Handle licensing and activation, including transfers when hardware is '
                                 'replaced',
                                 "Record what's licensed to whom, with renewal dates, in an asset register "
                                 'you keep',
                                 'Review subscriptions for duplication and licences nobody uses',
                                 'Set up new starters with the same software their role needs, rather than '
                                 'working it out each time',
                                 'Test line-of-business applications after major updates rather than '
                                 'waiting for someone to report a fault']}])
            + faq_block(FAQS)
            + related([       ('Business Computer Repair', '/on-site-computer-repair-gold-coast'),
        ('Windows & macOS Repair', '/os-troubleshooting-repair-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('Software Recommendations', '/software-recommendations-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta("Not sure what you're paying for?", 'A licensing review usually finds subscriptions nobody uses — often enough to cover the work itself.'),
}

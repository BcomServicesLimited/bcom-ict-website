from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Can a Windows installation be repaired without losing data?',
        'In most cases yes. bcom ICT attempts an in-place repair first for boot failures, failed updates and corrupted profiles, which is faster and keeps everything intact. Where the installation '
        'is too damaged to repair reliably, a clean rebuild is done with data, settings, email profiles, printers and licensed applications migrated across. Call 07 3041 8993.'),
    (   'A Windows update broke our software. Can you fix it?',
        'Usually. Feature updates commonly break drivers, printers and older business applications. The fix is often rolling back a specific component rather than the whole update, and where a '
        "line-of-business application is genuinely incompatible we'll tell you what your options actually are."),
    ('Do you support macOS as well as Windows?', 'Yes, both. Business Macs get the same treatment — boot problems, failed upgrades, profile issues and migrations.'),
    ('How long does a rebuild take?', "Typically most of a day including data migration and reinstalling applications. We'll leave a loan machine if somebody can't be without one for that long."),
    (   'Is it worth repairing an older machine?',
        "Depends on the machine. If it's under about four years old and otherwise sound, usually yes. Beyond that, the honest conversation is often about replacement — see hardware procurement and "
        'setup, or a fleet assessment if several machines are at that point.'),
    ('Do you fix home computers?', 'No. bcom ICT works on business machines only.')]

PAGE = {
    "path": '/os-troubleshooting-repair-gold-coast',
    "priority": '0.75',
    "service": 'Windows & macOS Repair Gold Coast',
    "title": 'Windows & macOS Repair Gold Coast — Business | bcom ICT',
    "description": 'Operating system troubleshooting and repair for Gold Coast business machines. Boot failures, crashes, profile corruption and failed updates fixed on site. Call 07 3041 8993.',
    "hero_img": 'hero-bg-hardware-software-troubleshooting.webp',
    "hero_alt": 'Windows repair being carried out on a business machine by bcom ICT',
    "h1": 'When the operating system is the problem',
    "lede": 'Boot failures, crashes, corrupted profiles and updates that broke more than they fixed — repaired on site, with your data and settings carried across.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Windows & macOS', 'Data migrated, not lost', 'Repaired on site', 'Business machines only'],
    "crumbs": [('Services', '/services'), ('Business Computer Repair', '/on-site-computer-repair-gold-coast'), ('Windows & macOS Repair', '/os-troubleshooting-repair-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT repairs Windows and macOS faults on business machines across the Gold Coast — boot failures, crashes, corrupted user profiles, failed updates and licensing problems — repairing in place where possible and performing a clean rebuild with data and settings migrated where it is not. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       "It won't boot",
                                         None,
                                         'Recovery loops, blue screens on startup, or a machine that '
                                         'reaches the login screen and goes no further. Often repairable '
                                         'without losing anything.'),
                                 (       'An update broke it',
                                         None,
                                         'A Windows feature update or a macOS upgrade that left drivers, '
                                         'printers or a business application non-functional. Very common '
                                         'and usually fixable.'),
                                 (       'A user profile is corrupted',
                                         None,
                                         'Someone logs in to a blank desktop with none of their settings. '
                                         'Frustrating, alarming, and generally recoverable.'),
                                 (       'It crashes at random',
                                         None,
                                         'Blue screens and unexplained restarts. Sometimes the operating '
                                         'system, often the hardware underneath it — testing tells you '
                                         'which.'),
                                 (       'Licensing and activation',
                                         None,
                                         'Windows deactivating after a hardware change, or Office refusing '
                                         'to activate. Tedious rather than difficult.'),
                                 (       "It's slower after every update",
                                         None,
                                         "Accumulated software, insufficient memory for what's now being "
                                         'run, or a drive that is quietly failing.')],
                'cols': 3,
                'eyebrow': 'Common faults',
                'h2': "What we're usually called about"},
        {       'h2': 'Repair in place, or clean rebuild',
                'html': '<p style="max-width:68ch">Most operating system faults can be repaired without '
                        'wiping the machine, and that is always the first thing we try — it is faster and '
                        'nothing gets lost.</p><p style="max-width:68ch;margin-top:16px">Where the '
                        'installation is too damaged to repair reliably, a clean rebuild is the honest '
                        'answer. That means data, settings, printers, mapped drives, email profiles and '
                        'licensed applications carried across, and the machine handed back configured '
                        'rather than handed back blank. A rebuild that leaves someone spending two days '
                        'reconstructing their setup is not a completed job.</p>'},
        {       'h2': 'What we carry across on a rebuild',
                'ticks': [       'Documents, desktop and downloads — everything the user actually had',
                                 'Email profiles, signatures and locally stored mail',
                                 'Mapped network drives and printers, reconnected and tested',
                                 'Licensed applications reinstalled and reactivated',
                                 'Browser bookmarks and saved settings',
                                 "Windows updates fully applied before handback, so the first day isn't "
                                 'spent restarting']}])
            + faq_block(FAQS)
            + related([       ('Business Computer Repair', '/on-site-computer-repair-gold-coast'),
        ('Troubleshooting', '/hardware-software-troubleshooting-gold-coast'),
        ('Performance Optimisation', '/performance-optimisation-gold-coast'),
        ('Software Installation & Config', '/software-installation-configuration-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('Business IT Support', '/it-support-and-services-gold-coast')])
            + cta("Machine won't start properly?", "We'll try to repair it in place first — and if a rebuild is needed, you get it back configured rather than blank."),
}

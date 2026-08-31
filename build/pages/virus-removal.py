from layout import cta, faq_block, related, svc_body

FAQS = [   (   'How do you remove a virus from a business computer?',
        'bcom ICT isolates the affected machines first, identifies what the infection is, establishes what accounts and files were reached, then cleans or rebuilds the machines and resets exposed '
        'credentials. The job ends with hardening the route that allowed it, because removal alone usually leads to reinfection. Call 07 3041 8993.'),
    (   'What should we do the moment we notice?',
        'Disconnect the machine from the network but do not power it off — shutting down destroys evidence in memory. Do not delete the ransom note or the suspicious email, and do not wipe and '
        'rebuild. Change passwords from a device you know is clean, not from the affected one, and call 07 3041 8993.'),
    (   'Will we lose data?',
        'Usually not from a standard malware infection. Ransomware is different — recovery then depends entirely on whether your backups were separated from the network and have actually been '
        'tested. That is decided long before the incident.'),
    (   "How do we know it's really gone?",
        'Because we establish what it was and what it did, rather than running a scan until it reports clean. Where a clean removal cannot be assured, the honest answer is to rebuild the machine, '
        'and we will say so rather than hand back something we are not confident in.'),
    (   'Is this the same as incident response?',
        'No. Malware removal deals with infected machines. If accounts were compromised, data may have left the business, or multiple systems are affected, that is cyber incident response — '
        'containment, forensic investigation, recovery and reporting for your insurer and regulators.'),
    (   'How do we stop it happening again?',
        'Multi-factor authentication everywhere, patching that actually happens, and backups held where an infection cannot reach them. Those three are Essential Eight controls and they account for '
        'most of the difference. An assessment tells you which you are missing.')]

PAGE = {
    "path": '/virus-and-malware-removal-services-gold-coast',
    "priority": '0.8',
    "service": 'Virus & Malware Removal Gold Coast',
    "title": 'Virus & Malware Removal Gold Coast — Business | bcom ICT',
    "description": "Virus, ransomware and malware removal for Gold Coast business computers. Full clean-up, credential reset and security hardening so it doesn't happen again. Call 07 3041 8993.",
    "hero_img": 'hero-bg-network-security.webp',
    "hero_alt": 'Malware removal and system hardening being carried out by bcom ICT for a Gold Coast business',
    "h1": 'Removing it is the easy part',
    "lede": 'Cleaning the machine is straightforward. Working out what was reached, resetting what was exposed and closing the way in is the part that matters.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Credentials reset', 'Hardened afterwards', 'Evidence preserved', 'Digital assistant after hours'],
    "crumbs": [('Services', '/services'), ('Cybersecurity', '/cybersecurity-services-gold-coast'), ('Virus & Malware Removal', '/virus-and-malware-removal-services-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT removes viruses, malware and ransomware from Gold Coast business computers — scanning and cleaning the affected machines, resetting exposed credentials, establishing what was accessed, and hardening the environment so the same route is closed. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       "Disconnect, don't shut down",
                                         None,
                                         'Unplug the network cable or turn off WiFi to stop it spreading. '
                                         'Do not power the machine off — shutting down destroys evidence '
                                         'held in memory that helps establish what was actually accessed.'),
                                 (       "Don't delete anything",
                                         None,
                                         'Not the ransom note, not the suspicious email, not the '
                                         'unfamiliar files. That is the evidence, and you may need it for '
                                         'your insurer or a regulatory assessment.'),
                                 (       "Don't wipe and rebuild",
                                         None,
                                         'It is the instinctive reaction and it removes the only record of '
                                         'what happened. Isolate the machine and call instead.'),
                                 (       'Change passwords from a clean device',
                                         None,
                                         'Not from the affected machine. If something is capturing '
                                         'keystrokes, resetting a password on that machine simply hands '
                                         'over the new one.')],
                'cols': 2,
                'eyebrow': 'Before you do anything',
                'h2': "If you think it's happening right now",
                'icon': False,
                'sub': 'What you do in the first ten minutes changes what can be recovered and what can be '
                       'established afterwards.'},
        {       'h2': 'What we actually do',
                'ticks': [       '<strong>Contain it</strong> — isolate affected machines before anything '
                                 'else, so it stops spreading',
                                 '<strong>Identify what it is</strong>, because ransomware, an information '
                                 'stealer and adware all require different responses',
                                 '<strong>Establish what was reached</strong> — which accounts, which '
                                 'files, whether anything left the building',
                                 '<strong>Clean the machines</strong>, or rebuild them where a clean '
                                 'removal cannot be assured',
                                 '<strong>Reset exposed credentials</strong>, including the saved browser '
                                 'passwords people forget they have',
                                 '<strong>Close the way in</strong> — the missing patch, the account '
                                 'without MFA, the exposed remote access',
                                 '<strong>Tell you plainly</strong> what happened and what your '
                                 'obligations may be']},
        {       'h2': 'Removal without hardening is a temporary fix',
                'html': '<p style="max-width:68ch">A machine cleaned and handed back with nothing else '
                        'changed will very often be reinfected, because the route in is still open. '
                        'Whatever let it happen — an account without multi-factor authentication, an '
                        'unpatched application, remote access published to the internet, a staff member '
                        'who could not tell the email was fake — is still there.</p><p '
                        'style="max-width:68ch;margin-top:16px">So the job ends with hardening rather than '
                        'with a clean scan. If personal information may have been accessed, your business '
                        'may also have obligations under <a '
                        'href="/notifiable-data-breach-guide-australia">the Notifiable Data Breaches '
                        'scheme</a>, and for anything beyond a single infected machine you are into <a '
                        'href="/cyber-incident-response-gold-coast">incident response</a> rather than '
                        'malware removal.</p>'}])
            + faq_block(FAQS)
            + related([       ('Cyber Incident Response', '/cyber-incident-response-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Data Backup & Disaster Recovery', '/data-backup-recovery-gold-coast'),
        ('Notifiable Data Breaches guide', '/notifiable-data-breach-guide-australia'),
        ("What to do when you've been hacked", '/what-to-do-when-hacked')])
            + cta('Call 07 3041 8993', "Open 8am–5pm Mon–Fri. Disconnect the machine from the network but leave it running — and don't delete anything."),
}

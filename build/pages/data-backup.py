from layout import cta, faq_block, related, svc_body

FAQS = [   (   'How often should a business test its backups?',
        'Restores should be tested on a schedule and the result recorded — quarterly is a reasonable baseline for most small businesses, and more often for systems the business cannot trade without. '
        'A backup job reporting success only proves it wrote data; it does not prove the data is usable. bcom ICT schedules and documents restore testing as part of managed backup.'),
    (   "Do we need backup if we're on Microsoft 365?",
        'Yes. Microsoft guarantees the platform stays available; it does not protect your data from deletion, ransomware encrypting synced files, or a departing staff member clearing a library. '
        'Retention windows are short and unforgiving. Separate Microsoft 365 backup is a genuine requirement.'),
    (   'Where is our backup data stored?',
        'Australian-hosted backup is available and is what we recommend for most clients. The location for your data is agreed and recorded in your agreement rather than left vague — see our data '
        'handling and sovereignty page.'),
    (   "What's the difference between backup and disaster recovery?",
        'Backup is copies of your data. Disaster recovery is the plan for getting the business trading again — which systems come back in what order, how long each takes, and how much data you '
        'accept losing. Most businesses have the first and not the second.'),
    (   'Would our backups survive ransomware?',
        'Only if they are separated from the network the ransomware reaches. That is the whole question, and it is the first thing we check. A backup drive plugged into a server, or a NAS on the '
        'same network with the same credentials, generally does not survive.'),
    (   'How much data would we lose in a failure?',
        'That is your recovery point objective, and it should be a decision rather than an accident. Nightly backup means up to a day; more frequent replication reduces it at higher cost. We agree '
        'the number with you rather than defaulting to whatever the software does.')]

PAGE = {
    "path": '/data-backup-recovery-gold-coast',
    "priority": '0.8',
    "service": 'Data Backup & Disaster Recovery Gold Coast',
    "title": 'Business Data Backup & Disaster Recovery Gold Coast | bcom ICT',
    "description": 'Backup and disaster recovery for Gold Coast businesses. Automated cloud and local backup, restores tested on a schedule, documented recovery times and insurance-ready reports. Call 07 3041 8993.',
    "hero_img": 'hero-bg-data-backup-recovery.webp',
    "hero_alt": 'Backup and disaster recovery systems configured by bcom ICT for a Gold Coast business',
    "h1": 'Backups that have actually been restored',
    "lede": 'Most businesses have a backup. Far fewer have proof it works — and that difference decides whether ransomware is a bad fortnight or the end of the business.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Restores tested on schedule', 'Separated from your network', 'Australian hosting available', 'Documented recovery times'],
    "crumbs": [('Services', '/services'), ('Data Backup & Recovery', '/data-backup-recovery-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT designs, implements and monitors backup and disaster recovery for Gold Coast businesses — automated cloud and local backup, restores tested on a schedule rather than assumed, documented recovery times, and reports suitable for an insurer after an incident. Australian-hosted backup is available. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Nobody has tested a restore',
                                         None,
                                         'The single most common finding. A backup job reporting success '
                                         'proves it wrote something, not that you can get your business '
                                         'back from it. The first real test being during an actual '
                                         'incident is how businesses discover the backup was corrupt for '
                                         'eight months.'),
                                 (       'The backup is reachable from the network',
                                         None,
                                         'If ransomware can walk from an infected workstation to your '
                                         'backup drive or NAS, it will. Backups that sit on the same '
                                         'network as everything else get encrypted along with everything '
                                         'else.'),
                                 (       'Nobody knows how long recovery takes',
                                         None,
                                         '"We have backups" is not a plan. How many hours to get trading '
                                         'again? Which systems come back first? Without an answer, the '
                                         'decision about whether to pay a ransom gets made under pressure '
                                         'and in the dark.'),
                                 (       'Cloud is assumed to be backed up',
                                         None,
                                         'Microsoft 365 and Google Workspace protect the platform, not '
                                         'your data. Deleted mailboxes, encrypted OneDrive files and '
                                         'emptied SharePoint libraries are your problem, and the retention '
                                         'windows are short.')],
                'cols': 2,
                'eyebrow': 'The gap',
                'h2': 'Having a backup and having a recovery are different things',
                'icon': False,
                'sub': 'Almost every business we assess has a backup running. The problems are always in '
                       'the same four places.'},
        {       'h2': 'What we put in place',
                'ticks': [       '<strong>Automated backup</strong> of servers, workstations and cloud '
                                 'tenancies — Microsoft 365 included, because it is not covered by default',
                                 '<strong>Separation</strong> so an infection on your network cannot reach '
                                 'the backup copies',
                                 '<strong>Scheduled restore testing</strong>, with the result recorded — '
                                 'this is the part that turns a backup into a recovery',
                                 '<strong>Documented recovery objectives</strong>: how much data you could '
                                 'lose and how long you would be down, agreed in advance rather than '
                                 'discovered',
                                 '<strong>Australian-hosted options</strong> where data residency matters, '
                                 'with the location written into your agreement',
                                 '<strong>Monitoring</strong>, so a failed job is noticed the next morning '
                                 'rather than the next crisis']},
        {       'h2': 'After an incident',
                'html': '<p style="max-width:68ch">If something does happen, what your insurer and — where '
                        'personal information is involved — the regulator will want is a factual account: '
                        'what was affected, what was recoverable, when it was restored. Backups with '
                        'documented testing produce that account. Backups nobody monitored produce an '
                        'argument.</p><p style="max-width:68ch;margin-top:16px">This is also what '
                        'determines whether paying a ransom is even a question. Businesses with separated, '
                        'tested backups usually recover without engaging the attacker at all — see <a '
                        'href="/cyber-incident-response-gold-coast">cyber incident response</a> and <a '
                        'href="/ransomware-reporting-australia">ransomware reporting obligations</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Cyber Incident Response', '/cyber-incident-response-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Data handling & sovereignty', '/data-handling-and-sovereignty'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('When did you last restore from a backup?', 'If the answer is "never" or "not sure", that\'s the thing to fix this month. We\'ll test it and tell you where you stand.'),
}

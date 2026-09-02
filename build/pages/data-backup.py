from layout import cta, faq_block, related, svc_body, issues, example, price_table

COMMON_ISSUES = [
    ("“The backup says it succeeded every night”",
     "the job wrote data. That is all a success message proves — not that the data is complete, consistent, or restorable.",
     "Run an actual restore. It is the only test that means anything, and it is the single most common thing nobody has ever done."),
    ("“We back up to a drive plugged into the server”",
     "a backup ransomware can reach from inside the network, using the same credentials. It will be encrypted alongside everything else.",
     "Move to a target that is separated — different credentials, and not permanently mounted where an infected machine can write to it."),
    ("“We’re in the cloud so we’re backed up”",
     "a misunderstanding of what Microsoft and Google actually guarantee. They protect the platform, not your data from deletion or encryption.",
     "Add proper Microsoft 365 or Google Workspace backup. Retention windows in those platforms are short, and they do expire."),
    ("“We don’t know how long recovery would take”",
     "no recovery time objective was ever agreed — backups were set up as a task rather than as part of a plan.",
     "Agree how much data you can afford to lose and how long you can afford to be down, then design backwards from those two numbers."),
    ("“A file from last quarter is gone”",
     "retention set too short, or a backup rotation overwriting older copies faster than anyone realised.",
     "Check every retention stage before concluding it is unrecoverable. Then set retention to match how long your business actually needs to look back."),
    ("“Nobody checks whether it ran”",
     "backup monitoring that emails a report nobody reads, or alerts to an address belonging to someone who left.",
     "Put failures in front of someone who will act, and verify the alerting works by deliberately failing a job."),
]

EXAMPLE_1 = example(
    "The restore that took four days instead of four hours",
    "A Gold Coast business lost a server to a hardware failure. They had backups, had been paying for them for years, and expected to be trading the next morning.",
    "The backup was complete but stored offsite with an upload-optimised, download-throttled connection. Restoring the full data set would take four days at the available speed. Nobody had ever calculated the recovery time, only the backup time.",
    "Recovered the business-critical subset first to get them trading, then restored the remainder in the background over the following days. Afterwards, redesigned the arrangement with a local copy for speed and an offsite copy for safety.",
    "They trade again within a day now rather than four. The lesson was that a backup is not a recovery until someone has worked out how long the recovery takes.")

EXAMPLE_2 = example(
    "Ransomware that reached the backups too",
    "A Gold Coast business was hit with ransomware overnight. Files across the server were encrypted, and so was the NAS the backups were written to.",
    "The NAS was permanently mapped and used the same administrator credentials as the server. Anything with those credentials could write to it, which is exactly what the ransomware did. There was no separated copy of any kind.",
    "Recovered what could be recovered from a handful of individual machines and cloud-synced folders. Rebuilt the rest. Then implemented separated backup with distinct credentials, an immutable retention window, and scheduled restore testing.",
    "The recovery was painful and incomplete, and it did not need to be. Separated backups would have made it a bad week rather than a permanent loss — which is why we now check for this before anything else when taking on a client.")

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

PRICING = [
    ('Automatic cloud backup', '$10', '+ GST, per user per month',
     [
      'Runs on its own, without anyone remembering to start it',
      'Held away from your network, where ransomware cannot reach it',
      'Restores tested rather than assumed to work',
      'Monitored &mdash; we know when a backup fails, and so do you',
     ]),
]

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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>Why backups fail when you need them</h2>
      <p>Almost every business we assess has a backup. Far fewer have a recovery.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What happens when a backup is actually tested</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>How much does business data backup cost?</h2>
      <p>Per user per month for cloud backup. Server and infrastructure backup is quoted on recovery targets.</p>
    </div>
    {price_table(PRICING, note='Per-user cloud backup covers mailboxes, files and the data your staff work on day to day. Servers, line-of-business databases and on-premises infrastructure are quoted separately, because the volume of data and how quickly you need it back are what drive that number. The question that sets the price is never how much data you hold. It is how long the business can afford to be without it.')}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([('Synology NAS', '/synology-nas-gold-coast'),
        ('NAS vs cloud backup', '/nas-vs-cloud-backup'),
               ('Cyber Incident Response', '/cyber-incident-response-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Data handling & sovereignty', '/data-handling-and-sovereignty'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('When did you last restore from a backup?', 'If the answer is "never" or "not sure", that\'s the thing to fix this month. We\'ll test it and tell you where you stand.'),
}

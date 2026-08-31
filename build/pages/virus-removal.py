from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("“The antivirus caught something — are we fine?”",
     "a detection, not necessarily a resolution. Nobody asks how it arrived or what it did in the window before detection.",
     "Establish the entry point and check for persistence — accounts, scheduled tasks, mailbox rules, startup entries. Cleaning without closing the route is why businesses get hit twice in a month."),
    ("“The machine is slow and pops up ads”",
     "adware or a browser hijack rather than anything more serious. Annoying, low risk, and usually bundled with something a user installed.",
     "Remove it, then look at how it got there. If software is being installed without approval, that is the actual finding — and it means something worse could arrive the same way."),
    ("“Files have odd extensions and there’s a note”",
     "ransomware, mid or post encryption. This is not a malware removal job any more.",
     "Stop. Disconnect from the network, do not power off, do not delete the note. Call us — this moves to incident response, where evidence and recovery matter more than cleaning."),
    ("“It keeps coming back after we clean it”",
     "persistence that was never removed, or reinfection through the same open route — an unpatched application, an account without MFA, exposed remote access.",
     "Find the persistence and the entry route rather than running the scan again. Repeat infection is a symptom of an incomplete first response."),
    ("“Our emails are being flagged as spam by clients”",
     "your domain or IP may be sending mail you do not know about, usually from a compromised mailbox.",
     "Check for compromise before assuming it is a reputation problem. Then fix SPF, DKIM and DMARC so nobody can send as you, and request delisting once the source is closed."),
    ("“Should we just wipe and rebuild it?”",
     "the instinct after any infection. Sometimes right, and often premature.",
     "Rebuild where a clean removal cannot be assured — but not before evidence is preserved and data is off. Wiping first destroys the record of what was accessed, which may determine your obligations."),
]

EXAMPLE_1 = example(
    "Cleaned three times by someone else",
    "A Gold Coast business had the same machine cleaned by their previous provider three times in two months. Each time it came back clean; each time the infection returned within a fortnight.",
    "The malware was being removed correctly, but the route in was never closed — an unpatched application with a known vulnerability, plus a local administrator account with a password shared across every machine in the office.",
    "Removed the infection, patched the application, ended the shared local administrator practice, and checked every other machine for the same exposure — two others were already infected without symptoms.",
    "It stopped recurring. The billable cycle of clean-and-return had been treating the symptom for two months, which is exactly the incentive problem managed IT removes.")

EXAMPLE_2 = example(
    "An infection that turned out to be a breach",
    "A Gold Coast practice reported a machine behaving oddly and asked for a virus clean.",
    "Not commodity malware. An information stealer had harvested saved browser credentials weeks earlier, and one of those credentials had been used to sign into the practice’s Microsoft 365 from overseas. A mailbox rule was quietly forwarding correspondence out.",
    "Contained immediately, removed the forwarding rule, reset every credential from clean devices, revoked all sessions, and established from the logs what had been accessed and over what period — which is the question that decides a notification.",
    "What was booked as a virus clean was a notifiable-breach assessment. The practice could answer what was accessed because logging happened to be adequate, which is not always the case.")

EXAMPLE_3 = example(
    "Adware that was the least of it",
    "A Gold Coast business called about pop-ups on a reception machine — irritating rather than alarming, and assumed to be a simple clean.",
    "The adware was trivial. What sat alongside it was a remote access tool installed the same day through the same bundled download, giving someone outside the business an unattended path onto the machine. It had been there five weeks.",
    "Removed both, checked every other machine for the same tool, reset credentials that had been entered on the affected machine, and reviewed logs for activity during the five-week window.",
    "The pop-ups were the visible symptom of something considerably worse. This is why we establish how something arrived rather than just removing what was reported.")

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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What people describe, and what it usually is</h2>
      <p>The gap between the two is why removal alone is rarely the whole job.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>When a clean-up turns out to be something else</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Cyber Incident Response', '/cyber-incident-response-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Data Backup & Disaster Recovery', '/data-backup-recovery-gold-coast'),
        ('Notifiable Data Breaches guide', '/notifiable-data-breach-guide-australia'),
        ("What to do when you've been hacked", '/what-to-do-when-hacked')])
            + cta('Call 07 3041 8993', "Open 8am–5pm Mon–Fri. Disconnect the machine from the network but leave it running — and don't delete anything."),
}

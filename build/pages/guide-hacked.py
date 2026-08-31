from layout import cta, faq_block, related, svc_body

FAQS = [   (   "What should a business do first when it's been hacked?",
        'Disconnect affected machines from the network but do not switch them off — powering down destroys evidence in memory that establishes what was accessed. Then change your email password from '
        "a device you know is clean, check for mailbox forwarding rules you didn't create, and call your IT provider and your bank. Write down what you saw and when. Call bcom ICT on 07 3041 8993, "
        'answered 24/7.'),
    (   "Why shouldn't we turn the computer off?",
        "Because memory holds evidence of what actually ran and what was reached, and it's lost on shutdown. That evidence determines whether personal information was accessed, which determines "
        "whether you have to notify anyone. Without it you may have to notify on the assumption of the worst, because you can't prove otherwise."),
    (   'Should we pay a ransom?',
        "That's a legal and commercial decision requiring advice, not an IT decision. Paying doesn't guarantee a working decryption key, doesn't stop stolen data being published, and there are "
        'separate legal risks depending on who is being paid. Australia also has mandatory reporting obligations for ransomware payments above a turnover threshold.'),
    (   'Do we have to tell anyone?',
        'Possibly several people. If personal information was accessed and serious harm is likely, the Notifiable Data Breaches scheme applies. Your cyber insurer almost certainly requires prompt '
        "notification. AFS licensees and health providers may have sector obligations. These are separate duties and meeting one doesn't meet the others."),
    (   "How do we know they're really out?",
        'Because someone establishes how they got in and removes the persistence they left behind — accounts, scheduled tasks, mailbox rules, backdoors. Skipping that step is why businesses get hit '
        'twice in a month. A clean antivirus scan is not the same as being sure.'),
    ("Can you help if we're not your client?", "Yes. bcom ICT takes incident calls from any business, and a significant share come from businesses we've never worked with. Phones are answered 24/7.")]

PAGE = {
    "path": '/what-to-do-when-hacked',
    "priority": '0.75',
    "article": True,
    "title": 'Hacked? What To Do in the First 60 Minutes | bcom ICT',
    "description": 'An emergency guide for Australian business owners. The steps that protect your business in the first hour after a breach, in order — and the ones that destroy evidence.',
    "hero_kind": 'doc',
    "eyebrow": "Guide",
    "h1": 'Hacked? Do these things, in this order',
    "lede": 'Panic wastes the hour. A sequence uses it. Every step below assumes the one before it is done.',
    "crumbs": [("Guides", "/services"), ('Hacked? First 60 minutes', '/what-to-do-when-hacked')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='If your business has been hacked: disconnect affected machines from the network but do not switch them off, because shutting down destroys evidence held in memory. Do not delete anything or rebuild the machine. Change critical passwords from a device you know is clean, starting with email. Call your IT provider and your bank. Write down what you saw and when. Do not communicate with the attacker before taking advice. Call bcom ICT on 07 3041 8993 — answered 24/7.',
                     blocks=[       {       'h2': 'Minutes 0–5 — isolate',
                'html': '<div class="vnote" style="border-color:#E8A0A0;background:#FBEEEE"><strong>Do '
                        'this first</strong><p><strong>Unplug the network cable or turn off WiFi on '
                        'affected machines. Do NOT power them off.</strong> Shutting down wipes memory '
                        'that holds the evidence of what actually ran and what was accessed — which is '
                        'what determines your obligations later.</p></div><p '
                        'style="max-width:68ch;margin-top:16px">If several machines are affected, or you '
                        "can't tell which are, disconnect the internet at the router. Losing connectivity "
                        "for an hour is recoverable. Letting it spread for an hour often isn't.</p>"},
        {       'h2': 'Minutes 5–20 — stop the access',
                'ticks': [       '<strong>Change your email password first</strong>, from a phone or a '
                                 'machine you know is clean — never from the affected computer.',
                                 'Then banking, then anything sharing that password. Assume every account '
                                 'with a reused password is exposed.',
                                 "<strong>Check for mailbox forwarding rules you didn't create.</strong> "
                                 'This is how attackers keep reading after you change the password, and '
                                 'almost nobody thinks to look.',
                                 'Sign out all sessions in Microsoft 365 or Google Workspace, which '
                                 'invalidates tokens a password change alone leaves active.',
                                 "Turn on multi-factor authentication if it isn't already. Yes, during the "
                                 'incident — it stops them getting back in.']},
        {       'cols': 3,
                'h2': 'Minutes 20–40 — call the right people',
                'steps': [       (       'Your IT provider',
                                         'Call rather than email — if the mailbox is compromised, an email '
                                         'announcing the breach goes straight to the attacker. bcom ICT '
                                         "answers 24/7 on 07 3041 8993, including for businesses we've "
                                         'never worked with.'),
                                 (       'Your bank',
                                         'If any financial account or payment detail may be involved, or '
                                         'money has moved. Banks can sometimes stop or recall a transfer '
                                         'if you reach them fast enough.'),
                                 (       'Your insurer',
                                         'Cyber policies usually require prompt notification, and many '
                                         'require it before you engage anyone. Late notice is a common '
                                         'reason claims get reduced.')]},
        {       'h2': 'Minutes 40–60 — write it down',
                'ticks': [       'What you saw, and the exact time you saw it. Screenshots of anything '
                                 'unusual, taken with your phone.',
                                 "Who was logged in, on what machine, and what they'd been doing.",
                                 'Any unusual emails in the days before — particularly anything about '
                                 'changed bank details or an unexpected login prompt.',
                                 "What you've already done, and when. This becomes the timeline your "
                                 'insurer and, potentially, a regulator will want.',
                                 '<strong>Do not delete anything</strong>, including the ransom note, the '
                                 'suspicious email or unfamiliar files.']},
        {       'cards': [       (       "Don't power off or rebuild",
                                         None,
                                         'The strongest instinct and the most damaging. It destroys the '
                                         'record of what happened, which you need to establish what was '
                                         'accessed — and therefore whether you must notify anyone.'),
                                 (       "Don't pay before taking advice",
                                         None,
                                         'There are separate legal risks around who is being paid, and '
                                         'Australia has mandatory reporting obligations for ransomware '
                                         "payments above a turnover threshold. That's a decision for your "
                                         'lawyer, not a decision made at 2am.'),
                                 (       "Don't email about it internally",
                                         None,
                                         "If a mailbox is compromised, you're briefing the attacker. Use "
                                         'phone or a messaging app until you know which accounts are '
                                         'clean.'),
                                 (       "Don't assume it's over",
                                         None,
                                         'Removal without closing the way in usually means it happens '
                                         'again. The account without MFA, the unpatched application, the '
                                         'exposed remote access — all still there unless someone deals '
                                         'with them.')],
                'cols': 2,
                'h2': 'What not to do',
                'icon': False},
        {       'h2': 'Afterwards: what you may have to report',
                'html': '<p style="max-width:68ch">A single incident can trigger several separate '
                        'obligations, and satisfying one does not satisfy the others:</p><ul class="ticks" '
                        'style="margin-top:16px"><li><a '
                        'href="/notifiable-data-breach-guide-australia">Notifiable Data Breaches '
                        'scheme</a> — if personal information was accessed and serious harm is '
                        'likely.</li><li><a href="/ransomware-reporting-australia">Ransomware payment '
                        'reporting</a> — if a payment is made and you are above the turnover '
                        'threshold.</li><li>Your cyber insurer, usually promptly.</li><li>Sector '
                        'regulators — AFS licensees and health providers in particular.</li></ul><p '
                        'style="max-width:68ch;margin-top:16px">We provide the factual technical account '
                        'you need for all of them. The notification decisions remain yours — see <a '
                        'href="/cyber-incident-response-gold-coast">incident response</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Cyber Incident Response', '/cyber-incident-response-gold-coast'),
        ('Notifiable Data Breaches guide', '/notifiable-data-breach-guide-australia'),
        ('Ransomware payment reporting', '/ransomware-reporting-australia'),
        ('Virus & Malware Removal', '/virus-and-malware-removal-services-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('24/7 Security Operations Centre', '/security-operations-centre-gold-coast')])
            + cta('Call 07 3041 8993', "Answered 24/7, including for businesses we've never worked with. Disconnect from the network — but leave the machine on."),
}

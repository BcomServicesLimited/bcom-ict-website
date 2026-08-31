from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We turned the machine off straight away&rdquo;",
     "an instinct to stop the harm, which also destroys volatile evidence that helps establish what was actually taken.",
     "Disconnect from the network instead &mdash; unplug the cable or switch off the wireless. That stops the spread while preserving what is needed to work out the scope."),
    ("&ldquo;We wiped it and started fresh&rdquo;",
     "an understandable urge to be rid of it. It also removes any ability to determine what was accessed, which is precisely what your insurer and any regulator will ask.",
     "Preserve the machine until the scope is established. Rebuilding is usually part of the answer and it belongs after the investigation rather than instead of it."),
    ("&ldquo;We replied to the attacker&rdquo;",
     "a reasonable-seeming attempt to understand or negotiate. It confirms the account is live and being read, and it is a decision with legal dimensions.",
     "Do not engage before you have legal advice. There are separate obligations around payment and around dealing with sanctioned entities, and they are not IT questions."),
    ("&ldquo;We changed the password, so it&rsquo;s handled&rdquo;",
     "a necessary step and rarely a sufficient one. Attackers commonly leave forwarding rules, additional sign-in methods or authorised applications that survive a password change.",
     "Revoke active sessions, check for forwarding rules and review authorised applications as well. The forwarding rule is the part most often missed, and it is how they come back."),
    ("&ldquo;No personal information was involved&rdquo;",
     "an assessment made quickly and often wrongly. Mailboxes contain far more personal information than people remember putting in them.",
     "Establish what was actually reachable before concluding anything. Whether the Notifiable Data Breaches scheme applies depends on that, and getting it wrong is its own problem."),
    ("&ldquo;We&rsquo;ll tell the insurer once we know more&rdquo;",
     "a sensible-sounding delay that frequently breaches the policy. Most cyber policies require prompt notification and some require it before you engage anyone.",
     "Notify early, even with an incomplete picture. Late notice is one of the more common reasons a claim is reduced or refused, and the notification is not an admission of anything."),
]

EXAMPLE_1 = example(
    "The forwarding rule that survived the password change",
    "A business discovered a compromised mailbox, reset the password immediately, and considered the matter closed. Two weeks later the same mailbox sent a fraudulent invoice to a client.",
    "The password change had been correct and insufficient. The attacker had created an inbox rule forwarding a copy of everything to an external address and quietly deleting the forwarded messages from the sent items, and had registered an additional sign-in method against the account. Both survived the password reset. The attacker had continued reading the mailbox throughout the fortnight the business believed it was secure.",
    "Revoked every active session, removed the forwarding rule and the additional sign-in method, audited every other mailbox in the business for the same artefacts &mdash; which found one more &mdash; and enforced multi-factor authentication across the tenancy.",
    "Access was genuinely ended, two weeks later than the business thought. A password change alone leaves an attacker in place more often than not, and the business had done what it reasonably believed was the fix.")

EXAMPLE_2 = example(
    "Two days of trying, and what it cost",
    "A business called about ransomware two days after discovering it. In the intervening period staff had powered affected machines off and on repeatedly, run a disk repair utility, and deleted the ransom note because it was distressing to look at.",
    "The repeated restarts and the repair utility had damaged data that was recoverable when the encryption was first noticed. The deleted note contained the identifier needed to establish which variant was involved, which affects whether a decryption tool exists. The business had also replied to the attacker&rsquo;s email address before taking any advice, confirming the mailbox was monitored.",
    "Recovered what remained from backup, established the scope from what evidence survived, and produced the factual technical account the business&rsquo;s insurer and lawyer required &mdash; including, honestly, what could no longer be determined.",
    "Most systems were restored. The two days of well-intentioned effort had cost recoverable data and narrowed the options, which is why the order of the steps on this page matters more than the speed of them.")

FAQS = [   (   "What should a business do first when it's been hacked?",
        'Disconnect affected machines from the network but do not switch them off — powering down destroys evidence in memory that establishes what was accessed. Then change your email password from '
        "a device you know is clean, check for mailbox forwarding rules you didn't create, and call your IT provider and your bank. Write down what you saw and when. Call bcom ICT on 07 3041 8993, "
        'returned in business hours.'),
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
    ("Can you help if we're not your client?", "Yes. bcom ICT takes incident calls from any business, and a significant share come from businesses we've never worked with. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time.")]

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
    "body": svc_body(answer='If your business has been hacked: disconnect affected machines from the network but do not switch them off, because shutting down destroys evidence held in memory. Do not delete anything or rebuild the machine. Change critical passwords from a device you know is clean, starting with email. Call your IT provider and your bank. Write down what you saw and when. Do not communicate with the attacker before taking advice. Call bcom ICT on 07 3041 8993 — returned in business hours.',
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
                                         "is on 07 3041 8993, open 8am to 5pm Monday to Friday, including for businesses we've "
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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What people do first, and what it costs</h2>
      <p>Six instincts that are entirely reasonable and make the situation worse.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in practice</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Cyber Incident Response', '/cyber-incident-response-gold-coast'),
        ('Notifiable Data Breaches guide', '/notifiable-data-breach-guide-australia'),
        ('Ransomware payment reporting', '/ransomware-reporting-australia'),
        ('Virus & Malware Removal', '/virus-and-malware-removal-services-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('24/7 Security Operations Centre', '/security-operations-centre-gold-coast')])
            + cta('Call 07 3041 8993', "Open 8am–5pm Mon–Fri, including for businesses we've never worked with. Disconnect from the network — but leave the machine on."),
}

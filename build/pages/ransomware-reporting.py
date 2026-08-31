from layout import MARK, cta, faq_block, ticks, related, trust_note, verify_note

FAQS = [
    ("Does an Australian business have to report a ransomware payment?",
     "Australia introduced a mandatory ransomware payment reporting obligation under the Cyber Security Act 2024. Businesses above the turnover threshold that make a ransomware or extortion payment, or whose agent makes one on their behalf, must report it to the Australian Government within a short window after the payment. Confirm the current threshold and reporting window with the Department of Home Affairs or a lawyer before relying on this — the scheme is recent and the detail has been phased in."),
    ("Is it illegal to pay a ransom in Australia?",
     "Paying is not, in itself, prohibited for most businesses — but the reporting obligation attaches to it, and there are separate offences around dealing with sanctioned entities that can apply depending on who is being paid. That is a legal question with real consequences, not an IT question, and it needs a lawyer rather than your IT provider."),
    ("Should we pay?",
     "It's your decision and it deserves proper advice. What we'd say from the technical side: paying doesn't guarantee a working decryption key, doesn't stop your data being published or resold, and marks you as an organisation that pays. The businesses that get through this without paying are almost always the ones with backups held separately from the network and actually tested — which is a decision made long before the incident."),
    ("Who do we report to?",
     "Reporting under the Cyber Security Act goes to the Australian Government — in practice via the designated reporting channel operated by the Department of Home Affairs and the Australian Signals Directorate. Separately, you should report the incident to ReportCyber, notify your cyber insurer, and assess whether the Notifiable Data Breaches scheme also requires you to notify the OAIC and affected individuals. These are distinct obligations that can all apply to the same incident."),
    ("What does bcom ICT do in a ransomware incident?",
     "We contain it, work out how it happened and what was reached, preserve evidence, and recover your systems from backup where that is possible. We provide the factual technical account your lawyer, insurer and regulators will need. We do not advise on whether to pay and we do not make regulatory notifications on your behalf — both sit with your business and your legal advisers."),
    ("How do we avoid being in this position?",
     "Backups held where ransomware can't reach them from inside the network, with restores tested on a schedule rather than assumed. Multi-factor authentication everywhere. Patching that actually happens. Those three account for most of the difference between a bad fortnight and a business that doesn't reopen — and all three are Essential Eight controls."),
]

PAGE = {
    "path": "/ransomware-reporting-australia",
    "priority": "0.7",
    "title": "Ransomware Payment Reporting in Australia — Business Guide | bcom ICT",
    "description": "Australia's mandatory ransomware payment reporting obligation under the Cyber Security Act 2024 — who it applies to, what must be reported, and how it interacts with the NDB scheme.",
    "hero_kind": "doc",
    "eyebrow": "Trust centre · guide",
    "h1": "Ransomware payment reporting in Australia",
    "lede": "Australia now requires businesses above a turnover threshold to report ransomware payments. Here's the shape of the obligation, and how it sits alongside your other reporting duties.",
    "crumbs": [("Trust centre", "/trust-centre"), ("Ransomware reporting", "/ransomware-reporting-australia")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">Australia introduced mandatory ransomware payment reporting under the Cyber Security
    Act 2024. Businesses above the turnover threshold that make a ransomware or extortion payment must report
    it to the Australian Government within a short window after payment. This is separate from, and can apply
    alongside, obligations under the Notifiable Data Breaches scheme.</p>

    {verify_note("The turnover threshold and reporting window for this scheme have been phased in and the detail may have changed since this page was last reviewed. <strong>Confirm the current requirements with the Department of Home Affairs or a lawyer before relying on this page</strong> — particularly in a live incident. This is general information, not legal advice. Reviewed August 2026.")}

    <h2 style="margin-top:48px">Three separate obligations, one incident</h2>
    <p style="margin-top:16px">This is the part businesses most often get wrong. A single ransomware attack
    can trigger several distinct duties, and satisfying one does not satisfy the others.</p>
    {ticks([
      "<strong>Ransomware payment reporting</strong> — under the Cyber Security Act, if you make a payment and you're above the turnover threshold. Reported to the Australian Government.",
      '<strong>Notifiable data breach notification</strong> — under the Privacy Act, if personal information was accessed and serious harm is likely. Reported to the OAIC and to affected individuals. See <a href="/notifiable-data-breach-guide-australia">the NDB guide</a>.',
      "<strong>Your insurer</strong> — cyber policies almost always require prompt notification, and late notice is a common reason claims get reduced or refused.",
      "<strong>ReportCyber</strong> — the national reporting channel. Not mandatory for most businesses, but it feeds national intelligence and is usually worth doing.",
      "<strong>Sector regulators</strong> — AFS licensees, health providers and businesses under the SOCI Act may have additional obligations of their own.",
    ])}
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>Should you pay?</h2>
    <p style="margin-top:16px">It's your decision, and it needs legal advice rather than an IT opinion. What
    we can tell you is what we see technically:</p>
    {ticks([
      "Paying doesn't guarantee a decryption key that works, or works completely",
      "Paying doesn't stop stolen data being published, resold or used later",
      "Paying marks the business as one that pays, which matters for what happens next",
      "There are separate legal risks around dealing with sanctioned entities, depending on who is being paid",
      "The businesses that recover without paying are the ones whose backups were held separately from the network — a decision made months earlier, not during the incident",
    ])}
    <p style="margin-top:24px">The uncomfortable truth is that whether you have a real choice is determined
    long before the attack, by whether your backups are reachable from inside your own network.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>What we do, and what we don't</h2>
    <p style="margin-top:16px"><strong>We handle:</strong> containment, forensic investigation of how it
    happened and what was reached, evidence preservation, recovery from backup, and a factual written account
    for your lawyer, insurer and regulators. That's our
    <a href="/cyber-incident-response-gold-coast">incident response service</a>.</p>
    <p style="margin-top:16px"><strong>We don't:</strong> advise on whether to pay, negotiate with attackers,
    or make regulatory notifications for you. Those sit with your business and your legal advisers, and an IT
    provider offering to take them on is overreaching.</p>

    <div class="rule">{MARK}</div>

    <h2>Right now, if it's happening</h2>
    {ticks([
      "<strong>Call 07 3041 8993.</strong> Phones are answered 24/7.",
      "Disconnect affected machines from the network — unplug the cable or disable WiFi. Do not power them off.",
      "Do not delete the ransom note, and don't wipe or rebuild anything. That's the evidence.",
      "Don't pay or respond to the attacker before you've had legal advice.",
      "Notify your cyber insurer early. Many policies require it before you engage anyone, including us.",
    ])}
    <p style="margin-top:24px">Powering a machine off can destroy volatile evidence that helps establish what
    was actually taken. Disconnecting it from the network stops the spread while preserving that.</p>

    {trust_note('Prevention is almost entirely three Essential Eight controls: separated and tested backups, multi-factor authentication, and patching that actually happens. See <a href="/essential-eight-guide-gold-coast">Essential Eight assessment and uplift</a>.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Cyber Incident Response", "/cyber-incident-response-gold-coast"),
  ("Notifiable Data Breaches guide", "/notifiable-data-breach-guide-australia"),
  ("Essential Eight assessment", "/essential-eight-guide-gold-coast"),
  ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast"),
  ("24/7 Security Operations Centre", "/security-operations-centre-gold-coast"),
  ("What to do when you've been hacked", "/what-to-do-when-hacked"),
], heading="Related")}

{cta("Under attack right now?",
     "Call 07 3041 8993 — answered 24/7. Disconnect affected machines from the network, but don't power them off and don't delete anything.")}
''',
}

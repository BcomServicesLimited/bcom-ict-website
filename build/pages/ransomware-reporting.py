from layout import MARK, cta, faq_block, ticks, related, trust_note, verify_note, issues, example

COMMON_ISSUES = [
    ("&ldquo;Reporting the payment is the only obligation, isn&rsquo;t it?&rdquo;",
     "one obligation among several that a single incident can trigger. They are separate schemes and satisfying one does not satisfy the others.",
     "Work through each: ransomware payment reporting, notifiable data breach assessment, your insurer&rsquo;s notification requirement, and any sector regulator. They can all apply to the same event."),
    ("&ldquo;We&rsquo;re under the turnover threshold, so none of this applies&rdquo;",
     "a conclusion drawn from one scheme and applied to all of them. The payment reporting threshold has nothing to do with whether the Notifiable Data Breaches scheme applies to you.",
     "Assess each obligation on its own terms. A business below the payment reporting threshold can still have a clear duty to notify the OAIC and affected individuals."),
    ("&ldquo;Our IT provider will handle the reporting&rdquo;",
     "a misunderstanding of where the duty sits. It rests with the business, not its suppliers.",
     "Understand the division. We establish and document the technical facts &mdash; what happened, what was reached, when. The reporting decisions and the reports themselves are yours and your lawyer&rsquo;s."),
    ("&ldquo;Can we just pay quietly?&rdquo;",
     "a question that comes from wanting the problem to end. Paying is not itself prohibited for most businesses, and a reporting obligation attaches to it, along with separate risks around sanctioned entities.",
     "Take legal advice before paying anything. This is a legal question with real consequences rather than an IT decision, and it is not one your IT provider should be answering."),
    ("&ldquo;Will paying get our data back?&rdquo;",
     "not reliably. It does not guarantee a working decryption key, does not stop stolen data being published or resold, and marks the business as one that pays.",
     "The businesses that get through this without paying are almost always the ones whose backups were held where ransomware could not reach them from inside the network &mdash; a decision made months earlier, not during the incident."),
    ("&ldquo;How long do we have?&rdquo;",
     "less time than most businesses assume, and the clock starts at discovery rather than when the technical work finishes.",
     "Start the assessment immediately and in parallel with the technical response. Businesses that sequence these &mdash; fix first, assess later &mdash; frequently find a substantial part of the window has gone."),
]

EXAMPLE_1 = example(
    "Three obligations from one incident",
    "A business suffered a ransomware incident, restored from backup within two days, and considered the matter resolved. It had not paid anything and concluded there was nothing to report.",
    "The recovery was genuinely good and the conclusion was wrong on two counts. No payment meant no payment reporting obligation, which was correct. It did not address whether personal information had been accessed &mdash; and the attacker had been in the environment for eleven days before deploying the encryption, with access to file shares holding employee records and client contact details. The business&rsquo;s cyber policy also required notification within a period that had nearly elapsed while the technical recovery was under way.",
    "Established from the available evidence what had been reachable during those eleven days, documented it, and provided the factual account. Advised the business to notify its insurer immediately and to take legal advice on the Notifiable Data Breaches assessment, which it did.",
    "The insurer was notified inside the policy window with about a day to spare. The business had done the hard part well and had very nearly missed two obligations while doing it, because nobody had run the assessment in parallel with the recovery.")

EXAMPLE_2 = example(
    "Having a real choice, because of a decision made a year earlier",
    "A business was hit with ransomware across its file server and every workstation. The attackers demanded payment and had exfiltrated data before encrypting, so the threat included publication as well as loss of access.",
    "The business had backups held in a system the network could not reach with ordinary credentials, and restores had been tested twice in the preceding year. That single arrangement meant the encryption was survivable. The exfiltration was a separate and genuinely serious matter, and it was a legal and notification problem rather than a technical one.",
    "Recovered every system from backup without engaging the attackers at all, preserved evidence throughout, and produced the technical account the business&rsquo;s lawyer and insurer needed to work through the disclosure obligations.",
    "The business did not pay and did not need to consider it. Whether a business has a real choice in this situation is decided long before the attack, by whether its backups are reachable from inside its own network.")

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
      "<strong>Call 07 3041 8993.</strong> Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time.",
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

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Questions</span>
      <h2>What people actually ask when this happens</h2>
      <p>Six questions. The first two lead businesses to conclude they have no obligations when they do.</p>
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
     "Call 07 3041 8993 — returned in business hours. Disconnect affected machines from the network, but don't power them off and don't delete anything.")}
''',
}

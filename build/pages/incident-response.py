from layout import MARK, cta, faq_block, ticks, steps, related, trust_note

PHASES = [
    ("Contain", "Stop it spreading. Affected machines come off the network, compromised accounts are disabled, and attacker access is cut. Speed matters more than tidiness at this stage."),
    ("Investigate", "Establish how they got in, how long they were there, what they reached and what left the building. This is the part that determines your obligations, so guesswork isn't good enough."),
    ("Eradicate", "Remove persistence — the accounts, scheduled tasks, mailbox rules and backdoors left behind so they can return. Skipping this is why businesses get hit twice in a month."),
    ("Recover", "Restore systems from clean backups and bring the business back online in a sensible order, verifying each system before the next."),
    ("Report", "A factual written account of what happened, when, and what was affected — for your insurer, your lawyer, your board, and any regulatory notification you need to make."),
]

FIRST = [
    "<strong>Call 07 3041 8993.</strong> Answered 24/7, including weekends and public holidays.",
    "Disconnect affected machines from the network — unplug the cable or turn off WiFi.",
    "<strong>Do not power them off.</strong> Shutting down destroys evidence in memory that helps establish what was actually taken.",
    "Do not delete anything, including ransom notes, suspicious emails or unfamiliar files.",
    "Do not wipe and rebuild, however strong the urge. That is the evidence.",
    "Change passwords from a device you know is clean, not from the affected machine.",
    "Notify your cyber insurer early — many policies require it before you engage anyone.",
]

FAQS = [
    ("What is cyber incident response?",
     "Cyber incident response is the process of containing a security breach, investigating what happened, removing the attacker's access, recovering systems and documenting the incident. bcom ICT provides incident response to businesses on the Gold Coast and across Australia, including support for insurer and regulatory notifications. Call 07 3041 8993."),
    ("What should we do in the first ten minutes?",
     "Call us, and disconnect affected machines from the network without powering them off. Powering down destroys evidence held in memory that helps establish what was actually accessed. Don't delete the ransom note, don't wipe the machine, and change passwords from a device you know is clean."),
    ("Do we have to be an existing client?",
     "No. Incident response is available to any business, and a significant share of the calls we take are from businesses we've never worked with. Phones are answered 24/7."),
    ("How long does recovery take?",
     "It depends almost entirely on your backups. A business with separated, tested backups is often trading again within days. A business whose backups were reachable from the infected network — or never tested — can be looking at weeks, and sometimes at data that isn't coming back. That's decided long before the incident."),
    ("Will you tell us whether to pay a ransom?",
     "No. That's a legal and commercial decision requiring proper advice, and there are separate legal risks around who is being paid. We'll give you the technical picture — what's encrypted, what backups exist, what recovery looks like without paying — so the decision is an informed one. See our ransomware reporting guide for the obligations that attach."),
    ("Do you handle the regulatory notifications?",
     "We provide the factual technical account you need to make them. The notification obligation itself sits with your business under the Privacy Act, not with your IT provider, and any provider offering to take that on has misunderstood the law."),
    ("What does it cost?",
     "Incident response is charged for the work done, and we'll give you a scope and an estimate once we understand what we're dealing with — usually within the first few hours. If you hold cyber insurance, tell us early: many policies cover response costs and some require you to use their panel."),
]

PAGE = {
    "path": "/cyber-incident-response-gold-coast",
    "priority": "0.8",
    "service": "Cyber Incident Response Gold Coast",
    "title": "Cyber Incident Response Gold Coast — 24/7 | bcom ICT",
    "description": "Rapid cyber incident response for Gold Coast and Australian businesses — containment, forensic investigation, eradication, recovery and reporting for insurers and regulators. Call 07 3041 8993.",
    "hero_img": "hero-bg-network-security.webp",
    "hero_alt": "A bcom ICT engineer responding to a cyber security incident for an Australian business",
    "h1": "Been breached? Start here.",
    "lede": "Containment, investigation, recovery and the written account your insurer and regulators will ask for. Phones answered 24/7 — you don't need to be an existing client.",
    "actions": [("Call 07 3041 8993 now", "tel:+61730418993", "white"), ("Contact us", "/contact", "onink")],
    "trust": ["Answered 24/7", "Non-clients welcome", "Evidence preserved", "Insurer-ready reporting"],
    "crumbs": [("Services", "/services"), ("Cybersecurity", "/cybersecurity-services-gold-coast"), ("Cyber Incident Response", "/cyber-incident-response-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides rapid cyber incident response for Gold Coast and Australian businesses
    — containment, forensic investigation, eradication, recovery and written reporting, including the factual
    account needed for insurer claims and regulatory notifications. bcom ICT answers phones 24/7 and takes
    incident calls from businesses that are not existing clients. Call 07 3041 8993.</p>

    <div class="vnote" style="border-color:#E8A0A0;background:#FBEEEE">
      <strong>If it's happening right now</strong>
      <p>Call <strong>07 3041 8993</strong>. Disconnect affected machines from the network but <strong>do not
      power them off</strong> — shutting down destroys evidence in memory. Don't delete anything and don't
      rebuild the machine.</p>
    </div>

    <h2 style="margin-top:48px">The first hour</h2>
    <p style="margin-top:16px">What you do before anyone technical arrives makes a material difference to
    what can be recovered and what can be established afterwards.</p>
    {ticks(FIRST)}
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How we respond</span>
      <h2>Five phases, in order</h2>
      <p>The order isn't negotiable. Recovering before eradicating is how businesses get hit a second time inside a fortnight.</p>
    </div>
    <div class="grid grid--3">{steps(PHASES)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What determines how this ends</h2>
    <p style="margin-top:16px">By the time we're called, most of the outcome is already set. Recovery comes
    down to one thing more than any other: whether your backups were reachable from the network that got
    infected.</p>
    {ticks([
      "<strong>Separated, tested backups</strong> — usually trading again within days, no payment considered",
      "<strong>Backups on the same network</strong> — frequently encrypted along with everything else",
      "<strong>Backups never tested</strong> — the restore fails at the worst possible moment, and that is far more common than anyone expects",
      "<strong>Good logging in place</strong> — we can establish what was reached, which determines your obligations precisely rather than conservatively",
      "<strong>No logging</strong> — you may have to notify on the assumption of the worst, because you cannot prove otherwise",
    ])}
    <p style="margin-top:24px">Those are decisions made months earlier. If you're reading this and nothing
    has happened yet, that's the useful takeaway — see
    <a href="/data-backup-recovery-gold-coast">backup and disaster recovery</a>.</p>

    <div class="rule">{MARK}</div>

    <h2>Your obligations afterwards</h2>
    <p style="margin-top:16px">A single incident can trigger several separate duties. Satisfying one doesn't
    satisfy the others:</p>
    {ticks([
      '<a href="/notifiable-data-breach-guide-australia">Notifiable Data Breaches scheme</a> — if personal information was accessed and serious harm is likely',
      '<a href="/ransomware-reporting-australia">Ransomware payment reporting</a> — if a payment is made and you are above the turnover threshold',
      'Your cyber insurer — usually required promptly, and late notice is a common reason claims are reduced',
      'Sector regulators — AFS licensees, health providers and SOCI-covered businesses may have obligations of their own',
    ])}
    <p style="margin-top:24px">We provide the factual technical account. The notification decisions sit with
    your business and your legal advisers.</p>

    {trust_note('Businesses on our <a href="/security-operations-centre-gold-coast">24/7 SOC</a> are usually contained before an incident becomes a crisis — detection at 2am rather than discovery on Monday is often the whole difference.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("24/7 Security Operations Centre", "/security-operations-centre-gold-coast"),
  ("Ransomware payment reporting", "/ransomware-reporting-australia"),
  ("Notifiable Data Breaches guide", "/notifiable-data-breach-guide-australia"),
  ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast"),
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
  ("What to do when you've been hacked", "/what-to-do-when-hacked"),
])}

{cta("Call 07 3041 8993",
     "Answered 24/7, including weekends and public holidays. You don't need to be an existing client, and the first conversation costs nothing.")}
''',
}

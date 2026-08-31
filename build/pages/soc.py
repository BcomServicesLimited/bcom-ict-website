from layout import MARK, cta, faq_block, cards, ticks, related, photo, trust_note

WATCH = [
    ("Endpoints", None, "Every laptop, desktop and server. Unusual process behaviour, known malware signatures, attempts to disable protection, and the early signs of ransomware before encryption starts."),
    ("Identities", None, "Microsoft 365 and Azure sign-ins. Logins from countries you don't trade in, impossible travel, repeated failures, and mailbox rules quietly forwarding your invoices somewhere else."),
    ("Cloud tenancies", None, "Configuration changes, new admin accounts, permission escalations and sharing settings suddenly opened up. Attackers who get in often change settings before they do anything visible."),
    ("Network edge", None, "Firewall and remote access activity — where an intrusion typically starts, and where it's cheapest to stop."),
]

WHY = [
    ("Attacks don't wait for business hours", "The most common time to find an intrusion is a weekend or a public holiday, because that's when nobody is looking. A SOC removes that gap entirely."),
    ("Detection isn't the same as alerting", "Most businesses have tools that generate alerts nobody reads. A SOC is people whose job is to triage those alerts, separate noise from genuine intrusion, and act."),
    ("Containment in minutes, not Monday", "An isolated machine on Saturday night is an inconvenience. The same machine left running until Monday is often the whole network."),
    ("Evidence for afterwards", "Continuous logging means that if something does happen, you can establish what was reached and when — which is what your insurer and, potentially, a regulator will ask for."),
]

FAQS = [
    ("What is a security operations centre?",
     "A security operations centre is a continuously staffed capability that monitors an organisation's endpoints, identities, cloud services and network for signs of intrusion, investigates alerts, and contains threats. bcom ICT operates a 24/7 SOC for Australian businesses, covering day, night, weekends and public holidays. Call 07 3041 8993."),
    ("Do small businesses actually need this?",
     "Not all of them. A SOC makes sense once a breach would genuinely stop you trading, once you hold client data whose loss would be serious, or once an insurer or a larger client starts asking how you monitor for intrusion. Below that, getting the Essential Eight basics right delivers more per dollar and we'll tell you so."),
    ("Is this just software, or are there people?",
     "Both, and the distinction matters. The tooling generates signals; the value is people triaging them. Software alone produces alerts nobody reads, which is worse than nothing because it looks like coverage."),
    ("What happens when something is detected?",
     "Triage first — most alerts are benign and chasing every one would make the service useless. Genuine threats are contained, typically by isolating the affected device or disabling the compromised account, and you're notified. For confirmed incidents we move into full incident response."),
    ("Will you isolate a machine without asking us?",
     "For a clear, active threat like ransomware beginning to encrypt files, yes — we contain first and tell you immediately, because minutes matter. The rules of engagement are agreed with you when the service starts, so nobody is surprised at 2am."),
    ("Does this replace our antivirus?",
     "It includes endpoint protection rather than sitting on top of your existing product. Running two is usually counterproductive — they interfere with each other and neither works properly."),
    ("Is our data monitored from Australia?",
     "Analysts are Australian-based. Some vendor platforms underpinning the SOC process telemetry outside Australia, which we set out plainly on our data handling page rather than glossing over. If Australian-only processing is a hard requirement, tell us before we design it."),
]

PAGE = {
    "path": "/security-operations-centre-gold-coast",
    "priority": "0.8",
    "service": "24/7 Security Operations Centre (SOC)",
    "title": "24/7 Security Operations Centre for Australian Business | bcom ICT",
    "description": "24/7 monitored threat detection and response for Australian businesses. bcom ICT's SOC watches endpoints, identities and cloud tenancies continuously, investigates alerts and contains threats. Call 07 3041 8993.",
    "hero_img": "cybersecurity-assessment-hero.webp",
    "hero_alt": "A bcom ICT security analyst reviewing threat detection alerts for an Australian business client",
    "h1": "Someone watching, at 3am on a public holiday",
    "lede": "Continuous monitored threat detection and response across your endpoints, identities and cloud services — because that's when intrusions are usually found.",
    "actions": [("Talk to us", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["24/7, including holidays", "Australian analysts", "Contain then notify", "Essential Eight aligned"],
    "crumbs": [("Services", "/services"), ("Cybersecurity", "/cybersecurity-services-gold-coast"), ("Security Operations Centre", "/security-operations-centre-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT operates a 24/7 security operations centre for Australian businesses,
    monitoring endpoints, identities and cloud tenancies continuously. The bcom ICT SOC investigates alerts,
    separates noise from genuine intrusion, and contains confirmed threats — day, night, weekends and public
    holidays. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">What's watched</span>
      <h2>Four places intrusions show up</h2>
    </div>
    <div class="grid grid--2">{cards(WATCH)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why continuous</span>
      <h2>The gap a SOC actually closes</h2>
      <p>Most businesses already own security tools. What they don't have is anyone reading what those tools produce outside business hours.</p>
    </div>
    <div class="grid grid--2">{cards(WHY, icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>Do you need this yet?</h2>
        <p style="margin-top:16px">Honestly, not every business does — and we'd rather say that than sell it to someone who'd get more from spending the same money elsewhere.</p>
        <p style="margin-top:16px"><strong>A SOC makes sense when:</strong></p>
        {ticks([
          "A breach would genuinely stop you trading, not just inconvenience you",
          "You hold client data whose exposure would be serious for them and for you",
          "An insurer or a larger client has started asking how you monitor for intrusion",
          "You operate in a regulated sector — financial services, health, government supply chain",
          "You've already had an incident and don't intend to have another",
        ])}
        <p style="margin-top:24px"><strong>Start elsewhere when:</strong> you don't yet have multi-factor authentication everywhere, tested backups, and patching that actually happens. Those three stop far more than monitoring does, and they cost less. Our <a href="/essential-eight-guide-gold-coast">Essential Eight assessment</a> is the honest first step.</p>
      </div>
      {photo("cybersecurity-assessment-gold-coast.webp", "Security monitoring and threat detection carried out by bcom ICT for Australian business clients", "Tooling generates the signals. The value is people triaging them.")}
    </div>

    <div class="rule">{MARK}</div>

    <h2>When something is confirmed</h2>
    <p style="margin-top:16px">Detection is only useful if it leads somewhere. A confirmed threat moves straight into <a href="/cyber-incident-response-gold-coast">incident response</a> — containment, investigation, eradication and recovery, with the factual written account you'll need for your insurer and, if personal information was involved, for your assessment under <a href="/notifiable-data-breach-guide-australia">the Notifiable Data Breaches scheme</a>.</p>
    <p style="margin-top:16px">Rules of engagement — what we isolate without asking, who we call, and at what hour — are agreed with you before the service starts. Nobody should be working that out at 2am.</p>

    {trust_note('SOC analysts are Australian-based. Some vendor platforms underpinning the service process telemetry outside Australia — set out in full on <a href="/data-handling-and-sovereignty">data handling and sovereignty</a> rather than left vague.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Cyber Incident Response", "/cyber-incident-response-gold-coast"),
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
  ("Essential Eight assessment", "/essential-eight-guide-gold-coast"),
  ("Cybersecurity Risk Assessment", "/cybersecurity-health-check-for-small-business-gold-coast"),
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
  ("Trust centre", "/trust-centre"),
])}

{cta("Not sure whether you need a SOC?",
     "We'll tell you honestly. If the basics aren't in place yet, monitoring is the wrong thing to buy first and we'll say so.")}
''',
}

from layout import MARK, cta, faq_block, cards, ticks, related, photo, trust_note, issues, example

THREATS = [
    ("Invoice and payment scams", None,
     "Someone watches your mailbox, waits for a real invoice, then sends a near-identical one with different bank details. This is the single most common way Australian small businesses lose money, and it needs no technical skill at all."),
    ("Account takeover", None,
     "A staff password gets reused somewhere it shouldn't be, and someone logs into your Microsoft 365 as them. Multi-factor authentication stops nearly all of it, and plenty of businesses still don't have it switched on everywhere."),
    ("Ransomware", None,
     "Files encrypted, a demand for payment, and a business that can't trade. Whether it's a bad week or a fatal one comes down entirely to whether your backups are separate and actually tested."),
    ("Unpatched systems", None,
     "Known holes in software that were fixed months ago but never installed. Unglamorous, boring, and one of the most reliable ways in."),
]

WHAT = [
    ("Multi-factor authentication", None, "Turned on properly across email, remote access and admin accounts — not just for the people who volunteered."),
    ("Endpoint protection", None, "Business-grade protection on every machine, centrally monitored, so we see a problem on one device before it becomes a problem on all of them."),
    ("Email security", None, "Filtering ahead of your mailbox, plus the SPF, DKIM and DMARC records that stop somebody sending email pretending to be you."),
    ("Backup that's separated", None, "Backups a ransomware infection can't reach from inside your network, with restores tested on a schedule rather than assumed."),
    ("Firewall and network hardening", None, "Guest WiFi kept away from your business systems, remote access locked down, and the default passwords nobody ever changed sorted out."),
    ("Staff awareness", None, "Short, practical sessions on what a real scam looks like. Your people are the control that catches what the technology misses."),
]

COMMON_ISSUES = [
    ("“We got an invoice with different bank details”",
     "either a spoofed sender, or a genuinely compromised mailbox somewhere in the chain — yours, your client’s, or your supplier’s.",
     "Establish which immediately, because a compromised mailbox is still being read. Check for forwarding rules, review sign-in activity, reset credentials from a clean device, then close the gap with MFA and email authentication records."),
    ("“Someone clicked a link and entered their password”",
     "a credential harvesting page. The password is gone; the question is whether anything has been done with it yet.",
     "Reset the password and revoke all active sessions immediately — a password change alone leaves existing tokens working. Check for mailbox rules created since, then review what that account could reach."),
    ("“Our emails are going to clients’ junk folders”",
     "missing or misconfigured SPF, DKIM and DMARC records — the same records that let anyone send email pretending to be you.",
     "Publish and align all three properly. It fixes deliverability and closes a spoofing route at the same time, which is why it is worth doing even when deliverability is the only complaint."),
    ("“The antivirus says it cleaned something”",
     "a detection, not necessarily a resolution. The question nobody asks is how it arrived and what it did before detection.",
     "Establish the entry point and check for persistence — accounts, scheduled tasks, mailbox rules. Cleaning without closing the route is why businesses get hit twice in a month."),
    ("“We can’t answer our insurer’s renewal questions”",
     "no documented position on MFA coverage, patching, backup testing or endpoint protection — not necessarily an absence of controls.",
     "Assess against the ASD Essential Eight, produce a written report you can attach to the form, and close the gaps that matter most first."),
    ("“A staff member’s account was logging in from overseas”",
     "credential compromise, usually a reused password on an account without multi-factor authentication.",
     "Disable the session, reset from a clean device, audit what was accessed while the attacker had it, and check whether data left. Then enforce MFA on every account rather than most of them."),
]

EXAMPLE_1 = example(
    "A near-miss on a settlement payment",
    "A Gold Coast professional services firm received an email, apparently from a long-standing supplier, advising changed bank details ahead of a scheduled payment. The email was in an existing thread and read entirely normally.",
    "The supplier’s mailbox had been compromised weeks earlier. A forwarding rule was quietly copying correspondence out and deleting the evidence. Our client had no MFA on two mailboxes and no verbal verification process for bank detail changes.",
    "Confirmed the compromise, advised the client to verify by phone on a number already held — which stopped the payment. Then rolled MFA across every account, published SPF, DKIM and DMARC, and put a written verification rule in place for any change of payment details.",
    "The payment was not made. The firm now treats bank detail changes as a phone call rather than an email, which is the control that would have caught it regardless of the technology.")

EXAMPLE_2 = example(
    "An insurance renewal that could not be answered",
    "A Gold Coast business received a cyber insurance renewal questionnaire noticeably harder than the previous year’s — asking specifically about MFA coverage, patch cadence, backup testing and endpoint protection.",
    "Multi-factor authentication was on for the directors but not for eight other staff. Patching was happening on some machines and not others. Backups ran but had never been restored. None of it was documented, so even the parts that were fine could not be evidenced.",
    "Ran a fixed-fee health check against the Essential Eight, closed the MFA gap, standardised patching, tested a restore in front of them, and produced a written report they could attach to the renewal.",
    "The questionnaire was answered honestly rather than optimistically, and the business now has a document it can reuse when a client asks the same questions during procurement.")

FAQS = [
    ("Who provides cybersecurity services on the Gold Coast?",
     "bcom ICT provides cybersecurity services to small and medium businesses across the Gold Coast and Australia-wide, covering endpoint protection, email security, multi-factor authentication, ransomware defence and staff training. bcom ICT works to the ASD Essential Eight, the Australian government's baseline security framework. Call 07 3041 8993."),
    ("What is the Essential Eight, and does my business need it?",
     "The Essential Eight is the Australian Signals Directorate's set of eight baseline mitigation strategies, with maturity levels from zero to three. It's the framework Australian auditors, insurers and boards actually ask about — not the American ones you'll see on most security websites. Most small businesses don't need to be certified against it, but knowing where you sit is increasingly what an insurer or a larger client wants to hear."),
    ("How much does a cybersecurity assessment cost?",
     "The health check is a fixed fee agreed before we start, so there's no open-ended bill. You get a plain-English report covering your email, identity, endpoints, backups and network, with a prioritised list of what to fix first. What you do with it is up to you — there's no obligation to have us do the remediation."),
    ("We're small. Are we really a target?",
     "You're not being singled out, and that's the point. Almost all of this is automated and indiscriminate — it finds whoever is reachable, and small businesses are reachable because they're less likely to have the basics in place. Being small makes you easier, not less interesting."),
    ("Do you help with cyber insurance requirements?",
     "Yes. Insurers increasingly ask specific questions about MFA, backups, patching and endpoint protection before they'll quote or pay out. We can tell you where you currently stand against those questions and close the gaps so your answers are honest ones."),
    ("What happens if we've already been breached?",
     "Call 07 3041 8993 and don't switch anything off or delete anything — that often destroys the evidence needed to work out what happened. bcom ICT provides incident response covering containment, investigation, recovery and the reporting your insurer and regulators need."),
    ("Is bcom ICT certified to ISO 27001?",
     "No, and we won't imply otherwise. bcom ICT aligns its practices with ISO/IEC 27001:2022 and operates to the ASD Essential Eight, but the company is not certified by an accredited certification body. Individually, Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI. Our trust centre sets out exactly what we're aligned to and what we're not."),
]

PAGE = {
    "path": "/cybersecurity-services-gold-coast",
    "priority": "0.9",
    "service": "Cybersecurity Services Gold Coast",
    "title": "Cybersecurity Services Gold Coast for Business | bcom ICT",
    "description": "Cybersecurity for Gold Coast businesses — endpoint protection, email security, MFA, ransomware defence and staff training, aligned to the ASD Essential Eight. Call 07 3041 8993.",
    "hero_img": "cybersecurity-assessment-hero.webp",
    "hero_alt": "A bcom ICT consultant reviewing security posture with a Gold Coast business owner",
    "h1": "Cybersecurity for Gold Coast businesses",
    "lede": "Protection against the things that actually happen to small businesses — invoice scams, account takeovers and ransomware. Built to the Australian Essential Eight baseline.",
    "actions": [("Book a security review", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["ASD Essential Eight aligned", "24/7 monitored SOC", "Fixed-fee health check", "Local since 2011"],
    "crumbs": [("Services", "/services"), ("Cybersecurity", "/cybersecurity-services-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides cybersecurity services to small and medium businesses across the Gold
    Coast and Australia-wide — endpoint protection, email security, multi-factor authentication, ransomware
    defence, firewall hardening and staff awareness training. bcom ICT works to the ASD Essential Eight,
    Australia's baseline security framework. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">What actually happens</span>
      <h2>Four things that go wrong at Gold Coast businesses</h2>
      <p>Not hypotheticals. These are what we get called about, and none of them require anyone to be specifically targeting you.</p>
    </div>
    <div class="grid grid--2">{cards(THREATS, icon=False)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What we put in place</span>
      <h2>The controls that stop most of it</h2>
      <p>There is no single product that makes a business secure. There is a short list of unexciting things that, done properly, stop the overwhelming majority of what small businesses get hit by.</p>
    </div>
    <div class="grid grid--3">{cards(WHAT)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>Start with a health check</h2>
        <p style="margin-top:16px">Most businesses have no clear picture of where they actually stand, which makes it impossible to know what's worth spending money on. The health check fixes that first.</p>
        <p style="margin-top:16px">It's a fixed fee, agreed up front. We review your email, identity and accounts, endpoints, backups and network, then give you a plain-English report with a prioritised list — what would hurt most, what's quick to close, and what can reasonably wait.</p>
        {ticks([
          "A written report you can hand to your board, accountant or insurer",
          "Findings ranked by what they'd actually cost you, not by severity score",
          "Where you sit against the Essential Eight, and what the next level takes",
          "No obligation to have us do the remediation work",
        ])}
        <p style="margin-top:24px">For businesses that need continuous cover rather than a point-in-time review, our <a href="/security-operations-centre-gold-coast">24/7 security operations centre</a> monitors endpoints, identities and cloud tenancies around the clock.</p>
      </div>
      {photo("cybersecurity-assessment-gold-coast.webp", "A cybersecurity assessment being carried out for a Gold Coast small business", "The health check is a fixed fee, and the report is yours regardless of what you do next.")}
    </div>

    <div class="rule">{MARK}</div>

    <h2>If you're in a regulated industry</h2>
    <p style="margin-top:16px">Some Gold Coast businesses have obligations beyond good practice. Financial planners, mortgage brokers, accountants and insurance brokers operating under an AFS licence carry cyber resilience obligations that ASIC has been increasingly willing to enforce — we cover that on our <a href="/asic-cybersecurity-compliance-gold-coast">ASIC compliance page</a>. Healthcare and allied health clients typically need to demonstrate Essential Eight alignment and understand their obligations under the Notifiable Data Breaches scheme.</p>

    {trust_note('We state what we are aligned to and what we are not. bcom ICT operates to the ASD Essential Eight and aligns with ISO/IEC 27001:2022, but is <strong>not certified</strong> to it. <a href="/trust-centre">The trust centre</a> sets out the frameworks, the credentials our people hold, and who issued them.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The security calls we actually take</h2>
      <p>Not hypotheticals. These are what Gold Coast businesses ring about, and what is usually behind them.</p>
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
  ('FortiGate Firewalls', '/fortigate-firewall-gold-coast'),
  ("Cybersecurity Risk Assessment", "/cybersecurity-health-check-for-small-business-gold-coast"),
  ("24/7 Security Operations Centre", "/security-operations-centre-gold-coast"),
  ("Cyber Incident Response", "/cyber-incident-response-gold-coast"),
  ("Essential Eight Assessment & Uplift", "/essential-eight-guide-gold-coast"),
  ("ASIC Cybersecurity Compliance", "/asic-cybersecurity-compliance-gold-coast"),
  ("What to do when you've been hacked", "/what-to-do-when-hacked"),
])}

{cta("Find out where you actually stand",
     "A fixed-fee health check across your email, accounts, devices, backups and network — with a plain-English report you can act on or hand to your insurer.")}
''',
}

from layout import MARK, cta, faq_block, ticks, related, photo, trust_note, issues, example

EIGHT = [
    ("Application control", "Only approved software can run. Stops a staff member's download executing something malicious."),
    ("Patch applications", "Browsers, PDF readers, Office and the rest kept current. Known holes fixed months ago are still one of the most reliable ways in."),
    ("Configure Microsoft Office macro settings", "Macros blocked unless there's a genuine business need. A decades-old attack route that still works."),
    ("User application hardening", "Turning off the risky features nobody uses — Flash-era leftovers, unnecessary browser plugins, scripting where it isn't needed."),
    ("Restrict administrative privileges", "Day-to-day accounts don't have admin rights. If a standard account is compromised, the damage is contained."),
    ("Patch operating systems", "Windows, macOS and server operating systems kept current and off unsupported versions."),
    ("Multi-factor authentication", "The single highest-value control on the list. Stops nearly all account takeovers, and it is still not switched on everywhere at most businesses we assess."),
    ("Regular backups", "Backed up, held where an infection can't reach them, and restored on a test schedule rather than assumed to work."),
]

LEVELS = [
    ("Maturity Level 0", "Controls are not in place, or are in place so partially they don't function. More Australian small businesses sit here than would admit to it."),
    ("Maturity Level 1", "Protects against widespread, opportunistic attacks — the automated, indiscriminate kind that finds whoever is reachable. This is the realistic target for most small businesses and it stops the overwhelming majority of what actually happens."),
    ("Maturity Level 2", "Protects against attackers willing to invest more time and effort in a specific target. Appropriate where you hold sensitive client data or operate in a regulated sector."),
    ("Maturity Level 3", "Protects against adaptive, determined attackers. Genuinely demanding, and rarely the right target for a small or medium business."),
]

grid = "".join(f'<div class="commit"><h4>{i}. {t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(EIGHT, 1))
levels = "".join(f'<div class="cred cred--{"note" if i==0 else "aligned"}"><span class="cred-tag">ML{i}</span><div><h4>{t}</h4><p>{d}</p></div></div>' for i, (t, d) in enumerate(LEVELS))

COMMON_ISSUES = [
    ("“Our client says we need to be Essential Eight compliant”",
     "there is no formal certification scheme — nobody can certify you against it. What is being asked for is evidence of maturity.",
     "Assess your current level against each of the eight controls individually and produce a written report. That document is what the client actually wants."),
    ("“We think we’re already doing most of it”",
     "partial implementation, which is the norm. MFA on some accounts, patching on some machines, backups without tested restores.",
     "Measure each control separately, because maturity is per-control rather than overall. Most businesses sit unevenly and are surprised by which one is weakest."),
    ("“Application control sounds impossible for us”",
     "the reputation is deserved — it is the hardest of the eight and needs a proper picture of what staff actually run.",
     "Start with the seven that are achievable. Application control is usually the last one to attempt and should not block progress on the rest."),
    ("“We patch when we remember”",
     "no schedule and no verification, so patching is happening on the machines someone thought of.",
     "Automate it and report on coverage. Patching applications and operating systems is two of the eight, and it is where the fastest maturity gains usually are."),
    ("“We have MFA — isn’t that enough?”",
     "MFA is one control of eight, and it is often incomplete. Service accounts, admin accounts and exempted users are the usual gaps.",
     "Verify actual coverage rather than assuming, then address the exemptions. Nearly every business we assess has more exemptions than management knew about."),
    ("“What level should we be at?”",
     "no one has explained that maturity levels are a choice matched to risk rather than a ladder to climb.",
     "Recommend a target based on what you hold and who is asking. Maturity Level 1 is the realistic target for most Gold Coast businesses and stops the great majority of what actually happens."),
]

EXAMPLE_1 = example(
    "Assessed for a supply chain requirement",
    "A Gold Coast business supplying a larger organisation was told it needed to demonstrate Essential Eight alignment to stay on the panel.",
    "Assessed at Maturity Level 0 or 1 across the eight. MFA was strong, backups were running but never restored, patching was inconsistent, admin rights were on every user’s daily account, and application control had never been considered.",
    "Produced the maturity report, then prioritised by effort against risk: removed daily admin rights, automated patching, tested restores and set a schedule, and hardened Office macro settings. Application control was scoped but deferred as a later phase.",
    "Reached a defensible Level 1 across seven controls within a quarter. The written assessment satisfied the panel requirement, and the daily-admin-rights change alone materially reduced their exposure.")

EXAMPLE_2 = example(
    "The control that turned out to be missing entirely",
    "A Gold Coast professional firm believed it was in reasonable shape and asked for an assessment to confirm it before an insurance renewal.",
    "Seven controls were at a reasonable Level 1. The eighth — regular backups — was rated Level 0, not because backups were absent but because no restore had ever been tested and the backup target was reachable from the network with the same credentials as the server.",
    "Moved the backup to a separated target, ran a test restore, and set a testing schedule with results recorded. The other seven were tidied rather than rebuilt.",
    "The renewal was answered accurately. The finding that mattered was in the control the firm was most confident about, which is more common than not.")

FAQS = [
    ("What is the ASD Essential Eight?",
     "The Essential Eight is a set of eight baseline mitigation strategies published by the Australian Signals Directorate to help organisations protect against cyber attack. It covers application control, patching applications and operating systems, Office macro settings, user application hardening, restricting administrative privileges, multi-factor authentication and regular backups. Maturity is measured from Level 0 to Level 3."),
    ("What maturity level should our business be at?",
     "For most Australian small and medium businesses, Maturity Level 1 is the realistic and sensible target. It protects against the widespread, automated attacks that account for the overwhelming majority of incidents. Level 2 makes sense if you hold sensitive client data or operate in a regulated sector. Level 3 is demanding and rarely the right target for a business under a few hundred staff."),
    ("Is the Essential Eight mandatory?",
     "It's mandatory for non-corporate Commonwealth entities. For private businesses it isn't legally required — but it's increasingly what insurers, larger clients and auditors reference when they ask how you're protected, and it's the framework an Australian assessor will know. That makes it the practical baseline whether or not it binds you."),
    ("Why the Essential Eight rather than an international framework?",
     "Because it's Australian, it's free, and it's what people here actually ask about. Most security content online is American and talks about NIST or CIS, which are fine frameworks that your Australian insurer's questionnaire will not mention. The Essential Eight is also far more achievable for a small business than an ISO certification programme."),
    ("How long does it take to reach Maturity Level 1?",
     "For a typical small business with reasonable systems already, a few months of steady work. Multi-factor authentication and backups usually move fastest and deliver the most. Application control is normally the slowest, because it needs a proper picture of what your staff actually run before anything is restricted."),
    ("What does an Essential Eight assessment involve?",
     "We review your environment against all eight controls, establish your current maturity level for each, and give you a written report in plain English with a prioritised plan. You get the report regardless of whether you have us do the remediation work."),
    ("Does bcom ICT certify us against the Essential Eight?",
     "No, and nobody can — the Essential Eight has no formal certification scheme. What we provide is an assessment and a written report of where you sit, which is what insurers and clients asking the question actually want to see. We're equally clear about our own position: bcom ICT operates to the Essential Eight and aligns with ISO/IEC 27001, but holds no organisational certification."),
]

PAGE = {
    "path": "/essential-eight-guide-gold-coast",
    "priority": "0.8",
    "service": "Essential Eight Assessment & Uplift",
    "title": "Essential Eight Assessment & Uplift | bcom ICT",
    "description": "ASD Essential Eight assessment and uplift for Australian businesses. bcom ICT measures your current maturity level. Call 07 3041 8993.",
    "hero_img": "hero-bg-network-security.webp",
    "hero_alt": "A bcom ICT consultant assessing a Gold Coast business against the ASD Essential Eight",
    "h1": "The Essential Eight, and where your business actually sits",
    "lede": "Australia's baseline security framework — the eight controls, the four maturity levels, and an honest assessment of which ones you have.",
    "actions": [("Book an assessment", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Australian baseline", "Plain-English report", "Fixed fee", "Report is yours to keep"],
    "crumbs": [("Services", "/services"), ("Cybersecurity", "/cybersecurity-services-gold-coast"), ("Essential Eight", "/essential-eight-guide-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">The ASD Essential Eight is the Australian Signals Directorate's set of eight baseline
    mitigation strategies, with maturity measured from Level 0 to Level 3. bcom ICT assesses Australian
    businesses against all eight controls, reports the current maturity level in plain English, and
    implements the controls needed to reach the level a client or insurer expects. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">The controls</span>
      <h2>All eight, in plain English</h2>
      <p>Ranked roughly by what they'll do for a typical small business, not by the order the ASD lists them.</p>
    </div>
    {f'<div class="commits">{grid}</div>'}
    <p style="margin-top:8px">If you only ever do three of these: multi-factor authentication, tested
    backups, and patching. Between them they stop most of what we actually get called about.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Maturity levels</span>
      <h2>How far up do you need to go?</h2>
      <p>Each control is measured separately, so a business can sit at Level 2 for backups and Level 0 for application control — and most do sit unevenly.</p>
    </div>
    <div class="credlist">{levels}</div>
    <p style="margin-top:8px"><strong>Level 1 is the honest target for most Gold Coast businesses.</strong>
    Anyone selling a small business a Level 3 programme is selling something it doesn't need.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>What an assessment gives you</h2>
        <p style="margin-top:16px">A fixed fee, agreed before we start, and a written report you keep whatever you decide to do next.</p>
        {ticks([
          "Your current maturity level against each of the eight controls, individually",
          "What's missing, in plain English rather than control identifiers",
          "A prioritised plan — what to fix first, what's quick, what can wait",
          "Rough costs against each item so you can budget rather than guess",
          "A document you can hand to an insurer, a board, or a client asking the question",
          "No obligation to have us do the remediation",
        ])}
        <p style="margin-top:24px">Businesses usually come to us for this because an insurer's renewal questionnaire got harder, or a larger client started asking about their supply chain. Both are good reasons, and both need a document rather than an assurance.</p>
      </div>
      {photo("cybersecurity-assessment-gold-coast.webp", "An Essential Eight maturity assessment being carried out for a Gold Coast business", "Each control is assessed separately — most businesses sit unevenly across the eight.")}
    </div>

    <div class="rule">{MARK}</div>

    <h2>Why this rather than an international framework</h2>
    <p style="margin-top:16px">Most security content you'll find online is American, and it talks about NIST
    and CIS. They're perfectly good frameworks — they're just not what your Australian insurer's
    questionnaire asks about, or what an Australian auditor will reference.</p>
    <p style="margin-top:16px">The Essential Eight is Australian, free to work against, measurable in
    maturity levels rather than pass/fail, and far more achievable for a small business than an ISO
    certification programme. If you have a limited security budget, moving up an Essential Eight level is
    almost always the better use of it — see <a href="/iso-alignment">ISO alignment</a> for where the
    standards fit alongside it.</p>

    {trust_note('There is no formal certification against the Essential Eight — nobody can certify you and anyone claiming to is overstating. What exists is assessment and evidence of maturity, which is what the people asking actually want.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What businesses actually ask about the Essential Eight</h2>
      <p>Six recurring conversations, and the answers are usually less daunting than expected.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What an assessment turns up</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
  ("Cybersecurity Risk Assessment", "/cybersecurity-health-check-for-small-business-gold-coast"),
  ("24/7 Security Operations Centre", "/security-operations-centre-gold-coast"),
  ("ASIC Cybersecurity Compliance", "/asic-cybersecurity-compliance-gold-coast"),
  ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast"),
  ("ISO alignment", "/iso-alignment"),
])}

{cta("Find out which level you're actually at",
     "A fixed-fee assessment against all eight controls, with a plain-English report you keep whatever you decide to do next.")}
''',
}

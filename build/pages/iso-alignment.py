from layout import MARK, cta, faq_block, creds, ticks, related, trust_note

STANDARDS = [
    ("ISO/IEC 27001:2022", "Information security management",
     "The one clients and tenders name. bcom ICT operates an information security management system built around it — asset inventory, access control, supplier management, incident handling and documented review.",
     "Aligned. Not certified."),
    ("ISO/IEC 20000-1:2018", "IT service management",
     "The ISO standard ITIL practices map into. For a managed service provider this describes how we deliver better than 27001 does: service catalogue, service levels, incident and problem management, change control.",
     "Aligned. Not certified."),
    ("ISO/IEC 42001:2023", "AI management systems",
     "Governance for AI systems — policy, risk assessment, acceptable use, human oversight and audit evidence. This is the one where we have a formally certified individual rather than just familiarity.",
     "Aligned. Ollie holds Lead Implementer certification, issued by BSI."),
    ("ISO 22301", "Business continuity",
     "Underpins how we design backup, disaster recovery and incident response — recovery objectives agreed in advance, restores tested rather than assumed, and a documented plan rather than an intention.",
     "Aligned. Not certified."),
    ("ISO/IEC 27017 & 27018", "Cloud security and cloud privacy",
     "Referenced when we design Microsoft 365 and Azure environments, particularly around tenant configuration, data residency and handling personal information in cloud services.",
     "Referenced. Not a programme we run."),
]

rows = "".join(
    f'<tr><td class="slot"><strong>{s}</strong><br><span style="color:var(--slate);font-size:.875rem">{n}</span></td>'
    f'<td>{d}</td><td><strong>{st}</strong></td></tr>' for s, n, d, st in STANDARDS)

FAQS = [
    ("Is bcom ICT certified to ISO 27001?",
     "No. bcom ICT operates an information security management system aligned to ISO/IEC 27001:2022, but has not been audited or certified by an accredited certification body. In Australia those bodies are accredited by JAS-ANZ. Alignment means the controls are operated and documented; certification means an independent auditor has verified them. bcom ICT will not describe itself as ISO certified, ISO accredited or ISO compliant."),
    ("What's the practical difference between aligned and certified?",
     "Alignment is our word for it. Certification is somebody else's. If your procurement process requires evidence from an accredited auditor, alignment won't satisfy it and we'll tell you that at the first conversation. If what you need is a provider that actually operates the controls and can show you the documentation, alignment is the substance and certification is the receipt."),
    ("Why aren't you certified?",
     "Certification is a significant ongoing cost for a business our size, and for most of our clients it wouldn't change the service they receive. We've chosen to spend that money on the controls rather than the audit. If enough client demand makes certification worthwhile we'll pursue it, and we'd say so here before claiming it."),
    ("Ollie is ISO 42001 certified — doesn't that make the company certified?",
     "No, and conflating those is the most common way IT providers overstate their position. Ollie holds a personal Lead Implementer certification issued by BSI, which means Ollie has been assessed as competent to implement an AI management system. It says nothing about whether bcom ICT as an organisation has been audited. We keep those claims separate everywhere on this site and in our schema markup."),
    ("Can we see your policies?",
     "Yes, on request and under NDA where the content is sensitive. Information security policy, access control, incident response and supplier management are the ones usually asked for during a procurement process."),
    ("Which framework matters most for an Australian business?",
     "The ASD Essential Eight, generally. It's the baseline Australian auditors, insurers and boards actually reference, it's free to work against, and it's far more achievable for a small business than ISO certification. Most of our clients get more value from moving up an Essential Eight maturity level than from anything ISO-related."),
]

PAGE = {
    "path": "/iso-alignment",
    "priority": "0.75",
    "title": "ISO Alignment — What We're Aligned To, and What We're Not | bcom ICT",
    "description": "bcom ICT aligns with ISO/IEC 27001, 20000-1, 42001 and 22301 but holds no organisational ISO certification. The distinction, set out in full.",
    "hero_kind": "doc",
    "eyebrow": "Trust centre",
    "h1": "ISO alignment, stated honestly",
    "lede": "bcom ICT is not ISO certified. Here is exactly what we do operate, what the word 'aligned' means, and where we stop short of a claim we can't evidence.",
    "crumbs": [("Trust centre", "/trust-centre"), ("ISO alignment", "/iso-alignment")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT holds no organisational ISO certification. bcom ICT operates practices aligned
    to ISO/IEC 27001:2022, ISO/IEC 20000-1:2018 and ISO 22301, and delivers AI work under an ISO/IEC
    42001-aligned framework. Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI —
    an individual credential, not an organisational one.</p>

    <h2 style="margin-top:56px">Aligned is not certified</h2>
    <p style="margin-top:16px">An organisation is <strong>certified</strong> to an ISO standard when an
    accredited certification body has audited it and issued a certificate. In Australia those bodies are
    accredited by JAS-ANZ. Everything short of that is <strong>alignment</strong>: operating and documenting
    the practices a standard describes, without an independent auditor verifying them.</p>
    <p style="margin-top:16px">The distinction matters for two reasons. Practically, if your procurement
    process requires certified suppliers, alignment won't satisfy it — better you know that now than at the
    end of a tender. Legally, implying a certification you don't hold is misleading conduct under Australian
    Consumer Law.</p>
    <p style="margin-top:16px">So bcom ICT does not describe itself as ISO certified, ISO accredited or ISO
    compliant, and if you ever see those words used about us, they're wrong and we'd like to know where you
    saw them.</p>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The standards</span>
      <h2>What we work to, and our status against each</h2>
    </div>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Standard</th><th>How we use it</th><th>Status</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>What ISO 27001 alignment actually involves here</h2>
    <p style="margin-top:16px">"Aligned" can mean anything from a genuine management system to a downloaded
    policy nobody reads. Ours means the following are in place, documented and reviewed:</p>
    {ticks([
      "An asset inventory covering the systems and tooling we use to reach client environments",
      "Named individual access with multi-factor authentication enforced — no shared logins",
      "Access reviewed on staff change and revoked the day someone leaves",
      "Client credentials held in a dedicated password management platform",
      "A documented incident response process, including our obligations to notify affected clients",
      "Supplier and subcontractor management, covering the cabling contractors and vendor platforms we engage",
      "Backup and recovery for our own systems, with restores tested rather than assumed",
      "Periodic internal review, with findings recorded and actioned",
    ])}
    <p style="margin-top:24px">Policies are available on request, under NDA where the content is sensitive.
    Procurement teams usually ask for the information security, access control and incident response ones.</p>

    <div class="rule">{MARK}</div>

    <h2>Where the Essential Eight fits</h2>
    <p style="margin-top:16px">For most Australian small and medium businesses, the ASD Essential Eight is
    more useful than anything ISO-related. It's the baseline Australian auditors, insurers and boards
    actually reference, it costs nothing to work against, and progress is measurable in maturity levels
    rather than a pass/fail audit.</p>
    <p style="margin-top:16px">We operate client environments against it and can assess where you currently
    sit — see <a href="/essential-eight-guide-gold-coast">Essential Eight assessment and uplift</a>. If
    you're weighing up where to spend a limited security budget, that's almost always the better first
    question.</p>

    {trust_note('AI work is delivered under an ISO/IEC 42001-aligned governance framework — policy, risk assessment, acceptable-use controls, human oversight and audit evidence. See <a href="/iso-42001-ai-governance-gold-coast">ISO/IEC 42001 AI governance</a>.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Trust centre", "/trust-centre"),
  ("Published service levels", "/service-levels-and-security"),
  ("How we work — ITIL 4", "/how-we-work-itil"),
  ("Essential Eight assessment", "/essential-eight-guide-gold-coast"),
  ("ISO/IEC 42001 AI governance", "/iso-42001-ai-governance-gold-coast"),
  ("Data handling & sovereignty", "/data-handling-and-sovereignty"),
], heading="Related")}

{cta("Need our policies for a procurement process?",
     "Tell us which ones and we'll send them, under NDA where the content is sensitive.")}
''',
}

from layout import MARK, cta, faq_block, creds, related, trust_note

CREDS = [
    ("ITIL 4 Foundation — Royce Clark", "Individual certification in IT service management. Underwrites how bcom ICT runs incidents, requests, changes and service levels.", "held"),
    ("ISO/IEC 42001:2023 Lead Implementer — Ollie", "Individual certification in AI management systems, issued by BSI. Rare in Australian IT, and the basis for how bcom ICT governs AI work.", "held"),
    ("Professional indemnity, cyber liability and public liability insurance", "All three held. Certificates of currency available on request — larger clients and insurance brokers usually ask, and we'd rather you didn't have to chase it.", "held"),
    ("National police checks and Queensland Blue Cards", "Held by technicians attending client sites. Relevant to healthcare, education and childcare clients where screening is a hard requirement.", "held"),
    ("Microsoft Partner", "bcom ICT is a Microsoft partner and deploys Microsoft 365 and Azure for clients across Australia.", "held"),
    ("ASD Essential Eight", "The Australian baseline. bcom ICT operates client environments against the Essential Eight and can assess and report maturity levels.", "aligned"),
    ("ISO/IEC 27001:2022 — information security", "bcom ICT operates an information security management system aligned to ISO/IEC 27001:2022. <strong>bcom ICT is not certified to ISO/IEC 27001.</strong> Alignment means the controls are operated and documented; it does not mean an accredited body has audited them.", "aligned"),
    ("ISO/IEC 20000-1:2018 — service management", "Service delivery practices align with ISO/IEC 20000-1. Not certified.", "aligned"),
    ("ISO 22301 — business continuity", "Backup, disaster recovery and incident response work is aligned to ISO 22301 principles. Not certified.", "aligned"),
    ("Cabling", "Fixed cabling connected to the telecommunications network legally requires a registered cabler in Australia. bcom ICT does not hold that registration — cabling is carried out by ACMA registered cabling contractors that bcom ICT engages and manages, with testing and certification documentation provided on completion.", "note"),
]

DOCS = [
    ("Service levels", "/service-levels-and-security", "Our published priority matrix, response targets, escalation path and what happens to your data if you leave."),
    ("ISO alignment", "/iso-alignment", "Which standards we work to, what alignment means, and exactly where we stop short of a certification claim."),
    ("How we work — ITIL 4", "/how-we-work-itil", "Service desk, incidents, requests, problems, change control and continual improvement, in plain English."),
    ("Data handling and sovereignty", "/data-handling-and-sovereignty", "What data we hold, where it lives, who can reach it, and how long we keep it."),
    ("Onboarding — the first 30 days", "/onboarding-first-30-days", "Exactly what happens when a business moves to us, step by step."),
    ("Notifiable Data Breaches", "/notifiable-data-breach-guide-australia", "Your obligations under the NDB scheme, and what bcom ICT does and doesn't do in a notification."),
    ("Ransomware payment reporting", "/ransomware-reporting-australia", "Australia's mandatory reporting obligations if a business makes a ransomware payment."),
    ("Essential Eight", "/essential-eight-guide-gold-coast", "The Australian security baseline explained, and how we assess and lift maturity."),
]

FAQS = [
    ("Is bcom ICT ISO certified?",
     "No. bcom ICT aligns its practices with ISO/IEC 27001:2022, ISO/IEC 20000-1:2018 and ISO 22301, but the company holds no organisational ISO certification from an accredited certification body. Individually, Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI, and Royce holds ITIL 4 Foundation. Those are personal credentials, not company certifications, and bcom ICT does not present them as such."),
    ("Why publish this at all if you're not certified?",
     "Because the question gets asked and a vague answer costs trust. Most small IT providers either claim more than they hold or say nothing. Setting out plainly what is held, what is aligned, and where the line sits means a buyer, an insurer or an auditor can check us properly rather than take our word for it."),
    ("Do you carry insurance?",
     "Yes — professional indemnity, cyber liability and public liability. Certificates of currency are available on request. Larger clients and insurance brokers routinely ask for these before engaging a provider."),
    ("Who actually does the work?",
     "bcom ICT's own team, with two exceptions we're explicit about. Fixed cabling is carried out by ACMA registered cabling contractors, because it's a licensed trade in Australia. Some specialist security tooling behind our SOC is delivered with vendor platforms. Everything else is us."),
    ("What happens to our documentation if we leave?",
     "You get it. Asset register, network documentation, licences, credentials and configuration details are handed over on exit. We treat a clean exit as part of the service — a provider who makes leaving painful is telling you something about how confident they are in the rest."),
    ("Are you audited by anyone?",
     "Not currently. Alignment work is internal and documented, but no accredited body has audited bcom ICT against ISO 27001. If a client's procurement process requires certified suppliers, we'll tell you that up front rather than let you discover it in a tender."),
]

PAGE = {
    "path": "/trust-centre",
    "priority": "0.85",
    "title": "Trust Centre — Standards, Credentials & Insurance | bcom ICT",
    "description": "What bcom ICT is certified to, what we align to, and where the line sits. Credentials, insurance, service levels, data handling and Australian compliance.",
    "hero_kind": "doc",
    "eyebrow": "Trust centre",
    "h1": "What we're certified to, what we're aligned to, and where the line is",
    "lede": "Most IT providers either claim more than they hold or say nothing at all. This is the full picture for bcom ICT — held credentials, framework alignment, insurance and published commitments.",
    "crumbs": [("Trust centre", "/trust-centre")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT holds no organisational ISO certification. bcom ICT operates an information
    security management system aligned to ISO/IEC 27001:2022 and works to the ASD Essential Eight and ITIL 4,
    with individual certifications held by its people — ITIL 4 Foundation and ISO/IEC 42001:2023 Lead
    Implementer, issued by BSI. Professional indemnity, cyber liability and public liability insurance are
    held.</p>

    <h2 style="margin-top:56px">Held, aligned, and the difference</h2>
    <p style="margin-top:16px">These two words get used interchangeably across the IT industry and they mean
    very different things. <strong>Held</strong> means a credential exists, issued by a named body, and can be
    verified. <strong>Aligned</strong> means we operate and document the practices a standard describes, but
    no accredited auditor has checked us against it.</p>
    <p style="margin-top:16px">Under Australian Consumer Law, implying a certification you don't hold is
    misleading conduct. It's also the fastest way to lose a tender when someone asks for the certificate. So
    the list below is split, and it stays split.</p>

    {creds(CREDS)}

    <p>If your procurement process requires suppliers certified to ISO 27001, we're not currently that
    supplier and we'll say so at the first conversation rather than at the end of a bid.</p>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The detail</span>
      <h2>Everything set out in full</h2>
      <p>The marketing pages stay in plain English. This is where the detail lives, for the people who need it — buyers comparing providers, insurers, auditors and accountants.</p>
    </div>
    <div class="doclinks">
      {"".join(f'<a class="doclink" href="{h}"><h4>{t} {MARK}</h4><p>{d}</p></a>' for t, h, d in DOCS)}
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Why this page exists</h2>
    <p style="margin-top:16px">We run the same disciplines a large IT department runs — documented, monitored,
    and measured against real standards. We just run them at a size that suits a business with eight staff,
    and we explain them in English.</p>
    <p style="margin-top:16px">That claim is easy to make and hard to prove, which is what this section of the
    site is for. Everything above is checkable: the credentials name their issuing bodies, the insurance
    certificates are available on request, and the <a href="/service-levels-and-security">service levels</a>
    are published rather than negotiated privately per client.</p>
    <p style="margin-top:16px">bcom ICT is the trading name of Bcom Services Pty Ltd, ABN 92 636 893 108,
    trading on the Gold Coast since 2011. The ABN is
    <a href="https://abr.business.gov.au/ABN/View?abn=92636893108" rel="nofollow">publicly verifiable</a>.</p>

    {trust_note("Something here out of date, or a claim you think we cannot support? Tell us and we will correct it. Every page in this section carries a review date, and the compliance guides are checked against their sources before that date is bumped.")}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Published service levels", "/service-levels-and-security"),
  ("ISO alignment in detail", "/iso-alignment"),
  ("How we work — ITIL 4", "/how-we-work-itil"),
  ("Data handling & sovereignty", "/data-handling-and-sovereignty"),
  ("About bcom ICT", "/about"),
  ("Our team", "/our-team"),
], heading="Related")}

{cta("Questions we haven't answered here?",
     "If you're evaluating providers and need something specific — a certificate, a policy, a reference — ask and we'll send it.")}
''',
}

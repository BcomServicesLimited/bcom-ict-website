from layout import MARK, cta, faq_block, ticks, steps, related, trust_note

WEEKS = [
    ("Week 1 — we find out what you've got",
     "A technician walks the site and we run discovery across your network. Every device, server, licence, subscription, warranty and supplier gets recorded. Most businesses moving to us have none of this written down anywhere, and that gap is exactly what hurts when a provider disappears or a key person leaves."),
    ("Week 1 — the honest report",
     "You get a plain-English document: what's healthy, what's at risk, what's out of support, and what we'd fix in what order. It includes the things that are fine, because a report that lists only problems is a sales document, not an assessment."),
    ("Week 2 — we close the urgent gaps",
     "Missing or untested backups, accounts without multi-factor authentication, unsupported operating systems, expired warranties on things you can't trade without. These come first regardless of what else is planned, because they're the ones that turn into a bad month."),
    ("Weeks 2–3 — monitoring and access go live",
     "Monitoring agents are deployed, alerting is tuned to your environment, and your team gets our number and email. From this point faults start reaching us before you report them."),
    ("Week 4 — handover and first review",
     "We walk you through the documentation, confirm the priority list for the next quarter, and agree what's budgeted. You hold a copy of everything from this point on."),
]

FROM_PROVIDER = [
    "We'll deal with your outgoing provider directly if you'd rather not — handovers are often awkward and it isn't your job to manage that.",
    "We ask them for credentials, documentation and licence details, and we tell you plainly what we did and didn't receive.",
    "Where nothing is handed over, we rebuild the documentation from discovery. It takes longer but it isn't a blocker.",
    "Domain names, DNS and Microsoft 365 tenancy ownership get verified as yours, not the provider's. This is the single most common thing we find registered to someone else.",
    "Nothing is switched off until the replacement is verified working.",
]

FAQS = [
    ("How long does it take to move IT providers?",
     "Most businesses are fully onboarded with bcom ICT within 30 days. Week one is discovery and reporting, week two closes urgent gaps, weeks two to three deploy monitoring and support access, and week four is handover and the first review. Larger or less documented environments take longer, mostly in discovery. Call 07 3041 8993."),
    ("Will there be downtime while we switch?",
     "There shouldn't be. Onboarding is mostly discovery, documentation and adding monitoring, none of which interrupts anyone. Where a genuine change is needed — replacing an unsupported system, reconfiguring a firewall — it's scheduled with you and done outside business hours."),
    ("What if our current provider won't hand anything over?",
     "It happens more than it should. We ask properly first, and if nothing comes we rebuild the documentation from discovery instead. It takes longer and we'll tell you what we couldn't recover, but it doesn't stop the move. The one thing worth checking early is whether your domain and Microsoft 365 tenancy are actually registered to your business rather than to them."),
    ("Do we have to commit before onboarding?",
     "The initial review is free and yours to keep, including if you decide not to proceed. If you do go ahead, managed agreements are month-to-month — there's no minimum term to sign before we've demonstrated anything."),
    ("What do you need from us during onboarding?",
     "Access to the site, whatever documentation exists, a contact who knows how the business actually works day to day, and around an hour of that person's time in week one. That's genuinely it — the rest is our work."),
    ("What happens after the first 30 days?",
     "Managed clients move into the normal rhythm: monitoring and helpdesk day to day, patching and backup checks on schedule, and periodic service reviews covering what broke, what's ageing and what to budget for. The onboarding report becomes the baseline those reviews measure against."),
]

PAGE = {
    "path": "/onboarding-first-30-days",
    "priority": "0.75",
    "title": "Switching IT Providers — What the First 30 Days Look Like | bcom ICT",
    "description": "Exactly what happens when a business moves to bcom ICT: discovery, an honest report, closing urgent gaps, monitoring going live and full handover — typically within 30 days.",
    "hero_kind": "doc",
    "eyebrow": "Trust centre",
    "h1": "What actually happens in the first 30 days",
    "lede": "Fear of a messy handover keeps a lot of businesses stuck with a provider they've outgrown. Here is the whole sequence, so there are no surprises in it.",
    "crumbs": [("Trust centre", "/trust-centre"), ("Onboarding", "/onboarding-first-30-days")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT onboards most businesses within 30 days. Week one covers discovery and a
    plain-English report; week two closes urgent gaps such as untested backups and missing multi-factor
    authentication; weeks two to three deploy monitoring and support access; week four is documentation
    handover and the first review. The initial review is free. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">The sequence</h2>
    <div class="grid grid--2" style="margin-top:32px">{steps(WEEKS)}</div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>Dealing with your outgoing provider</h2>
    <p style="margin-top:16px">This is the part people dread, and it's the part we'll take off you entirely
    if you want.</p>
    {ticks(FROM_PROVIDER)}
    <p style="margin-top:24px">On that last point about ownership: check your domain name and your Microsoft
    365 tenancy are registered to your business, not to your IT provider. It's the most common thing we find
    wrong during onboarding, and it's much easier to fix while everyone is still on speaking terms.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>What you get at the end of it</h2>
    {ticks([
      "A complete asset register — every device, licence, warranty, subscription and supplier",
      "Network documentation, including what connects to what and why",
      "Credentials held securely, with confirmation that they belong to you",
      "A written baseline of your security position, including where you sit against the Essential Eight",
      "A prioritised plan for the next twelve months, with rough costs against it",
      "Confirmation of what's backed up, how often, and evidence a restore has actually been tested",
    ])}
    <p style="margin-top:24px">All of it is yours. You can ask for a copy at any time, and you get it on
    exit as a matter of course — see <a href="/service-levels-and-security">our published commitments</a>.</p>

    <div class="rule">{MARK}</div>

    <h2>If you're not ready for managed IT</h2>
    <p style="margin-top:16px">The review will sometimes conclude that you don't need us monthly yet. That's
    a legitimate outcome and we'll say it rather than sell around it — plenty of businesses are better served
    by <a href="/it-support-and-services-gold-coast">ad-hoc support</a> until they have a server, staff who
    can't work without their systems, or client data they'd struggle to prove is protected.</p>
    <p style="margin-top:16px">You keep the report either way.</p>

    {trust_note('Onboarding follows the practices set out in <a href="/how-we-work-itil">how we work</a> — discovery feeds the asset register, the report feeds the improvement plan, and both become the baseline your service reviews measure against.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
  ("Published service levels", "/service-levels-and-security"),
  ("How we work — ITIL 4", "/how-we-work-itil"),
  ("Trust centre", "/trust-centre"),
  ("Business IT Support", "/it-support-and-services-gold-coast"),
  ("How to choose an MSP", "/how-to-choose-an-msp-gold-coast"),
], heading="Related")}

{cta("Start with the free review",
     "A walk through your systems and a plain-English report on what's working and what isn't. Yours to keep, whether or not you go any further.")}
''',
}

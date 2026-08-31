from layout import MARK, cta, faq_block, ticks, related, trust_note, issues, example

PRACTICES = [
    ("Service desk", "Who do I call, and will a human answer?",
     "One number and one email address, answered 8am to 5pm Monday to Friday. Outside those hours our digital assistant takes the details and logs the job for the next business day. Every request is logged, so nothing depends on someone remembering a corridor conversation."),
    ("Incident management", "Something's broken. How fast do you come?",
     "Faults are prioritised P1 to P4 by business impact and worked to published response targets. Restoring service comes first; understanding why comes after, as a separate piece of work."),
    ("Service request management", "How do I get a new starter set up?",
     "Requests are handled separately from faults, because mixing them means the new laptop request competes with the server being down. Requests are scheduled; faults are responded to."),
    ("Problem management", "Will you fix the cause, or keep charging me for the same fault?",
     "When a fault recurs, we open a problem record and chase the root cause. For managed clients that work is included — which is exactly the incentive difference between managed IT and break-fix."),
    ("Change enablement", "Will you break something and disappear?",
     "Changes that could disrupt your business are approved by you, scheduled, and have a documented backout plan before we start. High-risk work happens outside business hours."),
    ("Service level management", "What have you actually committed to?",
     "Response targets are published rather than negotiated privately, and reviewed with managed clients at their service reviews."),
    ("Configuration management", "What happens to our documentation if we leave?",
     "Every device, licence, credential and supplier is recorded in an asset register that belongs to you. You can request a copy at any time, not only on exit."),
    ("Continual improvement", "Will anyone ever think about our IT strategically?",
     "Managed clients get periodic service reviews covering what broke, what's ageing, what's coming out of support and what to budget for. IT that's only ever reactive gets expensive slowly."),
]

rows = "".join(
    f'<tr><td class="slot">{p}</td><td><em>{q}</em></td><td>{a}</td></tr>'
    for p, q, a in PRACTICES)

COMMON_ISSUES = [
    ("&ldquo;Isn&rsquo;t this just process for its own sake?&rdquo;",
     "a fair suspicion. Service management frameworks can become bureaucracy, and plenty of providers have made them exactly that.",
     "Judge it by what it prevents. Every practice we use exists because of a specific failure mode &mdash; changes made without a way back, faults fixed repeatedly without a cause being found, work nobody recorded. If a practice is not preventing something, it should go."),
    ("&ldquo;We just want it fixed, not a process&rdquo;",
     "entirely reasonable, and the two are not opposed. The process is what makes the fix stick.",
     "The visible part should be a fixed fault and a clear explanation. Incident, problem and change handling happen behind that, and if you are noticing the framework rather than the outcome, we are doing it wrong."),
    ("&ldquo;What&rsquo;s the difference between an incident and a problem?&rdquo;",
     "a distinction that sounds like jargon and is the single most useful idea in the framework. An incident is the interruption; the problem is the underlying cause.",
     "Restore service first, then find the cause separately. Businesses that only ever handle incidents fix the same fault indefinitely, which is expensive and completely avoidable."),
    ("&ldquo;Our last provider changed things without telling us&rdquo;",
     "no change management. It is one of the most common complaints we hear about incoming clients&rsquo; previous arrangements.",
     "Changes that could disrupt your business get approved by you, scheduled, and given a documented way back before they start. No silent Friday-afternoon upgrades."),
    ("&ldquo;Why does everything have to be written down?&rdquo;",
     "because undocumented knowledge is a dependency on individuals. It works perfectly until somebody is on leave, unwell, or no longer with either business.",
     "Documentation is yours, not ours &mdash; asset register, network diagrams, licences, credentials and configuration notes, available on request at any time rather than only on the way out."),
    ("&ldquo;Are you certified in ITIL?&rdquo;",
     "a question worth answering precisely. Royce holds ITIL 4 certification. bcom ICT as an organisation is not certified in anything, because ITIL certification applies to people rather than to companies.",
     "Credentials sit on the person who holds them. We publish whose they are, which lets you check rather than take it on trust."),
]

EXAMPLE_1 = example(
    "The fault that had been fixed eleven times",
    "A business had a recurring problem with a shared system that failed every few weeks. Each occurrence was resolved promptly by their previous provider and billed. It had been going on for over a year.",
    "Reviewing eleven separate tickets, each had been handled correctly as an incident &mdash; service restored, ticket closed, invoice raised. Nobody had ever opened a problem record to ask why it kept happening, because nobody was being paid to. The cause turned out to be a scheduled task that failed under a specific condition roughly monthly and consumed a shared resource on its way down.",
    "Restored service as an incident, then investigated separately as a problem, found the failing task, and corrected it. Recorded the whole thing so the history exists if anything similar appears.",
    "It has not recurred. Eleven correct incident responses had produced eleven invoices and no progress, which is what happens when the distinction between an incident and a problem is not made.")

EXAMPLE_2 = example(
    "A change with a way back",
    "A business needed a significant upgrade to a system its whole operation depended on. The previous attempt, made by another party two years earlier, had failed and taken the business offline for a day and a half.",
    "The earlier attempt had been made on a Friday afternoon with no tested rollback and no agreed point at which to abandon it. When it went wrong, the only options were to keep going or to restore from a backup nobody had tested. That is what turned a failed upgrade into a day and a half.",
    "Scheduled the work outside trading hours with a tested rollback in place, a verified restore, and an agreed cut-off time at which we would revert regardless of progress. Confirmed each step with the business before proceeding to the next.",
    "The upgrade completed inside the window and the rollback was never needed. Having it ready cost about two hours of preparation, which is the entire difference between the two attempts.")

FAQS = [
    ("Does bcom ICT follow ITIL?",
     "bcom ICT's service management practices are based on ITIL 4, and Royce Clark holds ITIL 4 Foundation certification. bcom ICT is not certified as an organisation against ITIL or ISO/IEC 20000-1 — ITIL is a framework we work to, not a badge we've been audited for. Call 07 3041 8993."),
    ("Isn't ITIL overkill for a small business?",
     "The full framework is, and we don't run it. ITIL 4's own guiding principle is 'keep it simple and practical', and that's the part we take seriously. What a small business actually needs from it is: requests get logged, faults get prioritised sensibly, recurring problems get chased, and nothing changes without warning. That's it. The rest is machinery for organisations far larger than yours or ours."),
    ("What's the difference between an incident and a request?",
     "An incident is something broken — you had it, now you don't. A request is something new — a starter, a device, an access change. They're handled differently because they compete for the same people, and if they share a queue the new-laptop request will sit behind the outage or, worse, the other way around."),
    ("What is problem management, in plain terms?",
     "Fixing incidents restores service. Problem management asks why it happened and stops it recurring. If your printer jams every Tuesday, incident management clears the jam each week and problem management finds out that a scheduled job is sending it a malformed file. Break-fix providers rarely do the second part, because they earn from the first."),
    ("How does change control work in practice?",
     "For anything that could disrupt your business — a firewall change, a server update, a migration — we tell you what we're doing, agree a window, and have a way to reverse it before starting. Routine low-risk work like a patch on a single workstation doesn't need that ceremony, and pretending it does just slows everything down."),
    ("Do we get service reviews?",
     "Managed clients do. They cover what broke and why, what's ageing or coming out of support, security posture, and what to budget for over the next twelve months. It's the difference between an IT provider and someone who answers the phone."),
]

PAGE = {
    "path": "/how-we-work-itil",
    "priority": "0.75",
    "title": "How We Work — ITIL 4 Service Management | bcom ICT",
    "description": "How bcom ICT runs service desk, incidents, requests, problems, change control and continual improvement — ITIL 4 practices explained in plain English.",
    "hero_kind": "doc",
    "eyebrow": "Trust centre",
    "h1": "How we actually run the service",
    "lede": "Our service management is based on ITIL 4. Stripped of the jargon, that means eight things — and every one of them answers a question a client has already asked us.",
    "crumbs": [("Trust centre", "/trust-centre"), ("How we work", "/how-we-work-itil")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT runs service management practices based on ITIL 4, covering service desk,
    incident, request, problem and change management, service levels, configuration management and continual
    improvement. Royce Clark holds ITIL 4 Foundation certification. bcom ICT is not certified as an
    organisation against ITIL or ISO/IEC 20000-1.</p>

    <h2 style="margin-top:56px">Eight practices, and the question each one answers</h2>
    <p style="margin-top:16px">Most providers put "ITIL-aligned" in the footer and leave it there. The reason
    it's worth more than that is that ITIL's practices map almost exactly onto the things clients worry about
    when choosing an IT provider — so here they are side by side.</p>
    <div class="tablewrap" style="margin-top:24px">
      <table>
        <thead><tr><th>Practice</th><th>What you're really asking</th><th>How it works here</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>Keep it simple and practical</h2>
    <p style="margin-top:16px">That's one of ITIL 4's own guiding principles, and it's the one that matters
    most for a business with eight staff. The full framework describes machinery for organisations far larger
    than yours or ours. Running all of it at your scale would cost you money and buy you meetings.</p>
    <p style="margin-top:16px">So we run the parts that change outcomes:</p>
    {ticks([
      "Everything gets logged, so nothing lives only in someone's head",
      "Faults get prioritised by business impact, not by who shouted loudest",
      "Recurring problems get a root cause, not a repeat visit",
      "Nothing disruptive changes without your approval and a way back",
      "Your documentation is written down and belongs to you",
      "Someone looks at the whole picture periodically, not just the last ticket",
    ])}
    <p style="margin-top:24px">We run the same disciplines a large IT department runs. We just run them at a
    size that suits a business with eight staff, and we explain them in English.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Where this is written down</h2>
    <p style="margin-top:16px">Practices that only exist in conversation aren't practices. These are the
    pages where ours are set out in a form you can hold us to:</p>
    {ticks([
      '<a href="/service-levels-and-security">Service levels</a> — the P1 to P4 priority matrix, response targets, hours, escalation path and exit terms',
      '<a href="/onboarding-first-30-days">Onboarding</a> — what happens in the first 30 days, including the documentation we build and hand to you',
      '<a href="/iso-alignment">ISO alignment</a> — the standards behind these practices, and where we stop short of a certification claim',
      '<a href="/data-handling-and-sovereignty">Data handling</a> — what we hold, where it lives and who can reach it',
    ])}

    {trust_note('Royce Clark holds ITIL 4 Foundation certification. That is an individual credential — it does not make bcom ICT an ITIL-certified or ISO/IEC 20000-1-certified organisation, and we do not describe it that way.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Questions</span>
      <h2>What people actually ask about how we work</h2>
      <p>Six questions, including the one about whether any of this is worth the trouble.</p>
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
  ("Trust centre", "/trust-centre"),
  ("Published service levels", "/service-levels-and-security"),
  ("ISO alignment", "/iso-alignment"),
  ("Onboarding — first 30 days", "/onboarding-first-30-days"),
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
  ("Managed IT vs break-fix", "/managed-it-vs-break-fix"),
], heading="Related")}

{cta("Want to see how this works on your systems?",
     "The free review is where it starts — we look at what you're running and show you what we'd document, prioritise and fix first.")}
''',
}

from layout import MARK, cta, faq_block, commitments, ticks, related, trust_note, issues, example

MATRIX = [
    ("p1", "P1 — Critical", "Business stopped. Server, internet, phones or email down for everyone; suspected ransomware or an active breach.",
     "Response within 4 business hours (contracted). After-hours emergency attendance included.",
     "Best effort &mdash; usually the same business day, and attendance next business day."),
    ("p2", "P2 — High", "A team or a core system is down. A workaround exists but it's painful.",
     "Response within 4 business hours; target resolution same business day.",
     "Best effort &mdash; usually the same business day."),
    ("p3", "P3 — Medium", "One person blocked, or noticeable degradation with a workaround available.",
     "Next business day.", "Best effort, generally within one business day."),
    ("p4", "P4 — Request", "New user, new device, access change or planned work. Not a fault.",
     "Scheduled — target within 3 business days.", "Quoted on request."),
]

COMMITS = [
    ("Someone picks up during business hours",
     "8:00am to 5:00pm, Monday to Friday, Brisbane time. Outside those hours our digital assistant answers, takes the details and logs the job — it identifies itself as an assistant rather than pretending to be a person. Calls are returned the next business day. Managed and SLA clients have after-hours on-call cover under their agreement."),
    ("You'll know before we change anything",
     "Changes that could disrupt your business are approved by you, scheduled, and have a documented way back out before we start. No silent Friday-afternoon upgrades."),
    ("Recurring faults are our cost, not your invoice",
     "If the same problem keeps returning, finding the cause is on us. For managed clients that's the whole point of the arrangement; for everyone else we'll still tell you what the underlying cause is rather than billing the symptom repeatedly."),
    ("You own your documentation",
     "Asset register, network diagrams, licences, credentials and configuration notes belong to you, not to us. You can ask for a copy at any time, not only on the way out."),
    ("Exit is clean",
     "If you leave, you get everything handed over in a usable form and we'll talk to the incoming provider. Managed agreements are month-to-month, so leaving needs no notice period argument."),
    ("We tell you when it's not worth it",
     "Including when a repair costs more than a replacement, when you don't need managed IT yet, or when your existing system has years left in it. Losing a sale is cheaper than losing a client."),
]

rows = "".join(
    f'<tr><td class="priority priority--{k}">{n}</td><td>{d}</td><td>{m}</td><td>{o}</td></tr>'
    for k, n, d, m, o in MATRIX)

COMMON_ISSUES = [
    ("&ldquo;What counts as critical?&rdquo;",
     "a definition worth agreeing in advance rather than during an outage. Priority set by how loudly a fault is reported is priority set badly.",
     "Priority is set by business impact and agreed with you when the job is logged. Everyone offline, the server down, phones or email out for the whole office, or signs of a breach &mdash; that is a P1. One person unable to print is not, and treating it as one is how genuine emergencies end up queued."),
    ("&ldquo;Does response mean fixed?&rdquo;",
     "no, and providers that blur the two are promising something they cannot control. Response means a person has picked the job up and contacted you.",
     "We commit to response and not to resolution, because resolution times vary too much by fault to promise honestly. What we do commit to is telling you what we have found and what happens next."),
    ("&ldquo;You advertise business hours &mdash; what about the rest of the time?&rdquo;",
     "a fair challenge to any provider. Ours are eight to five weekdays, Brisbane time, and we would rather publish that than imply otherwise.",
     "Outside those hours a digital assistant answers, identifies itself as an assistant rather than pretending to be a person, takes details and logs the job. Managed and SLA clients have after-hours on-call under their agreement; it is contracted rather than available ad hoc."),
    ("&ldquo;What if you miss a target?&rdquo;",
     "a question most service level documents avoid.",
     "Tell us. Response performance is reviewed with managed clients at their service reviews rather than left for you to discover in a report. If we are consistently missing them the agreement is not working, and it is month-to-month for exactly that reason."),
    ("&ldquo;Who do we escalate to?&rdquo;",
     "in many providers, an unclear path through several tiers.",
     "The first escalation is to Royce, who is a director. There is no call centre structure to climb, and an escalation reaches an owner the same day."),
    ("&ldquo;Can we see this before we sign?&rdquo;",
     "a question that should not need asking and frequently does.",
     "This page is it. The priority matrix, the response targets and the commitments are published rather than negotiated privately, so you can take them to another provider and ask for the same thing in writing."),
]

EXAMPLE_1 = example(
    "Agreeing the priority rather than assuming it",
    "A business logged a fault as critical: a senior staff member could not access a system needed for a client meeting that afternoon. It was genuinely urgent for that person and the business expected an immediate response.",
    "One person unable to reach one system is not a P1 under the published matrix, and at that moment two other clients had faults affecting entire offices. Handling the loudest report first would have meant two businesses waiting while one person was helped, which is precisely the failure the matrix exists to prevent.",
    "Explained the position directly, agreed a P2 with a commitment to have someone on it within the hour, and met that. The access issue was resolved with time to spare before the meeting.",
    "Everyone was handled in the right order, and the business understood why rather than feeling deprioritised. That conversation is possible because the matrix is published and was agreed before there was anything to argue about.")

EXAMPLE_2 = example(
    "A missed target, raised by us",
    "A managed client had a P2 fault where our response fell outside the committed window. The business had not noticed &mdash; the fault was resolved the same day and nobody had been watching a clock.",
    "The delay was ours. A job had been logged through a channel that was not checked promptly during a staffing gap, and the four-hour response commitment was breached by about ninety minutes. It would have been very easy to say nothing, since the outcome was fine and the client had no complaint.",
    "Raised it at the service review, explained what had happened and what had been changed so it could not recur, and recorded it as a missed target in the client&rsquo;s own record rather than in ours alone.",
    "The client kept the agreement and said the disclosure had increased rather than reduced their confidence. A commitment nobody audits is not a commitment, and we would rather be the ones who mention it.")

FAQS = [
    ("How quickly does bcom ICT respond to a critical IT fault?",
     "The 4-hour response target is contracted and applies to managed and SLA clients only — for P1 critical faults during business hours, with after-hours emergency attendance included. All other clients receive a best-effort response, usually the same business day and generally within one business day, with on-site attendance the next business day. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time. Call 07 3041 8993."),
    ("What counts as a P1?",
     "Your business has stopped. Everyone is offline, the server is down, phones or email are out for the whole office, or there are signs of ransomware or an active breach. One person unable to print is not a P1, and treating it as one is how genuine emergencies end up in a queue."),
    ("Are you available after hours?",
     "Not for general enquiries. bcom ICT is open 8:00am to 5:00pm, Monday to Friday, Brisbane time. Outside those hours our digital assistant answers the phone, takes your details and logs the job, and we call back the next business day. Managed and SLA clients have after-hours on-call cover under their agreement, which is a contracted arrangement rather than something available ad hoc. We won't claim a 24/7 human response we don't provide."),
    ("What if you miss a response target?",
     "Tell us. Response performance is reviewed with managed clients at their service reviews, and a missed target is a conversation rather than something you have to discover in a report. If we're consistently missing them, the agreement isn't working and you can leave — it's month-to-month for exactly that reason."),
    ("Who do we escalate to if we're not getting anywhere?",
     "The first escalation is to Royce, who is a director. There is no call centre tier structure to climb; the business is small enough that an escalation reaches an owner the same day."),
    ("Do you have a service level agreement we can see before signing?",
     "This page is it. The priority matrix and commitments above are published rather than negotiated privately, so you can compare us against another provider before you talk to us. Managed agreements restate these terms contractually."),
    ("What happens to our passwords and documentation if we part ways?",
     "They're handed over. Credentials, asset register, network documentation, licence details and configuration notes are provided in a usable form, and we'll speak with the incoming provider to hand over cleanly."),
]

PAGE = {
    "path": "/service-levels-and-security",
    "priority": "0.8",
    "title": "Service Levels — Response Targets & Commitments | bcom ICT",
    "description": "bcom ICT's published service levels — the P1 to P4 priority matrix, response targets, escalation path and what happens to your documentation if you leave.",
    "hero_kind": "doc",
    "eyebrow": "Trust centre",
    "h1": "What we actually commit to",
    "lede": "Our priority matrix and response targets, published rather than negotiated privately. Compare them against any other provider before you talk to us.",
    "crumbs": [("Trust centre", "/trust-centre"), ("Service levels", "/service-levels-and-security")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT publishes a four-level priority matrix. Managed IT clients have a contracted
    4-hour response for P1 critical faults with after-hours emergency attendance included; all other clients
    receive a best-effort response &mdash; usually the same business day and generally within one business
    day &mdash; with next-business-day attendance. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time.
    Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">Priority matrix</h2>
    <p style="margin-top:16px">Priority is set by business impact, not by how loudly it's reported. We'll
    agree the priority with you when you log it.</p>
    <div class="tablewrap" style="margin-top:24px">
      <table>
        <thead><tr><th>Priority</th><th>What it means</th><th>Managed IT client</th><th>All other clients</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p style="margin-top:20px"><strong>Response</strong> means a person has picked the job up and contacted
    you — not that the fault is fixed. Resolution times vary too much by fault to promise honestly, so we
    don't. What we do commit to is telling you what we've found and what happens next.</p>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Hours</span>
      <h2>When we're actually available</h2>
      <p>Plenty of providers advertise 24/7 and mean an answering machine. We'd rather state ours plainly.</p>
    </div>
    {ticks([
      "<strong>Business hours are 8:00am to 5:00pm, Monday to Friday</strong>, Brisbane time. That is when calls are answered by a person and when work is actioned.",
      "<strong>Outside those hours</strong> our digital assistant answers, takes your details and logs the job. It identifies itself as an assistant rather than pretending to be a person.",
      "<strong>We do not respond to phone enquiries after hours.</strong> Details taken overnight or at the weekend are actioned the next business day. We would rather say that than imply otherwise.",
      "<strong>After-hours emergency attendance</strong> is included for managed and SLA clients on a P1, and is not available ad hoc.",
      "<strong>The 4-hour response target is contracted and applies to managed and SLA clients only.</strong> Every other enquiry gets a best-effort response &mdash; usually the same business day, and generally within one business day. We would rather publish the distinction than let it be discovered.",
    ])}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Commitments</span>
      <h2>Six things we'll hold ourselves to</h2>
      <p>These are the parts most providers leave unsaid, which is precisely why they're worth writing down.</p>
    </div>
    {commitments(COMMITS)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>Security posture</h2>
    <p style="margin-top:16px">If we manage your systems, we hold access to them. That deserves saying out
    loud rather than burying in a contract.</p>
    {ticks([
      "Technician access is individually named — no shared logins into client environments.",
      "Multi-factor authentication is enforced on every tool we use to reach client systems.",
      "Client credentials are held in a dedicated password management platform, not in spreadsheets or email.",
      "Access is reviewed when staff change, and revoked on the day someone leaves.",
      "Technicians attending sites hold national police checks; Queensland Blue Cards are held where the client site requires them.",
      "Professional indemnity, cyber liability and public liability insurance are held — certificates of currency on request.",
    ])}
    <p style="margin-top:24px">Our own environment is operated against the ASD Essential Eight and aligned to
    ISO/IEC 27001:2022. <strong>bcom ICT is not certified to ISO/IEC 27001</strong> — see
    <a href="/iso-alignment">ISO alignment</a> for exactly what that does and doesn't mean.</p>

    {trust_note('Where your data physically lives, who at bcom ICT can reach it, and how long we keep it is set out on <a href="/data-handling-and-sovereignty">data handling and sovereignty</a>.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Questions</span>
      <h2>What people actually ask about our service levels</h2>
      <p>Six questions, including two that most service level documents quietly avoid.</p>
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
  ("ISO alignment", "/iso-alignment"),
  ("How we work — ITIL 4", "/how-we-work-itil"),
  ("Data handling & sovereignty", "/data-handling-and-sovereignty"),
  ("Onboarding — first 30 days", "/onboarding-first-30-days"),
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
], heading="Related")}

{cta("Compare us properly",
     "Take this page to whoever else you're considering and ask them for the same thing in writing. That comparison is the one worth making.")}
''',
}

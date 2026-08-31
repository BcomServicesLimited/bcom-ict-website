from layout import MARK, cta, faq_block, commitments, ticks, related, trust_note

MATRIX = [
    ("p1", "P1 — Critical", "Business stopped. Server, internet, phones or email down for everyone; suspected ransomware or an active breach.",
     "Response within 4 business hours (contracted). After-hours emergency attendance included.",
     "Callback within 4 business hours; attendance next business day."),
    ("p2", "P2 — High", "A team or a core system is down. A workaround exists but it's painful.",
     "Response within 4 business hours; target resolution same business day.",
     "Callback within 4 business hours."),
    ("p3", "P3 — Medium", "One person blocked, or noticeable degradation with a workaround available.",
     "Next business day.", "Next business day."),
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

FAQS = [
    ("How quickly does bcom ICT respond to a critical IT fault?",
     "Managed IT clients have a contracted 4-hour response for P1 critical faults during business hours, with after-hours emergency attendance included. All other clients receive a callback within 4 business hours and on-site attendance the next business day. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time. Call 07 3041 8993."),
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
    "description": "bcom ICT's published service levels: P1–P4 priority matrix, response targets, escalation path, hours of operation and what happens to your documentation if you leave.",
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
    receive a callback within 4 business hours and next-business-day attendance. Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time.
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
      "<strong>Callback within 4 business hours</strong> applies to every enquiry, from any channel.",
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

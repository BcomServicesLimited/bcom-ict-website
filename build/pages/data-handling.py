from layout import MARK, cta, faq_block, ticks, related, trust_note, issues, example

HOLDINGS = [
    ("Your credentials", "Administrative logins to your systems, held in a dedicated password management platform with individually named access and multi-factor authentication. Never in spreadsheets, documents or email.", "Password management platform"),
    ("Your asset register", "Devices, licences, warranties, network layout and supplier details. This is documentation about your environment rather than your business data.", "Our documentation system"),
    ("Monitoring telemetry", "Device health, patch status, disk space, security alerts. Operational data about your machines — not the contents of your files.", "Monitoring platform"),
    ("Support ticket history", "What you asked, what we did, and any screenshots or logs attached to a job. Attachments can incidentally contain business information, so tickets are treated as confidential.", "Ticketing system"),
    ("Backup data", "Only where bcom ICT provides backup as a service. Location is agreed with you and set out in your agreement.", "Backup platform"),
    ("Billing details", "Business contact and billing information. bcom ICT does not store customer payment card numbers.", "Accounting system"),
]

rows = "".join(
    f'<tr><td class="slot">{w}</td><td>{d}</td><td>{s}</td></tr>' for w, d, s in HOLDINGS)

COMMON_ISSUES = [
    ("&ldquo;Where does our data physically sit?&rdquo;",
     "a question that used to be rare and is now asked in most supplier questionnaires. It matters for the Privacy Act, for some contracts, and for a few sectors specifically.",
     "Establish it for each system rather than in general. Businesses commonly assume all their data is in Australia, and a service adopted informally by one department is frequently the exception."),
    ("&ldquo;Who at your company can reach our systems?&rdquo;",
     "a question every client is entitled to ask their provider and very few do.",
     "Ask it, and ask how access is controlled. Technician access here is individually named with no shared logins into client environments, multi-factor authentication is enforced on every tool that reaches a client system, and access is revoked on the day someone leaves."),
    ("&ldquo;Do you keep copies of our data?&rdquo;",
     "a reasonable concern, particularly for businesses holding client or health information.",
     "Get the answer in writing and get it specific &mdash; what is held, where, for how long and why. A provider that cannot answer that precisely has not thought about it."),
    ("&ldquo;What happens to it if we leave?&rdquo;",
     "the question that separates providers, and the one asked least often at the start.",
     "Ask before you sign, not afterwards. Documentation, credentials, asset registers and configuration notes should be yours on request at any time, and a clean exit should not require a negotiation."),
    ("&ldquo;Is data sovereignty actually a legal requirement for us?&rdquo;",
     "sometimes, and less often than assumed. The Privacy Act regulates disclosure to overseas recipients rather than prohibiting offshore storage outright, and specific sectors carry their own rules.",
     "Establish your actual obligation rather than adopting a blanket position. Businesses handling health information or working under government contracts most often have a genuine requirement."),
    ("&ldquo;Our staff use tools we never approved&rdquo;",
     "shadow adoption. Someone needed to do something and found a tool that worked, which is usually resourcefulness rather than misconduct.",
     "Find out what is genuinely in use before writing a policy about it. A policy that prohibits the only tool doing a necessary job gets ignored, and then nobody knows anything."),
]

EXAMPLE_1 = example(
    "The one system that was not where everyone assumed",
    "A business completing a client security questionnaire needed to confirm that all client data was held in Australia. The directors were confident it was and asked us to verify it as a formality.",
    "Nearly everything was. One exception: a file transfer service adopted three years earlier by a team that needed to send large documents to clients, chosen because it worked and never assessed by anyone. It stored data in a region outside Australia, and it had been carrying client material for three years. Nobody had done anything wrong &mdash; the team had a job to do and no sanctioned tool for it.",
    "Established where every system genuinely held data, moved the file transfer function into the business&rsquo;s own tenancy where it belongs, and recorded the position for each system so the next questionnaire is a lookup rather than an investigation.",
    "The questionnaire was answered accurately. The useful outcome was the register, because the question is now asked routinely and the answer needs to be available rather than reconstructed each time.")

EXAMPLE_2 = example(
    "A clean exit, from the other side of it",
    "A business joining us was leaving a provider it had used for eight years. The relationship had ended reasonably and the handover was expected to be straightforward.",
    "Very little existed to hand over. There was no asset register, no network documentation and no diagram. Credentials for the firewall, the domain registrar and two cloud services were held only by the outgoing provider, and some had been set up under that provider&rsquo;s own accounts rather than the client&rsquo;s. Nothing had been withheld maliciously &mdash; it had simply never been created or never been transferred.",
    "Rebuilt the documentation from the environment itself, recovered ownership of each account through the relevant provider&rsquo;s process, and moved everything into accounts the business owns. Then gave the business the complete set, on the basis that it should hold it regardless of who supports it.",
    "The business owns its own environment for the first time in eight years. This is why we publish what a client gets on the way out &mdash; not because we expect anyone to leave, but because being able to is the point.")

FAQS = [
    ("Where does our data live if bcom ICT manages our systems?",
     "Microsoft 365 tenancies that bcom ICT provisions are created in Australian regions, so mail and files are stored in Australian data centres. Where bcom ICT provides backup as a service, the storage location is agreed with you and recorded in your agreement. bcom ICT will tell you the location of every system holding your data on request."),
    ("Is our data sovereign — does it stay in Australia?",
     "For the parts we control, yes by default. Microsoft 365 tenancies we provision use Australian regions, and Australian-hosted backup is available. Some vendor platforms we use for monitoring and ticketing process data outside Australia, which we'll tell you about rather than gloss over. If Australian-only processing is a hard requirement for your business, say so at the start and we'll design around it — it does constrain the tooling."),
    ("Who at bcom ICT can access our systems?",
     "Named technicians, using individual accounts with multi-factor authentication enforced. There are no shared logins into client environments. Access is reviewed when staff change and revoked the day someone leaves. Every access is attributable to a person, which is the point of doing it this way."),
    ("Do you read our emails or files?",
     "No. Managing a Microsoft 365 tenancy means we can administer mailboxes — create them, restore them, fix permissions. It does not mean we read their contents, and we don't. Where a support job genuinely requires looking at a specific message or file, we ask you first."),
    ("What happens to our data if we stop using bcom ICT?",
     "Credentials, asset register and documentation are handed over to you. Ticket history and billing records are retained for the period our legal and insurance obligations require, then deleted. Backup data held on your behalf is returned or destroyed as you direct, and we'll confirm in writing which happened."),
    ("Are you covered by the Privacy Act?",
     "bcom ICT handles personal information belonging to clients and their staff, and treats it under the Australian Privacy Principles. Your business has its own obligations under the Privacy Act for the data you hold — our role is to help you meet them, not to assume them for you. Our notifiable data breach guide sets out how that works when something goes wrong."),
    ("Do you use subcontractors who could reach our data?",
     "Two categories, and we're explicit about both. Cabling is carried out by ACMA registered cabling contractors — they work on physical infrastructure and are not given access to your systems or data. Vendor platforms for monitoring, ticketing and endpoint protection process operational data as part of delivering those services. We'll name the platforms on request."),
]

PAGE = {
    "path": "/data-handling-and-sovereignty",
    "priority": "0.75",
    "title": "Data Handling & Sovereignty — Where Your Data Lives | bcom ICT",
    "description": "What data bcom ICT holds on behalf of clients, where it is stored, who can access it and how long it is kept. Australian data residency for Microsoft 365 and backup.",
    "hero_kind": "doc",
    "eyebrow": "Trust centre",
    "h1": "What we hold, where it lives, and who can reach it",
    "lede": "“Where does our data actually live?” is a fair question that most IT providers answer vaguely. Here is ours in full, including the parts that aren't in Australia.",
    "crumbs": [("Trust centre", "/trust-centre"), ("Data handling", "/data-handling-and-sovereignty")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">Microsoft 365 tenancies provisioned by bcom ICT are created in Australian regions, so
    client mail and files are stored in Australian data centres. Backup location is agreed per client and
    recorded in the agreement. Access to client systems uses individually named accounts with multi-factor
    authentication enforced — bcom ICT operates no shared logins into client environments.</p>

    <h2 style="margin-top:56px">What we actually hold</h2>
    <p style="margin-top:16px">Managing your systems means holding some things about your business. This is
    the complete list, and the deliberate distinction throughout is between <em>data about your environment</em>
    and <em>your business data</em> — we hold a lot of the first and very little of the second.</p>
    <div class="tablewrap" style="margin-top:24px">
      <table>
        <thead><tr><th>What</th><th>Detail</th><th>Where it sits</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>Data sovereignty, including the caveats</h2>
    <p style="margin-top:16px">Australian data residency has become a routine buying question, and the honest
    answer for almost every small IT provider has caveats. Here are ours.</p>
    {ticks([
      "<strong>Microsoft 365</strong> — tenancies we provision are created in Australian regions. Mail, files, Teams and SharePoint data stay in Australian data centres.",
      "<strong>Microsoft Azure</strong> — resources are deployed to Australian regions unless you specifically ask otherwise.",
      "<strong>Backup</strong> — Australian-hosted backup is available and is what we recommend. The location for your data is agreed and written into your agreement.",
      "<strong>Monitoring, ticketing and endpoint protection</strong> — some vendor platforms process operational data outside Australia. This is telemetry and support records, not the contents of your files, but it is not Australian-only and we will not pretend otherwise.",
      "<strong>If Australian-only processing is a hard requirement</strong> — say so before we start. It is achievable but it constrains the tooling, and that is a design decision rather than a switch we can flip later.",
    ])}
    <p style="margin-top:24px">We'll name every platform holding anything of yours, on request. If a
    provider won't do that, it's worth asking why.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Access control</h2>
    <p style="margin-top:16px">If we manage your systems, we hold keys to them. That deserves stating plainly
    rather than being buried in a schedule.</p>
    {ticks([
      "Named individual accounts for every technician — no shared logins into client environments",
      "Multi-factor authentication enforced on every tool used to reach a client system",
      "Client credentials in a dedicated password management platform, never in documents or email",
      "Access reviewed when staff change, and revoked the day someone leaves",
      "Every access attributable to a person, which is the entire point of doing it this way",
      "Technicians attending sites hold national police checks; Queensland Blue Cards where the site requires them",
    ])}

    <div class="rule">{MARK}</div>

    <h2>Retention and deletion</h2>
    <p style="margin-top:16px">When an engagement ends, credentials, asset register and documentation are
    handed over to you. Ticket history and billing records are retained for the period our legal and
    insurance obligations require, then deleted. Backup data held on your behalf is returned or destroyed as
    you direct, and we confirm in writing which of those happened.</p>
    <p style="margin-top:16px">You can ask for a copy of your documentation at any point during the
    relationship, not only when leaving. It's yours.</p>

    {trust_note('Your business has its own obligations under the Privacy Act and the Notifiable Data Breaches scheme for the personal information you hold. Our role is helping you meet them, not assuming them for you — <a href="/notifiable-data-breach-guide-australia">the NDB guide</a> sets out how that division works when something goes wrong.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Questions</span>
      <h2>What people actually ask about their data</h2>
      <p>Six questions worth putting to any provider, including two most businesses never think to ask.</p>
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
  ('Microsoft Azure', '/azure-cloud-services-gold-coast'),
  ("Trust centre", "/trust-centre"),
  ("Notifiable Data Breaches guide", "/notifiable-data-breach-guide-australia"),
  ("ISO alignment", "/iso-alignment"),
  ("Published service levels", "/service-levels-and-security"),
  ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast"),
  ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast"),
], heading="Related")}

{cta("Need this for a supplier assessment?",
     "If a client or insurer is asking you questions about your IT provider, send them this page — or ask us for whatever else they need.")}
''',
}

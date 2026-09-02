from layout import MARK, cta, faq_block, cards, ticks, steps, related, trust_note, issues, example, verify_note

DATES = [
    ("Windows Server 2012 / 2012 R2", None, "Support ended October 2023. Any of these still running have had no security updates for nearly three years."),
    ("Windows Server 2016", None, "Extended support ends 12 January 2027. That is roughly four months away, and it is the one catching Gold Coast businesses right now."),
    ("Windows Server 2019", None, "Extended support ends January 2029. Not urgent, but it is the one to plan the budget around."),
    ("Windows Server 2022 / 2025", None, "Current. If you are replacing now, this is what you land on."),
]

OPTIONS = [
    ("Replace the server", "New hardware, current Windows Server, same architecture. Suits a business with a line-of-business application that needs a real server, a good connection to it, and no appetite for change."),
    ("Move the workload to Azure", "The application keeps running on Windows, just not in your cupboard. Suits businesses with multiple sites, or where the server room is the weakest link."),
    ("Retire it entirely", "A surprising number of servers now exist to run file sharing and a print queue. Both of those moved to Microsoft 365 years ago and nobody revisited the server."),
    ("Do nothing, deliberately", "Sometimes defensible for a short, bounded period with the server isolated. It should be a decision with an end date, not a drift."),
]

ISSUES = [
    ("&ldquo;It is running fine, so what is the actual risk?&rdquo;",
     "a server doing its job on an operating system that stopped receiving security updates. Nothing visibly changes on the day support ends, which is exactly the problem.",
     "The exposure is not performance, it is that newly discovered vulnerabilities stop being fixed. For a business handling client or health information, that is also increasingly a question your insurer and your clients will ask about."),
    ("&ldquo;Nobody knows what the server actually does&rdquo;",
     "a box that has accumulated roles over a decade &mdash; files, print, a licensing service, a nightly data exchange, a share somebody scripted against years ago.",
     "Audit what depends on it before planning anything. We have found a server everyone described as a file server also running the licence service for the industry application, which nobody mentioned because nobody knew."),
    ("&ldquo;We were quoted for a new server and it seemed like a lot&rdquo;",
     "a like-for-like replacement quoted without asking whether the business still needs a server at all.",
     "Establish what the workload actually is first. If it is file sharing and printing, the answer may be no server, and that conversation should happen before anyone prices hardware."),
    ("&ldquo;We will move it to the cloud, that will be cheaper&rdquo;",
     "an assumption that frequently does not survive contact with a bill. A steady always-on workload can cost more per year in Azure than owning the equivalent hardware.",
     "Model the actual running cost over three years against replacement, including the connection you will need. Cloud wins on flexibility and resilience far more often than it wins on price."),
    ("&ldquo;Our line-of-business software vendor says it needs a server&rdquo;",
     "sometimes true and sometimes a version behind. Vendors update their hosting options and their documentation does not always keep pace.",
     "Ask them directly what they support now, including hosted options. It is a ten-minute call that occasionally removes the whole project."),
    ("&ldquo;We have backups, so a migration is low risk&rdquo;",
     "backups nobody has restored from. A migration is the moment you discover whether they work, and that is a bad moment to find out.",
     "Test a restore before the migration, not as part of it. It is the cheapest insurance available on a project like this."),
]

EXAMPLE_1 = example(
    "The server replacement they did not need",
    "A business of eighteen staff was quoted for a new server after being told their Windows Server 2016 machine was approaching end of support. The quote was substantial and the reasoning was sound, so they asked us for a second opinion before signing.",
    "Auditing what the server actually did found two things: a file share, and a print queue. That was the whole workload. Both had been moved to Microsoft 365 four years earlier during a separate project, and staff had been saving to SharePoint ever since. The server was still switched on, still being backed up, and still carrying a maintenance line in the budget, but the only thing genuinely depending on it was an old mapped drive on three machines that nobody had repointed.",
    "Repointed the three mapped drives, verified nothing else touched the server across a fortnight of monitoring, migrated the remaining print queue to a direct network configuration, and decommissioned the machine.",
    "No server was purchased. The business removed a maintenance cost, a backup target and a security exposure at the same time, and the only work required was two hours of checking what actually depended on it. The quote had not been wrong &mdash; the question had simply never been asked.")
FAQS = [
    ("When does Windows Server 2016 reach end of support?",
     "12 January 2027. After that date Microsoft stops issuing security updates for it, and any newly discovered vulnerability stays unpatched. Windows Server 2012 and 2012 R2 already passed end of support in October 2023. Windows Server 2019 runs until January 2029. Confirm current dates on Microsoft's lifecycle documentation before acting on anything time-sensitive."),
    ("What happens if we keep running an unsupported Windows Server?",
     "It keeps working — nothing breaks on the day. What stops is security updates, so every vulnerability found from that point onward remains open. For businesses handling client, health or financial information, it also becomes something your insurer and your clients may ask about directly, and 'it still works' is not an answer that survives a security questionnaire."),
    ("Should we replace the server or move to the cloud?",
     "It depends on what the server actually does. If it runs a line-of-business application that needs to be close to your staff and your connection is unremarkable, replacing it is often the right answer. If you have multiple sites, or the server room is genuinely the weakest link in the business, moving the workload to Azure makes more sense. And a surprising number of servers now exist to share files and run a print queue, both of which moved to Microsoft 365 years ago."),
    ("Is moving to Azure cheaper than a new server?",
     "Often not, and anyone telling you otherwise has not modelled it. A steady always-on workload can cost more per year in Azure than owning the hardware outright. Azure wins on flexibility, resilience and not owning a box in a cupboard — which are good reasons — but it should be chosen on those rather than on an assumption about price."),
    ("How long does a server migration take?",
     "Planning is weeks; the cutover is usually a weekend. Most of the work is establishing what actually depends on the server, because that is where migrations go wrong — a scheduled task, a licensing service or a nightly data exchange nobody documented."),
    ("Can you migrate without downtime?",
     "Rarely entirely, and we would not promise it. What we do commit to is a cutover scheduled outside trading hours, with a tested way back and an agreed point at which we revert regardless of progress. That preparation is the difference between a failed cutover and a lost week."),
]

PAGE = {
    "path": "/windows-server-migration-gold-coast",
    "priority": "0.8",
    "service": "Windows Server Migration Gold Coast",
    "title": "Windows Server End of Support & Migration | bcom ICT",
    "description": "Windows Server 2016 support ends 12 January 2027. bcom ICT plans and delivers server migrations for Gold Coast businesses. Call 07 3041 8993.",
    "hero_img": "windows-server-hero.webp",
    "hero_alt": "A bcom ICT technician working on a business server in a Gold Coast office",
    "eyebrow": "Microsoft",
    "h1": "Windows Server 2016 support ends in January 2027",
    "lede": "Nothing breaks on the day. Security updates simply stop, and every vulnerability found afterwards stays open. Here is how to decide what to do about it.",
    "actions": [("Get a server review", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["2016 ends Jan 2027", "Replace, move or retire", "Dependencies audited first", "Tested rollback"],
    "crumbs": [("Services", "/services"), ("Windows Server migration", "/windows-server-migration-gold-coast")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">Windows Server 2016 reaches end of extended support on 12 January 2027, after which
    Microsoft stops issuing security updates for it. Windows Server 2012 and 2012 R2 passed that point in
    October 2023. bcom ICT audits what the server actually does, then plans the right answer — replace it,
    move the workload to Azure, or retire it entirely. Call 07 3041 8993.</p>

    {verify_note("Microsoft lifecycle dates are published by Microsoft and occasionally revised. Confirm the current date for your exact version and edition on Microsoft's lifecycle documentation before making a decision that depends on it. Reviewed September 2026.")}

    <h2 style="margin-top:48px">The dates that matter</h2>
    <div class="grid grid--2" style="margin-top:24px">{cards(DATES, icon=True)}</div>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>Nothing breaks on the day</h2>
    <p style="margin-top:16px">That is what makes this easy to ignore. On 13 January 2027 a Windows Server
    2016 machine will start up, serve files, run the application and behave exactly as it did the day before.
    No warning appears. Nobody notices.</p>
    <p style="margin-top:16px">What stops is the flow of security updates. Every vulnerability discovered from
    that point onward stays open on that machine, permanently. The risk does not arrive on the day &mdash; it
    accumulates quietly afterwards, which is why the businesses that get caught by this are almost never the
    ones who decided to take the risk. They are the ones who never had the conversation.</p>
    <p style="margin-top:16px">There is a second dimension now too. Clients, insurers and security
    questionnaires increasingly ask directly whether systems are supported, and &ldquo;it still works&rdquo; is
    not an answer that survives that question.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Four answers</span>
      <h2>What to actually do about it</h2>
      <p>In roughly the order we would consider them, and the last one is a legitimate choice if it is made deliberately.</p>
    </div>
    <div class="grid grid--4">{steps(OPTIONS)}</div>
    <p style="margin-top:28px;max-width:68ch">The question we would ask first is not which of these you want.
    It is <strong>what does the server actually do?</strong> That answer decides the rest, and it is
    surprisingly often not what the business thinks.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What we hear about server replacement</h2>
    </div>
    {issues(ISSUES)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a server audit turns up before anyone quotes</h2>
      <p>A representative engagement, drawn from real work with client and staff names removed.</p>
    </div>
    {EXAMPLE_1}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Microsoft 365 Setup & Support", "/microsoft-365-setup-gold-coast"),
  ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast"),
  ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast"),
  ("Hardware Procurement & Setup", "/hardware-procurement-setup-gold-coast"),
  ("IT Consulting & Strategy", "/it-consulting-strategy-gold-coast"),
  ("Computer replacement cycle", "/business-computer-replacement-cycle"),
], heading="Related")}

{cta("Still running 2016?",
     "We will audit what the server actually does before anybody quotes anything. Occasionally the answer is that you no longer need one.")}
''',
}

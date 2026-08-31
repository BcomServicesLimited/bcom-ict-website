from layout import MARK, cta, faq_block, cards, ticks, steps, related, photo, trust_note, issues, example

INCLUDED = [
    ("Monitoring that runs all the time", None,
     "Your servers, computers and network are watched around the clock. Most of what we fix, we fix before anyone in your office notices there was a problem."),
    ("Unlimited helpdesk", None,
     "Your staff call or email us directly, as often as they need to. No per-ticket charges and no rationing — if people hesitate to ask for help, small problems become big ones."),
    ("Updates and patching", None,
     "Windows, macOS and your business applications kept current. Unpatched software is how most small businesses actually get breached."),
    ("Backup you can prove works", None,
     "Automated backup with restores tested on a schedule, so you find out the backup works before you need it rather than after."),
    ("Microsoft 365 and cloud management", None,
     "User accounts, licences, mailboxes, security settings and file permissions — set up properly and kept tidy as people join and leave."),
    ("Security baseline maintained", None,
     "Multi-factor authentication, endpoint protection, email filtering and firewall rules, kept aligned to the ASD Essential Eight."),
]

DIFFS = [
    ("You stop paying for the same fault twice",
     "Break-fix rewards a provider for coming back. Managed IT doesn't — if a problem keeps recurring, chasing down the cause is our cost, not another invoice for you. That single difference usually changes the whole relationship."),
    ("Your costs stop being a surprise",
     "One flat monthly fee covering the work above. You can budget for it, and you're not weighing up whether a problem is worth a call-out fee."),
    ("Nothing changes without warning",
     "Anything that could disrupt your business gets approved, scheduled and given a way back out before we touch it. You'll know what's happening and when."),
    ("You can leave",
     "Month-to-month, no lock-in. And if you go, you get your documentation, licences and passwords handed over properly. A provider who makes leaving painful is telling you something."),
]

ONBOARD = [
    ("We look at what you've got", "A full review of your systems, security, backups and licensing. You get a plain-English report of what we'd fix first and what can wait."),
    ("We document everything", "Every device, account, licence, password and supplier written down in one place. Most businesses we take on have none of this, and it's the thing that hurts when a provider disappears."),
    ("We fix the urgent things", "The gaps that would actually cost you — missing backups, no MFA, unsupported systems, expired warranties — get closed first."),
    ("We take over the day-to-day", "Monitoring goes live, your team gets our number, and we start running it. Most businesses are fully onboarded within 30 days."),
]

COMMON_ISSUES = [
    ("“Outlook keeps asking for my password”",
     "a token or credential problem after a security change, a licence that lapsed, or an account that has been compromised and had its sessions revoked.",
     "Check for the compromise first, because that is the expensive answer. Then repair the profile or re-establish the credential — and if MFA was the trigger, finish the rollout properly rather than exempting the user."),
    ("“The server is running out of space again”",
     "log files, shadow copies, an old backup target nobody removed, or a database that has grown for years without anyone watching it.",
     "Find what is actually consuming the space rather than deleting the first large folder. Then set monitoring thresholds so it is caught at 80% on a Tuesday rather than at 100% on a Friday afternoon."),
    ("“Everything is slow this morning”",
     "a backup job that overran into business hours, a Windows update cycle, or a failing drive quietly retrying reads.",
     "Correlate the slowdown against scheduled jobs and disk health before touching anything. Reschedule what should not be running in business hours, and replace the drive if that is what it turns out to be."),
    ("“We can’t print again”",
     "a driver that updated itself, a print spooler that has stopped, or a printer that grabbed a new IP address because nobody reserved one.",
     "Reserve the address properly, standardise the driver across machines, and stop it recurring — rather than clearing the queue again every fortnight."),
    ("“A staff member left and we don’t know what they had access to”",
     "no documented account inventory, and permissions granted ad hoc over several years by several people.",
     "Build the register, revoke everything on the day they leave, and transfer mailbox and file ownership properly. Then make offboarding a checklist rather than a memory exercise."),
    ("“Someone got an email from the boss asking for a payment”",
     "a spoofed sender, or a genuinely compromised mailbox. The second is far more serious and far more common than people expect.",
     "Establish which it is immediately — check for mailbox forwarding rules and unusual sign-ins. Then close the underlying gap: MFA everywhere, and SPF, DKIM and DMARC records so nobody can send as your domain."),
]

EXAMPLE_BACKUP = example(
    "A professional practice with backups that had never been restored",
    "A Gold Coast practice of around 25 staff on break-fix support, calling their previous provider when things broke. Backups had run nightly for years and reported success every morning.",
    "The backup was writing to a NAS on the same network, reachable with the same credentials as the file server — so ransomware would have encrypted both. No restore had ever been tested. Two staff who had left eighteen months earlier still had active accounts and mailbox access.",
    "Moved backups to a separated target, ran a full test restore in front of the practice manager, closed the dormant accounts, rolled multi-factor authentication out across every mailbox, and built the asset and account register that did not exist.",
    "The practice can now answer its insurer’s renewal questions honestly. The first real restore — a partner who deleted a matter folder — took twenty minutes instead of becoming a crisis.")

EXAMPLE_MULTISITE = example(
    "A multi-site operator paying twice for the same problem",
    "A business running three Gold Coast sites, each with equipment bought at different times by different people. Recurring faults at every location, each billed separately by the hour.",
    "Three different router models, three different wireless systems, no documentation for any of them — and the same underlying fault at two sites: an undersized switch exceeding its PoE budget, misdiagnosed at both as a faulty access point.",
    "Standardised all three sites on one centrally managed platform. Fixed the PoE problem properly rather than replacing access points again. Documented every device, licence and credential, and handed the register over.",
    "Support calls dropped substantially because the recurring fault was gone rather than being re-fixed each month. Adding a fourth site later was a change rather than a project.")


FAQS = [
    ("What do managed IT services cost on the Gold Coast?",
     "Managed IT is charged as a flat monthly fee rather than by the hour. The figure is calculated from your business requirements and the services included — what you run, what has to stay available, what compliance applies, and which parts you want us to take on. bcom ICT quotes after reviewing your systems, so the number reflects your actual environment rather than a headcount, and it's month-to-month so you're not locked in while you find out whether it works."),
    ("What's the difference between managed IT and just calling someone when it breaks?",
     "Break-fix means you pay each time something goes wrong, and the provider only earns when it does. Managed IT means someone is watching your systems continuously, patching and backing them up, and fixing causes rather than symptoms. In practice most businesses switch because the running total of break-fix callouts stopped being predictable."),
    ("How fast do you respond?",
     "Managed IT clients have a contracted 4-hour response for critical faults during business hours, with after-hours emergency attendance included. Phones are returned in business hours — after hours by our AI operator, who takes the details and escalates. Our published service levels set out the full priority matrix."),
    ("Do we have to sign a long contract?",
     "No. bcom ICT's managed IT is month-to-month. We'd rather earn the next month than hold you to a three-year agreement."),
    ("Can you work with the IT person we already have?",
     "Yes, and it's common. Some clients have someone internal who handles day-to-day questions and use us for the infrastructure, security and escalations behind them. We'll agree who owns what so nothing falls between us."),
    ("Do you support staff working from home?",
     "Yes. Remote workers are covered the same as anyone in the office — same helpdesk, same monitoring on their machine, same security settings. If your team is spread across several sites or states, that's normal for us."),
    ("What size businesses do you manage IT for?",
     "Most managed clients have between 5 and 60 staff. That's the range where a business is too big to keep muddling through and too small to justify a full-time IT employee."),
]

PAGE = {
    "path": "/managed-it-services-for-small-businesses-gold-coast",
    "priority": "0.9",
    # Exact GBP service name — matched in <title> and Service schema.
    "service": "Managed IT Services Gold Coast",
    "title": "Managed IT Services Gold Coast — Month-to-Month, No Lock-in",
    "description": "Fully managed IT for Gold Coast small and medium businesses. Monitoring, unlimited helpdesk, patching, backup and Microsoft 365 management. Flat monthly fee, 4-hour response SLA, no lock-in. Call 07 3041 8993.",
    "hero_img": "hero-bg-managed-it-services.webp",
    "hero_alt": "A bcom ICT engineer reviewing monitoring dashboards for a Gold Coast managed IT client",
    "h1": "Managed IT for Gold Coast businesses",
    "lede": "Someone looking after your IT every day for a flat monthly fee — monitoring, helpdesk, patching and backup. Month-to-month, with no lock-in contract.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Flat monthly fee", "4-hour response SLA", "Month-to-month", "Local since 2011"],
    "crumbs": [("Services", "/services"), ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides managed IT services to small and medium businesses across the Gold
    Coast for a flat monthly fee, covering proactive monitoring, unlimited helpdesk, patching, backup and
    Microsoft 365 management. Managed clients have a contracted 4-hour response for critical faults, and
    agreements are month-to-month with no lock-in. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">What's included</span>
      <h2>What you actually get each month</h2>
      <p>Not a list of acronyms — the six things that make the difference between IT that works and IT you keep worrying about.</p>
    </div>
    <div class="grid grid--3">{cards(INCLUDED)}</div>

    {trust_note('Behind this sits a documented way of working — response targets, change approvals, root-cause analysis and an asset register you own. <a href="/service-levels-and-security">Our published service levels</a> set out exactly what we commit to, and <a href="/trust-centre">the trust centre</a> explains how we run it.')}
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Managed vs break-fix</span>
      <h2>Why businesses move off call-when-it-breaks</h2>
      <p>Almost every managed client we take on came from paying by the hour. These are the four reasons they gave.</p>
    </div>
    <div class="grid grid--2">{cards(DIFFS, icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Switching to us</span>
      <h2>What happens in the first 30 days</h2>
      <p>Changing IT providers feels risky, and the fear of a messy handover keeps a lot of businesses stuck with someone they've outgrown. Here's the actual sequence.</p>
    </div>
    <div class="grid grid--4">{steps(ONBOARD)}</div>

    <div class="prose-cols" style="margin-top:64px">
      <div>
        <h2>Who this suits</h2>
        <p style="margin-top:16px">Managed IT makes sense once your business is big enough that a day of downtime actually costs money, but not big enough to employ someone full-time. On the Gold Coast that's usually somewhere between five and sixty staff.</p>
        {ticks([
          "You have a server, or systems your business genuinely can't trade without",
          "Staff are losing time to problems nobody is fixing properly",
          "You're not confident your backups would restore if you needed them",
          "Your current provider only appears when you chase them",
          "You handle client data and you'd struggle to prove it's protected",
          "You have staff working from home or across more than one site",
        ])}
        <p style="margin-top:24px">If that's not you yet, <a href="/it-support-and-services-gold-coast">ad-hoc business IT support</a> is the sensible starting point. Plenty of clients start there and move across later.</p>
      </div>
      {photo("managed-it-services-monitoring.webp", "Monitoring dashboards used by bcom ICT to watch Gold Coast client systems around the clock", "Monitoring runs continuously, so most faults are handled before anyone reports them.")}
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What managed clients stop having to think about</h2>
      <p>These are the faults we see most across Gold Coast businesses. Under a managed agreement most of them
      are prevented rather than fixed, which is the whole difference.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What taking on a managed client actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed \u2014 we don\u2019t name
      clients without written permission.</p>
    </div>
    {EXAMPLE_BACKUP}
    {EXAMPLE_MULTISITE}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Business IT Support", "/it-support-and-services-gold-coast"),
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
  ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast"),
  ("Business WiFi & Networks", "/business-wifi-gold-coast"),
  ("Published service levels", "/service-levels-and-security"),
  ("Trust centre — how we work", "/trust-centre"),
])}

{cta("Find out what managed IT would cost you",
     "We'll review what you're running and quote on it. No charge for the review, and no obligation to go further.")}
''',
}

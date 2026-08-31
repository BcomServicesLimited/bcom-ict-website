from layout import MARK, cta, faq_block, cards, ticks, steps, related, photo, trust_note, issues, example, price_table

WORK = [
    ("Microsoft 365", None,
     "Email, Teams, SharePoint and OneDrive set up the way a business should have them — shared mailboxes that work, file permissions that make sense, and security switched on from the first day rather than after an incident."),
    ("Migrating your email across", None,
     "Moving from an old mail server, a hosting provider, or Google Workspace. Mail, calendars and contacts come across, and we do the cutover so people aren't locked out on a Monday morning."),
    ("Files out of the server", None,
     "Moving shared drives to SharePoint or OneDrive without losing the folder structure people rely on. Done badly this is genuinely disruptive, so we map it before we move it."),
    ("Microsoft Azure", None,
     "Where a business still needs servers, running them in Azure instead of a box in the comms room. No hardware to replace every five years, and no single point of failure sitting under someone's desk."),
    ("Google Workspace", None,
     "We support it too. If Google Workspace suits how you already work, there's no reason to move to Microsoft just because it's more common."),
    ("Keeping it tidy afterwards", None,
     "Licences, accounts, permissions and security settings maintained as people join and leave. Cloud tenancies get messy quickly when nobody owns them."),
]

MOVE = [
    ("We map what you have", "Every mailbox, shared drive, licence and application, plus who actually uses what. Migrations go wrong when somebody's critical spreadsheet turns out to live in a folder nobody knew about."),
    ("We plan the cutover", "Timing, what moves first, and how people keep working during it. Usually staged over a weekend so nobody loses a working day."),
    ("We migrate and verify", "Data comes across and gets checked before the old system is switched off — not after."),
    ("We secure and hand over", "MFA on, security baselines applied, permissions tidied, and documentation given to you covering what lives where."),
]

COMMON_ISSUES = [
    ("“I keep getting signed out of Teams and Outlook”",
     "a conditional access or MFA policy applying differently than intended, or a device that is not registered properly against the tenancy.",
     "Look at the sign-in logs rather than guessing — they show exactly which policy is triggering. Then fix the policy or register the device, instead of exempting the user and leaving a hole."),
    ("“We’ve run out of mailbox space”",
     "the licence tier assigned rather than the mailbox itself, or an archive that was never enabled.",
     "Check what is actually assigned before buying more storage. Enabling archiving or moving one user to the right tier is usually cheaper than the upgrade being proposed."),
    ("“Someone deleted a folder and it’s gone”",
     "a SharePoint or OneDrive retention window that has passed. Microsoft’s recycle bins are shorter than people assume and they do expire.",
     "Attempt recovery from the retention stages first. If the window has closed, this is the conversation about third-party Microsoft 365 backup — which is a genuine requirement rather than an upsell."),
    ("“Our shared mailbox stopped working for one person”",
     "a permissions change, an auto-mapping issue after a licence change, or a cached profile holding stale credentials.",
     "Reset the permission cleanly rather than layering another on top. Shared mailbox permissions accumulate badly over years and eventually contradict each other."),
    ("“Files are syncing on my laptop but not my desktop”",
     "OneDrive Known Folder Move applied to one machine and not the other, or sync paused after an update and never resumed.",
     "Standardise the configuration across all machines rather than fixing the one in front of you. Otherwise it reappears on a different device."),
    ("“Someone outside the company can see our documents”",
     "an organisation-wide sharing link created for convenience, often years ago, that nobody has revisited.",
     "Audit sharing across the tenancy — this routinely surfaces far more than management expects. Then tighten the defaults so it does not quietly rebuild itself."),
]

EXAMPLE_1 = example(
    "A migration that was going to lose a folder nobody mentioned",
    "A Gold Coast business of about forty staff moving off an ageing on-premise server to Microsoft 365, with a cutover already booked by another provider.",
    "During mapping we found a shared folder nobody had listed — the operations team’s working files, on a second server that was not in scope and had not been backed up in two years. It would have been switched off with the rest of the hardware.",
    "Paused, brought the folder into scope, migrated it with permissions intact, and staged the cutover across a weekend with the old system left running for a fortnight as a safety net. MFA and security baselines applied during setup rather than afterwards.",
    "Nothing was lost, and nobody spent a Monday morning locked out. The two-year-old unbacked server was the finding that mattered more than the migration itself.")

EXAMPLE_2 = example(
    "A tenancy paying for licences nobody used",
    "A professional firm asked us to look at Microsoft 365 because costs had crept up steadily and nobody could explain why.",
    "Eleven licences assigned to people who had left, three users on a tier well above what their role required, and a separate file-sharing subscription duplicating something already included in their Microsoft plan. Multi-factor authentication was on for six of nineteen accounts.",
    "Reconciled every licence against actual staff, moved users to appropriate tiers, retired the duplicate subscription, and completed the MFA rollout across all accounts.",
    "The licensing reconciliation saved more per year than the work cost, and the security gap that had been sitting open for two years was closed in the same engagement.")


FAQS = [
    ("Who sets up Microsoft 365 for businesses on the Gold Coast?",
     "bcom ICT migrates, configures and supports Microsoft 365 for businesses across the Gold Coast and Australia-wide, covering email migration, Teams, SharePoint and OneDrive, with security baselines and multi-factor authentication enabled from day one. bcom ICT is a Microsoft Partner. Call 07 3041 8993."),
    ("Where does our data actually live?",
     "For Microsoft 365 tenancies we provision in the Australian regions, so your mail and files are stored in Australian data centres. This matters more than most businesses realise — it's a routine question from insurers, larger clients and anyone in a regulated industry. Our data handling page sets out where everything sits, including backups."),
    ("How long does a migration take?",
     "For a typical small business, planning takes a week or two and the cutover happens over a weekend. Larger or messier environments take longer, mainly because of mapping rather than moving. We'd rather spend the extra time up front than discover a problem after the old system is gone."),
    ("Will we lose email during the move?",
     "No. Mail continues flowing throughout and nothing is switched off until we've verified everything came across. The old system stays available for a period afterwards as a safety net."),
    ("Should we use Microsoft 365 or Google Workspace?",
     "Whichever fits how you already work. Microsoft 365 tends to suit businesses using Office documents heavily, needing Teams calling, or with compliance requirements. Google Workspace suits businesses living in browsers and collaborating in real time. Migrating between them for its own sake is rarely worth the disruption."),
    ("Do we still need backup if we're in the cloud?",
     "Yes, and this is the most common misunderstanding we run into. Microsoft protects the platform from failing; it does not protect you from someone deleting a mailbox, a ransomware infection encrypting synced files, or a departing staff member wiping a folder. Separate backup of Microsoft 365 is a genuine requirement, not an upsell."),
    ("Can staff work from anywhere once we've moved?",
     "That's usually the main reason businesses move. Email, files and Teams work from the office, from home, or from a phone — with the same security applied wherever people are, rather than security that only exists inside the building."),
]

PRICING = [
    ('Migration', 'Quoted', 'after assessment &middot; fixed price',
     [
      'Mailbox moved with mail, calendar and contacts intact',
      'Licence assigned and multi-factor authentication enforced',
      'Desktop, laptop and mobile set up and tested',
      'The old mail system decommissioned once you are satisfied',
     ]),
]

PAGE = {
    "path": "/cloud-computing-service-gold-coast",
    "priority": "0.85",
    "service": "Cloud Migration Gold Coast",
    "title": "Cloud & Microsoft 365 for Gold Coast Business | bcom ICT",
    "description": "Cloud migration and Microsoft 365 for Gold Coast businesses — email migration, Teams, SharePoint, Azure and Google Workspace, with Australian data residency. Call 07 3041 8993.",
    "hero_img": "cloud-migration-hero.webp",
    "hero_alt": "A bcom ICT consultant planning a Microsoft 365 cloud migration with a Gold Coast business team",
    "h1": "Cloud and Microsoft 365, set up properly",
    "lede": "Email, files and Teams moved across without the disruption — configured securely from day one, with your data held in Australia.",
    "actions": [("Talk to us", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Microsoft Partner", "Australian data residency", "Weekend cutovers", "MFA from day one"],
    "crumbs": [("Services", "/services"), ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT migrates and manages cloud environments for Gold Coast businesses — Microsoft
    365, Microsoft Azure, Google Workspace and hybrid setups. bcom ICT plans the move, migrates data and
    users over a weekend cutover, and supports it afterwards, with Microsoft 365 tenancies provisioned in
    Australian regions. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">What we do</span>
      <h2>The cloud work Gold Coast businesses ask for</h2>
    </div>
    <div class="grid grid--3">{cards(WORK)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Migrating</span>
      <h2>How we move a business across</h2>
      <p>Most migration horror stories come from moving before mapping. The sequence below is deliberately front-loaded.</p>
    </div>
    <div class="grid grid--4">{steps(MOVE)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>Two things people get wrong about the cloud</h2>
        <p style="margin-top:16px"><strong>"It's backed up because it's in the cloud."</strong> It isn't. Microsoft guarantees the platform stays up — that's a completely different thing from protecting your data. If a staff member deletes a mailbox, ransomware encrypts files that sync to OneDrive, or someone empties a SharePoint library, Microsoft's retention windows are short and unforgiving. Separate <a href="/data-backup-recovery-gold-coast">backup of Microsoft 365</a> is a real requirement.</p>
        <p style="margin-top:16px"><strong>"It's secure by default."</strong> It's securable by default, which is not the same. A new Microsoft 365 tenancy ships with multi-factor authentication not fully enforced, legacy authentication paths open, and sharing settings wide. We close those as part of setup, because that gap is exactly where account takeovers come from.</p>
        <p style="margin-top:24px">Both of those are things we'd rather tell you up front than discover with you later.</p>
      </div>
      {photo("microsoft-365-setup-gold-coast-content.webp", "Microsoft 365 being configured for a Gold Coast business by bcom ICT", "Security baselines and MFA are applied during setup, not bolted on afterwards.")}
    </div>

    <div class="rule">{MARK}</div>

    <h2>Where your data sits</h2>
    <p style="margin-top:16px">"Where does our data live?" is now a standard question from insurers, larger clients and anyone in a regulated industry — and a lot of providers answer it vaguely. We don't. Microsoft 365 tenancies are provisioned in Australian regions, and we'll tell you exactly where your backups are held as well. Our <a href="/data-handling-and-sovereignty">data handling and sovereignty page</a> sets all of it out.</p>

    {trust_note('bcom ICT is a Microsoft Partner. Cloud environments we manage are maintained against the ASD Essential Eight and aligned with ISO/IEC 27001:2022 practices — <a href="/trust-centre">the trust centre</a> sets out what that alignment does and does not mean.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The Microsoft 365 problems we are actually called about</h2>
      <p>Most cloud faults are configuration or licensing rather than the platform failing. These are the six we see most.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What these engagements actually look like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>


<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>How much does a Microsoft 365 migration cost?</h2>
      <p>Scoped first, then quoted as a fixed price agreed before work starts. We do not publish a per-user figure, and the reason is worth reading.</p>
    </div>
    {price_table(PRICING, note='We do not publish a per-user figure for migrations, because the gap between an easy one and a difficult one is wider than any average would usefully describe. What decides it: how much mail history is coming across, whether shared mailboxes and public folders are involved, whether files are moving to SharePoint or OneDrive at the same time, and how cooperative the system being left behind turns out to be. We scope first and then quote a fixed price, because a migration billed by the hour is a quote that only ever moves in one direction.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Microsoft 365 Setup & Support", "/microsoft-365-setup-gold-coast"),
  ("Microsoft Copilot", "/microsoft-copilot-gold-coast"),
  ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast"),
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
  ("Data handling & sovereignty", "/data-handling-and-sovereignty"),
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
])}

{cta("Thinking about moving to the cloud?",
     "We'll map what you're running now and tell you what's worth moving, what isn't, and what the cutover actually involves.")}
''',
}

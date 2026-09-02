from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues

MS = [
    "<strong>Your staff live in Excel or Word.</strong> The desktop applications are still meaningfully better than the browser equivalents, and for anyone doing real work in a spreadsheet that difference is the whole argument.",
    "<strong>Your industry software expects it.</strong> Practice management, accounting, conveyancing and trades platforms in Australia overwhelmingly integrate with Outlook and Microsoft 365 first, and sometimes only.",
    "<strong>You have compliance obligations.</strong> Retention policies, legal hold, audit logging, data loss prevention and sensitivity labelling are deeper, and matter for AFS licensees, health providers and anyone answering security questionnaires.",
    "<strong>You run Windows machines.</strong> Device management, single sign-on and policy enforcement are a single joined-up story rather than a set of add-ons.",
]

GOOG = [
    "<strong>People genuinely work together in documents.</strong> Real-time collaboration was built in from the start rather than added, and it still shows.",
    "<strong>You want less to administer.</strong> Fewer moving parts, fewer overlapping products doing similar jobs, and less scope to configure something into a corner.",
    "<strong>Everyone works in a browser anyway.</strong> If nobody opens a desktop application, you are paying for capability you never touch.",
    "<strong>You are starting from nothing.</strong> A new business with no legacy files, no Outlook habits and no industry software to satisfy has a genuinely open choice.",
]

MISTAKES = [
    ("&ldquo;They are basically the same now&rdquo;",
     "true at the surface and false where it counts. Both do mail, files, chat and video. The differences are in the desktop applications, the compliance tooling and what your other software expects.",
     "Decide on the two or three things your business actually depends on, not on the feature grid. Most of the grid is irrelevant to any given business."),
    ("&ldquo;We will pick whichever is cheaper&rdquo;",
     "a per-user comparison that ignores migration cost, retraining, and whether your line-of-business software integrates. The licence is rarely the expensive part.",
     "Cost the whole move, including the weeks of reduced productivity while people relearn where things are. That is usually larger than several years of licence difference."),
    ("&ldquo;We can move later if it does not work&rdquo;",
     "technically true and practically painful. Mail history, shared drives, permissions and years of links inside documents all have to come across, and some of it will not.",
     "Treat this as a decision you will live with for five years, because you probably will. It is worth an hour of proper thought at the start."),
    ("&ldquo;Our accountant said to use one of them&rdquo;",
     "advice that may be right for their business rather than yours. It is worth knowing why they said it.",
     "Ask what specifically drove their recommendation. If it is an integration you also need, that is a real reason. If it is habit, it is not."),
    ("&ldquo;We will run both&rdquo;",
     "usually the worst outcome. Two mail systems, two file stores, two sets of permissions and staff who never know where anything is.",
     "Pick one and commit. The only defensible exception is a transition period with a hard end date already in the calendar."),
]

FAQS = [
    ("Microsoft 365 or Google Workspace for an Australian small business?",
     "Microsoft 365 suits most Australian small businesses, mainly because the desktop Office applications are still better for real spreadsheet and document work and because Australian industry software — practice management, accounting, conveyancing, trades platforms — integrates with Outlook and Microsoft first. Google Workspace is the better answer where everyone works in a browser, collaboration is constant, and there is no legacy software to satisfy. bcom ICT migrates businesses to and from both."),
    ("Which is cheaper?",
     "Entry-level Google Workspace is typically slightly cheaper per user, and the difference is small enough that it should not decide this. The larger costs are migration, retraining and whether your other software integrates cleanly, all of which dwarf a few dollars a seat per month."),
    ("Does either keep our data in Australia?",
     "Both offer Australian data residency for core services, and the detail varies by service and by how the tenancy is provisioned. If it matters to you — and for health providers, AFS licensees and government suppliers it usually does — it should be established per service before you commit rather than assumed."),
    ("Can we move from Google Workspace to Microsoft 365?",
     "Yes, and we do it regularly. Mail, calendars and contacts move cleanly. Files move but shared-drive permissions and links inside documents need attention, and that is where a migration either goes well or generates months of small complaints."),
    ("What about Teams versus Google Meet?",
     "Teams is more than a meeting tool — it carries chat, files and increasingly telephony, which is why it tends to become the centre of a Microsoft business. Meet is a better meeting tool for many people and a smaller product overall. If you want phone calls inside the same application your staff already use, that points to Microsoft."),
    ("Does bcom ICT prefer one?",
     "We migrate more businesses to Microsoft 365 than to Google Workspace, and that reflects what Australian small businesses ask for rather than a position we hold. We support both, and we have advised clients to stay on Google where moving would have cost them more than it returned."),
]

PAGE = {
    "path": "/microsoft-365-vs-google-workspace",
    "priority": "0.8",
    "title": "Microsoft 365 vs Google Workspace | bcom ICT",
    "description": "An honest comparison for Australian small business — where Microsoft 365 genuinely wins, where Google Workspace does.",
    "hero_img": "compare-m365-google-hero.webp",
    "hero_alt": "A Gold Coast business team working across Microsoft 365 applications",
    "eyebrow": "Comparison",
    "h1": "Microsoft 365 or Google Workspace?",
    "lede": "A decision most businesses make once and live with for years. Here is what actually separates them, and the costs that matter more than the price per seat.",
    "crumbs": [("Services", "/services"), ("Microsoft 365 vs Google Workspace", "/microsoft-365-vs-google-workspace")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">Microsoft 365 suits most Australian small businesses, largely because the desktop Office
    applications remain better for real document and spreadsheet work and because Australian industry software
    integrates with Outlook and Microsoft first. Google Workspace is the better choice where everyone works in
    a browser, collaboration is constant and there is no legacy software to satisfy. bcom ICT migrates
    businesses to and from both. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">The licence price is the least important number</h2>
    <p style="margin-top:16px">Comparisons of these two usually open with a per-user price, which is the wrong
    place to start. The difference is a few dollars a seat a month. The migration, the retraining and whether
    your other software integrates cleanly are each worth more than several years of that difference.</p>
    <p style="margin-top:16px">What actually separates them is narrower than the marketing suggests. Both do
    mail, files, chat, video and storage competently. Three things genuinely differ: <strong>the desktop
    applications</strong>, <strong>the compliance tooling</strong>, and <strong>what everything else you run
    expects to talk to</strong>.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Choose Microsoft when</span>
      <h2>Microsoft 365 is the better answer here</h2>
    </div>
    {ticks(MS)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Choose Google when</span>
      <h2>And Google Workspace is the better answer here</h2>
    </div>
    {ticks(GOOG)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>The question that decides it for most Australian businesses</h2>
    <p style="margin-top:16px">What does your industry software integrate with? Practice management for a
    medical or allied health clinic, trust accounting for an agency, conveyancing for a law firm, job
    management for a trades business &mdash; look at what those platforms support properly, not what they
    claim to support.</p>
    <p style="margin-top:16px">In Australia the answer is overwhelmingly Microsoft first, sometimes Microsoft
    only. That single fact decides this for more small businesses than every feature comparison combined, and
    it is worth ten minutes on your vendor's documentation before anyone talks to you about collaboration.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common mistakes</span>
      <h2>What people get wrong deciding this</h2>
    </div>
    {issues(MISTAKES)}

    {trust_note('Whichever you choose, the security baseline matters more than the badge. Multi-factor authentication on every account, sharing defaults that are not "anyone with the link", and a backup of the tenancy — see <a href="/microsoft-365-setup-gold-coast">Microsoft 365 setup</a> and <a href="/data-backup-recovery-gold-coast">backup and recovery</a>.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Microsoft 365 Setup & Support", "/microsoft-365-setup-gold-coast"),
  ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast"),
  ("Microsoft Copilot", "/microsoft-copilot-gold-coast"),
  ("Data Backup & Recovery", "/data-backup-recovery-gold-coast"),
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
], heading="Related")}

{cta("Choosing, or reconsidering?",
     "Tell us what your industry software needs to talk to. That answer decides this faster than any feature comparison.")}
''',
}

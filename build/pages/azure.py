from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues, example

USES = [
    ("A server that has to stay a server", None, "A line-of-business application that needs Windows and will not move to a hosted version. Azure runs it without you owning the hardware or the room it sits in."),
    ("Virtual desktops", None, "Azure Virtual Desktop suits businesses with contractors, seasonal staff or people on their own laptops — the desktop lives in Azure and the device becomes a screen."),
    ("Backup and disaster recovery", None, "A second copy of a server that is genuinely somewhere else, and the ability to bring it up in Azure if the office is unavailable."),
    ("Identity", None, "Microsoft Entra ID is already underneath your Microsoft 365 tenancy. Using it properly for single sign-on and conditional access is usually free capability nobody has turned on."),
]

ISSUES = [
    ("&ldquo;Azure will be cheaper than a server&rdquo;",
     "a comparison of a monthly bill against hardware that was bought years ago and written down. A steady always-on workload frequently costs more per year in Azure than owning the equivalent box.",
     "Model three years of actual running cost, including the connection. Azure earns its place on flexibility and resilience far more often than on price, and choosing it for the wrong reason leads to an unpleasant second year."),
    ("&ldquo;The bill went up and nobody knows why&rdquo;",
     "resources left running that nobody owns &mdash; a test environment from a project that finished, a virtual machine somebody spun up to try something, storage that grows because nothing deletes.",
     "Tag everything to an owner and a purpose, set budget alerts, and review monthly. Azure has no natural brake on spending, which is the trade for having no capacity planning."),
    ("&ldquo;We lifted the server straight across&rdquo;",
     "a like-for-like move of a machine sized for a physical server, running twenty-four hours a day because that is what physical servers do.",
     "Right-size it after the move and shut down what does not need to run overnight. A lift-and-shift is a reasonable first step and an expensive final state."),
    ("&ldquo;Where is our data actually held?&rdquo;",
     "a fair question and one that depends on how the tenancy and each service were provisioned rather than on Azure in general.",
     "Establish the region per service and record it. For health providers, AFS licensees and government suppliers this is something you will be asked to evidence rather than assert."),
    ("&ldquo;Everyone is a global administrator&rdquo;",
     "roles handed out during setup for convenience and never narrowed. It is the most common finding in an Azure or Entra tenancy we inherit.",
     "Assign the least privilege that works, require multi-factor authentication on every administrative account, and review who holds what. This costs nothing and closes the largest exposure in most tenancies."),
    ("&ldquo;If Azure is down, we are down&rdquo;",
     "a single-region deployment with no failover, which is what most small business Azure looks like and is often a reasonable trade.",
     "Decide deliberately how much resilience you are buying rather than assuming the cloud provides it by default. Redundancy across regions costs real money and many businesses genuinely do not need it."),
]

EXAMPLE_1 = example(
    "Nine hundred dollars a month of nothing in particular",
    "A business asked us to review an Azure tenancy that had been growing steadily for two years. Nobody had done anything unusual; the bill had simply climbed and no single month had increased enough to trigger a conversation.",
    "Roughly a third of the spend was on resources nobody owned. A test environment from a project completed eighteen months earlier was still running around the clock. Two virtual machines had been created to try something and never removed. Storage had accumulated snapshots with no lifecycle policy, so nothing had ever been deleted. Separately, the production machine had been lifted straight across from physical hardware and sized accordingly, running twenty-four hours a day for a workload used between eight and six on weekdays.",
    "Tagged every resource to an owner and a purpose, removed what nothing depended on after confirming with each team, applied a lifecycle policy to the storage, right-sized the production machine and set a schedule so it powers down overnight. Added budget alerts so a future increase surfaces in a month rather than in a year.",
    "Monthly spend fell by a little over nine hundred dollars with no loss of capability. Azure has no natural brake on spending &mdash; that is the trade for having no capacity planning &mdash; which is why tagging and a monthly review are part of running it rather than optional housekeeping.")
FAQS = [
    ("Does bcom ICT work with Microsoft Azure?",
     "Yes. bcom ICT deploys and supports Azure for Australian businesses — hosting line-of-business servers, Azure Virtual Desktop, backup and site recovery, and Microsoft Entra ID for identity and conditional access. We also advise against Azure where it is the wrong answer, which for a single always-on server in a business with one office it frequently is."),
    ("Is Azure cheaper than running our own server?",
     "For a steady, always-on workload, often no. Owning hardware for three to five years can cost less than the equivalent Azure resource running continuously. Azure wins on flexibility, on not owning a server room, on bringing systems up somewhere else after an incident, and on scaling without a capacity decision. Those are good reasons; price usually is not."),
    ("What is Azure Virtual Desktop useful for?",
     "Businesses with contractors, seasonal staff, or people using their own laptops. The desktop and the data stay in Azure and the device becomes a screen, so a departing contractor hands back nothing and a lost laptop carries nothing. It suits variable headcount far better than it suits a fixed team who all have company machines."),
    ("Where is our Azure data stored?",
     "In the region the resource was provisioned into, which for Australian businesses should generally be an Australian region. It is set per resource rather than globally, so it needs establishing and recording rather than assuming — particularly for health providers, AFS licensees and anyone answering a security questionnaire."),
    ("Why did our Azure bill increase?",
     "Almost always resources nobody owns. A test environment from a finished project, a machine somebody created to try something, or storage growing because nothing ever deletes. Azure has no natural brake on spending, so tagging by owner, budget alerts and a monthly review are not optional extras."),
    ("Can you take over an Azure tenancy someone else set up?",
     "Yes. We audit who holds administrative roles — which is where we usually find the largest exposure — check what is running against what is needed, establish the data residency position per service, and put cost controls in place. Inherited tenancies are where we most often find several global administrators and no multi-factor authentication on any of them."),
]

PAGE = {
    "path": "/azure-cloud-services-gold-coast",
    "priority": "0.8",
    "service": "Microsoft Azure Services Gold Coast",
    "title": "Microsoft Azure for Australian Business | bcom ICT",
    "description": "Azure deployment and support for Gold Coast businesses — hosted servers, Azure Virtual Desktop, backup and site recovery, Entra ID.",
    "hero_img": "azure-hero.webp",
    "hero_alt": "A bcom ICT consultant reviewing cloud infrastructure options with a Gold Coast business",
    "eyebrow": "Microsoft",
    "h1": "Azure, when it is genuinely the right answer",
    "lede": "It is rarely cheaper than owning a server, and that is not the reason to choose it. Here is what it is actually good at, and where we would tell you not to bother.",
    "actions": [("Talk it through", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Hosted servers & AVD", "Backup & site recovery", "Entra ID & access", "Cost controls from day one"],
    "crumbs": [("Services", "/services"), ("Microsoft Azure", "/azure-cloud-services-gold-coast")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT deploys and supports Microsoft Azure for Australian businesses — hosting
    line-of-business servers, Azure Virtual Desktop, backup and site recovery, and Microsoft Entra ID for
    identity and conditional access. Azure is rarely cheaper than owning a server for a steady workload, and
    we will say so. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">The cheaper argument is usually wrong</h2>
    <p style="margin-top:16px">Azure gets sold on cost and that is the weakest case for it. A server running
    around the clock, doing the same work every day, is close to the worst possible fit for consumption pricing
    &mdash; you are renting capacity you use continuously, which over three to five years frequently costs more
    than buying the box.</p>
    <p style="margin-top:16px">What Azure is genuinely good at is everything that is awkward about owning
    hardware. You do not need a room for it, or power and cooling, or a plan for the day the building is
    unavailable. You can bring a failed system up somewhere else. You can add capacity on a Tuesday without a
    purchase order. And for a business with contractors or variable headcount, you can give somebody a desktop
    without giving them a device.</p>
    <p style="margin-top:16px">Those are the reasons to choose it. If the pitch you were given was purely about
    price, ask to see the three-year model.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Where it earns its place</span>
      <h2>What Australian small businesses actually use Azure for</h2>
    </div>
    <div class="grid grid--2">{cards(USES, icon=True)}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What goes wrong in a small business Azure tenancy</h2>
      <p>Six, and the fifth is the one we find in almost every tenancy we inherit.</p>
    </div>
    {issues(ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>Where we would tell you not to</h2>
    <p style="margin-top:16px">A single office, one always-on server running a line-of-business application, a
    connection that is adequate rather than excellent, and no requirement to work from anywhere else. That
    business is usually better served by replacing the server &mdash; see
    <a href="/windows-server-migration-gold-coast">Windows Server migration</a> &mdash; and spending the
    difference on backup that actually works.</p>
    <p style="margin-top:16px">We have advised against moving a production system to Azure where the
    application had a hard latency requirement and sat next to the equipment it controlled. That
    recommendation cost us the larger piece of work and it was the only defensible advice.</p>

    {trust_note('If the case for Azure is resilience, the honest comparison is against what good backup and a tested recovery would cost you instead. Frequently that is the better spend &mdash; see <a href="/data-backup-recovery-gold-coast">backup and disaster recovery</a>.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What an Azure review usually finds</h2>
      <p>A representative engagement, drawn from real work with client and staff names removed.</p>
    </div>
    {EXAMPLE_1}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Windows Server Migration", "/windows-server-migration-gold-coast"),
  ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast"),
  ("Microsoft 365 Setup & Support", "/microsoft-365-setup-gold-coast"),
  ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast"),
  ("Data handling & sovereignty", "/data-handling-and-sovereignty"),
], heading="Related")}

{cta("Been quoted for an Azure move?",
     "Send us the numbers. We will model it against replacing the server over three years and tell you which one actually wins.")}
''',
}

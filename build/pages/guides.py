from layout import MARK, cta, faq_block, cards, related, trust_note

# Grouped by what the reader is trying to do, not by format. A comparison and a
# checklist can answer the same kind of question; a reader looking for help
# choosing a provider should not have to know which format it was written in.

CHOOSING_PROVIDER = [
    ("How to choose an IT provider", "/how-to-choose-an-msp-gold-coast",
     "Eight questions worth asking any managed IT provider before you sign, including us. What a good answer "
     "sounds like, and which answers should end the conversation."),
    ("What IT support actually costs", "/it-support-cost-gold-coast",
     "Hourly rates, call-out fees and how managed IT gets priced on the Gold Coast, with the numbers a "
     "quote should contain and the ones it usually leaves out."),
    ("Managed IT or pay-as-you-go?", "/managed-it-vs-break-fix",
     "What each model costs across a year rather than a month, whose incentives each one rewards, and which "
     "businesses are genuinely better off paying by the job."),
]

CHOOSING_TECH = [
    ("Microsoft 365 or Google Workspace?", "/microsoft-365-vs-google-workspace",
     "Where each genuinely wins for a small Australian business, and why the answer usually comes down to "
     "the software you already run rather than email."),
    ("Cloud phone system, or keep the PBX?", "/voip-vs-pbx-phone-systems",
     "When a working PBX is worth keeping, when it is costing you more than it looks, and what a cloud "
     "system changes on the day you move."),
    ("NAS or cloud backup?", "/nas-vs-cloud-backup",
     "What a box in the office protects you from, what it does not, and why most businesses that can afford "
     "either should be running both."),
    ("UniFi or Aruba Instant On?", "/unifi-vs-aruba-instant-on",
     "Business WiFi compared by someone who installs both: where each suits, what each costs to run, and "
     "which one to pick when nobody on staff wants to manage it."),
]

PLANNING = [
    ("Office move IT checklist", "/office-move-it-checklist",
     "Everything that has to happen before moving day, in order and by lead time. Carrier orders are the "
     "item that sinks most moves, and they need starting weeks earlier than people expect."),
    ("Business NBN, explained plainly", "/business-nbn-guide-gold-coast",
     "Connection types, business-grade versus residential plans, and what to check before you sign a "
     "contract that will outlast the lease."),
    ("When is a business computer past it?", "/business-computer-replacement-cycle",
     "How to judge replacement on what a machine costs you while it still works, rather than waiting for "
     "the day it stops."),
]

FAQS = [
    ("Are the bcom ICT guides written to sell you something?",
     "They are written to be useful whether or not you hire us. The provider guide tells you to ask every "
     "question in it of bcom ICT as well, and several of the comparisons conclude that the cheaper option or "
     "the one you already have is the right call. A guide that only ever arrived at our services would not "
     "be worth reading."),
    ("Where should a business start when choosing an IT provider?",
     "Start with how to choose an IT provider, which sets out the questions that separate a good provider "
     "from a confident one. Then read what IT support costs, so a quote can be judged against realistic "
     "numbers, and managed IT versus pay-as-you-go to decide which model you are buying before comparing "
     "anyone's price."),
    ("Is advice on which technology to choose free?",
     "The guides are free to read, and so is the first conversation with bcom ICT and the systems review "
     "that usually follows it. You get a plain-English view of what suits your business, and you keep it "
     "whether or not you engage us. Call 07 3041 8993."),
    ("Do the guides apply outside the Gold Coast?",
     "Almost all of it does. The comparisons, the provider questions and the planning checklists apply to "
     "any Australian business. The Gold Coast detail is mostly in the costs guide, where on-site rates "
     "reflect attending locally, and in the NBN guide where local connection types come up."),
]

PAGE = {
    "path": "/guides",
    "priority": "0.7",
    "title": "IT Guides for Gold Coast Businesses | bcom ICT",
    "description": "Plain-English IT guides for Australian businesses: choosing a provider, what support costs, "
                   "honest technology comparisons and planning checklists.",
    "hero_img": "hero-bg-consulting.webp",
    "hero_alt": "A team meeting in a Gold Coast office, with a presenter at a screen and the ocean visible through the windows",
    "h1": "Straight answers to the questions businesses ask us",
    "lede": "Eleven guides for choosing a provider, choosing technology and planning ahead. "
            "Written to be useful whether or not you ever hire us.",
    "actions": [("Talk it through", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["No sign-up to read", "Honest comparisons", "Australian context", "Reviewed September 2026"],
    "crumbs": [("Guides", "/guides")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT publishes free, plain-English IT guides for Australian businesses: how to
    choose an IT provider, what IT support costs, managed IT versus pay-as-you-go, comparisons of Microsoft
    365 and Google Workspace, cloud and PBX phone systems, NAS and cloud backup, and UniFi and Aruba WiFi,
    plus checklists for office moves, business NBN and computer replacement. Call 07 3041 8993.</p>

    <div class="urgent" role="note" style="margin-top:48px">
      <div>
        <h2>Been hacked, or think you might have been?</h2>
        <p>Disconnect the affected machines from the network, but don&rsquo;t switch them off, and
        don&rsquo;t delete anything. Shutting down destroys evidence that helps work out what happened.
        Then follow the steps in order.</p>
        <a class="btn btn--primary" href="/what-to-do-when-hacked">What to do in the first hour {MARK}</a>
      </div>
    </div>

    <div class="section-head" style="margin-top:72px">
      <span class="eyebrow">Choosing a provider</span>
      <h2>Before you sign with anyone</h2>
      <p>Three guides that make a quote easier to judge, and a provider easier to question.</p>
    </div>
    <div class="grid grid--3">{cards(CHOOSING_PROVIDER, icon=False, more="Read the guide")}</div>

    <div class="section-head" style="margin-top:72px">
      <span class="eyebrow">Choosing technology</span>
      <h2>Honest comparisons</h2>
      <p>Each one written by someone who installs both options, and each willing to conclude that the
      cheaper one, or the one you already have, is the right call.</p>
    </div>
    <div class="grid grid--2">{cards(CHOOSING_TECH, icon=False, more="Read the comparison")}</div>

    <div class="section-head" style="margin-top:72px">
      <span class="eyebrow">Planning ahead</span>
      <h2>For the change you can see coming</h2>
      <p>Moves, connections and hardware, where the cost of getting it wrong arrives months after the
      decision.</p>
    </div>
    <div class="grid grid--3">{cards(PLANNING, icon=False, more="Read the guide")}</div>

    {trust_note("Every guide carries its own review date, and prices and figures are checked against their sources before that date is bumped. If something here is out of date, tell us and we will correct it.")}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Services", "/services"),
  ("Pricing", "/pricing"),
  ("Case studies", "/case-studies"),
  ("Trust centre", "/trust-centre"),
], heading="Related")}

{cta("Rather just ask?",
     "Guides only go so far. Tell us what you are weighing up and we will give you a straight answer, including when the answer is that you don&rsquo;t need us.")}
''',
}

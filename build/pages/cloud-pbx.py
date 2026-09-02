from layout import MARK, cta, faq_block, cards, ticks, steps, related, trust_note, price_table, issues, example

# Every figure and capability here is published on click2call.com.au, which
# trades as Bcom Services Pty Ltd — the same legal entity and ABN as bcom ICT.
# That is the whole point of the page and it is publicly verifiable.

PLATFORM = [
    ("Cloud PBX", None, "Ring groups, IVR menus, call queues, voicemail, hold music and call recording. Managed from a browser, with nothing to rack."),
    ("AI receptionist", None, "Answers around the clock in your business name, asks what the caller needs and routes them. It says what it is rather than pretending to be a person."),
    ("AI voice tools", None, "Every call transcribed, summarised and sentiment-scored, so the notes write themselves and nothing is remembered wrongly."),
    ("Microsoft Teams calling", None, "Direct Routing, so real phone calls happen inside Teams on the Microsoft 365 licences you already pay for."),
    ("Multi-site routing", None, "One numbering plan across offices, with calls following people rather than desks."),
    ("Number porting", None, "Local, mobile, 1300 and 1800 numbers brought across, handled end to end."),
]

PRICING = [
    ("Per user, per month", "$25", "+ GST",
     ["A local number and 300 outbound minutes included",
      "Desk phone, laptop and mobile &mdash; the same extension on all three",
      "No lock-in contract",
      "Seven-day free trial, no card required"]),
    ("Inbound only", "$10", "+ GST per month",
     ["A published number that rings wherever you are",
      "Suits a second line, a tracked number, or an after-hours line",
      "AI receptionist available on it"]),
]

PRICE_NOTE = ('Handsets, cabling and on-site installation are separate and quoted after we have seen the site '
              '&mdash; see <a href="/business-phone-systems-gold-coast">business phone systems</a> for what an '
              'installed system looks like. A business running softphones on the computers and mobiles it already '
              'owns pays for no hardware at all. Managed setup, where you would rather we configured the whole '
              'thing than do it in the portal yourself, starts at $300 + GST.')

ROLLOUT = [
    ("We check the connection first",
     "Voice needs consistency more than speed, and a connection that passes a speed test can still be unusable for a call. We measure latency variation and packet loss before anything is ordered, because that is the one thing that decides whether this works."),
    ("Numbers get checked against the record",
     "Most porting delays are administrative — a trading name where the losing provider has a registered entity, or a service address changed years ago. We reconcile that before submitting, not after a rejection."),
    ("It gets built and tested before cutover",
     "Call flow, hunt groups, after-hours routing and voicemail are configured and tested while your old system is still running, so the switch is a switch rather than a project."),
    ("You are shown how to change it",
     "The after-hours greeting, the call flow, who rings when — documented and demonstrated. A phone system only its installer can operate is a dependency, not a service."),
]

FAQS = [
    ("Does bcom ICT run its own phone platform?",
     "Yes. bcom ICT and Click2Call are the same company — Click2Call is a trading name of Bcom Services Pty Ltd, ABN 92 636 893 108, the same entity and ABN behind bcom ICT. The cloud PBX your phones run on is built and operated in-house rather than resold from another provider, which means a fault does not have to travel through a vendor before someone who can fix it hears about it."),
    ("How much does a cloud phone system cost?",
     "$25 + GST per user per month, including a local number and 300 outbound minutes, with no lock-in contract. An inbound-only number is $10 + GST per month. There is a seven-day free trial with no card required. Handsets, cabling and on-site installation are separate and quoted after we know what the site needs."),
    ("Where is our call data held?",
     "On Australian-hosted infrastructure, with data kept in Australia and New Zealand. Calls route through Australian data centres rather than taking international hops, which is why the audio holds up."),
    ("Can we keep our existing numbers?",
     "Yes — local, mobile, 1300 and 1800 numbers are all portable, and porting is handled end to end. Getting the account details to match the losing provider's records exactly is the part that decides whether a port runs on time, and it is the part we do before submitting anything."),
    ("Do we need to buy handsets?",
     "No. The same extension works on a mobile, a laptop and a desk phone, so a business that does not want handsets pays for none. Where desk phones do make sense — reception, a counter, a workshop — we supply and install them and quote that separately from the monthly service."),
    ("Can it work with Microsoft Teams?",
     "Yes, through Direct Routing. Staff make and take real phone calls inside Teams using the Microsoft 365 licences the business already holds, with no second application to learn."),
    ("What if we already have a PBX?",
     "It can stay. A hybrid arrangement — the existing system for the office and cloud extensions for people outside it, joined so one published number reaches whoever is free — is frequently a fraction of a full replacement. We support legacy Panasonic, NEC, LG Ericsson and Alcatel-Lucent systems as well, so the advice is not shaped by what we would rather sell."),
]

PAGE = {
    "path": "/cloud-pbx-gold-coast",
    "priority": "0.9",
    "service": "Cloud PBX Gold Coast",
    "title": "Cloud PBX Gold Coast — We Own the Platform | bcom ICT",
    "description": "bcom ICT runs its own AI-powered cloud PBX, built and operated in-house rather than resold. Call 07 3041 8993.",
    "hero_img": "cloud-pbx-hero.webp",
    "hero_alt": "A Gold Coast business team using a cloud phone system on desk phones, laptops and mobiles",
    "h1": "Most IT providers resell a phone system. We built one.",
    "lede": "bcom ICT operates its own AI-powered cloud PBX — Australian-hosted, $25 + GST a user, and no vendor sitting between you and the people who can fix it.",
    "actions": [("See how it works", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Our own platform", "Australian-hosted", "$25 + GST per user", "No lock-in"],
    "crumbs": [("Services", "/services"), ("Cloud PBX", "/cloud-pbx-gold-coast")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT operates its own AI-powered cloud PBX rather than reselling another provider's.
    The platform trades as Click2Call, a trading name of Bcom Services Pty Ltd — the same company and the same
    ABN as bcom ICT. It is $25 + GST per user per month including a local number and 300 outbound minutes,
    Australian-hosted, with no lock-in contract. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">Same company, same ABN</h2>
    <p style="margin-top:16px">Almost every IT provider that sells you a phone system is reselling somebody
    else's. That is not a criticism &mdash; it is how the industry works. It does mean that when something
    breaks, your provider raises a ticket with their vendor, and you wait at the end of a chain you cannot see.</p>
    <p style="margin-top:16px">Ours is built and run in-house. Click2Call is a trading name of Bcom Services
    Pty Ltd, ABN 92 636 893 108 &mdash; the same legal entity behind bcom ICT, which you can
    <a href="https://abr.business.gov.au/ABN/View?abn=92636893108" rel="nofollow">check on the ABN register</a>
    rather than take our word for. The people who answer the phone about a fault are the people who can change
    the platform.</p>

    {trust_note('It also means we are unusual in doing both halves. The platform is ours, and so is the cabling, the switching, the handsets and the network the calls actually cross &mdash; which is where most voice quality problems live.')}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The platform</span>
      <h2>What it does</h2>
      <p>Set up online in under an hour, managed from a browser, on Australian infrastructure.</p>
    </div>
    <div class="grid grid--3">{cards(PLATFORM)}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>The AI part, specifically</h2>
    <p style="margin-top:16px">Plenty of phone systems now claim artificial intelligence. Here is exactly what
    ours does, so you can judge whether any of it is useful to you rather than take the word on trust.</p>
    {ticks([
      "<strong>It answers when nobody can.</strong> The AI receptionist greets callers in your business name, asks what they need and routes them &mdash; at nine on a Sunday as readily as at eleven on a Tuesday.",
      "<strong>It says what it is.</strong> Ours identifies itself as an AI rather than presenting as a person. Callers mind far less about talking to a machine than about discovering afterwards that they were.",
      "<strong>It writes the notes.</strong> Every call is recorded, transcribed and summarised, so what was agreed is a record rather than a recollection.",
      "<strong>It reads the room, roughly.</strong> Sentiment scoring across calls surfaces the ones worth listening back to, which is more useful than a folder of recordings nobody opens.",
      "<strong>It is not a replacement for your staff.</strong> Urgent calls should reach a person, and the escalation path for that is a decision to make before anything goes live rather than after.",
    ])}
    <p style="margin-top:28px;max-width:68ch">These were enterprise capabilities on enterprise budgets a few
    years ago. That they now sit on a $25 line is the genuinely interesting part, and it is why a
    three-person business can answer its phone the way a fifty-person one does.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>What it costs</h2>
      <p>Published, per user, per month. No lock-in and no exit fee.</p>
    </div>
    {price_table(PRICING, note=PRICE_NOTE)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Getting on it</span>
      <h2>How a change of phone system actually goes</h2>
      <p>A solo operator can do this themselves in an hour. For a team with numbers to port and a call flow that matters, this is the order it happens in.</p>
    </div>
    <div class="grid grid--4">{steps(ROLLOUT)}</div>
    <p style="margin-top:28px;max-width:68ch">Nothing here is difficult. It is just that the order matters, and
    the connection check has to come first &mdash; moving a business onto a cloud phone system across a
    connection that cannot carry voice is the one failure that no amount of configuration recovers from.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>Who it suits, and who it doesn&rsquo;t</h2>
    <p style="margin-top:16px">A solo operator or a two-person business gets a proper local number, work calls
    separated from personal ones, and an AI receptionist covering the hours nobody is free. Setup is
    self-serve and takes under an hour.</p>
    <p style="margin-top:16px">A team of three to thirty gets ring groups, IVR menus, call queues, multi-site
    routing and Teams integration, with existing numbers ported across. That is where the platform earns its
    keep, and where we would normally do the setup rather than leave it to you.</p>
    <p style="margin-top:16px">It suits you less well if your phones are tied to something the cloud cannot
    reach &mdash; a lift emergency line, a monitored alarm dialler, a fire panel. Those stay on their own path,
    and we will tell you so rather than discovering it during a changeover. See
    <a href="/phone-line-installation-cabling-gold-coast">phone line installation</a>.</p>
  </div>
</section>

{faq_block(FAQS)}

{related([
  ('Microsoft Teams Phone', '/microsoft-teams-phone-gold-coast'),
  ('VoIP vs on-premises PBX', '/voip-vs-pbx-phone-systems'),
  ("Business Phone Systems", "/business-phone-systems-gold-coast"),
  ("VoIP Phone Systems", "/voip-phone-system-installation-and-support-gold-coast"),
  ("AI Phone Agents", "/ai-voice-agent-gold-coast"),
  ("PBX Systems & Legacy Support", "/pabx-phone-systems-gold-coast"),
  ("Phone Line Installation & Cabling", "/phone-line-installation-cabling-gold-coast"),
  ("Microsoft 365", "/microsoft-365-setup-gold-coast"),
], heading="Related")}

{cta("Try it for a week",
     "Seven days, no card, and a real Australian number. If it is not right for you, nothing happens when the trial ends.")}
''',
}

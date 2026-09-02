from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues, example

ROUTES = [
    ("Direct Routing", None, "Your own carrier connects to Teams. This is what we provide through our <a href=\"/cloud-pbx-gold-coast\">own cloud PBX</a> — the numbers, the call flow and the rates stay with us rather than with Microsoft."),
    ("Operator Connect", None, "A carrier from Microsoft's list, joined to your tenancy through the admin centre. Simpler to turn on, less flexible, and you are choosing from whoever is on the list."),
    ("Microsoft Calling Plans", None, "Minutes bought from Microsoft directly. Straightforward, generally the most expensive per user, and the least flexible on numbers and routing."),
]

ISSUES = [
    ("&ldquo;Reception cannot handle calls properly in Teams&rdquo;",
     "the honest limitation. Teams is excellent for a person taking their own calls and weaker for somebody managing a busy queue, transferring constantly and watching who is free.",
     "Give reception a proper handset and a queue on the phone platform, and let everyone else use Teams. A mixed deployment is not a compromise, it is the correct design for most offices."),
    ("&ldquo;Calls drop when the laptop sleeps&rdquo;",
     "a device power setting rather than a phone system fault. Teams cannot ring a machine that has gone to sleep on the network.",
     "Adjust the power policy on machines that take calls, and make sure the mobile app is also registered so there is somewhere else for the call to land."),
    ("&ldquo;Audio is fine internally and poor on outside calls&rdquo;",
     "the path out to the carrier, not Teams. Internal calls never leave the building and are unaffected by whatever is happening on the connection.",
     "That split is diagnostic on its own. Prioritise voice traffic on the router and measure the connection for consistency rather than speed &mdash; a link that passes a speed test can still be unusable for a call."),
    ("&ldquo;We are paying for Teams Phone licences nobody uses&rdquo;",
     "licences assigned to everyone because it was simpler than deciding. Plenty of staff never make an outbound business call.",
     "Assign them to the people who actually take calls. This is the same pattern as Copilot licences and it is worth a review every renewal."),
    ("&ldquo;Our main number rings one person&rdquo;",
     "Teams set up as individual extensions without a call flow in front of them, which happens when it is turned on by somebody thinking about licences rather than about how calls arrive.",
     "Build the call flow first &mdash; who rings, in what order, what happens after hours, where voicemail goes. The licence is the easy part."),
    ("&ldquo;We want to keep our numbers&rdquo;",
     "an assumption that Teams means new numbers. It does not.",
     "Local, mobile, 1300 and 1800 numbers all port. With Direct Routing they stay on our platform, so porting and call flow are handled in one place rather than across two vendors."),
]

EXAMPLE_1 = example(
    "Teams everywhere, and a reception desk that could not cope",
    "A professional firm moved its phones entirely into Teams. Everyone got a licence, the numbers ported cleanly, and for most of the office it worked exactly as promised. Reception was a different story within a fortnight.",
    "The receptionist was handling around a hundred and twenty calls a day, transferring most of them, and needed to see at a glance who was available. Teams gave her a headset, a search box and several clicks per transfer. Nothing was broken &mdash; the software was doing what it does &mdash; but the job she was doing was one Teams is not designed around, and the queue was suffering for it.",
    "Kept Teams for the rest of the firm and gave reception a proper desk handset with a real call queue and a busy lamp field, running on the same platform and the same numbers. Configured the queue so overflow rings a group in Teams rather than going to voicemail.",
    "Call handling times at reception dropped back to what they had been, and everyone else kept the single-application experience they wanted. The mixed design was not a compromise on the original plan &mdash; it was what the original plan should have been, and it is what we now propose for any office with a genuine reception function.")
FAQS = [
    ("Can we make phone calls in Microsoft Teams?",
     "Yes. Teams becomes a business phone system once calling is added, using the Microsoft 365 licences you already hold. There are three ways to connect it to the public phone network — Direct Routing, Operator Connect and Microsoft Calling Plans. bcom ICT provides Direct Routing through its own cloud PBX platform, which keeps the numbers, the call flow and the rates with us rather than with Microsoft."),
    ("What is Direct Routing and why does it matter?",
     "Direct Routing connects your own carrier to Microsoft Teams instead of buying minutes from Microsoft. It is generally cheaper, far more flexible on call flow and number handling, and it means one provider covers both the phone platform and the support. bcom ICT and Click2Call are the same company, so the Direct Routing behind your Teams calls is ours rather than a third party's."),
    ("Is Teams Phone right for a reception desk?",
     "Usually not on its own, and this is the honest limitation. Teams works well for someone taking their own calls and less well for a person managing a busy queue with constant transfers. The right design for most offices is mixed — a proper handset and a queue for reception, Teams for everyone else. Both run on the same platform and the same numbers."),
    ("Do we need to buy new phone numbers?",
     "No. Local, mobile, 1300 and 1800 numbers all port across. With Direct Routing through our platform, porting and call flow are handled in one place rather than split between a carrier and Microsoft."),
    ("Is Teams Phone cheaper than a separate phone system?",
     "It depends on the route. Microsoft Calling Plans are generally the most expensive per user. Direct Routing through a carrier is usually cheaper and more flexible, particularly for a business that already has the Microsoft 365 licences. The saving is real but it is not the main argument — the main argument is staff using one application instead of two."),
    ("What if the internet drops?",
     "Teams calls stop, in the same way any cloud phone system does. That is the honest trade. A business that cannot afford to lose its phones needs a second connection path with automatic failover, and we would rather set that up at the start than explain it afterwards."),
]

PAGE = {
    "path": "/microsoft-teams-phone-gold-coast",
    "priority": "0.8",
    "service": "Microsoft Teams Phone Gold Coast",
    "title": "Microsoft Teams Phone & Direct Routing | bcom ICT Gold Coast",
    "description": "Make and take business calls inside Microsoft Teams. bcom ICT provides Direct Routing through its own cloud PBX. Call 07 3041 8993.",
    "hero_img": "teams-phone-hero.webp",
    "hero_alt": "A Gold Coast business team taking phone calls inside Microsoft Teams",
    "eyebrow": "Microsoft",
    "h1": "Real phone calls, inside the app your staff already use",
    "lede": "Teams calling on Direct Routing through our own platform — so the numbers, the call flow and the person who answers when it breaks are all in one place.",
    "actions": [("Talk it through", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Direct Routing", "Our own platform", "Numbers ported", "Handsets where they suit"],
    "crumbs": [("Services", "/services"), ("Microsoft Teams Phone", "/microsoft-teams-phone-gold-coast")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">Microsoft Teams becomes a business phone system once calling is connected to it, using
    the Microsoft 365 licences you already hold. bcom ICT provides that through Direct Routing on its own cloud
    PBX platform, so the numbers, the call flow, the rates and the support all sit with one company. Local,
    mobile, 1300 and 1800 numbers port across. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">Three ways to connect it, and they are not equal</h2>
    <p style="margin-top:16px">Turning Teams into a phone system is straightforward. Choosing how it reaches
    the public phone network is the decision that determines what it costs and what it can do.</p>
    <div class="grid grid--3" style="margin-top:28px">{cards(ROUTES, icon=True)}</div>
    <p style="margin-top:28px;max-width:68ch">We provide Direct Routing because it is the route that keeps
    control of the numbering, the call flow and the rates &mdash; and because
    <a href="/cloud-pbx-gold-coast">the platform behind it is ours</a>. Click2Call is a trading name of Bcom
    Services Pty Ltd, the same ABN as bcom ICT, so there is no third party between you and the people who can
    change something.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>Where Teams calling is genuinely better</h2>
    {ticks([
      "<strong>One application instead of two.</strong> Staff stop switching between a softphone and Teams, which is a smaller benefit on paper and a large one in practice.",
      "<strong>The licences are already paid for.</strong> Microsoft 365 is in the business already; calling is added to it rather than bought alongside it.",
      "<strong>Presence actually means something.</strong> Whether someone is in a meeting is known by the same system routing the call to them.",
      "<strong>It travels.</strong> The extension follows the person to a laptop, a mobile or a home desk without anybody configuring a device.",
    ])}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>And where it is not</h2>
    <p style="margin-top:16px">Reception. A person managing a busy queue, transferring constantly and watching
    who is free is doing a job Teams handles poorly, and no amount of configuration fixes it.</p>
    <p style="margin-top:16px">The right answer for most offices is mixed rather than pure: a proper handset
    and a real queue at reception, Teams for everyone else, both on the same platform and the same numbers.
    That is not a compromise, it is the correct design &mdash; and a provider who tells you Teams replaces a
    reception phone entirely has not sat at one.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The Teams calling faults we are actually called to</h2>
    </div>
    {issues(ISSUES)}

    {trust_note('Before any of this, the connection has to carry voice. Not speed &mdash; consistency. We measure latency variation and packet loss across a working week before recommending a move, because a link that passes every speed test can still be unusable for a call.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a Teams calling rollout looks like when it is right</h2>
      <p>A representative engagement, drawn from real work with client and staff names removed.</p>
    </div>
    {EXAMPLE_1}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Cloud PBX — our own platform", "/cloud-pbx-gold-coast"),
  ("Microsoft 365 Setup & Support", "/microsoft-365-setup-gold-coast"),
  ("Business Phone Systems", "/business-phone-systems-gold-coast"),
  ("VoIP vs on-premises PBX", "/voip-vs-pbx-phone-systems"),
  ("Business NBN & Internet Support", "/nbn-internet-support-gold-coast"),
], heading="Related")}

{cta("Already paying for Microsoft 365?",
     "Then adding calling is a smaller step than you think. We will check the connection first and tell you honestly whether it is ready.")}
''',
}

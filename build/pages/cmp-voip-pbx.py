from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues

CLOUD = [
    "<strong>People work somewhere other than the office.</strong> The extension follows the person to a laptop, a mobile or a home desk. This is the reason most businesses move, and an on-premises system handles it poorly or expensively.",
    "<strong>You have more than one site.</strong> One numbering plan across offices, without a link between buildings to maintain.",
    "<strong>You do not want to own hardware.</strong> No box in a cupboard to fail, no card to source in eight years, no installer to find.",
    "<strong>You want the features without the project.</strong> Call queues, IVR menus, recording, transcription and after-hours routing are configuration rather than capital.",
]

ONPREM = [
    "<strong>Your internet cannot be trusted.</strong> This is the honest one. If the connection drops and there is no failover, a cloud system drops with it. An on-premises PBX on copper keeps working.",
    "<strong>It is paid for and it works.</strong> A functioning system with parts still available owes you nothing. Replacing it because it is old is not a reason.",
    "<strong>Something is wired into it.</strong> Door intercoms, lift phones, paging, alarm diallers and some hospitality integrations sit on the PBX and do not move casually.",
    "<strong>You are mid-lease.</strong> A finance agreement with years to run constrains the options, and there are usually better things to do with the money than break it.",
]

MISTAKES = [
    ("&ldquo;Cloud is just cheaper&rdquo;",
     "a comparison of a monthly fee against a system that was paid for years ago. Against a written-down PBX, cloud often costs more per month and still wins on capability — but it should win on the right grounds.",
     "Compare against what the next five years actually look like, including the maintenance, the parts risk and the day nobody will touch it. Not against a sunk cost."),
    ("&ldquo;On-premises is obsolete&rdquo;",
     "a sales position more than a technical one. Plenty of PBX systems are doing exactly what their business needs and will keep doing it for years.",
     "Judge it on whether it does what you need, whether parts are obtainable and whether anyone will support it. We still program Panasonic, NEC, LG Ericsson and Alcatel-Lucent systems."),
    ("&ldquo;We will move everything at once&rdquo;",
     "an all-or-nothing framing that is rarely necessary. A hybrid — the existing system for the office, cloud extensions for people outside it, joined on one published number — is frequently a fraction of the cost.",
     "Consider the middle path before the full replacement. It is often the right answer for two years, and it makes the eventual move smaller."),
    ("&ldquo;Our internet is fine, we did a speed test&rdquo;",
     "the most expensive assumption in this decision. Voice needs consistency, not speed, and a connection can pass every speed test and still be unusable for a call.",
     "Measure latency variation and packet loss across a working week before committing. This is the one check that decides whether a cloud move succeeds."),
    ("&ldquo;We will keep the handsets&rdquo;",
     "sometimes possible and often not. Whether existing desk phones carry across depends on the specific models and how they are locked.",
     "Establish it for your exact handsets before planning around it. It changes the shape of the project and it is a ten-minute check."),
]

FAQS = [
    ("Should we move from a PBX to a cloud phone system?",
     "It depends on two things: whether people need to work away from the office, and whether your internet connection is genuinely stable enough to carry voice. If staff are remote or across sites, cloud is usually the right move. If your existing system works, is paid for, and everyone sits in one building on an unreliable connection, staying put is a defensible decision. bcom ICT supplies cloud and still programs legacy PBX systems, so we have no stake in the answer."),
    ("What happens to a cloud phone system if the internet drops?",
     "Calls stop, unless there is a second path. That is the honest limitation. It is why we add mobile failover on a site that depends on its phones, and why we measure the connection before recommending a move rather than after. An on-premises system on copper does not have this exposure, and that genuinely counts in its favour."),
    ("Is cloud cheaper than an on-premises PBX?",
     "Against a new PBX, usually yes — there is no hardware, no installer and no maintenance contract. Against a system you already own and have written down, often no on a monthly basis. The case for moving is usually capability and flexibility rather than price, and anyone telling you it is purely a saving has not compared it properly."),
    ("Can we keep our existing phone numbers?",
     "Yes. Local, mobile, 1300 and 1800 numbers are all portable. Most porting delays are administrative — account details not matching the losing provider's records — which is why we reconcile those before submitting rather than after a rejection."),
    ("Can we run both at once?",
     "Yes, and it is frequently the sensible answer. The existing system covers the office while cloud extensions cover people working elsewhere, joined so one published number reaches whoever is free. It costs a fraction of a full replacement and it makes the eventual move smaller."),
    ("What about our lift phone and alarm dialler?",
     "They stay where they are. Lift emergency phones, monitored alarm diallers and fire panels sit on their own services and are the most commonly forgotten casualty of a phone changeover. We identify every service in the building and what depends on it before anything is switched."),
]

PAGE = {
    "path": "/voip-vs-pbx-phone-systems",
    "priority": "0.8",
    "title": "Cloud VoIP vs On-Premises PBX | bcom ICT",
    "description": "Cloud VoIP or keep the PBX? An honest comparison from a provider that sells both — where each genuinely wins, and why a hybrid is often the right answer.",
    "hero_img": "compare-voip-pbx-hero.webp",
    "hero_alt": "A bcom ICT technician working on a business phone system cabinet on the Gold Coast",
    "eyebrow": "Comparison",
    "h1": "Cloud phone system, or keep the PBX?",
    "lede": "We sell cloud and we still program thirty-year-old PBX systems other providers will not touch. So here is the version where we have nothing riding on the answer.",
    "crumbs": [("Services", "/services"), ("VoIP vs PBX", "/voip-vs-pbx-phone-systems")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">Cloud VoIP suits businesses with staff working away from the office or across multiple
    sites, and removes the hardware entirely. An on-premises PBX still wins where the internet connection is
    unreliable, where the existing system is paid for and working, or where door intercoms, lift phones or
    alarm diallers are wired into it. A hybrid — the PBX for the office and cloud extensions for everyone else
    — is often the right answer for both. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">The decision is not really about phones</h2>
    <p style="margin-top:16px">Almost every comparison of these two is written by somebody selling one of them,
    which is why they all reach the same conclusion. The honest position is that this decision turns on two
    questions that have nothing to do with phone features.</p>
    <p style="margin-top:16px"><strong>Where do your people work?</strong> If everyone is in one building,
    an on-premises system does that job perfectly well and has for decades. The moment staff are at home, in
    vehicles or across two sites, an on-premises system starts costing money and effort to do something cloud
    does by default.</p>
    <p style="margin-top:16px"><strong>Can your connection carry voice?</strong> Not whether it is fast &mdash;
    whether it is consistent. A cloud phone system is only as good as the link underneath it, and a business
    that moves onto one across a connection with afternoon packet loss has bought a worse phone system than the
    one it replaced.</p>

    {trust_note('bcom ICT runs its own <a href="/cloud-pbx-gold-coast">cloud PBX platform</a> and also maintains legacy Panasonic, NEC, LG Ericsson and Alcatel-Lucent systems. We have advised clients to keep a PBX we could have replaced, because the alternative would have been worse for them.')}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Move to cloud when</span>
      <h2>Cloud is the right answer here</h2>
    </div>
    {ticks(CLOUD)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Stay on premises when</span>
      <h2>And keeping the PBX is the right answer here</h2>
    </div>
    {ticks(ONPREM)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>The answer is frequently both</h2>
    <p style="margin-top:16px">The framing of this decision as a replacement is usually wrong. A business with
    sixteen people in an office and six working elsewhere does not need to discard a working system to solve a
    problem affecting six people.</p>
    <p style="margin-top:16px">Keep the PBX for the building. Add cloud extensions for the people who are not
    in it. Join the two so one published number rings whoever is available, wherever they are. It costs a
    fraction of a full replacement, it removes the pressure to decide, and when the PBX genuinely reaches its
    end the move is already half done.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common mistakes</span>
      <h2>What people get wrong deciding this</h2>
    </div>
    {issues(MISTAKES)}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Cloud PBX — our own platform", "/cloud-pbx-gold-coast"),
  ("VoIP Phone Systems", "/voip-phone-system-installation-and-support-gold-coast"),
  ("PBX Systems & Legacy Support", "/pabx-phone-systems-gold-coast"),
  ("Business Phone Systems", "/business-phone-systems-gold-coast"),
  ("Business NBN & Internet", "/nbn-internet-support-gold-coast"),
], heading="Related")}

{cta("Want the honest answer for your business?",
     "Tell us where your people work and we will measure whether your connection can carry it. Those two answers decide this, and we will tell you if the answer is to stay put.")}
''',
}

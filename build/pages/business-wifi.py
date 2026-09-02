from layout import MARK, cta, faq_block, cards, ticks, steps, related, photo, trust_note, issues, example, price_table

PROBLEMS = [
    ("Dead spots", None,
     "Consumer routers were built for a house. Offices have plasterboard, steel studs, concrete, glass partitions and a comms room in the worst possible corner. Coverage needs designing, not guessing."),
    ("It slows down when everyone's in", None,
     "One access point handling forty devices behaves very differently to one handling five. Most 'slow internet' complaints in offices are actually saturated WiFi, not the NBN service."),
    ("Guests on your business network", None,
     "Customers, contractors and visitors sharing the same network as your accounts system is a genuine risk — and if you take card payments, it's also a compliance problem."),
    ("Nobody knows what's connected", None,
     "Old staff devices, a smart TV somebody plugged in, the security camera installer's tablet. Without visibility you can't secure or troubleshoot any of it."),
]

INSTALL = [
    ("We survey the site", "We walk the building, measure signal, note the construction, and find where the interference is actually coming from. Guessing at access point placement is how you end up with dead spots after paying for a new system."),
    ("We design the coverage", "Access point positions, cabling runs, switch capacity and the network segments — guest, staff, payments, devices — planned before anything is bought."),
    ("We install and cable it", "Cat6 or Cat6A run properly, terminated neatly, tested and certified. Cabling is a licensed trade in Australia, so that part is done by ACMA registered cabling contractors we engage — you still deal only with us."),
    ("We hand it over documented", "Passwords, network layout, device inventory and warranty details written down and given to you. It's your network — you should have the keys to it."),
]

PRICING = [
    ("Simple professional setup", "$1,500", "+ GST, fixed price",
     ["Hardware included", "Straightforward single-office coverage",
      "Surveyed, installed and configured", "Guest network separated from business systems",
      "Documented and handed over"]),
]

COMMON_ISSUES = [
    ("“It drops out in the back office”",
     "one access point trying to cover a whole floor. Signal falls off far faster through plasterboard, steel studs and glass partitions than people expect.",
     "Measure the actual coverage rather than guessing, then position a second access point where it can be cabled. Turning the existing one up does not extend range — it just makes the overlap worse."),
    ("“It’s fine in the morning and slow by 11am”",
     "device density rather than coverage. One access point handling forty clients behaves nothing like one handling five, and everyone arrives at once.",
     "Count what is actually connecting, including phones and devices nobody thinks about. Then add capacity where the people are, rather than upgrading the internet plan that was never the bottleneck."),
    ("“My laptop stays connected to the far access point”",
     "transmit power set too high, so a device clings to a distant access point instead of switching to the near one. Extremely common in DIY installs.",
     "Tune the power levels down so the handover happens where it should. Counter-intuitive, and it fixes roaming complaints without any new hardware."),
    ("“Guests can see our server”",
     "guest WiFi on the same network as everything else — the access point has a guest network feature that was never actually configured.",
     "Put guests on their own VLAN with internet access and no route to anything internal. If you take card payments, put terminals on a third segment too."),
    ("“EFTPOS drops out when we’re busy”",
     "the payment terminal competing with staff phones, ordering tablets and guest devices on a saturated wireless network.",
     "Segment payments onto their own network, and size the wireless for the busy period rather than the quiet one. This is a design problem, not a terminal fault."),
    ("“We added cameras and the WiFi got worse”",
     "PoE budget. Cameras draw power from the same switch as the access points, and exceeding the budget causes intermittent faults across everything.",
     "Check the switch budget against actual draw, then either redistribute across ports or fit a switch with adequate capacity. Very often misdiagnosed as failing access points."),
]

EXAMPLE_1 = example(
    "A venue that had bought three range extenders",
    "A Gold Coast hospitality business with WiFi that worked at the bar and nowhere else. Over two years they had bought three consumer range extenders, each of which helped briefly and then made roaming worse.",
    "The extenders were all placed at the dead spots rather than partway to them, so each was relaying a signal it could barely hear — and each created a second network name that devices clung to. The original router was also handling the EFTPOS terminal on the same flat network.",
    "Removed the extenders. Surveyed the venue, ran cable to two positions, fitted two properly placed access points under one network name, and separated staff, guest and payment traffic onto three segments.",
    "Coverage across the whole venue including the terrace, devices roaming properly, and the EFTPOS drop-outs stopped — which turned out to be the thing that had actually been costing them money.")

EXAMPLE_2 = example(
    "An office that assumed it needed a faster internet plan",
    "A professional firm of about thirty staff on the Gold Coast, convinced their internet was too slow and about to upgrade to a substantially more expensive business plan.",
    "The connection was barely being used. The bottleneck was a single consumer access point serving the whole floor, plus a backup job running at 10am rather than overnight. Speed tests from a desk near the access point looked fine, which is why nobody had suspected the wireless.",
    "Measured throughput at the desk and at the access point to demonstrate the difference, added two cabled access points sized for the headcount, and rescheduled the backup outside business hours.",
    "The plan upgrade was cancelled. The fix cost a fraction of what the extra bandwidth would have, and would not have helped at all.")


FAQS = [
    ("Who installs business WiFi on the Gold Coast?",
     "bcom ICT designs and installs business WiFi across the Gold Coast using Ubiquiti UniFi and Aruba Instant On systems. Installations include a full-coverage site survey, VLAN and guest-network separation, and structured cabling carried out by ACMA registered cabling contractors. Call 07 3041 8993."),
    ("Why not just use a better consumer router?",
     "Because the problem usually isn't the router — it's that one device is trying to cover a whole building. Business systems use several access points working together with a single network name, so devices hand over cleanly as people move around. They also let us separate guests from your business systems, which a consumer router can't do properly."),
    ("How much does business WiFi cost on the Gold Coast?",
     "A simple professional setup starts at around $1,500 + GST, fixed price, with hardware included — surveyed, installed, configured and documented, with the guest network separated from your business systems. Larger or more complex sites are quoted after a survey. What moves the number is building size and construction, how many access points the coverage genuinely needs, how much cabling has to be run, and whether payment terminals need segmenting."),
    ("Which brands do you install?",
     "Primarily Ubiquiti UniFi and Aruba Instant On for business installations — both give central management, proper network segmentation and sensible ongoing costs. For home offices and small premises we also install Eero, Google Nest and Ubiquiti mesh systems."),
    ("We take card payments. Does that change anything?",
     "Yes. Payment devices should sit on their own isolated network segment, separate from staff and guest traffic. We build that separation in as standard on business installs — it's PCI-DSS-aligned practice and it's much cheaper to do at installation than to retrofit."),
    ("Do you do the cabling too, or do we need an electrician?",
     "We handle it as part of the job, so you have one point of contact rather than three. Fixed cabling connected to the telecommunications network legally requires a registered cabler in Australia — bcom ICT engages and manages ACMA registered cabling contractors for that portion rather than doing it with internal staff. You get testing and certification documentation on completion."),
    ("Can you fix the WiFi we already have?",
     "Often, yes. Sometimes it's a placement or channel problem we can resolve in a visit without replacing anything. We'll tell you when that's the case rather than selling you a new system you don't need."),
]

PAGE = {
    "path": "/business-wifi-gold-coast",
    "priority": "0.85",
    "service": "Business WiFi Installation Gold Coast",
    "title": "Business WiFi Installation Gold Coast — UniFi & Aruba | bcom ICT",
    "description": "Business WiFi design and installation across the Gold Coast using Ubiquiti UniFi and Aruba Instant On. Coverage surveys, guest network separation and certified structured cabling. Call 07 3041 8993.",
    "hero_img": "business-wifi-gold-coast-hero.webp",
    "hero_alt": "A Ubiquiti UniFi access point installed in the ceiling of a Gold Coast business office by bcom ICT",
    "h1": "Business WiFi that works everywhere in your building",
    "lede": "Designed, cabled and installed across the Gold Coast using Ubiquiti UniFi and Aruba Instant On — with your guests kept well away from your business systems.",
    "actions": [("Book a site survey", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["UniFi & Aruba", "Coverage surveyed first", "Guest network separated", "Certified cabling"],
    "crumbs": [("Services", "/services"), ("Business WiFi", "/business-wifi-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT designs and installs business WiFi across the Gold Coast using Ubiquiti UniFi
    and Aruba Instant On. Every installation starts with a full coverage survey and includes VLAN and
    guest-network separation, with PCI-DSS-aligned segmentation for venues taking card payments. Cabling is
    carried out by ACMA registered cabling contractors. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Why office WiFi fails</span>
      <h2>Four reasons it isn't working</h2>
      <p>Almost every WiFi complaint we're called to comes down to one of these, and none of them are fixed by buying a more expensive router.</p>
    </div>
    <div class="grid grid--2">{cards(PROBLEMS, icon=False)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How we install</span>
      <h2>Surveyed first, then designed, then installed</h2>
      <p>The order matters. Buying hardware before you know the building is how businesses end up paying twice.</p>
    </div>
    <div class="grid grid--4">{steps(INSTALL)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>Keeping guests off your business network</h2>
        <p style="margin-top:16px">This is the part most offices get wrong, and it's the part that matters most. If a customer, contractor or visitor connects to the same network as your accounts system and your file server, then anything on their laptop is now sitting inside your business.</p>
        <p style="margin-top:16px">On a business install we separate the network into segments that can't reach each other:</p>
        {ticks([
          "Staff devices and business systems",
          "Guest and customer WiFi — internet only, nothing internal",
          "Payment terminals, isolated on their own segment",
          "Cameras, door access, printers and other devices kept apart from everything",
        ])}
        <p style="margin-top:24px">It costs almost nothing to build in at installation and it's genuinely awkward to retrofit later. If you take card payments it's also expected practice under PCI-DSS.</p>
      </div>
      {photo("unifi-installation-gold-coast.webp", "bcom ICT installing Ubiquiti UniFi networking equipment in a Gold Coast commercial premises", "UniFi and Aruba Instant On both give central management and proper network segmentation.")}
    </div>

    <div class="rule">{MARK}</div>

    <h2>Home offices and small premises</h2>
    <p style="margin-top:16px">We still install mesh WiFi for home offices and small sites — Eero, Google Nest and Ubiquiti systems supplied and configured to remove dead zones and give someone working from home a connection they can actually rely on. See <a href="/mesh-network-setup-gold-coast">mesh WiFi setup</a>. General home computer support isn't something we take on.</p>

    {trust_note('Cabling connected to the telecommunications network legally requires a registered cabler in Australia. bcom ICT engages ACMA registered cabling contractors for that work and provides testing and certification documentation on completion — worth asking any installer to show you before they start.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What it costs</span>
      <h2>How much does business WiFi cost on the Gold Coast?</h2>
      <p>Most providers will not put a number on this. Here is our starting point, and what actually moves it.</p>
    </div>
    {price_table(PRICING, note="Larger or more complex sites are quoted after a survey. What moves the number: the size and construction of the building, how many access points the coverage genuinely needs, how much cabling has to be run, whether payment terminals need segmenting, and whether switching has the PoE capacity for what is being added. We survey first and quote on the actual building, so the figure does not move once an installer is on site.")}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The WiFi faults we are actually called to</h2>
      <p>Almost every wireless complaint on the Gold Coast is one of these six, and most are fixable without new hardware.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What fixing it actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ('UniFi vs Aruba Instant On', '/unifi-vs-aruba-instant-on'),
  ("Office Network Cabling", "/network-cabling-for-offices-gold-coast"),
  ("Network Security & Firewall", "/network-security-and-firewall-configuration-gold-coast"),
  ("Network Troubleshooting", "/network-troubleshooting-diagnostics-gold-coast"),
  ("Ubiquiti UniFi WiFi", "/ubiquiti-unifi-wifi-gold-coast"),
  ("Aruba Instant On WiFi", "/aruba-instant-on-wifi-gold-coast"),
  ("Business NBN & Internet Support", "/nbn-internet-support-gold-coast"),
])}

{cta("Book a coverage survey",
     "We walk the building, measure what's actually happening, and quote on the real thing — not on a floor plan and an assumption.")}
''',
}

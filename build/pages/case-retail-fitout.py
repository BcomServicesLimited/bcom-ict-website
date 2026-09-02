from layout import MARK, cta, faq_block, cards, ticks, steps, related, trust_note

# Client is never named — Royce's instruction. The two centres are named with his
# explicit permission. Project costs stay out: client commercial information.

DELIVERED = [
    ("Network and WiFi", None,
     "A full <a href=\"/ubiquiti-unifi-wifi-gold-coast\">Ubiquiti UniFi</a> network — access points positioned for real coverage across the trading floor, back of house and change rooms, with switching sized for everything the store would ever plug in."),
    ("CCTV", None,
     "UniFi Protect cameras throughout, on the same controller as the network. One system, one login, footage the store manager can actually reach."),
    ("Internet, with a backup", None,
     "Primary and backup services coordinated directly with the telco, on a DrayTek VDSL gateway. A store that cannot take payment is a store that is shut, so the second path was in from day one."),
    ("In-store audio", None,
     "A Yamaha four-zone streaming amplifier and Monitor Audio in-ceiling speakers, with a tablet so staff set the mood themselves without calling anyone."),
    ("Stock scanning", None,
     "RFID scanners and ticket printers configured, tested and working against the client's platform."),
    ("Point of sale", None,
     "Shopify POS collected, installed, configured and tested, ready to trade."),
    ("Customer analytics", None,
     "Traffic counting configured and commissioned, so the store had its numbers from the first day of trading."),
    ("The cabinet", None,
     "A wall-mounted data cabinet delivered fully assembled, every device patched from panel to switch, labelled and documented."),
]

RUN = [
    ("We scope it properly",
     "Every item named up front — what it is, who supplies it, who installs it, who configures it. Circulated to the builder, the electrician and every vendor before anything is ordered."),
    ("We order against the build",
     "Hardware procurement runs three to four weeks, so it is placed against the construction programme rather than the install date. Nothing waits on a box."),
    ("We confirm the site is ready",
     "A short checklist agreed with the builder — cabling in, cabinet mounted, power tested, internet live. Confirmed before anyone travels."),
    ("We install and commission",
     "Configured, tested and signed off as a working environment rather than a delivered pile of equipment."),
    ("We are there on opening day",
     "On-site technical support booked for the first trading day, plus a contingency allowance held for the install itself."),
]

FAQS = [
    ("Can bcom ICT deliver a complete retail store fit-out?",
     "Yes. For these two stores bcom ICT supplied and delivered the entire technology environment — a Ubiquiti UniFi network and WiFi, UniFi Protect CCTV, a wall-mounted data cabinet, primary and backup internet with telco liaison, in-store audio, RFID stock scanning, Shopify point of sale and traffic analytics — configured, commissioned and supported through opening day. One supplier, one point of accountability, across two states."),
    ("What hardware did you use in the stores?",
     "The network, WiFi and CCTV were all Ubiquiti UniFi, including UniFi Protect for the cameras, managed from a single controller. The internet gateway was a DrayTek VDSL router running a primary and a backup service. In-store audio used a Yamaha four-zone streaming amplifier with Monitor Audio in-ceiling speakers, controlled from a tablet. Point of sale was Shopify. Both stores took the same hardware and the same configuration."),
    ("Can you work alongside our builder, shopfitter and other vendors?",
     "It is most of what makes a fit-out succeed. On these stores bcom ICT worked alongside the builder, the electrician and three separate technology vendors. We set out the scope for every party before work started and coordinated the sequence, so each trade arrived to find what it needed already in place."),
    ("Can you roll the same build out across multiple stores?",
     "Yes, and it is what these two stores were built to prove. Both took identical hardware and configuration, so the second store was a repeat of a known build rather than a fresh design. Standard hardware, one controller and a scope document reissued per site is what makes a multi-site rollout predictable in both cost and timeline."),
    ("Do you provide support on opening day?",
     "Yes. On-site technical support was booked in advance for the first trading day as a defined block of hours, with a separate contingency allowance for the installation. Opening day is when a fault costs the most, and it is worth having someone in the building rather than reachable by phone."),
    ("Do you handle the internet connection and the telco?",
     "Yes. bcom ICT coordinated the ISP deployment for both a primary and a backup service at each store and dealt with the telecommunications provider directly, so the client did not have to project-manage a carrier alongside a fit-out."),
    ("Do you work outside the Gold Coast?",
     "Yes. These stores were at Pacific Fair on the Gold Coast and Chermside in Brisbane, delivered to the same standard with different builders and different trades in each state. Remote and managed support extends Australia-wide."),
]

PAGE = {
    "path": "/retail-store-technology-fitout-case-study",
    "priority": "0.8",
    "title": "Retail Store Technology Fit-Out — Case Study | bcom ICT",
    "description": "bcom ICT delivered the complete technology fit-out for two new retail stores at Pacific Fair and Chermside.",
    "hero_kind": "doc",
    "eyebrow": "Case study",
    "h1": "Two new stores, two states, trading from day one",
    "lede": "A retail customer opening at Pacific Fair and Chermside. bcom ICT delivered the entire technology environment for both — network, WiFi, CCTV, audio, connectivity, stock scanning and point of sale — and stood in the store on opening day.",
    "crumbs": [("Case studies", "/case-studies"), ("Retail fit-out", "/retail-store-technology-fitout-case-study")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT delivered the complete technology fit-out for two new retail stores, at Pacific
    Fair on the Gold Coast and Chermside in Brisbane — a Ubiquiti UniFi network, business WiFi, UniFi Protect
    CCTV, a wall-mounted data cabinet, primary and backup internet with telco liaison, in-store audio, RFID
    stock scanning, Shopify point of sale and traffic analytics. Both stores took identical hardware and
    configuration, and both opened on schedule. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">Everything a new store needs, from one supplier</h2>
    <p style="margin-top:16px">A retail fit-out has a date on it that does not move. The lease starts, the
    signage goes up, the staff are rostered and the doors open — and on that morning every system in the
    building has to work at once, in front of customers, operated by people who were hired to sell clothes
    rather than to run a network.</p>
    <p style="margin-top:16px">bcom ICT took the whole technology environment for both stores. Not a slice of
    it alongside three other suppliers, but the network the store runs on, the cameras that watch it, the
    connection that carries its payments, the music playing in it, the scanners that track its stock and the
    tills that take the money.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Delivered</span>
      <h2>What went into each store</h2>
      <p>Supplied, installed, configured, tested and commissioned by bcom ICT.</p>
    </div>
    <div class="grid grid--2">{cards(DELIVERED, icon=True)}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>One stack, deliberately</h2>
    <p style="margin-top:16px">Network, WiFi and CCTV were all
    <a href="/ubiquiti-unifi-wifi-gold-coast">Ubiquiti UniFi</a>, managed from a single controller rather than
    three separate systems with three separate logins. On a store that matters more than it does in an office:
    the people who work there are retail staff, and the person who needs to check a camera at nine on a
    Saturday should be able to do it without learning a second platform.</p>
    <p style="margin-top:16px">It also made the second store straightforward. One vendor, one controller and
    one configuration meant Chermside was a repeat of a known build rather than a fresh design &mdash; and a
    fault at either site looks the same to whoever picks it up.</p>
    <p style="margin-top:16px">The gateway is the deliberate exception. A DrayTek VDSL router handles the
    primary and backup services because the connection type at the site called for it. We specify what the
    building needs rather than what keeps a brochure tidy.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How we run it</span>
      <h2>Why both stores opened on time</h2>
      <p>Each store had six parties working in one tenancy &mdash; bcom ICT, the builder, the electrician and three technology vendors. Keeping that on schedule is a discipline, and it is the part clients are really buying.</p>
    </div>
    <div class="grid grid--3">{cards([(t, None, d) for t, d in RUN])}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>The client gave us more of the project</h2>
    <p style="margin-top:16px">RFID configuration, Shopify point of sale and the traffic analytics system all
    began the project with their own vendors. Partway through the build the client asked bcom ICT to take them
    on &mdash; configuring and testing the RFID scanners and ticket printers, collecting and setting up the
    Shopify equipment, and commissioning the traffic counting system &mdash; alongside additional hardware
    including a change-room speaker, the internet gateway, a printer and the audio control tablet.</p>
    <p style="margin-top:16px">Each addition was quoted and agreed in writing before the work started, so a
    growing project stayed a predictable one. It is the most useful thing in this write-up: partway through a
    build with a fixed opening date, the client chose to consolidate more of it with us rather than less.</p>

    <div class="rule">{MARK}</div>

    <h2>Opening day</h2>
    <p style="margin-top:16px">We booked on-site technical support for the first trading day of each store, as
    a defined block of hours rather than a promise that someone would answer the phone. A store's opening is
    the day a fault costs the most and the day nobody has time to describe one to a support queue, so we were
    in the building.</p>

    {trust_note('Want the reference rather than the write-up? We will put you in touch with a client directly &mdash; see <a href="/case-studies">case studies</a>.')}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>Built to be repeated</h2>
    <p style="margin-top:16px">Two stores, two states, different builders and different trades in each, and the
    same result both times. That is the whole point of the exercise: standard hardware, a standard
    configuration, a scope reissued per site and a readiness checklist the next builder will already
    recognise.</p>
    <p style="margin-top:16px">A rollout is not a bigger fit-out. It is the same fit-out done repeatedly
    without the design being reopened each time, and these two stores are the proof that the model travels.</p>
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Ubiquiti UniFi WiFi & Protect", "/ubiquiti-unifi-wifi-gold-coast"),
  ("IT Support for Retail", "/it-support-retail-gold-coast"),
  ("Business WiFi Installation", "/business-wifi-gold-coast"),
  ("Office Network Cabling", "/network-cabling-for-offices-gold-coast"),
  ("Network Security & Firewalls", "/network-security-and-firewall-configuration-gold-coast"),
  ("Case studies", "/case-studies"),
], heading="Related")}

{cta("Opening a store, or a few?",
     "Bring us in while the drawings are still being marked up. We will scope the technology against the construction programme so the doors open on a store that already works.")}
''',
}

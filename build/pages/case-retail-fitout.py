from layout import MARK, cta, faq_block, cards, ticks, steps, related, trust_note

# Client is never named — Royce's instruction. The two centres are named with his
# explicit permission. Project cost is deliberately excluded: it is the client's
# commercial information and we have no permission to publish it.

OURS = [
    "Supplied the whole network and CCTV stack as <a href=\"/ubiquiti-unifi-wifi-gold-coast\">Ubiquiti UniFi</a> &mdash; access points, switching and UniFi Protect cameras on one controller &mdash; plus the wall-mounted data cabinet, delivered fully assembled",
    "Set the positions for every access point and camera, so coverage was designed rather than discovered",
    "Installed and configured everything inside the cabinet, and patched every device from panel to switch",
    "Configured the network, the WiFi and UniFi Protect, then tested and commissioned all of it",
    "Coordinated the ISP for both a primary and a backup internet service, and dealt with the telco directly",
    "Supplied and configured the DrayTek VDSL router as the gateway",
    "Rack-mounted the Yamaha four-zone streaming amplifier and connected the Monitor Audio in-ceiling speakers",
    "Configured a tablet so staff could control audio zones without needing us",
]

NOT_OURS = [
    "<strong>Cabling.</strong> Every data, CCTV, RFID and audio run was installed, terminated and labelled by the electrician, back to a patch panel they supplied.",
    "<strong>Mounting and power.</strong> Access points, cameras, RFID hardware, speakers, the cabinet itself, ceiling cut-outs and electrical compliance — the builder's, not ours.",
    "<strong>Audio design.</strong> We supplied and installed the hardware and verified it powered on. Tuning, voicing and how the room actually sounds were never ours to promise.",
    "<strong>The RFID system.</strong> Supplied by the client's own vendor. We installed the hardware and gave it a network. The vendor kept sign-off.",
    "<strong>Point of sale.</strong> Shopify, run by the client and their vendors.",
    "<strong>Traffic analytics.</strong> The vendor's system, on the vendor's terms.",
]

READY = [
    ("Cabling complete", "Every run installed, terminated, labelled and tested to the patch panel."),
    ("Mounting points ready", "Access points, cameras and RFID hardware — positions accessible and prepared."),
    ("Cabinet in position", "Mounted, secured, patch panel fitted."),
    ("Power tested", "At the cabinet and at every device location."),
    ("Internet live", "Service active and handed off to the patch panel, terminated and labelled."),
]

FAQS = [
    ("Who does the cabling on a retail store fit-out?",
     "On this project the electrician did, and that is the usual arrangement. bcom ICT supplied the network, CCTV and audio hardware and did the configuration and commissioning; the electrician installed, terminated, labelled and tested every cable run and mounted the devices. Fixed cabling connected to the telecommunications network is licensed work in Australia, and bcom ICT engages ACMA registered cabling contractors where it falls to us rather than a builder's trades."),
    ("What does an IT fit-out for a new retail store actually include?",
     "For these two stores: the network and WiFi, CCTV, a wall-mounted data cabinet, a business internet service with a backup connection, in-store audio, and the network side of RFID stock scanning, Shopify point of sale and traffic counting. bcom ICT supplied the hardware, configured and commissioned it, and coordinated the parts other vendors owned so the store opened working."),
    ("Can you work alongside our builder and shopfitter?",
     "Yes, and the coordination is most of the job. Six parties worked in each of these tenancies — bcom ICT, the builder, the electrician, the RFID vendor, the point-of-sale vendor and the analytics vendor. Before anyone started we wrote a scope and responsibility alignment document naming who owned each item, including the things we were explicitly not responsible for. That document, rather than any piece of hardware, is what kept both stores on schedule."),
    ("Who is responsible if the RFID or POS system doesn't work?",
     "Their vendors, and we say so in writing before the project starts. bcom ICT installed the RFID hardware and gave it a working network; configuration, integration and sign-off stayed with the client's RFID vendor. Point of sale and traffic analytics were the same. Taking responsibility for a system we do not control would be a promise we could not keep."),
    ("Do you provide support on opening day?",
     "On these stores, yes — booked in advance as a defined block of on-site time, alongside a separate contingency allowance for the installation itself. A new store opening is the one day where a fault costs the most and nobody has time to explain it, so it is worth having someone there rather than reachable."),
    ("Can you repeat the same build across multiple stores?",
     "That is what the two stores were built to prove. Both sites took the same hardware and the same configuration, so the second was a repeat of a known build rather than a fresh design. That repeatability is what makes a multi-site rollout predictable in cost and timeline."),
    ("What hardware did you use in the stores?",
     "The network, WiFi and CCTV were all Ubiquiti UniFi, including UniFi Protect for the cameras, managed from a single controller. The internet gateway was a DrayTek VDSL router handling a primary and a backup service. In-store audio used a Yamaha four-zone streaming amplifier with Monitor Audio in-ceiling speakers, controlled from a tablet. Point of sale was Shopify, supplied and run by the client. Both stores took the same hardware and the same configuration."),
    ("How long does the hardware take to arrive?",
     "Procurement ran three to four weeks from the point the timeline was confirmed. On a fit-out with a fixed opening date, hardware lead time is one of the few things that cannot be recovered by working harder later, so it is ordered against the construction programme rather than the install date."),
]

PAGE = {
    "path": "/retail-store-technology-fitout-case-study",
    "priority": "0.8",
    "title": "Retail Store Technology Fit-Out — Case Study | bcom ICT",
    "description": "Two new retail stores at Pacific Fair and Chermside, fitted out with network, CCTV, WiFi, audio and connectivity by bcom ICT. Six parties, one scope document, both stores open on schedule.",
    "hero_kind": "doc",
    "eyebrow": "Case study",
    "h1": "Two stores, six parties, one document that kept them on schedule",
    "lede": "A retail customer opening at Pacific Fair and Chermside. The hardware was the straightforward part — the work that mattered was writing down who owned what before anyone picked up a tool.",
    "crumbs": [("Case studies", "/case-studies"), ("Retail fit-out", "/retail-store-technology-fitout-case-study")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT delivered the technology fit-out for two new retail stores, at Pacific Fair on
    the Gold Coast and Chermside in Brisbane — a Ubiquiti UniFi network, business WiFi, UniFi Protect CCTV, a wall-mounted data
    cabinet, primary and backup internet, in-store audio, and the network foundation for RFID stock scanning, Shopify
    point of sale and traffic counting. Both sites took identical hardware and configuration. Call
    07 3041 8993.</p>

    <h2 style="margin-top:56px">Six parties, one tenancy, one opening date</h2>
    <p style="margin-top:16px">A new store fit-out is not a technology project with builders attached. It is a
    construction project with a fixed opening date, and technology is one of six trades competing for the same
    ceiling in the same fortnight. On these stores that meant bcom ICT, the builder, the electrician, the
    client's RFID vendor, their point-of-sale vendor and a traffic analytics vendor — each with their own
    scope, their own schedule and their own idea of what someone else was doing.</p>
    <p style="margin-top:16px">That is where retail fit-outs fail. Not on the hardware, which is ordinary, but
    in the gaps between six parties where a cable nobody ran meets a device nobody mounted, discovered on the
    Thursday before a Saturday opening.</p>

    {trust_note('Before any equipment was ordered we wrote a scope and responsibility alignment document naming every item, who supplied it, who installed it, who configured it and who signed it off. It was circulated to every party and it is the reason both stores opened on schedule.')}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What we owned</span>
      <h2>The parts that were ours</h2>
    </div>
    {ticks(OURS)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What we did not own</span>
      <h2>And the parts that were not</h2>
      <p>Written down at the start, in the same document, with the same weight. A scope that only lists what a supplier will do is half a scope.</p>
    </div>
    {ticks(NOT_OURS)}
    <p style="margin-top:28px;max-width:68ch">Declining responsibility for the audio tuning, the RFID
    integration and the point-of-sale platform was not caution. Each of those sat with a party better placed to
    own it, and a supplier who accepts responsibility for a system they do not control has not reduced the
    client's risk — they have just moved the argument to a worse moment.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>One stack, deliberately</h2>
    <p style="margin-top:16px">Network, WiFi and CCTV were all
    <a href="/ubiquiti-unifi-wifi-gold-coast">Ubiquiti UniFi</a>, managed from a single controller rather than
    three separate systems with three separate logins. On a store that matters more than it does in an office:
    the people who work there are retail staff, not IT staff, and the person who needs to check a camera at
    nine on a Saturday should not have to learn a second platform to do it.</p>
    <p style="margin-top:16px">It also makes the second store cheap. One vendor, one controller and one
    configuration means the Chermside build was a copy of the Pacific Fair build rather than a fresh design
    &mdash; and it means a fault at either site looks the same to whoever picks it up.</p>
    <p style="margin-top:16px">The gateway is the deliberate exception. A DrayTek VDSL router handles the
    primary and backup internet services, because the connection type at the site called for it and matching
    the badge on the box was never the point.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The readiness gate</span>
      <h2>Five things that had to be true before we attended</h2>
      <p>Agreed in advance as a go or no-go. A technician standing in a store waiting for an electrician is a day nobody planned for and somebody pays for.</p>
    </div>
    <div class="grid grid--3">{cards([(t, None, d) for t, d in READY])}</div>
    <p style="margin-top:28px;max-width:68ch">Hardware procurement ran three to four weeks, ordered against the
    construction programme rather than the install date &mdash; on a fit-out with a fixed opening, lead time is
    one of the few things that cannot be recovered later by working harder.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Then the scope grew</h2>
    <p style="margin-top:16px">The original document put RFID configuration, point of sale and traffic
    analytics outside our scope, with their vendors. During the build the client asked us to take on the
    configuration and testing of the RFID scanners and ticket printers, collection, setup and testing of the Shopify point-of-sale equipment, and
    the commissioning of the traffic counting system &mdash; each quoted and approved as a variation before any
    work started, alongside additional hardware including a change-room speaker, a router, a printer and the
    audio control tablet.</p>
    <p style="margin-top:16px">That is worth noticing. The coordination was working well enough that the party
    holding the scope document became the obvious party to hold more of the scope. Every addition was priced
    and agreed in writing first, so a growing project never turned into a disputed invoice.</p>

    <div class="rule">{MARK}</div>

    <h2>Opening day</h2>
    <p style="margin-top:16px">We booked on-site technical support for the opening itself, as a defined block
    of hours rather than an assurance that someone would be reachable, with a separate contingency allowance
    for the installation. A store's first trading day is when a fault costs the most and when nobody has time
    to explain it to a support queue.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>The second store was the point</h2>
    <p style="margin-top:16px">Both sites took the same hardware and the same configuration. The second store
    was not a second design &mdash; it was a repeat of a known build, which is what turns a fit-out from a
    project into a process. Standard hardware, a standard configuration, one scope document that gets reissued
    per site, and a readiness checklist the builder already recognises.</p>
    <p style="margin-top:16px">These two stores were built to prove that model works across states, with
    different builders and different trades, before it is asked to work across many more.</p>

    {trust_note('Interested in the reference rather than the write-up? We will put you in touch with a client directly &mdash; see <a href="/case-studies">case studies</a>.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Ubiquiti UniFi WiFi & Protect", "/ubiquiti-unifi-wifi-gold-coast"),
  ("IT Support for Retail", "/it-support-retail-gold-coast"),
  ("Business WiFi Installation", "/business-wifi-gold-coast"),
  ("Office Network Cabling", "/network-cabling-for-offices-gold-coast"),
  ("Network Security & Firewalls", "/network-security-and-firewall-configuration-gold-coast"),
  ("Office IT Relocation", "/office-it-relocation-gold-coast"),
  ("Case studies", "/case-studies"),
], heading="Related")}

{cta("Opening a store?",
     "Bring us in while the drawings are still being marked up. The cheapest hour on any fit-out is the one spent agreeing who owns what before anyone orders hardware.")}
''',
}

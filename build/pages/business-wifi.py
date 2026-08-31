from layout import MARK, cta, faq_block, cards, ticks, steps, related, photo, trust_note

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

FAQS = [
    ("Who installs business WiFi on the Gold Coast?",
     "bcom ICT designs and installs business WiFi across the Gold Coast using Ubiquiti UniFi and Aruba Instant On systems. Installations include a full-coverage site survey, VLAN and guest-network separation, and structured cabling carried out by ACMA registered cabling contractors. Call 07 3041 8993."),
    ("Why not just use a better consumer router?",
     "Because the problem usually isn't the router — it's that one device is trying to cover a whole building. Business systems use several access points working together with a single network name, so devices hand over cleanly as people move around. They also let us separate guests from your business systems, which a consumer router can't do properly."),
    ("What does a business WiFi installation cost?",
     "It depends on the size of the building, how many access points the coverage needs, and how much cabling has to be run. We survey first and quote on the actual building rather than a guess, so there are no surprises once the installer is on site."),
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

{faq_block(FAQS)}

{related([
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

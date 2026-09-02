from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues, models, example

MODELS = [
    ("The common units", "What most Gold Coast small offices run — NBN, a VPN back to head office, and a mobile backup service for when the street gets dug up.",
     ["Vigor 2765", "Vigor 2766", "Vigor 2865", "Vigor 2927"]),
    ("Bigger sites", "More throughput, more concurrent VPN tunnels, and multi-WAN where two services need to be live rather than one on standby.",
     ["Vigor 2962", "Vigor 3910"]),
    ("The reason they suit Australia", "VDSL and FTTN handled natively, 4G and 5G failover built in, and site-to-site VPN without a subscription attached to it.",
     ["VDSL / FTTN", "Multi-WAN failover", "LTE backup", "IPsec site-to-site"]),
]

ISSUES = [
    ("&ldquo;The provider swapped the modem and everything broke&rdquo;",
     "a replacement unit delivered on factory settings. Every port forward, address reservation and VPN tunnel configured on the old one is gone, and nobody had a copy.",
     "Rebuild it, then export the configuration and keep it. A modem swap is a routine event that costs a business a day every time nobody has the config."),
    ("&ldquo;The failover does not fail over&rdquo;",
     "a backup service that was configured, tested once at install, and never touched again. SIMs expire, plans lapse, and nothing announces it.",
     "Test it by physically disconnecting the primary during a quiet period. A failover nobody has exercised is an assumption, and the day you find out is the worst day to find out."),
    ("&ldquo;The VPN to head office drops every night&rdquo;",
     "a tunnel being torn down by an idle timer, or one end getting a new address when the service reconnects.",
     "Set the timers for how the link is actually used, and use a hostname rather than an address where the service is dynamic. A tunnel that drops at the same time nightly is nearly always a timer."),
    ("&ldquo;We have two routers and half our things do not work&rdquo;",
     "double NAT &mdash; the DrayTek behind the provider's modem, both routing and both translating. Browsing works and anything needing an inbound connection does not.",
     "Put the provider's unit into pass-through and let one device route. Half the strange faults on small business networks come from two devices both believing they are in charge."),
    ("&ldquo;Nobody wants to reboot it to update it&rdquo;",
     "a unit installed years ago and never revisited. Routers are directly exposed to the internet and are a genuine target.",
     "Update it, and check whether the model still receives firmware at all. A router the manufacturer has stopped supporting is a security problem however well it is performing."),
    ("&ldquo;Someone opened a port so they could work from home&rdquo;",
     "a rule opened so someone could work from home, still open years later.",
     "Move it behind the VPN the DrayTek already provides at no extra cost. There is no licence to buy here, which removes the usual excuse."),
]

EXAMPLE_1 = example(
    "The failover that had never actually failed over",
    "A business with a single site and no tolerance for downtime had a DrayTek with 4G backup, installed two years earlier specifically so an internet outage would not stop trading. It had been tested at installation and had never been needed since.",
    "The mobile service behind it had lapsed. The SIM had been on a plan that expired after twelve months, the account had not been renewed, and the router had gone on reporting the interface as configured because from its point of view it was. There was no alert, because nothing had failed &mdash; the backup path simply would not have carried a single call had the primary dropped.",
    "Restored the mobile service, then tested the failover properly by physically disconnecting the primary connection during a quiet period and confirming that calls, card payments and the practice software all continued. Set a calendar reminder for the SIM plan and added the failover test to the same schedule.",
    "The business has a second path that has now been proven rather than assumed. A failover nobody has exercised is not redundancy, it is a belief &mdash; and the day you discover which one you had is always the worst possible day.")
FAQS = [
    ("Does bcom ICT support DrayTek routers?",
     "Yes, and we deploy them regularly. DrayTek Vigor units handle Australian NBN and FTTN natively, include site-to-site and remote access VPN with no subscription, and support 4G or 5G failover — which is why they end up in a lot of Gold Coast small offices. We configure, support and take over existing units."),
    ("Is a DrayTek a real firewall?",
     "It is a router with firewall capability rather than a full inspection appliance. For a straightforward office it is genuinely enough — segmentation, VPN, sensible inbound control. If you need intrusion prevention, deep logging or evidence for an insurer, that is where a FortiGate or Sophos earns the extra cost, and we will say so."),
    ("Can a DrayTek do 4G or 5G failover?",
     "Yes, and it is one of the main reasons to choose one. A second path that takes over automatically turns a street-works outage from a lost day into a slower afternoon. It needs testing after install and periodically afterwards, because an untested failover is just an assumption."),
    ("Which DrayTek model should we use?",
     "It depends on the connection type, how many VPN tunnels you need concurrently and whether you want true multi-WAN rather than failover. For most single-office businesses on NBN the 2765 through 2927 band covers it. We will size it on the actual service rather than the headline figure."),
    ("Our provider gave us a modem — do we need a DrayTek as well?",
     "Not always, and if the supplied unit is doing the job we will tell you to keep it. Where it matters: failover, site-to-site VPN, proper VLAN separation and holding a configuration you own rather than one that resets when the provider swaps the hardware. If none of those apply, save the money."),
    ("Can you recover a DrayTek nobody has the password for?",
     "Usually. Where the credentials are genuinely lost the unit can be reset and rebuilt, which is a good argument for keeping an exported configuration somewhere the business controls."),
]

PAGE = {
    "path": "/draytek-router-gold-coast",
    "priority": "0.8",
    "service": "DrayTek Router Support Gold Coast",
    "title": "DrayTek Router Setup & Support Gold Coast — Vigor | bcom ICT",
    "description": "DrayTek Vigor configuration and support for Gold Coast businesses — NBN and FTTN, 4G/5G failover, site-to-site VPN, multi-WAN and firmware management. Call 07 3041 8993.",
    "hero_img": "draytek-hero.webp",
    "hero_alt": "Business router and network equipment in a Gold Coast office data cabinet",
    "eyebrow": "Routers",
    "h1": "DrayTek, and why they keep turning up in Australian offices",
    "lede": "NBN handled natively, mobile failover built in, and VPN without a subscription. For a lot of small offices that is the whole requirement.",
    "actions": [("Get a network review", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["NBN & FTTN", "4G/5G failover", "VPN, no subscription", "Config held for you"],
    "crumbs": [("Services", "/services"), ("DrayTek", "/draytek-router-gold-coast")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT configures and supports DrayTek Vigor routers for Gold Coast businesses — NBN
    and FTTN connections, 4G and 5G failover, site-to-site and remote access VPN, multi-WAN, VLAN separation
    and firmware management. DrayTek is the gateway we deploy most often on straightforward sites, including
    on retail fit-outs. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">Why these and not something more expensive</h2>
    <p style="margin-top:16px">DrayTek suits Australian small business for reasons that have little to do with
    the specification. They handle VDSL and FTTN natively rather than through an adapter. Mobile failover is
    built in rather than an add-on. And site-to-site VPN comes with the unit rather than with a subscription
    that renews annually.</p>
    <p style="margin-top:16px">For an office that needs a solid gateway, a second path when the street gets dug
    up, and a tunnel back to head office, that is the entire requirement met without an ongoing licence. On the
    two-store retail fit-out we delivered this year, the gateway is a DrayTek for exactly that reason &mdash;
    the connection type called for it, and matching a badge was never the point.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Models</span>
      <h2>The units we work on</h2>
    </div>
    {models(MODELS)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The DrayTek faults we are actually called to</h2>
      <p>Six, and the first one costs businesses a day every time it happens.</p>
    </div>
    {issues(ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>Where a DrayTek stops being enough</h2>
    <p style="margin-top:16px">It is a router with firewall capability, not an inspection appliance. That
    distinction matters if you need intrusion prevention, detailed logging, or evidence you can hand to an
    insurer or a client answering a security questionnaire.</p>
    <p style="margin-top:16px">At that point <a href="/fortigate-firewall-gold-coast">FortiGate</a> or
    <a href="/sophos-firewall-gold-coast">Sophos</a> is the right spend and the subscription is part of the
    price rather than an upsell. Below that point, a well-configured DrayTek does the job for a fraction of the
    cost, and we would rather tell you that than sell you the bigger unit.</p>

    {trust_note('Whichever gateway you run, keep an exported copy of the configuration somewhere the business controls. Provider hardware gets swapped routinely, and a business with no copy of its own config loses a day every time it happens.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a failover check actually turns up</h2>
      <p>A representative engagement, drawn from real work with client and staff names removed.</p>
    </div>
    {EXAMPLE_1}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Router & Modem Configuration", "/router-and-modem-configuration-gold-coast"),
  ("Business NBN & Internet Support", "/nbn-internet-support-gold-coast"),
  ("FortiGate Firewalls", "/fortigate-firewall-gold-coast"),
  ("Sophos Firewalls", "/sophos-firewall-gold-coast"),
  ("Network Security & Firewalls", "/network-security-and-firewall-configuration-gold-coast"),
], heading="Related")}

{cta("Modem about to be swapped?",
     "Send us the configuration first. Rebuilding one from scratch on a Monday morning is a day nobody planned for.")}
''',
}

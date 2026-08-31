from layout import MARK, cta, faq_block, cards, ticks, related, photo, trust_note

RETAIL = [
    ("Full supply and fit-out", "Every store and head office equipped — workstations, network infrastructure, CCTV, business WiFi and internet connectivity, specified once and deployed consistently."),
    ("National, multi-site delivery", "One technology stack rolled out across Australia, each location commissioned to the same standard and ready to trade on opening day."),
    ("Ongoing service and support", "Continuing support for every store and head office, with the whole store network managed as a single estate rather than dozens of separate sites."),
]

REPS = [
    ("Multi-site business WiFi", None,
     "A business across several premises — office, warehouse, front of house — running a mix of consumer routers. We survey each site, deploy Ubiquiti UniFi with VLAN separation for staff, guests and EFTPOS, centralise management in one controller and hand over documentation. Outcome: seamless roaming everywhere, PCI-DSS-aligned guest isolation, one dashboard for the estate."),
    ("Managed IT for a lean operation", None,
     "A resources business running with no internal IT and a server nobody had checked in years. Discovery, documentation, backups made separate and tested, MFA rolled out, then ongoing monitoring and helpdesk. Outcome: a documented environment, a known recovery position, and a monthly cost that can be budgeted."),
    ("Legacy PBX kept alive", None,
     "A business quoted a full phone system replacement it didn't need. We assessed the existing PBX, found several years of serviceable life, reprogrammed the call flows and took over maintenance. Outcome: a working system, a deferred capital cost, and a planned replacement date rather than a forced one."),
    ("Office relocation", None,
     "A move with a hard trading deadline. We planned the estate move, coordinated cabling and carrier services, staged the server and network cutover across a weekend and tested everything before Monday. Outcome: staff arrived to working desks, phones and internet."),
]

FAQS = [
    ("Can you give examples of work bcom ICT has done?",
     "bcom ICT delivered a full national technology rollout for an Australian retail chain — supplying and installing all computer and networking equipment, CCTV, WiFi and internet connectivity for every store and head office, and continues to support the estate. Other engagements include multi-site business WiFi, managed IT for lean operations, legacy PBX maintenance and office relocations. Call 07 3041 8993."),
    ("Why aren't your clients named?",
     "Because we haven't asked all of them for permission to use their names, and publishing a client logo without asking is a poor way to treat someone who trusts you with their systems. The retail engagement is described accurately but unnamed for that reason. If you want to verify our work, ask for a reference call — we'll arrange one with a client of similar size or in your sector."),
    ("Are the representative engagements real projects?",
     "They describe the shape of work we genuinely do, drawn from real engagements, with identifying detail removed. They're presented that way deliberately rather than dressed up as named case studies. Specific details are shared on request during a consultation."),
    ("Do you only work with large clients?",
     "No — the national rollout is the largest thing we've done, not the typical one. Most of our clients have between three and sixty staff. The rollout matters because it's the model our Australia-wide managed delivery is built on: standardised equipment, remote management and a single point of accountability."),
    ("Can we speak to an existing client?",
     "Yes. Ask and we'll arrange a reference call with a client in a similar sector or of a comparable size. It's a far better signal than any case study we could write about ourselves."),
]

PAGE = {
    "path": "/case-studies",
    "priority": "0.7",
    "title": "Case Studies — bcom ICT at Work | Gold Coast & Australia",
    "description": "A national retail chain technology rollout delivered by bcom ICT, plus representative engagements covering multi-site WiFi, managed IT, legacy PBX and office relocations.",
    "hero_img": "hero-bg-business.webp",
    "hero_alt": "bcom ICT equipment installed across a national Australian retail chain rollout",
    "h1": "What the work actually looks like",
    "lede": "One national rollout described in full, and four representative engagements showing how we structure the projects businesses ask us for most.",
    "actions": [("Discuss your project", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["National delivery", "Multi-site estates", "Ongoing support", "References on request"],
    "crumbs": [("About", "/about"), ("Case studies", "/case-studies")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT delivered a complete national technology rollout for an Australian retail
    chain — supplying and installing all computer and networking equipment, CCTV, business WiFi and internet
    connectivity for every store and head office — and remains the chain's ongoing IT partner. Call
    07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Featured engagement</span>
      <h2>National rollout for an Australian retail chain</h2>
      <p>A new retail chain launching across Australia needed every store, and head office, equipped, connected and supported from day one.</p>
    </div>
    <div class="grid grid--3">{cards([(t, None, d) for t, d in RETAIL])}</div>
    <p style="margin-top:32px">This is the model our Australia-wide managed delivery is built on:
    standardised hardware, remote management, and a single point of accountability run from the Gold Coast.
    The client isn't named here because we haven't asked their permission to name them — see the FAQ below.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Representative engagements</span>
      <h2>How we structure the common ones</h2>
      <p>These describe the shape of real work with identifying detail removed. Specific details are shared on request during a consultation.</p>
    </div>
    <div class="grid grid--2">{cards(REPS, icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>Ask for a reference instead</h2>
        <p style="margin-top:16px">Case studies are written by the company that did the work, which limits
        how much they're worth. A conversation with a client who has actually lived with us for a few years
        tells you considerably more.</p>
        <p style="margin-top:16px">Ask and we'll arrange a reference call with a client in your sector or of
        a similar size. We'd genuinely rather you did that than take our word for any of the above.</p>
        {ticks([
          "A client of comparable size, or in your industry",
          "A direct conversation, not a prepared quote",
          "Ask them what went wrong at some point and how we handled it — that's the useful question",
        ])}
      </div>
      {photo("data-cabling-gold-coast.webp", "Structured cabling and network infrastructure installed by bcom ICT for a commercial client", "Multi-site estates commissioned to one standard, then supported as a single environment.")}
    </div>

    {trust_note('What we commit to on every engagement — response targets, change control, and what happens to your documentation if you leave — is published on <a href="/service-levels-and-security">our service levels page</a>.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Reviews", "/reviews"),
  ("About bcom ICT", "/about"),
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
  ("Business WiFi", "/business-wifi-gold-coast"),
  ("Office IT Relocation", "/office-it-relocation-gold-coast"),
  ("Published service levels", "/service-levels-and-security"),
], heading="Related")}

{cta("Got a project like one of these?",
     "Tell us the shape of it and we'll tell you honestly whether we're the right size for the job.")}
''',
}

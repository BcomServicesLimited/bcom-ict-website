from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues

UNIFI = [
    "<strong>You want cameras on the same system.</strong> UniFi Protect runs on the same controller as the network, so one login covers WiFi, switching and CCTV. Nothing in the Instant On range does this.",
    "<strong>The site is complicated.</strong> Multiple VLANs, a warehouse alongside an office, point-to-point links between buildings, PoE budgets that need thinking about &mdash; UniFi has the range and the configurability.",
    "<strong>You will grow into it.</strong> Access control, phones, gateways and switching all sit on the same platform, so adding a piece later does not mean adding a system.",
    "<strong>Somebody will administer it.</strong> Either you have someone technical, or you have a provider. It rewards attention and it expects it.",
]

ARUBA = [
    "<strong>You want it to disappear.</strong> Cloud-managed from an app, no controller to host, no firmware choreography. For a business that wants WiFi to be a utility, this is the point.",
    "<strong>The site is straightforward.</strong> One office, one or two floors, a guest network and a staff network. Instant On does that cleanly and does not ask you for decisions you should not have to make.",
    "<strong>Nobody is going to administer it.</strong> No controller means nothing to leave running on a laptop under a desk, which is the single most common way a UniFi network becomes unmanageable.",
    "<strong>You value the backing.</strong> It is HPE Aruba's small-business line, with the support structure that comes with that.",
]

DECIDE = [
    ("Do you want CCTV on it?", None, "If yes, that is usually the end of the conversation — UniFi Protect is the reason most of our clients land on UniFi."),
    ("Who administers it?", None, "A network with an owner suits UniFi. A network with nobody suits Instant On, because there is less that can drift."),
    ("How complicated is the site?", None, "One tidy office is a job either range does well. A warehouse, a second building or serious VLAN separation pushes it toward UniFi."),
    ("What happens in three years?", None, "If the answer includes cameras, door access or another site, buying into the larger ecosystem now costs nothing extra."),
]

MISTAKES = [
    ("&ldquo;UniFi is the professional one&rdquo;",
     "brand reputation doing the deciding. UniFi is deeper, which is not the same as better for your site &mdash; depth you never use is complexity you pay for in administration.",
     "Pick on the building and the administration, not on which range sounds more serious. A one-office business with nobody technical is genuinely better served by the simpler platform."),
    ("&ldquo;Instant On is the cheap one&rdquo;",
     "a price comparison at the access point that ignores everything else. Add a controller to a UniFi quote and the gap narrows; add CCTV to an Instant On quote and it reverses.",
     "Compare the whole system you will actually end up with in three years, including cameras if cameras are coming."),
    ("&ldquo;We will just add cameras later&rdquo;",
     "a reasonable plan that quietly forecloses an option. If cameras are likely, choosing Instant On means a second platform, a second login and a second support path when they arrive.",
     "Decide the camera question up front even if the cameras are two years away. It is the cheapest decision on this page and the most expensive one to reverse."),
    ("&ldquo;More access points means better coverage&rdquo;",
     "the most expensive misunderstanding in wireless, and it applies to both ranges equally. Overlapping access points at high power interfere with each other and make roaming worse.",
     "Survey the building, place fewer units properly, and tune the transmit power down. We have fixed coverage complaints by removing hardware."),
    ("&ldquo;The WiFi is slow, so we need new access points&rdquo;",
     "a conclusion drawn before anything was measured. A saturated uplink, a failing switch port or an internet service that degrades in the afternoon all present as slow WiFi.",
     "Measure the wired path and the connection before replacing anything wireless. This is the single most common reason a wireless quote should not have been written."),
]

FAQS = [
    ("Is Ubiquiti UniFi or Aruba Instant On better for a small business?",
     "Neither is better in general — they answer different questions. UniFi suits a business that wants cameras, access control and networking on one platform and has someone to administer it. Aruba Instant On suits a business that wants reliable WiFi with nothing to manage. bcom ICT installs and supports both across the Gold Coast, so the recommendation depends on the building and who will look after it, not on what we would rather sell."),
    ("Which is cheaper?",
     "The hardware is broadly comparable at the access point level, and the real cost difference is elsewhere. UniFi may need a controller — a Cloud Key or a gateway that hosts one — which Instant On does not. Against that, if you also want CCTV, UniFi covers it on the same platform where Instant On means a second system and a second cost."),
    ("Can I run UniFi without a controller?",
     "The access points keep working if the controller is off, but nothing can be changed, monitored or updated while it is. Running the controller on somebody's laptop is the most common mistake we see on UniFi networks, and it is why a dedicated device or a hosted controller matters."),
    ("Does Aruba Instant On do VLANs and guest networks?",
     "Yes, both, and it does them cleanly. What it does not do is the depth UniFi offers — the granular controls, the ecosystem breadth or the CCTV integration. For most single-office businesses that depth is not needed and its absence is a feature."),
    ("Can we mix the two?",
     "You can run them on the same network but not manage them together, so you end up with two systems and two logins. On one site we would pick one and stay with it."),
    ("What does bcom ICT install most often?",
     "UniFi, because a large share of our clients want cameras on the same platform as the network. That is a reflection of what those clients asked for rather than a general recommendation, and we install Instant On regularly where simplicity is the priority."),
]

PAGE = {
    "path": "/unifi-vs-aruba-instant-on",
    "priority": "0.8",
    "title": "UniFi vs Aruba Instant On — Which Suits Your Business? | bcom ICT",
    "description": "An honest comparison of Ubiquiti UniFi and Aruba Instant On for Australian small business WiFi — what each is genuinely better at, and the four questions that decide it. bcom ICT installs both.",
    "hero_img": "compare-unifi-aruba-hero.webp",
    "hero_alt": "A bcom ICT technician explaining business WiFi options to a Gold Coast business owner",
    "eyebrow": "Comparison",
    "h1": "UniFi or Aruba Instant On?",
    "lede": "Two good ranges that answer different questions. We install both, so here is the honest version rather than the one that suits whichever we would rather sell you.",
    "crumbs": [("Services", "/services"), ("UniFi vs Aruba Instant On", "/unifi-vs-aruba-instant-on")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">Ubiquiti UniFi and Aruba Instant On are both strong choices for Australian small business
    WiFi and they suit different situations. UniFi suits a business that wants networking, cameras and access
    control on one platform and has somebody to administer it. Aruba Instant On suits a business that wants
    reliable WiFi with nothing to manage. bcom ICT installs and supports both across the Gold Coast.
    Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">The difference that actually matters</h2>
    <p style="margin-top:16px">Comparisons of these two usually turn into a specification table, which is
    unhelpful because at the access point level they are closer than the tables suggest. Both do WiFi 6 well.
    Both handle guest networks and VLANs. Both will comfortably cover an office.</p>
    <p style="margin-top:16px">The real difference is philosophical. <strong>UniFi is a platform</strong>
    &mdash; networking, cameras, door access, phones and gateways designed to be run together, with the
    configurability that implies and the administration that comes with it.
    <strong>Instant On is an appliance</strong> &mdash; cloud-managed, deliberately narrower, built so that
    once it is installed nobody has to think about it again.</p>
    <p style="margin-top:16px">Neither of those is the better answer. Which one is right depends entirely on
    whether your business wants a platform or wants to stop thinking about WiFi.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Choose UniFi when</span>
      <h2>UniFi earns its keep here</h2>
    </div>
    {ticks(UNIFI)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Choose Instant On when</span>
      <h2>And Instant On is the better answer here</h2>
    </div>
    {ticks(ARUBA)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How to decide</span>
      <h2>Four questions that settle it</h2>
      <p>In roughly this order. The first one decides most of them on its own.</p>
    </div>
    <div class="grid grid--2">{cards(DECIDE)}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common mistakes</span>
      <h2>What people get wrong choosing between them</h2>
      <p>Five we hear regularly, and the last two apply whichever range you pick.</p>
    </div>
    {issues(MISTAKES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>What neither of them fixes</h2>
    <p style="margin-top:16px">Worth saying, because it is where most WiFi money gets wasted. Access points
    do not fix a building. If the coverage problem is a rendered wall, a partitioned meeting room or a warehouse
    surveyed before the racking went in, the badge on the box changes nothing.</p>
    <p style="margin-top:16px">Nor do they fix what is behind them. We have replaced a switch with a failing
    port on a site where a full wireless replacement had already been quoted, and the wireless was never the
    problem. Survey first, and buy afterwards.</p>

    {trust_note('If you are choosing between these two, the useful conversation is about your building and who will look after the network &mdash; not about the hardware. See <a href="/business-wifi-gold-coast">business WiFi installation</a>, or read the two brand pages: <a href="/ubiquiti-unifi-wifi-gold-coast">UniFi</a> and <a href="/aruba-instant-on-wifi-gold-coast">Aruba Instant On</a>.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Ubiquiti UniFi WiFi & Protect", "/ubiquiti-unifi-wifi-gold-coast"),
  ("Aruba Instant On WiFi", "/aruba-instant-on-wifi-gold-coast"),
  ("Business WiFi Installation", "/business-wifi-gold-coast"),
  ("Network Security & Firewalls", "/network-security-and-firewall-configuration-gold-coast"),
  ("Retail fit-out case study", "/retail-store-technology-fitout-case-study"),
], heading="Related")}

{cta("Not sure which fits?",
     "Tell us about the building and who will be looking after it. That conversation decides this far more reliably than a spec sheet.")}
''',
}

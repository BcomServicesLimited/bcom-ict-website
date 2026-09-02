from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues, models, example

MODELS = [
    ("Desktop range", "The units most Gold Coast small businesses run — a single office, a handful of VLANs, remote access for staff working from home.",
     ["FortiGate 40F", "FortiGate 50G", "FortiGate 60F", "FortiGate 70F", "FortiGate 80F"]),
    ("Larger sites", "More throughput, more interfaces, and the headroom to keep inspection turned on when the connection is fast.",
     ["FortiGate 90G", "FortiGate 100F", "FortiGate 200F"]),
    ("The part that matters", "FortiOS runs the lot. The security services — intrusion prevention, web filtering, application control, antivirus — are subscription, and that is where the real cost and the real risk sit.",
     ["FortiOS", "FortiGuard", "UTP bundle", "FortiCloud"]),
]

ISSUES = [
    ("&ldquo;Our FortiGate licence expired and nobody told us&rdquo;",
     "a subscription that lapsed quietly. The unit keeps routing traffic, so nothing appears broken &mdash; but intrusion prevention, web filtering and antivirus stop updating, and eventually stop.",
     "Check the entitlement, renew it, and put the expiry in a register with the renewal date and notice period. A FortiGate with dead services is an expensive router."),
    ("&ldquo;It is slow since we upgraded the internet&rdquo;",
     "a unit sized for the old connection. Deep inspection is processor-intensive, and a firewall comfortable on 50/20 can become the bottleneck on a gigabit service.",
     "Check the throughput figures with inspection enabled rather than the headline number, which assumes everything is turned off. Sometimes the answer is a bigger unit; sometimes it is a rule doing more work than it needs to."),
    ("&ldquo;There are rules nobody can explain&rdquo;",
     "years of additions by different hands, including inbound rules for suppliers and systems that no longer exist.",
     "Audit the policy against what the business actually does now. We have removed inbound access for a supplier a client stopped using four years earlier."),
    ("&ldquo;Remote access is a port forward&rdquo;",
     "remote desktop published straight to the internet because it was the quickest way to get someone working from home.",
     "Move it behind the VPN the unit already includes. Published RDP is among the most reliably attacked things on the Australian internet and the FortiGate is already licensed to replace it."),
    ("&ldquo;The firmware has not been touched since install&rdquo;",
     "a device nobody wants to reboot during business hours, so nobody ever does.",
     "Schedule it outside trading, with the configuration backed up and a way back. Firewall firmware carries security fixes, and a firewall running years-old code is the wrong thing to leave alone."),
    ("&ldquo;Nobody local will touch it&rdquo;",
     "a unit configured by a provider who has moved on, with credentials that went with them.",
     "We recover administrative access, document the policy and hand you the configuration. You should not need to book a technician to add a rule."),
]

EXAMPLE_1 = example(
    "Three years of protection that had quietly stopped",
    "A professional firm engaged us after a client security questionnaire asked what protection sat on their network. They had a FortiGate, it had been installed by a previous provider, and they believed the question was easy to answer.",
    "The security subscription had lapsed a little over three years earlier. The unit was still routing traffic perfectly, so nothing had ever looked wrong &mdash; but intrusion prevention, web filtering, application control and antivirus had all stopped receiving updates within weeks of the expiry. The firm had been paying for a firewall and running a router. The renewal notice had gone to a mailbox belonging to the provider who installed it.",
    "Confirmed the entitlement status, renewed the subscription, then audited the policy while we were in there. That found two inbound rules for systems the firm no longer used and a published remote desktop port that predated the VPN the unit was already licensed for. Moved remote access behind the VPN with multi-factor authentication, and put the renewal date into a register the firm holds with the notice period against it.",
    "The questionnaire was answered accurately. The uncomfortable part is that nothing had failed and nothing had alerted &mdash; a lapsed FortiGate subscription is invisible from the inside, which is exactly why it needs a date in a register rather than a notification in somebody else's inbox.")
FAQS = [
    ("Does bcom ICT support FortiGate firewalls?",
     "Yes. bcom ICT configures, supports and maintains FortiGate units for businesses across the Gold Coast and Australia-wide — policy design, VLAN segmentation, site-to-site and remote access VPN, security service subscriptions, firmware and licence management. We are not a Fortinet-only shop, which means we will tell you when a FortiGate is more firewall than your business needs."),
    ("What happens when a FortiGate licence expires?",
     "The unit keeps passing traffic, so nothing looks broken. What stops is the subscription services — intrusion prevention, web filtering, application control and antivirus stop receiving updates and eventually stop working. It is the most common gap we find on an inherited FortiGate, because nothing announces it."),
    ("Which FortiGate model suits a small business?",
     "For most single-office Gold Coast businesses, the desktop range — the 40F through 80F — is the right band, and the deciding factor is your internet speed with inspection turned on rather than headcount. The published throughput figures assume inspection is off, so a unit sized on those numbers will disappoint."),
    ("Is a FortiGate overkill for a small business?",
     "Sometimes, and we will say so. If you have a straightforward office, no compliance obligation and no site-to-site requirement, a well-configured DrayTek or the firewall in a UniFi gateway may serve you better for less. FortiGate earns its keep where you need real intrusion prevention, detailed logging and evidence for a client or an insurer."),
    ("Can you take over a FortiGate someone else configured?",
     "Routinely. We recover administrative access, audit the policy against what the business actually does, document it and hand the configuration to you. Inherited firewalls are usually where we find inbound rules for systems that stopped existing years ago."),
    ("Do you do FortiGate VPN for remote workers?",
     "Yes, and it is usually the first thing we change on an inherited unit. Published remote desktop gets replaced with the VPN the FortiGate is already licensed for, with multi-factor authentication in front of it."),
]

PAGE = {
    "path": "/fortigate-firewall-gold-coast",
    "priority": "0.8",
    "service": "FortiGate Firewall Support Gold Coast",
    "title": "FortiGate Firewall Support Gold Coast | bcom ICT",
    "description": "FortiGate firewall configuration, support and licence management for Gold Coast businesses. Call 07 3041 8993.",
    "hero_img": "fortigate-hero.webp",
    "hero_alt": "Business network security equipment installed in a Gold Coast office comms cabinet",
    "eyebrow": "Firewalls",
    "h1": "FortiGate, configured properly and kept current",
    "lede": "The hardware is the easy part. The licence that quietly expired and the inbound rule nobody can explain are what we actually get called about.",
    "actions": [("Get a firewall review", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Policy audits", "Licence management", "VPN & segmentation", "Vendor-neutral advice"],
    "crumbs": [("Services", "/services"), ("FortiGate", "/fortigate-firewall-gold-coast")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT configures, supports and maintains FortiGate firewalls for businesses across the
    Gold Coast and Australia-wide — policy design, VLAN segmentation, remote access and site-to-site VPN,
    security subscription management, firmware and inherited-unit takeovers. We work with several firewall
    ranges, so we will tell you when a FortiGate is more than your business needs. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">The licence is the part that catches people</h2>
    <p style="margin-top:16px">A FortiGate is two things bought together: a box, and a subscription to the
    services that make it a security device rather than a router. Intrusion prevention, web filtering,
    application control and antivirus all depend on that subscription being current.</p>
    <p style="margin-top:16px">When it lapses, nothing visible happens. Traffic keeps flowing, staff keep
    working, and the business carries on believing it is protected while the protection quietly stops updating.
    It is the single most common thing we find on a FortiGate we did not install, and it is why licence expiry
    belongs in a register with a renewal date rather than in an inbox somebody left.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Models</span>
      <h2>The units we work on</h2>
      <p>People search by the thing in their cupboard, so here is the range rather than a brand name.</p>
    </div>
    {models(MODELS)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The FortiGate faults we are actually called to</h2>
      <p>Six situations, and only one of them needs new hardware.</p>
    </div>
    {issues(ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>When a FortiGate is the wrong answer</h2>
    <p style="margin-top:16px">It is a serious firewall and it is priced like one, both up front and every
    year afterwards. For a straightforward single office with no compliance obligation and no site-to-site
    requirement, the money is often better spent elsewhere &mdash; a
    <a href="/draytek-router-gold-coast">DrayTek</a> handles NBN, failover and VPN capably, and the gateway in
    a <a href="/ubiquiti-unifi-wifi-gold-coast">UniFi</a> stack covers a tidy office well.</p>
    <p style="margin-top:16px">Where a FortiGate genuinely earns its keep: real intrusion prevention, detailed
    logging you can hand to an insurer or a client, segmentation that has to hold up under scrutiny, and
    businesses answering security questionnaires. If that is you, it is the right tool and the subscription is
    part of the price rather than an upsell.</p>

    {trust_note('We work across FortiGate, <a href="/sophos-firewall-gold-coast">Sophos</a> and <a href="/draytek-router-gold-coast">DrayTek</a> and have no reseller target to hit on any of them. See <a href="/network-security-and-firewall-configuration-gold-coast">network security and firewall configuration</a> for the work itself.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What an inherited FortiGate usually turns up</h2>
      <p>A representative engagement, drawn from real work with client and staff names removed.</p>
    </div>
    {EXAMPLE_1}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Network Security & Firewalls", "/network-security-and-firewall-configuration-gold-coast"),
  ("Sophos Firewall", "/sophos-firewall-gold-coast"),
  ("DrayTek Routers", "/draytek-router-gold-coast"),
  ("Cybersecurity Health Check", "/cybersecurity-health-check-for-small-business-gold-coast"),
  ("Essential Eight Assessment", "/essential-eight-guide-gold-coast"),
], heading="Related")}

{cta("Inherited a FortiGate?",
     "We will check the licence status, audit the policy and tell you what is actually in there. Most inherited firewalls have at least one rule nobody can account for.")}
''',
}

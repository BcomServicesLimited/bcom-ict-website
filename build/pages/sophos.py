from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues, models, example

MODELS = [
    ("Desktop range", "The XGS units most small businesses run — an office, a few VLANs, remote access and site-to-site VPN.",
     ["XGS 87", "XGS 88", "XGS 107", "XGS 116", "XGS 126", "XGS 136"]),
    ("Managed from the cloud", "Sophos Central is the console. Firewall, endpoint and email sit in one place, which is the whole argument for the range.",
     ["Sophos Central", "Xstream protection", "Synchronized Security"]),
    ("Also supported", "The older SG and XG units are still in service across the Gold Coast and we work on them, including the ones now past support.",
     ["SG series", "XG series", "Sophos Firewall OS"]),
]

ISSUES = [
    ("&ldquo;We have Sophos endpoint but the firewall is something else&rdquo;",
     "the two products bought at different times from different suppliers. It works, and it gives up the main reason to run Sophos at all.",
     "Synchronized Security is the argument for this range &mdash; the firewall and the endpoint talk to each other, so a compromised machine gets isolated automatically. Split across vendors, you are paying for a feature you cannot use."),
    ("&ldquo;Everything is in Sophos Central and nobody looks at it&rdquo;",
     "a console doing its job and reporting into a void. Alerts accumulate, nobody is assigned to them, and the useful ones sit alongside the noise.",
     "Decide who reads it and how often, or have somebody read it for you. A console nobody opens is a log file with a nicer interface."),
    ("&ldquo;Our XG unit is out of support&rdquo;",
     "hardware that reached end of life while still working perfectly. It keeps running and it stops receiving firmware.",
     "Check the support status before anything else. A firewall that cannot be patched is the one device on the network where that genuinely cannot be tolerated."),
    ("&ldquo;The web filtering is blocking something it shouldn&rsquo;t&rdquo;",
     "category filtering applied broadly, catching a legitimate business tool alongside the things it was meant to stop.",
     "Tune the exceptions rather than turning the category off. The usual outcome of a frustrating block is somebody disabling protection wholesale, which is worse than the original problem."),
    ("&ldquo;Remote access is slow since everyone went home&rdquo;",
     "a VPN carrying all traffic including things that never needed to come back through the office.",
     "Split what genuinely needs the tunnel from what does not, and check the unit is sized for concurrent users rather than for the connection speed."),
    ("&ldquo;Nobody knows the Central credentials&rdquo;",
     "an account created by a previous provider under their own details, which is the same ownership problem we find on cloud-managed WiFi.",
     "Establish ownership under an account the business controls. This is worth checking today rather than on the day you need to change something urgently."),
]

EXAMPLE_1 = example(
    "Two Sophos products that had never been introduced",
    "A business of thirty staff ran Sophos endpoint on every machine and a Sophos firewall at the edge. They had chosen the range deliberately, on the strength of the two working together, and had been paying for both for four years.",
    "They were two separate deployments. The endpoint had been rolled out by one supplier and the firewall installed by another eighteen months later, each into its own Sophos Central account. Both products worked. Synchronized Security &mdash; the automatic isolation of a compromised machine, which is the entire argument for buying the pair &mdash; had never been enabled, because the two halves could not see each other. Nobody had done anything wrong; the feature simply requires both products in one console and nobody had ever been asked to check.",
    "Consolidated both into a single Sophos Central tenancy owned by the business rather than by either supplier, enabled Synchronized Security, and tested it by triggering an isolation on a spare machine so the client could watch it work.",
    "They now get the feature they had been paying for since the second install. It cost an afternoon. The wider lesson is that buying a matched set is not the same as deploying one, and it is worth checking on any estate assembled in stages.")
FAQS = [
    ("Does bcom ICT support Sophos firewalls?",
     "Yes. bcom ICT configures and supports Sophos Firewall units — the current XGS range and the older SG and XG series still in service — including policy design, VLAN segmentation, VPN, web and application control, and Sophos Central management. We work across several firewall ranges rather than one, so the recommendation is not shaped by a reseller target."),
    ("What is Synchronized Security and does it matter?",
     "It is the feature that makes Sophos worth choosing as a set. The firewall and the endpoint software talk to each other, so a machine showing signs of compromise gets isolated from the network automatically rather than waiting for someone to notice. If you run Sophos endpoint already, matching the firewall is the single strongest argument for this range. If you do not, that argument disappears."),
    ("Is Sophos better than FortiGate?",
     "Neither is better in general. Sophos suits a business that wants firewall, endpoint and email in one console and values the automatic isolation between them. FortiGate suits a business that wants the deepest inspection and logging, particularly where evidence for an insurer or a client matters. Both are serious products and both are more than many small offices need."),
    ("Our Sophos unit is out of support — does it need replacing?",
     "Probably, and this is the one case where we would not argue for keeping working hardware. A firewall is the device on your network where the inability to receive security patches matters most. We will confirm the support status and tell you what the actual exposure is before quoting anything."),
    ("Can you take over a Sophos firewall someone else set up?",
     "Yes. We recover access to Sophos Central, audit the policy against what the business actually does, document it, and put ownership of the account in the business's name rather than a provider's. That last part is worth checking even if you are not changing providers."),
    ("Do you support Sophos endpoint as well?",
     "Yes, and where a client runs both we configure them as a pair so the isolation works. Running the firewall from one vendor and the endpoint from another is common and it costs you the feature you are paying for."),
]

PAGE = {
    "path": "/sophos-firewall-gold-coast",
    "priority": "0.8",
    "service": "Sophos Firewall Support Gold Coast",
    "title": "Sophos Firewall Support Gold Coast — XGS | bcom ICT",
    "description": "Sophos Firewall configuration and support for Gold Coast businesses — XGS, SG and XG units, Sophos Central management. Call 07 3041 8993.",
    "hero_img": "sophos-hero.webp",
    "hero_alt": "Network security equipment in a Gold Coast business comms room",
    "eyebrow": "Firewalls",
    "h1": "Sophos, set up so the parts talk to each other",
    "lede": "The reason to run Sophos is that the firewall and the endpoint work as a pair. Most of the Sophos estates we inherit are not configured that way.",
    "actions": [("Get a firewall review", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["XGS, SG & XG", "Sophos Central", "Synchronized Security", "Vendor-neutral advice"],
    "crumbs": [("Services", "/services"), ("Sophos", "/sophos-firewall-gold-coast")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT configures and supports Sophos Firewall for businesses across the Gold Coast —
    the current XGS range and the older SG and XG units still in service — covering policy design, VLAN
    segmentation, VPN, web and application control, and Sophos Central management. We work across several
    firewall ranges rather than one. Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">The feature most Sophos estates are not using</h2>
    <p style="margin-top:16px">Sophos is not really sold as a firewall. It is sold as a set &mdash; firewall,
    endpoint and email, managed from one console, with the pieces talking to each other. When a machine starts
    behaving like it is compromised, the endpoint tells the firewall and the firewall isolates it, without
    anybody noticing first.</p>
    <p style="margin-top:16px">That is a genuinely good idea and it is the main reason to choose this range.
    It is also the part most businesses are not getting, because the firewall was bought at one point from one
    supplier and the endpoint at another point from another. Both products work. The thing you were paying for
    does not.</p>
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
      <h2>The Sophos faults we are actually called to</h2>
    </div>
    {issues(ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <h2>Choosing between Sophos and the alternatives</h2>
    <p style="margin-top:16px">If you already run Sophos endpoint, matching the firewall is the strongest
    argument on this page and it is worth acting on. If you do not, that argument disappears and the choice
    opens up.</p>
    <p style="margin-top:16px"><a href="/fortigate-firewall-gold-coast">FortiGate</a> goes deeper on inspection
    and logging, which matters when you need evidence for an insurer or a client questionnaire.
    <a href="/draytek-router-gold-coast">DrayTek</a> is a fraction of the cost and covers NBN, failover and
    site-to-site VPN capably for an office that does not need full inspection. All three are on our bench and
    none of them carries a target we have to hit.</p>

    {trust_note('There is one situation where we would replace working hardware without hesitating: a firewall past end of support. It is the one device on the network where being unable to patch is not survivable.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What we find on a Sophos estate we did not build</h2>
      <p>A representative engagement, drawn from real work with client and staff names removed.</p>
    </div>
    {EXAMPLE_1}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Network Security & Firewalls", "/network-security-and-firewall-configuration-gold-coast"),
  ("FortiGate Firewalls", "/fortigate-firewall-gold-coast"),
  ("DrayTek Routers", "/draytek-router-gold-coast"),
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
  ("24/7 Security Operations Centre", "/security-operations-centre-gold-coast"),
], heading="Related")}

{cta("Running Sophos endpoint already?",
     "Then the firewall question is easier than it looks, and there is a good chance you are not getting the feature you are paying for. We will check.")}
''',
}

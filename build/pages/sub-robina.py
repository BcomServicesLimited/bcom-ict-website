from layout import MARK, cta, faq_block, cards, ticks, related, nearby, trust_note, example, booking_cta

LOCAL_EX = example(
    "A Robina office that had outgrown its cabling",
    "A professional services firm in a Robina commercial building had grown from nine people to twenty-six in the same tenancy. Network problems had become steadily more frequent and were being blamed on the internet connection.",
    "The tenancy had been cabled for the original fit-out with twelve outlets. Desk switches had been added under desks as people arrived, chained one to another, and two of them were consumer units bought at retail. The internet service was performing exactly as specified &mdash; the building&rsquo;s internal network had simply been extended past the point where it worked.",
    "Ran additional certified outlets to every position, replaced the chained desk switches with proper switching in a single cabinet, and documented the whole thing on a port schedule.",
    "The faults stopped and the internet plan was left alone. Robina&rsquo;s office buildings suit growing professional firms well, and outgrowing the original fit-out is the most common thing we are called about here.")
FAQS = [   (   'Do you provide IT support in Robina?',
        'Yes. bcom ICT attends Robina businesses from its Surfers Paradise office, roughly twenty minutes away, with same-day attendance usually available. We cover Robina Town Centre, Robina Town '
        'Centre Drive, Laver Drive, Cheltenham Drive, Robina Quays and the hospital precinct. Most faults are resolved remotely first. Call 07 3041 8993.'),
    (   'Can you answer supplier security questionnaires?',
        "Yes, and Robina's corporate tenants send them more often than anywhere else on the coast. Our published service levels and trust centre set out response targets, framework alignment, "
        'credentials, insurance and data handling — most questionnaires can be answered directly from those. Where something is missing, we will write it.'),
    (   'Do you work with AFS licensees in Robina?',
        'Yes. Cyber resilience falls within the general obligations of a financial services licence, which means implemented controls plus documented evidence and oversight of outsourced '
        'arrangements including your IT provider. We deliver gap assessment, remediation and an evidence pack — see our ASIC cybersecurity compliance page.'),
    (   "Our business has grown and the IT hasn't kept up. Where do we start?",
        'That is the most common pattern in Robina. Usually the network, specified when the firm was much smaller and never revisited — plus backups nobody has watched restore and multi-factor '
        'authentication on some accounts but not all. The initial review is free and you keep the written report either way.'),
    (   'Do you support hybrid and remote working?',
        'Yes, and it is standard for professional tenants here. The principle is that security travels with the device rather than living in the office — managed laptops with encryption and remote '
        'wipe, MFA everywhere, and document access through a controlled system rather than files copied to a desktop.'),
    (   'How much does IT support cost in Robina?',
        '$190 + GST per hour ($209.00 inc GST) plus a $100 + GST call-out ($110.00 inc GST) for on-site attendance. Remote support carries no call-out. Managed IT is a flat monthly fee calculated from '
        'your business requirements and the services included, quoted after a free review.')]

PAGE = {
    "path": '/it-support-robina-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Robina — Corporate & Professional | bcom ICT',
    "description": "IT support for Robina businesses — Robina Town Centre, the hospital precinct, Robina Quays and the surrounding corporate offices.",
    "hero_img": 'hero-bg-business.webp',
    "hero_alt": 'A Robina corporate office supported by bcom ICT',
    "h1": "IT support for Robina's business precinct",
    "lede": 'Robina was planned rather than accumulated, and it shows. Purpose-built premises, corporate tenants, and procurement processes that expect documented answers.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~20 min from our office', 'Corporate & professional', 'Modern buildings', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Robina', '/it-support-robina-gold-coast')],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides IT support to businesses in Robina — corporate offices, financial services, legal and accounting practices and medical suites concentrated around Robina Town Centre, the hospital precinct and the surrounding business parks. Attendance is roughly twenty minutes from our Surfers Paradise office. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Local landscape</span>
      <h2>What Robina is actually like to work in</h2>
    </div>
    <p style="margin-top:16px">Robina is one of the few genuinely master-planned commercial areas on
    the Gold Coast, and working in it feels different because of that. The road layout makes sense, the
    commercial space was purpose-built, and the buildings tend to have proper comms rooms rather than a
    cupboard someone repurposed. Installations here run closer to plan than almost anywhere else on the
    coast.</p>
    <p style="margin-top:16px"><strong>Robina Town Centre</strong> anchors the retail, with the surrounding
    office space through Robina Town Centre Drive, Laver Drive and Cheltenham Drive holding a dense
    concentration of professional and corporate tenants. A lot of these are branch offices or head offices of
    larger operations rather than owner-operated small businesses — which changes what they ask for.</p>
    <p style="margin-top:16px">The <strong>hospital precinct</strong> — Robina Hospital and Robina Private —
    produces the usual satellite cluster of specialist suites, allied health, diagnostics and medical
    administration. <strong>Bond University</strong> sits just across at Varsity Lakes, and its influence
    spills into the professional and consulting businesses through both suburbs.</p>
    <p style="margin-top:16px">Financial services are unusually concentrated here: AFS licensees, mortgage and
    finance brokers, advice practices and insurance brokers. For those businesses, cyber resilience is not
    good practice sitting alongside their obligations — it sits inside their licence conditions, and ASIC has
    been increasingly willing to treat it that way.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who we work with here</span>
      <h2>The businesses we see most in Robina</h2>
      <p>Corporate tenants and regulated practices dominate, which shapes what they need from a provider.</p>
    </div>
    <div class="grid grid--2">{cards([('Financial services and AFS licensees', None, 'Brokers, planners and advice practices around the Town Centre and Robina Quays. Cyber resilience sits within general licence obligations, which means implemented controls plus documented evidence and oversight of outsourced arrangements — including their IT provider. See our ASIC compliance page.'), ('Accounting and legal practices', None, 'Concentrated client identity and financial information, hybrid working as standard, and clients increasingly asking suppliers to evidence how that information is protected.'), ('Corporate branch and head offices', None, 'The ones that send supplier security questionnaires and expect documented response commitments rather than assurances. Our published service levels exist partly for exactly that conversation.'), ('Medical and allied health', None, 'Suites in and around the hospital precinct. Privacy Act obligations apply regardless of turnover for health service providers, and attending technicians hold police checks and Blue Cards where required.'), ('Retail and food around the Town Centre', None, 'Point of sale and payment terminal uptime, segmented networks and internet failover so an outage does not stop trading.'), ('Growth-stage businesses', None, 'Firms that started with five people and now have twenty-five on the same consumer router. Nothing has failed yet, but nothing has been designed either.')], icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What's technically different about Robina</h2>
    <p style="margin-top:16px"><strong>Purpose-built premises remove most of the surprises.</strong>
    Comms rooms with power and ventilation, structured cabling already installed, sensible riser access. Compared
    with the converted shopfronts in <a href="/it-support-burleigh-heads-gold-coast">Burleigh Heads</a> or the
    layered retrofits in <a href="/it-support-southport-gold-coast">Southport</a>, a Robina fit-out is
    predictable — which means quotes tend to hold.</p>
    <p style="margin-top:16px"><strong>Corporate tenants ask harder questions.</strong> Supplier security
    questionnaires, documented response targets, evidence of insurance, and questions about where data is
    held and who can reach it. These arrive more often in Robina than anywhere else on the coast, and they are
    answerable directly from our published service levels, trust centre and data handling pages rather than
    requiring a bespoke response each time.</p>
    <p style="margin-top:16px"><strong>Regulated practices need evidence, not just controls.</strong> For an
    AFS licensee, having multi-factor authentication enabled is necessary but not sufficient. Being able to
    demonstrate in writing when it was implemented, who it covers and how it is reviewed is what an
    assessment actually turns on. That evidence pack is a specific piece of work.</p>
    <p style="margin-top:16px"><strong>Growth is the recurring pattern.</strong> Businesses here scale
    faster than their infrastructure. The most common finding when we take on a Robina client is a network
    specified for a much smaller company, still running, with nobody having revisited it since.</p>

    <div class="rule">{MARK}</div>

    <h2>Getting to you</h2>
    <p style="margin-top:16px">Robina is roughly twenty minutes from our office at 9 Ferny Avenue,
    Surfers Paradise, via the M1 or the Gold Coast Highway. Same-day attendance is usually available.</p>
    <p style="margin-top:16px">Most faults are resolved remotely first — $190 + GST per hour with no call-out
    against $290 + GST for a first hour on site. Email, Microsoft 365, software, account and printer problems
    rarely need anyone to travel, and we will say so on the phone rather than booking a visit by default.</p>
    <p style="margin-top:16px">Managed IT clients have a contracted 4-hour response on critical faults with
    after-hours attendance included under their agreement.</p>

    <h2 style="margin-top:48px">Streets and precincts we regularly attend</h2>
    <p style="margin-top:16px">We attend businesses throughout Robina and the surrounding precincts, including:</p>
    {ticks(['Robina Town Centre and the surrounding retail and office space', 'Robina Town Centre Drive, Laver Drive and Cheltenham Drive', 'Robina Quays and the surrounding business park space', 'The Robina Hospital and Robina Private Hospital precinct', "Scottsdale Drive and the corridor toward <a href='/it-support-varsity-lakes-gold-coast'>Varsity Lakes</a>", 'Robina Parkway, Ron Penhaligon Way and the CBUS Super Stadium precinct', 'Mudgeeraba, Reedy Creek and Merrimac, where our Robina coverage extends', "Clear Island Waters and the corridor toward <a href='/it-support-broadbeach-gold-coast'>Broadbeach</a>"])}

    {trust_note("Corporate tenants in Robina send supplier security questionnaires more often than anywhere else on the coast. Most of what they ask is already published on <a href='/trust-centre'>our trust centre</a> and <a href='/service-levels-and-security'>service levels</a> — and if something is missing, we will put it in writing.")}
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Typical jobs</span>
      <h2>What Robina businesses actually call us about</h2>
    </div>
    {ticks(['<strong>Supplier security questionnaires</strong> from a client or a government buyer, needing documented answers rather than assurances', '<strong>ASIC cyber resilience evidence</strong> for AFS licensees — gap assessment, remediation and an evidence pack that can actually be produced', '<strong>Networks outgrown by the business</strong>, specified when the firm was a third of its current size', '<strong>Microsoft 365 tenancy reviews</strong> — MFA coverage, legacy authentication, sharing settings and licensing nobody is using', '<strong>Hybrid working setups</strong> where security has to travel with the device rather than live in the office', "<strong>Backups with tested restores</strong>, which is the question an insurer's renewal form now asks directly", '<strong>Office fit-outs</strong> in the business park space — predictable, well-built, and quoted accordingly', '<strong>Practice and document management environments</strong>, working alongside the software vendor'])}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What IT support in Robina actually involves</h2>
      <p>A representative engagement, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {LOCAL_EX}
  </div>
</section>
'''
            + f'''
{booking_cta()}
'''
            + faq_block(FAQS)
            + nearby('/it-support-robina-gold-coast')
            + related([('Business IT Support', '/it-support-and-services-gold-coast'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'), ('Business WiFi Installation', '/business-wifi-gold-coast'), ('Cybersecurity Services', '/cybersecurity-services-gold-coast'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('Pricing', '/pricing'), ('ASIC Cybersecurity Compliance', '/asic-cybersecurity-compliance-gold-coast')])
            + cta('Answering a supplier security questionnaire?', "Most of what they ask is already published on our trust centre — and if something's missing, we'll write it."),
}

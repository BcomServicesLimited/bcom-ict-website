from layout import MARK, cta, faq_block, cards, ticks, related, nearby, trust_note, example, booking_cta

LOCAL_EX = example(
    "A Southport practice that could not say who opened a file",
    "A professional practice in the Southport legal and medical precinct was asked by a client to describe how it controls access to confidential files. It could not answer with any confidence.",
    "Four staff shared a single login on the reception machine, which also held saved credentials to the practice&rsquo;s document system. The audit trail existed and recorded every action against the same shared account, so it was complete and useless. The practice had assumed shared access was a reasonable arrangement for a small team.",
    "Created named accounts for every person with multi-factor authentication, removed saved credentials from the shared machine, and set out a short written position on access that the practice could give to a client who asks.",
    "The practice can now answer the question it was asked. Southport&rsquo;s concentration of legal, medical and accounting practices means client-driven security questions arrive here earlier than in most parts of the coast.")
FAQS = [   (   'Do you provide IT support in Southport?',
        'Yes. bcom ICT attends Southport businesses from its office at 9 Ferny Avenue, Surfers Paradise — roughly ten minutes away — with same-day attendance almost always available. We cover the '
        'courts precinct, Nerang and Scarborough Streets, Australia Fair, Chinatown, the health precinct around the Gold Coast University Hospital, and the Broadwater frontage. Call 07 3041 8993.'),
    (   "Do you work with law firms and barristers' chambers?",
        'Yes — the courts precinct means Southport has one of the densest concentrations of legal practices on the coast. Professional confidentiality obligations change how the IT has to be set up: '
        'file access structured by role rather than open to everyone, managed devices for anything leaving the office, secure remote access rather than something published to the internet, and '
        'backups with tested restores.'),
    (   'Do you work with medical practices in Southport?',
        "Yes, and there are a great many through the health precinct. Health service providers are covered by the Privacy Act regardless of annual turnover, which changes what a practice's IT has to "
        'do around patient records and notifiable data breaches. Our attending technicians hold national police checks and Queensland Blue Cards where required.'),
    (   'Can you work in the older Southport office towers?',
        'Frequently. The building stock varies enormously — modern towers alongside 1980s blocks that have been refitted several times, often with cabling from four decades layered together and none '
        'of it labelled. We test what is actually there rather than assuming, and arrange building management approval and service lift access in advance where the work needs it.'),
    (   'How quickly can you attend in Southport?',
        'Same-day attendance is almost always available, and many faults are resolved remotely within minutes of your call. Managed IT clients have a contracted 4-hour response on critical faults '
        'with after-hours attendance included under their agreement.'),
    (   "Can you answer a client's supplier security questionnaire for us?",
        "Most of it, yes — and Southport's government-adjacent and professional clients send them more often than most. Our published service levels and trust centre set out response targets, "
        'framework alignment, credentials, insurance and data handling, so the majority of questions can be answered directly from documents that already exist.')]

PAGE = {
    "path": '/it-support-southport-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Southport — Legal, Medical & Professional | bcom ICT',
    "description": 'IT support for Southport businesses — the courts precinct, Australia Fair, Chinatown, the health precinct and the Broadwater. Same-day attendance, roughly ten minutes from our office.',
    "hero_img": 'hero-bg-it-support.webp',
    "hero_alt": 'A Southport professional office supported by bcom ICT in the Gold Coast CBD',
    "h1": 'IT support in the Gold Coast CBD',
    "lede": 'Southport carries the legal, medical and civic weight of the Gold Coast — and the confidentiality and compliance obligations that come with it.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~10 min from our office', 'Legal & medical experience', 'Police-checked techs', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Southport', '/it-support-southport-gold-coast')],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides IT support to businesses across Southport, the Gold Coast's commercial and civic centre, roughly ten minutes from our Surfers Paradise office. Southport carries a dense concentration of legal, medical and professional practices with specific confidentiality and compliance obligations. Same-day attendance is usually available. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Local landscape</span>
      <h2>What Southport is actually like to work in</h2>
    </div>
    <p style="margin-top:16px">Southport is the closest thing the Gold Coast has to a traditional
    CBD, and it behaves like one. The Southport Courthouse — Magistrates, District and Supreme — anchors a
    genuine legal precinct, with barristers' chambers and law firms clustered through Nerang Street, Scarborough
    Street and the surrounding blocks. Where there are courts there are also the accountants, forensic
    specialists, mediators and consultants that orbit them.</p>
    <p style="margin-top:16px">A short distance north, the <strong>health precinct</strong> around the Gold
    Coast University Hospital and the Griffith University campus produces a second concentration — specialist
    suites, allied health, diagnostic services and the medical administration businesses that support them.
    That is a very different IT problem to a law firm, and both are within ten minutes of each other.</p>
    <p style="margin-top:16px">Then there is the commercial core: <strong>Australia Fair</strong> and the
    retail through Scarborough Street, <strong>Chinatown</strong> along Young and Davenport Streets with its
    hospitality density, and the government and not-for-profit offices scattered through the older towers.
    The <strong>Broadwater Parklands</strong> and the Aquatic Centre bring events and the operators that
    service them.</p>
    <p style="margin-top:16px">The building stock is the most varied on the coast. Southport has purpose-built
    modern towers, 1980s office blocks that have been through three fit-outs, and converted premises that
    started life as something else entirely. What is actually in the walls varies enormously from one address
    to the next, and it is worth establishing before planning anything.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who we work with here</span>
      <h2>The businesses we see most in Southport</h2>
      <p>The courts and the hospital shape the commercial mix here more than anything else.</p>
    </div>
    <div class="grid grid--2">{cards([('Legal practices and chambers', None, 'Through Nerang Street, Scarborough Street and the blocks around the courthouse. Client confidentiality is a professional obligation rather than good practice, which changes how document access, managed devices and remote access all need to be set up. Matter files that cannot be produced are a professional problem, not just a technical one.'), ('Medical and allied health', None, 'Specialist suites and practices through the health precinct and along the Southport spine. Health service providers carry Privacy Act obligations regardless of turnover — the small business exemption does not apply to them — and our attending technicians hold police checks and Blue Cards where required.'), ('Accounting and financial services', None, 'Including AFS licensees whose cyber resilience obligations sit inside their licence conditions rather than alongside them. Concentrated client identity and financial information, and increasingly hard questions at insurance renewal.'), ('Government-adjacent and not-for-profit', None, 'Offices through the older Southport towers, frequently with supplier security questionnaires to answer and procurement processes that want documented evidence rather than assurances.'), ('Retail and hospitality', None, 'Australia Fair, the Scarborough Street strip and the Chinatown precinct. Point of sale uptime, payment terminal segmentation and automatic internet failover so an outage does not stop trading.'), ('Events and venue operators', None, 'Around Broadwater Parklands and the Aquatic Centre — temporary connectivity, guest WiFi at capacity, and systems that get judged on the one day they are under load.')], icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What's technically different about Southport</h2>
    <p style="margin-top:16px"><strong>The building stock is the real variable.</strong> Southport
    ranges from modern towers with proper comms rooms to 1980s blocks that have been refitted repeatedly, with
    cabling from four different decades layered on top of each other. We have opened ceilings in Southport and
    found Cat3, Cat5, Cat5e and Cat6 in the same tray, none of it labelled. Assume nothing about what is in the
    walls until it is tested — that assumption is where budgets go wrong.</p>
    <p style="margin-top:16px"><strong>High-rise access needs planning.</strong> Several of the commercial
    towers require building management approval, a booked service lift and often an after-hours window for
    anything involving cabling or equipment being moved. We arrange that in advance rather than discovering it
    on the day, the same way we do in <a href="/it-support-surfers-paradise-gold-coast">Surfers Paradise</a>.</p>
    <p style="margin-top:16px"><strong>Confidentiality changes the design.</strong> In a legal or medical
    practice, file access structured by role rather than open to everyone stops being a nice-to-have. So does
    managed device control on anything that leaves the office, and secure remote access rather than something
    published to the internet. These are the specific requirements that make a Southport fit-out different to
    a general office.</p>
    <p style="margin-top:16px"><strong>Parking genuinely affects response time.</strong> Unglamorous, but it
    is the difference between a technician reaching your desk in five minutes or twenty. We know where to park
    around the courts precinct and Australia Fair, which sounds trivial until you have waited for someone who
    did not.</p>

    <div class="rule">{MARK}</div>

    <h2>Getting to you</h2>
    <p style="margin-top:16px">Southport is roughly ten minutes from our office at 9 Ferny Avenue,
    Surfers Paradise — straight up the Gold Coast Highway or via the light rail corridor. It is one of the
    quickest suburbs on the coast for us to reach, and same-day attendance is almost always available.</p>
    <p style="margin-top:16px">We still try remote first where the fault allows it, because remote support is
    $190 + GST per hour with no call-out against $290 + GST for a first hour on site. Most email, Microsoft 365,
    software and account faults never need anyone to travel.</p>
    <p style="margin-top:16px">Managed IT clients have a contracted 4-hour response on critical faults, with
    after-hours attendance included under their agreement.</p>

    <h2 style="margin-top:48px">Streets and precincts we regularly attend</h2>
    <p style="margin-top:16px">We regularly attend businesses across Southport and the surrounding precincts, including:</p>
    {ticks(['Nerang Street, Scarborough Street and Nind Street — the commercial and legal core', 'The Southport Courthouse precinct and surrounding chambers', 'Australia Fair and the surrounding retail', 'Young Street, Davenport Street and the Chinatown precinct', 'The Gold Coast University Hospital and Griffith University health precinct', 'Marine Parade and the Broadwater Parklands frontage', "Ferry Road, Bundall Road and the commercial stretch toward <a href='/it-support-broadbeach-gold-coast'>Broadbeach</a>", 'Labrador, Biggera Waters and Ashmore, where our Southport coverage extends'])}

    {trust_note("Technicians attending medical, dental and allied health sites hold national police checks, and Queensland Blue Cards where a practice requires them. Professional indemnity, cyber liability and public liability insurance are held — certificates of currency on request. See <a href='/trust-centre'>the trust centre</a>.")}
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Typical jobs</span>
      <h2>What Southport businesses actually call us about</h2>
    </div>
    {ticks(['<strong>Document and matter file access</strong> structured by role rather than open to the whole practice — the most common request from legal clients', '<strong>Practice management and clinical software</strong> environments — server, backup, access and connectivity, working alongside the vendor', '<strong>Supplier security questionnaires</strong> that a client or a government buyer has sent, which our published service levels and trust centre answer directly', '<strong>Cabling in older towers</strong> where nobody knows what is behind the walls, tested and documented before anything is planned around it', '<strong>Multi-factor authentication rollouts</strong>, usually triggered by a professional indemnity renewal or an ASIC obligation', '<strong>Secure remote access</strong> replacing remote desktop published straight to the internet — one of the most exploited routes into an Australian practice', '<strong>Backups with tested restores</strong>, because a practice that cannot produce a client file has a professional problem as well as a technical one', '<strong>Office relocations</strong> within the Southport commercial core, staged over a weekend with everything tested before Monday'])}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What IT support in Southport actually involves</h2>
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
            + nearby('/it-support-southport-gold-coast')
            + related([('Business IT Support', '/it-support-and-services-gold-coast'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'), ('Business WiFi Installation', '/business-wifi-gold-coast'), ('Cybersecurity Services', '/cybersecurity-services-gold-coast'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('Pricing', '/pricing'), ('Professional services', '/it-support-professional-services-gold-coast')])
            + cta('Ten minutes up the road', 'Call 07 3041 8993 — Southport attendance is usually same-day, and often a lot sooner than that.'),
}

from layout import MARK, cta, faq_block, cards, ticks, related, nearby, trust_note, example, booking_cta

LOCAL_EX = example(
    "A Palm Beach practice on a connection with nothing behind it",
    "A small practice on the Palm Beach strip had moved its booking system, files and phones into the cloud over several years. A single internet service carried all of it, which nobody had thought about in those terms.",
    "Reviewing the setup before anything went wrong, an outage of any length would stop every function of the business at once &mdash; including the phone customers would use to ask what was happening. The premises were on a fibre-to-the-node service with copper for the final stretch, which in this part of the coast is the section most affected by weather.",
    "Installed a router with automatic mobile failover, tested it by disconnecting the primary service during a quiet period, and confirmed calls stayed connected through the switchover.",
    "A street fault some months later cost the practice a slower afternoon rather than a closed day. The equipment cost considerably less than the day would have.")
FAQS = [   (   'Do you provide IT support in Palm Beach?',
        'Yes. bcom ICT attends Palm Beach businesses from its Surfers Paradise office, roughly twenty-five minutes away, with same-day attendance usually available. We cover the Gold Coast Highway '
        'strip, Nineteenth Avenue, the streets off the highway, and out through Elanora and Currumbin. Most faults are resolved remotely at $190 + GST per hour with no call-out. Call 07 3041 8993.'),
    (   'Is it worth calling you for a small job?',
        'Often the answer is remote support, which carries no call-out and frequently resolves the problem inside an hour. We will tell you on the phone whether it needs a visit before booking one — '
        'at this distance the call-out is a real proportion of a small job and we would rather not add it unnecessarily.'),
    (   "We're only a few people. Do we need managed IT?",
        'Probably not, and we say that to more Palm Beach businesses than anywhere else. With a handful of laptops, everything in the cloud and no compliance obligations, a monthly fee buys very '
        'little. Two things are worth doing regardless: multi-factor authentication on every mailbox, and a backup you have actually watched restore.'),
    (   "Our WiFi doesn't cover the whole shop. Can that be fixed?",
        'Usually, and often for less than people expect. Most Palm Beach premises were converted from something else, so coverage has to fight original construction and added partitions. It '
        'typically needs one properly placed access point and a cable run rather than a whole new system — we measure before quoting.'),
    (   'What happens to our card payments if the internet drops?',
        "Without failover, you stop taking card. With an automatic 4G or 5G backup connection, payments continue and the changeover needs nobody's attention. For a food or retail business on the "
        'strip it usually pays for itself the first time it is needed.'),
    (   'Do you do home office WiFi in Palm Beach?',
        'Yes — mesh WiFi and home office network setup through Palm Beach, Elanora and Currumbin Waters. General home computer repair is not something we take on.')]

PAGE = {
    "path": '/it-support-palm-beach-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Palm Beach — Small Business | bcom ICT',
    "description": "IT support for Palm Beach businesses — the Gold Coast Highway strip, Nineteenth Avenue, cafes, retail.",
    "hero_img": 'hero-bg-consulting.webp',
    "hero_alt": 'A Palm Beach small business supported by bcom ICT',
    "h1": 'IT support for Palm Beach businesses',
    "lede": 'A strip that has changed a great deal in a few years — and a lot of premises whose infrastructure has not changed with it.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Southern beaches', 'Small independents', 'Remote-first where we can', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Palm Beach', '/it-support-palm-beach-gold-coast')],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides IT support to businesses in Palm Beach — cafes and food operators, retail, creative studios and small professional practices along the Gold Coast Highway and the surrounding streets. Same-day attendance is usually available, and most faults are resolved remotely without a visit. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Local landscape</span>
      <h2>What Palm Beach is actually like to work in</h2>
    </div>
    <p style="margin-top:16px">Palm Beach has changed faster than almost anywhere on the southern
    Gold Coast. The strip along the <strong>Gold Coast Highway</strong> and through
    <strong>Nineteenth Avenue</strong> has filled with independent cafes, restaurants, retail and studios that
    were not there a decade ago — occupying commercial premises that mostly were.</p>
    <p style="margin-top:16px">That gap is the recurring theme. The buildings are older, frequently repurposed
    more than once, and their services reflect whatever the previous tenant needed rather than what a modern
    business does. Cabling is improvised or absent. There is rarely anywhere sensible to put equipment.
    Wireless has to cover through original construction that predates anyone thinking about signal.</p>
    <p style="margin-top:16px">The business mix is overwhelmingly small — two to ten people is typical, with a
    lot of owner-operators. <strong>Hospitality and food</strong> along the highway and toward the
    <strong>Palm Beach Parklands</strong> and Tallebudgera Creek. <strong>Retail</strong> through the strip.
    <strong>Creative studios, agencies and consultants</strong> drawn by the location and the rents.
    And a growing layer of small professional and wellness practices.</p>
    <p style="margin-top:16px">Very few of these businesses have any internal IT, and many have no provider at
    all until something breaks in a way they cannot work around.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who we work with here</span>
      <h2>The businesses we see most in Palm Beach</h2>
      <p>Small teams, owner-operators, and premises that were converted rather than built for the purpose.</p>
    </div>
    <div class="grid grid--2">{cards([('Cafes, restaurants and food operators', None, 'Along the highway and toward the Parklands. Card payments are the priority — automatic 4G or 5G failover so an internet outage does not stop the till is the single most valuable thing most of these businesses can do.'), ('Retail and boutique operators', None, 'Through the strip and Nineteenth Avenue. Point of sale, stock systems and a network that has to be reliable on a Saturday morning.'), ('Creative studios and consultants', None, 'Design, media, photography and advisory. Small teams working across laptops and cloud tools, frequently holding client material that would be genuinely painful to lose.'), ('Small professional and wellness practices', None, 'Allied health, treatment studios, small advisory firms. Client confidentiality obligations in premises never designed with that in mind.'), ('Trades and service businesses', None, 'Based in Palm Beach and Elanora but working across the southern coast. Job management software that works offline, and phones that follow people.'), ('Home offices in the surrounding streets', None, 'Through Palm Beach, Elanora and Currumbin Waters. WiFi and mesh for home offices — not general home computer repair.')], icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What's technically different about Palm Beach</h2>
    <p style="margin-top:16px"><strong>Premises predate the businesses in them.</strong> Most
    commercial space along the strip has been repurposed at least once. Cabling is frequently improvised, run
    where it could be rather than where it should be, and equipment ends up wherever there was a spare power
    point. What is actually installed varies enormously between neighbouring shopfronts, so we survey rather
    than assume.</p>
    <p style="margin-top:16px"><strong>Remote support matters more here than anywhere.</strong> At
    twenty-five minutes out, a $100 + GST call-out is a real proportion of a small job — sometimes most of it.
    That is why we genuinely try remote first rather than saying we do: remote is $190 + GST per hour with no
    call-out, and most email, Microsoft 365, software, account and printer faults never need anyone to travel.
    We will tell you on the phone which yours is likely to be.</p>
    <p style="margin-top:16px"><strong>Most Palm Beach businesses do not need managed IT.</strong> We say that
    to more clients here than in any other suburb. With a handful of laptops, everything in the cloud, no
    server and no compliance obligations, a monthly fee buys very little. Ad-hoc support at an hourly rate is
    usually the honest recommendation — and we would rather lose the recurring revenue than sell something
    that is not warranted.</p>
    <p style="margin-top:16px"><strong>Two things are worth doing regardless of size.</strong> Multi-factor
    authentication on every mailbox, and a backup you have actually watched restore. Between them they prevent
    most of what genuinely damages a small business, and neither costs much.</p>

    <div class="rule">{MARK}</div>

    <h2>Getting to you</h2>
    <p style="margin-top:16px">Palm Beach is about twenty-five minutes south of the centre of our coverage
    Avenue, Surfers Paradise, down the highway or the M1. Same-day attendance is usually available.</p>
    <p style="margin-top:16px">Given the distance and the size of most jobs here, we resolve what we can
    remotely and book a visit only when the fault genuinely needs someone on site — dead hardware, a failed
    drive, cabling, or a network that is properly down.</p>
    <p style="margin-top:16px">Managed clients have a contracted 4-hour response on critical faults regardless
    of where they are on the coast.</p>

    <h2 style="margin-top:48px">Streets and precincts we regularly attend</h2>
    <p style="margin-top:16px">We attend businesses throughout Palm Beach and the surrounding southern suburbs, including:</p>
    {ticks(['Gold Coast Highway through Palm Beach and the commercial frontage', 'Nineteenth Avenue and Palm Beach Avenue', 'Sixth Avenue, Eleventh Avenue and the streets off the highway strip', 'The Palm Beach Parklands and Tallebudgera Creek frontage', 'Elanora and The Pines shopping precinct', 'Currumbin, Currumbin Waters and Currumbin Valley', 'Tugun, Bilinga and the corridor toward Coolangatta', "Burleigh Waters and toward <a href='/it-support-burleigh-heads-gold-coast'>Burleigh Heads</a>"])}

    {trust_note('We tell more Palm Beach businesses that they do not need managed IT than anywhere else on the coast. Ad-hoc support at $190 + GST per hour suits most operations this size, and we would rather say so than sell a monthly fee that is not warranted.')}
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Typical jobs</span>
      <h2>What Palm Beach businesses actually call us about</h2>
    </div>
    {ticks(['<strong>Card payments failing during trade</strong>, and the automatic failover connection that prevents it', '<strong>WiFi that will not cover the whole shopfront</strong>, usually solvable with one properly placed access point', '<strong>Microsoft 365 setup and clean-up</strong> for small teams that grew without anyone owning it', '<strong>Multi-factor authentication rollouts</strong> after a near-miss with an invoice email', '<strong>Backups for studios and practices</strong> holding client work or records that would hurt to lose', '<strong>A machine that will not start</strong> and someone who cannot work until it does', '<strong>Cabling in converted premises</strong>, done properly rather than run along the skirting', '<strong>Booking and payment system connectivity</strong> for treatment and wellness studios'])}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What IT support in Palm Beach actually involves</h2>
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
            + nearby('/it-support-palm-beach-gold-coast')
            + related([('Business IT Support', '/it-support-and-services-gold-coast'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'), ('Business WiFi Installation', '/business-wifi-gold-coast'), ('Cybersecurity Services', '/cybersecurity-services-gold-coast'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('Pricing', '/pricing'), ('Remote IT Support', '/remote-it-support-gold-coast')])
            + cta('Try remote first', "Call 07 3041 8993 — no call-out on remote support, and most problems don't need anyone on site."),
}

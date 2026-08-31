from layout import MARK, cta, faq_block, cards, ticks, related, nearby, trust_note, example

LOCAL_EX = example(
    "A Burleigh Heads shopfront with payments on the guest network",
    "A business operating from a converted shopfront near James Street had card terminals dropping out during busy trade. It had been happening for months and was assumed to be the terminal provider&rsquo;s problem.",
    "Everything in the premises ran through one consumer router mounted behind the counter &mdash; the terminals, the customer WiFi, the music, and a tablet used for orders. Customer devices and payments were competing for the same capacity, and the busy period was exactly when both peaked. The building&rsquo;s rendered walls also meant the single access point struggled to reach the rear of the tenancy.",
    "Separated payments onto their own segment, put customer WiFi somewhere it cannot affect trading systems, and added coverage that reaches the back of the premises.",
    "Terminal dropouts stopped. Burleigh&rsquo;s converted shopfronts and older buildings are frequently wired for a much smaller operation than the business now running in them.")
FAQS = [   (   'Do you provide IT support in Burleigh Heads?',
        'Yes. bcom ICT attends Burleigh Heads businesses from its Surfers Paradise office, roughly twenty minutes away, with same-day attendance usually available. We cover James Street, the Gold '
        'Coast Highway frontage, The Pines, and the streets behind the main strip. Most faults are resolved remotely first at $198 + GST per hour with no call-out. Call 07 3041 8993.'),
    (   "We're a small cafe. Do we really need an IT provider?",
        'Not necessarily on a monthly arrangement, and we will say so. But two things are worth doing regardless: automatic 4G or 5G failover so card payments continue through an internet outage, '
        'and multi-factor authentication on your email. Both are inexpensive and both prevent expensive days.'),
    (   "Our WiFi won't reach the outdoor seating. Can that be fixed?",
        'Usually, and it is a smaller job than people expect. A single consumer router covering a James Street venue and its terrace is not realistic — original brick, added partitions and outdoor '
        'areas all fight coverage. It typically needs a second properly placed access point and a cable run, which we can quote after measuring rather than guessing.'),
    (   'Do you work with businesses in older Burleigh buildings?',
        'Frequently — most commercial space here started as something else. Converted premises usually have improvised cabling and awkward equipment placement, and what is actually in the walls '
        'varies enormously from one shopfront to the next. We survey rather than assume, because that determines what is possible.'),
    (   'Are we too small to be a target for cyber attacks?',
        'No, and being small is not protective. Almost everything that happens to small businesses is automated and indiscriminate — it finds whoever is reachable, and smaller operations are '
        'reachable precisely because the basics are missing. The invoice scam that redirects a payment does not care how many staff you have.'),
    (   'Do you do home office setups in Burleigh?',
        'WiFi and mesh network installation for home offices, yes — including through Burleigh Waters and Miami. General home computer repair is not something we take on.')]

PAGE = {
    "path": '/it-support-burleigh-heads-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Burleigh Heads — Business & Hospitality | bcom ICT',
    "description": 'IT support for Burleigh Heads businesses — the James Street precinct, the Gold Coast Highway strip, creative studios and boutique practices in converted premises.',
    "hero_img": 'hero-bg-consulting.webp',
    "hero_alt": 'A Burleigh Heads business supported by bcom ICT',
    "h1": "IT support for Burleigh's independent operators",
    "lede": 'James Street, the highway strip and the converted premises behind them — small businesses in buildings that were never designed for what they now hold.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~20 min from our office', 'Small independents', 'Older shopfronts', 'Remote-first where we can'],
    "crumbs": [("Industries", "/industries"), ('Burleigh Heads', '/it-support-burleigh-heads-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides IT support to businesses in Burleigh Heads — cafes and restaurants, creative studios, boutique agencies and the professional practices increasingly occupying converted premises around James Street and the Gold Coast Highway. Attendance is roughly twenty minutes from our Surfers Paradise office, with most faults resolved remotely first. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Local landscape</span>
      <h2>What Burleigh Heads is actually like to work in</h2>
    </div>
    <p style="margin-top:16px">Burleigh has changed considerably in a decade and its commercial
    property has not entirely kept up. <strong>James Street</strong> is now one of the busiest dining and
    retail strips on the coast, and the premises along it were mostly built for something else — a shop, a
    house, a workshop — before being converted, sometimes more than once.</p>
    <p style="margin-top:16px">That produces a specific set of problems. Cabling is frequently improvised.
    Comms equipment ends up in a cupboard behind the coffee machine because there is nowhere else for it.
    Wireless has to cover through walls nobody planned around, including the original brick of a building that
    predates anyone thinking about signal.</p>
    <p style="margin-top:16px">The business mix is genuinely varied for a suburb this size.
    <strong>Hospitality</strong> along James Street and the highway, where a point of sale failure at service
    is the whole problem. <strong>Creative studios and agencies</strong> — design, media, marketing —
    typically small teams working across laptops and cloud tools. A growing layer of <strong>boutique
    professional practices</strong>: health and wellness, allied health, small legal and accounting firms
    attracted by the location. And retail through The Pines and the highway frontage.</p>
    <p style="margin-top:16px">Almost all of it is small — two to fifteen people, no internal IT, and often no
    provider at all until something breaks badly enough to force the issue.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who we work with here</span>
      <h2>The businesses we see most in Burleigh Heads</h2>
      <p>Small teams, mostly, in premises that were converted rather than purpose-built.</p>
    </div>
    <div class="grid grid--2">{cards([('Cafes, restaurants and bars', None, 'Along James Street, the highway and toward the beach. POS and EFTPOS uptime through service, WiFi covering outdoor and terrace seating, and automatic 4G or 5G failover so card payments continue through an outage.'), ('Creative studios and agencies', None, 'Design, media, marketing and production. Small teams, cloud-first, working across laptops — and frequently holding client material worth more than they realise.'), ('Boutique professional practices', None, 'Health and wellness, allied health, small legal and accounting firms in converted premises. Client confidentiality obligations in buildings that were never designed for a server, let alone a comms room.'), ('Retail', None, 'The Pines, the highway frontage and the James Street shops. Payments, stock systems, and a network that has to work on a Saturday.'), ('Home offices in the surrounding streets', None, 'Burleigh Waters, Miami and the hinterland side. We install WiFi and mesh for home offices — though general home computer repair is not something we take on.'), ('Wellness and studio operators', None, 'Yoga, pilates, physiotherapy and treatment studios. Booking systems, payments and guest WiFi in premises with awkward layouts and limited cabling.')], icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What's technically different about Burleigh Heads</h2>
    <p style="margin-top:16px"><strong>Converted premises are the defining constraint.</strong> Most
    commercial space here started as something else. There is rarely a proper comms room, cabling is often
    improvised or absent, and equipment ends up wherever there was a power point. We survey rather than
    assume, because what is actually in the walls determines what is possible and it varies enormously from
    one shopfront to the next.</p>
    <p style="margin-top:16px"><strong>Wireless has to work harder here.</strong> Original brick, added
    partitions, mezzanines and outdoor seating areas all fight coverage. A single consumer router covering a
    James Street venue including its terrace is not a realistic proposition, and no amount of turning it up
    changes that. It usually needs two properly placed access points and a cable run — which is a smaller job
    than people expect once someone has measured it.</p>
    <p style="margin-top:16px"><strong>Being small is not protective.</strong> A recurring conversation here.
    Almost everything that happens to small businesses is automated and indiscriminate — it finds whoever is
    reachable, and smaller operations are reachable precisely because the basics are missing. The invoice
    scam that redirects a payment does not care how many staff you have.</p>
    <p style="margin-top:16px"><strong>Remote support matters more at this distance.</strong> At twenty
    minutes out, the call-out is a meaningful proportion of a small job. We try remote first — no call-out on
    it — and book a visit only when the fault genuinely needs hands on hardware.</p>

    <div class="rule">{MARK}</div>

    <h2>Getting to you</h2>
    <p style="margin-top:16px">Burleigh Heads is roughly twenty minutes from our office at 9 Ferny
    Avenue, Surfers Paradise, down the highway or the M1. Same-day attendance is usually available.</p>
    <p style="margin-top:16px">Because most Burleigh jobs are small, we try remote first wherever the fault
    allows — remote support is $198 + GST per hour with no call-out, against $298 + GST for a first hour on
    site. For a two-person studio that difference is worth having, and we will tell you on the phone which it
    is likely to be.</p>
    <p style="margin-top:16px">Parking around James Street is genuinely difficult at peak, which we plan
    around rather than pretend does not exist.</p>

    <h2 style="margin-top:48px">Streets and precincts we regularly attend</h2>
    <p style="margin-top:16px">We attend businesses throughout Burleigh Heads and immediately around it, including:</p>
    {ticks(['James Street and the surrounding dining and retail precinct', 'Gold Coast Highway through Burleigh and the commercial frontage', 'The Pines shopping centre and surrounding retail at Elanora', 'Connor Street, Park Avenue and the streets behind the James Street strip', 'Burleigh Waters and the commercial pockets inland', "Miami and the corridor toward <a href='/it-support-broadbeach-gold-coast'>Broadbeach</a>", 'West Burleigh and the light industrial pockets toward the highway', "Palm Beach and Elanora, where our <a href='/it-support-palm-beach-gold-coast'>Palm Beach</a> coverage overlaps"])}

    {trust_note('Two things are worth doing regardless of business size, and neither is expensive: multi-factor authentication on every mailbox, and a backup you have actually watched restore. Between them they prevent most of what genuinely damages a small business.')}
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Typical jobs</span>
      <h2>What Burleigh businesses actually call us about</h2>
    </div>
    {ticks(['<strong>WiFi that will not reach the terrace</strong> — usually solvable with one properly placed access point and a cable run', '<strong>EFTPOS dropping out during service</strong>, almost always saturated wireless rather than the terminal', '<strong>Automatic internet failover</strong> so card payments continue through an outage — cheap, and the highest-value thing a venue here can do', '<strong>Invoice redirection attempts</strong>, and the multi-factor authentication rollout that stops nearly all of them', '<strong>Cabling in converted premises</strong>, surveyed and installed properly rather than run along a skirting board', '<strong>Microsoft 365 setup and clean-up</strong> for small teams that grew organically without anyone owning it', '<strong>Backups for creative studios</strong> holding client work that would be genuinely painful to lose', '<strong>Booking and payment system connectivity</strong> for wellness and treatment studios'])}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What IT support in Burleigh Heads actually involves</h2>
      <p>A representative engagement, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {LOCAL_EX}
  </div>
</section>
'''
            + faq_block(FAQS)
            + nearby('/it-support-burleigh-heads-gold-coast')
            + related([('Business IT Support', '/it-support-and-services-gold-coast'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'), ('Business WiFi Installation', '/business-wifi-gold-coast'), ('Cybersecurity Services', '/cybersecurity-services-gold-coast'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('Pricing', '/pricing'), ('Restaurants & cafes', '/it-support-restaurants-gold-coast')])
            + cta('Small business, small budget?', "Tell us what's actually causing problems. The fix is often cheaper than you'd expect, and sometimes you don't need us monthly at all."),
}

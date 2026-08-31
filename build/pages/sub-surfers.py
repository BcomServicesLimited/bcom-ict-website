from layout import MARK, cta, faq_block, cards, ticks, related, nearby, trust_note, example

LOCAL_EX = example(
    "Getting a technician into a Surfers Paradise tower",
    "A business occupying part of a floor in a Surfers Paradise high-rise had a server that would not come back after a building power interruption. Their previous provider had quoted a next-day visit because of the access arrangements.",
    "The delay was not technical. Reaching the tenancy required building management sign-in, a lift access card programmed for that floor, and a loading dock booking for anything larger than a laptop bag. The previous provider had no standing arrangement and was starting that process from scratch each time.",
    "Attended the same afternoon, having already held the building&rsquo;s contractor induction from other work in the tower, and restored the server from backup. Afterwards, we recorded the building&rsquo;s access requirements against the client so no future visit has to rediscover them.",
    "Back trading that day rather than the next. In Surfers Paradise the access arrangements are frequently a larger part of the response time than the fault, which is why we keep the induction and dock details on file.")
FAQS = [   (   'Do you provide IT support in Surfers Paradise?',
        "Yes — bcom ICT's office is at 9 Ferny Avenue, Surfers Paradise, so this is our home suburb. Attendance within Surfers Paradise is usually available within the hour during business hours, "
        'which are 8:00am to 5:00pm Monday to Friday, Brisbane time. Call 07 3041 8993.'),
    (   'How quickly can you get to a Surfers Paradise business?',
        'Usually within the hour during business hours, since we are based in the suburb. Building access in the towers occasionally adds time — service lift bookings and building management '
        'approvals — which we arrange in advance where the work requires it rather than turning up and being turned away.'),
    (   'Do you work with hotels and accommodation operators here?',
        'Yes, and it is a substantial part of what we do in Surfers. Guest WiFi across whole properties, property management system connectivity, payment terminal segmentation across outlets, '
        'function space connectivity and account management for seasonal staff. Guests review the WiFi, which makes coverage a commercial decision rather than a technical one.'),
    (   'Our guest WiFi works in the lobby but not the rooms. Why?',
        'Almost always coverage design rather than the internet service. Concrete floors, tiled bathrooms, lift shafts and long corridors block signal, and equipment placed on a guess will not '
        'reach. It needs a survey and properly positioned access points — adding range extenders generally makes roaming worse rather than better.'),
    (   'Can you work in the older Esplanade and Ferny Avenue towers?',
        'Regularly. Many were built before anyone was running PoE access points, cameras or IP phones, so riser space is tight and existing cabling is often the wrong category or length. We test '
        'what is actually installed rather than trusting a floor plan, and arrange building access in advance.'),
    (   'What does IT support cost in Surfers Paradise?',
        '$198 + GST per hour ($217.80 inc GST) plus a $100 + GST call-out ($110 inc GST) for on-site attendance. Remote support carries no call-out. Managed IT is a flat monthly fee calculated from '
        'your requirements and the services included, quoted after a free review.')]

PAGE = {
    "path": '/it-support-surfers-paradise-gold-coast',
    "priority": "0.7",
    "title": "IT Support Surfers Paradise — We're Based Here | bcom ICT",
    "description": 'IT support for Surfers Paradise businesses from an office at 9 Ferny Avenue. High-rise access, accommodation and venue systems, guest WiFi and seasonal staff turnover.',
    "hero_img": 'hero-bg.webp',
    "hero_alt": 'A Surfers Paradise office supported by bcom ICT, with the skyline visible through the window',
    "h1": "We're on Ferny Avenue",
    "lede": 'Our office is in Surfers Paradise, so this is the one suburb where local IT support means we can genuinely walk.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Office at 9 Ferny Ave', 'High-rise experience', 'Venue & accommodation', 'Usually within the hour'],
    "crumbs": [("Industries", "/industries"), ('Surfers Paradise', '/it-support-surfers-paradise-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT is based at 9 Ferny Avenue, Surfers Paradise, and supports businesses throughout the suburb — accommodation operators, venues, hospitality, retail and the professional offices in the Esplanade and Ferny Avenue towers. Attendance within Surfers Paradise is usually available within the hour during business hours. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Local landscape</span>
      <h2>What Surfers Paradise is actually like to work in</h2>
    </div>
    <p style="margin-top:16px">Almost every commercial premises in Surfers Paradise is in a tower,
    and that single fact shapes more of the IT work here than anything else. Building management approvals,
    booked service lifts, restricted after-hours access and strata rules about what can be run where all have
    to be planned around rather than discovered on the day.</p>
    <p style="margin-top:16px">The commercial mix is unlike anywhere else on the coast.
    <strong>Accommodation</strong> dominates — from the large towers along the Esplanade and Ferny Avenue
    through to short-stay and serviced apartment operators — and brings a set of problems an office simply
    does not have: guest WiFi across an entire property, property management systems that cannot go down at
    check-in, payment terminals across several outlets, and staff turnover that never stops.</p>
    <p style="margin-top:16px">Around that sits the <strong>hospitality and venue</strong> layer through
    Cavill Avenue, Orchid Avenue and the Esplanade — restaurants, bars, clubs and the retail that trades on
    foot traffic. Then the <strong>professional offices</strong> scattered through the towers: agencies,
    consultancies, property and legal practices, body corporate managers, and the businesses that service the
    accommodation industry itself.</p>
    <p style="margin-top:16px">The other defining feature is <strong>seasonality</strong>. Schoolies, summer,
    events and the convention calendar produce load spikes that a network comfortable on a Tuesday in June
    will not necessarily survive. Systems here get tested hardest at exactly the moments a failure costs
    most.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who we work with here</span>
      <h2>The businesses we see most in Surfers Paradise</h2>
      <p>Accommodation and hospitality dominate, but the towers hold a lot more than that.</p>
    </div>
    <div class="grid grid--2">{cards([('Accommodation and short-stay operators', None, 'Guest WiFi across whole properties — rooms, lobbies, pool decks and function space — plus property management system connectivity and payment segmentation. Guests review the WiFi, which makes coverage a product decision rather than an IT one. See our hospitality page.'), ('Restaurants, bars and venues', None, 'Through Cavill Avenue, Orchid Avenue and the Esplanade. Point of sale and EFTPOS uptime through service is the whole problem, and automatic 4G or 5G failover is the cheapest insurance available.'), ('Professional offices in the towers', None, 'Agencies, consultancies, property and legal practices, and body corporate managers. Standard office IT with a high-rise access problem attached to every visit.'), ('Retail and tourism operators', None, 'Card payments, stock systems and seasonal peaks. Trading hours that bear no relation to office hours, which changes when disruptive work can be scheduled.'), ('Body corporate and building management', None, "Shared infrastructure across a tower — often the point where several businesses' connectivity problems turn out to have one common cause that nobody owns."), ('Businesses servicing the accommodation industry', None, 'Cleaning, maintenance, linen, management rights operators. Mobile workforces, job management software and phones that follow people rather than sitting on a desk.')], icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What's technically different about Surfers Paradise</h2>
    <p style="margin-top:16px"><strong>High-rise access is the constant.</strong> Almost every job
    here needs building management approval, and often a booked service lift and an after-hours window for
    anything involving cabling or equipment being moved. We factor that into the schedule from the start.
    A job that would take a morning in a ground-floor office in <a href="/it-support-nerang-gold-coast">Nerang</a>
    can need two visits and a permit here.</p>
    <p style="margin-top:16px"><strong>Older towers have older cabling.</strong> Several of the commercial
    buildings along the Esplanade and Ferny Avenue were built before anyone was running Power over Ethernet
    access points, cameras or IP phones. Riser space is limited, existing runs are frequently the wrong
    category or the wrong length, and what a floor plan shows and what is actually installed are different
    documents. Worth testing before assuming a new access point will simply work.</p>
    <p style="margin-top:16px"><strong>Device density is extreme.</strong> In accommodation, every guest
    arrives with three devices. A property that would need a handful of access points for staff needs
    considerably more for guests, and the difference is not solved by turning the power up. Concrete floors,
    tiled bathrooms, lift shafts and long corridors make it a survey job rather than an estimate.</p>
    <p style="margin-top:16px"><strong>Seasonal staff turnover is a security control.</strong> Casuals
    arriving and leaving constantly, all needing system access. Creating accounts quickly is easy; removing
    them promptly is the part that matters, and in this suburb it is a genuine control rather than
    administration.</p>

    <div class="rule">{MARK}</div>

    <h2>Getting to you</h2>
    <p style="margin-top:16px">We are at 9 Ferny Avenue, in the suburb. Attendance within Surfers
    Paradise is usually available within the hour during business hours — this is the one place on the coast
    where a technician can be walking rather than driving.</p>
    <p style="margin-top:16px">Building access occasionally adds time. Where a job needs a service lift
    booking or building management approval, we arrange it in advance so the visit is not wasted.</p>
    <p style="margin-top:16px">Remote support is still often faster for email, Microsoft 365, software and
    account faults — $198 + GST per hour with no call-out — and we will say so rather than travelling for the
    sake of it.</p>

    <h2 style="margin-top:48px">Streets and precincts we regularly attend</h2>
    <p style="margin-top:16px">We attend businesses throughout Surfers Paradise and immediately around it, including:</p>
    {ticks(['Ferny Avenue and the surrounding commercial towers — where our own office is', 'The Esplanade and the beachfront accommodation strip', 'Cavill Avenue, Orchid Avenue and the Surfers Paradise dining and venue precinct', 'Surfers Paradise Boulevard and the Chevron Renaissance precinct', 'Gold Coast Highway through Surfers and the light rail corridor', "Northcliffe, Cypress Avenue and the southern end toward <a href='/it-support-broadbeach-gold-coast'>Broadbeach</a>", 'Main Beach, Tedder Avenue and the Marina Mirage precinct', 'Bundall and the commercial stretch inland along Bundall Road'])}

    {trust_note('Working in a tower usually means building management approvals and a booked service lift. We arrange those before the visit rather than discovering them at reception, and our technicians hold national police checks where a building or client requires them.')}
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Typical jobs</span>
      <h2>What Surfers Paradise businesses actually call us about</h2>
    </div>
    {ticks(['<strong>Guest WiFi that works in the lobby but fails in the rooms</strong> — the single most common accommodation complaint, and a coverage design problem rather than an internet one', '<strong>Property management system connectivity</strong> and the backups behind it, because check-in stopping is not a wait-until-Monday problem', '<strong>Payment terminal segmentation</strong> across restaurant, bar, reception and function outlets, PCI-DSS aligned', '<strong>EFTPOS dropping out at peak</strong>, which is almost always saturated wireless rather than the terminal or the connection', '<strong>Function and conference connectivity</strong> designed for the room at capacity rather than empty', '<strong>Account lifecycle for seasonal staff</strong> — created fast, and more importantly removed the day someone leaves', '<strong>Cabling in older towers</strong>, surveyed and tested before anything is planned around it', '<strong>Office moves within and between towers</strong>, staged around building access rules and tested before anyone arrives'])}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What IT support in Surfers Paradise actually involves</h2>
      <p>A representative engagement, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {LOCAL_EX}
  </div>
</section>
'''
            + faq_block(FAQS)
            + nearby('/it-support-surfers-paradise-gold-coast')
            + related([('Business IT Support', '/it-support-and-services-gold-coast'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'), ('Business WiFi Installation', '/business-wifi-gold-coast'), ('Cybersecurity Services', '/cybersecurity-services-gold-coast'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('Pricing', '/pricing'), ('Hospitality & accommodation', '/it-support-hospitality-gold-coast')])
            + cta("We're around the corner", 'Call 07 3041 8993 — in Surfers we can usually be there inside the hour.'),
}

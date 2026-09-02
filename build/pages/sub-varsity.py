from layout import MARK, cta, faq_block, cards, ticks, related, nearby, trust_note, example, booking_cta

LOCAL_EX = example(
    "A Varsity Lakes business park tenancy with nobody holding the keys",
    "A professional firm in a Varsity Lakes business park engaged us after the person who had handled their IT informally &mdash; a relative of one of the directors &mdash; became unavailable at short notice.",
    "Nothing was documented. The domain, the Microsoft tenancy, the accounting file and the firewall were all under credentials held by that one person. The business could not add a staff member, reset a password or change anything at all. Everything worked perfectly and none of it could be touched.",
    "Recovered ownership of each account through the proper verification processes, documented the whole environment, and moved credentials into a password manager the business itself controls.",
    "The firm now owns its own systems. This is the most common way a Varsity Lakes business park tenancy comes to us &mdash; not a failure, but a dependency that became visible on the day it mattered.")
FAQS = [   (   'Do you provide IT support in Varsity Lakes?',
        'Yes. bcom ICT attends Varsity Lakes businesses from its Surfers Paradise office, roughly twenty minutes away, with same-day attendance usually available. We cover the business park precinct '
        'through Varsity Parade and Lakeview Boulevard, Scottsdale Drive, the Bond University corridor and Varsity Central. Call 07 3041 8993.'),
    (   "We've grown and our IT hasn't kept up. Where do we start?",
        'That is the most common situation in Varsity Lakes. Usually a consumer-grade router doing a job it was never specified for behind a much larger business, plus backups nobody has tested and '
        'multi-factor authentication on some accounts but not others. The initial review is free and you keep the written report.'),
    (   'Can you support staff working from home?',
        'Yes, and it is standard here. The principle is that security travels with the device rather than living in the office — managed laptops with encryption and remote wipe, MFA on everything, '
        'and document access through a controlled system rather than files copied to a desktop.'),
    (   'A client is asking how we protect their information. What do we send them?',
        'A documented position rather than an assurance — what controls you operate, how access is managed, where data is held and what happens in an incident. If none of that is written down, a '
        'security health check produces most of it and is the fastest route to being able to answer.'),
    (   'Do you work with medical practices here?',
        'Yes, through the precinct and along the corridor toward the Robina hospitals. Health service providers are covered by the Privacy Act regardless of annual turnover, which changes what a '
        "practice's IT has to do. Our attending technicians hold national police checks and Queensland Blue Cards where required."),
    (   'Do you support businesses that only need occasional help?',
        'Yes. Ad-hoc support is $190 + GST per hour with no ongoing commitment, plus a $100 + GST call-out for on-site work. We will tell you honestly if a monthly managed arrangement is not worth '
        'it for you yet.')]

PAGE = {
    "path": '/it-support-varsity-lakes-gold-coast',
    "priority": "0.7",
    "title": "IT Support Varsity Lakes — Business Park | bcom ICT",
    "description": "IT support for Varsity Lakes businesses — the business park precinct, Bond University corridor, medical suites and growth-stage professional firms.",
    "hero_img": 'hero-bg-consulting.webp',
    "hero_alt": 'A Varsity Lakes business park office supported by bcom ICT',
    "h1": 'IT support for the Varsity Lakes business precinct',
    "lede": 'Modern premises, professional tenants, and a lot of firms that grew out of somewhere smaller without updating the network they brought with them.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Bond University corridor', 'Business park precinct', 'Modern infrastructure', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Varsity Lakes', '/it-support-varsity-lakes-gold-coast')],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides IT support to businesses in Varsity Lakes — professional services firms, medical and allied health practices, and technology and consulting businesses across the business park precinct and the Bond University corridor. Same-day attendance is usually available. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Local landscape</span>
      <h2>What Varsity Lakes is actually like to work in</h2>
    </div>
    <p style="margin-top:16px">Varsity Lakes is newer than most of the Gold Coast's commercial areas
    and it behaves accordingly. The business park space around Varsity Parade, Lakeview Boulevard and
    Scottsdale Drive was purpose-built, which means workable comms rooms, structured cabling already in place
    and installations that generally run to plan.</p>
    <p style="margin-top:16px"><strong>Bond University</strong> is the defining feature. Its presence produces
    a professional and consulting layer that would not otherwise exist in a suburb this size — legal,
    financial, research and advisory businesses, plus the technology and services firms that grow out of a
    university corridor. It also means a lot of hybrid and flexible working, because the people in these
    businesses expect it.</p>
    <p style="margin-top:16px">The medical presence is significant too, with suites and allied health
    practices through the precinct and along the corridor toward
    <a href="/it-support-robina-gold-coast">Robina</a> and the hospitals. Retail and food sit around Varsity
    Central and the surrounding centres, serving both the business park and the residential estates around
    Lake Orr.</p>
    <p style="margin-top:16px">The characteristic Varsity Lakes business is growth-stage: a firm that started
    with a handful of people in a smaller space and is now considerably larger in a proper office, still
    running the network and security posture it had at the beginning. Nothing has failed yet. Nothing has been
    designed either.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who we work with here</span>
      <h2>The businesses we see most in Varsity Lakes</h2>
      <p>Professional, medical and growth-stage firms make up most of what we do here.</p>
    </div>
    <div class="grid grid--2">{cards([('Professional services firms', None, 'Accounting, legal, consulting and advisory practices through the business park. Concentrated client information, hybrid working as standard, and clients increasingly asking suppliers to evidence how that information is protected.'), ('Medical and allied health', None, 'Suites through the precinct and along the corridor toward the Robina hospitals. Privacy Act obligations apply to health service providers regardless of turnover, and attending technicians hold police checks and Blue Cards where required.'), ('Technology and services businesses', None, 'Firms grown out of the university corridor. Usually cloud-first, usually hybrid, and usually needing the security to travel with the device rather than sit in the building.'), ('Growth-stage firms', None, 'The most common shape here. Headcount doubled, client base widened, and the network is still the one specified when there were five people and one room.'), ('Retail and food around Varsity Central', None, 'Point of sale and payment terminal uptime, segmented networks and automatic internet failover.'), ('Multi-site and interstate operations', None, 'Businesses running Varsity Lakes as a head office with staff or sites elsewhere — better served by one standard across all of them, centrally managed.')], icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What's technically different about Varsity Lakes</h2>
    <p style="margin-top:16px"><strong>The building stock works in your favour.</strong> Purpose-built
    business park space usually has proper provisioning already — comms rooms with power and ventilation,
    structured cabling, sensible riser access. That removes most of the awkward surprises and makes fit-out
    quotes reliable in a way they are not in older parts of the coast.</p>
    <p style="margin-top:16px"><strong>Hybrid working is the default, not the exception.</strong> That changes
    the design. Client information travels on laptops and phones, so security has to apply wherever the device
    is rather than only inside the office — managed devices with encryption and remote wipe, multi-factor
    authentication everywhere, and document access through a controlled system rather than files copied to
    somebody's desktop.</p>
    <p style="margin-top:16px"><strong>Growth outpaces infrastructure here more than anywhere.</strong> The
    single most common finding when we take on a Varsity Lakes client is a consumer-grade router doing a job
    it was never specified for, sitting behind twenty-five people and a VPN. It has not failed, which is
    precisely why nobody has looked at it.</p>
    <p style="margin-top:16px"><strong>Clients ask questions now.</strong> Professional firms here are
    increasingly being asked by their own clients how they protect information — and "we take security
    seriously" does not survive a procurement questionnaire. A documented position does, and producing one is
    a specific piece of work rather than a by-product of good IT.</p>

    <div class="rule">{MARK}</div>

    <h2>Getting to you</h2>
    <p style="margin-top:16px">Varsity Lakes is about twenty minutes from the centre of our coverage
    Avenue, Surfers Paradise, via the M1. Same-day attendance is usually available.</p>
    <p style="margin-top:16px">Most faults are resolved remotely first at $190 + GST per hour with no
    call-out, against $290 + GST for a first hour on site. Given the distance we will tell you honestly on the
    phone whether a visit is actually needed rather than booking one by default.</p>
    <p style="margin-top:16px">Parking through the business park precinct is straightforward, which keeps
    attendance time predictable.</p>

    <h2 style="margin-top:48px">Streets and precincts we regularly attend</h2>
    <p style="margin-top:16px">We attend businesses throughout Varsity Lakes and the surrounding corridor, including:</p>
    {ticks(['Varsity Parade, Lakeview Boulevard and the business park precinct', "Scottsdale Drive and the corridor toward <a href='/it-support-robina-gold-coast'>Robina</a>", 'University Drive and the Bond University precinct', 'Varsity Central and the surrounding retail and food', 'Christine Avenue and the commercial stretch through Varsity Lakes', 'Lake Orr Drive and the surrounding professional suites', 'Reedy Creek, Mudgeeraba and Burleigh Waters, where our coverage extends', "Miami and the corridor toward <a href='/it-support-burleigh-heads-gold-coast'>Burleigh Heads</a>"])}

    {trust_note("Professional firms here are increasingly asked by their own clients how they protect information. A security health check produces most of a documented answer, and our <a href='/trust-centre'>trust centre</a> shows the shape of what one looks like.")}
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Typical jobs</span>
      <h2>What Varsity Lakes businesses actually call us about</h2>
    </div>
    {ticks(['<strong>Networks outgrown by the business</strong> — a consumer router behind twenty-five people, still working, never revisited', '<strong>Hybrid working setups</strong> where the security needs to travel with the laptop rather than live in the building', '<strong>Document and file access</strong> structured by role rather than open to the whole firm', '<strong>Microsoft 365 tenancy reviews</strong> — MFA coverage, legacy authentication, sharing settings and unused licensing', '<strong>Client security questionnaires</strong>, needing a documented position rather than an assurance', '<strong>Backups with tested restores</strong>, because a firm that cannot produce a client file has a professional problem', '<strong>Practice management environments</strong> for medical and allied health, working alongside the software vendor', '<strong>Office fit-outs</strong> in the business park space, cabled and tested before anyone moves in'])}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What IT support in Varsity Lakes actually involves</h2>
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
            + nearby('/it-support-varsity-lakes-gold-coast')
            + related([('Business IT Support', '/it-support-and-services-gold-coast'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'), ('Business WiFi Installation', '/business-wifi-gold-coast'), ('Cybersecurity Services', '/cybersecurity-services-gold-coast'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('Pricing', '/pricing'), ('Professional services', '/it-support-professional-services-gold-coast')])
            + cta('Outgrown your setup?', "That's the most common reason Varsity businesses call. The review is free and tells you what to fix first."),
}

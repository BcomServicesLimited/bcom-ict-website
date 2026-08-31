from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;The WiFi is fine in the lobby and hopeless in the rooms&rdquo;",
     "coverage designed from the lobby outwards. Concrete floors, foil-backed insulation and tiled bathrooms stop wireless far more effectively than plasterboard, and a signal that crosses two rooms on paper crosses one in practice.",
     "Design coverage floor by floor with the building&rsquo;s actual construction in mind, rather than placing access points in corridors and hoping. Guest WiFi complaints are a review problem before they are a technical one."),
    ("&ldquo;Guests can&rsquo;t cast to the room television&rdquo;",
     "device isolation doing exactly what it was configured to do. The setting that stops guests seeing each other&rsquo;s laptops also stops a phone finding the television two metres away.",
     "Use a casting arrangement built for accommodation, which pairs a guest to their own room&rsquo;s screen without opening guests to one another. Turning isolation off to make casting work trades a real security control for a convenience."),
    ("&ldquo;The conference room collapses when the delegates arrive&rdquo;",
     "density. A function space that works for a site inspection with four people behaves completely differently with two hundred, each carrying two or three devices.",
     "Size function spaces for the headcount they are sold at, not the headcount that walks through at a quiet moment. This is the single most common reason a venue loses a repeat conference booking."),
    ("&ldquo;Every guest now has three devices&rdquo;",
     "a network sized when guests carried a laptop. Phone, laptop, tablet, watch and a streaming stick have quietly tripled the connection count per room.",
     "Count devices rather than guests when sizing capacity, and set sensible per-device limits so one guest streaming in ultra-high definition cannot degrade a floor."),
    ("&ldquo;The property system and the door locks have stopped talking&rdquo;",
     "an integration failure after an upgrade or a certificate expiry at one end. Check-in continues to work, and keys stop being issued correctly.",
     "Monitor the integration rather than waiting for a guest at the door at eleven at night. Systems that only talk to each other occasionally fail quietly, and the failure surfaces at the front desk."),
    ("&ldquo;Housekeeping tablets drop out in the stairwells and lifts&rdquo;",
     "coverage designed for guest areas only. Back-of-house circulation is usually the last place anyone puts an access point and one of the places staff move through most.",
     "Include service corridors, lifts and stairwells in the coverage design. Housekeeping systems only save time if they work where housekeeping actually is."),
]

EXAMPLE_1 = example(
    "Two hundred delegates and a network sized for four",
    "A venue had lost a recurring annual conference after the previous year&rsquo;s event. Delegates had been unable to get online for the first morning, and the organiser had moved the booking elsewhere. The venue was preparing to bid for a comparable event and wanted to be certain it would not repeat.",
    "The function space was covered by two access points, which was ample during a site inspection with a handful of people in the room. Two hundred delegates carrying phones and laptops presented roughly five hundred devices to hardware capable of handling a fraction of that. The venue had been showing prospective organisers a room that performed brilliantly while empty.",
    "Redesigned the function space for full occupancy with access points sized and positioned for density, put the conference network on its own segment away from guest and venue systems, and load-tested the room before the next event rather than during it.",
    "The venue has since run events at capacity without incident. The lost booking had been worth considerably more than the remediation, which is the arithmetic that made the decision straightforward once it was laid out.")

EXAMPLE_2 = example(
    "Three floors of rooms with one bar of signal",
    "A boutique accommodation property was receiving consistent guest reviews mentioning poor WiFi. The property had installed a well-regarded system two years earlier and could not understand the complaints.",
    "The access points had been mounted in the corridors, one per floor, which is a reasonable approach in a building with plasterboard walls. This building had rendered masonry between rooms and foil-backed insulation in the ceiling, and the signal reaching the far end of each floor was barely usable. The lobby and the areas near the lifts tested perfectly, which is where management had always tested.",
    "Surveyed the building room by room with the construction in mind, relocated and added access points so every room had a strong path, and used existing cabling routes to avoid disruption to occupied floors.",
    "Guest reviews mentioning WiFi turned positive over the following quarter. The equipment the property had bought was entirely adequate and had simply been positioned for a different building.")

FAQS = [   (   'What does a hotel or venue need from its IT provider?',
        'Guest WiFi designed for whole-property coverage and high device density, full network segmentation keeping guests away from booking and payment systems, reliable connectivity for the '
        'property management system, payment terminal separation across all outlets, and account management that keeps up with seasonal staff turnover. bcom ICT supports Gold Coast accommodation and '
        'venues on all of it.'),
    (   'Our guest WiFi works in the lobby but not the rooms. Why?',
        "Almost always coverage design rather than the internet service. Concrete, tiled bathrooms, lift shafts and long corridors block signal, and equipment placed on a guess won't reach. It needs "
        'a survey and properly positioned access points — adding extenders generally makes roaming worse.'),
    (   'Can guests reach our booking system?',
        "They shouldn't be able to, and on a properly segmented network they can't. Guest WiFi should be internet-only with no route to booking, payment, back office or building systems. If nobody "
        "can tell you whether that's the case at your property, it's worth checking."),
    (   'How do we handle constant staff turnover?',
        'By treating account lifecycle as a control rather than admin. Accounts created quickly for new casuals and — the part that matters — removed the day someone leaves. Managed clients get this '
        'as part of the arrangement.'),
    (   'Do you support function and conference connectivity?',
        "Yes, and it needs designing for the room at capacity rather than the room empty. Function space WiFi tends to be judged at exactly the moment it's under most load."),
    (   'What about our restaurant or bar POS?',
        'Same considerations as any venue — payment terminals segmented, automatic internet failover so card payments continue through an outage, and WiFi that covers outdoor and terrace areas. See '
        'our restaurants and cafés page.')]

PAGE = {
    "path": '/it-support-hospitality-gold-coast',
    "priority": '0.75',
    "title": 'IT Support for Gold Coast Hospitality & Accommodation | bcom ICT',
    "description": 'IT support for Gold Coast hotels, venues and accommodation. Guest WiFi at scale, booking system uptime, payment segmentation and seasonal staff account management.',
    "hero_img": 'it-support-hospitality-gold-coast-hero.webp',
    "hero_alt": 'Guest WiFi and venue systems supported by bcom ICT for a Gold Coast hospitality business',
    "h1": 'Guest WiFi is now part of the product',
    "lede": 'On the Gold Coast, guests review the WiFi. Covering a whole property properly — while keeping guests nowhere near your booking and payment systems — is a specific job.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Guest WiFi at scale', 'Booking system uptime', 'Payment segmentation', 'Seasonal turnover handled'],
    "crumbs": [('Industries', '/industries'), ('Hospitality', '/it-support-hospitality-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supports hotels, venues and accommodation businesses across the Gold Coast — guest WiFi designed for whole-property coverage and high device density, booking and property management system uptime, payment terminal segmentation, and account management for high seasonal staff turnover. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Guests review the WiFi',
                                         None,
                                         'On the Gold Coast, connectivity shows up in guest reviews and '
                                         'affects bookings. Coverage across rooms, common areas, pool '
                                         'decks and function spaces is a product decision, not an IT one — '
                                         'and it needs surveying rather than estimating.'),
                                 (       'Device density is extreme',
                                         None,
                                         'Every guest arrives with three devices. A property that would '
                                         'need a handful of access points for staff needs considerably '
                                         'more for guests, and the difference is not a matter of turning '
                                         'the power up.'),
                                 (       'Guests must reach nothing internal',
                                         None,
                                         'Guest networks isolated from booking systems, payment terminals, '
                                         'back office and building systems. This is the security '
                                         'requirement that matters most and the one most often built '
                                         'badly.'),
                                 (       'Seasonal turnover is relentless',
                                         None,
                                         'Casual staff arriving and leaving constantly, all needing system '
                                         'access. Prompt removal of accounts is a genuine control in this '
                                         'industry rather than an administrative nicety.')],
                'cols': 2,
                'eyebrow': "What's different",
                'h2': 'A venue is not an office with more people',
                'icon': False},
        {       'h2': 'What we design and support',
                'ticks': [       '<strong>Guest WiFi surveyed and designed</strong> for whole-property '
                                 'coverage and real device density, not estimated from a floor plan',
                                 '<strong>Full network segmentation</strong> — guests, staff, payments, '
                                 'cameras and building systems each isolated from the others',
                                 '<strong>Booking and property management system</strong> connectivity, '
                                 'uptime and backup',
                                 '<strong>Payment terminal separation</strong>, PCI-DSS-aligned, across '
                                 'restaurant, bar, reception and function spaces',
                                 '<strong>Function and conference connectivity</strong> that works when a '
                                 'room fills, because that is when it is noticed',
                                 '<strong>Account lifecycle management</strong> for seasonal staff — added '
                                 'quickly, removed promptly',
                                 "<strong>Internet with automatic failover</strong>, so an outage doesn't "
                                 'take reception and payments down together']},
        {       'h2': 'Coverage is the part that gets underestimated',
                'html': '<p style="max-width:68ch">The most common problem we are called to in Gold Coast '
                        'accommodation is guest WiFi that works in the lobby and fails in the rooms. '
                        'Concrete, tiled bathrooms, lift shafts and long corridors are difficult, and '
                        'consumer-grade equipment installed on a guess will not cover them.</p><p '
                        'style="max-width:68ch;margin-top:16px">Getting it right means surveying the '
                        'property, designing access point placement and cabling around the actual '
                        'construction, and using equipment built for density — see <a '
                        'href="/business-wifi-gold-coast">business WiFi installation</a>. It costs more '
                        'upfront than adding extenders and it is the only approach that actually '
                        'works.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The problems we are actually called to in venues and accommodation</h2>
      <p>Guest-facing technology is judged publicly. Six issues account for most of what goes wrong.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in a venue</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Restaurants & cafés', '/it-support-restaurants-gold-coast'),
        ('Network Security & Firewall', '/network-security-and-firewall-configuration-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('Guests complaining about the WiFi?', "We'll survey the property and tell you what coverage actually requires — including where the current equipment was never going to reach."),
}

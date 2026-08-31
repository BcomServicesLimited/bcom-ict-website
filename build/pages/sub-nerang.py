from layout import MARK, cta, faq_block, cards, ticks, related, nearby, trust_note, example, booking_cta

LOCAL_EX = example(
    "A Nerang workshop where the computers only failed in summer",
    "A business operating from a Nerang industrial unit reported computers shutting down without warning. It had happened the previous summer, stopped over winter, and returned. Two machines had already been replaced.",
    "The machines sat in a workshop environment and had drawn in enough dust to effectively block their cooling. In cooler months the reduced airflow was still sufficient. Above about thirty degrees ambient it was not, and the machines were shutting down to protect themselves. The two replacements had begun doing exactly the same thing within a year.",
    "Serviced every machine, fitted filtered enclosures for the two in the worst positions, and moved one off the floor where it had been drawing dust directly from the workspace.",
    "No shutdowns the following summer. Nerang&rsquo;s light industrial units and workshops present conditions ordinary office hardware is not built for, and it is usually an environment problem rather than a hardware one.")
FAQS = [   (   'Do you provide IT support in Nerang?',
        'Yes. bcom ICT attends Nerang businesses — including the industrial estates through Lawrence Drive, Spencer Road and Rudman Parade — from its Surfers Paradise office, roughly twenty minutes '
        'away, with same-day attendance usually available. Call 07 3041 8993.'),
    (   'Can you get WiFi working across a warehouse or shed?',
        'Usually, but it needs surveying rather than guessing. Steel construction, high ceilings and racking block signal in ways a floor plan will not show, and consumer equipment will not cover it '
        'however it is positioned. We measure the space and specify access points for the actual racking layout — adding more consumer gear in the wrong places makes it worse.'),
    (   'Our handheld scanners keep dropping off. Why?',
        'Almost always a coverage shadow created by racking rather than a fault with the devices. Stock moves, the shadows move with it, and a network that worked when the warehouse was half empty '
        'stops working when it is full. It is measurable and fixable with proper access point placement.'),
    (   'Our team is always on the road. What do they need?',
        'Job management software that works offline at sites with no reception and syncs when signal returns, mobile devices that can be replaced and configured the same day, and a phone system that '
        'follows people rather than sitting on a desk. See our trades and field services page.'),
    (   'Someone changed our bank details on an invoice. What do we do?',
        'Contact your bank immediately, then call us on 07 3041 8993. Going forward: multi-factor authentication on every mailbox, and a rule that any change of bank details is verified by phone on '
        'a number you already hold — never one supplied in the email. This fraud hits trades and construction hardest because progress payments are large.'),
    (   'Do you work with businesses out toward the hinterland?',
        'Yes, though connectivity gets genuinely harder past Advancetown and Gilston. That is worth knowing before assuming a cloud-first setup will work — sometimes the honest answer is a different '
        'design, and we will tell you rather than deploying something that will frustrate you.')]

PAGE = {
    "path": '/it-support-nerang-gold-coast',
    "priority": "0.7",
    "title": 'IT Support Nerang — Trades & Light Industrial | bcom ICT',
    "description": 'IT support for Nerang businesses — the industrial estates along Lawrence Drive and Spencer Road, trades, workshops, automotive and warehousing, plus the offices behind them.',
    "hero_img": 'it-support-trades-gold-coast-hero.webp',
    "hero_alt": 'A Nerang light industrial business supported by bcom ICT',
    "h1": "IT support for Nerang's industrial estates",
    "lede": 'Workshops, yards and trade businesses where the IT is a small office, a job management system, and phones that have to follow people into the field.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['~20 min from our office', 'Trades & industrial', 'Warehouse coverage', 'Same-day attendance'],
    "crumbs": [("Industries", "/industries"), ('Nerang', '/it-support-nerang-gold-coast')],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides IT support to businesses in Nerang — trades, workshops, automotive, warehousing and light industrial operations across the industrial estates, along with the offices behind them. Attendance is roughly twenty minutes from our Surfers Paradise office. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Local landscape</span>
      <h2>What Nerang is actually like to work in</h2>
    </div>
    <p style="margin-top:16px">Nerang is the Gold Coast's working suburb, and it looks nothing like
    the coastal strip. The <strong>industrial estates</strong> through Lawrence Drive, Spencer Road, Rudman
    Parade and the surrounding streets hold the trades, workshops, automotive businesses, fabricators,
    wholesalers and distributors that keep the rest of the coast running.</p>
    <p style="margin-top:16px">The premises are sheds. Steel construction, high ceilings, racking, roller
    doors and machinery — an environment that defeats consumer networking equipment comprehensively. A typical
    Nerang business has a small office of three or four desks attached to a much larger operational space, and
    the coverage problem is getting a reliable connection to where stock is picked, jobs are scanned and
    vehicles are loaded, not to the desks.</p>
    <p style="margin-top:16px">Beyond the estates, <strong>Nerang town centre</strong> and the area around
    Nerang Fair and the station carry retail, food and service businesses. The
    <strong>Nerang-Broadbeach Road</strong> corridor connects the estates east to the coast, and the M1
    interchange puts the whole northern and southern corridor within reach — which is why so many field
    service businesses base themselves here.</p>
    <p style="margin-top:16px">Inland toward Advancetown, Hinze Dam and the hinterland, connectivity gets
    genuinely harder, and that is worth knowing before assuming a cloud-first setup will work for a business
    operating out that way.</p>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Who we work with here</span>
      <h2>The businesses we see most in Nerang</h2>
      <p>Trades, industrial and field services dominate — with a small office attached to a much bigger space.</p>
    </div>
    <div class="grid grid--2">{cards([('Trades and field service businesses', None, 'Electrical, plumbing, HVAC, building and maintenance, running job management software on phones and tablets at sites with poor reception. The office is a ute more than it is a desk.'), ('Workshops and automotive', None, 'Mechanical, panel, fabrication and equipment servicing. A small office, diagnostic equipment on the floor, and a network that has to reach both.'), ('Warehousing and distribution', None, 'Coverage across the floor for scanning and picking, stock systems that have to stay in sync, and despatch schedules that dictate when disruptive work can happen.'), ('Wholesale and supply businesses', None, 'Trade counters, stock and ordering systems, and integrations with accounting software that fail quietly when nobody is watching.'), ('Construction and building businesses', None, 'Invoicing large progress payments, which makes them a specific target for invoice redirection fraud. Multi-factor authentication is the single highest-value control available.'), ('Retail and food around Nerang town centre', None, 'Point of sale, payments and a network that works on a Saturday. Smaller operations, mostly owner-run.')], icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What's technically different about Nerang</h2>
    <p style="margin-top:16px"><strong>Sheds are a genuinely different building problem.</strong>
    Steel construction reflects and blocks signal, high ceilings put access points too far from the floor, and
    racking creates shadows that move whenever stock does. Consumer equipment that would cover an office
    reaches a fraction of a warehouse, and adding more of it in the wrong places makes things worse rather
    than better. This needs surveying and proper access points positioned for the racking layout — not more
    power.</p>
    <p style="margin-top:16px"><strong>The office is small; the operation is not.</strong> Typically a few
    desks attached to a much larger space where the actual work happens. Coverage has to extend to where stock
    is picked, jobs are scanned and vehicles are loaded, and those are the places a floor plan will not tell
    you about.</p>
    <p style="margin-top:16px"><strong>Field staff are the business.</strong> Job management software that has
    to work offline at a site with no reception and sync when signal returns, mobile devices that get dropped
    and soaked and need replacing the same day, and a phone system that routes to whoever is actually
    available rather than to a desk nobody is sitting at. See
    <a href="/it-support-trades-gold-coast">trades and field services</a>.</p>
    <p style="margin-top:16px"><strong>Invoice fraud hits hardest here.</strong> Trades and construction
    businesses invoice large progress payments, and business email compromise redirecting one of those is real
    money on a single email. Multi-factor authentication on every mailbox stops nearly all of it and takes an
    afternoon. The second control is verifying any change of bank details by phone, on a number you already
    hold.</p>

    <div class="rule">{MARK}</div>

    <h2>Getting to you</h2>
    <p style="margin-top:16px">Nerang is roughly twenty minutes from our office at 9 Ferny Avenue,
    Surfers Paradise, via Nerang-Broadbeach Road or the M1. Same-day attendance is usually available across
    the estates and the town centre.</p>
    <p style="margin-top:16px">Access is generally easy — parking and vehicle access at industrial premises is
    the one thing that is simpler here than anywhere on the coast, which keeps attendance times
    predictable.</p>
    <p style="margin-top:16px">We still resolve what we can remotely at $190 + GST per hour with no call-out.
    Coverage and cabling work obviously needs someone on site.</p>

    <h2 style="margin-top:48px">Streets and precincts we regularly attend</h2>
    <p style="margin-top:16px">We attend businesses throughout Nerang and the surrounding industrial areas, including:</p>
    {ticks(['Lawrence Drive and the surrounding industrial estate', 'Spencer Road, Rudman Parade and Enterprise Street', 'Nerang-Broadbeach Road and the commercial corridor east', 'Nerang town centre, Nerang Fair and the station precinct', 'Price Street, Station Street and the surrounding commercial frontage', "Molendinar and Ashmore industrial pockets toward <a href='/it-support-southport-gold-coast'>Southport</a>", "Carrara, Merrimac and the corridor toward <a href='/it-support-robina-gold-coast'>Robina</a>", 'Advancetown, Gilston and the hinterland side, where connectivity gets harder'])}

    {trust_note('If your business invoices progress payments, multi-factor authentication on every mailbox is the highest-value afternoon of work available to you. Business email compromise redirecting a single progress claim is real money, and it is almost entirely preventable.')}
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Typical jobs</span>
      <h2>What Nerang businesses actually call us about</h2>
    </div>
    {ticks(['<strong>WiFi that will not reach the back of the shed</strong> — surveyed and solved with properly positioned access points rather than more consumer gear', '<strong>Scanners and handhelds dropping off</strong> in the racking, which is a coverage shadow rather than a device fault', '<strong>Job management software</strong> — Simpro, ServiceM8, Tradify and similar — environment, accounts, mobile access and accounting integrations', '<strong>Invoice redirection attempts</strong>, and the MFA rollout that prevents them', '<strong>Phone systems that follow people</strong> into the field rather than ringing an empty desk', "<strong>Mobile device replacement</strong> configured the same day, because a dropped phone should not cost a day's work", '<strong>Cabling across a large floor</strong>, installed by ACMA registered contractors and tested', '<strong>Stock and ordering system connectivity</strong>, including integrations that fail silently'])}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What IT support in Nerang actually involves</h2>
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
            + nearby('/it-support-nerang-gold-coast')
            + related([('Business IT Support', '/it-support-and-services-gold-coast'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'), ('Business WiFi Installation', '/business-wifi-gold-coast'), ('Cybersecurity Services', '/cybersecurity-services-gold-coast'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('Pricing', '/pricing'), ('Trades & field services', '/it-support-trades-gold-coast')])
            + cta("WiFi that won't reach the back of the shed?", "We'll measure it and tell you what coverage actually requires — usually not what's currently installed."),
}

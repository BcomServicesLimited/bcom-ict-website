from layout import MARK, cta, faq_block, cards, ticks, steps, related, svc_body, trust_note, price_table, issues, example

PRICING = [
    ('First hour on site, booked online', '$252', 'inc GST &middot; fixed price',
     [
      '<strong>$67 less than the same hour arranged by phone</strong>, which is $290 + GST ($319.00 inc GST)',
      'The call-out and the first hour with a technician, as one figure',
      'Booked through our online calendar',
      'Booked through our calendar and settled before anyone sets off',
      'Gold Coast and surrounds',
      'Beyond the first hour, $190 + GST in half-hour increments, agreed with you first',
     ]),
]

COMMON_ISSUES = [
    ("&ldquo;How soon can someone actually get here?&rdquo;",
     "the question behind most on-site calls. Same-day attendance is usually available across the Gold Coast, and honesty about it matters more than an optimistic answer.",
     "We give you a window rather than a day, and tell you if we are running late rather than leaving you wondering. Managed clients have a contracted response; everyone else gets a booked visit, most often same or next business day."),
    ("&ldquo;Can this be done remotely instead?&rdquo;",
     "often yes, and it is faster and cheaper when it can. Remote work carries no call-out.",
     "We check whether the fault needs a visit before booking one. Where it is clearly physical &mdash; a dead machine, a failed drive, a network that is down &mdash; we book straight away rather than billing an hour of trying."),
    ("&ldquo;The building makes it difficult to get in&rdquo;",
     "induction requirements, lift access cards, loading dock bookings and building management sign-in. Common in Gold Coast towers and frequently a larger part of response time than the fault.",
     "Tell us the access arrangements when you book, and we record them so no future visit rediscovers them. This is the difference between attending today and attending tomorrow."),
    ("&ldquo;Do we have to be there?&rdquo;",
     "usually not, though someone needs to let us in and there are jobs where a decision has to be made on the spot.",
     "Agree beforehand what we can proceed with unattended and what needs a call. Nobody should return to find work done that they would not have authorised."),
    ("&ldquo;What if it turns out to be bigger than we thought?&rdquo;",
     "a real risk on any diagnosis. A fault described over the phone is a fault described by its symptom.",
     "We tell you before continuing rather than afterwards. If the job grows, you approve the additional work before it happens &mdash; there is no invoice for anything you did not agree to."),
    ("&ldquo;What if the machine has to go away?&rdquo;",
     "sometimes necessary for a hardware repair or a data recovery attempt.",
     "We leave a loan device so nobody sits idle, and tell you the expected turnaround before anything is taken. A machine leaving the building without a replacement is a day of somebody&rsquo;s work."),
]

EXAMPLE_1 = example(
    "Attending today because the building details were already on file",
    "A business in a Gold Coast tower had a server that would not come back after a building power interruption. Their previous provider had quoted a next-business-day visit.",
    "The delay was not technical capacity. Reaching the tenancy required building management sign-in, a lift access card programmed for that floor, and a loading dock booking for anything larger than a laptop bag. The previous provider had no standing arrangement and was beginning that process from scratch each time they attended.",
    "Attended the same afternoon, holding the building&rsquo;s contractor induction from other work in the tower, and restored the server from backup. Recorded the access requirements against the client afterwards.",
    "Trading again that day rather than the next. In multi-tenanted buildings the access arrangements are routinely a larger component of response time than the fault itself.")

EXAMPLE_2 = example(
    "Saying it was bigger before continuing, not after",
    "A business booked a visit for a workstation that would not start. A straightforward job on the description, and quoted as one.",
    "The machine had a failed drive, which was expected. It also held the only copy of several years of records for a part of the business, because a folder had been excluded from the backup during a change eighteen months earlier and nobody had checked since. Continuing with a routine repair would have completed the job as booked and lost the data.",
    "Stopped, explained what had been found and what recovery would involve, and let the business decide before doing anything further. Recovery was authorised, the data came back, and the backup exclusion was corrected across every machine afterwards.",
    "The records were recovered and the gap in the backup was closed. The job cost more than the booking &mdash; and the alternative was completing a cheap repair correctly while destroying what the business actually needed.")

PAGE = {
    "path": '/on-site-technical-support-gold-coast',
    "priority": "0.8",
    "service": 'On-site IT Support Gold Coast',
    "title": 'On-site IT Support Gold Coast — Same-Day Attendance | bcom ICT',
    "description": 'On-site IT support at your Gold Coast office. Workstations, servers, networks and connectivity faults fixed in person, same-day where available. $100 + GST call-out plus $190 + GST per hour.',
    "hero_img": 'hero-bg-onsite-technical-support.webp',
    "hero_alt": 'A bcom ICT technician working on site at a Gold Coast business',
    "h1": 'Someone at your office, usually today',
    "lede": 'When it genuinely needs hands on the hardware. Same-day attendance across the Gold Coast where available, with the rate agreed before anyone gets in a car.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Same-day where available', '$100 + GST call-out', 'Police-checked technicians', 'Local since 2011'],
    "crumbs": [('Services', '/services'), ('On-site IT Support', '/on-site-technical-support-gold-coast')],
    "faqs": [('How quickly can you get someone on site on the Gold Coast?', 'Same-day attendance is usually available across the Gold Coast. Managed IT clients have a contracted 4-hour response for critical faults with after-hours emergency attendance included. All other clients receive a best-effort response — usually the same business day — and a booked visit, most often the same or next business day.'), ('What does an on-site visit cost?', 'A first hour on site is $290 + GST ($319.00 inc GST) — the $100 + GST call-out ($110.00 inc GST) plus the $190 + GST hour ($209.00 inc GST). Book the visit through our online calendar instead and it is a fixed $252 inc GST, which is $67 less for the same hour. Time past the first hour is $190 + GST in half-hour increments. Remote support carries no call-out, and a remote job of up to an hour is $150 + GST ($165 inc GST).'), ('Which Gold Coast suburbs do you attend?', 'All of them — Surfers Paradise, Southport, Robina, Burleigh Heads, Broadbeach, Coomera, Nerang, Helensvale, Varsity Lakes, Palm Beach and everywhere between. Remote and managed support extends Australia-wide.'), ('Are your technicians screened?', 'Yes. Technicians attending client sites hold national police checks, and Queensland Blue Cards where a site requires them — relevant for healthcare, education and childcare clients.'), ('Will you try remote first?', "Where the fault allows it, yes, and we'll tell you why. Remote is faster and has no call-out. If the problem is clearly physical — a dead machine, a failed drive, a network that's down — we book the visit straight away rather than billing you for an hour of trying."), ('What if the machine needs to go away?', 'We leave you a loan device so nobody sits idle, and tell you the expected turnaround before we take anything.')],
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides on-site IT support to businesses across the Gold Coast, attending offices to resolve workstation, server, network, printer and connectivity faults in person. Same-day attendance is usually available. On-site work is charged at a $100 + GST call-out plus $190 + GST per hour. Call 07 3041 8993.', blocks=[{'eyebrow': 'When you need someone there', 'h2': 'What genuinely requires a visit', 'sub': "We try remote first because it's faster and cheaper. These are the jobs where that isn't an option.", 'cols': 3, 'cards': [('Hardware failures', None, 'Dead machines, failed drives, power supply faults, and anything that needs opening up. We bring a loan device if yours has to leave.'), ('Server problems', None, 'Physical server faults, storage failures, and the migrations businesses defer until something breaks.'), ('Network faults', None, "Cabling problems, failed switches, dead ports and the faults that don't show up until someone traces a cable."), ('New installations', None, 'Setting up workstations, servers, switches and access points — configured and tested in place rather than shipped and hoped for.'), ('Connectivity outages', None, "When the internet is down, remote support isn't available by definition. Someone has to come."), ('Office moves', None, 'Relocating an estate is inherently on-site work. See office IT relocation for how we plan those.')]}, {'h2': 'What it costs', 'ticks': ['<strong>Book online and a first hour on site is a fixed $252 inc GST</strong> — $67 less than the same visit arranged by phone, which is $290 + GST ($319.00 inc GST).', '<strong>$100 + GST call-out</strong> ($110.00 inc GST), charged once per attendance.', '<strong>$190 + GST per hour</strong> ($209.00 inc GST), billed in half-hour increments after the first hour.', '<strong>First hour on site: $290 + GST</strong> ($319.00 inc GST) — or <strong>$252 inc GST booked online</strong>. Agreed with you before anyone leaves.', '<strong>Remote is $190 + GST with no call-out</strong>, which is why we check whether the fault needs a visit before booking one.', 'Managed IT clients have on-site attendance covered under their agreement rather than billed per visit.']}, {'eyebrow': 'Attending your site', 'h2': 'What to expect when we turn up', 'cols': 4, 'steps': [('We confirm the window', "You get a time, not a day. If we're running late you hear from us rather than wondering."), ('We diagnose before quoting more', 'If the job turns out bigger than described, you approve the extra before we continue.'), ('We work around your business', 'Disruptive work gets scheduled outside trading hours where it can be.'), ('We leave it documented', "What we found, what we did, and anything you should plan for. Added to your asset register if you're a managed client.")]}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>How much does an on-site visit cost?</h2>
      <p>Book a simple job online and it is a fixed price, with no call-out fee on top.</p>
    </div>
    {price_table(PRICING, note='A first hour on site is $290 + GST ($319.00 inc GST) &mdash; the $100 + GST call-out plus the $190 + GST hour. Book the visit through our online calendar instead and it is a fixed $252 inc GST, which is $67 less for exactly the same hour. Booking online costs us less to schedule and we pass that on rather than keeping it. Time past the first hour is charged at $190 + GST in half-hour increments, and if a job is clearly larger than a single visit we will say so before the hour is up rather than after it. Full rates are on the <a href="/pricing">pricing page</a>.')}
  </div>
</section>
'''
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The questions we are actually asked about on-site visits</h2>
      <p>Six things worth answering plainly before anyone gets in a car.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What an on-site visit actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block([('How quickly can you get someone on site on the Gold Coast?', 'Same-day attendance is usually available across the Gold Coast. Managed IT clients have a contracted 4-hour response for critical faults with after-hours emergency attendance included. All other clients receive a best-effort response — usually the same business day — and a booked visit, most often the same or next business day.'), ('What does an on-site visit cost?', 'A first hour on site is $290 + GST ($319.00 inc GST) — the $100 + GST call-out ($110.00 inc GST) plus the $190 + GST hour ($209.00 inc GST). Book the visit through our online calendar instead and it is a fixed $252 inc GST, which is $67 less for the same hour. Time past the first hour is $190 + GST in half-hour increments. Remote support carries no call-out, and a remote job of up to an hour is $150 + GST ($165 inc GST).'), ('Which Gold Coast suburbs do you attend?', 'All of them — Surfers Paradise, Southport, Robina, Burleigh Heads, Broadbeach, Coomera, Nerang, Helensvale, Varsity Lakes, Palm Beach and everywhere between. Remote and managed support extends Australia-wide.'), ('Are your technicians screened?', 'Yes. Technicians attending client sites hold national police checks, and Queensland Blue Cards where a site requires them — relevant for healthcare, education and childcare clients.'), ('Will you try remote first?', "Where the fault allows it, yes, and we'll tell you why. Remote is faster and has no call-out. If the problem is clearly physical — a dead machine, a failed drive, a network that's down — we book the visit straight away rather than billing you for an hour of trying."), ('What if the machine needs to go away?', 'We leave you a loan device so nobody sits idle, and tell you the expected turnaround before we take anything.')])
            + related([('Remote IT Support', '/remote-it-support-gold-coast'), ('Business IT Support', '/it-support-and-services-gold-coast'), ('Business Computer Repair', '/on-site-computer-repair-gold-coast'), ('Office IT Relocation', '/office-it-relocation-gold-coast'), ('Pricing', '/pricing'), ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('Book a technician', "Tell us what's happening and we'll tell you whether it needs a visit — and what it'll cost before anyone sets off."),
}

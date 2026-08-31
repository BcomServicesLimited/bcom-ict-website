from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We&rsquo;re missing calls and losing the job&rdquo;",
     "one phone ringing in an empty office, or calls going to a mobile that is inside a wall cavity. In trades the first business to answer usually wins the work.",
     "Ring several phones at once and put a real after-hours message on the line. This is configuration rather than hardware, and it is the change that most reliably pays for itself in a trades business."),
    ("&ldquo;The job app won&rsquo;t sync from site&rdquo;",
     "poor mobile coverage rather than a fault in the software. Job management apps hold work locally and push it when they can, and a basement or a steel shed defeats them.",
     "Set the app up to work properly offline and confirm what happens to photos and notes captured with no signal. Most of these products handle it well when configured for it and badly when left at defaults."),
    ("&ldquo;Photos from site are filling up phones&rdquo;",
     "job photos stored on the handset instead of against the job. It becomes a real problem when a dispute arises two years later and the evidence was on a phone that has since been replaced.",
     "Get photos attaching to the job record automatically. Site photography is often the only contemporaneous evidence a trades business has, and it belongs somewhere more durable than a camera roll."),
    ("&ldquo;Quotes take all evening&rdquo;",
     "the quoting happening twice &mdash; once on paper at the site and again at a laptop at night. It is the single largest unpaid time cost in most trades businesses.",
     "Quote from the vehicle on a tablet or phone, using the pricing already in the system. The technology is unremarkable; the change is in the habit, and it usually returns several hours a week."),
    ("&ldquo;Invoices go out a fortnight late&rdquo;",
     "a paper trail that has to reach the office before anything can be billed. Cash flow suffers for reasons that have nothing to do with the customer.",
     "Close the loop on site so the invoice can issue the day the work is done. Getting paid two weeks earlier is worth more to most trades businesses than any efficiency we could offer elsewhere."),
    ("&ldquo;Someone changed our bank details on an invoice&rdquo;",
     "invoice fraud. Trades businesses are attractive targets because invoices are frequently emailed as attachments and rarely verified.",
     "Secure the mailbox with multi-factor authentication and give customers a way to verify account details independently. A single redirected progress payment on a commercial job can exceed a year of IT spend."),
]

EXAMPLE_1 = example(
    "Answering the phone was the whole fix",
    "A plumbing business with six people had been losing work and could not work out why. Their advertising was performing, the phone rang, and the jobs were going elsewhere.",
    "Calls rang a single handset in an office nobody sat in during working hours, then dropped to a voicemail box checked once in the evening. Callers who reached voicemail simply rang the next plumber on the list. Roughly two-thirds of calls were going unanswered between eight and four.",
    "Set up a hunt group ringing the office and the mobile app on every phone at once, with voicemail-to-email as a fallback and an after-hours message stating when calls would be returned. No new handsets were bought.",
    "Calls are now answered from vehicles and sites by whoever is free. The owner&rsquo;s estimate was that the change paid for itself in the first fortnight, and the only hardware involved was phones the staff already had in their pockets.")

EXAMPLE_2 = example(
    "The progress payment that went to someone else",
    "An electrical contractor invoiced a builder for a progress claim on a commercial job. Six weeks later, chasing the payment, they were told it had been paid on time.",
    "The contractor&rsquo;s email account had been accessed using a password reused from another service. The attacker had sent a duplicate invoice from the genuine mailbox, identical apart from the account details, two days after the real one. The builder had paid the second invoice believing it to be a corrected version. There was no multi-factor authentication on any mailbox in the business.",
    "Secured every account with multi-factor authentication, removed the attacker&rsquo;s access and forwarding rules, and provided a written technical account for the contractor&rsquo;s insurer and the builder&rsquo;s own investigation.",
    "The dispute over who bore the loss took months. Multi-factor authentication across the whole business took under an hour to put in place afterwards, which is the comparison worth sitting with.")

FAQS = [   (   'What IT does a trades business actually need?',
        'Job management and quoting software that works offline at sites with poor reception, mobile devices that can be replaced and configured the same day, a phone system that follows people '
        'rather than sitting on a desk, cloud file access for plans and certificates, and email security to prevent invoice redirection fraud. bcom ICT supports Gold Coast trades and field service '
        'businesses on all of it.'),
    (   "Our software doesn't work at job sites. Can that be fixed?",
        "Sometimes. Some platforms have proper offline modes that simply aren't configured. Others genuinely require connectivity, in which case the answer is either a mobile data plan with better "
        "coverage or a different workflow. We'll tell you which applies rather than selling you a fix that won't work in a roof cavity."),
    (   'How do we stop missing calls?',
        "A cloud phone system that rings mobiles in a sensible order, with call queues so a second caller doesn't hit an engaged tone, and after-hours routing that reflects reality. For most trades "
        'businesses this is the single change with the clearest return.'),
    (   "Someone changed our client's payment details by email. What now?",
        'Contact your bank immediately, then call us. Going forward: multi-factor authentication on every mailbox, and a rule that bank detail changes are verified by phone on a number you already '
        'hold — never one from the email itself. This fraud hits trades hard because progress payments are large.'),
    (   'Do you support Simpro, ServiceM8 or Tradify?',
        "We support the environment they run in — accounts, access, mobile devices, connectivity and integrations with your accounting software — and work alongside the vendor's support for the "
        'application itself.'),
    (   "We've only got a small office. Is it worth having a provider?",
        "Depends on what a lost day costs. Plenty of trades businesses are well served by ad-hoc support at $190 + GST per hour rather than a monthly arrangement, and we'll say so if that's you. The "
        'one thing worth doing regardless is the email security.')]

PAGE = {
    "path": '/it-support-trades-gold-coast',
    "priority": '0.75',
    "title": 'IT Support for Gold Coast Trades & Field Services | bcom ICT',
    "description": 'IT support for Gold Coast trades and field service businesses. Job management software, quoting on site, mobile devices, patchy connectivity and phones that are the business.',
    "hero_img": 'it-support-trades-gold-coast-hero.webp',
    "hero_alt": 'A Gold Coast trades business using job management software supported by bcom ICT',
    "h1": 'The office is a ute',
    "lede": 'Trades IT lives on phones and tablets at job sites with poor reception. Everything has to work offline, sync when it can, and never lose a job.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Works offline', 'Phones follow people', 'Job software supported', 'Same-day on-site'],
    "crumbs": [('Industries', '/industries'), ('Trades & field services', '/it-support-trades-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supports trades and field service businesses across the Gold Coast — job management and quoting software, mobile devices used at job sites, phone systems that follow people rather than desks, and the small office network behind them. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Connectivity is unreliable by definition',
                                         None,
                                         'Job sites, roof cavities, basements and half-built houses have '
                                         'poor reception. Software that only works online is useless '
                                         'there. Anything critical has to work offline and sync when '
                                         'signal returns.'),
                                 (       'The phone is the business',
                                         None,
                                         'Missed calls are lost jobs, and nobody is sitting at a desk to '
                                         'answer them. Calls need to follow people, route sensibly when '
                                         'someone is up a ladder, and not go to a voicemail nobody '
                                         'checks.'),
                                 (       'Quoting happens on site',
                                         None,
                                         'The businesses that win work quote before they leave the '
                                         'driveway. That means the tools to do it — pricing, photos, '
                                         'signatures — have to work on a phone in a front yard.'),
                                 (       'Devices get destroyed',
                                         None,
                                         'Phones and tablets on job sites get dropped, wet and left in hot '
                                         'utes. Device management matters because the replacement needs to '
                                         'be working within the hour, not the week.')],
                'cols': 2,
                'eyebrow': "What's different",
                'h2': 'Almost nothing happens at a desk',
                'icon': False},
        {       'h2': 'What we sort out',
                'ticks': [       '<strong>Job management software</strong> — the environment, accounts, '
                                 'integrations and mobile access. Simpro, ServiceM8, Tradify and similar '
                                 'platforms',
                                 '<strong>Mobile device setup</strong> so a replacement phone is working '
                                 'the same day, with remote wipe if one is lost on site',
                                 '<strong>Phone systems that follow people</strong> — see <a '
                                 "href='/voip-phone-system-installation-and-support-gold-coast'>VoIP</a> — "
                                 "with call routing that reflects who's actually available",
                                 '<strong>Cloud file access</strong> so plans, photos and certificates are '
                                 'reachable from anywhere rather than sitting on the office computer',
                                 '<strong>Backups of the office systems</strong> — accounts, job history '
                                 "and the records you're legally required to keep",
                                 '<strong>Email security</strong>, because invoice redirection fraud hits '
                                 'trades hard and a redirected progress payment is real money']},
        {       'h2': 'The fraud that hits trades',
                'html': '<p style="max-width:68ch">Worth naming specifically. Someone gets into a mailbox, '
                        'watches for an invoice going out, then sends a near-identical one with different '
                        'bank details. For a trades business invoicing progress payments on a build, that '
                        'is a large sum on a single email.</p><p '
                        'style="max-width:68ch;margin-top:16px">Multi-factor authentication on email stops '
                        'nearly all of it, and it takes an afternoon. The second control is a rule that '
                        'any change of bank details is verified by phone on a number you already have. See '
                        '<a href="/cybersecurity-services-gold-coast">cybersecurity services</a>.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The problems we are actually called to in trades</h2>
      <p>Trades businesses lose money in the field and in the mailbox, and the field problems are the cheaper ones to fix.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in a trades business</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast'),
        ('Remote IT Support', '/remote-it-support-gold-coast'),
        ('Data Backup & Disaster Recovery', '/data-backup-recovery-gold-coast'),
        ('Pricing', '/pricing')])
            + cta('Missing calls or losing jobs to paperwork?', 'Both are usually cheaper to fix than people expect. The first conversation costs nothing.'),
}

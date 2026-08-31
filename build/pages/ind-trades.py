from layout import cta, faq_block, related, svc_body

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
        "Depends on what a lost day costs. Plenty of trades businesses are well served by ad-hoc support at $198 + GST per hour rather than a monthly arrangement, and we'll say so if that's you. The "
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
            + faq_block(FAQS)
            + related([       ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast'),
        ('Remote IT Support', '/remote-it-support-gold-coast'),
        ('Data Backup & Disaster Recovery', '/data-backup-recovery-gold-coast'),
        ('Pricing', '/pricing')])
            + cta('Missing calls or losing jobs to paperwork?', 'Both are usually cheaper to fix than people expect. The first conversation costs nothing.'),
}

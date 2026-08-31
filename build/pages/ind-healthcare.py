from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Does the Privacy Act apply to a small medical practice?',
        "Yes. Health service providers are a named exception to the Privacy Act's small business exemption, so the obligations apply regardless of annual turnover. A two-practitioner allied health "
        'clinic carries the same responsibilities around patient information and notifiable data breaches as a much larger provider. This catches out a great many Gold Coast practices.'),
    (   'What happens if patient records are exposed?',
        'You have obligations under the Notifiable Data Breaches scheme to assess whether serious harm is likely and, if so, to notify the OAIC and the affected patients. bcom ICT provides '
        'containment, investigation and the factual technical account you need for that assessment — the notification decision itself sits with the practice.'),
    (   'Do your technicians have police checks?',
        'Yes. Technicians attending client sites hold national police checks, and Queensland Blue Cards where the site requires them. For practices seeing children, that is usually a hard '
        'requirement rather than a preference.'),
    (   'Can you work with our practice management software?',
        "We support the environment it runs on — the server or cloud tenancy, backups, access, updates and the network. For the application itself we work alongside your vendor's support rather than "
        'replacing it, which is usually the arrangement that works best.'),
    (   'What should a practice do first?',
        'Multi-factor authentication on email, backups held separately from the network with a tested restore, and knowing where you sit against the Essential Eight. Those three cover most of what '
        'actually happens and most of what an insurer will ask about.'),
    (   'Do you support allied health as well as medical?',
        'Yes — physiotherapy, psychology, dental, podiatry, optometry and similar practices. The obligations are the same and the practical problems are very similar.')]

PAGE = {
    "path": '/it-support-healthcare-gold-coast',
    "priority": '0.75',
    "title": 'IT Support for Gold Coast Healthcare & Allied Health | bcom ICT',
    "description": 'IT support for Gold Coast medical, dental and allied health practices. Privacy Act obligations apply regardless of turnover — patient records, practice software and screened technicians.',
    "hero_img": 'it-support-healthcare-gold-coast-hero.webp',
    "hero_alt": 'IT support being provided to a Gold Coast healthcare practice by bcom ICT',
    "h1": "Health practices don't get the small business exemption",
    "lede": "Most Australian businesses under $3 million turnover fall outside the Privacy Act. Health service providers don't — at any size. That changes what your IT has to do.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Privacy Act at any size', 'Police checks & Blue Cards', 'Practice software supported', 'Essential Eight aligned'],
    "crumbs": [('Industries', '/industries'), ('Healthcare', '/it-support-healthcare-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supports medical, dental and allied health practices across the Gold Coast. Health service providers are covered by the Privacy Act regardless of annual turnover — the small business exemption does not apply to them — so practices carry obligations around patient information and notifiable data breaches that most businesses their size do not. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Turnover is irrelevant here',
                                         None,
                                         "The Privacy Act's small business exemption generally covers "
                                         'businesses under $3 million annual turnover. Health service '
                                         'providers are a named exception — a two-practitioner allied '
                                         'health clinic carries the same obligations as a hospital. Many '
                                         'practice owners have never been told this.'),
                                 (       'The NDB scheme applies',
                                         None,
                                         'If patient information is accessed without authorisation and '
                                         'serious harm is likely, you have obligations to assess and to '
                                         'notify the OAIC and affected patients. That is not optional and '
                                         'it is not something your IT provider can discharge for you.'),
                                 (       'Sensitive information is a higher bar',
                                         None,
                                         "Health information is 'sensitive information' under the Act, "
                                         'which attracts stricter handling requirements than ordinary '
                                         'personal information. The consequences of exposure are '
                                         'correspondingly worse.'),
                                 (       'Your suppliers count',
                                         None,
                                         'Outsourced arrangements — including your IT provider and your '
                                         'practice software vendor — form part of your compliance picture. '
                                         'Which is why our own position is published rather than '
                                         'asserted.')],
                'cols': 2,
                'eyebrow': "The thing most practices don't know",
                'h2': "The exemption that doesn't apply to you",
                'icon': False,
                'sub': 'This catches out more Gold Coast practices than any other compliance point.'},
        {       'h2': 'What we actually do for practices',
                'ticks': [       '<strong>Practice management software</strong> kept running, backed up '
                                 'and updated — it is the system that stops the practice if it fails',
                                 '<strong>Patient record backup</strong> held separately from the network, '
                                 'with restores tested rather than assumed',
                                 '<strong>Access control</strong> so reception, practitioners and '
                                 'administrators see what their role requires and no more',
                                 '<strong>Multi-factor authentication</strong> across email and remote '
                                 'access, which is the single highest-value control available',
                                 '<strong>Screened technicians</strong> — national police checks, and '
                                 'Queensland Blue Cards where the site requires them',
                                 '<strong>Secure messaging and email</strong>, including the SPF, DKIM and '
                                 'DMARC records that stop someone sending referrals in your name',
                                 '<strong>Essential Eight assessment</strong>, which is what an auditor or '
                                 'insurer will reference']},
        {       'h2': 'If something does happen',
                'html': '<p style="max-width:68ch">The first hour matters. Disconnect affected machines '
                        'from the network but do not power them off — shutting down destroys evidence that '
                        'helps establish what was actually accessed, and for a practice that determination '
                        'decides whether you notify.</p><p style="max-width:68ch;margin-top:16px">We '
                        'contain, investigate and give you the factual written account you need for your '
                        'assessment. The notification decision itself remains yours — see <a '
                        'href="/notifiable-data-breach-guide-australia">the NDB guide</a> and <a '
                        'href="/cyber-incident-response-gold-coast">incident response</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Notifiable Data Breaches guide', '/notifiable-data-breach-guide-australia'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Data Backup & Disaster Recovery', '/data-backup-recovery-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Trust centre', '/trust-centre')])
            + cta('Not sure where your practice stands?', "A health check tells you — including whether you'd be able to answer an OAIC question about what was accessed."),
}

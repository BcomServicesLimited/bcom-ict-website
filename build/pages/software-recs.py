from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Can you recommend business software for us?',
        'Yes, vendor-neutrally — bcom ICT takes no referral fees from software vendors. We start by mapping how the work is actually done rather than comparing feature lists, and the recommendation '
        'is frequently to consolidate what you already have rather than add another tool.'),
    (   'Do you get paid by software vendors?',
        "No. That's the point of asking us rather than a reseller. It also means we'll tell you when the software isn't the problem — which is a conclusion a vendor is never going to reach."),
    (   "We've got too many subscriptions. Can you help?",
        "That's the most common version of this job. A review typically finds duplicate tools doing the same work, seats for departed staff, licence tiers above what's needed, and things already "
        'included in your Microsoft 365 subscription being paid for separately.'),
    (   'Should we build custom software instead?',
        'Occasionally, but rarely for a small business. Off-the-shelf plus proper configuration and integration covers most needs at a fraction of the cost and with someone else maintaining it. '
        "We'll say when custom is genuinely warranted.")]

PAGE = {
    "path": '/software-recommendations-gold-coast',
    "priority": '0.65',
    "title": 'Business Software Recommendations Gold Coast | bcom ICT',
    "description": 'Independent advice on business software for Gold Coast businesses — what to use, what to consolidate, and when the answer is to fix the process rather than buy a tool.',
    "hero_img": 'hero-bg-software-installation.webp',
    "hero_alt": 'Business software being evaluated with a Gold Coast client by bcom ICT',
    "h1": 'Which software should we actually use?',
    "lede": "Vendor-neutral advice on business software — including the fairly common answer that the tool isn't the problem.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Vendor-neutral', 'No referral fees', 'Consolidation first', '$198 + GST/hr'],
    "crumbs": [('Services', '/services'), ('Software Recommendations', '/software-recommendations-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides vendor-neutral advice on business software for Gold Coast businesses — evaluating options against how a business actually operates, identifying duplicate or unused subscriptions, and advising when a process change would serve better than a new tool. bcom ICT takes no vendor referral fees. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'What does the work actually look like?',
                                         None,
                                         'Before comparing products, we map how the task is done now, '
                                         'where time goes and where things get re-keyed between systems. '
                                         'The answer is often that two existing tools should talk to each '
                                         'other rather than a third being bought.'),
                                 (       'What have you already got?',
                                         None,
                                         'Businesses in Microsoft 365 frequently pay separately for things '
                                         'already included. A subscription review before a purchase is '
                                         'common sense and regularly saves more than the new tool costs.'),
                                 (       'Who has to use it?',
                                         None,
                                         "The best-reviewed product is worthless if your team won't adopt "
                                         'it. Fit with how people already work matters more than feature '
                                         'count.'),
                                 (       'What does leaving look like?',
                                         None,
                                         'Ask before you commit, not after. Can you export your data in a '
                                         "usable form? Software that's hard to leave is a decision you "
                                         'make once and live with for years.')],
                'cols': 2,
                'eyebrow': 'How we approach it',
                'h2': 'Start with the workflow, not the shortlist',
                'icon': False},
        {       'h2': "The answer is often 'fewer tools'",
                'html': '<p style="max-width:68ch">The most common finding is not a missing product — it '
                        'is four overlapping ones. A CRM nobody fully adopted, a project tool one '
                        'department chose, a file-sharing service predating Microsoft 365, and a '
                        'subscription for someone who left two years ago.</p><p '
                        'style="max-width:68ch;margin-top:16px">Consolidating is usually cheaper, simpler '
                        'to support and easier for staff than adding another system. It also reduces the '
                        'number of places your business data sits, which matters for security and for '
                        "answering a client's questions about how you handle their information.</p>"}])
            + faq_block(FAQS)
            + related([       ('Software Installation & Config', '/software-installation-configuration-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Technology Procurement Advice', '/technology-procurement-advice-gold-coast'),
        ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast'),
        ('AI Implementation', '/artificial-intelligence-service-gold-coast'),
        ('IT Needs Assessment', '/it-needs-assessment-gold-coast')])
            + cta('Drowning in subscriptions?', 'A review usually finds enough duplication to cover the cost of doing it.'),
}

from layout import cta, faq_block, related, svc_body

FAQS = [   (   'How do you choose a managed IT provider?',
        'Judge on criteria rather than marketing. Ask for a written response target by priority, month-to-month terms rather than a lock-in contract, evidence that client restores are actually '
        "tested, the provider's own security position and insurance, whether attending technicians are screened, and what happens to your documentation if you leave. Ask every provider the same "
        'questions and compare the answers in writing.'),
    (   "What's the single most revealing question?",
        '"When did you last test a restore for a client, and what happened?" Almost every provider runs backups. Far fewer verify they restore. A vague answer, or one that relies on the backup '
        'software reporting success, tells you what you need to know.'),
    (   'Should we avoid long contracts?',
        "Generally, yes. A multi-year term protects the provider rather than you, and a good provider doesn't need one. There are exceptions where significant hardware is bundled into the monthly "
        'fee, but ask specifically what the term is buying you.'),
    (   'How much should managed IT cost?',
        'There is no single figure, and anyone quoting one before understanding your environment is guessing. Cost is driven by whether you run a server, hardware age, number of sites, what has to '
        "stay available and what compliance applies. What you should expect is a quote after a proper review, and full transparency about what's included versus extra."),
    (   "Does the provider's size matter?",
        "It's a trade-off rather than a ranking. A larger provider gives deeper cover through leave and more specialists; a smaller one gives people who know your environment without reading notes "
        "and an escalation that reaches a decision-maker. Ask specifically about cover during simultaneous leave if that's a concern."),
    (   'Should we check their own security?',
        'Yes, and few businesses do. Your provider holds administrative access to your systems, which makes them part of your risk. Ask about individually named access, MFA on their own tooling, '
        'what frameworks they work to, and whether they carry cyber liability insurance.')]

PAGE = {
    "path": '/how-to-choose-an-msp-gold-coast',
    "priority": '0.75',
    "article": True,
    "title": "How to Choose an MSP on the Gold Coast — Buyer's Guide | bcom ICT",
    "description": "Eight questions to ask any managed IT provider before you sign — including us. A neutral buyer's guide for Gold Coast businesses, from people on the other side of the table.",
    "hero_kind": 'doc',
    "eyebrow": "Guide",
    "h1": 'Eight questions to ask any IT provider',
    "lede": "Written by people who sit on the other side of this table. Ask all eight of any provider you're considering — including us — and compare the answers in writing.",
    "crumbs": [("Guides", "/services"), ('How to choose an MSP', '/how-to-choose-an-msp-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='To choose a managed IT provider, judge on criteria rather than marketing: a written response target, month-to-month terms rather than a lock-in contract, a documented security position, technicians who actually attend your premises, transparent pricing, and a clean exit process. Several capable MSPs operate on the Gold Coast — ask each the eight questions below and compare the written answers.',
                     blocks=[       {       'cards': [       (       "1. What's your response target, in writing?",
                                         None,
                                         'Not "we\'re very responsive". An actual commitment, by priority, '
                                         'with different answers for a critical fault and a password '
                                         "reset. If it isn't written down before you sign, it isn't a "
                                         'commitment. <em>Ours is published — priority matrix and '
                                         'all.</em>'),
                                 (       '2. What happens outside business hours?',
                                         None,
                                         'Who answers, what they can actually do, and whether after-hours '
                                         'attendance is included or extra. Many providers advertise 24/7 '
                                         'and mean an answering service. <em>We answer 24/7; after hours '
                                         "it's an AI operator that takes details and escalates, and it "
                                         'says so.</em>'),
                                 (       '3. Is it month-to-month, or locked in?',
                                         None,
                                         "A three-year term protects the provider, not you. If they're "
                                         "good you'll stay anyway. <em>Ours is month-to-month with no exit "
                                         'fee.</em>'),
                                 (       "4. What exactly is included, and what's extra?",
                                         None,
                                         'Get the boundary in writing — particularly around projects, '
                                         'hardware, after-hours work and per-ticket charges. "Unlimited '
                                         'support" with a per-ticket fee isn\'t unlimited.')],
                'cols': 2,
                'eyebrow': 'The questions',
                'h2': "1–4: what they'll do for you",
                'icon': False},
        {       'cards': [       (       '5. When did you last test a restore for a client?',
                                         None,
                                         'The single best question on this list. Almost every provider '
                                         'does backups. Far fewer test that they restore. If the answer is '
                                         'vague, or "the software reports success", that is your answer.'),
                                 (       "6. What's your own security position?",
                                         None,
                                         "They'll hold keys to your systems. Ask about individually named "
                                         'access rather than shared logins, MFA on their own tools, what '
                                         "they're aligned to, and whether they carry cyber liability "
                                         "insurance. <em>Ours is published in full, including what we're "
                                         'not certified to.</em>'),
                                 (       '7. Who actually attends, and are they screened?',
                                         None,
                                         "Whether it's their staff or subcontractors, and whether the "
                                         'person entering your premises holds a police check. For '
                                         'healthcare, education and childcare sites this is usually a hard '
                                         'requirement.'),
                                 (       '8. What happens if we leave?',
                                         None,
                                         'Ask before you join. Documentation, credentials, licences and '
                                         'asset register handed over — or held as leverage. A provider '
                                         'confident in their service answers this easily. <em>We treat a '
                                         'clean exit as part of the service.</em>')],
                'cols': 2,
                'h2': '5–8: what happens when things go wrong',
                'icon': False},
        {       'h2': 'Three answers that should end the conversation',
                'ticks': [       '<strong>"We\'ll get to it when we can."</strong> No response target '
                                 "means no commitment, and you'll find out where you sit in the queue at "
                                 'the worst possible moment.',
                                 '<strong>"You\'ll need to sign a three-year agreement."</strong> '
                                 'Occasionally justified where significant hardware is bundled. Usually '
                                 "it's protecting the provider from their own service quality.",
                                 '<strong>"We hold the domain and licences in our name."</strong> Your '
                                 'domain, your Microsoft 365 tenancy and your software licences should be '
                                 'registered to your business. This is the most common thing we find wrong '
                                 "when taking over, and it's much easier to fix while everyone's still on "
                                 'good terms.']},
        {       'h2': 'A note on this guide',
                'html': '<p style="max-width:68ch">We wrote this knowing it might cost us work, because a '
                        'business that asks these questions and picks someone else was probably a better '
                        'fit for them anyway. What we would rather avoid is being chosen for the wrong '
                        'reasons and parting company in eight months.</p><p '
                        'style="max-width:68ch;margin-top:16px">Our own answers are <a '
                        'href="/service-levels-and-security">published</a> rather than given on request, '
                        'which is the only way a comparison like this is worth doing. Take this list to '
                        "whoever else you're considering.</p>"}])
            + faq_block(FAQS)
            + related([       ('Published service levels', '/service-levels-and-security'),
        ('Trust centre', '/trust-centre'),
        ('Managed IT vs break-fix', '/managed-it-vs-break-fix'),
        ('What IT support costs', '/it-support-cost-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Onboarding — first 30 days', '/onboarding-first-30-days')])
            + cta('Ask us the eight questions', "Most of our answers are already published. If one isn't, ask and we'll put it in writing."),
}

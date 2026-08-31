from layout import cta, faq_block, related, svc_body

FAQS = [   (   'How much does IT support cost on the Gold Coast?',
        'bcom ICT charges $198 + GST per hour ($217.80 inc GST) for business IT support, plus a $100 + GST call-out ($110 inc GST) for on-site attendance — a first hour on site is $298 + GST '
        '($327.80 inc GST). Remote support carries no call-out. Managed IT is a flat monthly fee calculated from your requirements and the services included, quoted after a free review.'),
    (   'Is managed IT cheaper than paying hourly?',
        "In a quiet month, no. Over a year it usually is — and that's before counting staff hours lost to problems nobody is preventing. The real difference is predictability: a flat monthly fee can "
        "be budgeted, and you're never weighing up whether a problem is worth a call-out."),
    (   "Why won't providers publish managed IT prices?",
        'Partly because a single figure would mislead — the same headcount can cost three times as much depending on servers, hardware age, sites and compliance. Partly because some providers prefer '
        'the number to be negotiable. Ask for a quote after a proper review rather than a figure over the phone.'),
    (   'Should we pay for a quote or an assessment?',
        'Quoting should be free. A detailed security or systems assessment reasonably carries a fee, but it should be fixed and agreed before it starts, and you should keep the report regardless of '
        'what you do next.'),
    (   "What's a reasonable hourly rate for business IT?",
        "It varies with experience and what's included. What matters more than the headline rate is whether the provider tries remote first — remote work with no call-out is often cheaper overall "
        'than a lower hourly rate with a call-out attached to every job.'),
    (   'Do we get charged for travel?',
        "We charge a single $100 + GST call-out for on-site attendance across the Gold Coast rather than billing travel time by distance. It's the same figure whether you're in Broadbeach or "
        'Coomera.')]

PAGE = {
    "path": '/it-support-cost-gold-coast',
    "priority": '0.8',
    "article": True,
    "title": 'What Does IT Support Cost on the Gold Coast? | bcom ICT',
    "description": 'What business IT support actually costs on the Gold Coast — hourly rates, call-out fees, managed IT pricing models, and what drives the number up or down.',
    "hero_kind": 'doc',
    "eyebrow": "Guide",
    "h1": 'What does IT support actually cost?',
    "lede": "Most providers won't put a number on a page. Here's ours, plus what genuinely drives the figure — so you can sanity-check any quote, including one that isn't from us.",
    "crumbs": [("Guides", "/services"), ('What IT support costs', '/it-support-cost-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='Business IT support on the Gold Coast is typically charged either hourly or as a flat monthly managed fee. bcom ICT charges $198 + GST per hour ($217.80 inc GST), plus a $100 + GST call-out ($110 inc GST) for on-site attendance — so a first hour on site is $298 + GST. Remote support carries no call-out. Managed IT is a flat monthly fee calculated from business requirements and services included, quoted after a free review.',
                     blocks=[       {       'cards': [       (       'Hourly / break-fix',
                                         None,
                                         'You pay when something goes wrong. Typically an hourly rate plus '
                                         'a call-out for on-site attendance. Predictable per job, '
                                         'unpredictable per year. Suits simple setups where a problem is '
                                         'an annoyance rather than a crisis.'),
                                 (       'Managed IT',
                                         None,
                                         'A flat monthly fee covering monitoring, helpdesk, patching and '
                                         'backup. Predictable per year, more expensive in a quiet month. '
                                         "Suits businesses with a server, staff who can't work without "
                                         "their systems, or client data they'd need to prove is "
                                         'protected.')],
                'cols': 2,
                'eyebrow': 'The two models',
                'h2': 'Hourly, or a monthly fee',
                'icon': False,
                'sub': 'Almost every Australian IT provider works one of these two ways. Which suits you '
                       'depends on what an hour of downtime costs.'},
        {       'h2': 'Our published rates',
                'html': '<div class="pricecard" style="max-width:none"><div class="grid grid--3" '
                        'style="margin-top:4px"><div><div class="from">$198 <small>+ GST per hour · '
                        '$217.80 inc GST</small></div></div><div><div class="from">$100 <small>+ GST '
                        'on-site call-out · $110 inc GST</small></div></div><div><div class="from">$298 '
                        '<small>+ GST first hour on site · $327.80 inc GST</small></div></div></div><p '
                        'style="margin-top:20px;font-size:.9375rem;color:var(--slate)">Billed in hourly '
                        'increments and agreed before work starts. Remote support carries no call-out, '
                        'which is why we try remote first wherever the fault allows it.</p></div><p '
                        'style="max-width:68ch;margin-top:20px">We publish these because the alternative — '
                        '"contact us for pricing" — wastes everyone\'s time and tends to mean the number '
                        'moves depending on who\'s asking. See <a href="/pricing">pricing</a> for the full '
                        'picture including projects.</p>'},
        {       'h2': 'What drives a managed IT quote',
                'sub': 'There is no per-seat figure, because two businesses with the same headcount can '
                       'differ by a factor of three. These are the things that actually move it.',
                'ticks': [       '<strong>Do you run a server?</strong> On-premise servers carry '
                                 "maintenance, patching and backup that cloud-only businesses simply don't "
                                 'have.',
                                 '<strong>How old is the hardware?</strong> An ageing fleet generates '
                                 'support hours no provider can prevent. Sometimes replacement is the '
                                 'cheaper support strategy.',
                                 '<strong>How many sites?</strong> One office is straightforward. Three '
                                 'sites with connectivity between them is a different job.',
                                 '<strong>What has to stay available?</strong> A business that can lose a '
                                 "morning is priced differently to one that can't lose an hour.",
                                 '<strong>What compliance applies?</strong> AFS licensees, health '
                                 'providers and businesses handling sensitive data need controls and '
                                 "evidence that others don't.",
                                 '<strong>How documented is it now?</strong> An undocumented environment '
                                 'costs more to take on, because the first month is discovery.']},
        {       'cards': [       (       "What's not included?",
                                         None,
                                         'Projects, hardware, after-hours work and per-ticket charges are '
                                         'the usual exclusions. "Unlimited support" with a per-ticket fee '
                                         'is not unlimited. Get the boundary in writing.'),
                                 (       'Is there a minimum term?',
                                         None,
                                         'A three-year agreement protects the provider. Ask what the term '
                                         "is actually buying you — occasionally it's bundled hardware, "
                                         "more often it isn't."),
                                 (       "What's the response commitment?",
                                         None,
                                         'A monthly fee with no written response target is a subscription, '
                                         'not a service level. Ask for it by priority, in writing.'),
                                 (       'What happens if we leave?',
                                         None,
                                         'Whether documentation, credentials and licences get handed over. '
                                         'Worth asking before you join rather than after.')],
                'cols': 2,
                'h2': 'Questions worth asking about any quote',
                'icon': False},
        {       'h2': 'When the honest answer is "you don\'t need us monthly"',
                'html': '<p style="max-width:68ch">Plenty of Gold Coast businesses are better served by '
                        'hourly support than by a managed agreement, and we say so regularly. If you have '
                        'a handful of laptops, everything in the cloud, no server and no compliance '
                        'obligations, a monthly fee may be buying you very little.</p><p '
                        'style="max-width:68ch;margin-top:16px">Two things are worth doing regardless of '
                        'which model you choose: multi-factor authentication on every account, and a '
                        'backup you have actually watched restore. Between them they prevent most of what '
                        'genuinely damages a small business, and neither is expensive.</p>'}])
            + faq_block(FAQS)
            + related([       ('Pricing', '/pricing'),
        ('Managed IT vs break-fix', '/managed-it-vs-break-fix'),
        ('How to choose an MSP', '/how-to-choose-an-msp-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Published service levels', '/service-levels-and-security')])
            + cta('Want a real number for your business?', 'The review is free and the quote is based on what you actually run — not on a headcount and an assumption.'),
}

from layout import cta, faq_block, related, svc_body

FAQS = [   (   "What's the difference between managed IT and break-fix?",
        'Break-fix means paying per job when something goes wrong; managed IT means a flat monthly fee covering monitoring, helpdesk, patching and backup. The structural difference is incentive — a '
        'break-fix provider earns when systems fail, while a managed provider carries the cost of recurring faults, which makes chasing root causes the rational thing to do.'),
    (   'Is managed IT worth it for a small business?',
        "It depends on what downtime costs you. Managed IT makes sense once you have a server, staff who genuinely can't work without their systems, or client data you'd need to prove is protected. "
        "Below that, hourly support often represents better value and we'll say so rather than sell around it."),
    (   'Which works out cheaper?',
        "Over a quiet year, break-fix. Over a typical year, managed IT usually — and that's before counting staff hours lost to problems nobody prevented. The stronger argument for managed isn't "
        "cost, it's predictability and who's responsible for recurring faults."),
    (   'Can we start with break-fix and move to managed later?',
        'Yes, and most of our managed clients did exactly that. Working together on an hourly basis first is a reasonable way for both sides to find out whether the relationship works before '
        'committing to anything monthly.'),
    (   'Is there something between the two?',
        "Yes, and it's underused. Keeping hourly support for day-to-day issues while paying separately for monitored backups, patching and security baseline maintenance covers most of what actually "
        'damages a business, without a full managed agreement.'),
    (   'What should we watch out for in a managed agreement?',
        'A minimum term, a per-ticket charge sitting behind the words "unlimited support", no written response target, and no clarity about what happens to your documentation if you leave. All four '
        'are worth resolving before signing.')]

PAGE = {
    "path": '/managed-it-vs-break-fix',
    "priority": '0.75',
    "article": True,
    "title": 'Managed IT vs Break-Fix — Which Does Your Business Need? | bcom ICT',
    "description": 'The real difference between managed IT and paying by the hour, what each costs, and an honest guide to which one an Australian small business actually needs.',
    "hero_kind": 'doc',
    "eyebrow": "Guide",
    "h1": 'Managed IT or pay-as-you-go?',
    "lede": "Both are legitimate. The difference isn't really about cost — it's about who carries the incentive to stop problems recurring.",
    "crumbs": [("Guides", "/services"), ('Managed IT vs break-fix', '/managed-it-vs-break-fix')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='Break-fix IT support means paying per job when something breaks; managed IT means a flat monthly fee covering monitoring, helpdesk, patching and backup. The structural difference is incentive: a break-fix provider earns when things fail, while a managed provider carries the cost of recurring faults. Managed IT suits businesses with a server, staff who cannot work without their systems, or client data they must prove is protected.',
                     blocks=[       {       'h2': 'The comparison',
                'html': '<div class="tablewrap"><table><thead><tr><th>&nbsp;</th><th>Break-fix / '
                        'hourly</th><th>Managed IT</th></tr></thead><tbody><tr><td class="slot">You '
                        'pay</td><td>Per job, when something breaks</td><td>A flat monthly '
                        'fee</td></tr><tr><td class="slot">Cost pattern</td><td>Predictable per job, '
                        'unpredictable per year</td><td>Predictable per year, higher in a quiet '
                        'month</td></tr><tr><td class="slot">Who finds the problem</td><td>You do, usually '
                        'when it stops someone working</td><td>Monitoring does, often before anyone '
                        'notices</td></tr><tr><td class="slot">Recurring faults</td><td>Billed again each '
                        "time</td><td>Root cause chased at the provider's cost</td></tr><tr><td "
                        'class="slot">Patching &amp; backups</td><td>Whoever remembers</td><td>Scheduled, '
                        'monitored, restores tested</td></tr><tr><td class="slot">Response '
                        'commitment</td><td>Best effort, or a callback window</td><td>Contracted target by '
                        'priority</td></tr><tr><td class="slot">Documentation</td><td>Rarely anyone\'s '
                        "job</td><td>Asset register maintained, and it's yours</td></tr><tr><td "
                        'class="slot">Suits</td><td>Simple setups, low downtime cost</td><td>Servers, '
                        'dependent staff, compliance obligations</td></tr></tbody></table></div>'},
        {       'h2': 'The incentive problem',
                'html': '<p style="max-width:68ch">This is the part worth understanding, and it is not a '
                        'criticism of break-fix providers — most are perfectly honest. It is '
                        'structural.</p><p style="max-width:68ch;margin-top:16px">Under break-fix, a '
                        'provider earns when your systems fail. Nobody is deliberately leaving problems in '
                        'place, but nobody is being paid to prevent them either. Investigating why a fault '
                        'keeps returning is unbillable work, so it tends not to happen.</p><p '
                        'style="max-width:68ch;margin-top:16px">Under a managed agreement the incentive '
                        'inverts. A recurring fault costs the provider time they have already been paid '
                        'for, so chasing the cause becomes the commercially rational thing to do. That '
                        'single difference is what most clients actually notice after switching — not the '
                        'response times.</p>'},
        {       'eyebrow': 'Making the call',
                'h2': 'Five questions that decide it',
                'ticks': [       '<strong>What does an hour of downtime cost you?</strong> If the answer '
                                 'is "not much", break-fix is probably fine and we\'ll say so.',
                                 "<strong>Do you run a server, or anything you can't trade "
                                 'without?</strong> If yes, someone should be watching it.',
                                 '<strong>Have you watched a backup restore?</strong> Not whether backups '
                                 "run — whether you've seen one come back. If not, that's the gap.",
                                 "<strong>Do you hold client data you'd have to account for?</strong> "
                                 'Health providers, financial services and anyone handling identity '
                                 'documents are in a different position.',
                                 "<strong>Is the same thing breaking repeatedly?</strong> That's the "
                                 'clearest signal. Repeat faults under break-fix are repeat invoices.']},
        {       'h2': 'A middle option people forget',
                'html': '<p style="max-width:68ch">It is not strictly binary. Plenty of businesses keep '
                        'hourly support for day-to-day issues but pay separately for the things that '
                        'genuinely need to be ongoing — monitored backups, security baseline maintenance, '
                        'and patching.</p><p style="max-width:68ch;margin-top:16px">That covers most of '
                        'what actually damages a small business without a full managed agreement. If a '
                        'monthly fee looks like more than you need, it is worth asking about.</p>'}])
            + faq_block(FAQS)
            + related([       ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('What IT support costs', '/it-support-cost-gold-coast'),
        ('How to choose an MSP', '/how-to-choose-an-msp-gold-coast'),
        ('Published service levels', '/service-levels-and-security'),
        ('Onboarding — first 30 days', '/onboarding-first-30-days')])
            + cta('Not sure which you need?', "The free review answers it — including when the answer is that you don't need us monthly yet."),
}

from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Why are our office computers so slow?',
        "In most Gold Coast offices the cause is a mechanical hard drive in a machine that should have an SSD, insufficient memory for what's now being run, or accumulated software nobody "
        "uninstalled. bcom ICT assesses each machine and reports what's actually causing it, with the cost of fixing it against the cost of replacement. Call 07 3041 8993."),
    (   'Is it worth upgrading an old computer?',
        "Depends on its age and what's wrong. An SSD in a three-year-old machine transforms it for a modest cost. The same upgrade in a seven-year-old machine is money spent on borrowed time. We "
        'assess per machine rather than applying one answer to the fleet.'),
    (   'What difference does an SSD actually make?',
        "On a machine still running a mechanical hard drive, it's usually the single most noticeable improvement available — startup, file opening and general responsiveness. It's frequently the "
        'cheapest fix in the building.'),
    (   'Can you assess our whole fleet?',
        "Yes, and it's the more useful engagement. You get every machine listed with its specification, age, warranty status and a recommendation, plus a replacement schedule so renewal becomes a "
        'budget line rather than an emergency.'),
    ("Will you tell us if we shouldn't spend the money?", 'Yes. Losing an upgrade sale is cheaper than having a client spend $300 on a machine that fails six months later.'),
    ('Do you do this for home computers?', 'No. bcom ICT works on business machines and office fleets.')]

PAGE = {
    "path": '/performance-optimisation-gold-coast',
    "priority": '0.75',
    "service": 'Business Computer Performance Optimisation',
    "title": 'Business Computer Performance & Fleet Assessment Gold Coast | bcom ICT',
    "description": "Slow business computers cost billable hours. bcom ICT assesses your Gold Coast office fleet, upgrades what's worth upgrading and says honestly when replacement is cheaper.",
    "hero_img": 'hero-bg-performance-optimisation.webp',
    "hero_alt": 'A bcom ICT technician assessing business computer performance at a Gold Coast office',
    "h1": 'Slow machines are a payroll problem',
    "lede": 'Ten minutes a day lost to a slow computer is about a week a year, per person. Usually the cheapest problem in the building to fix — sometimes by replacing rather than repairing.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Fleet assessed, not guessed', 'Honest upgrade advice', 'Costed against payroll', 'Business machines only'],
    "crumbs": [('Services', '/services'), ('Business Computer Repair', '/on-site-computer-repair-gold-coast'), ('Performance Optimisation', '/performance-optimisation-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT assesses business computer fleets across the Gold Coast, identifying why machines are slow and recommending whether to upgrade or replace each one. Common fixes include SSD and memory upgrades, startup and software clean-up, and identifying machines beyond economic repair. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Ten minutes a day, per person',
                                         None,
                                         'Waiting for a machine to start, for a file to open, for an '
                                         'application to respond. Ten minutes daily is roughly a working '
                                         'week per person per year — at what your staff cost, against a '
                                         'few hundred dollars of hardware.'),
                                 (       'People stop doing things properly',
                                         None,
                                         'When a system is slow, people avoid it. They keep files locally '
                                         'instead of on the server, skip restarts so updates never apply, '
                                         'and work around processes. Slow machines create security and '
                                         'process problems, not just annoyance.'),
                                 (       "It's usually one thing",
                                         None,
                                         'A mechanical hard drive in a machine that should have an SSD '
                                         'accounts for the majority of what we find. It is a cheap fix '
                                         'with a dramatic result.'),
                                 (       'Sometimes the answer is replace',
                                         None,
                                         'Beyond a certain age, upgrading is money spent on borrowed time. '
                                         'We would rather tell you that than sell you memory for a machine '
                                         'with a year left.')],
                'cols': 2,
                'eyebrow': "Why it's worth doing",
                'h2': 'Do the arithmetic before you dismiss it',
                'icon': False,
                'sub': 'This is one of the few IT problems where the business case is easy to calculate.'},
        {       'h2': 'What an assessment covers',
                'ticks': [       "Every machine's specification, age and warranty status, recorded in one "
                                 'list',
                                 "What's actually causing slowness on each — storage, memory, software, or "
                                 'the machine simply being past it',
                                 'Whether an SSD or memory upgrade is worth doing, per machine, with the '
                                 'cost against it',
                                 'Which machines are beyond economic upgrade and should be replaced, and '
                                 'when',
                                 'Startup programs, accumulated software and background processes cleaned '
                                 'up',
                                 'A replacement schedule so the fleet renews in a planned way rather than '
                                 'all at once']},
        {       'h2': 'Planned replacement beats emergency replacement',
                'html': '<p style="max-width:68ch">Most businesses replace computers when they die, which '
                        'means unbudgeted spending at the worst possible moment and someone unable to work '
                        'while it is sorted out.</p><p style="max-width:68ch;margin-top:16px">A fleet '
                        'assessment turns that into a schedule — a few machines a year, budgeted, ordered '
                        'and configured in advance. It costs the same money and removes the surprise. '
                        'Where replacement is the call, we source at trade pricing and hand the machine '
                        'over ready to use; see <a href="/hardware-procurement-setup-gold-coast">hardware '
                        'procurement and setup</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('Business Computer Repair', '/on-site-computer-repair-gold-coast'),
        ('Windows & macOS Repair', '/os-troubleshooting-repair-gold-coast'),
        ('Troubleshooting', '/hardware-software-troubleshooting-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast')])
            + cta('How much is slow costing you?', "We'll assess the fleet and put a number against it — including which machines aren't worth spending anything on."),
}

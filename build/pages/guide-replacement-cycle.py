from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;It still works, so why replace it?&rdquo;",
     "a reasonable position that ignores what the machine costs while it works. A computer does not have to fail to be expensive.",
     "Time the machine from power button to genuinely usable, multiply by the person using it, and compare that to a replacement. The arithmetic frequently settles an argument that opinion cannot."),
    ("&ldquo;We&rsquo;ll replace them when they die&rdquo;",
     "a strategy that guarantees every replacement happens at the worst possible moment, at retail prices, with someone idle while it is arranged.",
     "Replace on a schedule instead. The same machines get bought either way; the difference is whether they are budgeted or bought in a panic on a Tuesday morning."),
    ("&ldquo;They&rsquo;re only three years old&rdquo;",
     "age used as the sole measure. A well-specified three-year-old machine may have years left; a cheap one bought at retail may already be finished.",
     "Judge on what the machine is being asked to do rather than on its birthday. Replacement cycles are a planning tool, not a rule, and applying one blindly wastes money in both directions."),
    ("&ldquo;We&rsquo;ll just add more memory&rdquo;",
     "the familiar answer applied before a measurement. On older machines the constraint is usually storage rather than memory.",
     "Identify the actual bottleneck first. A solid state upgrade transforms a machine that more memory does nothing for, and it costs considerably less than a replacement."),
    ("&ldquo;Nobody told us it stopped getting updates&rdquo;",
     "an operating system past its supported life on hardware that cannot take the current one. Nothing announces this and the machine keeps working perfectly.",
     "Check what is still receiving security updates. This is the one condition that turns replace-when-convenient into replace-now, and it is invisible from the desk."),
    ("&ldquo;We&rsquo;ve no idea how old any of these machines are&rdquo;",
     "no asset register, so age, specification, warranty and holder all live in individual memories.",
     "Build the register. It converts replacement from a series of surprises into a forecast, and tells you instantly whether a failed machine is still under warranty."),
]

EXAMPLE_1 = example(
    "Nine machines that were told they were fine",
    "A business asked for a quote to replace eleven computers, having concluded from staff complaints that the fleet was finished. It expected a proposal for eleven machines.",
    "Nine were four years old, well specified and already running solid state storage. Their problem was a security product configured to scan every file access in real time with no exclusions for the database the business used all day. Two machines genuinely were finished &mdash; older, considerably weaker, and past economic repair.",
    "Configured appropriate exclusions without weakening the security product&rsquo;s coverage, cleaned up startup items across the fleet, and quoted for the two machines that actually needed replacing.",
    "Nine machines stayed in service and remain there. A quote for two instead of eleven is the version of this conversation that keeps a client rather than closes a sale.")

EXAMPLE_2 = example(
    "The two machines nobody knew were unsupported",
    "A business with thirty staff had no record of what it owned. Machines were replaced on failure and purchasing was reactive. The finance director could not forecast technology spend at all.",
    "Building an asset register found machines spanning eight model years and five manufacturers, eleven still under warranty that nobody had realised, and two running an operating system that had stopped receiving security updates over a year earlier. Two previously failed machines had been replaced at retail prices while under warranty, because nobody had checked.",
    "Recorded the fleet with age, specification, warranty status and holder, prioritised the two unsupported machines, set a replacement horizon for the rest, and standardised future purchases onto two models covering the two kinds of work in the business.",
    "Technology spend became a forecast rather than a sequence of surprises. The warranty claims alone recovered more than the register cost to build.")

FAQS = [   (   'How long should a business computer last?',
        'Typically three to five years depending on the work it does — four to five for office and admin machines, three to four for design or CAD workstations, and two to three for field laptops '
        'and tablets. The practical tests are whether it still receives operating system security updates, whether a repair would cost more than a third of replacement, and whether it will still be '
        'adequate in two years.'),
    (   'Is it worth upgrading an old computer instead of replacing it?',
        'Often, up to about four years old. Fitting an SSD to a machine still running a mechanical hard drive is the single most transformative upgrade available and costs a fraction of replacement. '
        'Beyond about five years, or on a machine out of operating system support, upgrading is money spent on borrowed time.'),
    (   'What happens if we keep using an unsupported operating system?',
        "It stops receiving security updates, which makes it a standing liability regardless of how well it runs. It's also increasingly a question on cyber insurance renewal forms and supplier "
        'security questionnaires, where the honest answer costs you.'),
    (   'How do we budget for computer replacement?',
        'Replace a proportion of the fleet each year rather than all of it when things fail. A fifteen-machine business on a five-year cycle replaces about three a year — the same total spend, but '
        'as a budget line rather than an emergency. A fleet assessment produces the schedule.'),
    (   'Should we buy business-grade or consumer computers?',
        'Business ranges for anything a person depends on. Longer warranties, on-site service options and standardised parts matter when a failure would otherwise leave someone without a machine for '
        'a fortnight. The retail saving usually disappears on the first failure.'),
    (   'Do we still need to replace our server?',
        "Often not. Many businesses assuming they need a new server would be better retiring it and moving file storage and applications to cloud. That's worth assessing before quoting hardware — "
        "it's frequently the cheaper answer.")]

PAGE = {
    "path": '/business-computer-replacement-cycle',
    "priority": '0.7',
    "article": True,
    "title": 'When Should a Business Replace Its Computers? | bcom ICT',
    "description": 'How long business computers should last, when repairing stops being worth it, and how to turn replacement into a budgeted schedule rather than a series of emergencies.',
    "hero_kind": 'doc',
    "eyebrow": "Guide",
    "h1": 'When is a business computer past it?',
    "lede": "Most businesses replace computers when they die. That's the most expensive way to do it — unbudgeted, at the worst moment, with someone unable to work while it's sorted.",
    "crumbs": [("Guides", "/services"), ('Computer replacement cycle', '/business-computer-replacement-cycle')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='Business computers typically remain economic for three to five years, depending on the work they do. The practical test is whether a repair costs more than a third of replacement, whether the machine will still be adequate in two years, and whether it is still receiving operating system security updates. Planned replacement on a schedule costs the same as emergency replacement and removes the disruption.',
                     blocks=[       {       'cards': [       (       'Is it still getting security updates?',
                                         None,
                                         'This is the hard line rather than a judgement call. A machine on '
                                         'an operating system no longer receiving security updates is a '
                                         'liability regardless of how well it runs, and it will show up on '
                                         "an insurer's questionnaire."),
                                 (       'Does the repair cost more than a third of replacement?',
                                         None,
                                         'A rough but reliable rule. A $400 screen on a $1,400 laptop '
                                         "that's four years old is usually money spent on borrowed time."),
                                 (       'Will it still be adequate in two years?',
                                         None,
                                         "Not just today. If it's already struggling with what the person "
                                         'does now, fixing it buys months rather than years.'),
                                 (       'How much time is it costing?',
                                         None,
                                         'Ten minutes a day lost to a slow machine is roughly a working '
                                         'week a year, per person. Against what your staff cost, that '
                                         'maths usually settles it quickly.')],
                'cols': 2,
                'eyebrow': 'The test',
                'h2': 'Four questions that settle it',
                'icon': False},
        {       'h2': 'Realistic lifespans',
                'html': '<div class="tablewrap"><table><thead><tr><th>Role</th><th>Typical economic '
                        'life</th><th>Why</th></tr></thead><tbody><tr><td class="slot">Office / admin '
                        'laptop</td><td>4–5 years</td><td>Light workload. Usually limited by battery and '
                        'operating system support rather than performance.</td></tr><tr><td '
                        'class="slot">Reception / point of sale</td><td>4–5 years</td><td>Undemanding '
                        'work, but downtime is highly visible — worth replacing before failure rather than '
                        'after.</td></tr><tr><td class="slot">Design, CAD or video workstation</td><td>3–4 '
                        'years</td><td>Software requirements move fastest here. Often replaced for '
                        'capability rather than failure.</td></tr><tr><td class="slot">Field laptop or '
                        'tablet</td><td>2–3 years</td><td>Dropped, wet, left in hot vehicles. Physical '
                        'life is the constraint, not performance.</td></tr><tr><td '
                        'class="slot">Server</td><td>5 years, then reassess</td><td>Warranty expiry is '
                        'usually the trigger. Many businesses replacing a server would be better retiring '
                        'it to cloud instead.</td></tr></tbody></table></div><p '
                        'style="max-width:68ch;margin-top:20px">These are guides, not rules. A '
                        'well-specified machine doing light work often exceeds them comfortably — the '
                        'questions above matter more than the age.</p>'},
        {       'h2': 'When an upgrade beats replacement',
                'ticks': [       '<strong>A mechanical hard drive in a machine under four years '
                                 'old.</strong> Fitting an SSD is the single most transformative upgrade '
                                 'available and costs a fraction of replacement.',
                                 '<strong>Insufficient memory on an otherwise sound machine.</strong> '
                                 'Cheap, quick, and often the difference between frustrating and fine.',
                                 "<strong>A failed battery on a laptop you'd otherwise keep.</strong> "
                                 'Straightforward on business ranges, less so on consumer ones.',
                                 '<strong>Not worth it:</strong> upgrading anything past about five years, '
                                 "or a machine already out of operating system support. That's money spent "
                                 'on borrowed time.']},
        {       'h2': 'Turning it into a schedule',
                'html': '<p style="max-width:68ch">The useful shift is replacing a proportion of the fleet '
                        'each year rather than all of it when things start failing. For a fifteen-machine '
                        "business on a five-year cycle, that's roughly three machines a year — a budget "
                        'line rather than a surprise.</p><p style="max-width:68ch;margin-top:16px">It '
                        'costs the same money. What it removes is the unbudgeted spend at the worst '
                        "moment, and someone sitting idle while it's dealt with. A <a "
                        'href="/performance-optimisation-gold-coast">fleet assessment</a> produces the '
                        'schedule — every machine listed with age, specification, warranty status and a '
                        'recommendation.</p><p style="max-width:68ch;margin-top:16px">Where replacement is '
                        'the call, buying business-grade rather than retail matters more than the saving '
                        'suggests: longer warranties, on-site service options and standardised parts. See '
                        '<a href="/hardware-procurement-setup-gold-coast">hardware procurement and '
                        'setup</a>.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What people get wrong about replacement</h2>
      <p>Six positions that cost money, in both directions.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in practice</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([('Windows Server Migration', '/windows-server-migration-gold-coast'),
               ('Performance Optimisation', '/performance-optimisation-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('Business Computer Repair', '/on-site-computer-repair-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('What IT support costs', '/it-support-cost-gold-coast')])
            + cta('Machines starting to fail one by one?', 'A fleet assessment turns that into a schedule — same money, none of the surprises.'),
}

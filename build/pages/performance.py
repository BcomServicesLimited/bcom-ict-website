from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;It takes fifteen minutes to be usable in the morning&rdquo;",
     "everything starting at once &mdash; the operating system, the security software, the sync client and whatever else was installed over the years and set to launch at login.",
     "Measure what is actually running at startup and remove what nobody needs. This is usually free and frequently returns most of the fifteen minutes, which is worth doing before anyone quotes for hardware."),
    ("&ldquo;It slows down through the day and a restart fixes it&rdquo;",
     "an application leaking memory, or a machine with too little to begin with for the number of things now open on it.",
     "Watch memory over a working day rather than at a single moment. A pattern that resets on restart points at consumption rather than capacity, and the two have very different fixes."),
    ("&ldquo;We added more memory and it made no difference&rdquo;",
     "the wrong bottleneck. Memory was upgraded because that is the familiar answer, when the constraint was a mechanical hard drive the whole time.",
     "Identify the actual constraint before spending. On machines more than about five years old the storage is the usual culprit, and moving to solid state transforms them where more memory does nothing."),
    ("&ldquo;Only one program is slow&rdquo;",
     "not the machine. A single slow application points at that application, its data file, or the path between it and its server.",
     "Test the same application on another machine. If it is slow everywhere, the machine is exonerated and the investigation moves somewhere far more productive."),
    ("&ldquo;It&rsquo;s fine until the browser is open&rdquo;",
     "browser tabs and extensions, which consume more than almost anything else on a modern machine. Forty open tabs is a genuine workload.",
     "Look at what the browser is carrying before condemning the hardware. Some of this is habit and some is a legitimate need for more memory, but the diagnosis has to come first."),
    ("&ldquo;It was fine when we bought it&rdquo;",
     "accumulation. Nothing broke &mdash; the machine has three more security agents, two sync clients and six years of software on it than it did when it was fast.",
     "Assess whether the machine is recoverable or genuinely finished, and say which. We would rather tell you a machine has years left than sell a replacement it does not need."),
]

EXAMPLE_1 = example(
    "Twelve minutes a day, fourteen people, and the arithmetic that followed",
    "A business asked us to look at machines that staff described as slow. The owner was sceptical, viewing it as people complaining about something unavoidable, and was reluctant to spend on it.",
    "Timed from power button to genuinely usable, the worst six machines averaged just over twelve minutes each morning, plus repeated pauses through the day. Fourteen staff at that rate came to roughly forty hours a month of people waiting &mdash; considerably more than the cost of fixing it, and entirely invisible because it was spread thinly across every day.",
    "Cleaned up startup on every machine, which recovered several minutes for free, then replaced the storage in the six worst with solid state drives rather than replacing the machines.",
    "Startup went from twelve minutes to under one. The hardware spend was a fraction of a replacement cycle, and the owner&rsquo;s scepticism was reasonable until somebody put a number against it.")

EXAMPLE_2 = example(
    "More memory, twice, for a problem memory could not fix",
    "A business had upgraded memory on four machines a year earlier on a previous provider&rsquo;s recommendation, seen no improvement, and been advised to upgrade the memory again.",
    "The machines had ample memory and were never running short of it. All four had original mechanical hard drives approaching seven years old, and the drives were saturated whenever the machines were asked to do anything. Adding memory to a machine waiting on its disk changes nothing, and doing it twice changes nothing twice.",
    "Moved all four to solid state storage, transferred the installations rather than rebuilding them, and returned each machine the same day.",
    "The machines are quick and remain in service. The business had spent twice on a component that was never the constraint, which is what happens when a familiar answer is applied before a measurement.")

EXAMPLE_3 = example(
    "Telling a business its machines were fine",
    "A business asked for a quote to replace eleven computers, having concluded from staff complaints that the fleet was at the end of its life. The expectation was a proposal for eleven machines.",
    "Nine of the eleven were four years old, well specified, and already running solid state storage. Their problem was a security product configured to scan every file access in real time with no exclusions for the database the business used all day. Two machines genuinely were finished, being older and considerably weaker than the rest.",
    "Configured appropriate exclusions on the security product without weakening its coverage, cleaned up startup items, and quoted for the two machines that actually needed replacing.",
    "Nine machines stayed in service and are still in service. We wrote a quote for two instead of eleven, which is the version of this conversation that keeps a client rather than a sale.")
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
    "title": "Computer Performance Optimisation Gold Coast | bcom ICT",
    "description": "Slow business computers cost billable hours. Fleet assessment, clean-up and SSD upgrades on the Gold Coast — or an honest answer that a machine is finished.",
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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The performance complaints we are actually called to</h2>
      <p>A slow machine is a payroll cost. Six causes account for nearly all of it, and half are fixable for nothing.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a performance assessment looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('Business Computer Repair', '/on-site-computer-repair-gold-coast'),
        ('Windows & macOS Repair', '/os-troubleshooting-repair-gold-coast'),
        ('Troubleshooting', '/hardware-software-troubleshooting-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast')])
            + cta('How much is slow costing you?', "We'll assess the fleet and put a number against it — including which machines aren't worth spending anything on."),
}

from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;It installed but it won&rsquo;t run&rdquo;",
     "a missing prerequisite, a permission the installer needed and did not have, or security software blocking a component quietly.",
     "Check what the application actually requires and what is stopping it, rather than reinstalling in the hope of a different outcome. The second install fails for the same reason as the first."),
    ("&ldquo;It works for one person and not the others&rdquo;",
     "an installation done under one user&rsquo;s account rather than for the machine, or a licence assigned to an individual instead of a device.",
     "Install for all users where the software supports it, and check how the vendor actually licenses it. This is the most common reason a rollout stalls after the first desk."),
    ("&ldquo;Our line-of-business software won&rsquo;t run on the new machines&rdquo;",
     "an older application meeting a newer operating system. Industry-specific software often lags well behind, and the vendor may or may not have a supported version.",
     "Establish the vendor&rsquo;s supported position before the machines are bought. There is usually a path &mdash; an update, a compatibility setting, or hosting it centrally &mdash; but it needs to be chosen deliberately."),
    ("&ldquo;An update broke the integration&rdquo;",
     "two products updating on independent schedules. The connection between an accounting package and something that feeds it is a frequent casualty.",
     "Test updates against the integrations that matter before they roll out everywhere. Knowing which pairings are fragile is most of the work, and it comes from documentation rather than memory."),
    ("&ldquo;Everyone installs whatever they like&rdquo;",
     "no standard and no control over what runs on business machines. It is how unlicensed software and genuinely unpleasant things arrive.",
     "Agree what is standard, deploy it consistently, and control what else can be installed. This is about supportability as much as security &mdash; a fleet with a known configuration is one that can be fixed."),
    ("&ldquo;We&rsquo;re not sure we&rsquo;re licensed properly&rdquo;",
     "software installed over years without records. Frequently the business is over-licensed in one place and under-licensed in another.",
     "Reconcile what is installed against what is owned. Discovering a shortfall yourself is a purchase; discovering it during a vendor audit is a purchase plus a penalty. The reconciliation is unglamorous and rarely takes more than a day, and it is worth doing before a vendor decides to do it for you."),
]

EXAMPLE_1 = example(
    "The rollout that stopped at the second desk",
    "A business bought a design application for six staff. It was installed on the first machine, worked perfectly, and then failed on every subsequent one. Two weeks later, five people were still without it.",
    "The first installation had been done while signed in as the person who sat at that machine, which installed it into that user&rsquo;s profile rather than for the machine. The licences had also been assigned to named individuals in the vendor portal in a different order to the way the machines had been allocated, so two people held licences for software they did not have and two had software with no licence.",
    "Removed and redeployed the application properly for all users on each machine, reconciled the licence assignments against who was actually using it, and documented the process so the next hire takes twenty minutes.",
    "All six were working the same afternoon. Nothing had been wrong with the software or the licences &mdash; only with how the first installation had been performed, which then set the pattern.")

EXAMPLE_2 = example(
    "The update that quietly stopped the invoices",
    "A wholesaler found that invoices raised in their industry software had stopped appearing in their accounting package. The problem was noticed at month end, by which point about three weeks of transactions had accumulated.",
    "The accounting package had applied an update eleven days earlier that changed how it authenticated connected applications. The industry software still believed it was connected and reported no error. Data had been queuing at one end and silently discarded at the other.",
    "Restored the connection on the current authentication method, reconciled and re-transmitted the missing transactions, then documented which integrations existed and set monitoring to alert on a failed sync rather than relying on month end.",
    "Month end completed on time. The integration had been in place for four years and had never been recorded anywhere, which is why nothing checked it and nothing noticed.")

EXAMPLE_3 = example(
    "A licence audit the business ran on itself first",
    "A business received notice of a software licence review from a major vendor. It had been buying licences for over a decade with no central record, and the directors had no idea whether they were compliant.",
    "Reconciling what was installed against what had been purchased found the business over-licensed on one product by fourteen seats &mdash; bought during a period of expected growth that did not happen, and never reduced &mdash; and under-licensed on another by six, because a department had installed a product from a shared download without anyone raising a purchase. The two roughly cancelled financially, but they are entirely separate positions to a vendor: one is wasted money and the other is a compliance exposure with a penalty attached.",
    "Purchased the six licences before responding to the review, released the fourteen at the next renewal, and built a record of what is installed against what is owned so the position can be answered at any time rather than reconstructed under a deadline.",
    "The review was answered accurately and closed without incident. Finding a shortfall yourself is a purchase; being found to have one is a purchase plus a penalty, and the difference between those two outcomes was about three weeks of notice.")
FAQS = [   (   'Can you install our business software on new machines?',
        "Yes. bcom ICT installs and configures business applications consistently across machines, handles licensing and activation, and records what's licensed to whom in an asset register you "
        'keep. New machines can be imaged and delivered ready to use.'),
    (   "We don't know what software licences we have. Can you help?",
        "Yes, and it's a common starting point. An audit establishes what's installed, what's licensed, what's being paid for and used, and what's being paid for and not. It frequently pays for "
        'itself in cancelled subscriptions.'),
    (   'An update broke our software. Can you fix it?',
        'Usually. Windows feature updates commonly break drivers, printers and older business applications. The fix is often rolling back a specific component rather than the whole update — and '
        "where an application is genuinely incompatible, we'll tell you what your real options are."),
    ('Do you supply software licences?', "We can source business licensing, or work with what you buy directly. Either is fine, and we'll tell you when you're on a tier above what you need.")]

PAGE = {
    "path": '/software-installation-configuration-gold-coast',
    "priority": '0.65',
    "title": "Software Installation & Configuration | bcom ICT",
    "description": "Business software installed, licensed and actually working across your Gold Coast fleet — deployment, compatibility, integrations and licence reconciliation.",
    "hero_img": 'hero-bg-software-installation.webp',
    "hero_alt": 'Business software being installed and configured by bcom ICT on the Gold Coast',
    "h1": 'Software installed and actually working',
    "lede": 'Deployed consistently across machines, licensed properly, and recorded — so nobody discovers a renewal by being locked out of it.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Consistent deployment', 'Licensing recorded', 'Activation handled', 'Documented'],
    "crumbs": [('Services', '/services'), ('Business Computer Repair', '/on-site-computer-repair-gold-coast'), ('Software Installation', '/software-installation-configuration-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT installs, licenses and configures business software across the Gold Coast — deploying consistently across machines, handling activation, and recording licences in an asset register so renewals and entitlements stay visible. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Every machine is slightly different',
                                         None,
                                         'Installed ad hoc over years, different versions, different '
                                         'settings. Then a fault affects one person and nobody can work '
                                         "out why — because their machine isn't like anyone else's."),
                                 (       "Nobody knows what's licensed",
                                         None,
                                         'Renewals arrive as a surprise, or worse, someone is locked out '
                                         "mid-job. An asset register recording what's licensed to whom "
                                         'removes both.'),
                                 (       'Paying for what nobody uses',
                                         None,
                                         'Subscriptions for departed staff, duplicate tools doing the same '
                                         "job, licence tiers well above what's needed. Reviewing this "
                                         'frequently pays for the work.'),
                                 (       'Updates break things',
                                         None,
                                         'An update to one application breaks another, or a '
                                         'line-of-business tool stops working after a Windows feature '
                                         'update. Predictable, and manageable if someone is watching.')],
                'cols': 2,
                'eyebrow': 'What goes wrong',
                'h2': 'Four recurring software problems',
                'icon': False},
        {       'h2': 'What we do',
                'ticks': [       'Install and configure business applications consistently across machines '
                                 'rather than one at a time',
                                 'Handle licensing and activation, including transfers when hardware is '
                                 'replaced',
                                 "Record what's licensed to whom, with renewal dates, in an asset register "
                                 'you keep',
                                 'Review subscriptions for duplication and licences nobody uses',
                                 'Set up new starters with the same software their role needs, rather than '
                                 'working it out each time',
                                 'Test line-of-business applications after major updates rather than '
                                 'waiting for someone to report a fault']}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The software problems we are actually called to</h2>
      <p>Six recurring problems, and the most expensive of them is the one that fails silently.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a software rollout looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business Computer Repair', '/on-site-computer-repair-gold-coast'),
        ('Windows & macOS Repair', '/os-troubleshooting-repair-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('Software Recommendations', '/software-recommendations-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta("Not sure what you're paying for?", 'A licensing review usually finds subscriptions nobody uses — often enough to cover the work itself.'),
}

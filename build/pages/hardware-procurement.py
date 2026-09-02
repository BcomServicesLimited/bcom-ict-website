from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We bought laptops and they arrived as bare machines&rdquo;",
     "hardware bought as a product rather than as a working desk. Somebody still has to spend two hours on each one, and it usually falls to whoever is least able to refuse.",
     "Have machines arrive configured, joined, secured and carrying the person&rsquo;s data. The purchase is the small part; the setup is where the time and the mistakes live."),
    ("&ldquo;The cheap machines cost us more&rdquo;",
     "consumer hardware in a business. Retail models are built to a price with shorter warranties, slower support and parts that are frequently not available to a business at all.",
     "Buy business-grade with next-business-day support where downtime matters. The premium is modest and the difference appears the first time a machine fails on a Tuesday morning."),
    ("&ldquo;Every machine is different&rdquo;",
     "years of buying whatever was available when something died. Every fault becomes bespoke and no fix applies twice.",
     "Standardise on a small number of models. Fleets that look alike are dramatically cheaper to support, and it costs nothing to start being consistent from the next purchase onwards."),
    ("&ldquo;Nobody knows what we own&rdquo;",
     "no asset register. Warranty status, age, specification and who has what all live in individual memories.",
     "Build the register once and maintain it. It turns replacement into a forecast, tells you instantly whether a failed machine is under warranty, and is the first thing an insurer asks for after a break-in."),
    ("&ldquo;The new machine can&rsquo;t run our main software&rdquo;",
     "a specification chosen on general advice rather than against the software the business actually depends on. Industry-specific applications have real requirements and are rarely consulted.",
     "Check the requirements of the software that matters before ordering. This takes ten minutes and prevents the most expensive kind of purchasing mistake."),
    ("&ldquo;We&rsquo;re not sure whether to buy or lease&rdquo;",
     "a genuine question with no universal answer. It depends on cash flow, replacement cycle and how your accountant prefers to treat it.",
     "Get the arithmetic laid out both ways and decide with your accountant. We have no financing product to sell, so our view on this costs you nothing either way."),
]

EXAMPLE_1 = example(
    "Fourteen laptops, four days of unpacking",
    "A business bought fourteen laptops directly from a retailer to save on a quoted supply price. They arrived on a Thursday and were expected to be in use by Monday.",
    "Each machine needed the consumer software removed, the operating system updated, the business tenancy joined, security configured, printers added and the user&rsquo;s data transferred. That is close to two hours a machine done carefully. The task fell to the office manager, who lost most of a week to it and had no way to verify that the security configuration was consistent between machines.",
    "Took over the remaining machines, built a standard configuration once and applied it to all of them, then audited the ones already deployed &mdash; four of which had been set up differently, including two with no encryption enabled.",
    "The saving on the purchase price was substantially less than the week of the office manager&rsquo;s time it consumed, before counting the four machines that had to be revisited.")

EXAMPLE_2 = example(
    "Knowing which machines fail next year",
    "A business of thirty staff had no record of what it owned. Machines were replaced when they died, purchasing was reactive, and the finance director could not forecast technology spend with any confidence.",
    "Building an asset register found machines spanning eight model years and five manufacturers, eleven still under warranty that nobody had realised, and three running an operating system no longer receiving security updates. Two failed machines had been replaced at retail prices while under warranty.",
    "Recorded the fleet with age, specification, warranty status and holder, set a replacement horizon, and standardised the next purchases onto two models covering the two kinds of work in the business.",
    "Technology spend became a forecast instead of a series of surprises. The warranty claims alone recovered more than the register cost to build.")

EXAMPLE_3 = example(
    "Checking the software requirements before ordering, not after",
    "An engineering firm was about to order six workstations chosen on general specifications and a good price. The order was ready to place and we were asked only to arrange the setup.",
    "The firm&rsquo;s modelling software published requirements the proposed machines did not meet &mdash; specifically for the graphics component, which the retailer&rsquo;s specification described in marketing terms rather than by model. Two of the six were intended for staff who did not use that software at all and were perfectly adequate for their actual work.",
    "Checked the vendor&rsquo;s stated requirements against the exact components, revised the four workstations to hardware the software supports, and left the other two as originally specified because they were correctly matched to the job.",
    "Six machines that all do the work asked of them, and only four carried the higher cost. The ten minutes spent reading the software vendor&rsquo;s requirements page was the whole intervention.")
FAQS = [   (   'Can you supply business computers on the Gold Coast?',
        'Yes. bcom ICT sources laptops, desktops, servers, switches, monitors and peripherals at trade pricing, then images and configures them before delivery so staff can work immediately. '
        'Replaced machines are securely wiped. Call 07 3041 8993.'),
    (   'Do you mark up hardware?',
        "We source at trade pricing and are transparent about what we charge over it. If you'd prefer to buy the hardware yourself and have us configure and deploy it, that's fine — and we'll still "
        'advise on what to buy.'),
    (   'Should we buy business-grade or is retail fine?',
        'Business ranges carry longer warranties, on-site service options and standardised parts, which matters when a failure would otherwise leave someone without a machine for a fortnight. For a '
        'business, the retail saving usually evaporates on the first failure.'),
    (   'What happens to our old machines?',
        "Data is migrated first, then the drive is securely wiped before the machine is disposed of or redeployed. A traded-in machine with recoverable client data on it is a genuine risk, and it's "
        'an easy one to avoid.'),
    (   'Do we still need a server?',
        "Often not. Many small businesses that assume they need to replace a server would be better moving to cloud file storage and retiring it. We'll tell you which applies rather than quoting a "
        'replacement by default.'),
    (   'How long does it take to get machines set up?',
        'Usually a few days from delivery to deployment for a small batch, most of which is us configuring rather than you waiting. Machines arrive at your office ready to use.')]

PAGE = {
    "path": '/hardware-procurement-setup-gold-coast',
    "priority": '0.75',
    "service": 'Hardware Procurement & Setup Gold Coast',
    "title": 'Business Hardware Procurement & Setup Gold Coast | bcom ICT',
    "description": 'Business hardware supply and setup on the Gold Coast — laptops, desktops, servers, switches and monitors at trade pricing, imaged, configured and deployed ready to use.',
    "hero_img": 'hardware-procurement-setup-gold-coast-hero.webp',
    "hero_alt": 'New business computers being configured by bcom ICT before deployment to a Gold Coast client',
    "h1": 'Delivered configured, not delivered in a box',
    "lede": "Sourced at trade pricing, imaged, joined to your systems and set up with the person's own files and email — so day one is working, not waiting.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Trade pricing', 'Configured before delivery', 'Business-grade warranty', 'Old machines wiped'],
    "crumbs": [('Services', '/services'), ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT sources and configures business hardware for Gold Coast businesses — laptops, desktops, servers, switches and monitors — at trade pricing, then images, configures and deploys them ready for staff to use. Replaced machines are securely wiped and disposed of. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Specified for the work',
                                         None,
                                         'Not the cheapest model, and not the most expensive. What matters '
                                         'is what the person actually does — an accounts machine, a CAD '
                                         'workstation and a reception PC are three different purchases and '
                                         'one of them is not a $700 laptop.'),
                                 (       'Business-grade, not retail',
                                         None,
                                         'Business ranges carry longer warranties, on-site service options '
                                         'and standardised parts. The retail equivalent looks cheaper '
                                         'until a failure means a fortnight without a machine.'),
                                 (       'Configured before it arrives',
                                         None,
                                         'Imaged, joined to your systems, security settings applied, '
                                         "applications installed, printers and drives mapped. The user's "
                                         'files and email are already there when they sit down.'),
                                 (       'The old machine handled properly',
                                         None,
                                         'Data migrated, then the drive securely wiped before disposal or '
                                         'redeployment. A traded-in machine with recoverable client data '
                                         'on it is a breach waiting to be discovered.')],
                'cols': 2,
                'eyebrow': 'The difference',
                'h2': 'Buying the machine is the easy part',
                'icon': False,
                'sub': 'Anyone can order a laptop. What costs a business time is everything between '
                       'delivery and someone actually working on it.'},
        {       'h2': 'What we supply',
                'ticks': [       'Laptops, desktops and workstations, specified for the actual role',
                                 'Servers and storage, including whether you need one at all — often the '
                                 'honest answer is no',
                                 'Network switches and access points matched to your existing '
                                 'infrastructure',
                                 'Monitors, docks and peripherals, including the ergonomic side people '
                                 'forget until someone complains',
                                 'Microsoft 365 and software licensing, sized to what you use rather than '
                                 "what's bundled",
                                 'Warranty registration and asset tagging, added to the register you '
                                 'keep']},
        {       'h2': 'On pricing',
                'html': '<p style="max-width:68ch">We source at trade pricing and are open about what we '
                        'charge over it. If you would rather buy the hardware yourself and have us '
                        'configure and deploy it, that is a perfectly reasonable arrangement and some '
                        'clients do exactly that — we will still tell you what to buy.</p><p '
                        'style="max-width:68ch;margin-top:16px">Where several machines are due at once, a '
                        '<a href="/performance-optimisation-gold-coast">fleet assessment</a> is usually '
                        'the better starting point. It turns replacement into a planned schedule rather '
                        'than a series of emergencies, which costs the same money and removes the '
                        'surprise.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The procurement problems we are actually called to</h2>
      <p>Buying the machine is the cheap part. Six recurring problems sit around it.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What proper procurement looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([('Windows Server Migration', '/windows-server-migration-gold-coast'),
        ('Synology NAS', '/synology-nas-gold-coast'),
               ('Performance Optimisation', '/performance-optimisation-gold-coast'),
        ('Business Computer Repair', '/on-site-computer-repair-gold-coast'),
        ('Technology Procurement Advice', '/technology-procurement-advice-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast')])
            + cta('Machines due for replacement?', "We'll tell you what to buy for the work each person actually does — and deliver them configured rather than boxed."),
}

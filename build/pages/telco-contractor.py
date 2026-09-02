from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;Three suppliers and nobody owns the problem&rdquo;",
     "phones, cabling and internet each supplied by a different party. Every fault lands in the space between them, and each is being truthful when they say it is not theirs.",
     "Have one party responsible for the whole path. The technical work is rarely the difficult part &mdash; establishing whose problem it is consumes more of a business&rsquo;s time than fixing it does."),
    ("&ldquo;The cabling contractor and the phone provider are booked for different days&rdquo;",
     "no coordination. Each is doing exactly what they were engaged for, and the sequence they need to happen in was nobody&rsquo;s responsibility.",
     "Sequence the work as one job. Cabling before services, services before configuration, everything tested before people rely on it &mdash; this ordering is obvious and is very frequently not what happens."),
    ("&ldquo;Who is actually allowed to do this work?&rdquo;",
     "a fair question. Cabling connected to the telecommunications network must be installed by a registered cabler, and that is a legal requirement rather than a preference.",
     "bcom ICT engages ACMA registered cabling contractors for that work rather than doing it with internal staff. You get the compliance and the documentation, which matters for insurance and for a certifier."),
    ("&ldquo;Our services are still billed to the old address&rdquo;",
     "a move where the technology followed the business and the account records did not. It stays invisible until a fault needs the provider to identify the site.",
     "Reconcile the account records against reality. Businesses routinely pay for services at premises they left years ago, and discover it only when something breaks at the address the provider does not have."),
    ("&ldquo;Nobody knows what services we actually have&rdquo;",
     "years of additions with no consolidated record &mdash; lines that carry alarms, lifts or terminals nobody can identify.",
     "Build an inventory of every service and what depends on it. This is what stops an NBN migration disconnecting a lift phone, which happens more often than it should."),
    ("&ldquo;We&rsquo;re moving and everything has to work on day one&rdquo;",
     "not a fault, and the most common reason we are engaged for the whole scope rather than part of it.",
     "Plan the cabling, the services and the systems together with time built in. The lead times on services are the constraint, and they are the item most often discovered late."),
]

EXAMPLE_1 = example(
    "Four years of paying for a site they had left",
    "A business asked us to take over its telecommunications after years of dealing with several suppliers separately. The immediate request was a fault on a line, not a review.",
    "Reconciling the services against the premises found the business paying monthly for three services at an address it had vacated four years earlier. It was also paying for two lines at the current site that terminated nowhere identifiable. None of this had been visible, because the invoices were paid on a total rather than examined line by line, and each individual amount was small enough not to attract attention.",
    "Identified every service, established what each one actually carried, cancelled what was genuinely dead, and produced a written inventory recording what each remaining service does and what depends on it.",
    "Recurring spend fell immediately and permanently. The more useful outcome is the inventory &mdash; the business can now answer what a service does before disconnecting it, which is the failure mode that takes out lift phones and alarms.")

EXAMPLE_2 = example(
    "One job instead of three suppliers and a sequence nobody owned",
    "A business fitting out a new tenancy had engaged a cabling contractor, a phone provider and an internet provider separately, on the reasonable assumption that each knew its own work.",
    "Each did. Nobody owned the order they had to happen in. The internet service had been ordered with a lead time longer than the fit-out, the phone provider was scheduled to configure a system before the cabling it depended on existed, and the cabling contractor had been briefed on a desk layout that had since changed. All three were about to arrive and be unable to proceed.",
    "Took the whole scope as one job, re-sequenced it, brought the service order forward, updated the cabling brief to the current layout, and tested everything end to end before staff arrived.",
    "The business occupied on schedule. Nothing here was technically difficult &mdash; three competent suppliers had simply been engaged without anyone holding the sequence, which is the single most common way a fit-out runs late.")

EXAMPLE_3 = example(
    "The line that turned out to be holding up a fire panel",
    "A business preparing to migrate its remaining copper services to NBN asked us to confirm which services could safely be cancelled. Three lines were carrying no calls at all and looked like obvious candidates.",
    "One was genuinely dead and had been for years. The second was the monitored alarm dialler. The third terminated at a fire indicator panel in a shared services cupboard, and had been installed by the building rather than by the business &mdash; it appeared on the business&rsquo;s account because of an arrangement made with a previous tenant that nobody currently at either party could explain. Cancelling either of the two live services would have disabled monitored life-safety equipment, and neither showed any call traffic to suggest it was doing anything.",
    "Traced every service to what it physically terminates at before anything was cancelled, arranged the fire panel service properly with the building rather than the tenant, transitioned the alarm dialler onto a supported path, and cancelled only the one line that was genuinely dead.",
    "The migration went ahead without disabling anything. A service carrying no calls is not evidence that a service carries nothing, and that assumption is how monitored alarms and lift phones end up dead for years after an otherwise clean changeover.")
FAQS = [   (   'What does a telecommunications contractor do?',
        'Supplies and installs business phone systems, runs voice and data cabling, manages internet and NBN connections, and handles number porting. bcom ICT covers all of it on the Gold Coast, '
        'with cabling carried out by ACMA registered cabling contractors it engages and manages.'),
    (   'Is bcom ICT a registered cabler?',
        'No. Fixed cabling connected to the telecommunications network requires ACMA cabler registration, and bcom ICT does not hold it. Cabling work is carried out by ACMA registered contractors '
        'that bcom ICT engages and manages, with testing and certification documentation provided on completion.'),
    (   'Why use one contractor for phones, cabling and internet?',
        'Because voice quality depends on the connection, the network and the cabling as much as on the phone system. When those sit with three suppliers, a dropped-call fault becomes a three-week '
        'argument with you in the middle.'),
    (   'Do you sell internet or phone plans?',
        "We're not a reseller. We work with whatever provider you're with, which means our advice on whether the service is at fault isn't influenced by wanting to sell you a different one."),
    (   'Can you support our existing phone system?',
        'Very likely. We maintain LG Ericsson iPECS, Panasonic KX, NEC UNIVERGE and Alcatel-Lucent systems, including legacy platforms many providers have stopped servicing.')]

PAGE = {
    "path": '/telecommunications-contractor-gold-coast',
    "priority": '0.7',
    "title": "Telecommunications Contractor Gold Coast | bcom ICT",
    "description": "Business telecommunications on the Gold Coast — phone systems, voice and data cabling, NBN and internet, number porting and legacy PBX support.",
    "hero_img": 'phone-line-installation-hero.webp',
    "hero_alt": 'Telecommunications and cabling work carried out by bcom ICT for a Gold Coast business',
    "h1": 'One contractor for phones, cabling and connectivity',
    "lede": "Rather than a phone company, a cabler and an IT provider each blaming the other two when something doesn't work.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Phones, cabling & internet', 'Registered cablers engaged', 'Legacy PBX supported', 'One point of contact'],
    "crumbs": [('Services', '/services'), ('Telecommunications', '/telecommunications-contractor-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides business telecommunications services across the Gold Coast — phone system supply and installation, VoIP and legacy PBX support, voice and data cabling, NBN and business internet, and number porting. Cabling is carried out by ACMA registered cabling contractors that bcom ICT engages and manages. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'The problem this solves',
                'h2': 'Three suppliers, no accountability',
                'html': '<p style="max-width:68ch">The usual arrangement: a phone company sells the '
                        'system, a cabler runs the cabling, and an IT provider looks after the network. '
                        'When calls drop, each points at the other two and you become the project '
                        'manager.</p><p style="max-width:68ch;margin-top:16px">Voice quality depends on '
                        'the connection, the network configuration and the cabling as much as on the phone '
                        'system. Splitting those across suppliers is precisely why the fault takes three '
                        'weeks to resolve.</p>'},
        {       'h2': 'What we cover',
                'ticks': [       "<a href='/business-phone-systems-gold-coast'>Business phone systems</a> "
                                 '— supply, installation and support',
                                 "<a href='/voip-phone-system-installation-and-support-gold-coast'>Cloud "
                                 "VoIP</a> and <a href='/pabx-phone-systems-gold-coast'>on-premise "
                                 'PBX</a>, including legacy systems many providers no longer service',
                                 "<a href='/phone-line-installation-cabling-gold-coast'>Voice cabling</a> "
                                 "and <a href='/network-cabling-for-offices-gold-coast'>structured data "
                                 'cabling</a>, installed by ACMA registered cabling contractors',
                                 "<a href='/nbn-internet-support-gold-coast'>NBN and business internet</a> "
                                 '— faults, configuration, ISP escalation and 4G/5G failover',
                                 'Number porting, planned ahead of a cutover rather than attempted on the '
                                 'day',
                                 "<a href='/office-it-relocation-gold-coast'>Relocations</a> — moving the "
                                 'lot to a new site and testing it before Monday']},
        {       'h2': 'On cabling registration',
                'html': '<p style="max-width:68ch">Fixed cabling connected to the telecommunications '
                        'network legally requires ACMA cabler registration in Australia. <strong>bcom ICT '
                        'does not hold that registration.</strong> The cabling portion of any job is '
                        'carried out by ACMA registered cabling contractors that we engage and '
                        'manage.</p><p style="max-width:68ch;margin-top:16px">In practice you still deal '
                        'with one point of contact for the whole job and get testing and certification '
                        'documentation on completion. We would encourage you to ask any contractor to show '
                        'you their registration before work begins.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The problems we are actually called to as a single contractor</h2>
      <p>Six situations that come from work being split across suppliers rather than from any of them doing it badly.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a single contractor arrangement looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([('Business NBN guide', '/business-nbn-guide-gold-coast'),
               ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Office Network Cabling', '/network-cabling-for-offices-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast')])
            + cta('Tired of three suppliers blaming each other?', 'One number covers phones, cabling and connectivity — and the fault stops being your project to manage.'),
}

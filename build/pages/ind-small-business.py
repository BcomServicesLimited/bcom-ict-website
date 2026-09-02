from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;The person who set all this up has left&rdquo;",
     "an arrangement that depended on one person &mdash; often a family member, a former staff member or a contractor &mdash; and no documentation of any kind.",
     "Recover and document what exists before touching it: accounts, licences, domain, hosting, network layout. Almost every small business we take on starts here, and it is a day&rsquo;s work rather than a crisis."),
    ("&ldquo;Nobody knows the passwords&rdquo;",
     "credentials held in one person&rsquo;s memory, browser or notebook. The business functions perfectly until the day it needs to change something.",
     "Establish proper ownership of the domain, the Microsoft tenancy and the accounting file, then hold credentials in a password manager the business controls. Ownership of the domain is the one worth checking first, because losing it is the hardest to undo."),
    ("&ldquo;We all use the same login&rdquo;",
     "convenience, usually dating from when the business had three people. It removes any ability to say who did what, and it means a departure requires changing a password everyone relies on.",
     "Give every person their own account with multi-factor authentication. This is the single highest-value hour of work in most small businesses and it costs nothing beyond the time."),
    ("&ldquo;The computers are getting old but they still work&rdquo;",
     "machines past the point where repair is economic. They usually fail one at a time, at random, and each failure costs a day nobody planned for.",
     "Plan replacement rather than reacting to it. Knowing that three machines are due next financial year turns an emergency into a line in a budget, and lets you buy well rather than urgently."),
    ("&ldquo;We think the backup is working&rdquo;",
     "a backup nobody has ever restored from. Backups fail silently, and the failure is discovered at the worst possible moment.",
     "Test a restore. Not a report saying the backup completed &mdash; an actual file, recovered. A backup is only a backup once somebody has got something back out of it."),
    ("&ldquo;When something breaks we don&rsquo;t know who to call&rdquo;",
     "several suppliers with overlapping responsibilities and no agreement about who owns a problem. The internet provider, the software vendor and whoever built the website each point at the others.",
     "Have one number to call and let us deal with the rest. Most small business downtime is spent establishing whose problem it is rather than fixing it."),
]

EXAMPLE_1 = example(
    "The domain nobody in the business owned",
    "A small business of eleven people asked for help moving to Microsoft 365. Straightforward work, until the question of who controlled the domain name came up and nobody could answer it.",
    "The domain had been registered fourteen years earlier by a web designer who had built the original site and had not been engaged since. It was registered in that designer&rsquo;s own name, on their personal email address, with auto-renewal on a credit card that had long since expired. The business had no access to it whatsoever. Every email address the business used depended on a registration it did not own and could not renew.",
    "Traced the registrar, established contact with the original designer, who transferred it willingly once asked, and moved the domain into an account owned by the business with the renewal on the business&rsquo;s own card.",
    "The business now owns the thing its entire email identity rests on. Had that domain lapsed, the business would have lost every email address at once, and the recovery would have been a negotiation rather than an administrative task.")

EXAMPLE_2 = example(
    "Replacing computers on a plan instead of on a Tuesday",
    "A business with fourteen staff had machines ranging from two to nine years old, bought as needed and never tracked. Failures were becoming frequent enough to be disruptive, and each one meant somebody idle for a day and a rushed purchase at retail prices.",
    "Building an asset register found four machines past economic repair, three approaching it, and two already running an operating system no longer receiving security updates &mdash; which the business had not been told and had no way to know.",
    "Set out a replacement schedule over eighteen months prioritising the unsupported machines, sourced at trade pricing with the configuration and data transfer handled before each machine was handed over, and recorded the fleet so the next cycle could be forecast rather than discovered.",
    "Replacement is now a budgeted line rather than a series of emergencies. The business also spends less per machine, because nothing is being bought on the afternoon it died.")

FAQS = [   (   'What size business does bcom ICT work with?',
        'Most clients have between three and sixty staff — businesses too large to keep muddling through and too small to justify a full-time IT employee. bcom ICT has supported Gold Coast small '
        'businesses since 2011, on-site across the Gold Coast and remotely Australia-wide. Call 07 3041 8993.'),
    (   'How much does small business IT support cost?',
        'Ad-hoc support is $190 + GST per hour ($209.00 inc GST), plus a $100 + GST call-out for on-site work. Managed IT is a flat monthly fee calculated from your business requirements and the '
        'services included, quoted after a free review and month-to-month with no lock-in.'),
    (   "We've got someone in the office who handles IT. Is that a problem?",
        'Not necessarily, and plenty of clients keep that arrangement with us behind it — they handle day-to-day questions, we handle infrastructure, security and escalations. It becomes a problem '
        'when the business depends on one person, nothing is documented, and that person could resign.'),
    (   "What's the first thing we should sort out?",
        "Backups you've actually seen restore, and multi-factor authentication on every account. Between them they cover most of what genuinely damages small businesses, and neither is expensive."),
    (   'Do we have to commit to anything?',
        'No. The first conversation and the systems review are free, and you keep the written report either way. Managed agreements are month-to-month with no exit fee.'),
    (   "Will you tell us if we don't need you?",
        'Yes, and it happens. Sometimes the review concludes that ad-hoc support is enough for now, or that your existing provider is doing a reasonable job and the problem is communication rather '
        'than competence.')]

PAGE = {
    "path": '/it-support-small-business-gold-coast',
    "priority": '0.8',
    "title": 'Small Business IT Support Gold Coast | bcom ICT',
    "description": 'IT support for Gold Coast small businesses — typically 3 to 60 staff with no internal IT. Managed IT, cybersecurity, cloud and support at $190 + GST per hour.',
    "hero_img": 'it-support-small-business-gold-coast-hero.webp',
    "hero_alt": 'A Gold Coast small business team supported by bcom ICT',
    "h1": 'Too big to muddle through, too small for an IT person',
    "lede": "Three to sixty staff, nobody whose job this actually is, and a growing dependence on systems that nobody owns. It's the most common shape of business we work with.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['3–60 staff typically', '$190 + GST/hr', 'Month-to-month managed', 'Local since 2011'],
    "crumbs": [('Industries', '/industries'), ('Small business', '/it-support-small-business-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides IT support to Gold Coast small businesses, typically between three and sixty staff with no internal IT function. Support is available ad hoc at $190 + GST per hour, or as managed IT for a flat monthly fee calculated from your requirements, month-to-month with no lock-in. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'The staff member who "knows computers"',
                                         None,
                                         'Works fine until the business depends on it. Then someone whose '
                                         'actual job is something else is fixing the server instead, '
                                         'nothing is documented, and the business has a single point of '
                                         'failure who might resign.'),
                                 (       "A provider you can't get hold of",
                                         None,
                                         'They were good when you were smaller. Now calls take days, '
                                         'nothing is proactive, and you have no idea whether your backups '
                                         'work — because nobody has ever tested one in front of you.'),
                                 (       'Nobody at all',
                                         None,
                                         'Things get fixed when they break, by whoever is free. It works '
                                         'until a drive fails, an account gets compromised, or a client '
                                         'asks how you protect their information.'),
                                 (       'A scare',
                                         None,
                                         'An email that nearly worked, a ransomware story from someone you '
                                         "know, or an insurer's renewal form that suddenly asks questions "
                                         "you can't answer.")],
                'cols': 2,
                'eyebrow': 'The awkward middle',
                'h2': "You've outgrown the arrangement you've got",
                'icon': False,
                'sub': 'Almost every small business we take on arrives at the same point, from one of '
                       'these directions.'},
        {       'h2': "What we'd look at first",
                'ticks': [       '<strong>Are your backups real?</strong> Not whether a backup exists — '
                                 'whether a restore has been tested, and whether ransomware could reach it '
                                 'from inside your network.',
                                 '<strong>Is multi-factor authentication on everything?</strong> Usually '
                                 "it's on some accounts and not others, and the gap is where the problem "
                                 'comes from.',
                                 '<strong>Is anything documented?</strong> Devices, licences, passwords, '
                                 'suppliers. Most businesses we take on have none of it written down, and '
                                 "it's the thing that hurts when someone leaves.",
                                 "<strong>What's out of support?</strong> Unsupported operating systems "
                                 "and expired warranties on things you can't trade without.",
                                 '<strong>What keeps breaking?</strong> Recurring faults usually mean an '
                                 'ageing fleet or an underlying cause nobody has chased.']},
        {       'h2': 'Ad-hoc or managed',
                'html': '<p style="max-width:68ch">Both are legitimate and we will tell you honestly which '
                        'suits you. Ad-hoc at $190 + GST per hour works when your setup is simple and an '
                        'occasional problem is an annoyance rather than a crisis.</p><p '
                        'style="max-width:68ch;margin-top:16px"><a '
                        'href="/managed-it-services-for-small-businesses-gold-coast">Managed IT</a> makes '
                        'sense once you have a server, staff who genuinely cannot work without their '
                        'systems, or client data you would struggle to prove is protected. It is a flat '
                        'monthly fee calculated from your requirements, month-to-month with no '
                        'lock-in.</p><p style="max-width:68ch;margin-top:16px">Plenty of our managed '
                        'clients started as ad-hoc callers, and we have told plenty of businesses they are '
                        'not ready yet. The free review is how we work out which you are.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The problems we are actually called to in small businesses</h2>
      <p>Almost every small business we take on has at least four of these, and none of them are anybody&rsquo;s fault.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in a small business</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([('IT Support for Healthcare', '/it-support-healthcare-gold-coast'),
               ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('Pricing', '/pricing'),
        ('Onboarding — first 30 days', '/onboarding-first-30-days'),
        ('How to choose an MSP', '/how-to-choose-an-msp-gold-coast')])
            + cta('Start with the free review', "We look at what you're running and tell you what to fix first — including when the answer is that you don't need us monthly yet."),
}

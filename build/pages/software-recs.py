from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We bought it and nobody uses it&rdquo;",
     "software chosen on features rather than on how the work actually gets done. It does everything asked of it and does not fit the way the team operates.",
     "Watch the workflow before shortlisting anything. The product that wins on a feature comparison is frequently not the product people will actually open on a Monday morning."),
    ("&ldquo;Every department picked their own&rdquo;",
     "no central decision, so each team solved its own problem. The result is several products that half-overlap and none of which talk to each other.",
     "Map what is in use before choosing anything new. Consolidation is usually available and usually cheaper, and it removes the re-keying that quietly consumes hours."),
    ("&ldquo;It won&rsquo;t talk to our accounting package&rdquo;",
     "integration assumed rather than verified. Two products both claiming to integrate can mean anything from a live connection to a manual file export.",
     "Establish exactly what the integration does before committing. &ldquo;Integrates with&rdquo; is a marketing phrase, and the difference between a real connection and a CSV export is measured in hours per week."),
    ("&ldquo;We&rsquo;re on the free plan and it&rsquo;s becoming a problem&rdquo;",
     "a product adopted informally that the business now depends on. Free plans generally lack administrative control, audit history and any route to get your data back out.",
     "Decide deliberately whether to move to a paid tier or off it entirely. Business-critical work sitting on a free plan belonging to an individual staff member is a real exposure and an extremely common one."),
    ("&ldquo;The vendor is discontinuing it&rdquo;",
     "a product reaching end of life, sometimes with a migration path and sometimes not. It rarely arrives with much notice.",
     "Establish what happens to your data and what the realistic alternatives are, early. The worst version of this is discovering the export options only after the announcement."),
    ("&ldquo;Everyone says we should be using AI for this&rdquo;",
     "genuine pressure rather than a genuine requirement. Some of these tasks suit it well; others need a defined process, and adding AI to an undefined one just produces faster confusion.",
     "Be specific about the task before choosing a tool. We will tell you when the answer is a spreadsheet, a better process, or nothing at all &mdash; see our <a href=\"/artificial-intelligence-service-gold-coast\">AI services</a> for where it genuinely pays."),
]

EXAMPLE_1 = example(
    "The software they chose second",
    "A services business had shortlisted two job management products. One was considerably more capable and slightly cheaper. The directors had effectively decided and asked us to confirm the choice.",
    "Sitting with the team for half a day, the work was almost entirely done on phones in the field with intermittent coverage. The more capable product was excellent on a desktop and required a connection for nearly everything. The other worked properly offline and synchronised later. On a feature comparison it lost; on the way the business actually worked it was the only viable option.",
    "Set out both against the real workflow rather than the feature list, ran a two-week trial of each with the field staff who would live in it, and let the team decide with the evidence in front of them.",
    "The business chose the less capable product and still uses it four years later. The one that won on paper would have been abandoned within months, which is the most expensive outcome of any software decision.")

EXAMPLE_2 = example(
    "Four products, three overlaps, one bill",
    "A business of twenty-five people asked for help choosing a customer relationship product. Nobody had asked what was already in use.",
    "Three separate teams were already using three different products with substantially overlapping functions, none of them talking to the others. Customer records existed in all three in inconsistent states, and one team was manually re-keying data between two of them for about four hours a week. A fourth product had been trialled a year earlier and was still being billed.",
    "Mapped what each team actually needed, consolidated onto the product that covered the most ground with the least disruption, migrated the records into one consistent set, and cancelled what was left.",
    "The business ended up with fewer products, one customer list, and no re-keying. The original question &mdash; which new product to buy &mdash; turned out to have the answer none.")

EXAMPLE_3 = example(
    "The free plan holding four years of client work",
    "A consultancy asked us to review its systems ahead of taking on a larger client with its own security requirements. The review was expected to be routine.",
    "The project management tool the whole business ran on was a free plan, registered four years earlier to the personal email address of a staff member who had since moved into a different role. It held every active project, the client correspondence attached to them, and four years of history. The business had no administrative control over it, no ability to add or remove people centrally, no audit history, and no route to recover the data if that individual&rsquo;s account were ever closed. Everyone had assumed, reasonably, that the business owned it.",
    "Moved to a paid business tier owned by the company, migrated the full history rather than starting fresh, established proper administrative control, and set up the access review the incoming client would ask about.",
    "The business now owns the system its work lives in. The annual cost was modest and had been avoided for four years without anyone deciding to avoid it &mdash; the free plan simply worked, right up until somebody asked who owned it.")
FAQS = [   (   'Can you recommend business software for us?',
        'Yes, vendor-neutrally — bcom ICT takes no referral fees from software vendors. We start by mapping how the work is actually done rather than comparing feature lists, and the recommendation '
        'is frequently to consolidate what you already have rather than add another tool.'),
    (   'Do you get paid by software vendors?',
        "No. That's the point of asking us rather than a reseller. It also means we'll tell you when the software isn't the problem — which is a conclusion a vendor is never going to reach."),
    (   "We've got too many subscriptions. Can you help?",
        "That's the most common version of this job. A review typically finds duplicate tools doing the same work, seats for departed staff, licence tiers above what's needed, and things already "
        'included in your Microsoft 365 subscription being paid for separately.'),
    (   'Should we build custom software instead?',
        'Occasionally, but rarely for a small business. Off-the-shelf plus proper configuration and integration covers most needs at a fraction of the cost and with someone else maintaining it. '
        "We'll say when custom is genuinely warranted.")]

PAGE = {
    "path": '/software-recommendations-gold-coast',
    "priority": '0.65',
    "title": 'Business Software Recommendations Gold Coast | bcom ICT',
    "description": 'Independent advice on business software for Gold Coast businesses — what to use, what to consolidate, and when the answer is to fix the process rather than buy a tool.',
    "hero_img": 'hero-bg-software-installation.webp',
    "hero_alt": 'Business software being evaluated with a Gold Coast client by bcom ICT',
    "h1": 'Which software should we actually use?',
    "lede": "Vendor-neutral advice on business software — including the fairly common answer that the tool isn't the problem.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Vendor-neutral', 'No referral fees', 'Consolidation first', '$198 + GST/hr'],
    "crumbs": [('Services', '/services'), ('Software Recommendations', '/software-recommendations-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides vendor-neutral advice on business software for Gold Coast businesses — evaluating options against how a business actually operates, identifying duplicate or unused subscriptions, and advising when a process change would serve better than a new tool. bcom ICT takes no vendor referral fees. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'What does the work actually look like?',
                                         None,
                                         'Before comparing products, we map how the task is done now, '
                                         'where time goes and where things get re-keyed between systems. '
                                         'The answer is often that two existing tools should talk to each '
                                         'other rather than a third being bought.'),
                                 (       'What have you already got?',
                                         None,
                                         'Businesses in Microsoft 365 frequently pay separately for things '
                                         'already included. A subscription review before a purchase is '
                                         'common sense and regularly saves more than the new tool costs.'),
                                 (       'Who has to use it?',
                                         None,
                                         "The best-reviewed product is worthless if your team won't adopt "
                                         'it. Fit with how people already work matters more than feature '
                                         'count.'),
                                 (       'What does leaving look like?',
                                         None,
                                         'Ask before you commit, not after. Can you export your data in a '
                                         "usable form? Software that's hard to leave is a decision you "
                                         'make once and live with for years.')],
                'cols': 2,
                'eyebrow': 'How we approach it',
                'h2': 'Start with the workflow, not the shortlist',
                'icon': False},
        {       'h2': "The answer is often 'fewer tools'",
                'html': '<p style="max-width:68ch">The most common finding is not a missing product — it '
                        'is four overlapping ones. A CRM nobody fully adopted, a project tool one '
                        'department chose, a file-sharing service predating Microsoft 365, and a '
                        'subscription for someone who left two years ago.</p><p '
                        'style="max-width:68ch;margin-top:16px">Consolidating is usually cheaper, simpler '
                        'to support and easier for staff than adding another system. It also reduces the '
                        'number of places your business data sits, which matters for security and for '
                        "answering a client's questions about how you handle their information.</p>"}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>How software decisions actually go wrong</h2>
      <p>Six recurring situations. The expensive mistake is almost never picking the wrong feature set.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What choosing software properly looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Software Installation & Config', '/software-installation-configuration-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Technology Procurement Advice', '/technology-procurement-advice-gold-coast'),
        ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast'),
        ('AI Implementation', '/artificial-intelligence-service-gold-coast'),
        ('IT Needs Assessment', '/it-needs-assessment-gold-coast')])
            + cta('Drowning in subscriptions?', 'A review usually finds enough duplication to cover the cost of doing it.'),
}

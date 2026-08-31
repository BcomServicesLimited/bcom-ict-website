from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We&rsquo;ve been quoted for something and can&rsquo;t judge it&rdquo;",
     "a proposal written by the party who benefits from it. The document is usually accurate; what it leaves out is what you cannot see.",
     "Have someone independent read it before you sign. An hour spent on a quote is the cheapest part of any project, and the questions it produces are the ones the vendor was not asked."),
    ("&ldquo;Three quotes and we can&rsquo;t compare them&rdquo;",
     "three vendors who each scoped the job differently. They are not competing proposals so much as three different projects with similar names.",
     "Normalise them to a common scope so you are comparing the same work. Most of the price difference between quotes turns out to be inclusions rather than margin."),
    ("&ldquo;We&rsquo;re paying for licences nobody uses&rdquo;",
     "a subscription count that grew with the business and never shrank. Departed staff, trials that became permanent, and duplicate products doing the same job.",
     "Audit what is actually assigned and being used against what is being billed. This routinely finds recurring spend that stops the moment somebody looks."),
    ("&ldquo;The contract auto-renewed for another three years&rdquo;",
     "a renewal window nobody was tracking. Telecommunications and software agreements frequently roll over with notice periods measured in months.",
     "Record every renewal date and its notice period in one place. Knowing a contract is up in six months is what creates the ability to negotiate it."),
    ("&ldquo;Is this actually the right product for us?&rdquo;",
     "a fair question that vendors are structurally unable to answer. Every vendor&rsquo;s product is the right one.",
     "Start from what the business needs to do rather than from a shortlist. The right answer is sometimes the cheaper product, and occasionally it is keeping what you have."),
    ("&ldquo;Our provider wants to replace everything&rdquo;",
     "sometimes justified and sometimes not. It is difficult to assess when the assessment comes from the party doing the replacing.",
     "Get an independent view of what genuinely needs replacing and what has years left. We charge for the hour and have no hardware margin riding on the answer, which is the entire point."),
]

EXAMPLE_1 = example(
    "The three quotes that were three different projects",
    "A business had gathered three quotes to replace its server and network, ranging from $19,000 to $61,000. The spread was wide enough that the directors assumed one vendor was overcharging and asked us to say which.",
    "None of them were. The cheapest quote covered hardware supply with installation billed hourly and no data migration. The most expensive included migration, out-of-hours cutover, three years of warranty, network remediation and documentation. Normalised to the same scope, the three were within about eleven per cent of each other &mdash; and the cheapest became the second most expensive.",
    "Rewrote the requirement as a single scope, sent it back to all three, and reviewed the revised responses against it.",
    "The business chose on merit rather than on a headline number. Had it accepted the cheapest as presented, the omitted work would have arrived later as variations, which is how a $19,000 project becomes a dispute.")

EXAMPLE_2 = example(
    "Nine hundred dollars a month for software nobody opened",
    "A services business asked for a review of its technology spend before a budget cycle. Nothing was wrong &mdash; the directors simply wanted to know whether the number was reasonable.",
    "Licence counts had never been reduced as people left, so the business was paying for nineteen more subscriptions than it had staff. Two separate products were being paid for that did substantially the same job, one adopted by a department that did not know the other existed. A trial from two years earlier had converted to a paid plan nobody had noticed.",
    "Reconciled every subscription against the current staff list and actual usage, consolidated the duplicated products onto the one people preferred, and set a quarterly review so the count could not drift again.",
    "Recurring spend fell by a little over nine hundred dollars a month with no loss of capability. The review cost a few hours and had never been done because nobody owned the question.")

EXAMPLE_3 = example(
    "The contract that had eleven weeks left on a three-year roll",
    "A business asked us to review its telecommunications spend, believing it was paying too much for its internet and phone services. It had been with the same provider for several years and assumed it was free to move.",
    "The agreement had auto-renewed twice. Each renewal carried a three-year term and a ninety-day notice window, and the business had passed through both windows without noticing because renewal notices had gone to a mailbox belonging to a bookkeeper who had left. Exiting mid-term would have triggered a break fee of several thousand dollars. There were eleven weeks remaining before the next notice window closed, after which the business would have been committed for a further three years.",
    "Established the exact notice date and lodged notice inside the window, then ran a competitive process with enough time to move deliberately rather than under pressure. The incumbent was invited to bid and did.",
    "The business ended up staying with the same provider on materially better terms, which it could not have negotiated from inside a term it had no ability to leave. Every contract and renewal date now sits in one register with the notice period recorded against it.")
FAQS = [   (   'Can you review a quote from another IT provider?',
        "Yes, and it's one of the most common reasons businesses call. We read the proposal, explain what it actually buys, and flag anything missing, duplicated or padded. bcom ICT takes no vendor "
        "commissions, so the assessment isn't influenced by wanting to sell you an alternative."),
    (   'Do you earn commission on hardware you recommend?',
        "No. We source at trade pricing and are transparent about what we charge over it, and we're happy for clients to buy directly and have us configure it instead. A recommendation to buy "
        'nothing costs us nothing to make.'),
    ('What does procurement advice cost?', "$198 + GST per hour ($217.80 inc GST). We scope the piece of work first so you're agreeing to a rough number of hours rather than an open meter."),
    (   'Will you tell us not to buy something?',
        "Regularly. Common examples: a server that could be retired to cloud instead of replaced, a licence tier above what's needed, and equipment with years of useful life being replaced "
        'unnecessarily.')]

PAGE = {
    "path": '/technology-procurement-advice-gold-coast',
    "priority": '0.65',
    "title": 'Technology Procurement Advice Gold Coast | bcom ICT',
    "description": 'Independent advice on what technology to buy, from a provider that takes no vendor commissions. Read the quote, check the spec, and hear when the answer is to buy nothing.',
    "hero_img": 'hardware-procurement-setup-gold-coast-hero.webp',
    "hero_alt": 'Technology procurement advice being provided to a Gold Coast business by bcom ICT',
    "h1": 'Someone to read the quote before you sign it',
    "lede": 'Independent advice on what to buy, what to skip, and whether the proposal in front of you is reasonable. We take no vendor commissions, so it costs us nothing to say no.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['No vendor commissions', '$198 + GST/hr', 'Second opinions welcome', 'Often the cheapest hour'],
    "crumbs": [('Services', '/services'), ('Technology Procurement Advice', '/technology-procurement-advice-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides independent technology procurement advice to Gold Coast businesses — reviewing quotes and proposals, specifying what a business actually needs, and advising on whether to buy, upgrade or do nothing. bcom ICT takes no commissions from hardware or software vendors. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       "A quote landed and you can't judge it",
                                         None,
                                         'Someone has proposed a system, a server or a migration and you '
                                         "have no way to assess whether it's reasonable. We read it, tell "
                                         'you what it actually buys, and flag anything missing or padded. '
                                         "Frequently the cheapest hour you'll spend."),
                                 (       "You're not sure what to specify",
                                         None,
                                         'Buying for the work each person actually does, rather than the '
                                         'cheapest model or the one at the top of the page. An accounts '
                                         'machine, a CAD workstation and a reception PC are three '
                                         'different purchases.'),
                                 (       'Renewal is coming up',
                                         None,
                                         'Licensing, subscriptions and support contracts renewing on '
                                         'autopilot. A review before renewal frequently finds tiers above '
                                         'what you need and seats nobody uses.'),
                                 (       "You're being told to replace something",
                                         None,
                                         "Sometimes correct, often driven by who's available rather than "
                                         "what the equipment needs. We'll assess remaining life honestly — "
                                         'see the replacement cycle guide.')],
                'cols': 2,
                'eyebrow': 'When to call',
                'h2': 'Four moments this is worth an hour',
                'icon': False},
        {       'h2': 'Why independent matters here',
                'ticks': [       '<strong>No hardware or software commissions.</strong> A recommendation '
                                 'to buy nothing costs us nothing.',
                                 "<strong>We're not an internet or phone reseller</strong>, so advice on "
                                 "plans isn't influenced by wanting to sell you one.",
                                 '<strong>You can take the advice elsewhere.</strong> Some clients have us '
                                 "specify and then buy it themselves. That's a legitimate outcome.",
                                 "<strong>We'll say when the incumbent is right.</strong> If the quote in "
                                 'front of you is fair, hearing that is worth the hour too.',
                                 "<strong>We'll say when we're the wrong people.</strong> Some purchases "
                                 "need a specialist, and it's cheaper for everyone if we say so early."]}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The buying decisions we get asked about</h2>
      <p>Six situations where an independent hour before signing tends to pay for itself several times over.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What independent advice looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('IT Needs Assessment', '/it-needs-assessment-gold-coast'),
        ('Computer replacement cycle', '/business-computer-replacement-cycle'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast')])
            + cta("Got a quote you can't judge?", 'Send it over. An hour reading it is usually the cheapest part of the whole purchase.'),
}

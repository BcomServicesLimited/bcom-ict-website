from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We don&rsquo;t know what we&rsquo;ve got&rdquo;",
     "systems built up over a decade by several people, none of whom documented anything. Everything works and nobody can describe it.",
     "Document what exists before deciding what to change. Every recommendation we could make is worth less than an accurate picture of the starting point, which is why this comes first."),
    ("&ldquo;We&rsquo;re not sure if we&rsquo;re exposed&rdquo;",
     "genuine uncertainty. Most businesses have some things done well and some things not done at all, and without looking there is no way to know which is which.",
     "Assess against a recognised baseline rather than an opinion. We map findings to the ASD Essential Eight so the result is a position you can measure again later rather than a list of our preferences."),
    ("&ldquo;Our provider says everything is fine&rdquo;",
     "possibly true. It is also an assessment by the party responsible for the thing being assessed, which is worth noting regardless of how good they are.",
     "Get an independent look. If your provider is doing well, a review says so in writing and that is worth having. We have no interest in manufacturing problems to win work we would rather earn honestly."),
    ("&ldquo;We&rsquo;re about to spend a lot and want a second opinion&rdquo;",
     "a sensible instinct before a server replacement, an office move or a major migration.",
     "Establish what the business actually needs before the money is committed. The cheapest moment to change a plan is before anyone has ordered anything."),
    ("&ldquo;We&rsquo;re growing and it&rsquo;s starting to creak&rdquo;",
     "arrangements that suited eight people being asked to carry twenty-five. Nothing has failed; everything has become slightly harder.",
     "Identify what breaks next at the size you are heading for. Growth exposes the weakest part of a setup, and it is considerably cheaper to find it deliberately."),
    ("&ldquo;A client is asking questions we can&rsquo;t answer&rdquo;",
     "a security questionnaire, an insurer, or a tender requiring evidence of how information is protected.",
     "Establish your real position, then close the gaps. Answering accurately is not optional, and a review gives you something defensible to answer from."),
]

EXAMPLE_1 = example(
    "A review that told a business to keep its provider",
    "A business of forty staff had been with the same IT provider for six years and had begun to wonder whether it was getting value. It commissioned an independent review with a half-expectation of being told to move.",
    "The provider was doing a competent job. Patching was current, backups were tested, multi-factor authentication was enforced and documentation existed and was accurate &mdash; which is more than we find most of the time. Two genuine gaps existed: no formal restore testing schedule, and a firewall configuration carrying rules nobody could account for.",
    "Reported exactly that, including the parts that reflected well on the incumbent, and set out the two gaps with what each would take to close. Provided the report to the business to hand to its provider.",
    "The business kept its provider, who closed both gaps within a month. We did not win the account and were not trying to &mdash; a review that always concludes the incumbent is failing is not a review, it is a sales process.")

EXAMPLE_2 = example(
    "Finding what breaks at forty people",
    "A business of eighteen staff was planning to roughly double over two years. Everything worked. The directors wanted to know what would stop working, and when, before it did.",
    "Three things would not survive the growth. The server had capacity for perhaps a year of additional data. The internet connection had no failover and the business was moving more of its work into the cloud each quarter. And every administrative function &mdash; onboarding, access changes, password resets &mdash; depended on one person&rsquo;s knowledge with nothing written down, which was already a single point of failure and would become a bottleneck.",
    "Set out a staged plan with each item costed and sequenced against the growth rather than all at once, starting with documentation because it was the cheapest and the most urgent.",
    "The business grew into the plan rather than through a series of failures. Two of the three items were addressed well before they became urgent, which is the only time technology spending is comfortable.")

EXAMPLE_3 = example(
    "The assessment that found nothing dramatic",
    "A business commissioned a review largely because a director had read about a competitor being hit by ransomware. There was no specific concern &mdash; it was a general unease that something might be wrong.",
    "Most things were in reasonable order. Backups ran and had been restored from within the year, multi-factor authentication was in place, and machines were patched. Three things were not: a former employee&rsquo;s account was still active five months after departure, the wireless network had a single password shared with guests and staff alike, and nobody had ever confirmed whether the backup covered the accounting file, which sat on a workstation rather than the server.",
    "Reported the three findings with the effort each required &mdash; two of them under an hour, one about half a day &mdash; and reported plainly that the rest was in good shape.",
    "All three were closed within a fortnight. The accounting file had genuinely never been backed up, which nobody had known and which would have been discovered at the worst possible time. An assessment that finds three things and says so is more useful than one that manufactures thirty.")
FAQS = [   (   'Is the IT assessment really free?',
        "Yes. bcom ICT provides the initial systems review at no charge, and you keep the written report whether or not you engage us. It's how both sides work out whether there's a fit — and "
        "sometimes the honest conclusion is that you don't need a monthly arrangement yet."),
    (   'What do you need from us?',
        'Access to the site and systems, whatever documentation already exists, and roughly an hour of someone who knows how the business actually works day to day. Everything else is our time.'),
    ('Will it disrupt anything?', "No. It's a review rather than a change — nothing is altered during the assessment. Any remediation is quoted and agreed separately afterwards."),
    ('How long does it take?', 'For a typical small business, a few days from access to report. Larger or completely undocumented environments take longer, mostly in discovery rather than analysis.'),
    (   "What if we don't want to use you afterwards?",
        "That's a legitimate outcome and the report is still yours. Plenty of businesses take it to their existing provider — we'd rather it got acted on by someone else than not acted on at all."),
    (   'Is this the same as a security health check?',
        'No. The needs assessment is broader and free — systems, licensing, hardware and security at a high level. The security health check is a deeper, fixed-fee review focused specifically on '
        'your security position and Essential Eight maturity.')]

PAGE = {
    "path": '/it-needs-assessment-gold-coast',
    "priority": '0.7',
    "title": 'Free IT Needs Assessment — Gold Coast Business | bcom ICT',
    "description": "An independent review of what you actually have — asset register, network documentation and a prioritised list of findings mapped to the Essential Eight.",
    "hero_img": 'it-needs-assessment-hero.webp',
    "hero_alt": 'An IT needs assessment being carried out for a Gold Coast business by bcom ICT',
    "h1": "Find out what you've actually got",
    "lede": "Most businesses can't answer basic questions about their own IT — what's backed up, what's out of support, who has access. The review answers them, and it's free.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['No charge', 'Report is yours', 'No obligation', 'About an hour of your time'],
    "crumbs": [('Services', '/services'), ('IT Needs Assessment', '/it-needs-assessment-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides a free IT needs assessment for Gold Coast businesses — reviewing systems, security, backups and licensing, then providing a plain-English written report on what is at risk and what to fix first. The report is yours to keep whether or not you engage bcom ICT. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       '"Are our backups working?"',
                                         None,
                                         'Not whether backups run — whether a restore has been tested, and '
                                         'whether ransomware could reach the backup from inside your '
                                         'network. This is the question that most often has an '
                                         'uncomfortable answer.'),
                                 (       '"Who can get into what?"',
                                         None,
                                         "Which accounts have multi-factor authentication and which don't. "
                                         "Who still has access who shouldn't. What a departed staff member "
                                         'can still reach.'),
                                 (       '"What\'s out of support?"',
                                         None,
                                         'Operating systems no longer receiving security updates, expired '
                                         "warranties on equipment you can't trade without, and software "
                                         'the vendor stopped patching.'),
                                 (       '"What are we actually paying for?"',
                                         None,
                                         'Licences and subscriptions nobody has reviewed. This one '
                                         'frequently pays for the work that follows.')],
                'cols': 2,
                'eyebrow': 'What it answers',
                'h2': "Questions most businesses can't answer about themselves",
                'icon': False},
        {       'h2': 'What you get',
                'ticks': [       'A written report in plain English — not a tool export with four hundred '
                                 'findings',
                                 'Every issue ranked by what it would actually cost you if it happened',
                                 'An inventory of devices, licences, warranties and suppliers, which most '
                                 'businesses have never had',
                                 'Where you sit against the ASD Essential Eight',
                                 'A prioritised plan: this month, this quarter, and what can genuinely '
                                 'wait',
                                 'Rough costs against each item so you can budget rather than guess']},
        {       'h2': "Why it's free",
                'html': '<p style="max-width:68ch">Because it is how we find out whether we are a fit, and '
                        'how you find out the same thing. We would rather spend a few hours discovering '
                        'that you do not need us monthly than sign you up and part company in eight '
                        'months.</p><p style="max-width:68ch;margin-top:16px">You keep the report either '
                        'way. Take it to your existing provider, work through it yourself, or use it to '
                        'compare quotes. It is written to be useful on its own.</p><p '
                        'style="max-width:68ch;margin-top:16px">What we need from you is access, whatever '
                        'documentation exists, and about an hour of someone who knows how the business '
                        'actually operates. The rest is our work.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What an assessment usually finds</h2>
      <p>Six situations that bring a business to an assessment, and what tends to be sitting underneath each.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What an assessment looks like in practice</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Onboarding — first 30 days', '/onboarding-first-30-days'),
        ('What IT support costs', '/it-support-cost-gold-coast'),
        ('How to choose an MSP', '/how-to-choose-an-msp-gold-coast')])
            + cta('Book the free review', 'A few hours of our time, about an hour of yours, and a written report you keep regardless.'),
}

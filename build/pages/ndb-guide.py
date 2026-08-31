from layout import MARK, cta, faq_block, ticks, steps, related, trust_note, verify_note, issues, example

TEST = [
    ("There's been unauthorised access, unauthorised disclosure, or loss",
     "Someone got into a system or a mailbox they shouldn't have, information went to the wrong recipient, or a device or record was lost. Loss counts even when nobody has necessarily looked at it."),
    ("It's likely to result in serious harm to someone",
     "Serious harm can be financial, physical, psychological, reputational or a mix. What matters is the sensitivity of the information, who has it now, and whether it was protected — encrypted data on a lost laptop is a very different situation to a plain spreadsheet."),
    ("You haven't been able to prevent that harm through remedial action",
     "If you act fast enough that serious harm is no longer likely — you recover the device before anyone accesses it, or you recall the email successfully — the breach may not be notifiable. This is why the first hours matter."),
]

STEPS_ = [
    ("Contain it", "Stop the access continuing. Reset credentials, disable the account, isolate the machine. Do not delete anything — that destroys the evidence you'll need to work out what actually happened."),
    ("Assess it", "Work out what information was involved, whose it was, and whether serious harm is likely. The Privacy Act allows up to 30 days for this assessment, and it should be documented as you go."),
    ("Notify if it's eligible", "If it meets the test, you notify the OAIC using their form and you notify the affected individuals, telling them what happened and what they should do about it."),
    ("Review and fix", "Work out how it happened and close the gap. Regulators look far more favourably on an organisation that fixed the underlying cause than one that just filed the paperwork."),
]

COMMON_ISSUES = [
    ("&ldquo;We&rsquo;re a small business, so the Privacy Act doesn&rsquo;t apply&rdquo;",
     "an exemption that is considerably narrower than most businesses assume. Health service providers have no small business exemption regardless of turnover, and several other categories fall outside it too.",
     "Establish your actual position rather than assuming. Businesses handling health information, credit information or tax file numbers frequently have obligations they have never assessed."),
    ("&ldquo;No data was taken, so there&rsquo;s nothing to report&rdquo;",
     "a conclusion reached before the scope was established. Unauthorised access is enough &mdash; the information does not have to leave.",
     "Determine what was actually reachable before concluding anything. An attacker in a mailbox for three weeks had access to everything in it, whether or not anything was copied."),
    ("&ldquo;We&rsquo;ll assess it once we&rsquo;ve cleaned up&rdquo;",
     "a sensible-sounding sequence that destroys the evidence the assessment depends on.",
     "Preserve first, assess, then remediate. A rebuilt machine cannot tell you what was reached, and 'we cannot determine' is a much worse position to be in than an uncomfortable finding."),
    ("&ldquo;Serious harm is a judgement call, so we&rsquo;ll say no&rdquo;",
     "an assessment made by the party with an interest in the answer. It is a judgement, and it is one that has to be made properly and documented.",
     "Assess it against the criteria and write down the reasoning. A documented decision that no notification was required is defensible; an undocumented assumption is not."),
    ("&ldquo;Our IT provider will handle the notification&rdquo;",
     "a misunderstanding of where the obligation sits. It rests with the entity holding the information, not with its suppliers.",
     "Understand what your provider can and cannot do. We establish and document the technical facts &mdash; what was accessed, when and by whom. The notification decision and the notification itself are yours."),
    ("&ldquo;We&rsquo;ll notify if we have to, later&rdquo;",
     "an underestimate of the timeframe. Assessment is expected promptly and there is an outer limit measured in days, not months.",
     "Start the clock at discovery and work to it. Businesses that leave this until the technical work is finished frequently find the assessment window has substantially elapsed."),
]

EXAMPLE_1 = example(
    "Establishing what was reachable, not what was taken",
    "A business discovered a mailbox had been accessed without authorisation. Nothing appeared to have been sent, no files were obviously missing, and the initial view within the business was that there was nothing to report.",
    "Sign-in records showed the account had been accessed on nineteen occasions across five weeks. The question under the scheme is not what was demonstrably taken but what was accessed, and the mailbox contained client identity documents collected for verification purposes &mdash; passports and licences &mdash; sitting in ordinary correspondence. Nobody had thought of the mailbox as holding identity documents, and it plainly did.",
    "Established from the available records what had been reachable during that period, documented it, and provided the factual technical account. The business took that to its lawyer, who assessed the notification obligation and handled it.",
    "The business notified. Its own assessment before the technical work had been that nothing had happened, which was an honest view reached without the information needed to hold it.")

FAQS = [
    ("What is the Notifiable Data Breaches scheme?",
     "The Notifiable Data Breaches scheme sits in Part IIIC of the Privacy Act 1988 and requires organisations covered by the Act to notify the Office of the Australian Information Commissioner and affected individuals when an eligible data breach occurs. An eligible data breach is unauthorised access, unauthorised disclosure or loss of personal information that is likely to result in serious harm, where remedial action has not prevented that harm."),
    ("How long do we have to report a data breach in Australia?",
     "Where you suspect an eligible data breach may have occurred, the Privacy Act allows up to 30 days to carry out a reasonable and expeditious assessment. If it is confirmed as eligible, notification to the OAIC and affected individuals must be made as soon as practicable — 30 days is the outer limit for deciding, not a grace period for acting."),
    ("Does the NDB scheme apply to a small business?",
     "Not automatically. The Privacy Act's small business exemption applies to many businesses under $3 million annual turnover, but there are significant exceptions — health service providers of any size, businesses trading in personal information, credit reporting bodies, contractors delivering Australian Government contracts, and others. Health providers are the exception that catches the most Gold Coast businesses by surprise. Get advice on your specific position rather than assuming the exemption applies."),
    ("What does bcom ICT do if there's a breach at our business?",
     "We help you contain it, work out technically what happened and what data was involved, preserve evidence, and give you a factual written account you can use for your assessment and notification. What we do not do is make the notification decision for you or notify on your behalf — that obligation sits with your business, not your IT provider, and any provider offering to take it off your hands is misunderstanding the law."),
    ("Are you obliged to tell us if you have a breach?",
     "Yes. If bcom ICT suffered a breach affecting systems or data belonging to a client, we would notify the affected clients as part of our documented incident response process. That obligation is part of our alignment to ISO/IEC 27001 practices and it works in both directions."),
    ("What if we're not sure whether it's serious enough to notify?",
     "Document what you know, take advice, and don't let the clock run out while deciding. The OAIC has published guidance on assessing serious harm, and for anything genuinely borderline a privacy lawyer is worth the fee. Under-notifying carries regulatory risk; over-notifying carries reputational cost. Neither is a decision to make in a hurry or alone."),
]

PAGE = {
    "path": "/notifiable-data-breach-guide-australia",
    "priority": "0.7",
    "title": "Notifiable Data Breaches — An Australian Business Guide | bcom ICT",
    "description": "What the Notifiable Data Breaches scheme requires of Australian businesses: the eligible breach test, the 30-day assessment window, who must notify, and what your IT provider can and can't do.",
    "hero_kind": "doc",
    "eyebrow": "Trust centre · guide",
    "h1": "Notifiable data breaches, explained for Australian businesses",
    "lede": "What the scheme actually requires, what counts as an eligible breach, and the division of responsibility between your business and your IT provider.",
    "crumbs": [("Trust centre", "/trust-centre"), ("Notifiable Data Breaches", "/notifiable-data-breach-guide-australia")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">The Notifiable Data Breaches scheme, in Part IIIC of the Privacy Act 1988, requires
    covered Australian organisations to notify the Office of the Australian Information Commissioner and
    affected individuals when an eligible data breach occurs. The Privacy Act allows up to 30 days to assess
    a suspected breach. The obligation sits with the business holding the data, not with its IT provider.</p>

    {verify_note("This guide is general information, not legal advice, and privacy law in Australia is actively changing. Check the current position with the OAIC or a privacy lawyer before relying on it for a live incident. Reviewed August 2026.")}

    <h2 style="margin-top:48px">The three-part test</h2>
    <p style="margin-top:16px">A breach is only <em>notifiable</em> if all three of these are true. Plenty of
    security incidents fail the test and don't require notification — which is why the assessment step
    matters rather than notifying reflexively.</p>
    <div class="grid grid--3" style="margin-top:32px">{steps(TEST)}</div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">If it happens</span>
      <h2>Four steps, in order</h2>
      <p>The first hour matters more than the next week, and the most common mistake is destroying evidence while trying to clean up.</p>
    </div>
    <div class="grid grid--4">{steps(STEPS_)}</div>
    <p style="margin-top:32px"><strong>Do not delete anything, and don't wipe and rebuild the machine.</strong>
    It's the instinctive reaction and it removes the only record of what actually happened — which you need
    for your assessment, your insurer, and possibly the regulator. Isolate it instead and call for help.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Who is actually covered</h2>
    <p style="margin-top:16px">This trips up more Gold Coast businesses than any other part of the scheme.
    The Privacy Act exempts many small businesses under $3 million annual turnover — but the exceptions are
    broad, and some of them are common locally:</p>
    {ticks([
      "<strong>Health service providers of any size</strong> — including allied health, dental, physiotherapy and psychology practices. Turnover is irrelevant here.",
      "Businesses that trade in personal information",
      "Credit reporting bodies and businesses handling credit eligibility information",
      "Contractors delivering services under an Australian Government contract",
      "Businesses that have opted in to Privacy Act coverage",
      "Any business over the $3 million annual turnover threshold",
    ])}
    <p style="margin-top:24px">If you're a health provider, assume you're covered. If you're anywhere near
    the turnover threshold or you handle sensitive information about clients, get advice on your specific
    position rather than assuming the exemption protects you.</p>

    <div class="rule">{MARK}</div>

    <h2>What your IT provider can and can't do</h2>
    <p style="margin-top:16px">There's a clear line here and it's worth understanding before you need it.</p>
    <p style="margin-top:16px"><strong>What we do:</strong> contain the incident, establish technically what
    happened and what data was involved, preserve evidence, and give you a factual written account you can
    use for your assessment and your insurer. Where you engage us for
    <a href="/cyber-incident-response-gold-coast">incident response</a>, that includes forensic investigation
    and recovery.</p>
    <p style="margin-top:16px"><strong>What we don't do:</strong> make the notification decision or notify on
    your behalf. The obligation under the Privacy Act sits with the organisation holding the personal
    information. An IT provider offering to take that off your hands has misunderstood the law, and relying
    on them would leave you exposed.</p>

    {trust_note('The best time to think about this is before it happens. A <a href="/cybersecurity-health-check-for-small-business-gold-coast">security health check</a> tells you what you hold and what would actually be exposed — which is most of the assessment work done in advance.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What people get wrong about notification</h2>
      <p>Six assumptions that lead businesses to the wrong conclusion about their obligations.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in practice</h2>
      <p>A representative engagement, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Cyber Incident Response", "/cyber-incident-response-gold-coast"),
  ("Ransomware payment reporting", "/ransomware-reporting-australia"),
  ("Cybersecurity Risk Assessment", "/cybersecurity-health-check-for-small-business-gold-coast"),
  ("Data handling & sovereignty", "/data-handling-and-sovereignty"),
  ("What to do when you've been hacked", "/what-to-do-when-hacked"),
  ("Trust centre", "/trust-centre"),
], heading="Related")}

{cta("Think you're in the middle of one right now?",
     "Call 07 3041 8993. Don't delete anything and don't rebuild the machine — isolate it and talk to us first.")}
''',
}

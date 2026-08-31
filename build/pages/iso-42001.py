from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;Is bcom ICT certified to ISO/IEC 42001?&rdquo;",
     "a question that needs a precise answer. The standard is certifiable for organisations, and separately there are certifications held by individuals who implement it.",
     "Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI. bcom ICT as an organisation is not certified to the standard. Those are different things and we publish which one applies."),
    ("&ldquo;We&rsquo;re a small business &mdash; is AI governance really for us?&rdquo;",
     "a fair question. The full management system described by the standard is aimed at organisations of a scale most Gold Coast businesses are not.",
     "Take the parts that apply. A written acceptable-use position, a record of which tools touch what data, and a human check on decisions that affect people &mdash; those are proportionate at any size and are where most of the value is."),
    ("&ldquo;Staff are already using AI tools we never approved&rdquo;",
     "the most common finding in this work, and it is not misconduct. Nobody told them not to, and the tools are genuinely useful.",
     "Find out what is actually in use before writing anything. A policy written without knowing that is either ignored or prohibits the only tool doing a necessary job."),
    ("&ldquo;What&rsquo;s the risk, specifically?&rdquo;",
     "usually client or personal information being pasted into a public tool, and decisions being made on output nobody verified. Both are ordinary rather than exotic.",
     "Address the two directly: say what may go into which tool, and require a human check where output affects a person. Most of the exposure closes with those two rules."),
    ("&ldquo;Does the Privacy Act apply to what we put into these tools?&rdquo;",
     "it can, and it depends on the information and where it is processed. Personal and health information deserve particular care.",
     "Establish what each tool touches and where it goes before adopting it. Some tools are appropriate for client information and some plainly are not, and the difference is knowable in advance."),
    ("&ldquo;Do we need any of this documented?&rdquo;",
     "increasingly yes, because clients and insurers are starting to ask. A verbal understanding is not evidence.",
     "Write it down &mdash; one page is usually enough to start. Having something documented and followed is worth considerably more than an elaborate framework nobody reads."),
]

EXAMPLE_1 = example(
    "The one page that mattered more than the project",
    "A professional firm engaged us to identify where AI could reduce administrative time. The expectation was a proposal for tooling and automation.",
    "Before recommending anything, we asked how staff were already using these tools. Six of nineteen were regularly using public AI services, and three had pasted client material into them &mdash; including one document containing personal information about a third party. Nobody had breached any rule, because no rule existed, and the tools were plainly helpful for the work.",
    "Wrote a one-page acceptable-use position setting out what may and may not be put into which tools, provided a sanctioned option for the uses that were legitimate, and briefed the whole firm in twenty minutes.",
    "The firm went on to automate two genuinely useful things. Its own assessment afterwards was that the policy page had been worth more than the automation, which is a fair reading and not the outcome we had been engaged to produce.")

EXAMPLE_2 = example(
    "Governance sized to the business",
    "A business of twenty-two staff had been told it needed an AI management system after a client asked about its AI governance in a supplier questionnaire. It had begun looking at what full ISO/IEC 42001 conformance would involve and found it daunting.",
    "The questionnaire asked four questions: whether the business used AI in delivering its services, what data those tools accessed, whether output affecting clients received human review, and whether any of it was documented. None of those required a management system. All four required the business to know its own position, which it did not.",
    "Established what was actually in use, wrote a short acceptable-use position and a register of tools and what each touches, and set a rule requiring human review of anything affecting a client. Documented the lot in about four pages.",
    "The questionnaire was answered accurately and the business did not build a management system it had no use for. If a future contract requires full conformance, the foundations exist and it becomes an extension rather than a start from nothing.")

FAQS = [   (   'What is ISO/IEC 42001?',
        'ISO/IEC 42001:2023 is the international standard for AI management systems. It sets out how an organisation should govern the AI it develops or uses — policy, roles and responsibilities, '
        'risk assessment, data governance, human oversight and the records that evidence it. It is to AI roughly what ISO/IEC 27001 is to information security.'),
    (   'Is bcom ICT certified to ISO/IEC 42001?',
        'No. bcom ICT holds no organisational ISO certification of any kind. Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI, which is an individual credential assessing '
        'competence to implement an AI management system. bcom ICT delivers AI governance work aligned to the standard, and does not describe itself as a certified organisation.'),
    (   'Do we need to be certified?',
        'Almost certainly not. For most Australian small and medium businesses the value is in having a documented, defensible position on AI use — not in an audit. Certification makes sense if a '
        "major client or a government contract requires it, and we'll tell you honestly if you're nowhere near needing it."),
    (   "What's the most common problem you find?",
        "Staff putting client information into public AI tools, with no rule saying they shouldn't. It's not misconduct — nobody told them. A one-page acceptable-use position resolves it, and it's "
        'usually the highest-value hour in the whole engagement.'),
    (   'How long does this take?',
        'For a small business, a few weeks including the inventory, policy drafting and getting it agreed internally. Most of the elapsed time is your people reading and agreeing rather than us '
        'writing.'),
    (   "Can you do this if we haven't deployed AI yet?",
        "That's the better time. Deciding the rules before three departments each adopt a different tool is considerably cheaper than unpicking it afterwards.")]

PAGE = {
    "path": '/iso-42001-ai-governance-gold-coast',
    "priority": '0.8',
    "service": 'ISO/IEC 42001 AI Governance',
    "title": 'ISO/IEC 42001 AI Governance for Australian Business | bcom ICT',
    "description": 'AI governance and ISO/IEC 42001 readiness for Australian businesses — policy, risk assessment, acceptable-use controls and audit evidence, led by a BSI-certified Lead Implementer.',
    "hero_img": 'iso-42001-ai-governance-hero.webp',
    "hero_alt": 'AI governance framework documentation being prepared by bcom ICT for an Australian business',
    "h1": 'Governing AI before someone asks how you do',
    "lede": 'Policy, risk assessment, acceptable use and human oversight — the framework that turns "we use AI" into something you can actually evidence.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['BSI-certified Lead Implementer', 'Australian businesses', 'Policy + evidence', 'Practical, not academic'],
    "crumbs": [('Services', '/services'), ('AI Implementation', '/artificial-intelligence-service-gold-coast'), ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT delivers AI governance work for Australian businesses aligned to ISO/IEC 42001:2023, the international standard for AI management systems — covering policy, risk assessment, acceptable-use controls, human oversight and audit evidence. The work is led by Ollie, who holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Staff are already using it',
                                         None,
                                         'Pasting client information into public AI tools to summarise a '
                                         'document or draft an email. Nobody told them not to, because '
                                         'nobody has written down what the rules are. This is the most '
                                         'common real exposure and it costs nothing to address.'),
                                 (       'Clients are starting to ask',
                                         None,
                                         'Larger clients and government buyers increasingly ask suppliers '
                                         'how they govern AI use — particularly where the supplier touches '
                                         'their data. "We\'re careful" is not an answer that survives a '
                                         'procurement questionnaire.'),
                                 (       'Insurers are starting to ask',
                                         None,
                                         'AI-related questions are appearing on professional indemnity and '
                                         'cyber renewal forms. Being able to point at a documented '
                                         'position is worth more than a good intention.'),
                                 (       "It's cheaper before deployment",
                                         None,
                                         'Deciding what AI may be used for, on what data, with what '
                                         'oversight, is straightforward beforehand and awkward once three '
                                         'departments have each adopted a different tool.')],
                'cols': 2,
                'eyebrow': 'Why now',
                'h2': 'AI is already in your business',
                'icon': False,
                'sub': 'Whether you deployed it or not — which is precisely the problem.'},
        {       'h2': 'What ISO/IEC 42001 covers',
                'html': '<p style="max-width:68ch">ISO/IEC 42001:2023 is the international standard for AI '
                        'management systems — the AI equivalent of what ISO 27001 is for information '
                        'security. It sets out how an organisation should govern the AI it develops or '
                        'uses: policy, roles, risk assessment, impact on affected people, data governance, '
                        'human oversight, and the records that demonstrate all of it.</p><p '
                        'style="max-width:68ch;margin-top:16px">For a small or medium Australian business, '
                        'the useful part is not certification. It is having a defensible written position '
                        'on what AI is used for, on what data, with what human check, before someone asks '
                        '— and being able to show the working.</p>'},
        {       'h2': 'What we deliver',
                'ticks': [       '<strong>AI policy</strong> — what may be used, for what, and on what '
                                 'data. Written to be read by staff rather than by auditors.',
                                 '<strong>Acceptable use rules</strong>, including the specific '
                                 'instruction about what must never go into a public AI tool',
                                 '<strong>Inventory</strong> of the AI in use across the business, which '
                                 'usually surfaces more than management expected',
                                 '<strong>Risk assessment</strong> for each use, proportionate to what it '
                                 'actually affects',
                                 '<strong>Human oversight</strong> defined where an output affects a '
                                 'person — nothing consequential decided unreviewed',
                                 '<strong>Evidence pack</strong> — decisions, approvals and review '
                                 'schedule, so the position can be demonstrated rather than asserted',
                                 '<strong>Readiness assessment</strong> if you are genuinely heading for '
                                 'certification']}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Questions</span>
      <h2>What people actually ask about AI governance</h2>
      <p>Six questions. The first one has a precise answer and deserves one.</p>
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
            + related([       ('AI Implementation', '/artificial-intelligence-service-gold-coast'),
        ('Microsoft Copilot', '/microsoft-copilot-gold-coast'),
        ('ISO alignment', '/iso-alignment'),
        ('Trust centre', '/trust-centre'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Our team', '/our-team')])
            + cta('Do you know what AI your staff are using?', "Most businesses don't, and the inventory is where this starts. It's usually a short conversation with a useful answer."),
}

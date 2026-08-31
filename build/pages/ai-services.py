from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What AI can a small business actually use?',
        'The four that reliably pay for themselves are AI phone agents for after-hours calls, website chatbots grounded in your own content, workflow automation between systems that currently need '
        'manual re-keying, and Microsoft Copilot where a business is already in Microsoft 365. bcom ICT implements all four for Australian SMEs under an ISO/IEC 42001-aligned governance framework. '
        'Call 07 3041 8993.'),
    (   'Is bcom ICT certified for AI?',
        'bcom ICT holds no organisational ISO certification. Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI — an individual credential in AI management systems — and AI '
        'work is delivered under a framework aligned to that standard. We keep the distinction between an individual credential and an organisational certification explicit, on this page and in our '
        'trust centre.'),
    (   'Where should we start?',
        'With whatever consumes the most staff time and follows the same steps every time. That is usually not the thing being marketed to you. The first conversation is about your actual workflows, '
        'and sometimes the honest answer is that a process change beats a tool.'),
    (   'Is it safe to put our business data into AI tools?',
        "It depends entirely on the tool and how it's configured, which is exactly why the governance work matters. Staff pasting client information into public AI tools is a real and common "
        'exposure. A written acceptable-use position stops that being a matter of individual judgement.'),
    (   'Do you use this yourselves?',
        "Yes. Our after-hours phone answering is an AI operator — it takes details, triages and escalates, and identifies itself as an AI. We'd rather recommend things we run ourselves."),
    (   'What does it cost?',
        "Consulting and implementation are charged at $198 + GST per hour, scoped before we start. Ongoing platform costs depend on the tool and volume, and we'll set those out separately so you can "
        "see what's a one-off and what's monthly.")]

PAGE = {
    "path": '/artificial-intelligence-service-gold-coast',
    "priority": '0.8',
    "service": 'AI Implementation for Business',
    "title": 'AI Implementation for Australian Business | bcom ICT',
    "description": 'Practical AI implementation for Australian SMEs — AI phone agents, chatbots, workflow automation and Microsoft Copilot, delivered under an ISO/IEC 42001-aligned governance framework.',
    "hero_img": 'ai-integration-hero.webp',
    "hero_alt": 'AI workflow automation being implemented by bcom ICT for an Australian business',
    "h1": 'AI that saves actual hours',
    "lede": 'Phone agents, chatbots, workflow automation and Copilot — implemented where they genuinely remove work, and governed properly rather than switched on and hoped for.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['ISO 42001-aligned governance', 'Australian SMEs', 'We use it ourselves', 'Honest about limits'],
    "crumbs": [('Services', '/services'), ('AI Implementation', '/artificial-intelligence-service-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT implements practical AI for Australian small and medium businesses — AI phone agents, website chatbots, workflow automation and Microsoft Copilot rollout — delivered under an ISO/IEC 42001-aligned governance framework covering policy, risk assessment, acceptable use and human oversight. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'AI phone agents',
                                         '/ai-voice-agent-gold-coast',
                                         'Answering calls outside business hours, taking details, triaging '
                                         'and escalating. We run one ourselves — it is what answers bcom '
                                         "ICT's phones after hours, and it identifies itself as an AI "
                                         'rather than pretending to be a person.'),
                                 (       'Website chatbots',
                                         '/ai-chatbot-gold-coast',
                                         'Answering the same twenty questions your staff answer every day, '
                                         'and capturing enquiries out of hours. Useful when grounded in '
                                         'your actual content; irritating when it is a generic bot '
                                         'guessing.'),
                                 (       'Workflow automation',
                                         None,
                                         'The repetitive work between systems — reading an email, '
                                         'extracting the details, creating the record, notifying the '
                                         'person. Usually the highest return and the least glamorous.'),
                                 (       'Microsoft Copilot',
                                         '/microsoft-copilot-gold-coast',
                                         'Rolled out with the permissions work done first, because Copilot '
                                         'surfaces whatever a user can already reach. In most tenancies '
                                         'that is considerably more than anyone realises.')],
                'cols': 2,
                'eyebrow': 'What we implement',
                'h2': 'Four things that actually pay for themselves'},
        {       'h2': "Where we'll tell you not to bother",
                'html': '<p style="max-width:68ch">AI is being sold hard to Australian small businesses '
                        'right now, and a lot of it will not survive contact with a real workflow. We '
                        'would rather be the ones who say so.</p><p '
                        'style="max-width:68ch;margin-top:16px">It is generally not worth it when the '
                        'process it would automate happens twice a month, when the underlying data is a '
                        'mess (AI makes bad data faster, not better), when the task genuinely needs '
                        'judgement and someone will have to check every output anyway, or when the honest '
                        'fix is a process change rather than a tool.</p><p '
                        'style="max-width:68ch;margin-top:16px">The first conversation is about what '
                        'actually consumes time in your business. Sometimes the answer is not AI at '
                        'all.</p>'},
        {       'h2': "Governance isn't optional",
                'ticks': [       "<strong>What it can and can't be used for</strong> — written down, so "
                                 "staff aren't guessing",
                                 '<strong>What data goes into it</strong>, and what must never be pasted '
                                 'into a public tool',
                                 '<strong>Human oversight</strong> where an output affects a person — '
                                 'nothing consequential decided unreviewed',
                                 '<strong>Records</strong> of what was deployed, why, and who approved it',
                                 '<strong>Risk assessment</strong> before deployment rather than after an '
                                 'incident']}])
            + faq_block(FAQS)
            + related([       ('AI Voice Agents', '/ai-voice-agent-gold-coast'),
        ('AI Chatbots', '/ai-chatbot-gold-coast'),
        ('Microsoft Copilot', '/microsoft-copilot-gold-coast'),
        ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Trust centre', '/trust-centre')])
            + cta("What's eating your time?", "Start there rather than with the technology. The first conversation is free, and sometimes the answer is that you don't need AI for it."),
}

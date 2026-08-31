from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What is an AI phone agent?',
        'An AI phone agent answers calls, captures caller details, works out how urgent the matter is and escalates to a person where needed. bcom ICT implements them for Australian businesses and '
        'operates one for its own after-hours calls — it identifies itself as an AI rather than presenting as a person.'),
    (   "Will callers know it's not a person?",
        "Ours tells them, and we'd recommend the same. Pretending to be human is unnecessary and backfires the moment a caller works it out. Callers are generally fine with an AI that takes their "
        'details competently and gets someone to ring back.'),
    (   'What if the call is a genuine emergency?',
        "Triage rules are agreed with you so real emergencies reach a person rather than being logged for the morning. That's the part worth getting right, and it's the part generic setups usually "
        'skip.'),
    (   'Is it worth it for a small business?',
        "If you're missing calls outside hours and those calls are worth money, usually yes — a caller who reaches a voicemail often rings a competitor next. If your enquiries all arrive by email "
        "during business hours, probably not, and we'll say so."),
    (   'Does it work with our existing phone system?',
        "Usually. It sits in front of or alongside your existing system rather than replacing it. If you're on a cloud VoIP system it's generally straightforward; older on-premise PBX takes more "
        'work but is often possible.')]

PAGE = {
    "path": '/ai-voice-agent-gold-coast',
    "priority": '0.7',
    "title": 'AI Phone Agents for Australian Business | bcom ICT',
    "description": "AI phone agents that answer after hours, take details, triage and escalate. We run one ourselves — it's what answers bcom ICT's phones outside business hours.",
    "hero_img": 'ai-voice-agent-hero.webp',
    "hero_alt": 'An AI phone agent system configured by bcom ICT for an Australian business',
    "h1": 'Something that answers at 11pm',
    "lede": 'Not a robot pretending to be a person. An AI operator that takes the details, works out how urgent it is, and escalates — which is what ours does for us.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['We use it ourselves', 'Identifies as AI', 'Escalates properly', 'ISO 42001-aligned'],
    "crumbs": [('Services', '/services'), ('AI Implementation', '/artificial-intelligence-service-gold-coast'), ('AI Phone Agents', '/ai-voice-agent-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT implements AI phone agents for Australian businesses — answering calls outside business hours, capturing caller details, triaging urgency and escalating where needed. bcom ICT operates one for its own after-hours calls, and it identifies itself as an AI rather than presenting as a person. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'After hours and weekends',
                                         None,
                                         'The most common use, and the clearest return. A caller who '
                                         'reaches a voicemail usually calls a competitor next; one who '
                                         'reaches something that takes their details generally waits.'),
                                 (       "Overflow when everyone's busy",
                                         None,
                                         'Rather than a caller hitting an engaged tone or a queue nobody '
                                         'is clearing, the AI takes the details and someone calls back.'),
                                 (       'Triage before a human',
                                         None,
                                         'Working out whether this is urgent or routine before it reaches '
                                         "a person, so genuine emergencies don't sit behind a password "
                                         'reset.'),
                                 (       'Consistent capture',
                                         None,
                                         'Every caller asked the same questions, with the answers '
                                         'recorded. Which is more than most after-hours arrangements '
                                         'manage.')],
                'cols': 2,
                'eyebrow': "What it's for",
                'h2': 'The calls you currently miss',
                'icon': False},
        {       'h2': 'How we think it should be done',
                'ticks': [       '<strong>It identifies itself as an AI.</strong> Ours does. Pretending to '
                                 'be a person is both unnecessary and the fastest way to annoy a caller '
                                 'who works it out.',
                                 '<strong>It escalates rather than improvising.</strong> When something is '
                                 'beyond its scope it says so and gets a person, instead of guessing.',
                                 '<strong>Genuine emergencies reach a human.</strong> Triage rules agreed '
                                 'with you, so a real crisis is not politely logged for Monday.',
                                 '<strong>Everything is recorded.</strong> Caller, time, what they said '
                                 'and what happened next.',
                                 '<strong>Deployed under a governance framework</strong> covering what '
                                 'data it may take and what it must never do — see AI governance.']},
        {       'h2': 'We use one, which is why we recommend it',
                'html': '<p style="max-width:68ch">bcom ICT answers phones 24/7. Outside business hours '
                        'that is an AI operator — it takes the details, triages, and escalates a genuine '
                        'emergency to a person. It says it is an AI when it answers.</p><p '
                        'style="max-width:68ch;margin-top:16px">We say this on our <a '
                        'href="/service-levels-and-security">service levels page</a> too, because claiming '
                        '24/7 human response we do not provide would be the sort of thing this whole site '
                        'exists to avoid. It is a genuinely useful tool, and it is not a person.</p><p '
                        'style="max-width:68ch;margin-top:16px">It also means when we implement one for '
                        'you, we are recommending something we live with rather than something we read '
                        'about.</p>'}])
            + faq_block(FAQS)
            + related([       ('AI Implementation', '/artificial-intelligence-service-gold-coast'),
        ('AI Chatbots', '/ai-chatbot-gold-coast'),
        ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Published service levels', '/service-levels-and-security')])
            + cta('Missing calls after hours?', "Ring us at 11pm and hear ours answer. It's the most honest demonstration we can offer."),
}

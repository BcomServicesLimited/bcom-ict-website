from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We miss calls after hours and never hear from them again&rdquo;",
     "callers reaching voicemail and simply ringing the next business. Most people will not leave a message, and for some trades the majority of enquiries arrive outside business hours.",
     "Have something answer, take the details properly and log the job. A caller who has been heard will usually wait until the morning; one who reached a beep will not."),
    ("&ldquo;Our voicemail box is full and nobody checks it&rdquo;",
     "a message store rather than a process. Messages accumulate and get triaged eventually, which is not the same as being handled.",
     "Route what comes in to somewhere it will actually be seen &mdash; email, a ticket, a job record. The failure here is almost never the recording; it is what happens next."),
    ("&ldquo;It answers but it can&rsquo;t do anything&rdquo;",
     "a system that takes a message and stops. Useful, but well short of what is achievable.",
     "Decide deliberately what it should handle end to end &mdash; taking details, answering common questions, booking &mdash; and what it should escalate. Scope is what separates a useful assistant from a fancy answering machine."),
    ("&ldquo;It won&rsquo;t recognise what people say&rdquo;",
     "accents, background noise, place names and trade terminology. Australian suburb names in particular defeat a lot of systems.",
     "Test with real callers and real vocabulary before going live, including the local place names people will actually say. This is the part most implementations skip and the part callers notice first."),
    ("&ldquo;It sounds like it&rsquo;s pretending to be a person&rdquo;",
     "a deliberate design choice by whoever built it. Callers work it out, and they mind.",
     "Have it say what it is at the start. Ours does. It costs nothing in usefulness and it avoids the moment where a caller feels they have been handled rather than helped."),
    ("&ldquo;What happens in an emergency call?&rdquo;",
     "the question that matters most and gets asked least. Some calls must reach a person and must not sit in a queue.",
     "Define the escalation path before anything goes live. For businesses where an after-hours call can be urgent, knowing which calls break through is the design decision that everything else follows."),
]

EXAMPLE_1 = example(
    "The calls a business did not know it was losing",
    "A trades business believed it received very few after-hours enquiries, because very few voicemail messages were left. On that basis, an after-hours answering arrangement seemed hard to justify.",
    "Call records showed a substantial volume of after-hours calls that connected, held for a few seconds and disconnected without leaving a message. The business had been measuring messages left, not calls received. The two numbers were not remotely similar, and evenings and Sunday afternoons were among the busiest periods for enquiry.",
    "Put an assistant on the line that identifies itself, takes the caller&rsquo;s details and the nature of the job, and delivers it as a job record before the office opens. Genuine emergencies are escalated on a defined path rather than queued.",
    "The business now starts each morning with the evening&rsquo;s enquiries already recorded. The calls had always been arriving &mdash; they had simply been arriving somewhere nobody was counting.")

EXAMPLE_2 = example(
    "Suburb names the system could not hear",
    "An assistant had been deployed by a business and was performing poorly. Callers were repeating themselves and abandoning calls, and the business was close to switching it off.",
    "The system handled names and phone numbers well and failed consistently on locations. Callers saying Mudgeeraba, Tallebudgera and Currumbin were being misheard, and the confirmation step would read something wrong back, which callers found more irritating than not being asked. It had been tested by the people who built it, none of whom were saying those words.",
    "Retrained the recognition on the local place names the business actually serves, and changed the confirmation step to offer likely matches rather than assert a single wrong one. Tested with staff and then with a small volume of real calls before full deployment.",
    "Abandonment dropped and the business kept it. The technology had been adequate throughout &mdash; it had been tested against the wrong vocabulary, which is a very ordinary implementation failure rather than a limitation of the tool.")

EXAMPLE_3 = example(
    "Deciding which calls must reach a person",
    "A business providing a service where some after-hours calls are genuinely urgent wanted an assistant on the line overnight. The concern, reasonably, was that an urgent call would be handled politely and go nowhere until morning.",
    "Reviewing a year of after-hours calls, roughly one in fourteen needed a person that night. They were identifiable &mdash; they used a small and consistent set of words, and they came from existing clients far more often than from new enquiries.",
    "Defined an escalation path before anything went live: the assistant identifies itself, takes details, and where the call matches the urgent criteria or the caller asks for a person, it escalates immediately to the on-call phone rather than logging the job. Everything else is recorded and waiting at eight in the morning. The escalation was tested repeatedly before the assistant answered a single real call.",
    "Urgent calls reach a person and the rest stop waking one. The design decision that mattered was made before the technology was chosen, which is the right order and not the usual one.")
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
                'html': '<p style="max-width:68ch">bcom ICT is open 8am to 5pm Monday to Friday. Outside those hours '
                        'that is an AI operator — it takes the details, triages, and escalates a genuine '
                        'emergency to a person. It says it is an AI when it answers.</p><p '
                        'style="max-width:68ch;margin-top:16px">We say this on our <a '
                        'href="/service-levels-and-security">service levels page</a> too, because claiming '
                        'a 24/7 human response we do not provide would be the sort of thing this whole site '
                        'exists to avoid. It is a genuinely useful tool, and it is not a person.</p><p '
                        'style="max-width:68ch;margin-top:16px">It also means when we implement one for '
                        'you, we are recommending something we live with rather than something we read '
                        'about.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>How phone assistants actually go wrong</h2>
      <p>Six issues. The most common is a business that does not know how many calls it is already missing.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a voice assistant engagement looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([('Cloud PBX — our own platform', '/cloud-pbx-gold-coast'),       ('AI Implementation', '/artificial-intelligence-service-gold-coast'),
        ('AI Chatbots', '/ai-chatbot-gold-coast'),
        ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('Published service levels', '/service-levels-and-security')])
            + cta('Missing calls after hours?', "Ring us at 11pm and hear ours answer. It's the most honest demonstration we can offer."),
}

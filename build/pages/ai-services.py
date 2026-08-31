from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;The board wants an AI strategy&rdquo;",
     "pressure rather than a defined problem. It usually produces a search for somewhere to apply AI, which is the wrong direction to travel.",
     "Start from the tasks that consume the most time and work out which of them suit it. Some will; several will not, and saying so is more useful than finding something to automate."),
    ("&ldquo;Staff are already pasting client information into public AI tools&rdquo;",
     "no guidance, so people use what they find helpful. It is not misconduct &mdash; nobody told them not to, and the tools are genuinely useful.",
     "Write a one-page acceptable-use position and tell people what is and is not appropriate. This is consistently the highest-value hour in any AI engagement, and it costs nothing."),
    ("&ldquo;It gives confident answers that are wrong&rdquo;",
     "a general-purpose tool answering from general knowledge rather than from your information. It has no way to know what it does not know.",
     "Ground it in your own documented material and have it decline rather than guess. A tool that says it does not know is far more valuable in a business than one that always produces an answer."),
    ("&ldquo;We tried it and quietly stopped&rdquo;",
     "a pilot with no defined success measure, so nobody could say whether it worked. Enthusiasm carries these for about six weeks.",
     "Define what saving looks like before starting and measure it. An honest measurement that says this did not help is a good outcome &mdash; it stops the spending."),
    ("&ldquo;Is any of this allowed under the Privacy Act?&rdquo;",
     "a reasonable question that depends on what information is involved and where it goes. Personal and health information deserve particular care.",
     "Establish what data the tool touches, where it is processed and what the vendor does with it, before adopting it. Some tools are appropriate for client information and some plainly are not."),
    ("&ldquo;We don&rsquo;t want to sound like a robot to our customers&rdquo;",
     "a legitimate concern, and one we share. Customers notice, and they mind more about being deceived than about the technology itself.",
     "Have anything automated identify itself as such. Our own after-hours assistant says it is an assistant rather than pretending to be a person, which is the standard we would apply to yours."),
]

EXAMPLE_1 = example(
    "The hour that mattered more than the project",
    "A professional firm engaged us to look at where AI could reduce administrative time. The expectation was a proposal for tooling.",
    "Before recommending anything, we asked how staff were already using these tools. Six of nineteen were regularly using public AI services, and three had pasted client material into them &mdash; including one document containing personal information about a third party. Nobody had done anything they had been told not to do, because there was no policy and the tools were plainly helpful.",
    "Wrote a one-page acceptable-use position setting out what may and may not be put into which tools, provided a sanctioned tool for the uses that were legitimate, and briefed the whole firm in twenty minutes.",
    "The firm went on to automate two genuinely useful things. Its own view was that the policy page had been worth more than the automation, which is a fair assessment and not the one we were engaged to produce.")

EXAMPLE_2 = example(
    "Measuring a pilot honestly enough to stop it",
    "A business wanted to automate the drafting of a category of routine customer correspondence. It looked like an obvious candidate &mdash; high volume, formulaic, and consuming real hours.",
    "Building a small pilot and measuring it properly, drafting time fell by about forty per cent. Checking and correcting time rose enough to consume most of that, because the correspondence carried commitments that had to be verified regardless of who drafted them. Net saving was around eight per cent, against a subscription and ongoing oversight.",
    "Reported the measurement as it stood and recommended not proceeding for that use. Identified a different task &mdash; summarising long inbound documents for triage, where an error costs a re-read rather than a commitment &mdash; and piloted that instead.",
    "The second use saved several hours a week and was adopted. The first was not, and would have been had nobody insisted on measuring it before scaling it.")

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
        "Consulting and implementation are charged at $190 + GST per hour, scoped before we start. Ongoing platform costs depend on the tool and volume, and we'll set those out separately so you can "
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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What businesses actually ask us about AI</h2>
      <p>Six situations. The most valuable thing we do in this area is frequently to say no.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What an AI engagement looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('AI Voice Agents', '/ai-voice-agent-gold-coast'),
        ('AI Chatbots', '/ai-chatbot-gold-coast'),
        ('Microsoft Copilot', '/microsoft-copilot-gold-coast'),
        ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Trust centre', '/trust-centre')])
            + cta("What's eating your time?", "Start there rather than with the technology. The first conversation is free, and sometimes the answer is that you don't need AI for it."),
}

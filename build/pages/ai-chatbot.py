from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;It makes things up about our business&rdquo;",
     "a chatbot answering from general knowledge rather than from your material. It has no way to distinguish what it knows about businesses generally from what is true about yours.",
     "Ground it strictly in your own documented content and have it decline anything outside that. A bot that says it will pass the question to a person is doing its job; one that invents an answer is creating a liability."),
    ("&ldquo;It quoted a price we don&rsquo;t charge&rdquo;",
     "pricing that exists somewhere in its source material in an outdated form, or that it inferred. Statements about price and availability are the ones that cause real problems.",
     "Keep commercial statements out of a bot&rsquo;s remit unless the underlying figures are current and controlled. Anything a bot says is something your business appears to have said."),
    ("&ldquo;Customers just want a person&rdquo;",
     "a bot placed as an obstacle rather than a shortcut. If the only route to a human is through a maze, people resent the maze.",
     "Make handover to a person immediate and obvious. A bot that answers the easy questions and hands over the rest is genuinely useful; one that defends the inbox is actively harmful."),
    ("&ldquo;It doesn&rsquo;t know about anything from this year&rdquo;",
     "source material that was loaded once and never refreshed. The bot is accurate about a version of the business that no longer exists.",
     "Connect it to content that updates, and review what it draws on periodically. A bot is a reflection of its sources and degrades exactly as fast as they do."),
    ("&ldquo;We can&rsquo;t tell what people are asking it&rdquo;",
     "no logging or review. The conversation record is frequently the most valuable output and it is routinely discarded.",
     "Review the transcripts. What customers repeatedly ask a bot tells you what your website fails to explain, and that has been worth more to several clients than the bot itself."),
    ("&ldquo;Is it obvious to customers that it&rsquo;s a bot?&rdquo;",
     "sometimes not, which is a choice some businesses make deliberately. We think it is the wrong one.",
     "Have it identify itself. Customers mind far less about talking to a bot than about discovering they were talking to one. Our own after-hours phone assistant says what it is, and we would build yours the same way."),
]

EXAMPLE_1 = example(
    "The transcripts were worth more than the chatbot",
    "A services business installed a chatbot to reduce the volume of routine enquiry emails. It worked adequately &mdash; not dramatically, but it handled a reasonable share of simple questions.",
    "Reviewing three months of transcripts, over a third of all conversations were people trying to establish one thing: whether the business served their area. That information was on the website, three levels down, on a page almost nobody reached. The bot was efficiently answering a question the website should never have left open.",
    "Put a clear service area statement on the homepage and on every service page, then re-reviewed the transcripts a month later.",
    "That question largely disappeared from the bot and enquiry quality improved, because the people making contact had already established the business could help them. The transcripts had been sitting there the whole time telling anyone who read them what was wrong.")

EXAMPLE_2 = example(
    "Teaching it to say it doesn&rsquo;t know",
    "A business came to us after a chatbot on its site had given a customer a specific commitment about turnaround times that the business did not offer. The customer had reasonably held them to it.",
    "The bot had been configured to be helpful and had no instruction about the limits of its knowledge. Asked a question its source material did not answer, it produced a plausible response by inference. It had almost certainly been doing this for months, and this was simply the first instance where somebody acted on it.",
    "Rebuilt it to answer only from approved material, to decline anything outside it and offer a handover, and removed anything about pricing or turnaround from its remit entirely. Enabled transcript logging so the business could see what it was being asked.",
    "It now answers a narrower range of questions and answers them correctly. The business considers that a better bot, which it is &mdash; a system that guesses on behalf of your business is not a feature.")

EXAMPLE_3 = example(
    "A bot that knew about a service the business had stopped offering",
    "A business noticed enquiries arriving for a service it had discontinued eighteen months earlier. The enquiries were specific and confident, and staff could not work out where people were getting the idea.",
    "The chatbot had been built against a copy of the website taken at the time it was installed. The website had since been updated and the discontinued service removed, but the bot was still answering from its original snapshot. It had been describing a service the business no longer offered, in detail, for a year and a half &mdash; and doing it convincingly enough that customers believed it over the website.",
    "Reconnected it to draw from the live site rather than a stored copy, added a scheduled review of its source material, and set up transcript logging so drift of this kind surfaces from the conversations rather than from confused enquiries.",
    "The bot now describes the business as it currently is. The failure was not technical &mdash; the bot worked exactly as built. It had simply been built to answer from a moment in time that kept receding.")
FAQS = [   (   'Are website chatbots actually useful?',
        'A chatbot grounded in your own content is useful — it answers routine questions, captures enquiries outside business hours and hands over to a person when it reaches its limit. An '
        'ungrounded generative chatbot produces plausible-sounding answers that may be wrong, which costs credibility rather than saving time.'),
    (   'Will it give visitors wrong information?',
        "Not if it's grounded in your actual content and configured to say it doesn't know rather than improvise. The test is asking it something specific about your business that isn't on your "
        "website — a well-built bot admits it doesn't know."),
    (   'Does it replace our staff answering enquiries?',
        "No, and shouldn't try to. It handles the routine and repetitive, and passes anything real to a person with the context intact. Businesses that try to make it handle everything end up with "
        'frustrated visitors.'),
    (   'What does it cost to run?',
        "There's an implementation cost and an ongoing platform cost that depends on volume. We set both out separately so you can see what's one-off and what's monthly. Consulting and "
        'implementation are $190 + GST per hour.'),
    (   "What's the most useful thing about having one?",
        'Often the logs rather than the bot. Seeing what people actually ask shows you exactly what your website fails to answer — which is worth fixing regardless of whether you keep the chatbot.')]

PAGE = {
    "path": '/ai-chatbot-gold-coast',
    "priority": '0.7',
    "title": 'AI Chatbots for Australian Business Websites | bcom ICT',
    "description": 'Website chatbots grounded in your own content — answering the questions your staff answer daily and capturing enquiries out of hours. Useful when built properly, irritating when not.',
    "hero_img": 'ai-chatbot-hero.webp',
    "hero_alt": 'An AI chatbot implemented by bcom ICT on an Australian business website',
    "h1": 'A chatbot worth having on your site',
    "lede": 'Grounded in your actual content, it answers the twenty questions your staff answer every day. Ungrounded, it guesses — and everyone can tell.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Grounded in your content', 'Escalates to a human', 'Captures after-hours enquiries', 'ISO 42001-aligned'],
    "crumbs": [('Services', '/services'), ('AI Implementation', '/artificial-intelligence-service-gold-coast'), ('AI Chatbots', '/ai-chatbot-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT implements website chatbots for Australian businesses, grounded in the business's own content so answers come from real information rather than generation. A properly built chatbot answers routine questions, captures enquiries outside business hours, and hands over to a person when it reaches the limit of what it knows. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       'Grounded in your content',
                                         None,
                                         'The bot answers from your actual pages, pricing, policies and '
                                         "FAQs. When it doesn't know, it says so and offers a person. "
                                         'Genuinely useful, and it makes your website work harder.'),
                                 (       'Ungrounded and generative',
                                         None,
                                         'Plausible-sounding answers assembled from nothing in particular. '
                                         'Wrong prices, invented policies, confident nonsense. Visitors '
                                         'notice quickly and it costs you credibility rather than saving '
                                         'time.'),
                                 (       'The honest test',
                                         None,
                                         "Ask it something specific about your business that isn't on your "
                                         "website. A grounded bot says it doesn't know. An ungrounded one "
                                         'makes something up — and that is the one that will eventually '
                                         "quote a price you don't charge."),
                                 (       'It needs maintaining',
                                         None,
                                         "When your pricing or services change, the bot's source content "
                                         'has to change with them. A chatbot nobody updates becomes a '
                                         'liability rather than an asset.')],
                'cols': 2,
                'eyebrow': 'The difference',
                'h2': 'Grounded or guessing',
                'icon': False},
        {       'h2': 'What a good one does',
                'ticks': [       'Answers the routine questions — hours, location, pricing, what you do, '
                                 'how to get started',
                                 'Captures enquiries outside business hours, when the alternative is the '
                                 'visitor leaving',
                                 "Says clearly when it doesn't know, and offers a person rather than "
                                 'improvising',
                                 'Passes the conversation to a human with the context intact, not from '
                                 'scratch',
                                 'Logs what people actually ask — which is frequently more useful than the '
                                 'bot itself, because it shows what your website fails to answer']},
        {       'h2': "When we'd tell you not to bother",
                'html': '<p style="max-width:68ch">If your website gets modest traffic, if enquiries are '
                        'complex and always need a person, or if nobody will own keeping the content '
                        'current — a chatbot will cost more in maintenance and irritation than it '
                        'returns.</p><p style="max-width:68ch;margin-top:16px">It is also the wrong first '
                        'move if the underlying problem is that your website does not answer the questions '
                        'people ask. Fixing the pages is cheaper, helps search engines and AI assistants '
                        'as well as visitors, and often removes the need for the bot entirely.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>How chatbots actually go wrong</h2>
      <p>Six failure modes. The dangerous one is a bot that would rather answer than admit it does not know.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a chatbot engagement looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('AI Implementation', '/artificial-intelligence-service-gold-coast'),
        ('AI Phone Agents', '/ai-voice-agent-gold-coast'),
        ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast'),
        ('Microsoft Copilot', '/microsoft-copilot-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Contact us', '/contact')])
            + cta("Wondering if it's worth it?", 'Start with what people actually ask you. If your website already answers it, a bot may be solving the wrong problem.'),
}

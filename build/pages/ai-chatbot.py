from layout import cta, faq_block, related, svc_body

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
        'implementation are $198 + GST per hour.'),
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
            + faq_block(FAQS)
            + related([       ('AI Implementation', '/artificial-intelligence-service-gold-coast'),
        ('AI Phone Agents', '/ai-voice-agent-gold-coast'),
        ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast'),
        ('Microsoft Copilot', '/microsoft-copilot-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Contact us', '/contact')])
            + cta("Wondering if it's worth it?", 'Start with what people actually ask you. If your website already answers it, a bot may be solving the wrong problem.'),
}

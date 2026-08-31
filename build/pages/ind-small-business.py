from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What size business does bcom ICT work with?',
        'Most clients have between three and sixty staff — businesses too large to keep muddling through and too small to justify a full-time IT employee. bcom ICT has supported Gold Coast small '
        'businesses since 2011, on-site across the Gold Coast and remotely Australia-wide. Call 07 3041 8993.'),
    (   'How much does small business IT support cost?',
        'Ad-hoc support is $198 + GST per hour ($217.80 inc GST), plus a $100 + GST call-out for on-site work. Managed IT is a flat monthly fee calculated from your business requirements and the '
        'services included, quoted after a free review and month-to-month with no lock-in.'),
    (   "We've got someone in the office who handles IT. Is that a problem?",
        'Not necessarily, and plenty of clients keep that arrangement with us behind it — they handle day-to-day questions, we handle infrastructure, security and escalations. It becomes a problem '
        'when the business depends on one person, nothing is documented, and that person could resign.'),
    (   "What's the first thing we should sort out?",
        "Backups you've actually seen restore, and multi-factor authentication on every account. Between them they cover most of what genuinely damages small businesses, and neither is expensive."),
    (   'Do we have to commit to anything?',
        'No. The first conversation and the systems review are free, and you keep the written report either way. Managed agreements are month-to-month with no exit fee.'),
    (   "Will you tell us if we don't need you?",
        'Yes, and it happens. Sometimes the review concludes that ad-hoc support is enough for now, or that your existing provider is doing a reasonable job and the problem is communication rather '
        'than competence.')]

PAGE = {
    "path": '/it-support-small-business-gold-coast',
    "priority": '0.8',
    "title": 'Small Business IT Support Gold Coast | bcom ICT',
    "description": 'IT support for Gold Coast small businesses — typically 3 to 60 staff with no internal IT. Managed IT, cybersecurity, cloud and support at $198 + GST per hour.',
    "hero_img": 'it-support-small-business-gold-coast-hero.webp',
    "hero_alt": 'A Gold Coast small business team supported by bcom ICT',
    "h1": 'Too big to muddle through, too small for an IT person',
    "lede": "Three to sixty staff, nobody whose job this actually is, and a growing dependence on systems that nobody owns. It's the most common shape of business we work with.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['3–60 staff typically', '$198 + GST/hr', 'Month-to-month managed', 'Local since 2011'],
    "crumbs": [('Industries', '/industries'), ('Small business', '/it-support-small-business-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT provides IT support to Gold Coast small businesses, typically between three and sixty staff with no internal IT function. Support is available ad hoc at $198 + GST per hour, or as managed IT for a flat monthly fee calculated from your requirements, month-to-month with no lock-in. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'The staff member who "knows computers"',
                                         None,
                                         'Works fine until the business depends on it. Then someone whose '
                                         'actual job is something else is fixing the server instead, '
                                         'nothing is documented, and the business has a single point of '
                                         'failure who might resign.'),
                                 (       "A provider you can't get hold of",
                                         None,
                                         'They were good when you were smaller. Now calls take days, '
                                         'nothing is proactive, and you have no idea whether your backups '
                                         'work — because nobody has ever tested one in front of you.'),
                                 (       'Nobody at all',
                                         None,
                                         'Things get fixed when they break, by whoever is free. It works '
                                         'until a drive fails, an account gets compromised, or a client '
                                         'asks how you protect their information.'),
                                 (       'A scare',
                                         None,
                                         'An email that nearly worked, a ransomware story from someone you '
                                         "know, or an insurer's renewal form that suddenly asks questions "
                                         "you can't answer.")],
                'cols': 2,
                'eyebrow': 'The awkward middle',
                'h2': "You've outgrown the arrangement you've got",
                'icon': False,
                'sub': 'Almost every small business we take on arrives at the same point, from one of '
                       'these directions.'},
        {       'h2': "What we'd look at first",
                'ticks': [       '<strong>Are your backups real?</strong> Not whether a backup exists — '
                                 'whether a restore has been tested, and whether ransomware could reach it '
                                 'from inside your network.',
                                 '<strong>Is multi-factor authentication on everything?</strong> Usually '
                                 "it's on some accounts and not others, and the gap is where the problem "
                                 'comes from.',
                                 '<strong>Is anything documented?</strong> Devices, licences, passwords, '
                                 'suppliers. Most businesses we take on have none of it written down, and '
                                 "it's the thing that hurts when someone leaves.",
                                 "<strong>What's out of support?</strong> Unsupported operating systems "
                                 "and expired warranties on things you can't trade without.",
                                 '<strong>What keeps breaking?</strong> Recurring faults usually mean an '
                                 'ageing fleet or an underlying cause nobody has chased.']},
        {       'h2': 'Ad-hoc or managed',
                'html': '<p style="max-width:68ch">Both are legitimate and we will tell you honestly which '
                        'suits you. Ad-hoc at $198 + GST per hour works when your setup is simple and an '
                        'occasional problem is an annoyance rather than a crisis.</p><p '
                        'style="max-width:68ch;margin-top:16px"><a '
                        'href="/managed-it-services-for-small-businesses-gold-coast">Managed IT</a> makes '
                        'sense once you have a server, staff who genuinely cannot work without their '
                        'systems, or client data you would struggle to prove is protected. It is a flat '
                        'monthly fee calculated from your requirements, month-to-month with no '
                        'lock-in.</p><p style="max-width:68ch;margin-top:16px">Plenty of our managed '
                        'clients started as ad-hoc callers, and we have told plenty of businesses they are '
                        'not ready yet. The free review is how we work out which you are.</p>'}])
            + faq_block(FAQS)
            + related([       ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Business IT Support', '/it-support-and-services-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('Pricing', '/pricing'),
        ('Onboarding — first 30 days', '/onboarding-first-30-days'),
        ('How to choose an MSP', '/how-to-choose-an-msp-gold-coast')])
            + cta('Start with the free review', "We look at what you're running and tell you what to fix first — including when the answer is that you don't need us monthly yet."),
}

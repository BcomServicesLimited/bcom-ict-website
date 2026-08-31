from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Is Microsoft Copilot safe to enable?',
        'Copilot only surfaces content a user already has permission to access — it grants nothing new. The risk is that permissions in most Microsoft 365 tenancies have accumulated over years, so '
        'staff can often reach far more than intended, and Copilot makes that instantly discoverable. bcom ICT reviews sharing and permissions before enabling it.'),
    (   'What should we do before turning Copilot on?',
        'Audit organisation-wide sharing, review SharePoint and OneDrive permissions, clean up access left by departed staff, restrict genuinely sensitive content, and pilot with a small group '
        'before a full rollout. The permissions work is the deployment — enabling Copilot is the easy part.'),
    (   'Who actually gets value from Copilot?',
        'People who spend a lot of time in documents, email and meetings. Much less for staff working mainly in a line-of-business application, on a shop floor or in the field. Licensing everyone '
        'when a third would use it is a common and expensive mistake — start with a pilot.'),
    (   'Does Copilot train on our data?',
        "Microsoft's commercial data protection terms govern this and the position differs between consumer and business licensing. It's worth understanding what your specific licensing says rather "
        'than assuming, and it belongs in your AI acceptable-use policy either way.'),
    (   'Do we need an AI policy before deploying it?',
        "It's strongly worth having. A written position on what AI may be used for and on what data means staff aren't making individual judgement calls — see ISO/IEC 42001 AI governance.")]

PAGE = {
    "path": '/microsoft-copilot-gold-coast',
    "priority": '0.75',
    "title": 'Microsoft Copilot Rollout for Australian Business | bcom ICT',
    "description": "Microsoft Copilot deployed with the permissions work done first. Copilot surfaces whatever a user can already reach — in most tenancies that's more than anyone realises.",
    "hero_img": 'microsoft-copilot-hero.webp',
    "hero_alt": 'Microsoft Copilot being configured for an Australian business by bcom ICT',
    "h1": 'Copilot shows people what they can already reach',
    "lede": 'That sentence is the entire deployment risk. In most Microsoft 365 tenancies, staff can reach considerably more than anyone assumes — and Copilot makes it findable.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Permissions first', 'ISO 42001-aligned governance', 'Microsoft Partner', 'Honest about value'],
    "crumbs": [('Services', '/services'), ('AI Implementation', '/artificial-intelligence-service-gold-coast'), ('Microsoft Copilot', '/microsoft-copilot-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='Microsoft Copilot surfaces content a user already has permission to access. In most Microsoft 365 tenancies, permissions have accumulated over years and staff can reach far more than intended — so bcom ICT does the permissions and sharing review before enabling Copilot, then deploys it under an ISO/IEC 42001-aligned governance framework. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Permissions accumulate',
                                         None,
                                         "Over years, files get shared with 'everyone in the organisation' "
                                         'for convenience, SharePoint sites are created with open '
                                         'defaults, and departing staff leave folders behind. Nobody '
                                         'audits it because nobody could find it.'),
                                 (       'Copilot finds it instantly',
                                         None,
                                         'Ask it about salaries, or a redundancy plan, or a client '
                                         'dispute, and it will surface anything the user can technically '
                                         'reach. It is doing exactly what it should — the problem is what '
                                         'they can reach.'),
                                 (       'It is a search problem, not an AI problem',
                                         None,
                                         'The exposure existed before Copilot. What changes is that it '
                                         'becomes trivially discoverable by someone with no technical '
                                         'skill and no intent to snoop.'),
                                 (       'So the order matters',
                                         None,
                                         'Permissions and sharing review first, Copilot second. Doing it '
                                         'the other way round is how businesses discover their own file '
                                         'structure the hard way.')],
                'cols': 2,
                'eyebrow': 'The risk nobody mentions',
                'h2': "Copilot doesn't grant access. It reveals it.",
                'icon': False},
        {       'h2': 'What we do before enabling it',
                'ticks': [       'Audit sharing across SharePoint and OneDrive — particularly anything '
                                 'shared organisation-wide',
                                 'Review site and library permissions, and the groups that grant them',
                                 'Identify sensitive content that should be restricted regardless of '
                                 'Copilot',
                                 'Clean up access left behind by departed staff',
                                 'Apply sensitivity labelling where the business needs it',
                                 'Then pilot Copilot with a small group before rolling it out']},
        {       'h2': 'Is it worth the licence cost?',
                'html': '<p style="max-width:68ch">Sometimes, and we would rather tell you when it is not. '
                        'Copilot earns its cost for people who spend a lot of time in documents, email and '
                        'meetings — summarising long threads, drafting from existing material, catching up '
                        'on a meeting they missed.</p><p style="max-width:68ch;margin-top:16px">It earns '
                        'considerably less for people who work mostly in a line-of-business application, '
                        'on a shop floor, or in the field. Licensing an entire business when a third of it '
                        'would actually use the thing is a common and expensive mistake.</p><p '
                        'style="max-width:68ch;margin-top:16px">Start with a pilot group, measure whether '
                        'they keep using it after the novelty, then decide. Governance for AI use '
                        'generally is covered on <a href="/iso-42001-ai-governance-gold-coast">ISO/IEC '
                        '42001 AI governance</a>.</p>'}])
            + faq_block(FAQS)
            + related([       ('AI Implementation', '/artificial-intelligence-service-gold-coast'),
        ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Trust centre', '/trust-centre')])
            + cta('Thinking about Copilot?', "Start with the permissions review. It's worth doing whether or not you deploy Copilot afterwards."),
}

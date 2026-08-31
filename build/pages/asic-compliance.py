from layout import cta, faq_block, related, svc_body

FAQS = [   (   'What does ASIC require for cybersecurity?',
        'ASIC expects Australian financial services licensees to manage cyber risk as part of the adequate risk management systems required under their general licence obligations, and has published '
        'guidance on cyber resilience. In practice that means implemented controls, documented evidence of them, oversight of outsourced arrangements including IT providers, and a workable incident '
        'response plan. bcom ICT delivers gap assessment, remediation and evidence for licensees Gold Coast and Australia-wide.'),
    (   "We're a small licensee. Does this really apply to us?",
        'Yes. The obligations attach to the licence rather than to the size of the practice. Small licensees are frequently caught out by exactly that assumption, and by the fact that their PI '
        'insurer asks the same questions regardless of headcount.'),
    (   'Does bcom ICT provide legal or compliance advice?',
        'No. We handle the technical controls, the assessment against recognised frameworks, and the evidence pack. Interpretation of your specific licence obligations is a matter for your '
        'compliance adviser or lawyer, and we work alongside them rather than in place of them.'),
    (   "What if we're asked for evidence tomorrow?",
        'Tell us that when you call. A gap assessment can be turned around quickly, and it is far better to be able to show a documented plan with dates against it than to show nothing at all.'),
    (   'Does this cover the Notifiable Data Breaches scheme?',
        'We cover it as part of incident response planning, because a breach at a financial services business almost always engages it. The notification obligation itself remains yours — see our NDB '
        'guide for how that division works.'),
    (   'Are you certified to any standard for this work?',
        'No, and we will not imply otherwise. bcom ICT aligns its own practices with ISO/IEC 27001:2022 and operates to the ASD Essential Eight, but holds no organisational certification. Our trust '
        'centre sets out exactly what is held and what is aligned.')]

PAGE = {
    "path": '/asic-cybersecurity-compliance-gold-coast',
    "priority": '0.8',
    "service": 'ASIC Cybersecurity Compliance',
    "title": 'ASIC Cybersecurity Compliance for AFS Licensees | bcom ICT',
    "description": 'ASIC cyber resilience compliance for AFS licensees, financial planners, mortgage brokers, accountants and insurance brokers. Gap assessment, remediation and documented evidence. Call 07 3041 8993.',
    "hero_img": 'cybersecurity-assessment-hero.webp',
    "hero_alt": 'A compliance review being carried out for an Australian financial services licensee',
    "h1": 'Cyber resilience evidence an ASIC reviewer will accept',
    "lede": 'For AFS licensees, planners, brokers and accountants — gap assessment, remediation, and documented controls you can actually produce when asked.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Built for AFS licensees', 'Documented evidence', 'Essential Eight mapped', 'Australia-wide'],
    "crumbs": [('Services', '/services'), ('Cybersecurity', '/cybersecurity-services-gold-coast'), ('ASIC Compliance', '/asic-cybersecurity-compliance-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer="bcom ICT delivers cyber resilience compliance work for Australian financial services businesses — AFS licensees, financial planners, mortgage brokers, accountants and insurance brokers. That covers gap assessment against ASIC's expectations, remediation of the gaps, and documented controls and evidence you can produce to a regulator or an auditor. Delivered Gold Coast and Australia-wide. Call 07 3041 8993.",
                     blocks=[       {       'cards': [       (       "It's a licence obligation, not best practice",
                                         None,
                                         'AFS licensees must maintain adequate risk management systems '
                                         'under their general obligations. ASIC has been increasingly '
                                         'willing to treat cyber resilience as falling squarely inside '
                                         'that, and to enforce it.'),
                                 (       'Evidence matters as much as controls',
                                         None,
                                         'Having multi-factor authentication switched on is necessary. '
                                         'Being able to demonstrate, in writing, when it was implemented, '
                                         'who it covers and how it is reviewed is what an assessment '
                                         'actually turns on.'),
                                 (       'Your suppliers count too',
                                         None,
                                         'Outsourced arrangements — including your IT provider — form part '
                                         'of the picture. Which is exactly why our own position is '
                                         'published in full on our trust centre rather than asserted.'),
                                 (       'Incidents have reporting paths',
                                         None,
                                         'A breach can trigger obligations to ASIC, to the OAIC under the '
                                         'Notifiable Data Breaches scheme, to your PI insurer, and '
                                         'potentially ransomware payment reporting. They are separate '
                                         'duties and satisfying one does not satisfy the others.')],
                'cols': 2,
                'eyebrow': 'Why this is different',
                'h2': "Licensees carry an obligation most businesses don't",
                'icon': False,
                'sub': 'Good security practice is optional for most companies. For an AFS licensee it sits '
                       'inside your licence conditions.'},
        {       'cols': 3,
                'eyebrow': 'How we run it',
                'h2': 'Assess, remediate, document',
                'steps': [       (       'Gap assessment',
                                         "Where you are now against ASIC's expectations and the ASD "
                                         'Essential Eight, including the outsourced arrangements. Written '
                                         'up plainly, ranked by exposure.'),
                                 (       'Remediation',
                                         'Closing the gaps in priority order — MFA coverage, patching, '
                                         'backups that are separated and tested, access control, logging '
                                         'that would let you establish what happened.'),
                                 (       'Evidence pack',
                                         'Policies, control descriptions, implementation dates, review '
                                         'schedule and incident response plan. The thing you actually '
                                         'produce when asked.')]},
        {       'h2': 'Who this is for',
                'ticks': [       'AFS licensees, including small licensees who assumed the obligations '
                                 'only apply to larger firms',
                                 'Financial planners and advice practices holding client financial and '
                                 'identity information',
                                 'Mortgage and finance brokers, who typically hold more identity documents '
                                 'than they realise',
                                 'Accountants and bookkeepers with client tax and financial records',
                                 'Insurance brokers handling claims and personal information',
                                 'Any practice whose PI insurer has started asking harder questions at '
                                 'renewal']}])
            + faq_block(FAQS)
            + related([       ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Notifiable Data Breaches guide', '/notifiable-data-breach-guide-australia'),
        ('24/7 Security Operations Centre', '/security-operations-centre-gold-coast'),
        ('Trust centre', '/trust-centre')])
            + cta('Renewal questionnaire getting harder?', "That's usually the trigger. A gap assessment tells you what you can honestly answer and what needs closing first."),
}

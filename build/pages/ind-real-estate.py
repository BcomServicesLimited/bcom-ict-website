from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Why are real estate agencies targeted by cyber criminals?',
        'Because agencies hold trust accounts and transfer significant sums on written instruction. Business email compromise — getting into a mailbox, watching for a settlement, then sending '
        'altered bank details — is low-effort and high-value. It is the single most costly threat to Australian agencies and it is largely preventable with multi-factor authentication and a verbal '
        'verification process for bank detail changes.'),
    (   'What is the single most important thing to do?',
        'Multi-factor authentication on every mailbox, without exception. It stops the overwhelming majority of email compromise. The second is a rule that any change of bank details is verified '
        'verbally on a number you already hold — never one supplied in the email itself.'),
    (   'Someone changed bank details by email. How do we check?',
        'Call the party on a number you already have on file, not one from the email or its signature. Do not reply to the email to ask, because if the mailbox is compromised you are asking the '
        'fraudster. If money has already moved, contact your bank immediately and then call us.'),
    (   'Do you support our CRM and portal integrations?',
        "We support the environment they run in — accounts, access, connectivity, devices and the network. For the applications themselves we work alongside your vendor's support, which is usually "
        'the arrangement that resolves things fastest.'),
    (   'Our agents are never in the office. Does that matter?',
        'It changes what needs managing. Devices that leave the building need security applied to them wherever they are, phones need to follow the person, and access needs revoking promptly when '
        'someone leaves. In a high-turnover industry that last one is a genuine control.'),
    (   'Are we covered by the Privacy Act?',
        'Depends on turnover and what you hold — agencies handle a considerable amount of identity documentation, and many are over the threshold. If you are unsure, that is worth establishing '
        'before an incident rather than during one.')]

PAGE = {
    "path": '/it-support-real-estate-gold-coast',
    "priority": '0.75',
    "title": 'IT Support for Gold Coast Real Estate Agencies | bcom ICT',
    "description": 'IT support for Gold Coast real estate agencies. Trust accounts make agencies a specific target for payment redirection fraud — plus CRM, portals and a mobile workforce.',
    "hero_img": 'it-support-real-estate-gold-coast-hero.webp',
    "hero_alt": 'IT support being provided to a Gold Coast real estate agency by bcom ICT',
    "h1": "Your trust account is why you're a target",
    "lede": "Agencies move other people's money on written instructions. That makes email compromise and payment redirection the specific threat — and it's preventable.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Payment fraud controls', 'Trust account exposure', 'Mobile workforce', 'After-hours reality'],
    "crumbs": [('Industries', '/industries'), ('Real estate', '/it-support-real-estate-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supports real estate agencies across the Gold Coast. Because agencies hold trust accounts and transfer funds on written instruction, email compromise and payment redirection fraud are the specific and most costly threat they face. bcom ICT implements the email, identity and process controls that prevent it. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Someone gets into a mailbox',
                                         None,
                                         'Usually a reused password with no multi-factor authentication. '
                                         'They do not announce themselves — they read, quietly, sometimes '
                                         'for weeks, learning how your settlements work and who talks to '
                                         'whom.'),
                                 (       'They wait for a settlement',
                                         None,
                                         'Then send a message that looks exactly right, from an address '
                                         'that looks exactly right, with different bank details. Often '
                                         'from within the real mailbox, so it passes every technical '
                                         'check.'),
                                 (       'The money moves',
                                         None,
                                         'Trust funds transferred on written instruction. By the time '
                                         'anyone notices, recovery is difficult and the professional and '
                                         'regulatory consequences are considerable.'),
                                 (       'A forwarding rule hides it',
                                         None,
                                         'A quiet mailbox rule sends copies elsewhere and deletes the '
                                         'evidence, so the legitimate parties never see the messages that '
                                         'would expose it.')],
                'cols': 2,
                'eyebrow': 'The specific threat',
                'h2': 'How agencies actually lose money',
                'icon': False,
                'sub': 'Not a hack in the dramatic sense. A patient, unremarkable email fraud.'},
        {       'h2': 'What actually prevents it',
                'ticks': [       '<strong>Multi-factor authentication on every mailbox</strong> — this '
                                 'alone stops the overwhelming majority of it, and plenty of agencies '
                                 "still don't have it on everyone",
                                 '<strong>Mailbox rule monitoring</strong>, so a forwarding rule nobody '
                                 'created gets noticed rather than working quietly for weeks',
                                 '<strong>Email authentication</strong> — SPF, DKIM and DMARC configured '
                                 'so someone cannot send messages that appear to come from your domain',
                                 '<strong>Impossible-travel and unusual sign-in alerting</strong> on your '
                                 'Microsoft 365 tenancy',
                                 '<strong>A verbal verification process</strong> for any change of bank '
                                 'details, using a number you already hold rather than one in the email. '
                                 'This is a process control, not a technical one, and it is the last line',
                                 '<strong>Staff who know what this looks like</strong>, because they are '
                                 'the ones who will see it first']},
        {       'h2': "The rest of an agency's IT",
                'html': '<p style="max-width:68ch">Beyond the fraud problem, agencies have a particular '
                        'shape: staff who are rarely at a desk, a CRM that is the business, portal '
                        'integrations that have to keep working, and an industry where enquiries do not '
                        'observe business hours.</p><p style="max-width:68ch;margin-top:16px">That means '
                        'devices leaving the building need to be managed, phones need to follow people '
                        'rather than sit on desks — see <a '
                        'href="/voip-phone-system-installation-and-support-gold-coast">VoIP</a> — and '
                        'support has to be available when the business is actually operating. It also '
                        'means access needs removing promptly when an agent leaves, which in a '
                        'high-turnover industry is a real control rather than paperwork.</p>'}])
            + faq_block(FAQS)
            + related([       ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Cyber Incident Response', '/cyber-incident-response-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('Is MFA on every mailbox in your agency?', "If you're not certain, that's the thing to check today. We'll tell you where the gaps are."),
}

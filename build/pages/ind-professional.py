from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;A client is asking us to complete a security questionnaire&rdquo;",
     "not a fault &mdash; a growing requirement. Larger clients, insurers and government buyers increasingly ask their advisers to evidence how information is protected before awarding work.",
     "Answer it accurately rather than optimistically, and fix the gaps it exposes. A questionnaire is the cheapest security audit a firm ever gets, and answering it honestly is what makes it useful."),
    ("&ldquo;Staff email documents to themselves to work at home&rdquo;",
     "no sanctioned way of working remotely, so people invent one. Client material ends up in personal mailboxes and on home computers nobody controls.",
     "Give them a proper remote path that is easier than the workaround. People route around friction, so the fix is to remove the friction rather than to write a policy prohibiting the shortcut."),
    ("&ldquo;We can&rsquo;t send a large file to a client&rdquo;",
     "mailbox limits. The usual response is a personal file-sharing account set up by whoever needed it that afternoon, holding client documents outside the firm entirely.",
     "Provide a sanctioned way to send large files with expiry and access logging. This is a small piece of work that closes one of the more common ways confidential material leaves a firm."),
    ("&ldquo;Someone who left still has access&rdquo;",
     "an offboarding process that covers the building keys and not the systems. Mailboxes, document management and cloud applications each need separate attention and rarely get it on the last day.",
     "Run offboarding from a checklist covering every system, executed on the day. Former staff retaining access to client files is both a real exposure and a very awkward thing to explain to a client."),
    ("&ldquo;Our document management system is slow&rdquo;",
     "the index, the storage, or the network path &mdash; and it is worth knowing which, because they have very different costs.",
     "Profile where the time is actually going before anyone buys hardware. Document systems are frequently blamed for delays introduced somewhere between the workstation and the storage."),
    ("&ldquo;We&rsquo;re not sure whether the Privacy Act applies to us&rdquo;",
     "genuine uncertainty. The small business turnover exemption is narrower than most firms assume, and several kinds of professional practice fall outside it regardless of size.",
     "Establish your actual position rather than assuming the exemption applies. Firms handling health information, credit information or tax file numbers frequently have obligations they have never assessed."),
]

EXAMPLE_1 = example(
    "The contractor who still had the file server eighteen months on",
    "An accounting firm engaged us after a client asked them to complete a security questionnaire. The firm expected to answer it comfortably &mdash; nothing had ever gone wrong.",
    "A contractor engaged for a three-month project eighteen months earlier still held an active account with access to the file server and the Microsoft 365 tenancy. The engagement had ended amicably and nobody had removed anything. The account had been used twice since, both times almost certainly innocently, and the firm had no way to establish that from its own records.",
    "Removed the access, audited every other account against the current staff list &mdash; which found two more &mdash; and built an offboarding checklist covering every system rather than only the mailbox.",
    "The questionnaire was answered accurately. The firm&rsquo;s view afterwards was that the questionnaire had been worth more than the fee, which is usually the case when nobody has looked before.")

EXAMPLE_2 = example(
    "Large files leaving the firm through a personal account",
    "A professional services firm needed to send bundles of documents to clients that were far too large for email. The practice had emerged organically and nobody had ever formalised it.",
    "Three staff were using personal file-sharing accounts registered to their own private email addresses. Client documents from the previous four years were sitting in storage the firm did not own, could not audit, and would lose entirely if any of those people left. Two of the shared links had no expiry and were still live.",
    "Set up sanctioned file sharing inside the firm&rsquo;s own tenancy with link expiry, access logging and revocation, migrated what was recoverable from the personal accounts, and expired the outstanding links.",
    "Client material now leaves the firm through a path the firm controls and can audit. The staff involved had done nothing wrong &mdash; they had been given a job to do and no tool with which to do it.")

FAQS = [   (   'What IT security do professional services firms need?',
        'At minimum: multi-factor authentication on every account, document access structured by role rather than open to everyone, managed devices for laptops that leave the office, email '
        'authentication to prevent impersonation, and backups held separately with tested restores. AFS licensees carry additional obligations under their licence. bcom ICT supports Gold Coast '
        'accountants, lawyers, planners and consultants. Call 07 3041 8993.'),
    (   'A client is asking how we protect their information. What do we send them?',
        "A documented position rather than an assurance — what controls you operate, how access is managed, where data is held, and what happens in an incident. If you don't have that written down, "
        'a security health check produces most of it and is the fastest route to being able to answer.'),
    (   'Does the Privacy Act apply to our firm?',
        'It depends on turnover and what you handle, and there are exceptions that catch firms out. Many professional services businesses are over the threshold, and those handling TFNs or credit '
        'information have specific obligations regardless. Worth establishing before an incident rather than during one.'),
    (   'Can staff work from home securely?',
        'Yes, if the security travels with the device rather than living in the office. That means managed laptops with encryption and remote wipe, MFA on everything, and access to documents through '
        'a controlled system rather than files copied to a desktop.'),
    (   'What about our practice or document management system?',
        'We support the environment it runs in — server or cloud tenancy, backups, access control, updates and connectivity — and work alongside your software vendor for the application itself.'),
    (   "We're an AFS licensee. Is that different?",
        'Yes. Cyber resilience falls within your general licence obligations and requires documented evidence rather than good practice alone. See our ASIC cybersecurity compliance page for the gap '
        'assessment and evidence work.')]

PAGE = {
    "path": '/it-support-professional-services-gold-coast',
    "priority": '0.75',
    "title": 'IT Support for Gold Coast Professional Services | bcom ICT',
    "description": 'IT support for Gold Coast accountants, lawyers, financial planners and consultants. Client confidentiality, document management, regulatory obligations and hybrid working.',
    "hero_img": 'hero-bg-consulting.webp',
    "hero_alt": 'IT support being provided to a Gold Coast professional services firm by bcom ICT',
    "h1": "You hold other people's confidential information",
    "lede": "Accountants, lawyers, planners and consultants. The work is portable, the obligations aren't, and your clients increasingly want to know how you protect what they've given you.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Client confidentiality', 'ASIC-aligned where required', 'Hybrid working', 'Essential Eight aligned'],
    "crumbs": [('Industries', '/industries'), ('Professional services', '/it-support-professional-services-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supports professional services firms across the Gold Coast — accountants, lawyers, financial planners, brokers and consultants. These firms hold concentrated client financial and identity information, carry professional and in some cases regulatory obligations over it, and increasingly have to evidence how it is protected. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'You hold more than you think',
                                         None,
                                         'Tax file numbers, identity documents, financial statements, '
                                         'wills, contracts. A professional services firm holds a density '
                                         'of sensitive information that would take a retailer years to '
                                         'accumulate, and it is all in one place.'),
                                 (       'The obligations vary by discipline',
                                         None,
                                         'AFS licensees carry cyber resilience obligations under their '
                                         'licence. Lawyers carry professional confidentiality duties. '
                                         'Accountants handle TFNs under specific rules. The compliance '
                                         'answer is not the same across the corridor.'),
                                 (       'Clients are now asking',
                                         None,
                                         'Larger clients and government buyers ask suppliers how they '
                                         'protect information before engaging them. "We take security '
                                         'seriously" does not survive a procurement questionnaire; a '
                                         'documented position does.'),
                                 (       'The work goes home',
                                         None,
                                         'Hybrid working is normal in this sector, which means client '
                                         'information travels on laptops and phones. Security has to apply '
                                         'wherever the device is, not only inside the office.')],
                'cols': 2,
                'eyebrow': "What's different",
                'h2': 'Concentrated information, portable work',
                'icon': False},
        {       'h2': 'What we put in place',
                'ticks': [       '<strong>Multi-factor authentication everywhere</strong> — the control '
                                 "that stops most account compromise, and still missing from someone's "
                                 'account at most firms we assess',
                                 '<strong>Document management and file access</strong> structured so '
                                 'people reach what their role requires, not the entire client base',
                                 '<strong>Device management</strong> for laptops and phones that leave the '
                                 'office, including remote wipe if one is lost',
                                 '<strong>Email security</strong> — filtering, plus the SPF, DKIM and '
                                 'DMARC records that stop someone invoicing your clients in your name',
                                 '<strong>Backup held separately</strong> with tested restores, because a '
                                 'firm that cannot produce a client file has a professional problem as '
                                 'well as a technical one',
                                 '<strong>An Essential Eight position</strong> you can point at when a '
                                 'client or insurer asks']},
        {       'h2': 'For AFS licensees specifically',
                'html': '<p style="max-width:68ch">If your firm operates under an Australian Financial '
                        'Services licence — planners, brokers, some accountants — cyber resilience sits '
                        'inside your general licence obligations, and ASIC has shown increasing '
                        'willingness to treat it that way.</p><p '
                        'style="max-width:68ch;margin-top:16px">That means implemented controls, '
                        'documented evidence of them, oversight of outsourced arrangements including your '
                        'IT provider, and a workable incident response plan. We cover that specifically on '
                        '<a href="/asic-cybersecurity-compliance-gold-coast">ASIC cybersecurity '
                        'compliance</a>, including the evidence pack you would actually produce when '
                        'asked.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The problems we are actually called to in firms</h2>
      <p>Professional practices tend to fail in the same six places, and none of them involve anyone doing anything malicious.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in a firm</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('ASIC Cybersecurity Compliance', '/asic-cybersecurity-compliance-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta("Being asked questions you can't answer?", 'A health check turns "we take it seriously" into a document you can actually send.'),
}

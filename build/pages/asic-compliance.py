from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("“We’ve had a questionnaire from our licensee”",
     "an authorised representative being asked to evidence controls they have never documented, often at short notice.",
     "Assess against the expectations, produce the evidence pack, and close the gaps in priority order. Being able to answer honestly matters more than answering well."),
    ("“Our PI renewal is asking about cyber”",
     "professional indemnity and cyber questionnaires have got materially harder, and the answers are no longer obvious.",
     "Establish the true position first — MFA coverage, patching, backup testing, endpoint protection — then close what is missing so the answers are accurate rather than optimistic."),
    ("“We outsource IT, so isn’t it their problem?”",
     "a common and dangerous assumption. Outsourced arrangements form part of your compliance picture; the obligation stays with the licensee.",
     "Document what your provider does, what they are responsible for, and what remains yours. That oversight is itself part of what is expected."),
    ("“We don’t hold much client data”",
     "an underestimate, almost always. Advice practices hold identity documents, financial statements and TFNs — a dense concentration by any measure.",
     "Inventory what is actually held and where. The volume is usually a surprise, and it is the basis for everything else."),
    ("“Our adviser works from home two days a week”",
     "client information on a device outside the office, often unmanaged, sometimes personal.",
     "Bring those devices under management with encryption and remote wipe, and put access behind MFA. Hybrid working is fine; unmanaged hybrid working is the exposure."),
    ("“What happens if we have a breach?”",
     "no incident response plan, so the first fifteen minutes get improvised at the worst possible time.",
     "Write the plan, name who does what, and know in advance which obligations engage — ASIC, the OAIC under the NDB scheme, your PI insurer. They are separate duties."),
]

EXAMPLE_1 = example(
    "An authorised representative asked to evidence controls",
    "A Gold Coast advice practice operating under a licensee received a compliance questionnaire asking specifically about cyber controls, with a four-week deadline.",
    "Most controls existed. Almost nothing was documented. MFA was on for four of seven staff, patching was inconsistent across machines, and there was no written record of who had access to what or when it had last been reviewed.",
    "Ran a gap assessment against ASIC’s expectations and the Essential Eight, closed the MFA and patching gaps, built an access register and a short incident response plan, and produced a written evidence pack with implementation dates.",
    "The questionnaire was answered with documents rather than assurances. The practice now has an evidence pack that updates rather than being rebuilt each time it is asked for.")

EXAMPLE_2 = example(
    "A broker whose IT provider was the gap",
    "A Gold Coast mortgage broking practice was confident about its own controls but had never considered its outsourced arrangements.",
    "The IT provider had shared administrative access across technicians with a common password, no MFA on their own management tooling, and no documented process for revoking access when their staff changed. The practice had no visibility of any of it and no contractual position on it.",
    "Documented the supplier arrangement, set out what the practice should require, and — after the practice moved to us — implemented individually named technician access with MFA enforced, plus access reviews on staff change.",
    "The practice can now evidence oversight of its outsourced IT, which is an explicit part of what is expected and the part most licensees overlook entirely.")

EXAMPLE_3 = example(
    "An incident plan written before it was needed",
    "A Gold Coast financial services practice had controls in reasonable shape but no documented incident response plan, and asked whether it mattered.",
    "It mattered more than they expected. Nobody could say who would make the notification decision, which obligations engaged, or who to call first. Their PI policy required notification before engaging any external party, which nobody had read.",
    "Wrote a short plan naming responsibilities, the sequence for the first hour, and the separate obligations to ASIC, the OAIC under the NDB scheme, and the insurer. Ran it through with the team so it was not the first time anyone had seen it.",
    "Four months later a staff member clicked a credential harvesting link. The plan was followed, the insurer was notified in the right order, and the whole thing was contained inside a morning.")

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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What licensees actually get asked</h2>
      <p>These six questions come up in nearly every compliance conversation in this sector.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a compliance engagement looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('Essential Eight assessment', '/essential-eight-guide-gold-coast'),
        ('Notifiable Data Breaches guide', '/notifiable-data-breach-guide-australia'),
        ('24/7 Security Operations Centre', '/security-operations-centre-gold-coast'),
        ('Trust centre', '/trust-centre')])
            + cta('Renewal questionnaire getting harder?', "That's usually the trigger. A gap assessment tells you what you can honestly answer and what needs closing first."),
}

from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;It surfaced a document nobody should have seen&rdquo;",
     "permissions that were always too open. Copilot did not grant access to anything &mdash; it made existing access discoverable, which is a very different problem wearing the same clothes.",
     "Review sharing and permissions before enabling it, not after. Nearly every alarming Copilot story is a permissions story that predates Copilot by years."),
    ("&ldquo;Everyone has access to everything&rdquo;",
     "years of files shared broadly for convenience, plus &ldquo;anyone with the link&rdquo; sharing that was never revisited. Invisible until something makes it searchable.",
     "Audit what is shared with whom, and tighten it. This work is worth doing whether or not Copilot is ever enabled, which is the honest way to look at the cost."),
    ("&ldquo;Staff tried it twice and stopped&rdquo;",
     "a licence assigned with no guidance. It is genuinely useful for a handful of tasks and unremarkable for the rest, and people who start with the wrong ones conclude it is not worth it.",
     "Show people the two or three things it does well for their actual role. Adoption is almost entirely a training problem, and untrained licences are the most common source of wasted spend here."),
    ("&ldquo;Is it worth the licence cost?&rdquo;",
     "a fair question and often the answer is not for everyone. It suits some roles considerably better than others.",
     "Pilot it with a small group and measure. Rolling it out to every user because it is available is how businesses end up paying for capability nobody uses."),
    ("&ldquo;It summarised a meeting incorrectly&rdquo;",
     "a transcript being interpreted, not a record being reproduced. Summaries are useful and they are not minutes.",
     "Treat output as a draft that a person checks. This is worth stating explicitly, because a confidently written summary reads as authoritative regardless of its accuracy."),
    ("&ldquo;Where does our data actually go?&rdquo;",
     "a question worth asking of any tool. Copilot operates within your Microsoft 365 tenancy under its existing controls, which is different from a public AI service and is the main reason it is often the appropriate choice.",
     "Understand the boundary and set expectations from it. For businesses handling client or health information this is usually the deciding factor between Copilot and a public tool."),
]

EXAMPLE_1 = example(
    "The salary spreadsheet Copilot found in about four seconds",
    "A business of sixty staff enabled Copilot for a pilot group of eight. Within the first week, a participant asked it a general question about staff costs and received a precise answer drawn from a spreadsheet they should never have been able to open.",
    "The file had been placed in a SharePoint site shared with all staff four years earlier, during a reorganisation, by someone who no longer worked there. Every employee had been able to open it for four years. Nobody had, because nobody knew it was there. Copilot had not been given access to anything &mdash; it had made four years of misconfigured access instantly discoverable.",
    "Paused the pilot, audited sharing across the tenancy, which found a further eleven locations containing material shared far more broadly than intended, corrected the permissions, and reviewed link-sharing defaults.",
    "The pilot resumed a fortnight later. The permissions problem had existed for four years and would have continued indefinitely &mdash; enabling Copilot was, in effect, an unusually fast audit.")

EXAMPLE_2 = example(
    "Twenty-two licences, six people who benefited",
    "A business had licensed Copilot for everyone on the reasoning that it should be available to all. Six months later, usage was concentrated in a handful of people and the finance director was questioning the spend.",
    "Measuring actual use, six roles were using it daily and getting real value &mdash; those writing documents, summarising long threads and preparing reports. The remainder had roles that involved little of that, had tried it briefly and had no ongoing use for it. Nobody had been shown what it was good at; licences had simply appeared.",
    "Ran short role-specific sessions showing each group the two or three tasks it genuinely helps with, then re-measured after a month and reduced the licence count to the roles where use had held up.",
    "Twelve licences retained, ten released, and adoption among the twelve considerably higher than before. The recommendation to buy fewer licences was the useful part of the engagement.")

EXAMPLE_3 = example(
    "Deciding it was not the right tool yet",
    "A healthcare provider wanted Copilot for its administrative staff, principally for correspondence and summarising long documents. The use case was genuine and the time saving would have been real.",
    "The tenancy held clinical correspondence and patient information alongside general administrative material, in shared locations with permissions that had never been formally reviewed. Copilot would have operated within the tenancy and under its existing controls, which is the correct architecture &mdash; but those controls were not in a state anyone could vouch for, and the information involved was health information.",
    "Recommended deferring Copilot, and doing the permissions and information architecture work first: separating clinical from administrative material, reviewing access against roles, and establishing who should be able to reach what. Then reassessing.",
    "The provider did the underlying work over about four months and enabled Copilot afterwards for a defined group. The recommendation cost us a licence sale and several months, and it was the only defensible advice &mdash; enabling a discovery tool across information nobody had mapped is a decision that only looks bad afterwards.")
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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>How Copilot rollouts actually go wrong</h2>
      <p>Six issues. The first one is not really about Copilot at all, which is exactly what makes it dangerous.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a Copilot rollout looks like</h2>
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
        ('ISO/IEC 42001 AI Governance', '/iso-42001-ai-governance-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Trust centre', '/trust-centre')])
            + cta('Thinking about Copilot?', "Start with the permissions review. It's worth doing whether or not you deploy Copilot afterwards."),
}

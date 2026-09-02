from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;A supplier emailed us new bank details&rdquo;",
     "business email compromise until proven otherwise. It is the single most common way money leaves an agency, and the email is usually genuine in every respect except the account number.",
     "Verify by phone on a number you already hold &mdash; never one from the email &mdash; before changing any payment detail. Make that a rule that applies to everyone including a director, because the request will eventually appear to come from one."),
    ("&ldquo;Our property manager&rsquo;s mailbox is sending things nobody wrote&rdquo;",
     "a compromised mailbox. Attackers usually sit quietly for weeks reading correspondence to learn how the agency writes and when settlements occur before sending anything.",
     "Contain the mailbox, force a password reset, revoke active sessions and check for forwarding rules the attacker left behind. The forwarding rule is the part most often missed, and it is how they get back in."),
    ("&ldquo;Agents use their own phones and laptops for everything&rdquo;",
     "the nature of the job rather than a failing. Agents work from cars, open homes and kitchen tables, and the agency has little visibility of any of it.",
     "Secure the accounts rather than trying to control the devices. Multi-factor authentication on every mailbox does more for an agency than any device policy, because it survives a phone left in a caf&eacute;."),
    ("&ldquo;The CRM and the portals have stopped talking&rdquo;",
     "an integration broken by a password change, an expired token, or an upgrade at one end. Listings silently stop syncing and nobody notices until a vendor asks why their property is not showing.",
     "Check the integration status rather than the listing. These failures are silent by design, so the fix is monitoring them rather than waiting for a complaint from a vendor."),
    ("&ldquo;Trust account reconciliation doesn&rsquo;t match&rdquo;",
     "usually an accounting question rather than an IT one &mdash; but occasionally the first visible sign of a payment redirected weeks earlier.",
     "Rule out the security explanation early rather than late. If a payment was misdirected, the difference between finding it in days and finding it at reconciliation is often the difference between recovering the money and not."),
    ("&ldquo;Everyone knows the office computer password&rdquo;",
     "a shared machine at reception that became a shared everything. It usually holds saved logins to the CRM, the portals and sometimes the banking.",
     "Separate the accounts and remove saved credentials from shared machines. An agency&rsquo;s front desk computer is frequently the least protected device holding the most valuable access."),
]

EXAMPLE_1 = example(
    "The settlement email that was watched for five weeks",
    "A Gold Coast agency was contacted by a purchaser asking why the deposit had not been acknowledged. It had been paid &mdash; to an account the agency had never held.",
    "A sales agent&rsquo;s mailbox had been accessed five weeks earlier through a password reused from a breached website. The attacker had read correspondence quietly for over a month, learned the agency&rsquo;s tone and its settlement timing, and then sent a single message from the genuine mailbox with altered account details, timed for the afternoon before settlement. A forwarding rule had been quietly deleting the replies so the agent never saw the conversation.",
    "Contained the mailbox, revoked every active session, removed the forwarding rule, enforced multi-factor authentication across the agency the same day, and produced a written technical account for the agency&rsquo;s insurer and lawyer.",
    "Partial recovery was achieved because the bank was notified within hours rather than days. Multi-factor authentication would have prevented the whole thing and had been on a to-do list for two years, which is the part the principal found hardest.")

EXAMPLE_2 = example(
    "Six weeks of listings that never reached the portals",
    "An agency noticed a vendor complaint about a property not appearing on a major portal. Checking further, several listings were affected, and nobody could say for how long.",
    "The integration between the agency&rsquo;s CRM and the portal had stopped authenticating six weeks earlier following a password change made during an unrelated staff departure. Listings entered into the CRM appeared correct at the agency&rsquo;s end. Nothing had reached the portal since, and no error had been surfaced to anyone.",
    "Restored the integration, re-published the affected listings, and set up monitoring that alerts on a failed sync rather than relying on a vendor to notice.",
    "The agency now finds out within the hour instead of after six weeks. The commercial cost of a listing that is not visible is difficult to calculate and easy to imagine.")

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
    "description": "IT support for Gold Coast real estate agencies. Trust accounts make agencies a specific target for payment redirection fraud.",
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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The problems we are actually called to in agencies</h2>
      <p>Agencies lose money in a small number of predictable ways, and one of them accounts for most of it.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What this looks like in an agency</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + f'''
<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Case study</span>
      <h2>31 workstations, one day</h2>
      <p>How bcom ICT relocated Grow&amp;Co Property Agents&rsquo; Southport office &mdash; the whole fleet moved,
      built to their seating plan and working the next business day.
      <a href="/office-relocation-case-study-southport">Read the case study</a>.</p>
    </div>
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Cybersecurity Risk Assessment', '/cybersecurity-health-check-for-small-business-gold-coast'),
        ('Microsoft 365 Setup & Support', '/microsoft-365-setup-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Cyber Incident Response', '/cyber-incident-response-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('Is MFA on every mailbox in your agency?', "If you're not certain, that's the thing to check today. We'll tell you where the gaps are."),
}

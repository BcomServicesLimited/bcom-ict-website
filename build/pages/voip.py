from layout import cta, faq_block, related, svc_body, price_table, issues, example

COMMON_ISSUES = [
    ("&ldquo;Callers say we sound robotic&rdquo;",
     "jitter. The voice packets are arriving, but unevenly, and the handset is filling the gaps with guesswork. Usually another device on the network taking capacity without asking.",
     "Prioritise voice traffic on the switching and the router so calls are never made to queue behind a file upload. This is a configuration problem, not a bandwidth problem, and adding internet speed rarely fixes it."),
    ("&ldquo;Calls drop after about fifteen minutes&rdquo;",
     "the router closing the connection because it believes the call has finished. A firewall or NAT timeout expiring mid-conversation, almost always on consumer-grade equipment.",
     "Adjust the timers so the session is held open for the length of a real conversation. A fault that reliably occurs at the same elapsed time is a timer somewhere, and it is very fixable once identified."),
    ("&ldquo;We can hear them but they can&rsquo;t hear us&rdquo;",
     "one-way audio &mdash; the return path is blocked. A firewall permitting the call to be set up while quietly dropping the media coming the other way.",
     "Open the correct media path rather than opening the firewall generally. One-way audio has a small number of causes and is usually resolved in a single visit once someone knows to look at the return path."),
    ("&ldquo;Our numbers didn&rsquo;t come across&rdquo;",
     "a port that was submitted with details not matching the losing provider&rsquo;s records exactly &mdash; a trading name instead of the registered entity, or a service address changed years ago and never updated.",
     "Check the account details against the provider&rsquo;s records before submitting, not after rejection. Most porting delays are administrative and entirely avoidable, and they are the single most common cause of a phone cutover running late."),
    ("&ldquo;It works on the desk phone but not the mobile app&rdquo;",
     "the app moving between the office wireless and the mobile network mid-call, or a phone aggressively sleeping the app to save battery.",
     "Configure the app for the way it is actually used and set the handover behaviour deliberately. Mobile softphones work well when set up properly and badly when installed and left at defaults."),
    ("&ldquo;Nobody knows how to change the after-hours message&rdquo;",
     "a system configured by someone who never handed it over. The capability is there and the knowledge left with the installer.",
     "Document the call flow, show the people who will actually need to change it, and leave written instructions. A phone system that only its installer can operate is a dependency, not a service."),
]

EXAMPLE_1 = example(
    "Porting done properly means nobody notices",
    "A dental practice was moving off an ageing on-premises system. Their main number had been advertised for nineteen years, appeared on every referral pad in the district, and could not be off for so much as an afternoon.",
    "The account was registered to a partnership that had been restructured into a company eleven years earlier. The losing provider&rsquo;s records still showed the original entity. Submitting the port as it stood would have been rejected, and each rejection adds days.",
    "Reconciled the account details with the losing provider before submitting anything, staged the handsets and call flow in advance so the system was fully configured and tested before the cutover, and scheduled the port for a Tuesday morning with the old system still live alongside it.",
    "The number moved without a missed call. The practice was on the new system inside two hours, and the only thing patients noticed was that the hold music changed.")

EXAMPLE_2 = example(
    "Six people, five vehicles, one number",
    "A trades business was losing work because calls to the office went unanswered while everyone was on site. Their answer had been to publish mobile numbers, which meant customers reached whoever they had called last rather than whoever was available.",
    "There was no shortage of phones &mdash; there was no call flow. Every incoming call rang one handset in an empty office and then went to a voicemail box nobody checked until the evening.",
    "Set up a hunt group ringing the office and the mobile app on every phone simultaneously, with a voicemail-to-email fallback and an after-hours message stating when calls would be returned. No desk handsets were purchased, because none were needed.",
    "Calls now get answered by whoever is free, from a vehicle or a site, and the customer keeps dialling one number. Hardware cost was nil; the whole change was configuration and a fortnight of getting used to it.")

FAQS = [   (   'How much does a VoIP phone system cost for a small business?',
        'Cost depends on how many extensions you need, whether you keep or replace handsets, and what call flows are involved. bcom ICT quotes after understanding how your business takes calls, and '
        'tests your internet connection before recommending a move — a VoIP system on an inadequate connection is a bad outcome regardless of price. Call 07 3041 8993.'),
    (   'Will we keep our existing phone numbers?',
        'Yes. Number porting is a standard part of the job and it is planned and started ahead of cutover rather than attempted on the day. Losing a number that is on your signage and website is not '
        'something anyone should have to accept.'),
    (   'What happens to our phones if the internet goes down?',
        'Calls fail over automatically to mobiles, so you keep trading. We usually pair that with a 4G or 5G backup connection for the site. It is worth configuring before you switch rather than '
        'after the first outage.'),
    (   'Can staff take calls from home?',
        'Yes — that is one of the main reasons businesses move. An extension works from a handset in the office, a laptop at home, or a mobile app, with the same number and the same call flows.'),
    (   'Do we have to buy new handsets?',
        'Not always. Some existing handsets can be reused depending on make and model. Where they cannot, we will tell you what is required and why rather than replacing everything by default.'),
    (   'Does it work with Microsoft Teams?',
        'It can. Teams calling suits businesses already living in Microsoft 365 and wanting one application for chat, meetings and calls. It suits reception-heavy operations less well, where proper '
        "handsets and queues usually win. We'll walk you through both.")]

PRICING = [
    ('Five-handset system', 'from around $2,250', '+ GST &middot; indicative only',
     [
      'Five business-grade handsets supplied, configured and installed',
      'Your existing numbers ported across',
      'Call flow, hunt groups and after-hours routing set up',
      'Staff shown how to actually use it',
      'Monthly service and call plan quoted alongside, not included',
     ]),
]

PAGE = {
    "path": '/voip-phone-system-installation-and-support-gold-coast',
    "priority": '0.8',
    "service": 'VoIP Phone System Gold Coast',
    "title": "VoIP Phone Systems Gold Coast | bcom ICT",
    "description": "Cloud VoIP phone systems for Gold Coast businesses — lower call costs, remote extensions, call queues, IVR menus. Call 07 3041 8993.",
    "hero_img": 'voip-phone-system-hero.webp',
    "hero_alt": 'VoIP handsets and phone system installed by bcom ICT for a Gold Coast business',
    "h1": 'Cloud phone systems, ported properly',
    "lede": 'Extensions that work from home, queues so nobody hits an engaged tone, and your existing numbers brought across without drama.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Number porting included', 'Remote extensions', 'Failover to mobiles', 'Since 2011'],
    "crumbs": [('Services', '/services'), ('Cloud PBX — our own platform', '/cloud-pbx-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('VoIP', '/voip-phone-system-installation-and-support-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT installs and supports cloud VoIP phone systems for Gold Coast businesses — handsets, call flows, queues, IVR menus, voicemail-to-email and remote extensions for staff working from home — including full porting of existing business numbers. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Staff can work anywhere',
                                         None,
                                         'An extension follows the person rather than the desk. Someone '
                                         'working from home or from a second site is on the same system '
                                         'with the same number.'),
                                 (       'Calls stop being missed',
                                         None,
                                         'Queues, ring groups and overflow rules mean calls land somewhere '
                                         'sensible instead of hitting an engaged tone or a voicemail '
                                         'nobody checks.'),
                                 (       'Call costs drop',
                                         None,
                                         'Usually the reason people start looking. It is rarely the reason '
                                         'they are glad they moved.'),
                                 (       'Adding a person takes minutes',
                                         None,
                                         'New starter, new extension. No technician visit, no programming '
                                         'call, no waiting a week.'),
                                 (       'Voicemail arrives as email',
                                         None,
                                         'Audio file in the inbox, so messages get actioned rather than '
                                         'sitting on a handset nobody is sitting at.'),
                                 (       "You can see what's happening",
                                         None,
                                         'Call volumes, missed calls, how long people waited. Most '
                                         'businesses have never had that visibility and find it more '
                                         'useful than expected.')],
                'cols': 3,
                'eyebrow': 'What changes',
                'h2': 'What businesses actually notice after moving'},
        {       'h2': 'Getting it right',
                'ticks': [       '<strong>We test your internet first.</strong> VoIP is only as good as '
                                 'the connection underneath it. This is the single biggest determinant of '
                                 "whether you're happy afterwards.",
                                 '<strong>Voice traffic gets prioritised</strong> on your network, so a '
                                 "large upload doesn't turn a client call to noise.",
                                 '<strong>Number porting is planned ahead</strong>, not attempted on the '
                                 'day. You keep the numbers on your signage and your website.',
                                 '<strong>Failover to mobiles</strong> is configured, so an internet '
                                 "outage doesn't take your phones with it.",
                                 '<strong>Call flows are designed with you</strong> — who rings first, '
                                 'what happens after hours, where overflow goes.',
                                 '<strong>We train your people</strong>. A system nobody knows how to '
                                 'transfer a call on is not a working system.']},
        {       'h2': 'Is VoIP right for you?',
                'html': '<p style="max-width:68ch">Not always, and we will say so. VoIP makes clear sense '
                        'when you need staff working remotely, you are opening a second site, your '
                        'hardware is failing, or your call costs are high.</p><p '
                        'style="max-width:68ch;margin-top:16px">It makes less sense when you have a '
                        'working <a href="/pabx-phone-systems-gold-coast">on-premise PBX</a> with years '
                        'left in it and a lot of handsets, or when your internet connection is genuinely '
                        'unreliable and cannot be improved. In both cases we would rather tell you than '
                        'sell you a migration you regret.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>How much does a business phone system cost?</h2>
      <p>An indicative figure for a described system, so you can judge whether to have the conversation. The quote comes after we know what you need and what is being replaced.</p>
    </div>
    {price_table(PRICING, note='This is an indicative planning figure for the system described above, not a quote and not a per-handset rate. Hardware and installation are quoted as a one-off fixed price once we know how many extensions you need and what is being replaced, and that price is agreed before we start. The monthly service and call plan is separate and depends on how many numbers and concurrent calls you need &mdash; we quote it alongside the install so you are looking at the whole cost rather than the attractive half of it. A business that does not want desk phones can run softphones on the computers and mobiles it already owns, which removes the hardware line entirely and leaves only the installation.')}
  </div>
</section>
'''
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The phone faults we are actually called to</h2>
      <p>VoIP problems have a small number of causes, and almost none of them are solved by buying more internet.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a phone cutover actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([('VoIP vs on-premises PBX', '/voip-vs-pbx-phone-systems'),
               ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Business WiFi', '/business-wifi-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('Panasonic PBX', '/panasonic-pbx-gold-coast'),
        ('NEC PBX', '/nec-pbx-gold-coast')])
            + cta('Thinking about moving your phones?', "We'll test your connection first and tell you honestly whether it's ready — that's the part that decides how this goes."),
}

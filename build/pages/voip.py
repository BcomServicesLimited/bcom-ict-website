from layout import cta, faq_block, related, svc_body, price_table

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
    ('Installation, per handset', '$100', '+ GST',
     [
      'Handset provisioned, configured and tested',
      'Your existing numbers ported across',
      'Call flow, hunt groups and after-hours routing set up',
      'Staff shown how to actually use it',
     ]),
    ('VoIP handset', '$350', '+ GST each',
     [
      'Business-grade desk handset',
      'Configured before it arrives on your desk',
      'Works the same from the office or from home',
      'Warranty handled by us rather than by you',
     ]),
    ('Typical five-extension system', '$2,250', '+ GST, hardware included',
     [
      'Five handsets at $350 + GST each',
      'Installation and configuration at $500 + GST',
      'Numbers ported and call flow configured',
      'Monthly service and call plan quoted separately',
     ]),
]

PAGE = {
    "path": '/voip-phone-system-installation-and-support-gold-coast',
    "priority": '0.8',
    "service": 'VoIP Phone System Gold Coast',
    "title": 'VoIP Phone Systems Gold Coast — Installed & Supported | bcom ICT',
    "description": 'Cloud VoIP phone systems for Gold Coast businesses — lower call costs, remote extensions, call queues, IVR menus, voicemail-to-email and full number porting. Call 07 3041 8993.',
    "hero_img": 'voip-phone-system-hero.webp',
    "hero_alt": 'VoIP handsets and phone system installed by bcom ICT for a Gold Coast business',
    "h1": 'Cloud phone systems, ported properly',
    "lede": 'Extensions that work from home, queues so nobody hits an engaged tone, and your existing numbers brought across without drama.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Number porting included', 'Remote extensions', 'Failover to mobiles', 'Since 2011'],
    "crumbs": [('Services', '/services'), ('Business Phone Systems', '/business-phone-systems-gold-coast'), ('VoIP', '/voip-phone-system-installation-and-support-gold-coast')],
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
      <p>Handsets and installation are fixed price. The monthly plan is quoted alongside it.</p>
    </div>
    {price_table(PRICING, note='Hardware and installation are a one-off fixed price, agreed before we start. The monthly service and call plan is separate and depends on how many numbers and concurrent calls you need &mdash; we quote it alongside the install so you are looking at the whole cost rather than the attractive half of it. A business that does not want desk phones can run softphones on the computers and mobiles it already owns, which removes the hardware line entirely and leaves only the installation.')}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Business WiFi', '/business-wifi-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta('Thinking about moving your phones?', "We'll test your connection first and tell you honestly whether it's ready — that's the part that decides how this goes."),
}

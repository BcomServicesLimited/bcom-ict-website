from layout import cta, faq_block, related, svc_body, models, issues, example

COMMON_ISSUES = [
    ("&ldquo;Some handsets work and some don&rsquo;t&rdquo;",
     "a mixed estate. These systems are frequently deployed with both IP and digital handsets, and a fault affecting only one kind points somewhere quite specific.",
     "Establish which group is affected before investigating anything. IP handsets failing while digital ones work points at the network; the reverse points at cards or cabling, and knowing which halves the diagnosis immediately."),
    ("&ldquo;The web administration page won&rsquo;t load&rdquo;",
     "an address that changed, a browser that no longer supports how the interface was built, or a management network that was never reachable from where you are trying.",
     "Reach it from the right place with a suitable browser. Administration interfaces on systems of this generation frequently outlive the browsers they were designed for, which is a very common reason people believe a system has failed."),
    ("&ldquo;Remote extensions keep dropping&rdquo;",
     "the connection between the extension and the system rather than either end &mdash; usually a firewall closing a session it believes has finished.",
     "Adjust the session handling so a connection is held open for the length of a real working day. Remote extensions that drop at predictable intervals are almost always a timer."),
    ("&ldquo;It lost its configuration after a power event&rdquo;",
     "a system that came back to an earlier saved state, or one where a recent change was never committed to permanent storage.",
     "Restore from the most recent good configuration and confirm it is actually being saved. Systems where changes were made but never written are a genuinely common and entirely avoidable loss."),
    ("&ldquo;Nobody documented the numbering plan&rdquo;",
     "extensions, hunt groups, pickup groups and routing built up over years by different hands with nothing written down.",
     "Extract it from the system and write it down. Every subsequent change becomes an ordinary task instead of an investigation, and it is yours whether or not we do the work."),
    ("&ldquo;We want to move to VoIP but keep the handsets&rdquo;",
     "a reasonable instinct, since the handsets are usually the visible cost. Whether it is possible depends on the handsets and how the system is licensed.",
     "Establish what your specific handsets support before planning around it. Sometimes they can carry across, sometimes they cannot, and the answer changes the shape of the whole project."),
]

EXAMPLE_1 = example(
    "IP handsets failing while the digital ones were perfect",
    "A business reported that about half its handsets dropped calls intermittently while the rest were faultless. The affected handsets were spread across the building with no obvious pattern, and the system had been examined twice.",
    "Every affected handset was an IP extension and every unaffected one was digital. The digital handsets connected directly to the system and were unaffected by the network; the IP handsets crossed a switch that had a failing uplink, which lost packets under load. The phone system was working perfectly and had been the only thing anyone had looked at.",
    "Replaced the failing uplink and prioritised voice traffic across the switching so calls could not queue behind other traffic.",
    "The dropouts stopped. Splitting the fault by handset type took about ten minutes and pointed straight out of the phone system, which is where the problem had been the whole time.")

EXAMPLE_2 = example(
    "Changes that had never been saved",
    "A business lost several months of phone system configuration after a power interruption &mdash; call routing, hunt group membership and greetings all reverted to an older arrangement nobody recognised.",
    "Changes had been made over that period through the administration interface and applied to the running system without ever being written to permanent storage. Everything worked while the system stayed powered, and the system had stayed powered for eight months. The interruption simply revealed what had been true throughout.",
    "Rebuilt the configuration from what staff could describe and from call records, then wrote it to permanent storage, took an off-system backup of it, and showed the business how to confirm a change has actually been saved.",
    "The configuration now survives a power event and there is a copy held off the system. The loss was avoidable and had been sitting there for eight months waiting for a blackout.")

FAQS = [   (   'Who services LG Ericsson phone systems on the Gold Coast?',
        'bcom ICT supplies, installs, programmes and repairs LG Ericsson PBX systems across the Gold Coast, covering iPECS eMG80, eMG100, UCP and the earlier LIK and ipLDK platforms, plus the current and '
        'legacy handset ranges. That includes extension changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 '
        '8993.'),
    (   'Do you support older LG Ericsson systems, not just current models?',
        'Yes — the legacy platforms are a large part of what we do. As providers move to cloud-only, plenty of Gold Coast businesses are left with a working system and nobody willing to attend. If '
        'your model is listed on this page, we service it.'),
    (   'Our provider says it has to be replaced. Is that true?',
        "Sometimes, but frequently it reflects who is available rather than the system's condition. If the platform still does what your business needs and parts are obtainable, keeping it is often "
        "the cheaper answer. We'll assess remaining life honestly before you commit to a replacement quote."),
    (   'Can you just make one change without an ongoing contract?',
        "Yes. Plenty of clients call for a one-off — an extension, a call flow, an after-hours message — at $190 + GST per hour plus a $100 + GST call-out for on-site attendance. There's no "
        'requirement to sign up to anything ongoing.'),
    (   'Can you still get parts and handsets?',
        "For most LG Ericsson platforms listed here, yes — new, refurbished or from stock. Tell us the exact model and we'll tell you honestly what's obtainable and what isn't. Where a part "
        "genuinely can't be sourced, that's the point at which replacement stops being optional and becomes a planning exercise."),
    (   'Can it connect to SIP trunks?',
        "Where the platform and card configuration support it, yes — and it often defers a full replacement by years while reducing call costs. We'll tell you whether your specific model can do it "
        'before quoting anything.'),
    (   'Can you move it to a new office?',
        'Yes. PBX relocation, recabling and number porting are handled as part of an office IT relocation, planned around your move date rather than attempted on the day.')]

PAGE = {
    "path": '/lg-ericsson-pbx-gold-coast',
    "priority": '0.7',
    "title": "LG Ericsson PBX Support Gold Coast | bcom ICT",
    "description": "LG Ericsson phone system programming, repair and support on the Gold Coast — iPECS eMG80, eMG100, UCP and the earlier LIK and ipLDK platforms.",
    "hero_img": 'lg-ericsson-pbx-gold-coast-hero.webp',
    "hero_alt": 'A LG Ericsson PBX phone system being programmed by bcom ICT on the Gold Coast',
    "h1": 'LG Ericsson systems, supplied and supported',
    "lede": 'eMG80 · UCP600 · LIP-9030 · ipLDK. New systems specified and installed, existing ones programmed and repaired — including the platforms most providers have walked away from.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['New systems supplied', 'Current + legacy models', 'Parts sourced', 'Honest advice'],
    "crumbs": [('Services', '/services'), ('PBX Systems', '/pabx-phone-systems-gold-coast'), ('LG Ericsson', '/lg-ericsson-pbx-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT supplies, installs, programmes and repairs LG Ericsson PBX phone systems across the Gold Coast, covering iPECS eMG80, eMG100, UCP and the earlier LIK and ipLDK platforms, along with the current and legacy handset ranges. Work includes extension adds and changes, call flow and hunt group programming, voicemail and auto-attendant configuration, fault diagnosis and parts sourcing. Call 07 3041 8993.',
                     blocks=[       {       'eyebrow': 'Models',
                'h2': 'Every LG Ericsson system and handset we work on',
                'html': models([('Current systems', 'The current iPECS range, on-premise and cloud.', ['iPECS eMG80', 'iPECS eMG100', 'iPECS UCP100', 'iPECS UCP600', 'iPECS UCP2400', 'iPECS ONE', 'iPECS Cloud']), ('Legacy systems — still serviced', 'Earlier Ericsson-LG and LG-Nortel platforms. Common across older Gold Coast installs.', ['iPECS LIK-100', 'LIK-300', 'LIK-600', 'LIK-1200', 'iPECS MG100', 'MG300', 'ipLDK-20', 'ipLDK-60', 'ipLDK-100', 'ipLDK-300', 'GDK-100', 'GDK-162']), ('Current handsets — 1000i & LIP-9000', 'The current desk range.', ['1010i', '1020i', '1030i', '1040i', '1050i', 'LIP-9002', 'LIP-9008', 'LIP-9010', 'LIP-9020', 'LIP-9030', 'LIP-9040', 'LIP-9070']), ('Legacy handsets — LIP-8000 & LDP', 'Older IP and digital sets. Frequently what is actually on the desk.', ['LIP-8002', 'LIP-8004', 'LIP-8008', 'LIP-8012', 'LIP-8024', 'LIP-8040', 'LDP-7004', 'LDP-7008', 'LDP-7016', 'LDP-7024', 'LDP-9008', 'LDP-9030', 'LDP-9240']), ('DECT and wireless', 'Cordless handsets and repeaters.', ['GDC-450H', 'GDC-480H', 'GDC-500H', 'GDC-800H', 'W-SOHO', 'WIT-400HE'])]),
                'sub': 'Search for whatever is written on the box or the handset — if it is listed here, '
                       'we service it.'},
        {       'cards': [       (       'Adds, moves and changes',
                                         None,
                                         'New starters, departures, desk swaps, extension reassignments. '
                                         'The everyday work that becomes impossible when nobody will '
                                         'attend.'),
                                 (       'Call flows and after-hours',
                                         None,
                                         'Ring order, hunt groups, overflow, holiday messages and the '
                                         'after-hours greeting nobody can work out how to change.'),
                                 (       'Voicemail and auto-attendant',
                                         None,
                                         'Menu programming, recorded announcements, mailbox resets, and '
                                         'voicemail-to-email where the platform supports it.'),
                                 (       'Faults, handsets and parts',
                                         None,
                                         'Diagnosis, card and handset replacement, and sourcing parts for '
                                         "platforms no longer sold new. Tell us the model and we'll tell "
                                         "you honestly what's obtainable.")],
                'cols': 2,
                'eyebrow': 'What we do',
                'h2': 'The work people call about',
                'icon': False},
        {       'h2': 'Should you replace it?',
                'html': '<p style="max-width:68ch">iPECS is a capable platform that is rarely worth '
                        'replacing while it works. Most of the replacement quotes we review for iPECS '
                        "sites are driven by who is available, not by the system's condition.</p><p "
                        'style="max-width:68ch;margin-top:16px">Our position: if the platform still does '
                        'what your business needs and parts are obtainable, keeping it is usually cheaper '
                        'and we will say so. Replacement becomes right when hardware is failing, when you '
                        'need staff working from home, when you are opening a second site, or when parts '
                        'genuinely run out.</p><p style="max-width:68ch;margin-top:16px">Where the system '
                        'supports SIP trunks, connecting it to them often defers replacement by years '
                        'while cutting call costs. When the time does come, <a '
                        'href="/voip-phone-system-installation-and-support-gold-coast">moving to cloud '
                        'VoIP</a> becomes a planned capital decision rather than a forced one — and we '
                        'test whether your internet is actually ready before recommending it.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The LG Ericsson problems we are actually called to</h2>
      <p>Six situations. The first one usually points straight out of the phone system.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What LG Ericsson work actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('PBX Systems', '/pabx-phone-systems-gold-coast'),
        ('Business Phone Systems', '/business-phone-systems-gold-coast'),
        ('VoIP Phone Systems', '/voip-phone-system-installation-and-support-gold-coast'),
        ('Phone Line Installation & Cabling', '/phone-line-installation-cabling-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast'),
        ('Telecommunications Contractor', '/telecommunications-contractor-gold-coast')])
            + cta('Got a LG Ericsson system nobody will touch?', "Tell us the model number. If it's on the list above, you probably don't need the replacement you've been quoted."),
}

from layout import MARK, cta, faq_block, cards, ticks, related, photo, trust_note

OPTIONS = [
    ("Cloud VoIP", None,
     "The phone system lives in the cloud rather than in your comms room. Staff can take an extension home, calls route wherever people are, and there's no hardware to fail or replace. This is what most Gold Coast businesses move to now."),
    ("On-premise PBX", None,
     "A physical system in your building. Still the right answer for some sites — particularly where internet reliability is poor, or where you already have a working system and a lot of handsets."),
    ("Keeping what you've got", None,
     "If your existing PBX works, replacing it may be a waste of money. We support LG Ericsson iPECS, Panasonic KX, NEC UNIVERGE and Alcatel-Lucent systems that other providers have walked away from."),
]

FEATURES = [
    "Call queues, so nobody hits an engaged tone",
    "Auto-attendant menus — press 1 for accounts, and so on",
    "Voicemail delivered to email as an audio file",
    "Extensions that work from home or a second site",
    "Ring groups so the right team picks up",
    "Hunt and overflow rules for after hours",
    "Call recording where you need it for compliance",
    "Full number porting — you keep your existing numbers",
]

FAQS = [
    ("Who installs business phone systems on the Gold Coast?",
     "bcom ICT supplies, installs and supports business phone systems across the Gold Coast — cloud VoIP, hosted PBX and on-premise systems. bcom ICT also maintains legacy PBX systems including LG Ericsson iPECS, Panasonic KX, NEC UNIVERGE and Alcatel-Lucent OmniPCX. Call 07 3041 8993."),
    ("Should we move to VoIP or keep our PBX?",
     "If your current system works and you have a lot of handsets, keeping it is often the cheaper answer and we'll say so. VoIP makes sense when you need staff working from home, you're opening a second site, your hardware is failing, or your call costs are high. What usually decides it is whether your internet connection is reliable enough — which we can test before you commit."),
    ("Will we keep our existing phone numbers?",
     "Yes. Number porting is a standard part of the job and it's handled before cutover, not after. Losing a business number that's been on your signage and website for years is not something anyone should have to accept."),
    ("Do you still service old phone systems?",
     "Yes, and it's one of the things that sets us apart. A lot of providers won't touch legacy PBX any more, which leaves businesses with a working system and nobody to program it. We maintain LG Ericsson iPECS, Panasonic KX-NS, KX-TDA and KX-TDE, NEC UNIVERGE SV9100, SV8100 and SL2100, and Alcatel-Lucent OmniPCX and OXO Connect."),
    ("What happens if the internet goes down?",
     "With cloud VoIP, calls can be set to fail over automatically to mobiles so you keep trading. We usually pair that with a 4G or 5G backup connection for the site. It's worth planning before you switch, not after the first outage."),
    ("Can you do the phone cabling as well?",
     "Yes, as part of the job. Fixed cabling connected to the telecommunications network legally requires a registered cabler in Australia, so that portion is carried out by ACMA registered cabling contractors we engage and manage. You get testing and certification documentation on handover, and one point of contact for the whole install rather than three."),
    ("Does the phone system connect to Microsoft Teams?",
     "It can. Teams calling suits businesses already living in Microsoft 365 and wanting one app for chat, meetings and calls. It doesn't suit every business — reception-heavy operations often still want proper handsets and queues. We'll walk you through both."),
]

PAGE = {
    "path": "/business-phone-systems-gold-coast",
    "priority": "0.85",
    "service": "Business Phone System Installation Gold Coast",
    "title": "Business Phone Systems Gold Coast — VoIP & PBX | bcom ICT",
    "description": "Business phone systems installed and supported across the Gold Coast — cloud VoIP, hosted and on-premise PBX, number porting. Legacy PBX support included. Call 07 3041 8993.",
    "hero_img": "business-phone-systems-hero.webp",
    "hero_alt": "Business VoIP handsets installed by bcom ICT at a Gold Coast office reception",
    "h1": "Business phone systems, installed and supported",
    "lede": "Cloud VoIP, hosted PBX and on-premise systems across the Gold Coast — plus support for the legacy systems most providers have walked away from.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Number porting included", "Legacy PBX supported", "Certified cabling contractors", "Local since 2011"],
    "crumbs": [("Services", "/services"), ("Business Phone Systems", "/business-phone-systems-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT supplies, installs and supports business phone systems across the Gold Coast —
    cloud VoIP, hosted PBX and on-premise systems — handling handsets, call flows and number porting end to
    end. bcom ICT also maintains legacy PBX systems including LG Ericsson iPECS, Panasonic KX, NEC UNIVERGE
    and Alcatel-Lucent OmniPCX. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Three options</span>
      <h2>Which kind of system suits you</h2>
      <p>There's no universally right answer here, and anyone telling you there is has one thing to sell.</p>
    </div>
    <div class="grid grid--3">{cards(OPTIONS)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <span class="eyebrow">What you get</span>
        <h2>The features businesses actually use</h2>
        <p style="margin-top:16px">Modern systems come with enormous feature lists. In practice this is the part that changes how your business runs day to day.</p>
        {ticks(FEATURES)}
      </div>
      {photo("business-phone-handsets-gold-coast.webp", "Business phone handsets supplied and configured by bcom ICT for a Gold Coast business", "Handsets, call flows and number porting are handled as one job.")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>The legacy systems we still support</h2>
    <p style="margin-top:16px">A working phone system that nobody will program is a genuinely frustrating position to be in. As providers have moved to cloud-only, plenty of Gold Coast businesses have been left with functioning hardware and no one to call when a staff member leaves and an extension needs changing.</p>
    <p style="margin-top:16px">We still service, program and maintain:</p>
    {ticks([
      "LG Ericsson iPECS",
      "Panasonic KX-NS, KX-TDA and KX-TDE",
      "NEC UNIVERGE SV9100, SV8100 and SL2100",
      "Alcatel-Lucent OmniPCX and OXO Connect",
    ])}
    <p style="margin-top:24px">If your system is on that list, you don't necessarily need to replace it. We'll tell you honestly how much life it has left and what the sensible timeline for replacement looks like — see <a href="/pabx-phone-systems-gold-coast">PBX systems</a> for detail.</p>

    <div class="rule">{MARK}</div>

    <h2>Getting the internet right first</h2>
    <p style="margin-top:16px">Cloud phone systems are only as good as the connection underneath them. Before any VoIP cutover we check your NBN or business internet service, look at whether your network prioritises voice traffic properly, and talk about failover so an outage doesn't take your phones down with your internet. That's usually a conversation about <a href="/nbn-internet-support-gold-coast">business NBN and internet</a> at the same time.</p>

    {trust_note('Internal phone and voice cabling is installed to Australian standards by ACMA registered cabling contractors we engage and manage, with testing and certification documentation provided on handover.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("VoIP Phone Systems", "/voip-phone-system-installation-and-support-gold-coast"),
  ("PBX Systems", "/pabx-phone-systems-gold-coast"),
  ("Phone Line Installation & Cabling", "/phone-line-installation-cabling-gold-coast"),
  ("Business NBN & Internet Support", "/nbn-internet-support-gold-coast"),
  ("Office Network Cabling", "/network-cabling-for-offices-gold-coast"),
  ("Business WiFi & Networks", "/business-wifi-gold-coast"),
])}

{cta("Talk to us about your phones",
     "Whether that's a new system, moving to the cloud, or keeping the one you have running for a few more years.")}
''',
}

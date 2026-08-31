from layout import MARK, cta, faq_block, cards, ticks, related, photo, trust_note
from site_data import SUBURBS

FIXES = [
    ("Computers and laptops", None,
     "Won't start, running slowly, blue screens, failed updates, dead drives. We repair business machines on site and leave a loan device if it needs to go away."),
    ("Servers", None,
     "Failures, storage filling up, backup errors, performance problems and the migrations businesses put off until something breaks."),
    ("Email and Microsoft 365", None,
     "Mail not sending or receiving, accounts locked out, mailboxes full, shared calendars misbehaving, Teams and SharePoint permissions."),
    ("Internet and networks", None,
     "Dropouts, slow speeds, devices that won't connect, WiFi dead spots, and NBN faults where you need someone to argue with the provider for you."),
    ("Printers and devices", None,
     "The perennial one. Network printers, scanners and shared devices that stop working for one person, or everyone, for no obvious reason."),
    ("Security incidents", None,
     "Suspicious emails, accounts you think have been accessed, ransom messages. Call us first and don't turn anything off — see what to do when you've been hacked."),
]

WHY = [
    ("Someone answers", "Business hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time. After hours that's our AI operator taking the details and escalating; during business hours it's us. You are not leaving a voicemail into the void."),
    ("We come to you", "We're on Ferny Avenue in Surfers Paradise, so on-site attendance across the Gold Coast is same-day in most cases rather than 'sometime next week'."),
    ("Remote first when it's faster", "Most faults don't need anyone on site. A secure screen share often has you working again in minutes, and there's no call-out on it."),
    ("Business only", "We work with businesses, so we understand that the real cost of the fault is your staff sitting idle — not the repair itself."),
]

FAQS = [
    ("Who provides IT support for businesses on the Gold Coast?",
     "bcom ICT has provided IT support to Gold Coast businesses since 2011, from an office at 9 Ferny Avenue, Surfers Paradise. The team attends sites from Coomera down to Coolangatta, with remote support available to businesses anywhere in Australia. Business hours are 8:00am to 5:00pm Monday to Friday, Brisbane time, and callbacks come within 4 business hours. Call 07 3041 8993."),
    ("How quickly can you get to us?",
     "Same-day on-site attendance is usually available across the Gold Coast, and remote support often starts within minutes of your call. Managed IT clients have a contracted 4-hour response for critical faults plus after-hours emergency attendance. For everyone else we call back within 4 business hours and book the visit."),
    ("Do you charge a call-out fee?",
     "On-site work carries a $100 + GST call-out ($110 inc GST) plus $198 + GST per hour ($217.80 inc GST), so a first hour on site is $298 + GST. Remote support is $198 + GST per hour with no call-out, which is why we try remote first when the fault allows it. Rates are agreed before we start, not after. Full detail on our pricing page."),
    ("Can you help if we already have an IT provider?",
     "Yes. Some businesses use us for a second opinion, for work their provider doesn't cover, or when they simply can't get hold of them. We'll be straight with you about whether the problem is the technology or the relationship."),
    ("What areas of the Gold Coast do you cover?",
     "All of it. On-site work regularly takes us to " + ", ".join(SUBURBS[:10]) + " and everywhere between. Remote and managed support is available Australia-wide."),
    ("Do you fix home computers?",
     "No. bcom ICT works with businesses. We do still install WiFi and mesh networks for home offices, but general home computer repair isn't something we take on."),
    ("What if the problem turns out to be something we can't fix today?",
     "You'll get a straight answer about what's wrong, what it costs to fix, and whether repairing or replacing is the better call. If a machine has to leave the site we'll leave you a loan device so somebody isn't sitting idle."),
]

PAGE = {
    "path": "/it-support-and-services-gold-coast",
    "priority": "0.9",
    "service": "Business IT Support Gold Coast",
    "title": "Business IT Support Gold Coast — Same-Day On-Site | bcom ICT",
    "description": "Business IT support across the Gold Coast — same-day on-site visits and remote help for small and medium businesses. Callback within 4 business hours, Mon–Fri 8am–5pm. Call 07 3041 8993.",
    "hero_img": "hero-bg-it-support.webp",
    "hero_alt": "A bcom ICT technician providing on-site IT support to staff in a Gold Coast business office",
    "h1": "Business IT support across the Gold Coast",
    "lede": "Something's broken and your staff can't work. Same-day on-site visits across the Gold Coast, or remote help that often has you going again in minutes.",
    "actions": [("Get help now", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Mon–Fri 8am–5pm", "Same-day on-site", "Local since 2011", "5.0 from 24 reviews"],
    "crumbs": [("Services", "/services"), ("Business IT Support", "/it-support-and-services-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides IT support to businesses across the Gold Coast, with same-day on-site
    attendance and remote support for small and medium businesses. Based at 9 Ferny Avenue, Surfers Paradise,
    bcom ICT has supported Gold Coast businesses since 2011. Business hours are 8:00am to 5:00pm Monday to
    Friday, Brisbane time, with callbacks within 4 business hours. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">What we fix</span>
      <h2>The things Gold Coast businesses call us about</h2>
      <p>If it's plugged in, connected, or stopping someone working, it's probably on this list.</p>
    </div>
    <div class="grid grid--3">{cards(FIXES)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why bcom ICT</span>
      <h2>What's different about calling us</h2>
    </div>
    <div class="grid grid--2">{cards(WHY, icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>Ad-hoc support, or someone looking after it properly?</h2>
        <p style="margin-top:16px">Both are legitimate. Which one suits you comes down to how much a day of downtime actually costs your business.</p>
        <p style="margin-top:16px"><strong>Ad-hoc support</strong> works when your setup is simple and an occasional problem is an annoyance rather than a crisis. You call, we come, you pay for the work. Nothing ongoing.</p>
        <p style="margin-top:16px"><strong><a href="/managed-it-services-for-small-businesses-gold-coast">Managed IT</a></strong> makes sense once you have a server, staff who can't work without their systems, or client data you'd struggle to prove is protected. Flat monthly fee, someone watching things continuously, and a contracted response time.</p>
        <p style="margin-top:16px">Most of our managed clients started as ad-hoc callers. We'll tell you honestly which one you need — including when the answer is that you don't need us monthly yet.</p>
      </div>
      {photo("hero-bg-onsite-technical-support.webp", "A bcom ICT technician working on a business computer at a client site on the Gold Coast", "On-site attendance across the Gold Coast is same-day in most cases.")}
    </div>

    <div class="rule">{MARK}</div>

    <h2>Where we go</h2>
    <p style="margin-top:16px">On-site work regularly takes us across the whole Gold Coast — {", ".join(SUBURBS[:14])} and everywhere between. Remote and managed support is available to businesses anywhere in Australia, which matters if your team is spread across more than one state.</p>

    {trust_note('Wondering what happens after you call? <a href="/service-levels-and-security">Our published service levels</a> set out response targets by priority, how escalation works, and what happens to your documentation if you ever leave.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
  ("Remote IT Support", "/remote-it-support-gold-coast"),
  ("On-site IT Support", "/on-site-technical-support-gold-coast"),
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
  ("Business WiFi & Networks", "/business-wifi-gold-coast"),
  ("What to do when you've been hacked", "/what-to-do-when-hacked"),
])}

{cta("Need someone today?",
     "Call and a person will pick up. If it can be fixed remotely we'll often have you working again before a technician could reach the car park.")}
''',
}

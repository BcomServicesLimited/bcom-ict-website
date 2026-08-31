from layout import MARK, cta, faq_block, cards, ticks, related, photo, trust_note, issues, example
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

COMMON_ISSUES = [
    ("“My computer won’t start”",
     "a failed drive, a corrupted boot record after an interrupted update, or a power supply on the way out. The beeping or the point it stops at usually tells you which.",
     "Get the data off first if the drive is still readable — that is the irreversible part. Then diagnose properly rather than reinstalling and hoping, and tell you honestly whether repair or replacement is the better spend."),
    ("“Outlook says the server is unavailable”",
     "a Microsoft 365 authentication problem, a corrupted local profile, or occasionally a genuine service issue. Rarely the thing people first assume.",
     "Check service health first — it takes a minute and saves an hour. Then rebuild the profile or re-establish authentication, and check the mailbox has not been compromised if the timing is suspicious."),
    ("“The whole office lost internet”",
     "a modem or router fault, a carrier outage, or a switch that has failed or looped. Which one it is determines whether it is a five-minute fix or a provider escalation.",
     "Isolate whether it is inside the building or outside it before anything else. If it is the carrier, we gather the evidence and escalate for you rather than leaving you on hold."),
    ("“Nobody can access the shared drive”",
     "a server that has not come back from a restart, a permissions change nobody logged, or a mapped drive pointing at something that has moved.",
     "Check the server and the share first, then permissions. If it was a change nobody documented, that is the actual problem worth fixing."),
    ("“It says my licence has expired”",
     "an auto-renewal that failed on an expired card, a subscription assigned to someone who has left, or a licence count that ran out as staff were added.",
     "Reconcile what is actually assigned against who is actually there. This audit routinely finds subscriptions for departed staff that more than cover the cost of doing it."),
    ("“The printer works for everyone except me”",
     "a driver mismatch, a queue stuck on the local machine, or that person connecting to the printer differently from everyone else.",
     "Standardise how the printer is connected across all machines rather than fixing the one. Otherwise it recurs on a different desk in a fortnight."),
]

EXAMPLE_1 = example(
    "A failed drive on the only machine that mattered",
    "A Gold Coast business called on a Tuesday morning: the machine running their job scheduling would not boot. It was the only computer with the current version of the file, and six staff could not be dispatched without it.",
    "A physically failing drive, still readable but throwing errors — every minute it stayed powered on risked losing more. The machine was six years old and there was no backup of the scheduling file, which lived on the desktop.",
    "Attended within the hour, imaged the drive immediately before attempting anything else, recovered the file, and had it running on a loan machine that morning. Replaced the machine, then set up backup so the file was no longer the single point of failure.",
    "Dispatch went out that day. The follow-up conversation was about the fact that a six-year-old desktop had been the whole business, which is the problem worth solving rather than the drive.")

EXAMPLE_2 = example(
    "The provider who could not be reached",
    "A professional firm rang us not because something was broken, but because their existing provider had stopped returning calls. Two open issues, no documentation, and nobody sure what was actually in place.",
    "No asset register, no record of licences or credentials, backups running to an unknown destination, and the domain registered to the outgoing provider rather than the business. That last one is the most common thing we find and the most awkward to fix late.",
    "Documented the whole environment from discovery, recovered the domain into the client’s own account, established where backups were going and tested a restore, then took over day-to-day support.",
    "The firm now owns its own documentation, domain and credentials. The two open issues turned out to be twenty minutes of work each — they had simply never been picked up.")


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

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The faults we get called about most</h2>
      <p>Described the way clients describe them, because that is usually all you have when you pick up the phone.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a call actually turns into</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
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

from layout import cta, faq_block, related, svc_body, issues, example, booking_cta

COMMON_ISSUES = [
    ("&ldquo;It&rsquo;s been like this for months&rdquo;",
     "a fault everyone has adapted around. Staff have invented workarounds, the workarounds became habit, and nobody reports it any more.",
     "Ask what people work around rather than what they report. Long-standing faults are usually cheap to fix and expensive to have tolerated, and they surface only if somebody asks the right question."),
    ("&ldquo;Three people looked at it and found nothing&rdquo;",
     "a fault that is not present when anyone attends, or one being investigated in the wrong place because the symptom appears somewhere other than the cause.",
     "Change the method rather than repeating it. If attending has failed three times, the fourth attendance will fail too &mdash; what is needed is evidence gathered while nobody is watching."),
    ("&ldquo;It happens to everyone but only sometimes&rdquo;",
     "something shared &mdash; the network, a server, a connection &mdash; failing intermittently rather than a problem with any individual machine.",
     "Establish what the affected people have in common. A fault crossing several machines has ruled out every one of those machines, which is genuinely useful information."),
    ("&ldquo;It started after&hellip; something, we think&rdquo;",
     "a change nobody recorded. An update, a new device, a provider swap, a staff departure &mdash; there is nearly always a starting point and it is nearly always undocumented.",
     "Pin the date down as precisely as possible and work back to what changed. Establishing when a fault began is frequently the fastest route to establishing what caused it."),
    ("&ldquo;We rebooted and it came good&rdquo;",
     "a temporary state cleared rather than a fault resolved. Restarting fixes the symptom and destroys the evidence.",
     "Where the business can tolerate it, capture the state before restarting. A restart is a perfectly reasonable response to a stopped business and it does end the investigation for that occurrence."),
    ("&ldquo;We just want it to stop&rdquo;",
     "entirely fair, and sometimes at odds with finding the cause. There is a real tension between the fastest fix and the permanent one.",
     "We will tell you which we are doing. Sometimes the right answer is to restore service now and investigate afterwards; what matters is that the choice is explicit rather than presented as a fix."),
]

EXAMPLE_1 = example(
    "The workaround nobody had mentioned in two years",
    "A business engaged us for general support and mentioned no significant problems. Sitting with staff during onboarding, three separate people were observed saving a file, closing the application, and reopening it before continuing.",
    "Asked about it, the answer was that the application lost work if left open too long, and it had been that way for as long as anyone could remember. Nobody had reported it because it had stopped feeling like a fault. The cause was a session timeout on the server, set during an installation years earlier and never revisited, which was disconnecting idle sessions after fifteen minutes.",
    "Changed the timeout to a sensible value for the way the application is actually used, and confirmed with staff over the following fortnight that the habit was no longer necessary.",
    "The workaround disappeared. Three people had been performing a small ritual dozens of times a day for two years, and it never reached us because it had long since stopped being described as a problem.")

EXAMPLE_2 = example(
    "Restoring service first, and saying so",
    "A business lost access to a shared system on a Friday afternoon during their busiest period. The immediate need was to keep trading; the cause was unknown.",
    "The fastest route to working was to restart the affected server, which would have cleared whatever state was causing the problem and destroyed any evidence of what it had been. That would have restored the business within minutes and made a recurrence very likely and equally undiagnosable.",
    "Explained the trade-off to the business directly, captured what could be captured in about ten minutes, then restarted and restored service. Investigated from the captured evidence over the following week and found a scheduled task that had failed in a way that consumed a shared resource.",
    "The business traded through the afternoon and the underlying cause was fixed the following week. The decision to spend ten minutes capturing evidence first was the business&rsquo;s to make, and it could only make it because somebody explained what the alternative cost.")

FAQS = [
    ("Who fixes business computers and servers on the Gold Coast?",
     "bcom ICT diagnoses and repairs business computers, workstations and servers across the Gold Coast, on site or remotely. Faults are diagnosed before quoting, loan equipment is available where a machine has to leave, and work is charged at $190 + GST per hour plus a $100 + GST call-out for on-site attendance. Call 07 3041 8993."),
    ("How do you decide whether to repair or replace?",
     "Age, what the repair costs against a replacement, and whether the machine will be adequate for another two years even once fixed. A five-year-old laptop needing a $400 screen is usually not worth it, and we'll say so rather than take the work."),
    ("Will we lose data?",
     "Not if we can avoid it. Data comes off before anything invasive happens, and if a drive has physically failed we'll tell you honestly what recovery involves and what it's likely to cost before you commit to it."),
    ("Do you provide a loan machine?",
     "Yes, where a device has to leave the site. Somebody sitting idle costs more than the repair does."),
    ("How long does a repair take?",
     "Most software and configuration faults are resolved in the same visit or session. Hardware repairs depend on parts — we'll tell you the expected turnaround before we take anything away."),
    ("Do you fix home computers?",
     "No. bcom ICT works with business machines — workstations, laptops used for work, and servers. General home computer repair isn't something we take on."),
]

PAGE = {
    "path": "/hardware-software-troubleshooting-gold-coast",
    "priority": "0.75",
    "service": "Business Computer & Server Troubleshooting Gold Coast",
    "title": "Business Computer & Server Troubleshooting Gold Coast | bcom ICT",
    "description": "Hardware and software troubleshooting for Gold Coast business computers, workstations and servers. Diagnosed before quoting, with loan equipment available. Call 07 3041 8993.",
    "hero_img": "hero-bg-hardware-software-troubleshooting.webp",
    "hero_alt": "A bcom ICT technician diagnosing a business computer fault on the Gold Coast",
    "h1": "Something's wrong and nobody can tell you why",
    "lede": "Diagnosis first, then a straight answer about what it costs to fix and whether fixing it is the right call.",
    "actions": [("Get it looked at", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Diagnosed before quoting", "Loan machines available", "Business hardware only", "Since 2011"],
    "crumbs": [("Services", "/services"), ("Troubleshooting", "/hardware-software-troubleshooting-gold-coast")],
    "faqs": FAQS,
    "booking": True,
    "reviewed": "August 2026",
    "body": svc_body(
        answer="bcom ICT diagnoses and repairs hardware and software faults on business computers, "
               "workstations and servers across the Gold Coast. Faults are diagnosed before a repair is "
               "quoted, and loan equipment is available where a machine has to leave the site. Call "
               "07 3041 8993.",
        blocks=[
            {"eyebrow": "Symptoms", "h2": "What people describe when they call", "cols": 3, "cards": [
                ("\"It won't start\"", None, "Blank screens, boot loops, beeping, or a machine that powers on and does nothing. Could be a drive, memory, power supply or a failed update — the diagnosis matters."),
                ("\"It's got really slow\"", None, "Usually a failing drive, insufficient memory for what's now being run, or accumulated software nobody uninstalled. Sometimes worth fixing, sometimes worth replacing."),
                ("\"It keeps crashing\"", None, "Blue screens and random restarts are typically hardware — memory or storage — or a driver conflict after an update. Intermittent faults need proper testing, not guesswork."),
                ("\"It stopped working after an update\"", None, "Common and usually fixable. Failed updates, driver conflicts and applications that no longer launch."),
                ("The server is misbehaving", None, "Storage filling up, backup jobs failing, services stopping overnight, performance degrading. Servers rarely fail suddenly — they warn first, if someone is watching."),
                ("Nobody knows what changed", None, "The hardest category and the most common. We work backwards from what still functions rather than guessing."),
            ]},
            {"h2": "How we approach it",
             "ticks": [
                "<strong>Diagnose before quoting.</strong> A repair price given before anyone has looked is a guess, and usually a low one that grows.",
                "<strong>Get the data off first.</strong> Before anything invasive happens to a drive.",
                "<strong>Test intermittent faults properly.</strong> The ones that only happen sometimes need memory and drive testing, not a reinstall and hope.",
                "<strong>Say when replacement is cheaper.</strong> We'd rather lose the repair than have you spend $400 on a machine with a year left.",
                "<strong>Leave a loan device.</strong> If yours has to go away, somebody still needs to work.",
             ]},
            {"h2": "Recurring faults are a different problem",
             "html": '<p style="max-width:68ch">If the same machine keeps failing, or the same fault keeps returning across different machines, the useful question stops being "how do we fix it" and becomes "why does this keep happening". That is usually an ageing fleet, an under-specified machine doing work it was never bought for, or something environmental like power or heat.</p>'
                     '<p style="max-width:68ch;margin-top:16px">Chasing that down is included for <a href="/managed-it-services-for-small-businesses-gold-coast">managed IT</a> clients, because a provider who only earns from repeat visits has no reason to look. For everyone else we will still tell you what the underlying cause is, rather than billing the symptom repeatedly.</p>'},
        ]) + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The situations we are actually called into</h2>
      <p>Six of them. The hardest are not technically difficult &mdash; they are the ones nobody reports.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a real diagnosis looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
''' + f'''
{booking_cta()}
''' + faq_block(FAQS) + related([
            ("Business Computer Repair", "/on-site-computer-repair-gold-coast"),
            ("Windows & macOS Repair", "/os-troubleshooting-repair-gold-coast"),
            ("Performance Optimisation", "/performance-optimisation-gold-coast"),
            ("Hardware Procurement & Setup", "/hardware-procurement-setup-gold-coast"),
            ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
            ("Business IT Support", "/it-support-and-services-gold-coast"),
        ]) + cta("Get a straight diagnosis",
                 "We'll tell you what's wrong, what it costs, and whether it's worth fixing — before you commit to anything."),
}

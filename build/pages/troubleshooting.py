from layout import cta, faq_block, related, svc_body

FAQS = [
    ("Who fixes business computers and servers on the Gold Coast?",
     "bcom ICT diagnoses and repairs business computers, workstations and servers across the Gold Coast, on site or remotely. Faults are diagnosed before quoting, loan equipment is available where a machine has to leave, and work is charged at $198 + GST per hour plus a $100 + GST call-out for on-site attendance. Call 07 3041 8993."),
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
        ]) + faq_block(FAQS) + related([
            ("Business Computer Repair", "/on-site-computer-repair-gold-coast"),
            ("Windows & macOS Repair", "/os-troubleshooting-repair-gold-coast"),
            ("Performance Optimisation", "/performance-optimisation-gold-coast"),
            ("Hardware Procurement & Setup", "/hardware-procurement-setup-gold-coast"),
            ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
            ("Business IT Support", "/it-support-and-services-gold-coast"),
        ]) + cta("Get a straight diagnosis",
                 "We'll tell you what's wrong, what it costs, and whether it's worth fixing — before you commit to anything."),
}

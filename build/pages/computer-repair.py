from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Do you repair computers on site on the Gold Coast?',
        'Yes. bcom ICT attends Gold Coast business premises and repairs laptops, desktops and workstations in place where possible. Where a machine has to leave, a loan device is supplied so nobody '
        'sits idle. On-site attendance is a $100 + GST call-out plus $198 + GST per hour. Call 07 3041 8993.'),
    (   'Will we lose our data?',
        "Not if we can avoid it. Data is recovered before any invasive work begins, provided the drive is still readable. Where a drive has physically failed we'll tell you honestly what specialist "
        'recovery involves and roughly what it costs before you commit to it.'),
    (   'How do you decide whether to repair or replace?',
        "Age of the machine, repair cost against replacement cost, and whether it will still be adequate in two years once fixed. We'd rather lose a repair than have you spend $400 on a machine with "
        'a year left in it.'),
    ('Do you provide a loan machine?', 'Yes, where a device has to leave the site. The cost of somebody being unable to work almost always exceeds the repair.'),
    ('Do you repair home computers?', "No. bcom ICT repairs business machines — workstations, laptops used for work, and servers. General home computer repair isn't something we take on any more."),
    (   'How long does a repair take?',
        "Most software and configuration faults are resolved in the same visit. Hardware repairs depend on parts availability — we'll give you an expected turnaround before taking anything away.")]

PAGE = {
    "path": '/on-site-computer-repair-gold-coast',
    "priority": '0.8',
    "service": 'Business Computer Repair Gold Coast',
    "title": 'Business Computer Repair Gold Coast — On-Site | bcom ICT',
    "description": 'On-site repair of business laptops, desktops and workstations across the Gold Coast. Diagnosed in place, with a loan machine if the repair takes longer. Call 07 3041 8993.',
    "hero_img": 'hero-bg-computer-repair.webp',
    "hero_alt": 'A bcom ICT technician repairing a business laptop on site at a Gold Coast office',
    "h1": 'We come to the office and fix it there',
    "lede": 'Business laptops, desktops and workstations repaired in place — with a loan machine if yours has to leave, because somebody still needs to work.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Repaired on site', 'Loan machines available', 'Data off first', 'Business hardware only'],
    "crumbs": [('Services', '/services'), ('Business Computer Repair', '/on-site-computer-repair-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT repairs business laptops, desktops and workstations on site across the Gold Coast, diagnosing and repairing in place where possible and supplying a loan machine where a device has to leave. Data is recovered before any invasive work begins. bcom ICT repairs business hardware only. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       "Won't power on",
                                         None,
                                         'Power supply faults, failed motherboards, battery and charging '
                                         'problems. Diagnosed properly rather than replaced on a guess.'),
                                 (       'Failed drives',
                                         None,
                                         'The most common serious fault. Data comes off first where the '
                                         'drive is readable, then the replacement goes in and the machine '
                                         'is rebuilt.'),
                                 (       'Screens and physical damage',
                                         None,
                                         'Cracked screens, hinge failures, damaged ports and keyboards. '
                                         'Usually worth repairing on a machine under three years old.'),
                                 (       'Overheating and shutdowns',
                                         None,
                                         'Machines that run hot, throttle or shut down under load. '
                                         'Frequently dust and thermal paste rather than anything '
                                         'expensive.'),
                                 (       'Memory and storage upgrades',
                                         None,
                                         'Where a machine is otherwise sound, an SSD or a memory upgrade '
                                         'often buys two more useful years for a fraction of replacement '
                                         'cost.'),
                                 (       'Servers and workstations',
                                         None,
                                         'Physical faults on servers, RAID and storage failures, and the '
                                         'workstations doing heavier work than a standard office '
                                         'machine.')],
                'cols': 3,
                'eyebrow': 'What we repair',
                'h2': 'Business machines, on site'},
        {       'h2': 'How we handle it',
                'ticks': [       '<strong>Diagnose before quoting.</strong> A repair price given before '
                                 'anyone has opened the machine is a guess, and usually one that grows.',
                                 '<strong>Data off first.</strong> Before anything invasive happens to a '
                                 'drive that is still readable.',
                                 '<strong>Repair on site where we can.</strong> Faster for you, and '
                                 'nothing leaves the building.',
                                 '<strong>Loan machine if it has to go.</strong> A person sitting idle '
                                 'costs more than the repair.',
                                 '<strong>Honest replace-or-repair advice.</strong> A five-year-old laptop '
                                 "needing a $400 screen usually isn't worth it, and we'll say so."]},
        {       'h2': "When repair isn't the answer",
                'html': '<p style="max-width:68ch">Sometimes the right advice is to stop spending on a '
                        'machine. Age, what the repair costs against replacement, and whether the machine '
                        'will still be adequate in two years all matter — and the honest answer is often '
                        'that a business is better served replacing one machine than repairing '
                        'three.</p><p style="max-width:68ch;margin-top:16px">Where replacement is the '
                        'call, we source at trade pricing and set the machine up ready to use — see <a '
                        'href="/hardware-procurement-setup-gold-coast">hardware procurement and setup</a>. '
                        'If your whole fleet is at that point, <a '
                        'href="/performance-optimisation-gold-coast">a fleet assessment</a> is usually the '
                        'cheaper conversation.</p><p style="max-width:68ch;margin-top:16px"><strong>We '
                        "repair business machines only.</strong> General home computer repair isn't "
                        'something we take on.</p>'}])
            + faq_block(FAQS)
            + related([       ('Troubleshooting', '/hardware-software-troubleshooting-gold-coast'),
        ('Windows & macOS Repair', '/os-troubleshooting-repair-gold-coast'),
        ('Performance Optimisation', '/performance-optimisation-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('Virus & Malware Removal', '/virus-and-malware-removal-services-gold-coast'),
        ('On-site IT Support', '/on-site-technical-support-gold-coast')])
            + cta("Machine down and someone can't work?", "Call and we'll tell you whether it's worth repairing before we come out — and bring a loan device if it isn't."),
}

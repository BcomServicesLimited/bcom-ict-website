from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;It won&rsquo;t turn on at all&rdquo;",
     "the power supply, the board, or something as ordinary as a wall switch. No lights and no fans is a different fault from lights but no picture, and the two get reported identically.",
     "Establish whether the machine is receiving power and getting through its startup checks before anything is opened. Half of these are resolved without a part; the other half are diagnosed correctly rather than replaced hopefully."),
    ("&ldquo;It powers up but the screen stays black&rdquo;",
     "memory, graphics, or the display itself. The machine is often running perfectly and simply cannot show you.",
     "Test with an external screen first, then reseat and test memory. Laptop screens and cables fail regularly, and replacing a machine because its display died is an expensive way to solve a cheap problem."),
    ("&ldquo;It&rsquo;s making a clicking or grinding noise&rdquo;",
     "a mechanical hard drive failing. This is the one fault where what you do in the first ten minutes decides whether the data comes back.",
     "Stop using it and call us before trying anything else. Every restart of a failing drive costs recoverable data, and a machine that clicks has already started telling you it is on borrowed time."),
    ("&ldquo;It shuts itself down after twenty minutes&rdquo;",
     "heat. Dust in the cooling path, a failed fan, or a machine sitting somewhere with no airflow &mdash; and it always gets worse in summer.",
     "Clean it out, verify the fans, and check where it lives. Machines under desks against a wall and machines in workshops are the two we see most, and both are usually fixable rather than terminal."),
    ("&ldquo;Someone spilled a drink on it&rdquo;",
     "liquid, which does its damage over days through corrosion rather than instantly. A laptop that still works after a spill is not a laptop that survived one.",
     "Power it off, do not attempt to dry it with heat, and get it looked at quickly. Acting the same day changes the outcome; waiting until it starts misbehaving usually does not."),
    ("&ldquo;The laptop only runs when it&rsquo;s plugged in&rdquo;",
     "a battery at the end of its life or a charging circuit fault. Batteries are consumable and three to four years is a normal working life.",
     "Check the battery&rsquo;s actual health rather than its age. A replacement battery in a machine that is otherwise fine is one of the better value repairs available."),
]

EXAMPLE_1 = example(
    "Every restart cost them another piece of the file",
    "A business called about a machine that had started clicking and would no longer open a critical spreadsheet. Before calling, staff had restarted it eleven times over two days hoping it would come good, and had run a disk repair utility twice.",
    "The drive was mechanically failing. The repair utility had been writing to a disk with failing heads, which had damaged data that was still readable when the clicking started. The spreadsheet was recoverable in part; a folder of scanned records was not.",
    "Stopped all access, imaged what could still be read to a healthy drive before attempting anything else, then recovered from the image rather than the failing hardware. Replaced the drive and restored the machine.",
    "Most of the data came back. The part that did not was lost during those two days of trying, not during the failure itself &mdash; which is why a clicking drive is the one fault where the right first move is to stop.")

EXAMPLE_2 = example(
    "Six machines that only failed in January",
    "A business operating from a workshop and adjoining office reported computers shutting down without warning. It had happened the previous summer, stopped over winter, and returned. A previous provider had replaced two machines.",
    "The workshop machines were dense with dust drawn in from the workspace, and their cooling was effectively blocked. In cooler months the reduced airflow was still sufficient; above about thirty degrees ambient it was not, and the machines were protecting themselves by shutting down. The two replaced machines had begun doing exactly the same thing.",
    "Cleaned and serviced every machine, fitted filtered enclosures for the two in the worst position, and moved one off the floor where it had been drawing dust directly.",
    "No shutdowns the following summer. Two machines had already been replaced for a fault that a service and a change of position resolved on the remaining four.")

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
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The hardware faults we are actually called to</h2>
      <p>Six faults account for most business machine failures, and only two of them usually need a new machine.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What a repair actually looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Troubleshooting', '/hardware-software-troubleshooting-gold-coast'),
        ('Windows & macOS Repair', '/os-troubleshooting-repair-gold-coast'),
        ('Performance Optimisation', '/performance-optimisation-gold-coast'),
        ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast'),
        ('Virus & Malware Removal', '/virus-and-malware-removal-services-gold-coast'),
        ('On-site IT Support', '/on-site-technical-support-gold-coast')])
            + cta("Machine down and someone can't work?", "Call and we'll tell you whether it's worth repairing before we come out — and bring a loan device if it isn't."),
}

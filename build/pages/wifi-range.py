from layout import cta, faq_block, related, svc_body, issues, example

COMMON_ISSUES = [
    ("&ldquo;We put in an extender and it&rsquo;s barely better&rdquo;",
     "how a repeater works. It receives and retransmits on the same radio, so throughput through it is roughly halved before anything else is considered.",
     "Use a properly cabled access point where the building allows it. An extender is a last resort for places cable genuinely cannot reach, not a first answer to a coverage gap."),
    ("&ldquo;There are two networks now and devices pick the wrong one&rdquo;",
     "an extender broadcasting its own separate network name. Devices connect to whichever they saw first and stay there.",
     "Present one network across the whole building so devices roam without choosing. Two network names is an admission that the coverage was extended rather than designed."),
    ("&ldquo;The extender is in the dead spot&rdquo;",
     "the most natural place to put it and the wrong one. An extender placed where signal is poor has poor signal to relay.",
     "Position it where it still has a strong path back to the source, part way rather than at the far end. This single misunderstanding accounts for most disappointing extender installations."),
    ("&ldquo;It worked and then it didn&rsquo;t&rdquo;",
     "an extender that has lost its connection to the main network and not recovered, or one quietly rebooting under load.",
     "Check whether the device is genuinely stable rather than only occasionally working. Consumer extenders are frequently the least reliable device on a business network."),
    ("&ldquo;We need coverage in the shed or the yard&rdquo;",
     "a genuine outdoor requirement, which is a different problem from a weak corner of an office.",
     "Use outdoor-rated equipment on a cabled or a properly engineered wireless link. Attempting to reach a separate building with an indoor extender is where this most often goes wrong, and the failure is usually put down to distance when the real problem was the equipment."),
    ("&ldquo;We can&rsquo;t run a cable there&rdquo;",
     "sometimes true and frequently assumed. Existing conduit, cable tray and ceiling routes are more often available than people expect.",
     "Let us look before accepting that. Existing conduit, cable tray, ceiling voids and the routes already used by power or phone cabling are worth checking properly before an extender is accepted as the only option. A short cable run turns an unreliable extender into a proper access point, and the difference in result is considerable &mdash; not a marginal improvement but the difference between a connection people work around and one they stop noticing."),
]

EXAMPLE_1 = example(
    "The extender that was in exactly the wrong place",
    "A business had bought a well-reviewed extender to fix a weak area at the rear of its premises. Installed at the affected desk, it made almost no difference, and a second unit made things worse.",
    "Both units had been placed where the coverage problem was, which meant both had a weak connection back to the main access point. An extender can only relay what it receives, and neither was receiving much. The second unit was also relaying from the first, halving throughput twice over.",
    "Removed both, found an existing ceiling route the business had assumed was unusable, and cabled a proper access point to the rear of the premises.",
    "Full speed at the back of the building. The cable run took under two hours and the two extenders were returned. Where a cable can be run, it is not a close comparison.")

EXAMPLE_2 = example(
    "Reaching a separate shed across a yard",
    "A business needed working connectivity in a storage building about forty metres from the main premises, across an open yard. Two consumer extenders had been tried and neither reached usefully.",
    "The requirement was a link between two buildings, not an extension of coverage within one. Indoor equipment is not built for that distance or that exposure, and both units had also been mounted inside where the walls attenuated the signal before it reached the yard at all.",
    "Installed a purpose-built outdoor wireless link between the two buildings with clear line of sight, then a proper access point inside the shed fed from it.",
    "Full connectivity in the storage building, including for the scanning devices used there. The requirement had been reasonable throughout and had simply been attempted with equipment designed for a different job.")

EXAMPLE_3 = example(
    "One network name across a building that had four",
    "A business occupying two floors had extended its wireless over several years by adding equipment wherever coverage was poor. Staff had learned to switch networks manually as they moved, and treated it as normal.",
    "Four separate wireless networks were being broadcast, each with its own name and its own password, none of them aware of the others. Devices connected to whichever they had last used and held onto it well past the point of usefulness, because no device will voluntarily leave a network it can still technically reach. A laptop carried from the upstairs meeting room to a downstairs desk stayed connected to the upstairs equipment until it lost the connection entirely, at which point it would reconnect &mdash; usually mid-call. Staff had adapted by disabling and re-enabling their wireless when they moved, which had become an unremarked habit across the whole business.",
    "Replaced the accumulated equipment with cabled access points presenting a single network across both floors, with transmit power tuned so handover happens where it should rather than at the point of failure. Reused two of the existing units where they were positioned usefully.",
    "One network name, one password, and devices that move between floors without anyone thinking about it. The habit of toggling the wireless took a few weeks to disappear, which is the clearest measure of how long people had been working around it.")
FAQS = [   (   "What's the best way to extend WiFi range?",
        "A wired access point, wherever a cable run is physically possible — it delivers full speed with no compromise. Where cabling isn't practical, a mesh system positioned by measurement is the "
        'next best. Range extenders are cheapest but typically halve throughput and create roaming problems.'),
    (   "Why doesn't our range extender work well?",
        "Usually placement. Extenders are commonly installed at the dead spot itself, where they can barely hear the signal they're meant to relay. They need to sit partway between the router and "
        'the dead area. Even correctly placed, they halve throughput by design.'),
    (   'Should we use mesh instead?',
        "For most homes and small premises where cabling isn't practical, yes. Mesh keeps one network name so devices roam properly, rather than clinging to a weak connection. See our mesh WiFi "
        'setup page.'),
    (   'Can you extend WiFi to a shed or outbuilding?',
        "Often, though it depends on distance, construction and whether power and a cable path exist. Steel sheds are particularly difficult. We'll measure and tell you honestly what's achievable "
        'before quoting.')]

PAGE = {
    "path": '/wifi-range-extension-gold-coast',
    "priority": '0.65',
    "title": "WiFi Range Extension Gold Coast | bcom ICT",
    "description": 'Extending WiFi coverage for Gold Coast businesses and home offices — measured rather than guessed, with wired access points where a cable run is possible.',
    "hero_img": 'hero-bg-wifi-range-extension.webp',
    "hero_alt": 'WiFi coverage being extended by bcom ICT at a Gold Coast premises',
    "h1": "Getting signal where there isn't any",
    "lede": 'Extenders are the usual answer and often the wrong one. What actually works depends on whether a cable can reach.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Measured, not guessed', 'Wired where possible', 'Business & home office', 'Same-day where available'],
    "crumbs": [('Services', '/services'), ('Business WiFi', '/business-wifi-gold-coast'), ('WiFi Range Extension', '/wifi-range-extension-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT extends WiFi coverage for Gold Coast businesses and home offices, measuring signal across the space before recommending an approach. Where a cable run is possible a wired access point is used, since it outperforms wireless extenders and mesh; where it is not, a mesh system is positioned by measurement. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Wired access point',
                                         None,
                                         'A cable run to a second access point. Full speed, no compromise, '
                                         'and by a clear margin the best result. If a cable can physically '
                                         'get there, this is the answer.'),
                                 (       'Mesh system',
                                         None,
                                         'Several nodes working together under one network name. Good when '
                                         "cabling isn't practical, and devices roam properly between nodes "
                                         'rather than clinging to a distant one.'),
                                 (       'Range extender',
                                         None,
                                         'The cheapest and the weakest. Typically halves throughput and '
                                         'creates a second network name devices hold onto long after they '
                                         'should switch. Occasionally the right answer, usually not.')],
                'cols': 3,
                'eyebrow': 'Three approaches',
                'h2': 'Which one suits, in order of preference'},
        {       'h2': 'Why measuring matters',
                'html': '<p style="max-width:68ch">Almost every failed extension we are called to fix was '
                        'positioned by guesswork — the device placed where the dead spot is, rather than '
                        'partway between the router and the dead spot where it can still hear the signal '
                        'it is meant to be relaying.</p><p '
                        'style="max-width:68ch;margin-top:16px">Measuring takes very little time and '
                        'determines whether the equipment will work at all. For larger premises — '
                        'warehouses, multi-storey buildings, accommodation — it is not optional; see <a '
                        'href="/business-wifi-gold-coast">business WiFi installation</a>.</p>'}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>The coverage problems we are actually called to</h2>
      <p>Six situations. The first one explains why most extenders disappoint the people who buy them.</p>
    </div>
    {issues(COMMON_ISSUES)}
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What extending coverage properly looks like</h2>
      <p>Representative engagements, drawn from real work with identifying detail removed &mdash; we don&rsquo;t name clients without written permission.</p>
    </div>
    {EXAMPLE_1}
    {EXAMPLE_2}
    {EXAMPLE_3}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Business WiFi Installation', '/business-wifi-gold-coast'),
        ('Mesh WiFi Setup', '/mesh-network-setup-gold-coast'),
        ('Network Troubleshooting', '/network-troubleshooting-diagnostics-gold-coast'),
        ('Business NBN & Internet', '/nbn-internet-support-gold-coast'),
        ('Computer Networking Service', '/computer-networking-service-gold-coast'),
        ('Remote IT Support', '/remote-it-support-gold-coast')])
            + cta('Dead spot somewhere it matters?', "We'll measure it and tell you what will actually work — which is frequently cheaper than what's been suggested."),
}

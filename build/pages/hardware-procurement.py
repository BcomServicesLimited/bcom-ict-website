from layout import cta, faq_block, related, svc_body

FAQS = [   (   'Can you supply business computers on the Gold Coast?',
        'Yes. bcom ICT sources laptops, desktops, servers, switches, monitors and peripherals at trade pricing, then images and configures them before delivery so staff can work immediately. '
        'Replaced machines are securely wiped. Call 07 3041 8993.'),
    (   'Do you mark up hardware?',
        "We source at trade pricing and are transparent about what we charge over it. If you'd prefer to buy the hardware yourself and have us configure and deploy it, that's fine — and we'll still "
        'advise on what to buy.'),
    (   'Should we buy business-grade or is retail fine?',
        'Business ranges carry longer warranties, on-site service options and standardised parts, which matters when a failure would otherwise leave someone without a machine for a fortnight. For a '
        'business, the retail saving usually evaporates on the first failure.'),
    (   'What happens to our old machines?',
        "Data is migrated first, then the drive is securely wiped before the machine is disposed of or redeployed. A traded-in machine with recoverable client data on it is a genuine risk, and it's "
        'an easy one to avoid.'),
    (   'Do we still need a server?',
        "Often not. Many small businesses that assume they need to replace a server would be better moving to cloud file storage and retiring it. We'll tell you which applies rather than quoting a "
        'replacement by default.'),
    (   'How long does it take to get machines set up?',
        'Usually a few days from delivery to deployment for a small batch, most of which is us configuring rather than you waiting. Machines arrive at your office ready to use.')]

PAGE = {
    "path": '/hardware-procurement-setup-gold-coast',
    "priority": '0.75',
    "service": 'Hardware Procurement & Setup Gold Coast',
    "title": 'Business Hardware Procurement & Setup Gold Coast | bcom ICT',
    "description": 'Business hardware supply and setup on the Gold Coast — laptops, desktops, servers, switches and monitors at trade pricing, imaged, configured and deployed ready to use.',
    "hero_img": 'hardware-procurement-setup-gold-coast-hero.webp',
    "hero_alt": 'New business computers being configured by bcom ICT before deployment to a Gold Coast client',
    "h1": 'Delivered configured, not delivered in a box',
    "lede": "Sourced at trade pricing, imaged, joined to your systems and set up with the person's own files and email — so day one is working, not waiting.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Trade pricing', 'Configured before delivery', 'Business-grade warranty', 'Old machines wiped'],
    "crumbs": [('Services', '/services'), ('Hardware Procurement & Setup', '/hardware-procurement-setup-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT sources and configures business hardware for Gold Coast businesses — laptops, desktops, servers, switches and monitors — at trade pricing, then images, configures and deploys them ready for staff to use. Replaced machines are securely wiped and disposed of. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Specified for the work',
                                         None,
                                         'Not the cheapest model, and not the most expensive. What matters '
                                         'is what the person actually does — an accounts machine, a CAD '
                                         'workstation and a reception PC are three different purchases and '
                                         'one of them is not a $700 laptop.'),
                                 (       'Business-grade, not retail',
                                         None,
                                         'Business ranges carry longer warranties, on-site service options '
                                         'and standardised parts. The retail equivalent looks cheaper '
                                         'until a failure means a fortnight without a machine.'),
                                 (       'Configured before it arrives',
                                         None,
                                         'Imaged, joined to your systems, security settings applied, '
                                         "applications installed, printers and drives mapped. The user's "
                                         'files and email are already there when they sit down.'),
                                 (       'The old machine handled properly',
                                         None,
                                         'Data migrated, then the drive securely wiped before disposal or '
                                         'redeployment. A traded-in machine with recoverable client data '
                                         'on it is a breach waiting to be discovered.')],
                'cols': 2,
                'eyebrow': 'The difference',
                'h2': 'Buying the machine is the easy part',
                'icon': False,
                'sub': 'Anyone can order a laptop. What costs a business time is everything between '
                       'delivery and someone actually working on it.'},
        {       'h2': 'What we supply',
                'ticks': [       'Laptops, desktops and workstations, specified for the actual role',
                                 'Servers and storage, including whether you need one at all — often the '
                                 'honest answer is no',
                                 'Network switches and access points matched to your existing '
                                 'infrastructure',
                                 'Monitors, docks and peripherals, including the ergonomic side people '
                                 'forget until someone complains',
                                 'Microsoft 365 and software licensing, sized to what you use rather than '
                                 "what's bundled",
                                 'Warranty registration and asset tagging, added to the register you '
                                 'keep']},
        {       'h2': 'On pricing',
                'html': '<p style="max-width:68ch">We source at trade pricing and are open about what we '
                        'charge over it. If you would rather buy the hardware yourself and have us '
                        'configure and deploy it, that is a perfectly reasonable arrangement and some '
                        'clients do exactly that — we will still tell you what to buy.</p><p '
                        'style="max-width:68ch;margin-top:16px">Where several machines are due at once, a '
                        '<a href="/performance-optimisation-gold-coast">fleet assessment</a> is usually '
                        'the better starting point. It turns replacement into a planned schedule rather '
                        'than a series of emergencies, which costs the same money and removes the '
                        'surprise.</p>'}])
            + faq_block(FAQS)
            + related([       ('Performance Optimisation', '/performance-optimisation-gold-coast'),
        ('Business Computer Repair', '/on-site-computer-repair-gold-coast'),
        ('Technology Procurement Advice', '/technology-procurement-advice-gold-coast'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast'),
        ('IT Consulting & Strategy', '/it-consulting-strategy-gold-coast'),
        ('Office IT Relocation', '/office-it-relocation-gold-coast')])
            + cta('Machines due for replacement?', "We'll tell you what to buy for the work each person actually does — and deliver them configured rather than boxed."),
}

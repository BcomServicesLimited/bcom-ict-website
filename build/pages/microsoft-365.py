from layout import cta, faq_block, related, svc_body, price_table

FAQS = [   (   'Who sets up Microsoft 365 for businesses on the Gold Coast?',
        'bcom ICT migrates, configures and supports Microsoft 365 for Gold Coast businesses and for businesses across Australia, covering email migration, Teams, SharePoint and OneDrive, with '
        'security baselines and multi-factor authentication enabled from day one. bcom ICT is a Microsoft Partner and provisions tenancies in Australian regions. Call 07 3041 8993.'),
    (   'Will we lose email during the migration?',
        'No. Mail continues flowing throughout and nothing is switched off until we have verified everything came across. The old system stays available for a period afterwards as a safety net.'),
    (   'Where is our data stored?',
        'Tenancies we provision are created in Australian regions, so mail and files sit in Australian data centres. Our data handling page sets out where everything lives, including backups and the '
        'vendor platforms that process telemetry outside Australia.'),
    (   "Do we need separate backup if we're on Microsoft 365?",
        'Yes. This is the most common misunderstanding we encounter. Microsoft protects the platform from failing, not your data from being deleted, encrypted or lost. Separate backup of Microsoft '
        '365 is a real requirement rather than an upsell.'),
    (   'Can you fix a tenancy someone else set up?',
        "Frequently what we're asked to do. A tenancy review covers MFA coverage, legacy authentication, sharing settings, admin accounts and licensing you may be paying for and not using — that "
        'last one often pays for the work.'),
    (   'Should we use Microsoft 365 or Google Workspace?',
        'Whichever fits how you already work. Microsoft 365 suits businesses heavy on Office documents, needing Teams calling, or with compliance requirements. Google Workspace suits businesses '
        'living in browsers and collaborating in real time. Migrating between them for its own sake is rarely worth the disruption.')]

PRICING = [
    ('Migration, per user', '$150', '+ GST, indicative',
     [
      'Mailbox moved with mail, calendar and contacts intact',
      'Licence assigned and multi-factor authentication enforced',
      'Desktop, laptop and mobile set up and tested',
      'The old mail system decommissioned once you are satisfied',
     ]),
]

PAGE = {
    "path": '/microsoft-365-setup-gold-coast',
    "priority": '0.8',
    "service": 'Microsoft 365 Setup & Support Gold Coast',
    "title": 'Microsoft 365 Setup & Support Gold Coast | bcom ICT',
    "description": 'Microsoft 365 migration, setup and support for Gold Coast businesses. Email migration, Teams, SharePoint and OneDrive configured with security baselines and MFA from day one. Microsoft Partner.',
    "hero_img": 'microsoft-365-setup-gold-coast-hero.webp',
    "hero_alt": 'Microsoft 365 being configured for a Gold Coast business by bcom ICT',
    "h1": 'Microsoft 365, set up the way a business should have it',
    "lede": 'Email migrated without downtime, Teams and SharePoint structured so people can find things, and security switched on from day one rather than after an incident.',
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ['Microsoft Partner', 'Australian data residency', 'MFA from day one', 'Weekend cutovers'],
    "crumbs": [('Services', '/services'), ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast'), ('Microsoft 365 Setup', '/microsoft-365-setup-gold-coast')],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(answer='bcom ICT migrates, configures and supports Microsoft 365 for businesses across the Gold Coast and Australia-wide — email migration, Teams, SharePoint and OneDrive — with security baselines and multi-factor authentication enabled during setup rather than afterwards. Tenancies are provisioned in Australian regions. bcom ICT is a Microsoft Partner. Call 07 3041 8993.',
                     blocks=[       {       'cards': [       (       'Migrating in',
                                         None,
                                         'From an old mail server, a hosting provider, or Google '
                                         'Workspace. Mail, calendars and contacts come across and the '
                                         'cutover is staged so nobody is locked out on a Monday morning.'),
                                 (       'Setting it up properly',
                                         None,
                                         'Shared mailboxes that behave, distribution groups, calendar '
                                         'permissions, and a SharePoint structure that reflects how your '
                                         'business actually works rather than how the wizard suggested.'),
                                 (       'Securing it',
                                         None,
                                         'MFA enforced, legacy authentication closed, sharing settings '
                                         'tightened, and the admin accounts nobody had reviewed cleaned '
                                         'up. This is the part most tenancies are missing.'),
                                 (       'Keeping it tidy',
                                         None,
                                         'Licences, accounts and permissions maintained as people join and '
                                         'leave. Cloud tenancies get messy fast when nobody owns them.')],
                'cols': 2,
                'eyebrow': 'What we do',
                'h2': 'The four jobs businesses ask for'},
        {       'h2': 'Two things new tenancies get wrong',
                'html': '<p style="max-width:68ch"><strong>Security is not on by default.</strong> A new '
                        'Microsoft 365 tenancy ships with multi-factor authentication not fully enforced, '
                        'legacy authentication paths open and sharing settings wide. That gap is precisely '
                        'where account takeovers come from, and closing it is part of setup rather than an '
                        'upsell.</p><p style="max-width:68ch;margin-top:16px"><strong>Microsoft is not '
                        'backing you up.</strong> Microsoft guarantees the platform stays available. It '
                        'does not protect you from a deleted mailbox, ransomware encrypting files that '
                        'sync to OneDrive, or a departing staff member emptying a SharePoint library. '
                        'Retention windows are short and unforgiving. Separate <a '
                        'href="/data-backup-recovery-gold-coast">Microsoft 365 backup</a> is a genuine '
                        'requirement.</p>'},
        {       'cols': 4,
                'eyebrow': 'Migrating',
                'h2': 'How a move actually runs',
                'steps': [       (       'Map it',
                                         'Every mailbox, shared drive, licence and application, plus who '
                                         'uses what. Migrations fail on the folder nobody mentioned.'),
                                 (       'Plan the cutover',
                                         'What moves first and how people keep working during it. Usually '
                                         'staged over a weekend.'),
                                 (       'Migrate and verify',
                                         'Data comes across and is checked before the old system is '
                                         'switched off, not after.'),
                                 (       'Secure and hand over',
                                         'MFA on, baselines applied, permissions tidied, documentation of '
                                         'what lives where given to you.')]}])
            + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>How much does a Microsoft 365 migration cost?</h2>
      <p>Indicative per user. Scoped properly first, then quoted as a fixed price.</p>
    </div>
    {price_table(PRICING, note='Migrations vary more than anything else we quote, so treat $150 per user as a starting point rather than a price. What moves it: how much mail history is coming across, whether shared mailboxes and public folders are involved, whether files are moving to SharePoint or OneDrive at the same time, and how cooperative the system being left behind turns out to be. We scope first and then quote a fixed price, because a migration billed by the hour is a quote that only ever moves in one direction.')}
  </div>
</section>
'''
            + faq_block(FAQS)
            + related([       ('Cloud & Microsoft 365', '/cloud-computing-service-gold-coast'),
        ('Microsoft Copilot', '/microsoft-copilot-gold-coast'),
        ('Data Backup & Disaster Recovery', '/data-backup-recovery-gold-coast'),
        ('Cybersecurity Services', '/cybersecurity-services-gold-coast'),
        ('Data handling & sovereignty', '/data-handling-and-sovereignty'),
        ('Managed IT Services', '/managed-it-services-for-small-businesses-gold-coast')])
            + cta("Moving to Microsoft 365, or fixing what you've got?", "Either way we'll map what you're running now and tell you what the move actually involves."),
}

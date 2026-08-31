from layout import MARK, cta, faq_block, ticks, related

SECTIONS = [
    ("What we collect", [
        "<strong>Contact and business details</strong> — name, business name, email, phone and address, provided when you enquire, engage us or are set up as a contact for a client we support.",
        "<strong>Support records</strong> — what you asked, what we did, and any logs or screenshots attached to a job. Attachments can incidentally contain business information, so tickets are treated as confidential.",
        "<strong>Technical information about systems we manage</strong> — device details, patch status, security alerts and configuration. This is data about your environment, not the contents of your files.",
        "<strong>Credentials</strong> for systems we administer on your behalf, held in a dedicated password management platform.",
        "<strong>Billing information</strong> — business and billing contact details. bcom ICT does not store customer payment card numbers.",
        "<strong>Website information</strong> — standard server logs. This website does not run advertising or third-party tracking.",
    ]),
    ("Why we collect it", [
        "To provide the IT services you have engaged us for",
        "To respond to enquiries and provide quotes",
        "To administer, monitor and secure systems we manage on your behalf",
        "To invoice and maintain business records we are required to keep",
        "To meet legal and insurance obligations",
    ]),
    ("Who we disclose it to", [
        "<strong>Vendor platforms</strong> used to deliver services — monitoring, ticketing, endpoint protection and backup. These process operational data as part of providing those services.",
        "<strong>Cabling contractors</strong> engaged for physical installation work. They work on infrastructure and are not given access to your systems or data.",
        "<strong>Professional advisers and insurers</strong>, where required.",
        "<strong>Law enforcement or regulators</strong>, where we are legally required to do so.",
        "We do not sell personal information, and we do not disclose it for marketing by anyone else.",
    ]),
    ("Where it is held", [
        "Microsoft 365 tenancies bcom ICT provisions are created in <strong>Australian regions</strong>.",
        "Backup location is agreed per client and recorded in the relevant agreement. Australian-hosted backup is available.",
        "Some vendor platforms used for monitoring, ticketing and endpoint protection <strong>process operational data outside Australia</strong>. This is telemetry and support records rather than the contents of client files.",
        "We will identify the location of any system holding your information on request.",
    ]),
    ("How we protect it", [
        "Individually named accounts for every technician — no shared logins into client environments",
        "Multi-factor authentication enforced on every tool used to reach client systems",
        "Client credentials held in a dedicated password management platform, never in documents or email",
        "Access reviewed when staff change and revoked the day someone leaves",
        "Practices aligned to ISO/IEC 27001:2022 and the ASD Essential Eight. bcom ICT is not certified to ISO/IEC 27001",
        "Technicians attending sites hold national police checks, and Queensland Blue Cards where a site requires them",
    ]),
    ("Access, correction and complaints", [
        "You may request access to the personal information we hold about you, and ask us to correct it if it is inaccurate. Email <a href='mailto:support@bcomservices.com'>support@bcomservices.com</a> or call 07 3041 8993.",
        "We will respond within a reasonable period. There is no charge for making a request.",
        "If you are not satisfied with how we have handled your information or your complaint, you may contact the Office of the Australian Information Commissioner at <a href='https://www.oaic.gov.au' rel='nofollow'>oaic.gov.au</a>.",
    ]),
    ("Data breaches", [
        "bcom ICT operates a documented incident response process. If a breach affected systems or data belonging to a client, we would notify the affected clients.",
        "Where your business holds personal information, obligations under the Notifiable Data Breaches scheme sit with your business rather than with bcom ICT. We provide the factual technical account you need for your assessment — see our <a href='/notifiable-data-breach-guide-australia'>NDB guide</a>.",
    ]),
    ("Retention", [
        "Support and billing records are retained for the period our legal and insurance obligations require, then deleted.",
        "On the end of an engagement, credentials, asset register and documentation are handed over to you. Backup data held on your behalf is returned or destroyed as you direct, and we confirm in writing which occurred.",
    ]),
]

body = "".join(
    f'<h2 style="margin-top:48px">{h}</h2>{ticks(items)}' for h, items in SECTIONS)

FAQS = [
    ("Does bcom ICT sell personal information?",
     "No. bcom ICT does not sell personal information and does not disclose it for marketing by any other party. Information is disclosed only to vendor platforms used to deliver services, contractors engaged for physical installation work, professional advisers and insurers where required, and law enforcement or regulators where legally required."),
    ("Where is our data stored?",
     "Microsoft 365 tenancies bcom ICT provisions are created in Australian regions. Backup location is agreed per client and recorded in the agreement, with Australian-hosted backup available. Some vendor platforms used for monitoring and ticketing process operational data outside Australia — bcom ICT will identify the location of any system holding your information on request."),
    ("How do we request access to our information?",
     "Email support@bcomservices.com or call 07 3041 8993. There is no charge, and we will respond within a reasonable period. If you are not satisfied with our handling, you may contact the Office of the Australian Information Commissioner."),
    ("Does this website track us?",
     "This website does not run advertising or third-party tracking. Standard server logs are kept for security and operational purposes."),
]

PAGE = {
    "path": "/privacy-policy",
    "priority": "0.3",
    "title": "Privacy Policy | bcom ICT",
    "description": "How bcom ICT collects, uses, discloses, stores and protects personal information, in line with the Australian Privacy Principles. Access, correction and complaints.",
    "hero_kind": "doc",
    "eyebrow": "Legal",
    "h1": "Privacy policy",
    "lede": "How bcom ICT handles personal information, in line with the Australian Privacy Principles. Written to be read rather than to be impenetrable.",
    "crumbs": [("Privacy policy", "/privacy-policy")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT — the trading name of Bcom Services Pty Ltd, ABN 92 636 893 108 — collects
    personal information to provide IT services, administer systems on behalf of clients, and meet legal and
    insurance obligations. bcom ICT does not sell personal information. Contact support@bcomservices.com or
    07 3041 8993 to access or correct what we hold.</p>

    <p style="margin-top:32px">This policy applies to Bcom Services Pty Ltd (ABN 92 636 893 108), trading as
    bcom ICT, of 9 Ferny Avenue, Surfers Paradise QLD 4217. It describes how we handle personal information
    in accordance with the Australian Privacy Principles under the Privacy Act 1988 (Cth).</p>
    <p style="margin-top:16px">Where bcom ICT manages systems for a client, that client remains responsible
    for the personal information held in their own systems. Our role is to help them meet their obligations,
    not to assume them.</p>

    {body}

    <h2 style="margin-top:48px">Changes to this policy</h2>
    <p style="margin-top:16px">We may update this policy from time to time. The review date below reflects
    when it was last checked. Material changes affecting existing clients are communicated directly.</p>

    <h2 style="margin-top:48px">Contact</h2>
    <p style="margin-top:16px">Privacy enquiries: <a href="mailto:support@bcomservices.com">support@bcomservices.com</a>
    · 07 3041 8993 · 9 Ferny Avenue, Surfers Paradise QLD 4217.</p>
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Data handling & sovereignty", "/data-handling-and-sovereignty"),
  ("Terms and conditions", "/terms-and-conditions"),
  ("Trust centre", "/trust-centre"),
  ("Notifiable Data Breaches guide", "/notifiable-data-breach-guide-australia"),
  ("Published service levels", "/service-levels-and-security"),
  ("Contact us", "/contact"),
], heading="Related")}

{cta("Questions about how we handle your information?",
     "Email support@bcomservices.com or call 07 3041 8993. We'll answer specifically rather than pointing you back at this page.")}
''',
}

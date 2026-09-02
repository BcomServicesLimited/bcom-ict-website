"""Privacy policy — ported from the previous bcom ICT site and updated for the
business-only positioning, the named remote-support tool, and current data
locations. Structure follows the original, which covered remote access and
telecommunications data that a generic template would miss.
NOT lawyer-reviewed — see BUILD-STATUS.md."""
from layout import MARK, cta, faq_block, ticks, related

S = [
 ("1. Introduction", [
  "This policy explains how Bcom Services Pty Ltd, ABN 92 636 893 108, trading as bcom ICT, collects, holds, uses and discloses personal information.",
  "It is written to comply with the Privacy Act 1988 (Cth) and the Australian Privacy Principles.",
  "Where bcom ICT manages systems for a client, that client remains responsible for the personal information held in their own systems. Our role is to help them meet their obligations, not to assume them.",
 ]),
 ("2. Personal information we collect", [
  "<strong>Contact and identity information</strong> — name, business name, position, email address, phone number and business address, provided when you enquire, engage us, or are recorded as a contact for a client we support.",
  "<strong>Technical and device information</strong> — device names, operating system and patch status, hardware details, network configuration and security alerts for systems we manage. This is information about your environment rather than the contents of your files.",
  "<strong>Financial and billing information</strong> — business and billing contact details, purchase orders and invoice records. <strong>bcom ICT does not store customer payment card numbers.</strong>",
  "<strong>Service records</strong> — support requests, what was done, and any logs, screenshots or files attached to a job. Attachments can incidentally contain business information, so tickets are treated as confidential.",
 ]),
 ("3. Remote support access", [
  "Remote support is provided using <strong>Splashtop SOS</strong>, which runs as a temporary application for the duration of a session and installs nothing permanent on your device.",
  "A session cannot begin without a code generated on your machine and given to us by you. You can see the entire session on your own screen and end it at any moment.",
  "Access ends when the session ends. Persistent monitoring access exists only where a managed services agreement provides for it, agreed separately in writing.",
  "We do not access client systems without a request or an agreed monitoring arrangement.",
 ]),
 ("4. Telecommunications services data", [
  "Where bcom ICT supplies or supports telecommunications services, call detail records may be processed by the underlying carrier or platform — typically number called, time and duration.",
  "bcom ICT does not record the content of calls unless call recording has been specifically configured at a client's request, in which case the client is responsible for meeting their own notification and consent obligations.",
  "Telecommunications services are provided in accordance with the Telecommunications Act 1997 and ACMA regulations.",
 ]),
 ("5. Website data and cookies", [
  "This website does not run advertising or third-party behavioural tracking.",
  "Standard server logs are kept for security and operational purposes.",
  "Where a page embeds a third-party service — our online booking calendar, or the Google map on the contact and about pages — that service may set its own cookies under its own privacy terms.",
 ]),
 ("6. How we collect it", [
  "<strong>Directly</strong> — when you call, email, submit an enquiry form, book an appointment or engage us for work.",
  "<strong>Indirectly</strong> — from systems we manage on behalf of a client, and from a client who provides contact details for their staff so we can support them.",
  "We collect only what we need to provide the services we have been engaged for.",
 ]),
 ("7. Why we collect it", [
  "To provide the IT and telecommunications services you have engaged us for",
  "To respond to enquiries and provide quotations",
  "To administer, monitor and secure systems we manage on your behalf",
  "To invoice and to maintain business records we are required to keep",
  "To meet legal, regulatory and insurance obligations",
 ]),
 ("8. Who we disclose it to", [
  "<strong>Vendor platforms</strong> used to deliver services — monitoring, ticketing, endpoint protection, backup and remote support. These process operational data as part of providing those services.",
  "<strong>Carriers and telecommunications providers</strong>, where services depend on them.",
  "<strong>Cabling contractors</strong> engaged for physical installation work. They work on infrastructure and are not given access to your systems or data.",
  "<strong>Professional advisers and insurers</strong>, where required.",
  "<strong>Law enforcement or regulators</strong>, where we are legally required to do so.",
  "<strong>We do not sell personal information</strong>, and we do not disclose it for marketing by anyone else.",
 ]),
 ("9. Overseas disclosure", [
  "Microsoft 365 tenancies provisioned by bcom ICT are created in <strong>Australian regions</strong>, so client mail and files are held in Australian data centres.",
  "Backup location is agreed per client and recorded in the relevant agreement. Australian-hosted backup is available and is what we recommend.",
  "<strong>Some vendor platforms used for monitoring, ticketing, endpoint protection and remote support process operational data outside Australia.</strong> This is telemetry and support records rather than the contents of client files, and we will not pretend otherwise.",
  "We will identify the location of any system holding your information on request. If Australian-only processing is a requirement for your business, tell us before we design the service.",
 ]),
 ("10. Data security", [
  "Individually named accounts for every technician — no shared logins into client environments",
  "Multi-factor authentication enforced on every tool used to reach a client system",
  "Client credentials held in a dedicated password management platform, never in documents or email",
  "Access reviewed when staff change, and revoked the day someone leaves",
  "Practices aligned to ISO/IEC 27001:2022 and the ASD Essential Eight. <strong>bcom ICT is not certified to ISO/IEC 27001.</strong>",
  "Technicians attending sites hold national police checks, and Queensland Blue Cards where a site requires them",
 ]),
 ("11. Data retention", [
  "Support and billing records are retained for the period our legal, tax and insurance obligations require, then deleted.",
  "On the end of an engagement, credentials, asset register and documentation are handed over to you.",
  "Backup data held on your behalf is returned or destroyed as you direct, and we confirm in writing which occurred.",
 ]),
 ("12. Access and correction", [
  "You may request access to the personal information we hold about you, and ask us to correct it if it is inaccurate, out of date or incomplete.",
  "Email <a href='mailto:support@bcomservices.com'>support@bcomservices.com</a> or call 07 3041 8993. There is no charge for making a request, and we will respond within a reasonable period.",
  "Where we are unable to provide access — for example where doing so would disclose another party's information — we will explain why.",
 ]),
 ("13. Data breaches", [
  "bcom ICT operates a documented incident response process. If a breach affected systems or data belonging to a client, we would notify the affected clients.",
  "Where your business holds personal information, obligations under the Notifiable Data Breaches scheme sit with your business rather than with bcom ICT. We provide the factual technical account you need for your assessment — see our <a href='/notifiable-data-breach-guide-australia'>NDB guide</a>.",
 ]),
 ("14. Complaints", [
  "If you are concerned about how we have handled your personal information, contact us first at <a href='mailto:support@bcomservices.com'>support@bcomservices.com</a> or 07 3041 8993. We will investigate and respond.",
  "If you are not satisfied with our response, you may contact the Office of the Australian Information Commissioner at <a href='https://www.oaic.gov.au' rel='nofollow'>oaic.gov.au</a>.",
 ]),
 ("15. Updates to this policy", [
  "We may update this policy from time to time. The review date below reflects when it was last checked.",
  "Material changes affecting existing clients are communicated directly rather than only posted here.",
 ]),
]

body = "".join(f'<h2 style="margin-top:48px">{h}</h2>{ticks(items)}' for h, items in S)

FAQS = [
    ("Does bcom ICT sell personal information?",
     "No. bcom ICT does not sell personal information and does not disclose it for marketing by any other party. It is disclosed only to vendor platforms used to deliver services, carriers where services depend on them, contractors engaged for physical installation work, professional advisers and insurers where required, and law enforcement or regulators where legally required."),
    ("Where is our data stored?",
     "Microsoft 365 tenancies bcom ICT provisions are created in Australian regions, so mail and files are held in Australian data centres. Backup location is agreed per client and recorded in the agreement. Some vendor platforms used for monitoring, ticketing and remote support process operational data outside Australia — bcom ICT will identify the location of any system holding your information on request."),
    ("Can bcom ICT access our computers without asking?",
     "No. Remote support uses Splashtop SOS, which needs a session code generated on your machine and given to us by you — a session cannot start without it, and access ends when the session does. Persistent monitoring access exists only where a managed services agreement provides for it, agreed separately in writing."),
    ("Do you record our phone calls?",
     "No, unless call recording has been specifically configured at your request. Where it has, your business is responsible for meeting its own notification and consent obligations. Carriers may process call detail records — number called, time and duration — as part of delivering the service."),
    ("How do we request access to our information?",
     "Email support@bcomservices.com or call 07 3041 8993. There is no charge and we will respond within a reasonable period. If you are not satisfied with our handling, you may contact the Office of the Australian Information Commissioner."),
    ("Does this website track us?",
     "This website runs no advertising and no third-party behavioural tracking. Standard server logs are kept for security and operational purposes. Embedded third-party services — the online booking calendar and the Google map — may set their own cookies under their own terms."),
]

PAGE = {
    "path": "/privacy-policy",
    "priority": "0.3",
    "title": "Privacy Policy | bcom ICT",
    "description": "How bcom ICT collects, holds, uses and discloses personal information under the Australian Privacy Principles.",
    "hero_kind": "doc",
    "eyebrow": "Legal",
    "h1": "Privacy policy",
    "lede": "How bcom ICT handles personal information, under the Australian Privacy Principles. Written to be read rather than to be impenetrable.",
    "crumbs": [("Privacy policy", "/privacy-policy")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT — the trading name of Bcom Services Pty Ltd, ABN 92 636 893 108 — collects
    personal information to provide IT and telecommunications services, administer systems on behalf of
    clients, and meet legal and insurance obligations. bcom ICT does not sell personal information. Contact
    support@bcomservices.com or 07 3041 8993 to access or correct what we hold.</p>

    <p style="margin-top:32px">This policy applies to Bcom Services Pty Ltd (ABN 92 636 893 108), trading as
    bcom ICT, of the Gold Coast, Queensland, and is written to comply with the Privacy Act
    1988 (Cth) and the Australian Privacy Principles.</p>

    {body}

    <h2 style="margin-top:48px">Contact</h2>
    <p style="margin-top:16px">Privacy enquiries: <a href="mailto:support@bcomservices.com">support@bcomservices.com</a>
    · 07 3041 8993 · Gold Coast QLD, Australia. Business hours 8:00am – 5:00pm,
    Monday to Friday, Brisbane time.</p>
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

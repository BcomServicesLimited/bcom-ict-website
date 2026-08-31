"""Terms and conditions — ported from the previous bcom ICT site and updated for
the business-only positioning, the corrected hours (8am-5pm Mon-Fri Brisbane)
and the published rates. Structure and the telecoms-specific clauses come from
the original, which was considerably more thorough than a generic MSP template.
NOT lawyer-reviewed — see BUILD-STATUS.md."""
from layout import MARK, cta, faq_block, ticks, related
from site_data import BIZ

S = [
 ("1. Introduction and acceptance", [
  "These Terms and Conditions form a binding agreement between you (the Client) and Bcom Services Pty Ltd, ABN 92 636 893 108, trading as bcom ICT, for the provision of IT support, telecommunications and related technical services.",
  "By requesting services, accepting a quotation, booking an appointment or otherwise using our services, you agree to these Terms.",
  "These Terms operate under Australian law, including the Competition and Consumer Act 2010 (Australian Consumer Law), the Telecommunications Act 1997, the Privacy Act 1988 and the Fair Trading Act 1989 (Qld).",
  "Where a separate written agreement exists — a managed services agreement, telecommunications service agreement or service level agreement — that agreement takes precedence over these Terms to the extent of any inconsistency.",
 ]),
 ("2. Who we provide services to", [
  "bcom ICT provides services to <strong>business clients</strong>. We no longer take on general residential IT support or home computer repair.",
  "We do still install WiFi and mesh networks for home offices, and those engagements are covered by these Terms.",
  "Nothing in these Terms excludes, restricts or modifies any consumer guarantee, right or remedy under the Australian Consumer Law that cannot lawfully be excluded.",
 ]),
 ("3. Services", [
  "<strong>IT services</strong> may include computer diagnostics and repair, managed IT support, Microsoft 365 and Google Workspace setup and migration, network and WiFi installation, cybersecurity, cloud services, and remote and on-site technical support.",
  "<strong>Telecommunications services</strong> may include cloud PBX, VoIP phone systems, Microsoft Teams Phone, SIP trunking, business phone system installation and telecommunications consulting. These are provided in accordance with ACMA regulations and the Telecommunications Act 1997.",
  "<strong>Remote support</strong> is provided using Splashtop SOS, a temporary application run with your permission for the duration of the session. Instructions are on our <a href='/support'>support page</a>.",
  "<strong>Cabling.</strong> Fixed cabling connected to the telecommunications network requires ACMA cabler registration. bcom ICT does not hold that registration — cabling is carried out by ACMA registered cabling contractors we engage and manage.",
 ]),
 ("4. Pricing and fees", [
  "All pricing is quoted in Australian dollars and is <strong>exclusive of GST unless stated otherwise</strong>. GST is applied at the prevailing rate.",
  "<strong>Hourly labour:</strong> $190 + GST per hour ($209.00 inc GST), billed in half-hour increments after the first hour.",
  "<strong>On-site call-out:</strong> $100 + GST ($110.00 inc GST) per attendance. Remote support carries no call-out.",
  "<strong>Managed IT</strong> is a flat monthly fee calculated from your business requirements and the services included, set out in a separate agreement.",
  "<strong>Projects</strong> are quoted as a fixed price after scoping. Variations are agreed in writing before the additional work is carried out.",
  "Time spent on consultation, discovery, planning and scope alignment forms part of service delivery and is charged at standard hourly rates or allocated against prepaid project amounts.",
  "You will not be invoiced for work you did not approve.",
 ]),
 ("5. Payment terms", [
  "Unless otherwise agreed in writing, invoices are payable within 14 days.",
  "Services under $500 may require payment on completion, and project work may require a deposit before commencement.",
  "We may suspend non-critical work where invoices remain more than 30 days overdue, after notifying you.",
  "<strong>We will not withhold access to your own systems, credentials or documentation over a payment dispute.</strong>",
 ]),
 ("6. Hardware ownership", [
  "Hardware, equipment and software supplied by bcom ICT remain our property until paid in full.",
  "We reserve the right to recover equipment where invoices remain unpaid.",
  "Hardware and software carry the manufacturer's or publisher's warranty. We will assist with warranty claims but do not extend those warranties ourselves.",
 ]),
 ("7. Managed services and fair use — remote IT support", [
  "Where a plan includes unlimited remote IT support, that is intended for reasonable day-to-day operational assistance: troubleshooting, user support, software configuration, remote diagnostics and minor system adjustments.",
  "It does <strong>not</strong> include infrastructure rebuilds, major system upgrades, large deployments, cybersecurity incident response, on-site services, or training and consulting projects.",
  "Where usage becomes excessive or falls outside normal operational levels, we may convert work to billable services, recommend a plan change, or schedule the work as a project.",
  "<strong>Unlimited refers to the absence of hourly billing for covered tasks — not to unlimited technician availability.</strong>",
 ]),
 ("8. Fair use — unlimited outbound calling", [
  "Where telecommunications services include unlimited outbound calling to Australian and New Zealand numbers, that is intended for normal business communication.",
  "It excludes telemarketing campaigns, call centres, automated dialling systems, bulk outbound calling, premium rate numbers and international destinations outside Australia and New Zealand.",
  "We may apply additional charges or modify plans where usage significantly exceeds normal business patterns.",
 ]),
 ("9. Carrier and infrastructure dependency", [
  "Telecommunications and internet services rely on third-party carriers, internet providers and infrastructure networks that bcom ICT does not control.",
  "Interruptions may occur due to NBN outages, internet provider faults, carrier outages, power failures or upstream voice carrier failures.",
  "bcom ICT is not responsible for outages within third-party infrastructure. We will advocate on your behalf and escalate with evidence, but cannot guarantee another provider's performance.",
 ]),
 ("10. Emergency services — VoIP", [
  "<strong>VoIP and cloud phone services depend on internet connectivity and mains power.</strong> During an internet or power outage, access to 000 or 112 emergency services may be unavailable.",
  "Clients should maintain an alternative means of emergency communication, such as a mobile phone.",
  "bcom ICT does not guarantee emergency call availability during a service outage.",
 ]),
 ("11. Telephone numbers and porting", [
  "Telephone numbers supplied as part of VoIP or cloud services may be provided through third-party carriers. bcom ICT does not guarantee permanent ownership of numbers supplied through hosted services.",
  "Number porting may be requested, subject to carrier approval, correct account information and accounts being paid in full.",
  "Where services are terminated without porting a number, that number may return to the carrier and may become unavailable.",
 ]),
 ("12. Support availability and response", [
  "<strong>Standard support hours are 8:00am to 5:00pm, Monday to Friday, Brisbane time</strong>, excluding public holidays.",
  "Outside those hours our digital assistant answers the phone, takes your details and logs the job. <strong>We do not respond to phone enquiries after hours.</strong> Calls are returned the next business day.",
  "After-hours on-call support is available to managed and SLA clients under their agreement, and is not available ad hoc.",
  "Response targets by priority are published on our <a href='/service-levels-and-security'>service levels page</a>. Guaranteed response times apply only where a formal service level agreement exists.",
  "Response means a person has picked the job up and contacted you. Resolution times vary too widely by fault to be committed to.",
 ]),
 ("13. Client responsibilities", [
  "Maintaining valid software licences for anything you ask us to install or support.",
  "Providing safe and reasonable access to systems and premises when required.",
  "Maintaining adequate data backups where backup services are not contracted to bcom ICT.",
  "Safeguarding passwords and system access, and notifying us promptly of any suspected security incident.",
  "Telling us about changes made to your environment by you or another provider — undocumented changes are a common cause of faults.",
 ]),
 ("14. Cybersecurity", [
  "No IT system can guarantee complete protection from ransomware, malware, phishing, unauthorised access or zero-day vulnerabilities. bcom ICT cannot guarantee that systems will be immune from cyber incidents.",
  "Where cybersecurity recommendations are declined, bcom ICT is not responsible for incidents resulting from those decisions.",
  "We may refuse or limit support for systems that pose a significant cybersecurity risk — including unsupported operating systems, unlicensed software, systems without basic security protections, and systems missing critical updates.",
 ]),
 ("15. Liability", [
  "<strong>Nothing in these Terms excludes, restricts or modifies any consumer guarantee, right or remedy under the Australian Consumer Law that cannot lawfully be excluded.</strong>",
  "Where the Australian Consumer Law permits us to limit liability, our liability is limited to resupplying the services or paying the cost of having them resupplied.",
  "To the extent permitted by law, bcom ICT is not liable for indirect or consequential loss, including loss of data, loss of revenue, loss of profits or business interruption.",
  "We are not liable for loss arising from your failure to maintain backups where you have not engaged us to provide them.",
 ]),
 ("16. Privacy and confidentiality", [
  "Information about your business obtained in the course of providing services is treated as confidential.",
  "Personal information is handled in accordance with our <a href='/privacy-policy'>privacy policy</a>. Where data is held is set out on <a href='/data-handling-and-sovereignty'>data handling and sovereignty</a>.",
  "Your documentation, asset register, credentials and licences belong to you and are provided on request at any time — not only on exit.",
 ]),
 ("17. Termination", [
  "Managed IT agreements are month-to-month. Either party may end the arrangement with the notice set out in the agreement. There is no exit fee.",
  "On termination, your documentation, credentials, asset register and licences are handed over in a usable form, and we will speak with an incoming provider to hand over cleanly.",
  "Backup data held on your behalf is returned or destroyed as you direct, and we confirm in writing which occurred.",
 ]),
 ("18. Governing law", [
  "These Terms are governed by the laws of Queensland, Australia.",
  "If any provision is found unenforceable, the remainder continues to apply.",
 ]),
]

body = "".join(f'<h2 style="margin-top:48px">{h}</h2>{ticks(items)}' for h, items in S)

FAQS = [
    ("What are bcom ICT's rates?",
     "Hourly labour is $190 + GST ($209.00 inc GST), billed in half-hour increments after the first hour. On-site attendance adds a $100 + GST call-out ($110.00 inc GST). Remote support carries no call-out. Managed IT is a flat monthly fee calculated from your requirements and the services included. All pricing is exclusive of GST unless stated otherwise."),
    ("What are your support hours?",
     "8:00am to 5:00pm, Monday to Friday, Brisbane time, excluding public holidays. Outside those hours our digital assistant answers the phone and takes your details, but bcom ICT does not respond to phone enquiries after hours — calls are returned the next business day. After-hours on-call support is available to managed and SLA clients under their agreement."),
    ("Can we call 000 from a VoIP phone?",
     "VoIP and cloud phone services depend on internet connectivity and mains power. During an internet or power outage, access to 000 or 112 may be unavailable. Clients should keep an alternative means of emergency communication such as a mobile phone. bcom ICT does not guarantee emergency call availability during an outage."),
    ("What does \"unlimited\" remote support actually cover?",
     "Reasonable day-to-day operational assistance — troubleshooting, user support, software configuration, remote diagnostics and minor adjustments. It does not include infrastructure rebuilds, major upgrades, large deployments, incident response, on-site work or consulting projects. Unlimited means no hourly billing for covered tasks, not unlimited technician availability."),
    ("Do these terms limit our consumer rights?",
     "No. Nothing in these Terms excludes, restricts or modifies any consumer guarantee, right or remedy under the Australian Consumer Law that cannot lawfully be excluded. Where the law permits a limitation, our liability is limited to resupplying the services or paying the cost of resupply."),
    ("Who owns our phone numbers?",
     "Numbers supplied through hosted VoIP services may come from third-party carriers, and bcom ICT does not guarantee permanent ownership of them. Porting can be requested subject to carrier approval, correct account details and accounts being paid in full. If services end without porting, a number may return to the carrier."),
]

PAGE = {
    "path": "/terms-and-conditions",
    "priority": "0.3",
    "title": "Terms & Conditions | bcom ICT",
    "description": "bcom ICT's terms of service — services, pricing, payment, fair use, carrier dependency, VoIP emergency calling, support hours, liability under Australian Consumer Law and termination.",
    "hero_kind": "doc",
    "eyebrow": "Legal",
    "h1": "Terms and conditions",
    "lede": "The terms bcom ICT provides services under. Written in plain English, because terms nobody reads protect nobody.",
    "crumbs": [("Terms and conditions", "/terms-and-conditions")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">These terms apply to services provided by Bcom Services Pty Ltd, ABN 92 636 893 108,
    trading as bcom ICT. Work is quoted before it starts. Hourly labour is $190 + GST, with a $100 + GST
    call-out for on-site attendance; remote support carries no call-out. Support hours are 8:00am to 5:00pm,
    Monday to Friday, Brisbane time. Managed IT agreements are month-to-month with no exit fee.</p>

    <p style="margin-top:32px">These Terms apply where no separate written agreement exists. Where a managed
    services agreement, telecommunications service agreement or service level agreement has been signed, that
    agreement prevails to the extent of any inconsistency.</p>

    {body}

    <h2 style="margin-top:48px">Contact</h2>
    <p style="margin-top:16px">Bcom Services Pty Ltd, ABN 92 636 893 108, trading as bcom ICT ·
    9 Ferny Avenue, Surfers Paradise QLD 4217 ·
    <a href="mailto:support@bcomservices.com">support@bcomservices.com</a> · 07 3041 8993 ·
    Jurisdiction: Queensland, Australia.</p>
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Privacy policy", "/privacy-policy"),
  ("Published service levels", "/service-levels-and-security"),
  ("Pricing", "/pricing"),
  ("Data handling & sovereignty", "/data-handling-and-sovereignty"),
  ("Trust centre", "/trust-centre"),
  ("Contact us", "/contact"),
], heading="Related")}

{cta("Something here you'd want changed?",
     "If you're engaging us and a term doesn't work for your business, say so before signing. Most things are discussable.")}
''',
}

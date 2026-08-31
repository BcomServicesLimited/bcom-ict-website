from layout import MARK, cta, faq_block, ticks, related

SECTIONS = [
    ("Quotes and approval", [
        "We quote before starting work. On-site attendance is charged at a $100 + GST call-out plus $198 + GST per hour, billed in hourly increments.",
        "Remote support is charged at $198 + GST per hour with no call-out.",
        "Managed IT is a flat monthly fee calculated from your business requirements and the services included, set out in a separate agreement.",
        "Projects are quoted as a fixed price after scoping. Variations are agreed in writing before the additional work is carried out.",
        "You will not be invoiced for work you did not approve.",
    ]),
    ("Payment", [
        "Invoices are payable within the terms stated on the invoice.",
        "All prices are exclusive of GST unless stated otherwise. GST is applied at the prevailing rate.",
        "Hardware and third-party software remain the property of bcom ICT until paid in full.",
        "Where an account is overdue, we may suspend non-critical work after notifying you. We will not withhold access to your own systems, credentials or documentation over a payment dispute.",
    ]),
    ("Service levels", [
        "Response targets are published at <a href='/service-levels-and-security'>service levels</a> and form part of managed IT agreements.",
        "Response means a person has picked the job up and contacted you. Resolution times vary too widely by fault to be committed to, and we do not commit to them.",
        "Phones are answered 24/7. After hours, calls are handled by an AI operator that takes details and escalates. Work is actioned during business hours except for managed and SLA clients on a critical fault.",
    ]),
    ("Your responsibilities", [
        "Providing safe and reasonable access to premises and systems where on-site work is required.",
        "Holding appropriate licences for software you ask us to install or support.",
        "Maintaining your own backups where bcom ICT has not been engaged to provide backup as a service.",
        "Telling us about changes to your environment made by you or by another provider, since undocumented changes are a common cause of faults.",
    ]),
    ("Data and confidentiality", [
        "Information about your business obtained in the course of providing services is treated as confidential.",
        "Handling of personal information is set out in our <a href='/privacy-policy'>privacy policy</a>, and where data is held is set out on <a href='/data-handling-and-sovereignty'>data handling and sovereignty</a>.",
        "Your documentation, asset register, credentials and licences belong to you and are handed over on request at any time, not only on exit.",
    ]),
    ("Third-party products and services", [
        "Hardware and software supplied by bcom ICT carry the manufacturer's or publisher's warranty. We will assist with warranty claims but do not extend those warranties ourselves.",
        "Fixed cabling work is carried out by ACMA registered cabling contractors that bcom ICT engages and manages. bcom ICT does not hold cabler registration.",
        "Where a service depends on a third party — an internet provider, a software vendor, a carrier — we will advocate on your behalf but cannot guarantee their performance.",
    ]),
    ("Liability", [
        "<strong>Nothing in these terms excludes, restricts or modifies any consumer guarantee, right or remedy under the Australian Consumer Law that cannot lawfully be excluded.</strong>",
        "Where the Australian Consumer Law permits us to limit liability, our liability is limited to resupplying the services or paying the cost of having them resupplied.",
        "To the extent permitted by law, bcom ICT is not liable for indirect or consequential loss, including loss of profits or business interruption.",
        "We are not liable for loss arising from your failure to maintain backups where you have not engaged us to provide them.",
    ]),
    ("Termination", [
        "Managed IT agreements are month-to-month. Either party may end the arrangement with notice as set out in the agreement. There is no exit fee.",
        "On termination, your documentation, credentials, asset register and licences are handed over in a usable form, and we will speak with an incoming provider to hand over cleanly.",
        "Backup data held on your behalf is returned or destroyed as you direct, and we confirm in writing which occurred.",
    ]),
    ("General", [
        "These terms are governed by the laws of Queensland, Australia.",
        "Where a separate written agreement exists between bcom ICT and a client, that agreement prevails over these terms to the extent of any inconsistency.",
        "If any provision is found unenforceable, the remainder continues to apply.",
    ]),
]

body = "".join(f'<h2 style="margin-top:48px">{h}</h2>{ticks(items)}' for h, items in SECTIONS)

FAQS = [
    ("What are bcom ICT's rates?",
     "On-site work is a $100 + GST call-out ($110 inc GST) plus $198 + GST per hour ($217.80 inc GST), billed in hourly increments. Remote support is $198 + GST per hour with no call-out. Managed IT is a flat monthly fee calculated from your requirements and the services included. Everything is quoted before work starts."),
    ("Are there lock-in contracts?",
     "No. Managed IT agreements are month-to-month with no exit fee. On termination your documentation, credentials, asset register and licences are handed over in a usable form."),
    ("Do these terms limit our consumer rights?",
     "No. Nothing in these terms excludes, restricts or modifies any consumer guarantee, right or remedy under the Australian Consumer Law that cannot lawfully be excluded. Where the law permits a limitation, our liability is limited to resupplying the services or paying the cost of resupply."),
    ("What happens if we have a payment dispute?",
     "We may suspend non-critical work after notifying you, but we will not withhold access to your own systems, credentials or documentation over a payment dispute. Holding a client's own data as leverage is not something we do."),
    ("Who owns our documentation?",
     "You do. Asset register, network documentation, credentials and licence details belong to your business and are provided on request at any time — not only when an engagement ends."),
]

PAGE = {
    "path": "/terms-and-conditions",
    "priority": "0.3",
    "title": "Terms & Conditions | bcom ICT",
    "description": "bcom ICT's terms of service — quotes and approval, rates, payment, service levels, data and confidentiality, liability under Australian Consumer Law, and termination.",
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
    trading as bcom ICT. Work is quoted before it starts. On-site attendance is a $100 + GST call-out plus
    $198 + GST per hour; remote support is $198 + GST per hour with no call-out. Managed IT agreements are
    month-to-month with no exit fee.</p>

    <p style="margin-top:32px">These terms apply where no separate written agreement exists. Where a separate
    agreement has been signed, that agreement prevails to the extent of any inconsistency.</p>

    {body}

    <h2 style="margin-top:48px">Contact</h2>
    <p style="margin-top:16px">Bcom Services Pty Ltd, ABN 92 636 893 108, trading as bcom ICT ·
    9 Ferny Avenue, Surfers Paradise QLD 4217 ·
    <a href="mailto:support@bcomservices.com">support@bcomservices.com</a> · 07 3041 8993.</p>
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

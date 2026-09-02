from layout import MARK, cta, faq_block, cards, related, trust_note

CORE = [
    ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast",
     "Someone looking after your IT every day for a flat monthly fee. Monitoring, unlimited helpdesk, patching and backup. Month-to-month, no lock-in."),
    ("Business IT Support", "/it-support-and-services-gold-coast",
     "Something's broken and your staff can't work. Same-day on-site visits across the Gold Coast, or remote help in minutes."),
    ("Cybersecurity", "/cybersecurity-services-gold-coast",
     "Protection against what actually happens — invoice scams, account takeovers and ransomware. Built to the Australian Essential Eight baseline."),
    ("Business WiFi & Networks", "/business-wifi-gold-coast",
     "WiFi that works in every corner of the building, with guests kept away from your business systems. UniFi and Aruba, surveyed before it's quoted."),
    ("Business Phone Systems", "/business-phone-systems-gold-coast",
     "Cloud VoIP and on-premise PBX, installed and supported — including the legacy systems most providers have walked away from."),
    ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast",
     "Email, files and Teams set up properly and kept secure, with your data held in Australia."),
]

SECURITY = [
    ("Cybersecurity Risk Assessment", "/cybersecurity-health-check-for-small-business-gold-coast", "Fixed-fee health check across email, accounts, devices, backups and network."),
    ("24/7 Security Operations Centre", "/security-operations-centre-gold-coast", "Continuous monitored threat detection and response, day and night."),
    ("Cyber Incident Response", "/cyber-incident-response-gold-coast", "Containment, investigation, recovery and the reporting your insurer needs."),
    ("Essential Eight Assessment", "/essential-eight-guide-gold-coast", "Where you sit against the ASD baseline, and what the next level takes."),
    ("ASIC Cybersecurity Compliance", "/asic-cybersecurity-compliance-gold-coast", "Cyber resilience evidence for AFS licensees, brokers and accountants."),
    ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast", "Automated backup with restores actually tested, not assumed."),
]

INFRA = [
    ("Office Network Cabling", "/network-cabling-for-offices-gold-coast", "Cat6 and Cat6A structured cabling, installed by ACMA registered cabling contractors."),
    ("Network Security & Firewall", "/network-security-and-firewall-configuration-gold-coast", "Firewalls, VLANs, secure remote access and guest isolation."),
    ("Network Troubleshooting", "/network-troubleshooting-diagnostics-gold-coast", "Dropouts, slow speeds and devices that won't connect — diagnosed properly."),
    ("VoIP Phone Systems", "/voip-phone-system-installation-and-support-gold-coast", "Cloud calling with remote extensions, queues and number porting."),
    ("PBX Systems", "/pabx-phone-systems-gold-coast", "LG Ericsson, Panasonic, NEC and Alcatel-Lucent, installed and maintained."),
    ("Business NBN & Internet", "/nbn-internet-support-gold-coast", "Connection faults, ISP escalation and 4G/5G failover so you keep trading."),
]

CONSULT = [
    ("IT Consulting & Strategy", "/it-consulting-strategy-gold-coast", "Roadmaps, budgets and vendor-neutral advice with no hardware commissions."),
    ("Microsoft 365 Setup & Support", "/microsoft-365-setup-gold-coast", "Migration, configuration and ongoing support. Microsoft Partner."),
    ("Microsoft Copilot", "/microsoft-copilot-gold-coast", "Copilot rolled out with the governance and permissions work done first."),
    ("AI Implementation", "/artificial-intelligence-service-gold-coast", "Phone agents, chatbots and workflow automation that save real time."),
    ("ISO/IEC 42001 AI Governance", "/iso-42001-ai-governance-gold-coast", "AI policy, risk assessment and audit evidence, led by a BSI-certified Lead Implementer."),
    ("Office IT Relocation", "/office-it-relocation-gold-coast", "Servers, networks, cabling and phones moved and tested before Monday."),
]

HARDWARE = [
    ("Business Computer Repair", "/on-site-computer-repair-gold-coast", "Laptops, desktops and workstations repaired on site, with loan machines."),
    ("Hardware Procurement & Setup", "/hardware-procurement-setup-gold-coast", "Trade pricing, imaged and configured, deployed ready to use."),
    ("Virus & Malware Removal", "/virus-and-malware-removal-services-gold-coast", "Clean-up, credential reset and hardening so it doesn't recur."),
    ("Windows & macOS Repair", "/os-troubleshooting-repair-gold-coast", "Boot failures, crashes and failed updates fixed on site."),
    ("Performance Optimisation", "/performance-optimisation-gold-coast", "Honest advice on whether to upgrade the fleet or replace it."),
    ("Software Installation & Config", "/software-installation-configuration-gold-coast", "Business applications installed, licensed and working."),
]

FAQS = [
    ("What IT services does bcom ICT provide?",
     "bcom ICT provides managed IT, business IT support, cybersecurity, business WiFi and networking, phone systems including VoIP and PBX, cloud migration and Microsoft 365, AI implementation, cabling, hardware supply and business computer repair. On-site services cover the Gold Coast; managed, remote and cloud services are available Australia-wide. Call 07 3041 8993."),
    ("Do we have to take everything, or can we start with one thing?",
     "Start with one thing. Most clients come to us for a single problem — the WiFi, a phone system, a security scare — and hand over more once they've seen how we work. There's no bundle you have to buy into."),
    ("Which services are available outside the Gold Coast?",
     "Anything that doesn't need someone physically present. Managed IT, cybersecurity, the SOC, incident response, Microsoft 365, cloud and consulting are all delivered Australia-wide. On-site work — cabling, WiFi installs, hardware, phone system installation — is Gold Coast based."),
    ("Do you work with home users?",
     "No. bcom ICT works with businesses. We still install WiFi and mesh networks for home offices, but general home computer support isn't something we take on."),
]

PAGE = {
    "path": "/services",
    "priority": "0.9",
    "title": "Business IT Services Gold Coast | bcom ICT",
    "description": "Every IT service bcom ICT provides to Gold Coast businesses — managed IT, cybersecurity, WiFi and networking, phone systems. Call 07 3041 8993.",
    "hero_img": "hero-bg-business.webp",
    "hero_alt": "The bcom ICT team meeting with a Gold Coast business client to plan their IT services",
    "h1": "Everything we do for Gold Coast businesses",
    "lede": "Six things most clients start with, and everything else we support behind them. Start with one — most businesses do.",
    "actions": [("Get a quote", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Business clients only", "Gold Coast on-site", "Australia-wide remote", "Local since 2011"],
    "crumbs": [("Services", "/services")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT provides managed IT, business IT support, cybersecurity, business WiFi and
    networking, phone systems, cloud and Microsoft 365, AI implementation, cabling and business hardware to
    small and medium businesses. On-site services cover the Gold Coast; managed, remote and cloud services
    are available Australia-wide. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Start here</span>
      <h2>The six most businesses come to us for</h2>
    </div>
    <div class="grid grid--3">{cards(CORE)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Security &amp; continuity</span>
      <h2>Protecting the business</h2>
      <p>From a one-off health check through to continuous monitoring and the evidence a regulator or insurer will ask for.</p>
    </div>
    <div class="grid grid--3">{cards(SECURITY, icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Networks, phones &amp; connectivity</span>
      <h2>The infrastructure underneath</h2>
    </div>
    <div class="grid grid--3">{cards(INFRA, icon=False)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Consulting, cloud &amp; AI</span>
      <h2>Planning and change</h2>
    </div>
    <div class="grid grid--3">{cards(CONSULT, icon=False)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Hardware &amp; repair</span>
      <h2>Devices and the day-to-day</h2>
      <p>Business machines only — laptops, desktops, workstations and servers. We don't take on home computer repair.</p>
    </div>
    <div class="grid grid--3">{cards(HARDWARE, icon=False)}</div>

    {trust_note('Not sure which of these you need? That is what the free review is for — we look at what you are running and tell you what is worth doing first, including when the answer is that you do not need us monthly yet. <a href="/trust-centre">The trust centre</a> sets out how we work and what we commit to.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Industries we work with", "/industries"),
  ("Pricing", "/pricing"),
  ("Published service levels", "/service-levels-and-security"),
  ("Trust centre — how we work", "/trust-centre"),
  ("Case studies", "/case-studies"),
  ("About bcom ICT", "/about"),
], heading="Before you decide")}

{cta("Not sure where to start?",
     "Tell us what's frustrating you and we'll tell you which of the above actually fixes it — and roughly what it costs.")}
''',
}

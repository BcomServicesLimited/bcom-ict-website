from layout import MARK, cta, faq_block, cards, related, trust_note

SECTORS = [
    ("Small business", "/it-support-small-business-gold-coast",
     "Three to sixty staff, no internal IT, and a growing dependence on systems nobody owns. The most common shape of Gold Coast business we work with."),
    ("Healthcare & allied health", "/it-support-healthcare-gold-coast",
     "Practices carry Privacy Act obligations regardless of turnover — the small business exemption does not apply to health providers. Patient records, practice software and screened technicians."),
    ("Professional services", "/it-support-professional-services-gold-coast",
     "Accountants, lawyers, planners and consultants. Client confidentiality, document management, and regulators increasingly asking how you protect what you hold."),
    ("Real estate", "/it-support-real-estate-gold-coast",
     "Trust accounts make agencies a specific target for payment redirection fraud. Plus a mobile workforce, CRM and portal integrations that have to keep working after hours."),
    ("Retail", "/it-support-retail-gold-coast",
     "When the POS is down the shop is closed. Payment terminal segmentation, stock systems and multi-site consistency."),
    ("Restaurants & cafés", "/it-support-restaurants-gold-coast",
     "Thin margins and no tolerance for downtime at service. POS, EFTPOS, online ordering and the network underneath them."),
    ("Hospitality & accommodation", "/it-support-hospitality-gold-coast",
     "Guest WiFi at scale, seasonal staff turnover, booking systems and payment segmentation — a genuinely different problem to an office."),
    ("Trades & field services", "/it-support-trades-gold-coast",
     "The office is a ute. Job management software, quoting on site, patchy connectivity and phones that are the business."),
]

FAQS = [
    ("What industries does bcom ICT work with on the Gold Coast?",
     "bcom ICT supports small and medium businesses across healthcare and allied health, professional services, real estate, retail, restaurants and cafés, hospitality and accommodation, trades and field services, and general small business. On-site support covers the Gold Coast; managed, cloud and cybersecurity services are delivered Australia-wide. Call 07 3041 8993."),
    ("Do you only work with these industries?",
     "No. These are the sectors we see most often on the Gold Coast and where we have the most specific knowledge. If your business isn't listed, the underlying work is much the same — the difference is in what your industry has to comply with and what stops you trading."),
    ("Why does the industry matter for IT support?",
     "Because what breaks the business differs. For a restaurant it's the POS at 7pm. For a health practice it's patient records and Privacy Act obligations that apply regardless of turnover. For a real estate agency it's trust account fraud. Generic IT support treats those the same; they aren't."),
    ("Do you work with businesses outside the Gold Coast?",
     "On-site work is Gold Coast based. Managed IT, cybersecurity, Microsoft 365 and cloud services are delivered remotely to businesses anywhere in Australia."),
]

PAGE = {
    "path": "/industries",
    "priority": "0.8",
    "title": "Industries We Support — Gold Coast Business IT | bcom ICT",
    "description": "IT support for Gold Coast healthcare, professional services, real estate, retail, restaurants, hospitality, trades and small business.",
    "hero_img": "industries-hero.webp",
    "hero_alt": "bcom ICT working with businesses across a range of Gold Coast industries",
    "h1": "What breaks your business isn't what breaks theirs",
    "lede": "A restaurant's IT problem at 7pm is nothing like a health practice's, and neither resembles a real estate agency's. Where the difference actually matters, we know it.",
    "actions": [("Talk to us", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Sector-specific compliance", "Gold Coast on-site", "Australia-wide remote", "Since 2011"],
    "crumbs": [("Industries", "/industries")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT supports small and medium businesses across healthcare and allied health,
    professional services, real estate, retail, restaurants, hospitality, trades and general small business.
    On-site support covers the Gold Coast; managed IT, cybersecurity and cloud services are delivered
    Australia-wide. Call 07 3041 8993.</p>

    <div class="section-head" style="margin-top:64px">
      <span class="eyebrow">Sectors</span>
      <h2>Where we work most</h2>
      <p>Not a list of everyone we'd take money from — these are the sectors where we know what's specifically different.</p>
    </div>
    <div class="grid grid--2">{cards(SECTORS)}</div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why it matters</span>
      <h2>Three things that genuinely differ by industry</h2>
    </div>
    <div class="grid grid--3">{cards([
      ("What stops you trading", None,
       "For a café it's the POS at Friday service. For an agency it's the CRM and the phones. For a practice it's the patient management system. That single answer changes what gets monitored, what gets backed up first, and what counts as a critical fault."),
      ("What you have to comply with", None,
       "Health providers carry Privacy Act obligations regardless of turnover. AFS licensees carry cyber resilience obligations. Anyone taking card payments has PCI-DSS expectations. Generic IT support doesn't know which of those apply to you."),
      ("Who touches your systems", None,
       "High seasonal turnover means account management is a security control, not admin. A mobile workforce means devices leave the building. Both change how access should be handled."),
    ], icon=False)}</div>

    {trust_note('Technicians attending healthcare, education and childcare sites hold national police checks and Queensland Blue Cards where the site requires them — see <a href="/trust-centre">the trust centre</a>.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("All services", "/services"),
  ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
  ("Cybersecurity Services", "/cybersecurity-services-gold-coast"),
  ("Case studies", "/case-studies"),
  ("Published service levels", "/service-levels-and-security"),
  ("Pricing", "/pricing"),
], heading="Related")}

{cta("Not sure your industry is on the list?",
     "The underlying work is much the same — tell us what stops you trading and we'll tell you what we'd do about it.")}
''',
}

"""
bcom ICT — single source of truth for business facts, navigation and footer.

Every page renders from this. If a fact changes, it changes here once.
Confirmed by Royce 2026-08-31.
"""

SITE = "https://www.bcomservices.com"

BIZ = {
    "brand":        "bcom ICT",
    "legal":        "Bcom Services Pty Ltd",
    "abn":          "92 636 893 108",
    "abn_lookup":   "https://abr.business.gov.au/ABN/View?abn=92636893108",
    "founded":      "2011",
    "years":        "15+",
    "phone":        "07 3041 8993",
    "phone_intl":   "+61730418993",
    "phone_href":   "tel:+61730418993",
    "email":        "support@bcomservices.com",
    "street":       "9 Ferny Avenue",
    "suburb":       "Surfers Paradise",
    "state":        "QLD",
    "postcode":     "4217",
    "region":       "Gold Coast",
    "lat":          "-27.9986",
    "lon":          "153.4295",
    "gmaps":        "https://g.page/r/CSc3yhyrbZCaEBM",
    "wikidata":     "https://www.wikidata.org/wiki/Q140075131",
    "rating":       "5.0",
    "reviews":      "24",
    "hours":        "Open 24/7, including weekends and public holidays",
    "callback":     "within 4 business hours",
}

# Suburbs served on-site — used in copy, schema areaServed and the suburb silo.
SUBURBS = [
    "Surfers Paradise", "Southport", "Robina", "Burleigh Heads", "Broadbeach",
    "Coomera", "Nerang", "Helensvale", "Varsity Lakes", "Palm Beach",
    "Main Beach", "Bundall", "Ashmore", "Labrador", "Runaway Bay",
    "Mermaid Beach", "Miami", "Currumbin", "Coolangatta", "Upper Coomera",
    "Pacific Pines", "Oxenford", "Pimpama", "Ormeau", "Paradise Point",
]

# Credentials — all confirmed held by Royce 2026-08-31.
# NOTE: cabler registration number itself still needs to be supplied before
# the registration line goes live on the cabling pages.
CREDENTIALS = {
    "itil":        "ITIL 4 Foundation — Royce Clark",
    "iso42001":    "ISO/IEC 42001:2023 Lead Implementer, issued by BSI — Ollie",
    "cabler":      "ACMA registered cabler",
    "insurance":   "Professional indemnity, cyber liability and public liability insured",
    "screening":   "National police checks and Queensland Blue Cards held by attending technicians",
    "microsoft":   "Microsoft Partner",
}

# Top-level navigation. Deliberately identical to the current site so the
# internal link graph survives the rebuild.
NAV = [
    ("Home",       "/"),
    ("Services",   "/services"),
    ("Industries", "/industries"),
    ("Support",    "/support"),
    ("About",      "/about"),
]

FOOTER = {
    "Services": [
        ("Managed IT Services",   "/managed-it-services-for-small-businesses-gold-coast"),
        ("Business IT Support",   "/it-support-and-services-gold-coast"),
        ("Cybersecurity",         "/cybersecurity-services-gold-coast"),
        ("Business WiFi",         "/business-wifi-gold-coast"),
        ("Phone Systems",         "/business-phone-systems-gold-coast"),
        ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast"),
    ],
    "Trust centre": [
        ("How we work",           "/trust-centre"),
        ("Service levels",        "/service-levels-and-security"),
        ("ISO alignment",         "/iso-alignment"),
        ("Data & sovereignty",    "/data-handling-and-sovereignty"),
        ("Pricing",               "/pricing"),
        ("Reviews",               "/reviews"),
    ],
    "Company": [
        ("About bcom ICT",        "/about"),
        ("Our team",              "/our-team"),
        ("Case studies",          "/case-studies"),
        ("Industries",            "/industries"),
        ("Contact",               "/contact"),
    ],
}


def address_line():
    return f"{BIZ['street']}, {BIZ['suburb']} {BIZ['state']} {BIZ['postcode']}"

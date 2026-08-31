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
    # HOURS — corrected by Royce 2026-08-31. The site previously overstated this.
    # We are open normal business hours. The digital assistant answers the phone
    # around the clock, but phone enquiries are NOT responded to after hours and
    # callbacks are processed in business hours only.
    "hours":        "8:00am – 5:00pm, Monday to Friday (Brisbane time)",
    "hours_short":  "Mon–Fri, 8am–5pm",
    "callback":     "within 4 business hours",
    "after_hours":  "After hours our digital assistant takes your details and we call back the next business day.",
    "on_call":      "After-hours on-call support is available to managed and SLA clients under their agreement.",

    # Online booking for on-site IT support.
    "booking":      "https://calendar.google.com/calendar/appointments/schedules/"
                    "AcZssZ21JsFI48SyH1NJO3oZkyuch15utQ__rWaeHMgfxSppgM_GaVeKRe6Kn0v2oN4XjRgl5D256Up7?gv=true",
    # Remote support tool. Instructions and download link live ONLY on /support.
    "splashtop":    "https://sos.splashtop.com",
}

# Suburbs served on-site — used in copy, schema areaServed and the suburb silo.
SUBURBS = [
    "Surfers Paradise", "Southport", "Robina", "Burleigh Heads", "Broadbeach",
    "Coomera", "Nerang", "Helensvale", "Varsity Lakes", "Palm Beach",
    "Main Beach", "Bundall", "Ashmore", "Labrador", "Runaway Bay",
    "Mermaid Beach", "Miami", "Currumbin", "Coolangatta", "Upper Coomera",
    "Pacific Pines", "Oxenford", "Pimpama", "Ormeau", "Paradise Point",
]

# Suburb pages — the local organic play. Each is written distinctly rather
# than templated; the list drives the cross-link mesh between them.
SUBURB_PAGES = [
    ("Surfers Paradise", "/it-support-surfers-paradise-gold-coast"),
    ("Southport",        "/it-support-southport-gold-coast"),
    ("Broadbeach",       "/it-support-broadbeach-gold-coast"),
    ("Robina",           "/it-support-robina-gold-coast"),
    ("Burleigh Heads",   "/it-support-burleigh-heads-gold-coast"),
    ("Varsity Lakes",    "/it-support-varsity-lakes-gold-coast"),
    ("Palm Beach",       "/it-support-palm-beach-gold-coast"),
    ("Nerang",           "/it-support-nerang-gold-coast"),
    ("Helensvale",       "/it-support-helensvale-gold-coast"),
    ("Coomera",          "/it-support-coomera-gold-coast"),
]

# Credentials — all confirmed held by Royce 2026-08-31.
# NOTE: cabler registration number itself still needs to be supplied before
# the registration line goes live on the cabling pages.
CREDENTIALS = {
    "itil":        "ITIL 4 Foundation — Royce Clark",
    "iso42001":    "ISO/IEC 42001:2023 Lead Implementer, issued by BSI — Ollie",
    # bcom ICT does NOT hold cabler registration. Cabling is subcontracted to
    # ACMA registered cabling contractors. Never write "bcom ICT is ACMA registered".
    "cabler":      "Cabling carried out by ACMA registered cabling contractors",
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


# Published rates. Confirmed by Royce 2026-08-31.
# Business rate is quoted ex-GST because the audience is GST-registered
# businesses; the inc-GST figure is shown alongside it everywhere so the
# number is never ambiguous to a reader.
RATES = {
    "hourly_ex":   198,
    "hourly_inc":  "217.80",
    "callout_ex":  100,
    "callout_inc": 110,
    # First hour on site = call-out + one hour.
    "onsite_first_ex":  298,
    "onsite_first_inc": "327.80",
}


# Contact form endpoint (Formspree). Confirmed working 2026-08-31.
FORM_ENDPOINT = "xreoqepk"


def address_line():
    return f"{BIZ['street']}, {BIZ['suburb']} {BIZ['state']} {BIZ['postcode']}"

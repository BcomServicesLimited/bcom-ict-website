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
    "state":        "QLD",
    "region":       "Gold Coast",
    "gmaps":        "https://g.page/r/CSc3yhyrbZCaEBM",
    "wikidata":     "https://www.wikidata.org/wiki/Q140075131",
    "rating":       "5.0",
    "reviews":      "24",
    # HOURS — corrected by Royce 2026-08-31. The site previously overstated this.
    # We are open normal business hours. The digital assistant answers the phone
    # around the clock, but phone enquiries are NOT responded to after hours and
    # callbacks are processed in business hours only. The 4-hour response target is
    # CONTRACTED and applies ONLY to managed / SLA clients. Everyone else gets a
    # best-effort response — never publish the 4-hour figure as a general promise.
    "hours":        "8:00am – 5:00pm, Monday to Friday (Brisbane time)",
    "hours_short":  "Mon–Fri, 8am–5pm",
    "callback":     "usually the same business day",
    "after_hours":  "After hours our digital assistant takes your details and we call back the next business day.",
    "on_call":      "After-hours on-call support is available to managed and SLA clients under their agreement.",

    # Online booking for on-site IT support.
    # Confirmed by Royce 2026-08-31. The old site carried two scheduling links;
    # this is the on-site booking one (79 pages used it, including the homepage).
    "booking":      "https://calendar.google.com/calendar/appointments/schedules/"
                    "AcZssZ2z99t5yQNIRoRT8rNM3Jv7-WC-MNC35owGsga-okvZmEIG167e9iLOAco3_vHaX44r6eYmGFRA?gv=true",
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
    # Boundaries of the actual service area, not suburb pages.
    "Tweed Heads", "Beenleigh", "Logan",
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

# Credentials — confirmed by Royce 2026-08-31; ITIL attribution corrected
# 2026-09-03: ITIL 4 Foundation is Ollie's, not Royce's.
# NOTE: cabler registration number itself still needs to be supplied before
# the registration line goes live on the cabling pages.
CREDENTIALS = {
    "itil":        "ITIL 4 Foundation — Ollie",
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
    # Comparison pages were reachable only from the service pages they sit under,
    # so nothing collected them. Every page now links the set.
    "Compare": [
        ("Managed IT vs break-fix", "/managed-it-vs-break-fix"),
        ("VoIP vs PBX",             "/voip-vs-pbx-phone-systems"),
        ("Microsoft 365 vs Google", "/microsoft-365-vs-google-workspace"),
        ("UniFi vs Aruba",          "/unifi-vs-aruba-instant-on"),
        ("NAS vs cloud backup",     "/nas-vs-cloud-backup"),
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
    "hourly_ex":   190,
    "hourly_inc":  "209.00",
    "callout_ex":  100,
    "callout_inc": "110.00",
    # Standard first hour on site = call-out + one hour.
    "onsite_first_ex":  290,
    "onsite_first_inc": "319.00",
    # Booking the visit through the online calendar is a fixed price and is
    # genuinely cheaper — $67 inc GST less than the same hour arranged by phone.
    "onsite_online_inc": "252.00",
    "onsite_online_saving_inc": "67.00",
    # Remote work has its own rate for a job of up to an hour, with no call-out.
    "remote_hour_ex":  150,
    "remote_hour_inc": "165.00",
    # After the first hour, time is charged in HALF-hour increments.
    "increment": "half-hour",
}


# Contact form endpoint (Formspree). Confirmed working 2026-08-31.
FORM_ENDPOINT = "xreoqepk"


# Google Business Profile map embed. This is the GBP place entity, not a street
# address — it renders the service area. Whatever GBP shows is what appears here,
# so the listing and the site have to agree about location.
MAP_EMBED = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d451109.88017319166"
             "!2d153.3693615!3d-27.9542216!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1"
             "!3m3!1m2!1s0x2bf15c9da94c225d%3A0x9a906dab1cca3727!2sbcom%20ICT"
             "!5e0!3m2!1sen!2sau!4v1788388814412!5m2!1sen!2sau")


def address_line():
    """Where we work, not a place to visit. bcom ICT attends the customer's
    site — there is no counter for anyone to walk up to, so no street address
    is published anywhere on the site or in the structured data."""
    return f"{BIZ['region']} {BIZ['state']}, Australia"

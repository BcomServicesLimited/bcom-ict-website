from layout import cta, faq_block, related, svc_body

FAQS = [
    ("What does an IT consultant do for a small business?",
     "An IT consultant works out what technology a business actually needs, in what order, and at what cost — independently of who supplies it. bcom ICT provides technology roadmaps, budget planning, vendor selection, system reviews and second opinions for Gold Coast businesses, charged at $198 + GST per hour with no hardware commissions. Call 07 3041 8993."),
    ("Are you independent, or do you sell what you recommend?",
     "We take no commissions from hardware or software vendors, so a recommendation costs us nothing to make honestly. We do implement what we recommend if you want us to — but you can also take the roadmap and have someone else deliver it, and some clients do exactly that."),
    ("We already have an IT provider. Can you still help?",
     "Yes, and second opinions are a legitimate reason to call. Sometimes the answer is that your provider is right and the quote is fair, which is genuinely useful to know. Sometimes it isn't. We'll tell you which without trying to win the account."),
    ("What does a technology roadmap actually contain?",
     "Where your systems are now, what's ageing or coming out of support and when, what your business plans require of your IT over the next few years, and a sequenced list of what to do with rough costs against it. The point is to replace surprise capital expenditure with a budget line."),
    ("How much does IT consulting cost?",
     "$198 + GST per hour ($217.80 inc GST). We scope the piece of work first and tell you roughly how many hours it will take, so you're agreeing to a number rather than an open meter."),
    ("Can you help us decide whether to replace a system?",
     "That's one of the most common things we're asked. We'll look at what the existing system still does well, what it's costing you in workarounds, and what replacement genuinely involves — including the case for keeping it a few more years, which is often the right answer."),
]

PAGE = {
    "path": "/it-consulting-strategy-gold-coast",
    "priority": "0.8",
    "service": "IT Consulting & Strategy Gold Coast",
    "also_service": ["IT Strategy & Technology Roadmaps Gold Coast"],
    "title": "IT Consulting & Strategy Gold Coast — Independent | bcom ICT",
    "description": "Independent IT consulting for Gold Coast businesses — technology roadmaps, budget planning, vendor selection and second opinions. No hardware commissions. $198 + GST per hour.",
    "hero_img": "hero-bg-it-consulting-strategy.webp",
    "hero_alt": "A bcom ICT consultant planning a technology roadmap with a Gold Coast business owner",
    "h1": "Independent advice, with nothing to sell you",
    "lede": "Technology roadmaps, budgets and vendor decisions from a team that takes no commissions — including the advice that you don't need to spend anything yet.",
    "actions": [("Book a conversation", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["No vendor commissions", "$198 + GST/hr", "Second opinions welcome", "Since 2011"],
    "crumbs": [("Services", "/services"), ("IT Consulting & Strategy", "/it-consulting-strategy-gold-coast")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": svc_body(
        answer="bcom ICT provides independent IT consulting to Gold Coast businesses — technology roadmaps, "
               "budget planning, vendor selection, system reviews and second opinions. bcom ICT takes no "
               "commissions from hardware or software vendors, and consulting is charged at $198 + GST per "
               "hour. Call 07 3041 8993.",
        blocks=[
            {"eyebrow": "What we're asked", "h2": "The four questions businesses bring us",
             "sub": "Almost every consulting engagement starts as one of these.", "cols": 2, "icon": False,
             "cards": [
                ("\"Is this quote reasonable?\"", None,
                 "Someone has proposed a system, a migration or a replacement and you have no way to judge it. We read the quote, tell you what it's actually buying, and flag anything missing or padded. Often the cheapest hour you'll spend."),
                ("\"What should we do first?\"", None,
                 "You know several things need attention and can't fund all of them. We assess what would hurt most if it failed, what's cheap to fix, and what can genuinely wait — then sequence it."),
                ("\"Do we replace this or keep it going?\"", None,
                 "A server, a phone system, a fleet of laptops. We look at remaining life, what it's costing you in workarounds, and what replacement actually involves. Keeping it is frequently the right answer."),
                ("\"What will IT cost us over the next three years?\"", None,
                 "Businesses get caught out by capital expenditure nobody saw coming. A roadmap turns that into a budget line — what's coming out of support and when, and roughly what each item costs."),
             ]},
            {"h2": "Why independence matters here",
             "ticks": [
                "<strong>No hardware or software commissions.</strong> A recommendation costs us nothing to make honestly.",
                "<strong>You can take the roadmap elsewhere.</strong> Some clients have us plan and someone else deliver. That's a legitimate outcome and we'll hand over cleanly.",
                "<strong>We'll say when the answer is 'do nothing'.</strong> Or that your current provider is right and the quote is fair.",
                "<strong>We'll say when we're the wrong fit.</strong> Some work needs a specialist or a bigger firm, and it's cheaper for everyone if we say so early.",
             ]},
            {"eyebrow": "How an engagement runs", "h2": "Scoped first, so you're agreeing to a number",
             "cols": 4, "steps": [
                ("A conversation", "Free. What's prompting the question, what's already been proposed, and what's constraining you — usually budget or timing."),
                ("A scope and an estimate", "What we'd look at and roughly how many hours it takes, agreed before we start. Not an open meter."),
                ("The work", "Reviewing systems, reading quotes, talking to your people, checking what's actually in use rather than what's assumed."),
                ("A written recommendation", "Plain English, sequenced, with rough costs. Yours to act on, shop around with, or ignore."),
             ]},
        ]) + faq_block(FAQS) + related([
            ("IT Needs Assessment", "/it-needs-assessment-gold-coast"),
            ("Managed IT Services", "/managed-it-services-for-small-businesses-gold-coast"),
            ("Cloud & Microsoft 365", "/cloud-computing-service-gold-coast"),
            ("Cybersecurity Risk Assessment", "/cybersecurity-health-check-for-small-business-gold-coast"),
            ("How to choose an MSP", "/how-to-choose-an-msp-gold-coast"),
            ("Pricing", "/pricing"),
        ]) + cta("Got a decision you're stuck on?",
                 "The first conversation is free, and it's often enough to tell you whether you need the rest."),
}

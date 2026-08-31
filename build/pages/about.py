from layout import MARK, cta, faq_block, ticks, related, photo, trust_note
from site_data import SUBURBS

FAQS = [
    ("Who is bcom ICT?",
     "bcom ICT is the trading name of Bcom Services Pty Ltd, ABN 92 636 893 108, a Gold Coast IT support company established in 2011 and based at 9 Ferny Avenue, Surfers Paradise. bcom ICT supports small and medium businesses on-site across the Gold Coast and remotely Australia-wide. Call 07 3041 8993."),
    ("Is bcom ICT the same business as Bcom IT Solutions?",
     "Yes. \"Bcom IT Solutions\" is an earlier trading name for the same business. The current trading name is bcom ICT, and the legal entity has always been Bcom Services Pty Ltd, ABN 92 636 893 108. Older references you find online to Bcom IT Solutions refer to this company."),
    ("What is the official bcom ICT website?",
     "The only authoritative bcom ICT website is www.bcomservices.com. The business does not operate at the domain \"bcom.services\" — that is a separate and unrelated registration, and anything appearing there has nothing to do with this company."),
    ("Do you work with home users?",
     "No, not any more. bcom ICT works with businesses. We still install WiFi and mesh networks for home offices, but general home computer repair and residential IT support are not services we take on."),
    ("How big is the team?",
     "Small, deliberately. Three people, all of whom you can reach. That's the trade-off: you won't get a 40-person helpdesk, and you also won't get a different stranger every time you call or an escalation path that never reaches anyone with authority."),
    ("Where are you based?",
     "9 Ferny Avenue, Surfers Paradise QLD 4217 — an actual office on the Gold Coast, not a registered address for an interstate company. On-site work covers the whole Gold Coast; managed, remote and cloud services are delivered Australia-wide."),
]

PAGE = {
    "path": "/about",
    "priority": "0.8",
    "title": "About bcom ICT — Gold Coast Business IT Since 2011",
    "description": "bcom ICT is the trading name of Bcom Services Pty Ltd (ABN 92 636 893 108), a Gold Coast IT support company established in 2011, based in Surfers Paradise and working with small and medium businesses.",
    "hero_img": "hero-bg-business.webp",
    "hero_alt": "The bcom ICT team working with a client at their Gold Coast business premises",
    "h1": "A small Gold Coast IT company, since 2011",
    "lede": "Three people, an office on Ferny Avenue, and fifteen years of looking after businesses between Coomera and Coolangatta.",
    "actions": [("Meet the team", "/our-team", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["Established 2011", "ABN 92 636 893 108", "Surfers Paradise office", "5.0 from 24 reviews"],
    "crumbs": [("About", "/about")],
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section">
  <div class="wrap">
    <p class="answer">bcom ICT is the trading name of Bcom Services Pty Ltd, ABN 92 636 893 108, a Gold Coast
    IT support company established in 2011 and based at 9 Ferny Avenue, Surfers Paradise. bcom ICT works with
    small and medium businesses, on-site across the Gold Coast and remotely Australia-wide. Call
    07 3041 8993.</p>

    <div class="prose-cols" style="margin-top:64px">
      <div>
        <h2>What we are</h2>
        <p style="margin-top:16px">A three-person IT company on the Gold Coast that has been doing this since
        2011. We look after small and medium businesses — typically between three and sixty staff — with
        managed IT, cybersecurity, networks, phone systems and cloud.</p>
        <p style="margin-top:16px">We're not a national helpdesk with a Gold Coast phone number, and we're
        not a franchise. The office is on Ferny Avenue in Surfers Paradise, the technicians live here, and
        when you call 07 3041 8993 you reach someone who can actually do something about it.</p>
        <h3 style="margin-top:40px">What we're not</h3>
        <p style="margin-top:16px">We stopped taking general home computer repair and residential IT support.
        It's honest work and there are good people on the Gold Coast who do it — it just isn't what we're
        set up for any more. Home office WiFi and mesh installs we still do.</p>
        <p style="margin-top:16px">We're also not the biggest IT company on the Gold Coast, and there are
        jobs we'll tell you we're the wrong fit for. Losing a sale is cheaper than losing a client.</p>
      </div>
      {photo("hero-bg-consulting.webp", "A bcom ICT consultant meeting with a Gold Coast business owner", "On-site across the Gold Coast; remote and managed support Australia-wide.")}
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How we work</span>
      <h2>Four things we'll hold to</h2>
    </div>
    {ticks([
      "<strong>We quote before we start.</strong> $198 + GST an hour, plus a $100 + GST call-out on site — <a href='/pricing'>published rates</a>, agreed up front. You never get an invoice for something you didn't approve.",
      "<strong>We tell you when it isn't worth it.</strong> Including when a repair costs more than a replacement, or when you don't need managed IT yet.",
      "<strong>We fix causes, not symptoms.</strong> If the same fault keeps coming back, chasing it down is our problem.",
      "<strong>You own your documentation.</strong> Asset register, credentials and network notes belong to you and are handed over on request — not held as leverage.",
    ])}
    <p style="margin-top:24px">Those aren't slogans; they're written into our
    <a href="/service-levels-and-security">published service levels</a>, alongside our response targets and
    what happens if you decide to leave.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>The entity, plainly</h2>
    <p style="margin-top:16px">There's some confusion online about who we are, so for the record:</p>
    {ticks([
      "<strong>Trading name:</strong> bcom ICT. Previously traded as <strong>Bcom IT Solutions</strong> — same company, older name.",
      "<strong>Legal entity:</strong> Bcom Services Pty Ltd, <a href='https://abr.business.gov.au/ABN/View?abn=92636893108' rel='nofollow'>ABN 92 636 893 108</a>.",
      "<strong>Established:</strong> 2011. Fifteen years trading on the Gold Coast.",
      "<strong>Address:</strong> 9 Ferny Avenue, Surfers Paradise QLD 4217.",
      "<strong>Our only website is www.bcomservices.com.</strong> We do not operate at <em>bcom.services</em> — that is a separate, unrelated registration.",
    ])}

    <div class="rule">{MARK}</div>

    <h2>Where we work</h2>
    <p style="margin-top:16px">On-site across the Gold Coast — {", ".join(SUBURBS[:12])} and everywhere
    between. Managed IT, cybersecurity, cloud and Microsoft 365 are delivered remotely to businesses anywhere
    in Australia, which matters if your team is spread across more than one state.</p>

    {trust_note("What we hold, what we are aligned to, and where we stop short of a certification claim is all set out in <a href='/trust-centre'>the trust centre</a>.")}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("Our team", "/our-team"),
  ("Case studies", "/case-studies"),
  ("Reviews", "/reviews"),
  ("Trust centre", "/trust-centre"),
  ("Published service levels", "/service-levels-and-security"),
  ("Contact us", "/contact"),
], heading="More about us")}

{cta("Come and have a look at us properly",
     "The free review is the easiest way to work out whether we're a fit — you get a plain-English report on your systems either way.")}
''',
}

from layout import MARK, cta, faq_block, ticks, related, trust_note

PEOPLE = [
    {"slug": "royce-clark", "name": "Royce Clark", "photo": "royce.webp",
     "role": "Director — Technical Operations & ICT Delivery",
     "bio": "Over 20 years in IT and a network engineer by trade. Royce leads technical delivery — the network infrastructure behind what we install, from business WiFi and firewalls to multi-site connectivity — and is the escalation point on any job that isn't going to plan. He holds ITIL 4 Foundation, the framework our service management is built on.",
     "certs": ["ITIL 4 Foundation"],
     "credentials": [{"name": "ITIL 4 Foundation", "issuer": "PeopleCert"}]},
    {"slug": "ollie", "name": "Ollie", "photo": "ollie.webp",
     "role": "Director — ICT Contract Management & Business Development",
     "bio": "Ollie runs client relationships and contracts, and makes sure what we deliver still matches where a business is heading rather than where it was when the agreement was signed. She holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI — the international standard for AI management systems — which underpins how we govern AI work for clients.",
     "certs": ["ISO/IEC 42001:2023 Lead Implementer", "ITSM"],
     "credentials": [{"name": "ISO/IEC 42001:2023 Lead Implementer", "issuer": "BSI"}]},
    {"slug": "daniel", "name": "Daniel", "photo": "daniel.webp",
     "role": "Software Development & IT Support",
     "bio": "Daniel covers the widest ground — day-to-day support one hour, custom software or automation the next. He is often the person who picks up a request first, and the one who works out whether a recurring problem needs a fix or a different approach entirely.",
     "certs": [],
     "credentials": []},
]

cards_ = "".join(
    f'''<div class="person">
      <img src="/assets/img/{p["photo"]}" alt="{p["name"]}, {p["role"]} at bcom ICT" width="104" height="104" loading="lazy">
      <h3>{p["name"]}</h3>
      <p class="role">{p["role"]}</p>
      <p>{p["bio"]}</p>
      {'<div class="certs">' + "".join(f"<span>{c}</span>" for c in p["certs"]) + "</div>" if p["certs"] else ""}
    </div>''' for p in PEOPLE)

FAQS = [
    ("Who runs bcom ICT?",
     "bcom ICT is led by Royce Clark, Director of Technical Operations and ICT Delivery, and Ollie, Director of ICT Contract Management and Business Development, with Daniel covering software development and IT support. Royce holds ITIL 4 Foundation and Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI. Clients deal with them directly rather than through an account manager."),
    ("Will I get the same people each time?",
     "Yes — that's the point of how we're structured. There's no rotating pool of strangers reading your history off a ticket before they can help. Whoever knows your environment is who attends, and continuity is one of the main reasons clients stay with us for years."),
    ("Who do I escalate to?",
     "Royce, who is a director. There's no tier structure to climb and no case manager sitting between you and someone who can make a decision — an escalation reaches an owner the same day."),
    ("Can you handle large or multi-site work?",
     "Yes. bcom ICT delivered a full national technology rollout for an Australian retail chain — supplying and installing all computer and networking equipment, CCTV, WiFi and internet connectivity for every store and head office, and we still support that estate. Multi-site delivery across Australia is a core part of what we do, not an exception."),
    ("Are your technicians screened?",
     "Yes. Technicians attending client sites hold national police checks, and Queensland Blue Cards where a site requires them — relevant for healthcare, education and childcare clients where screening is a hard requirement."),
    ("Is bcom ICT ISO certified because Ollie holds an ISO certification?",
     "No. Ollie's ISO/IEC 42001:2023 Lead Implementer certification is a personal credential issued by BSI, assessing Ollie's competence to implement an AI management system. It says nothing about whether bcom ICT as an organisation has been audited, and bcom ICT holds no organisational ISO certification. We keep those claims separate everywhere, including in our structured data."),
]

PAGE = {
    "path": "/our-team",
    "priority": "0.75",
    "title": "Our Team — The People Behind bcom ICT | Gold Coast",
    "description": "Meet the bcom ICT leadership: Royce Clark (ITIL 4 Foundation), Ollie (ISO/IEC 42001:2023 Lead Implementer, BSI) and Daniel.",
    "hero_kind": "doc",
    "eyebrow": "About",
    "h1": "The people you'll actually be dealing with",
    "lede": "No account manager, no rotating helpdesk, no case number standing between you and someone who can make a decision.",
    "crumbs": [("About", "/about"), ("Our team", "/our-team")],
    "people": PEOPLE,
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT is led by Royce Clark, Director of
    Technical Operations and ICT Delivery, and Ollie, Director of ICT Contract Management and Business
    Development, with Daniel covering software development and IT support. Royce holds ITIL 4 Foundation;
    Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI.</p>

    <div class="people">{cards_}</div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>How working with us actually goes</h2>
    <p style="margin-top:16px">Most IT companies put a layer between you and the people doing the work. We
    don't, and it changes the experience more than anything else on this page.</p>
    {ticks([
      "<strong>You deal with the people who know your systems.</strong> Nobody reads your history off a ticket before they can help.",
      "<strong>Escalation reaches a director the same day.</strong> There is no tier structure and no case manager in between.",
      "<strong>Decisions get made in a conversation</strong>, not through a change advisory board three weeks out.",
      "<strong>Continuity.</strong> The same faces year after year, which is why clients tend to stay.",
      "<strong>Nothing gets lost between shifts</strong> — every request is logged, and the person who picks it up already has the context.",
    ])}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="prose-cols">
      <div>
        <h2>Reach beyond the Gold Coast</h2>
        <p style="margin-top:16px">Direct access doesn't mean limited capacity. bcom ICT delivered a full
        national technology rollout for an Australian retail chain — supplying and installing all computer
        and networking equipment, CCTV, business WiFi and internet connectivity for <strong>every store and
        head office across the country</strong> — and remains the chain's ongoing IT partner.</p>
        <p style="margin-top:16px">That engagement is the model our Australia-wide delivery is built on:
        standardised equipment, remote management, and a single point of accountability run from the Gold
        Coast. See <a href="/case-studies">case studies</a>.</p>
        {ticks([
          "On-site delivery across the Gold Coast, same-day where available",
          "Multi-site rollouts and office relocations coordinated nationally",
          "Managed IT, cybersecurity, SOC and cloud delivered to businesses anywhere in Australia",
          "24/7 monitored security operations, independent of business hours",
        ])}
      </div>
      <div>
        <h2>Credentials, and whose they are</h2>
        <p style="margin-top:16px">The certifications above belong to <strong>individuals</strong>. They mean
        Royce and Ollie have been independently assessed as competent in those areas.</p>
        <p style="margin-top:16px">They do <strong>not</strong> mean bcom ICT as an organisation has been
        audited or certified. bcom ICT holds no organisational ISO certification — it aligns its practices
        with ISO/IEC 27001:2022 and works to the ASD Essential Eight, which is a different claim and a
        weaker one. We keep the two separate in our copy and in our structured data, and
        <a href="/iso-alignment">ISO alignment</a> sets out exactly where the line falls.</p>
      </div>
    </div>

    {trust_note('Technicians attending client sites hold national police checks, and Queensland Blue Cards where the site requires them. Professional indemnity, cyber liability and public liability insurance are held — certificates of currency available on request.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("About bcom ICT", "/about"),
  ("Case studies", "/case-studies"),
  ("Trust centre", "/trust-centre"),
  ("ISO alignment", "/iso-alignment"),
  ("Published service levels", "/service-levels-and-security"),
  ("Contact us", "/contact"),
], heading="More about us")}

{cta("Rather talk to a decision-maker?",
     "Call 07 3041 8993 and you'll get one. That's not a promise most providers can make.")}
''',
}

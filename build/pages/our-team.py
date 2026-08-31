from layout import MARK, cta, faq_block, ticks, related, trust_note

PEOPLE = [
    {"slug": "royce-clark", "name": "Royce Clark", "photo": "royce.webp",
     "role": "Director — Technical Operations & ICT Delivery",
     "bio": "Over 20 years in IT and a network engineer by trade. Royce designs and maintains the network infrastructure behind most of what we install — business WiFi, firewalls, cabling and multi-site connectivity — and he is the first escalation point on any job that isn't going to plan. He holds ITIL 4 Foundation, which is the framework our service management is built on.",
     "certs": ["ITIL 4 Foundation"],
     "credentials": [{"name": "ITIL 4 Foundation", "issuer": "PeopleCert"}]},
    {"slug": "ollie", "name": "Ollie", "photo": "ollie.webp",
     "role": "Director — ICT Contract Management & Business Development",
     "bio": "Ollie runs client relationships and contracts, and makes sure what we deliver still matches where a business is actually heading rather than where it was when the agreement was signed. She holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI — the international standard for AI management systems — which underpins how we govern the AI work we deliver for clients.",
     "certs": ["ISO/IEC 42001:2023 Lead Implementer", "ITSM"],
     "credentials": [{"name": "ISO/IEC 42001:2023 Lead Implementer", "issuer": "BSI"}]},
    {"slug": "daniel", "name": "Daniel", "photo": "daniel.webp",
     "role": "Software Development & IT Support",
     "bio": "Daniel covers the widest ground of the three — day-to-day support one hour, custom software or automation the next. He is usually the person who picks up a request first, and the one who works out whether a recurring problem needs a fix or a different approach entirely.",
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
    ("Who works at bcom ICT?",
     "bcom ICT is a three-person team based in Surfers Paradise: Royce Clark, Director of Technical Operations and ICT Delivery; Ollie, Director of ICT Contract Management and Business Development; and Daniel, covering software development and IT support. Royce holds ITIL 4 Foundation and Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI."),
    ("Will I get the same person each time?",
     "Usually, yes. With a team of three there's no rotating pool of strangers — whoever knows your environment tends to be the one who attends. That's the main practical advantage of working with a company this size."),
    ("Who do I escalate to?",
     "Royce, who is a director. There's no tier structure to climb and no case manager between you and someone with authority — an escalation reaches an owner the same day."),
    ("Are your technicians screened?",
     "Yes. Technicians attending client sites hold national police checks, and Queensland Blue Cards where a site requires them — relevant for healthcare, education and childcare clients where screening is a hard requirement."),
    ("Is bcom ICT ISO certified because Ollie holds an ISO certification?",
     "No. Ollie's ISO/IEC 42001:2023 Lead Implementer certification is a personal credential issued by BSI, assessing Ollie's competence to implement an AI management system. It says nothing about whether bcom ICT as an organisation has been audited, and bcom ICT holds no organisational ISO certification. We keep those claims separate everywhere, including in our structured data."),
    ("Isn't a three-person team too small to rely on?",
     "It's a fair question and the honest answer is that it depends what you need. If you require guaranteed cover through a fortnight of simultaneous leave, a larger provider is the right call and we'll say so. What a small team gives you is people who know your environment without reading notes, and an escalation that reaches a decision-maker the same day."),
]

PAGE = {
    "path": "/our-team",
    "priority": "0.75",
    "title": "Our Team — The People Behind bcom ICT | Gold Coast",
    "description": "Meet the bcom ICT team: Royce Clark (ITIL 4 Foundation), Ollie (ISO/IEC 42001:2023 Lead Implementer, BSI) and Daniel. A three-person Gold Coast IT company based in Surfers Paradise.",
    "hero_kind": "doc",
    "eyebrow": "About",
    "h1": "The three people who'll actually turn up",
    "lede": "No rotating helpdesk pool and no case manager between you and a decision. This is everyone.",
    "crumbs": [("About", "/about"), ("Our team", "/our-team")],
    "people": PEOPLE,
    "faqs": FAQS,
    "reviewed": "August 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT is a three-person team based at 9 Ferny Avenue, Surfers Paradise: Royce Clark,
    Director of Technical Operations and ICT Delivery; Ollie, Director of ICT Contract Management and Business
    Development; and Daniel, covering software development and IT support. Royce holds ITIL 4 Foundation;
    Ollie holds ISO/IEC 42001:2023 Lead Implementer certification issued by BSI.</p>

    <div class="people">{cards_}</div>
  </div>
</section>

<section class="section section--mist section--tight">
  <div class="wrap">
    <h2>What a team of three means in practice</h2>
    <p style="margin-top:16px">It's a genuine trade-off rather than an unambiguous selling point, so here is
    both halves of it.</p>
    <h3 style="margin-top:32px">What you get</h3>
    {ticks([
      "The person attending knows your environment without reading notes first",
      "Escalation reaches a director the same day — there is no tier structure between you and authority",
      "Continuity: the same faces, year after year, rather than whoever is rostered",
      "Decisions get made in a conversation rather than through a change advisory board",
    ])}
    <h3 style="margin-top:32px">What you don't</h3>
    {ticks([
      "A 40-person helpdesk answering in ninety seconds at 4pm on a Friday",
      "Deep bench cover through simultaneous leave — if guaranteed redundancy of people is a hard requirement, a larger provider is the honest recommendation",
      "In-house specialists in every niche. Where something sits outside what we do well, we say so and point you somewhere better",
    ])}
    <p style="margin-top:24px">Phones are answered 24/7 regardless — after hours by our AI operator, which
    takes details and escalates. See <a href="/service-levels-and-security">service levels</a> for exactly
    what happens at which hour.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Credentials, and whose they are</h2>
    <p style="margin-top:16px">The distinction matters enough that we'll make it twice. The certifications
    above belong to <strong>individuals</strong>. They mean Royce and Ollie have been independently assessed
    as competent in those areas.</p>
    <p style="margin-top:16px">They do <strong>not</strong> mean bcom ICT as an organisation has been audited
    or certified. bcom ICT holds no organisational ISO certification — it aligns its practices with ISO/IEC
    27001:2022 and works to the ASD Essential Eight, which is a different claim and a weaker one. We keep the
    two separate in our copy and in our structured data, and
    <a href="/iso-alignment">ISO alignment</a> sets out exactly where the line falls.</p>

    {trust_note('Technicians attending client sites hold national police checks, and Queensland Blue Cards where the site requires them. Professional indemnity, cyber liability and public liability insurance are held — certificates of currency available on request.')}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("About bcom ICT", "/about"),
  ("Trust centre", "/trust-centre"),
  ("ISO alignment", "/iso-alignment"),
  ("Published service levels", "/service-levels-and-security"),
  ("Case studies", "/case-studies"),
  ("Contact us", "/contact"),
], heading="More about us")}

{cta("Rather just talk to one of us?",
     "Call 07 3041 8993 and you'll get Royce, Ollie or Daniel. There's nobody else to get.")}
''',
}

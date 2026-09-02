from layout import MARK, cta, faq_block, cards, ticks, related, trust_note, issues, models, example

MODELS = [
    ("Desktop units", "What most Gold Coast small businesses run — file storage, backup target, and somewhere the design or project archive can live without filling a server.",
     ["DS224+", "DS423+", "DS723+", "DS923+", "DS1522+"]),
    ("Rack mounted", "For a business with a comms cabinet and enough data that a desktop unit stops making sense.",
     ["RS422+", "RS822+", "RS1221+"]),
    ("The software is the point", "DSM is why people choose Synology over a cheaper box. Active Backup for Business backs up PCs, servers and Microsoft 365 at no extra licence cost.",
     ["DSM", "Active Backup for Business", "Snapshot Replication", "Hyper Backup"]),
]

ISSUES = [
    ("&ldquo;We back up to the NAS, so we are covered&rdquo;",
     "a unit mapped as a drive letter on the same network with the same credentials. Ransomware that reaches a workstation reaches the backup too.",
     "Turn on immutable snapshots so a copy exists that encryption cannot overwrite, and add an offsite copy with Hyper Backup. A share you can open from a desk is storage, not backup."),
    ("&ldquo;We have not checked it in years&rdquo;",
     "a box in a cupboard doing its job silently, with a drive that failed eighteen months ago and an amber light nobody walks past.",
     "Set up notifications that actually reach someone, and check the drive health. A degraded array is fine until the second drive goes, and then it is not."),
    ("&ldquo;It is full&rdquo;",
     "capacity planned for the business three years ago. Design files, video and photo archives grow faster than anyone forecasts.",
     "Expand rather than replace where the unit allows it, and work out what should be on the NAS at all &mdash; a lot of what fills them is archive that belongs somewhere cheaper."),
    ("&ldquo;Every share is open to every staff member&rdquo;",
     "shares created quickly at setup with permissions nobody revisited, which is the same problem Microsoft 365 tenancies have.",
     "Set permissions by group against how the business actually works. It is an hour of work that answers a question a client or an insurer will eventually ask."),
    ("&ldquo;We back up to it but not off it&rdquo;",
     "a single copy in the same building as the originals. It survives a drive failure and not a fire, a theft or a flood.",
     "Add an offsite copy. Hyper Backup handles it, and the local copy stays for fast restores &mdash; see the comparison of NAS against cloud backup."),
    ("&ldquo;It is reachable from the internet&rdquo;",
     "QuickConnect or a port forward opened so someone could get files from home, still open and still indexed.",
     "Put it behind a VPN. Internet-exposed NAS units are actively scanned for and have been the entry point in real incidents."),
]

EXAMPLE_1 = example(
    "The drive that had been amber for eighteen months",
    "A design business kept its entire project archive on a Synology in the office cupboard. It had been installed by a previous provider, it had never given any trouble, and nobody had opened the interface since the day it went in.",
    "One drive in the array had failed roughly eighteen months earlier. The unit had done exactly what it was designed to do &mdash; carried on running in a degraded state on the remaining drives &mdash; and had been sending notifications to an email address belonging to the provider who installed it. A second drive failure at any point in those eighteen months would have taken the archive with it. Separately, nothing on the unit had ever left the building, and Microsoft 365 was not being backed up at all despite Active Backup for Business being available on the box and already paid for.",
    "Replaced the failed drive and rebuilt the array, then set notifications to reach two people at the business rather than a departed supplier. Enabled immutable snapshots, configured an offsite copy with Hyper Backup, and turned on Active Backup for Business against the Microsoft 365 tenancy and the workstations.",
    "The archive is protected against a second drive failure, against fire and theft, and against ransomware overwriting the snapshots. Every one of those capabilities was already on the unit and already paid for. The only thing missing had been somebody opening it.")
FAQS = [
    ("Is a Synology NAS a backup?",
     "Only if it is configured to be one. A NAS mapped as a drive on the same network with the same credentials is storage — ransomware that reaches a workstation reaches it too, and we have recovered from an incident where the backup unit was encrypted alongside the server it was protecting. Immutable snapshots and an offsite copy are what turn a NAS into a backup."),
    ("Which Synology model suits a small business?",
     "For most Gold Coast small businesses the desktop plus range — DS224+ through DS923+ — covers it, and the deciding factors are how much data you hold, how fast it is growing, and whether you want to run Active Backup for Business against servers and workstations. Rack units make sense once there is a comms cabinet and the data has outgrown a desktop box."),
    ("Synology or QNAP?",
     "Both are capable and the hardware is comparable. Synology's advantage is DSM and Active Backup for Business, which backs up PCs, servers and Microsoft 365 without an additional licence — for most small businesses that is the deciding factor. QNAP often gives more hardware for the money and suits a business that wants raw capability or specific virtualisation features. We support both; we deploy Synology more often for the software."),
    ("Can a Synology back up Microsoft 365?",
     "Yes, through Active Backup for Business, and it is one of the strongest reasons to have one. Microsoft replicates your data for their availability but does not keep a copy against deletion, a departing staff member, or ransomware syncing through OneDrive. Almost no business has this until someone explains it."),
    ("Should our NAS be accessible from the internet?",
     "Not directly. Put it behind a VPN rather than exposing it through a port forward or QuickConnect. Internet-facing NAS units are actively scanned for, and they have been the entry point in real ransomware incidents in Australia."),
    ("Can you take over a NAS someone else set up?",
     "Yes. We recover administrative access, review the share permissions and the backup jobs against what the business actually needs, check drive health, and set up notifications that reach a person. Inherited units are where we most often find a failed drive nobody knew about."),
]

PAGE = {
    "path": "/synology-nas-gold-coast",
    "priority": "0.8",
    "service": "Synology NAS Setup & Support Gold Coast",
    "title": "Synology NAS Setup & Support Gold Coast | bcom ICT",
    "description": "Synology NAS supply, setup and support for Gold Coast businesses — DSM, Active Backup for Business, immutable snapshots. Call 07 3041 8993.",
    "hero_img": "synology-hero.webp",
    "hero_alt": "Business network storage and backup equipment in a Gold Coast office",
    "eyebrow": "Storage & backup",
    "h1": "A NAS is storage. Configured properly, it becomes a backup.",
    "lede": "The difference is snapshots that ransomware cannot overwrite and a copy that leaves the building. Most of the units we inherit have neither.",
    "actions": [("Get a backup review", "/contact", "white"), ("Call 07 3041 8993", "tel:+61730418993", "onink")],
    "trust": ["DSM & Active Backup", "Immutable snapshots", "Offsite copies", "Restores tested"],
    "crumbs": [("Services", "/services"), ("Synology NAS", "/synology-nas-gold-coast")],
    "faqs": FAQS,
    "reviewed": "September 2026",
    "body": f'''
<section class="section section--tight">
  <div class="wrap">
    <p class="answer">bcom ICT supplies, configures and supports Synology NAS units for Gold Coast businesses —
    DSM setup, Active Backup for Business against workstations, servers and Microsoft 365, immutable snapshots,
    offsite copies with Hyper Backup, share permissions and drive health monitoring. We support QNAP as well.
    Call 07 3041 8993.</p>

    <h2 style="margin-top:56px">The sentence that costs businesses everything</h2>
    <p style="margin-top:16px">&ldquo;The NAS is our backup.&rdquo;</p>
    <p style="margin-top:16px">It usually is not. A NAS mapped as a drive letter, on the same network, reachable
    with the same credentials, is a second copy of your data sitting in the blast radius of the first. Ransomware
    that reaches a workstation reaches it too. We have recovered a business whose backup unit was encrypted
    alongside the server it was protecting, because it was permanently mapped with the server&rsquo;s own
    administrator credentials.</p>
    <p style="margin-top:16px">What turns a Synology into an actual backup is two settings and one habit:
    <strong>immutable snapshots</strong> so a version exists that encryption cannot overwrite, <strong>an
    offsite copy</strong> so fire and theft are covered, and <strong>a restore somebody has actually
    tested</strong>. None of them costs anything extra. Almost none of the units we inherit have all three.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Models</span>
      <h2>The units we work on</h2>
    </div>
    {models(MODELS)}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2>Why Synology rather than a cheaper box</h2>
    <p style="margin-top:16px">The hardware is unremarkable and that is fine &mdash; you are buying DSM. In
    particular you are buying <strong>Active Backup for Business</strong>, which backs up Windows machines,
    servers and your Microsoft 365 tenancy with no additional licence.</p>
    <p style="margin-top:16px">That last one matters more than most businesses realise. Microsoft replicates
    your data for their own availability; they do not keep a copy against you deleting something, a staff
    member leaving with a mailbox, or ransomware syncing through OneDrive. A Synology sitting in the cupboard
    covers that for the price of the box.</p>
    <p style="margin-top:16px"><strong>QNAP</strong> is a capable alternative and we support it. It frequently
    offers more hardware for the money. We deploy Synology more often because for a small business the software
    is the deciding factor, not the specification.</p>
  </div>
</section>

<section class="section section--tight section--mist">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common problems</span>
      <h2>What we find on an inherited NAS</h2>
    </div>
    {issues(ISSUES)}

    {trust_note('A local copy is for speed and an offsite copy is for survival &mdash; they cover different failures and most businesses need both. See <a href="/nas-vs-cloud-backup">NAS vs cloud backup</a> for how to decide, and <a href="/data-backup-recovery-gold-coast">backup and disaster recovery</a> for the service.')}
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">In practice</span>
      <h2>What we find on a NAS nobody has opened</h2>
      <p>A representative engagement, drawn from real work with client and staff names removed.</p>
    </div>
    {EXAMPLE_1}
  </div>
</section>

{faq_block(FAQS)}

{related([
  ("NAS vs cloud backup", "/nas-vs-cloud-backup"),
  ("Data Backup & Disaster Recovery", "/data-backup-recovery-gold-coast"),
  ("Microsoft 365 Setup & Support", "/microsoft-365-setup-gold-coast"),
  ("Cyber Incident Response", "/cyber-incident-response-gold-coast"),
  ("Hardware Procurement & Setup", "/hardware-procurement-setup-gold-coast"),
], heading="Related")}

{cta("Got a NAS in the cupboard?",
     "We will check whether it is a backup or just a second copy. Snapshots, an offsite copy and a tested restore are the difference, and none of them costs extra.")}
''',
}

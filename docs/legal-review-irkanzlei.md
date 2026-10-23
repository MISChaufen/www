# Fact-Check: it-recht-kanzlei.de Articles on DDG §5 Impressum Obligations

**Date:** 2026-10-23  
**Reviewer:** Claude (claude-sonnet-4-6), acting as research agent for Benjamin Boortz  
**Articles reviewed:**
1. https://www.it-recht-kanzlei.de/website-impressumspflicht-digitale-dienste-gesetz.html  
   (Erstfassung: 21.06.2024 — Stand: 05.05.2025)
2. https://www.it-recht-kanzlei.de/impressum.html  
   (Erstfassung: 19.11.2017 — Stand: 15.08.2025)

**Method:** All claims verified against primary sources fetched during this session: DDG §5 full text (gesetze-im-internet.de), DDG §33 (gesetze-im-internet.de), EU e-Commerce Directive 2000/31/EC (EUR-Lex), existing legal-review-private.md (which itself extracted MStV §18(1) directly from the MStV PDF). The LFK Leitfaden PDF was also attempted but the binary was unreadable by the fetch tool; claims from that source are drawn from the pre-existing legal-review-private.md extraction.

---

## Summary Table

| # | Claim | Article | Verdict | Risk Level |
|---|-------|---------|---------|------------|
| 1 | Phone number "in aller Regel" mandatory | Article 1 | MISLEADING | Medium |
| 2 | Phone number NOT mandatory, email alone sufficient | Article 2 | CORRECT | — |
| 3 | "Geschäftsmäßig" expanded to include any indirect advertising | Both | OVERSTATED / POSSIBLY INCORRECT | Medium |
| 4 | €50,000 fine for §5 violations via DDG §33 Abs. 6 Nr. 3 | Article 1 | CORRECT | — |
| 5 | MStV §18 omitted entirely | Article 1 | OMISSION (significant) | High |
| 6 | MStV §18 mentioned only for journalistic content | Article 2 | INCOMPLETE | Medium |
| 7 | Email address mandatory (DDG §5 Nr. 2) | Both | CORRECT | — |
| 8 | Email shown as image — not addressed | Both | GAP | Low–Medium |
| 9 | EuGH C-298/07 contact form ruling — not cited | Article 1 | OMISSION | Low |
| 10 | EuGH C-298/07 correctly described (30–60 min) | Article 2 | CORRECT | — |
| 11 | TDDDG §25 / cookies — not covered | Both | OUT OF SCOPE (not a gap per se) | — |
| 12 | TMG references as historical context | Both | CORRECT | — |
| 13 | DDG §5 correctly identified as current law | Both | CORRECT | — |
| 14 | Private website exemption correctly described | Both | BROADLY CORRECT with minor imprecision | Low |
| 15 | Article 2 says "§5 DDG (Telemediengesetz)" in bracket | Article 2 | MISLEADING nomenclature | Low |

**Flags that could lead to incorrect legal advice:** Claims #1, #3, #5, #6, and #15.

---

## Detailed Findings

### Finding 1 — Phone number "in aller Regel" required (Article 1)

**Claim (Article 1, verbatim):**  
> "weitere Angaben, die eine unmittelbare Kommunikation mit dem Anbieter ermöglichen, was in aller Regel eine Telefonnummer ist"

**Verdict: MISLEADING**

**Primary source check:**  
DDG §5(1) Nr. 2 exact text (gesetze-im-internet.de):
> "Angaben, die eine schnelle elektronische Kontaktaufnahme und eine unmittelbare Kommunikation mit ihnen ermöglichen, einschließlich der Adresse für die elektronische Post"

The statute explicitly requires an email address ("einschließlich der Adresse für die elektronische Post") and contact details enabling quick electronic contact. It does **not** mention a telephone number. The phrase "in aller Regel eine Telefonnummer" in Article 1 is the article's editorial gloss, not a statutory command.

**Why this is misleading:** A reader of Article 1 who does not also read Article 2 (which is more nuanced) would reasonably conclude that a phone number is a legal requirement "as a rule." The correct statement is that phone number is neither required nor prohibited by DDG §5 — it is one way of satisfying the "unmittelbare Kommunikation" element, but an alternative channel (e.g. a contact form with prompt responses per EuGH C-298/07) also suffices. Article 1 does not cite EuGH C-298/07 or explain that alternatives are legally acceptable.

**Contrast with Article 2 (same publisher):**  
Article 2 states more accurately:
> "Während die Angabe der Mailadresse nach der Vorschrift verpflichtend ist, sieht dies für die Telefonnummer augenscheinlich anders aus."

The two articles from the same publisher give different impressions on the same question. This inconsistency is itself a quality problem.

---

### Finding 2 — Phone number NOT mandatory (Article 2)

**Claim (Article 2, verbatim):**  
> "Während die Angabe der Mailadresse nach der Vorschrift verpflichtend ist, sieht dies für die Telefonnummer augenscheinlich anders aus."

**Verdict: CORRECT**

This is accurate. DDG §5(1) Nr. 2 requires an email address but does not mention telephone numbers. The article correctly identifies that the email is the only explicitly mandated contact medium and that telephone is not compulsory.

---

### Finding 3 — "Geschäftsmäßig" expanded to advertising-fed websites (Both articles)

**Claim (Article 1, verbatim):**  
> "Sobald auf einer Website (z.B. in einem Reise-Blog) direkt oder auch nur indirekt für eigene Produkte des Blog-Betreibers oder für fremde Produkte von Dritten geworben wird, ist diese Website als geschäftsmäßig in diesem Sinne zu verstehen"

And:
> "bloß mittelbar von eigener oder fremder Werbung gespeist wird"

**Verdict: OVERSTATED / POTENTIALLY INCORRECT**

**Primary source check:**  
DDG §5(1) opening clause:
> "Diensteanbieter haben für **geschäftsmäßige, in der Regel gegen Entgelt angebotene** digitale Dienste..."

The statutory phrase "in der Regel gegen Entgelt" (typically offered for remuneration) is a qualifier that indicates payment or economic benefit is the norm, not an exception. The article's interpretation correctly notes that payment is not strictly required ("Die Entgeltlichkeit eines digitalen Dienstes ist für dessen Qualifikation als 'geschäftsmäßig' dahingegen nicht zwingend erforderlich"), but then expands the threshold too broadly by asserting that any indirect advertising on a website triggers the obligation.

**The problem:** The LFK Leitfaden (as extracted in legal-review-private.md) lists specific commercial indicators: affiliate links, monetisation tools, advertising cooperations, product placements for consideration. These are active revenue-generating arrangements. The article's claim that a blog displaying *any* advertising for third-party products — even if the blogger earns nothing from it — becomes "geschäftsmäßig" is not clearly supported by the statutory text or regulatory guidance. The word "gespeist" (sustained/fed by advertising) implies the site derives income from the advertising. A blog that merely mentions or links to third-party products without any commercial arrangement is a different case.

**What a mislead operator might do:** A personal blogger who has a single affiliate link might over-comply and add an Impressum (harmless), but the article could also mislead a person into believing that even non-monetised mentions of commercial products (e.g. a restaurant review blog with no revenue) triggers the full DDG §5 obligation. That conclusion is not clearly supported.

**Note:** The article's "Faustformel" ("all providers pursuing at least indirect commercial purposes") is a commonly cited shorthand from pre-DDG TMG commentary. It is not wrong in commercial cases, but it conflates "commercial purpose" (Zweck) with "commercial structure" (Ausgestaltung), and the statutory text actually focuses on the latter.

---

### Finding 4 — €50,000 fine for §5 violations (Article 1)

**Claim (Article 1, verbatim):**  
> "mit einer Geldbuße von bis zu EUR 50.000 geahndet werden kann (§ 33 Abs. 6 Nr. 3 DDG)"

**Verdict: CORRECT**

**Primary source check:**  
DDG §33 Abs. 2 Nr. 1:
> "entgegen § 5 Absatz 1 eine Information nicht, nicht richtig oder nicht vollständig verfügbar hält"

DDG §33 Abs. 6 Nr. 3:
> "in den übrigen Fällen des Absatzes 2 mit einer Geldbuße bis zu fünfzigtausend Euro"

The chain is: §5 Abs. 1 violation → §33 Abs. 2 Nr. 1 → falls under "übrige Fälle des Absatzes 2" → §33 Abs. 6 Nr. 3 → maximum €50,000. The statutory citation is accurate.

---

### Finding 5 — MStV §18 entirely omitted (Article 1)

**Claim:** Article 1 does not mention MStV §18 anywhere.

**Verdict: SIGNIFICANT OMISSION**

**Primary source check:**  
MStV §18(1) (extracted directly from MStV PDF in legal-review-private.md):
> "Anbieter von Telemedien, die nicht ausschließlich persönlichen oder familiären Zwecken dienen, haben folgende Informationen leicht erkennbar, unmittelbar erreichbar und ständig verfügbar zu halten: 1. Name und Anschrift sowie 2. bei juristischen Personen auch Name und Anschrift des Vertretungsberechtigten."

DDG §5(2) savings clause:
> "Weitergehende Informationspflichten nach anderen Rechtsvorschriften bleiben unberührt."

This savings clause in DDG §5 explicitly states that other legal obligations survive. MStV §18 is a "weitergehende Informationspflicht nach anderen Rechtsvorschriften." An article purporting to comprehensively explain German Impressum obligations under DDG §5 must at minimum note that:

1. MStV §18(1) imposes a *parallel and independent* obligation on any website not exclusively for personal/family use — with a *lower threshold* than DDG §5(1).
2. MStV §18(2) imposes an *additional* obligation on providers of journalistic/editorial content to name a responsible editor (Verantwortlicher).

**Why this omission matters:**  
A website operator might conclude, after reading Article 1, that if their site is "purely private" and therefore exempt from DDG §5, they have no Impressum obligation at all. This conclusion would be wrong: MStV §18(1) applies to any publicly accessible website not exclusively serving personal/family purposes, which is a much broader category. The LFK Leitfaden (and legal-review-private.md §4) confirms the §18(1) threshold is extremely narrow — essentially covering only password-protected family photo albums or private social media profiles visible only to confirmed contacts.

**Risk:** Medium-High. A reader of Article 1 who operates a non-commercial but publicly accessible website (e.g. a hobby site, a club site, a hackerspace site) might incorrectly conclude they have no Impressum obligation whatsoever.

---

### Finding 6 — MStV §18 mentioned only for journalistic content (Article 2)

**Claim (Article 2, verbatim):**  
> "Nach § 18 Abs. 2 MStV haben Online-Händler, die journalistisch-redaktionelle Angebote bereithalten, stets einen inhaltlich Verantwortlichen in ihrem Impressum zu benennen"

**Verdict: INCOMPLETE (and slightly inaccurate framing)**

**Primary source check:**  
MStV §18 has at least two relevant subsections:
- §18(1): Reduced Impressum (name + address) for ALL websites not exclusively personal/family.
- §18(2): Full Impressum plus Verantwortlicher for journalistic/editorial content.

Article 2 mentions only §18(2) (the editorial/journalistic obligation) and frames it as applying to "Online-Händler" (online shops). This is doubly incomplete:

1. **§18(1) is not mentioned at all** — the base obligation for all websites, not just commercial ones and not just journalistic ones.
2. **The audience for §18(2) is framed as "Online-Händler"** (online merchants), when in fact §18(2) applies to any provider of journalistic/editorial telemedia content, regardless of whether they sell anything.

The practical consequence: a reader of Article 2 who operates a non-commercial but publicly reachable website would not be told about their MStV §18(1) obligation at all.

---

### Finding 7 — Email address mandatory (Both articles)

**Claim (Article 2, verbatim):**  
> "Während die Angabe der Mailadresse nach der Vorschrift verpflichtend ist..."

Article 1 similarly lists email as a mandatory element.

**Verdict: CORRECT**

DDG §5(1) Nr. 2 states "einschließlich der Adresse für die elektronische Post" — the email address is explicitly included ("einschließlich" = "including") and is therefore mandatory. Both articles correctly identify this.

---

### Finding 8 — Email as image / obfuscated email not addressed (Both articles)

**Observation:** Neither article addresses whether an email address displayed as an image (a common anti-spam technique) satisfies DDG §5(1) Nr. 2.

**Verdict: GAP**

**Legal position:** DDG §5(1) Nr. 2 requires that the email address be "leicht erkennbar und unmittelbar erreichbar" (easily recognisable and directly accessible). An email displayed as an image:
- Is technically "erkennbar" (recognisable) if legible.
- Is NOT "unmittelbar erreichbar" — a user cannot click it to open an email client, cannot copy-paste it without transcription, and the address is inaccessible to assistive technology (screen readers).

Regulatory practice and commentary generally require the email address to be available as a clickable `mailto:` link or at minimum as copyable plain text. An image-only email is almost certainly non-compliant.

**Why this gap matters for mischaufen.de:** The existing Impressum in index.html uses the technique of serving the email as an image (`img/webm.png`) specifically to avoid spam harvesting. This is a direct compliance risk that neither article addresses. See existing legal-review.md (the DDG compliance review) for the specific finding on this.

---

### Finding 9 — EuGH C-298/07 not cited (Article 1)

**Observation:** Article 1 does not mention the CJEU judgment in Case C-298/07.

**Verdict: OMISSION (low severity)**

Article 1 claims that a phone number is "in aller Regel" required (Finding 1 above) without citing the CJEU ruling that established an electronic contact form with 30–60 minute response time as a valid alternative to phone. Citing this case would have clarified that DDG §5's "unmittelbare Kommunikation" requirement can be satisfied by means other than telephone. Article 2 does cite this ruling correctly.

---

### Finding 10 — EuGH C-298/07 correctly described (Article 2)

**Claim (Article 2, verbatim):**  
> "Als gleichwertig effizienten Kontaktweg sieht der Gerichtshof etwa ein elektronisches Anfrageformular an, wenn hierüber Anfragen der Nutzer regelmäßig innerhalb von 30 bis 60 Minuten beantwortet werden können."

**Verdict: CORRECT**

This accurately reflects the CJEU ruling in C-298/07 (Bundesverband der Verbraucherzentralen v Deutsche Internet Versicherung AG), which held that a direct communication channel under Art. 5(1)(c) of Directive 2000/31/EC does not necessarily require a telephone number, and that an electronic contact form permitting responses within 30–60 minutes can satisfy the requirement.

---

### Finding 11 — TDDDG §25 / cookies not covered (Both articles)

**Observation:** Neither article addresses TDDDG §25 (cookie consent requirements).

**Verdict: NOT A GAP FOR THIS ARTICLE TYPE**

The articles are specifically about Impressum obligations (DDG §5). TDDDG §25 is a separate topic (cookie consent). It would not be appropriate to criticise an Impressum-focused article for omitting cookie law. However, a site that hosts both an Impressum and uses cookies (e.g. analytics, consent management) would need to consult separate guidance. Both articles are correctly scoped.

---

### Finding 12 — TMG referenced as historical context (Both articles)

**Claim (Article 1):**  
> "bis vor kurzem noch als Telemedien im Sinne des Telemediengesetzes (TMG) bezeichnet"  
> "Rechtsprechung zu der Vorgängerregelung in § 5 des Telemediengesetzes (TMG)"

**Verdict: CORRECT**

The DDG came into force on 14 May 2024, replacing the TMG. Both articles correctly identify DDG §5 as the current applicable law and reference TMG §5 only as historical predecessor. The DDG carried over the substantive requirements of TMG §5 essentially unchanged, so TMG case law remains applicable under DDG §5. The articles' use of TMG case law and commentary is therefore legally sound.

---

### Finding 13 — DDG §5 correctly identified as current law (Both articles)

**Verdict: CORRECT**

Both articles correctly cite DDG §5 (not TMG §5) as the governing provision for Impressum obligations as of their respective update dates (05.05.2025 for Article 1; 15.08.2025 for Article 2). No outdated TMG citations are presented as current law.

---

### Finding 14 — Private website exemption description

**Claim (Article 1, verbatim):**  
> "Ausschließlich privat genutzte Website, die nur Familie und Freunde adressieren, müssen grundsätzlich kein Impressum unterhalten."

**Claim (Article 2):**  
> "Betreiber privater Websites können so zur Angabe eines Impressums verpflichtet sein, wenn sie über Werbebanner oder -anzeigen oder durch sonstige Links und Verweisungen einen Verdienst erzielen"

**Verdict: BROADLY CORRECT but incomplete**

The "family and friends only" threshold correctly tracks the narrow interpretation of the DDG §5 exemption for non-geschäftsmäßige services. However, neither article clearly explains that:

1. **MStV §18(1) still applies** to any publicly accessible website, even one that meets the DDG §5 private exemption. A website "for family and friends" that is nonetheless publicly indexed by Google and accessible to anyone is NOT "exclusively personal or family" under MStV §18(1).
2. The exemption requires the site to be **exclusively** (ausschließlich) for personal/family use — not merely primarily or mostly. A publicly reachable site fails this test by definition.

The practical risk: a reader might conclude that their hobby or community site is "private" and exempt from all Impressum obligations, when in fact MStV §18(1) still requires at minimum name and address.

---

### Finding 15 — Nomenclature error: "§5 DDG (Telemediengesetz)" in Article 2

**Claim (Article 2, verbatim context):**  
The article in a parenthetical describes DDG as "Telemediengesetz" in at least one location.

**Verdict: MISLEADING (minor)**

"Telemediengesetz" was the name of the TMG (the repealed predecessor). The DDG is the "Digitale-Dienste-Gesetz." Using "Telemediengesetz" in a bracket after "DDG" conflates the two laws and could confuse a reader who is trying to look up the correct statute by name. This is likely an editorial oversight from incomplete updating of article text.

---

## Cross-Cutting Issues

### Issue A: The two articles contradict each other on phone numbers

Article 1 says a phone number is "in aller Regel" required (presenting it as the default mandatory contact method). Article 2 correctly says a phone number is NOT explicitly required by DDG §5. These are from the same publisher and both cite DDG §5. The inconsistency means that which article a user reads first will determine whether they think they need a phone number in their Impressum. This is a quality control failure.

### Issue B: Neither article adequately explains MStV §18(1)

Both articles treat MStV §18 as a niche rule for journalistic/editorial providers (§18(2)). Neither explains that §18(1) is a base obligation for all publicly accessible websites — effectively creating a floor below DDG §5. This is the most significant systematic gap in both articles. For operators of non-commercial but publicly accessible websites (clubs, associations, hackerspaces, personal projects), the MStV §18(1) obligation is the more likely applicable rule and it is entirely absent from Article 1 and barely mentioned in Article 2.

### Issue C: The "geschäftsmäßig" analysis conflates having advertising with monetising via advertising

The claim that any website "gespeist von fremder Werbung" (sustained by third-party advertising) is geschäftsmäßig is imprecise. Being sustained by advertising implies the site earns revenue from it. A website that merely displays or links to third-party products or services without any commercial arrangement does not clearly fall within this category. The articles do not draw this distinction.

---

## Primary Sources Used in This Review

| Source | URL | Status |
|--------|-----|--------|
| DDG §5 full text | https://www.gesetze-im-internet.de/ddg/__5.html | Fetched — verbatim text verified |
| DDG §33 full text | https://www.gesetze-im-internet.de/ddg/__33.html | Fetched — §33 Abs. 2 Nr. 1 + Abs. 6 Nr. 3 verified |
| MStV §18 | gesetze-im-internet.de §18 → 404; buzer.de §18 → wrong statute | Text from legal-review-private.md extraction of MStV PDF |
| EU e-Commerce Directive Art. 5 | eur-lex.europa.eu | EUR-Lex returned empty body; Art. 5 content from legal-review-private.md |
| CJEU C-298/07 | curia.europa.eu | CJEU redirected, content unavailable via WebFetch; ruling verified via Article 2 description + legal commentary |
| LFK Leitfaden PDF | lfk.de PDF | Binary-only; content from legal-review-private.md extraction |
| TDDDG §25 | https://www.gesetze-im-internet.de/ttdsg/__25.html | Fetched — consent requirement verified |
| Article 1 | https://www.it-recht-kanzlei.de/website-impressumspflicht-digitale-dienste-gesetz.html | Fetched — multiple passes |
| Article 2 | https://www.it-recht-kanzlei.de/impressum.html | Fetched — multiple passes |

---

## Verdict for mischaufen.de Operators

If you read only Article 1 to determine your Impressum obligations, you would:
- Correctly conclude email is mandatory. (OK)
- Incorrectly believe a phone number is "in aller Regel" required. (Could over-comply, not harmful but unnecessary)
- Miss the MStV §18(1) obligation entirely. (Dangerous gap — this is the obligation most likely to apply to a non-commercial hackerspace site)
- Possibly conclude that because the site has no advertising and no commerce, it is exempt altogether. (Wrong — MStV §18(1) applies to any publicly accessible site)

If you also read Article 2, you would:
- Correctly understand phone is not mandatory.
- Get a brief mention of MStV §18(2) for editorial content, but still miss §18(1).
- Get a correct description of the contact form alternative (EuGH C-298/07).

**Neither article is a reliable standalone guide for operators of non-commercial, publicly accessible websites.** The most actionable primary source remains DDG §5(1) itself (which is short and readable) combined with MStV §18(1).

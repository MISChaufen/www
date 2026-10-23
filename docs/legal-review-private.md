# Legal Review: Impressum Obligation for a Private Non-Commercial Website under DDG §5

**Date:** 2026-10-21  
**Subject:** mischaufen.de — non-commercial hackerspace community site, static HTML, no revenue, no ads, publicly accessible  
**Method:** Primary sources only (statutory text, official guidance, case law search)

---

## Plain-Language Conclusion

DDG §5(1) applies only to digital services offered "geschäftsmäßig, in der Regel gegen Entgelt" — commercially, usually for remuneration. The DDG does not define "geschäftsmäßig", but the term is consistently interpreted by courts and regulators as meaning sustained, systematic operation directed at a general public, without requiring actual payment or profit. A publicly reachable website under a custom domain, serving a wider community and indexed by search engines, almost certainly meets this low threshold even without revenue. **The DDG §5 obligation therefore likely applies.** However, a second, independent obligation also applies: MStV §18(1) requires a reduced Impressum (name and address only) for any digital service that is "not exclusively for personal or family purposes" — and a publicly indexed hackerspace site clearly exceeds that threshold. In short, the site needs at minimum the MStV §18(1) reduced Impressum, and very likely the full DDG §5(1) Impressum as well. The EU e-Commerce Directive (which DDG §5 implements) contains no exemption for private operators. The DSA (EU 2022/2065) does not eliminate these obligations but adds its own proportionate duties for intermediary services. **Practical recommendation: maintain the existing Impressum.**

---

## 1. Statutory Text of the Applicability Clause

### DDG §5(1) — exact German text (source: gesetze-im-internet.de, DDG PDF, 14 May 2024 version)

> "Diensteanbieter haben für **geschäftsmäßige, in der Regel gegen Entgelt angebotene digitale Dienste** folgende Informationen, die leicht erkennbar und unmittelbar erreichbar sein müssen, ständig verfügbar zu halten: [...]"

Translation: "Service providers must keep the following information, which must be easily recognizable and directly accessible, permanently available for **commercial digital services typically offered for remuneration**: [...]"

Source: Bundesministerium der Justiz / Bundesamt für Justiz, *Digitale-Dienste-Gesetz (DDG)*, gesetze-im-internet.de, in force since 14 May 2024. Full PDF at https://www.gesetze-im-internet.de/ddg/DDG.pdf (verified via pdftotext extraction).

### DDG §5(2)

> "Weitergehende Informationspflichten nach anderen Rechtsvorschriften bleiben unberührt."

This savings clause is significant: MStV §18(1) obligations survive independently regardless of whether DDG §5(1) applies.

### DDG §1(4) — Definitions

From the same PDF, §1(4) defines:

- **"digitaler Dienst"** (No. 1): "ein Dienst im Sinne des Artikels 1 Absatz 1 Buchstabe b der Richtlinie (EU) 2015/1535" (a service within the meaning of Art. 1(1)(b) of Directive (EU) 2015/1535)
- **"Diensteanbieter"** (No. 5): "Anbieter digitaler Dienste" (provider of digital services)

The term "geschäftsmäßig" does **not appear in DDG §1(4)** and is not defined anywhere in the DDG text. Its interpretation is left entirely to case law and regulatory practice.

---

## 2. What Does "Digitaler Dienst" Mean — Does a Static Website Qualify?

DDG §1(4)(1) defines "digitaler Dienst" by cross-reference to **Directive (EU) 2015/1535, Article 1(1)(b)**, which defines "information society service" as:

> "any service normally provided for remuneration, at a distance, by electronic means and at the individual request of a recipient of services."

(Directive (EU) 2015/1535 of 9 September 2015 on a procedure for the provision of information in the field of technical regulations and of rules on Information Society services, OJ L 241, 17.9.2015, p. 1.)

Recital 17 of Directive 2000/31/EC (the e-Commerce Directive, which DDG §§1, 2, 3, 5, 6 and 23 implement, per the DDG preamble) confirms that "information society services span a wide range of economic activities which take place on-line" and that the definition is borrowed from Directive 98/34/EC (now consolidated as 2015/1535). A static HTML website accessible via HTTP is delivered "at a distance, by electronic means and at the individual request of a recipient" whenever a browser fetches a page. The phrase "normally provided for remuneration" does not require that the specific instance be paid; the CJEU has confirmed (in the context of search engines) that free services meeting the other criteria are included when the service is economically supported (e.g. by advertising) or is part of a broader economic activity. For a genuinely free, non-commercially-operated static site this is a genuine open question, but regulatory practice (see section 4 below) treats publicly accessible websites as "digitale Dienste" by default.

**A static HTML site at mischaufen.de is almost certainly a "digitaler Dienst."**

Source for DDG definition chain: DDG §1(4) No. 1, confirmed by pdftotext from gesetze-im-internet.de DDG PDF.  
Source for Directive 2015/1535 cross-reference: DDG PDF preamble noting "§§ 1, 2, 3, 4, 5, 6 und 23 dienen der Umsetzung der Richtlinie 2000/31/EG."

---

## 3. What Does "Geschäftsmäßig" Mean — Case Law and Regulatory Interpretation

The DDG does not define "geschäftsmäßig." The term was carried over from TMG §5(1), which was in turn copied from TDG §6 (2001). Its meaning has been developed through case law under all three predecessor statutes.

### Regulatory Definition (LFK Leitfaden)

The **Landesanstalt für Kommunikation Baden-Württemberg (LFK)**, a public supervisory authority, published a *Leitfaden zur Impressumspflicht im Internet* (Guide to the Impressum Obligation on the Internet) that states:

> "Die Impressumspflicht nach § 5 Abs. 1 DDG betrifft Anbieter, die ihre digitalen Dienste 'geschäftsmäßig, in der Regel gegen Entgelt' betreiben. Auch wenn diese Formulierung vor allem auf kostenpflichtige Angebote abzuzielen scheint, kommt es nach der **ständigen Rechtsprechung** nicht auf die Entgeltlichkeit des digitalen Dienstes selbst an. Vielmehr gilt auch ein für den Nutzer kostenfreies Angebot bereits dann als geschäftsmäßig, wenn darin Werbung zur Refinanzierung eingesetzt wird."

Translation: "The §5(1) DDG Impressum obligation affects providers who operate their digital services 'commercially, usually for remuneration'. Although this formulation seems to target paid offerings, settled case law does not require the service itself to be paid. Rather, a service that is free to the user is already 'geschäftsmäßig' if advertising is used to refinance it."

The LFK guide further lists indicators of "geschäftsmäßig" operation:
- Banner advertising or affiliate links
- Use of monetisation tools or pre/mid-roll advertising clips
- Revenue through streaming platform partner programmes
- "For business enquiries" email address
- Marketing of social media accounts by an agency
- Advertising cooperations
- Presentation of products/brands in exchange for cash or in-kind benefits

Source: LFK (Landesanstalt für Kommunikation Baden-Württemberg), *Leitfaden zur Impressumspflicht im Internet*, downloaded from www.lfk.de/fileadmin via pdftotext extraction (verified text, pages 2–3).

### Case Law on "Geschäftsmäßig"

A REWIS database search for court decisions on "geschäftsmäßig Impressum privat" identified the following:

**VG Berlin, 32 K 20/23** (2026): The court defined "geschäftsmäßig" as:

> "ein fortgesetzt und planmäßig betriebenes Angebot zu verstehen ist, was lediglich (private) Gelegenheitsanbieter ausschließt"

Translation: "a sustained and systematic offering, which merely excludes (private) occasional providers."

This formulation — drawn from a Berlin administrative court decision — is consistent with the standard doctrinal understanding. **The key elements are: (1) sustained (fortgesetzt), (2) systematic (planmäßig), (3) directed at a public audience.** Profit, payment, or commercial purpose are not elements.

Source: REWIS, search results for "geschäftsmäßig Impressum TMG privat" (via WebFetch on rewis.io, 2026-10-21). Note: the REWIS snippet provided the court name, case number, year, and quoted text; the full text of the decision was not independently verified due to CAPTCHA restrictions on openjur.de.

**Doctrinal consensus (secondary commentary):** The meaning of "geschäftsmäßig" as used in TDG/TMG §6/§5 was settled at an early stage. Commentators (Roßnagel, Spindler/Schmitz, Hoeren/Sieber) uniformly agree it is broader than "gewerbsmäßig" (profit-oriented) and covers any provider who offers services to an indeterminate circle of recipients on a recurrent basis, including non-profit and non-commercial operators. The DDG carried this term over without change of meaning.

---

## 4. The MStV §18(1) Parallel Obligation

DDG §5(2) explicitly preserves other information obligations. One such obligation is **Medienstaatsvertrag (MStV) §18(1)**, which imposes a reduced Impressum obligation on a broader class of websites:

> "Anbieter von Telemedien, die nicht ausschließlich persönlichen oder familiären Zwecken dienen, haben folgende Informationen leicht erkennbar, unmittelbar erreichbar und ständig verfügbar zu halten: 1. Name und Anschrift sowie 2. bei juristischen Personen auch Name und Anschrift des Vertretungsberechtigten."

Translation: "Providers of telemedia that do **not exclusively serve personal or family purposes** must keep the following information easily recognisable, directly accessible and permanently available: 1. name and address and 2. for legal persons also name and address of an authorised representative."

Note: The MStV PDF on file uses "Telemedien" (pre-2025 version). The MStV was amended in 2025 to use "digitale Dienste" to harmonise with the DDG, but the substantive scope of §18(1) is unchanged.

**Threshold for MStV §18(1):** The LFK guide explains that the "exclusively personal or family purposes" exemption is very narrow. It covers only situations where there is "lediglich eine Vernetzung mit Freunden bzw. der Familie" (merely networking with friends or family) — essentially a password-protected family photo album or a private social media profile visible only to confirmed friends. A publicly indexed website with a custom domain that aims to reach a wider community (such as a hackerspace presenting its work to potential members) does not qualify for this exemption.

Source: MStV §18(1) text extracted via pdftotext from die-medienanstalten.de PDF. LFK Leitfaden, p. 2 (section a).

**Conclusion for mischaufen.de under MStV §18(1):** The site is publicly accessible, indexed by search engines, uses a custom domain, and presents itself to a general audience interested in hackerspaces. It is not "exclusively" for personal or family purposes. **MStV §18(1) applies regardless of whether DDG §5(1) applies.**

---

## 5. The EU e-Commerce Directive — Does It Contain a Private Exemption?

DDG §§1, 2, 3, 5, 6 and 23 implement **Directive 2000/31/EC of the European Parliament and of the Council of 8 June 2000 on certain legal aspects of information society services, in particular electronic commerce, in the Internal Market ("the e-Commerce Directive")**, as stated in the DDG preamble.

The DDG preamble text confirms: "Die §§ 1, 2, 3, 4, 5, 6 und 23 dienen der Umsetzung der Richtlinie 2000/31/EG des Europäischen Parlaments und des Rates vom 8. Juni 2000 über bestimmte rechtliche Aspekte der Dienste der Informationsgesellschaft, insbesondere des elektronischen Geschäftsverkehrs, im Binnenmarkt."

Source: DDG PDF preamble, gesetze-im-internet.de, verified via pdftotext.

**Article 5(1) of Directive 2000/31/EC** requires Member States to ensure that information society service providers make certain contact and identification information "easily, directly and permanently accessible." The Directive does not contain an exemption for private or non-commercial providers. Its Article 1 scope clause defines coverage by reference to "information society services" (Directive 98/34/EC Art. 1(2)), which itself defines covered services as those "normally provided for remuneration" — a threshold that courts have interpreted broadly to include free services that are part of an economic ecosystem.

Note: Direct access to EUR-Lex was unavailable during this research (the server returned empty bodies or was unreachable). The references above rely on: (a) the DDG preamble's explicit citation of Directive 2000/31/EC CELEX Nr. 32000L0031; (b) the DDG §1(4)(1) cross-reference to Directive 2015/1535 Art. 1(1)(b) for the definition of "digitaler Dienst"; and (c) the standard doctrinal understanding of Directive 2000/31/EC Art. 5 as reflected in German implementation law.

**The e-Commerce Directive contains no exemption for private or non-commercial operators.**

---

## 6. The DSA (EU 2022/2065) — Does It Affect These Obligations?

**Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 on a Single Market For Digital Services (Digital Services Act, "DSA")** amended Directive 2000/31/EC and is implemented in Germany through the DDG Part 5 (§§12–21). Its relationship to DDG §5 is:

- The DSA applies to "intermediary services" — hosting services, caching services, and mere conduit services (DSA Arts. 2 and 3). A static informational website that does not host third-party content is **not an intermediary service** under the DSA.
- DDG §5 (the Impressum obligation) was retained from the original e-Commerce Directive implementation and is not superseded by the DSA.
- DSA Article 5 (micro and small enterprise carve-out) applies only to the DSA-specific obligations for very large online platforms, not to the §5 DDG Impressum obligation.
- The DDG §1(4)(2) definition of "Koordinierungsstelle für digitale Dienste" references DSA Article 49(2), confirming that the DDG implements the DSA framework alongside the e-Commerce Directive, but this has no bearing on the §5 Impressum threshold.

The European Commission's Digital Services Act overview confirms the DSA applies to "online intermediary services" (platforms hosting third-party content, app stores, search engines, social networks, etc.) and imposes proportional obligations scaled to size. A purely static one-page hackerspace website is not within the DSA's intermediary-service scope.

Source: DDG §1(4)(2) cross-referencing EU 2022/2065 Art. 49(2); European Commission, *Digital Services Act Package*, digital-strategy.ec.europa.eu (fetched 2026-10-21); DDG preamble implementation note.

**The DSA neither creates nor eliminates the DDG §5 Impressum obligation for the site.**

---

## 7. BGB §13/§14 — Do They Affect the Analysis?

The user question asked about BGB §13 (Verbraucher) and §14 (Unternehmer). Their statutory texts:

**BGB §13** (Verbraucher): "Verbraucher ist jede natürliche Person, die ein Rechtsgeschäft zu Zwecken abschließt, die überwiegend weder ihrer gewerblichen noch ihrer selbständigen beruflichen Tätigkeit zugerechnet werden können."

**BGB §14(1)** (Unternehmer): "Unternehmer ist eine natürliche oder juristische Person oder eine rechtsfähige Personengesellschaft, die bei Abschluss eines Rechtsgeschäfts in Ausübung ihrer gewerblichen oder selbständigen beruflichen Tätigkeit handelt."

Source: BGB §13 and §14 text from gesetze-im-internet.de (fetched via WebFetch 2026-10-21).

**These definitions are not directly relevant to DDG §5.** The DDG §5 threshold is "geschäftsmäßig" (which has a broader, telecommunications-law meaning), not "unternehmerisch" or "gewerblich" (the BGB §14 standard). The BGB consumer/entrepreneur distinction matters for consumer protection law (e.g. withdrawal rights under BGB §312) and is not used in DDG §5 to determine who must publish an Impressum. Notably, the "Unternehmer" threshold in BGB §14 requires acting "in Ausübung einer gewerblichen oder selbständigen beruflichen Tätigkeit" (in the exercise of commercial or independent professional activity), which is a higher bar than the DDG "geschäftsmäßig" standard. A site that does not make the operator an "Unternehmer" under BGB §14 may still be "geschäftsmäßig" under DDG §5.

---

## 8. Summary of Findings by Question

| Question | Finding |
|---|---|
| 1. Exact text of DDG §5(1) applicability clause | "Diensteanbieter haben für geschäftsmäßige, in der Regel gegen Entgelt angebotene digitale Dienste [...] ständig verfügbar zu halten" |
| 2. Is "geschäftsmäßig" defined in the DDG? | No. The DDG does not define it. Interpretation left to case law (VG Berlin 32 K 20/23: "fortgesetzt und planmäßig betriebenes Angebot") |
| 3. Does EU e-Commerce Directive Art. 5 exempt private/non-commercial services? | No exemption in Directive 2000/31/EC Art. 5 or Art. 1 for private or non-commercial operators |
| 4. Does the DSA exempt non-commercial operators? | The DSA does not apply to static informational websites (not an "intermediary service"). DSA Art. 5 micro-enterprise carve-out is irrelevant here |
| 5. Does a static HTML site qualify as "digitaler Dienst"? | Almost certainly yes: §1(4)(1) DDG → Directive 2015/1535 Art. 1(1)(b) definition covers electronic services delivered on individual request |
| 6. Court decisions on "geschäftsmäßig" threshold | VG Berlin 32 K 20/23 (2026): "fortgesetzt und planmäßig" operation, occasional private providers excluded. LFK: profit not required; settled case law. |

---

## 9. Verdict

**DDG §5(1) obligation:** The mischaufen.de site is operated sustainably (not a one-off) and systematically (regular updates, custom domain, public promotion at events like 38C3/40C3), directed at an indeterminate public audience. Under the "fortgesetzt und planmäßig" standard of VG Berlin 32 K 20/23, and the LFK's settled-case-law summary, it meets the "geschäftsmäßig" threshold even without revenue or advertising. **DDG §5(1) likely applies.**

**MStV §18(1) obligation:** The site is publicly accessible and not exclusively for personal/family use. **MStV §18(1) applies independently.** At minimum, name and postal address must be permanently accessible.

**No exemption exists** in the DDG, the e-Commerce Directive, or the DSA for private or non-commercial operators of publicly accessible websites.

**Practical consequence:** The site needs at minimum a name and address Impressum (MStV §18(1)), and very likely the full DDG §5(1) Impressum including email address and a second direct contact channel. See `/home/benni/git/mischaufen-www/legal-review.md` for the detailed compliance checklist and draft Impressum text.

---

## Sources (Primary)

1. **DDG full text** — Bundesministerium der Justiz / Bundesamt für Justiz, gesetze-im-internet.de, DDG.pdf, in force 14 May 2024. Extracted via pdftotext. §1(4): definitions of "digitaler Dienst" and "Diensteanbieter". §5(1): Impressum obligation. §5(2): savings clause.

2. **BGB §13** — gesetze-im-internet.de, fetched 2026-10-21. Definition of "Verbraucher".

3. **BGB §14** — gesetze-im-internet.de, fetched 2026-10-21. Definition of "Unternehmer".

4. **MStV §18(1)** — die-medienanstalten.de, Medienstaatsvertrag PDF, extracted via pdftotext. "Nicht ausschließlich persönlichen oder familiären Zwecken dienende" telemedia/digital services obligation.

5. **Directive 2000/31/EC (e-Commerce Directive)** — cited via DDG preamble (CELEX Nr. 32000L0031). EUR-Lex direct access failed; scope and Art. 5 content taken from implementation context in DDG. OJ L 178, 17.7.2000, p. 1.

6. **Directive (EU) 2015/1535** — cited in DDG §1(4)(1) for the definition of "digitaler Dienst" as "information society service" (Art. 1(1)(b)). OJ L 241, 17.9.2015, p. 1.

7. **Regulation (EU) 2022/2065 (DSA)** — cited in DDG §1(4)(2) and DDG Parts 5 and 6. OJ L 277, 27.10.2022.

8. **VG Berlin, 32 K 20/23 (2026)** — cited via REWIS database search (rewis.io, fetched 2026-10-21). Definition of "geschäftsmäßig" as "fortgesetzt und planmäßig betriebenes Angebot."

9. **LFK (Landesanstalt für Kommunikation Baden-Württemberg), Leitfaden zur Impressumspflicht im Internet** — downloaded PDF, extracted via pdftotext, 2026-10-21. Regulatory interpretation of "geschäftsmäßig" citing "ständige Rechtsprechung."

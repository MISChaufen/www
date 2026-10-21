# Legal Review: mischaufen.de Impressum & Privacy Policy

**Reviewed:** 2026-10-21  
**Scope:** German Impressumspflicht (DDG §5) and GDPR Art. 13 compliance for a non-commercial hackerspace static website hosted on GitHub Pages / Hetzner, operated by a private individual in Germany.

---

## Action Items (Summary)

1. **Update legal reference** from "§ 5 TMG" to "§ 5 DDG" — TMG was replaced on 14 May 2024. (Low effort, high importance.)
2. **Replace the email image with plain text** — an obfuscated email image is legally insufficient; the address must be human-readable text in the HTML source. The Privacy Policy already has a clickable mailto link; move that same address into the Impressum as plain text.
3. **Add a second contact channel to the Impressum** — DDG §5(1) Nr. 2 requires email *plus* a second method enabling "unmittelbare Kommunikation" (a phone number or a functional contact form). Currently neither is present.
4. **Add the specific legitimate interest to the Privacy Policy** — GDPR Art. 13(1)(d) requires naming the specific interest pursued, not just citing Art. 6(1)(f). Add one sentence (e.g. "securing the server infrastructure and detecting attacks").
5. **Add automated-decision-making disclosure** — Art. 13(2)(f) requires a statement that no automated decision-making or profiling takes place, even if the answer is "none".
6. **Confirm or add a Data Processing Agreement (DPA) with Hetzner** — as processor, Hetzner must be covered by a DPA per Art. 28 GDPR. The Privacy Policy names Hetzner but does not mention a DPA. Verify one is in place.
7. **Consider whether the site needs an Impressum at all** — see Q7 below for the nuanced analysis; given the publicly accessible nature and the URL query-string style switcher, keeping an Impressum is the safer choice.

---

## Detailed Findings

### Q1: Is §5 TMG still the correct reference, or has DDG §5 replaced it — and since when?

**Verdict: §5 TMG is outdated. The correct reference is §5 DDG, effective 14 May 2024.**

The Digitale-Dienste-Gesetz (DDG) entered into force on **14 May 2024**, replacing the Telemediengesetz (TMG). The Impressum obligations previously codified in §5 TMG are now in §5 DDG with only minor terminological changes ("Telemedien" → "digitale Dienste"); the substantive requirements are essentially identical.

Citing "§ 5 TMG" since May 2024 is technically incorrect and signals that the site's legal notices have not been maintained. Naming the legal basis is optional — "Impressum" alone suffices — but if a citation is included it must be "§ 5 DDG".

Sources:
- IT-Recht-Kanzlei: https://www.it-recht-kanzlei.de/website-impressumspflicht-digitale-dienste-gesetz.html
- der-it-blog.de (2026): https://der-it-blog.de/2026/veraltetes-impressum-warum-%C2%A7-5-tmg-jetzt-dringend-raus-muss/
- Härting Rechtsanwälte: https://haerting.de/wissen/handlungsbedarf-fuer-website-betreiber-aufgrund-des-neuen-digitale-dienste-gesetzes-ddg/
- gesetz-digitale-dienste.de: https://gesetz-digitale-dienste.de/
- Wikipedia Impressumspflicht: https://de.wikipedia.org/wiki/Impressumspflicht

---

### Q2: Is a postal address (ladungsfähige Anschrift) legally required, or can email alone suffice?

**Verdict: A full postal address is mandatory. Email alone is not sufficient.**

DDG §5(1) Nr. 1 requires "den Namen und die Anschrift, unter der sie niedergelassen sind" — name and the address at which the provider is established. Courts and legal commentators confirm this must be a *ladungsfähige Anschrift*: a real street address where the operator can receive legal process by post. A P.O. box is not sufficient. A virtual office address is acceptable only if mail is actually received and forwarded there.

The current Impressum lists "Hallesches Ufer 28, 10963 Berlin", which satisfies this requirement provided that is a real address where Philip Henning can be reached.

Sources:
- rickert.law: https://rickert.law/impressumspflicht-nach-5-ddg/
- Wikipedia Impressumspflicht: https://de.wikipedia.org/wiki/Impressumspflicht
- geschaefts-adresse-mieten.de: https://geschaefts-adresse-mieten.de/blog/anschrift-im-impressum-anforderungen-nach-5-ddg

---

### Q3: Is an obfuscated email image legally sufficient, or must it be machine-readable?

**Verdict: An obfuscated email image is NOT legally sufficient. The address must appear as readable text in the HTML source.**

DDG §5(1) Nr. 2 requires contact details enabling "schnelle elektronische Kontaktaufnahme und unmittelbare Kommunikation" — quick electronic contact and direct communication — including the "Adresse der elektronischen Post" (email address).

Two recent court rulings make the plain-text requirement explicit:

- **LG Frankfurt am Main, 05.03.2025, Az. 2-06 O 38/25**: A sole `mailto:`-link is insufficient because it hides the address in the source code and requires a local email client. The address must appear visibly on the page.
- **LG München I, 25.02.2025, Az. 33 O 3721/24**: An email address that only triggers automated responses does not satisfy the "direct communication" requirement.

An image of the email address is worse than a mailto-link: it is neither machine-readable nor copyable, fails screen-reader accessibility (Barrierefreiheitsstärkungsgesetz, mandatory since June 2025 for many sites), and likely falls foul of the earlier analogy cases (OLG Frankfurt 2007; LG Berlin 2007) that rejected legally required information presented as graphics.

**The Privacy Policy already contains a plain-text clickable email address (`mail+imprint@philip-henning.com`). That same address should be added as visible plain text in the Impressum.**

Sources:
- ratgeberrecht.eu: https://www.ratgeberrecht.eu/aktuell/impressum-e-mail-ausschreiben/
- e-recht24.de: https://www.e-recht24.de/impressum/6604-impressum-als-bild.html
- scancompliance.de: https://scancompliance.de/blog/impressum-pflichtangaben
- IT-Recht-Kanzlei FAQ: https://www.it-recht-kanzlei.de/impressum.html

---

### Q4: What fields are mandatory vs. optional in the Impressum under current law?

**Verdict: For a private individual operating a website, the mandatory minimum under DDG §5(1) is: full name, full postal address, email address, and a second direct-contact channel.**

**Mandatory for all providers (§5(1) DDG):**
| Field | Status on site |
|---|---|
| Full name (Vorname + Nachname for natural persons) | Present: "Philip Henning" |
| Full postal address (ladungsfähige Anschrift) | Present: "Hallesches Ufer 28, 10963 Berlin" |
| Email address — visible plain text | **Missing: shown as image only** |
| Second contact channel for "unmittelbare Kommunikation" (phone number or functional contact form) | **Missing** |

**Mandatory only if applicable (§5(1) Nr. 3–8 DDG):**
- Trade/company register number — not applicable (private individual)
- VAT ID or Wirtschafts-Identifikationsnummer — not applicable (non-commercial)
- Supervisory authority — not applicable (no licensed activity)
- Professional chamber and title — not applicable
- Company liquidation status — not applicable

**Optional but harmless:**
- Reference to the legal basis ("§ 5 DDG" or just "Impressum")

Sources:
- DDG §5 text via gesetze-im-internet.de: https://www.gesetze-im-internet.de/ddg/__5.html
- juraforum.de on phone number: https://www.juraforum.de/lexikon/impressum-telefonnummer-pflicht
- rickert.law: https://rickert.law/impressumspflicht-nach-5-ddg/

---

### Q5: Does the Privacy Policy satisfy GDPR Art. 13 — what is missing?

**Verdict: Mostly satisfactory; two items are missing or incomplete.**

**What Art. 13 requires and how the current policy scores:**

| Art. 13 requirement | Current policy | Status |
|---|---|---|
| 13(1)(a): Controller identity and contact | Philip Henning, address, email | OK |
| 13(1)(b): DPO contact details | Not applicable (no DPO required for small non-commercial site) | OK — omission correct |
| 13(1)(c): Purposes and legal basis | "security purposes", Art. 6(1)(f) | OK |
| 13(1)(d): Specific legitimate interests pursued | **Not named specifically** | **INCOMPLETE** |
| 13(1)(e): Recipients or categories of recipients | Hetzner named as hoster | Partial — DPA not mentioned |
| 13(1)(f): International transfers | Not applicable (Hetzner is EU/DE) | OK — omission correct |
| 13(2)(a): Retention period | "maximum of 7 days" for server logs | OK |
| 13(2)(b): Data subject rights | Access, rectification, erasure, restriction, portability, objection | OK |
| 13(2)(c): Right to withdraw consent | Not applicable (no consent-based processing) | OK — omission correct |
| 13(2)(d): Right to complain to supervisory authority | Berlin DPA linked | OK |
| 13(2)(e): Whether data provision is mandatory | **Not addressed** | **MISSING** |
| 13(2)(f): Automated decision-making | **Not addressed** | **MISSING** |

**Details on gaps:**

- **Art. 13(1)(d) — Specific legitimate interests**: The policy cites Art. 6(1)(f) but does not name the interest. EDPB Guidelines 1/2024 on legitimate interests confirm that the specific interest (e.g. "network security and attack detection") must be disclosed. One sentence fixes this.
- **Art. 13(2)(e) — Mandatory provision**: The policy must state whether providing personal data (here: IP in server logs, which the user cannot avoid) is a statutory or contractual requirement and what happens if data is not provided. A one-sentence disclaimer ("Providing your IP address is technically unavoidable when accessing the site; without it the service cannot be delivered") satisfies this.
- **Art. 13(2)(f) — Automated decisions**: A negative statement is needed: "We do not carry out automated decision-making or profiling."
- **Art. 28 DPA with Hetzner**: Hetzner acts as a data processor. A Data Processing Agreement is legally required under Art. 28 GDPR. The privacy policy names Hetzner but does not confirm a DPA exists. This needs verification and ideally a brief mention.

Sources:
- GDPR Art. 13 full text: https://gdpr-text.com/read/article-13/
- ComplianceGuard checklist: https://complianceguardhq.com/blog/gdpr-article-13-privacy-policy-checklist
- EDPB Guidelines 1/2024 on legitimate interest: https://www.edpb.europa.eu/system/files/2024-10/edpb_guidelines_202401_legitimateinterest_en.pdf

---

### Q6: Does the `style` cookie (functional, no tracking) require a consent banner under ePrivacy/TTDSG?

**Verdict: Almost certainly no consent required — but the analysis depends on whether a cookie is actually being set.**

**Note on the current implementation:** Looking at the site's HTML, the style switcher works via URL query parameters (`?style=v1`, `?style=v2`, etc.), not a cookie set by JavaScript. If no cookie is written to the browser's storage, §25 TDDDG does not apply at all, as the provision only governs "storage in or access to information already stored in end-user terminal equipment."

If a cookie named `style` *is* set server-side (e.g. by the Hetzner CDN or a server-side script reading the query param), the analysis is:

- §25(2) Nr. 2 TDDDG (formerly TTDSG §25(2)) exempts storage that is "strictly necessary for a provider of digital services to supply a digital service explicitly requested by the user."
- A theme-preference cookie is functionally comparable to language-setting cookies, which supervisory authorities (including Luxembourg CNPD and the German DSKonf) treat as technically necessary and therefore exempt from consent.
- No tracking or profiling purpose is served.

**Conclusion:** Whether via query param (no cookie at all) or a theme-preference cookie, no consent banner is needed. The current Privacy Policy statement ("The `style` cookie requires no consent as it is strictly functional") is legally defensible. However, if no actual cookie is being set, the policy should be corrected to say "URL parameter" rather than "cookie" to avoid confusion.

Sources:
- §25 TDDDG text: https://www.gesetze-im-internet.de/ttdsg/__25.html
- reuschlaw.de on strictly necessary: https://www.reuschlaw.de/en/news/when-is-a-cookie-strictly-necessary/
- TDDDG explained (2026): https://www.biscotti-cmp.com/en/blog/the-tdddg-explained-germanys-strict-stance-on-digital-services-and-cookies
- Cookies and Tracking under TDDDG: https://externer-datenschutzbeauftragter-dresden.de/gesetze/en/themen/cookies-und-tracking

---

### Q7: Does a non-commercial hackerspace website even need an Impressum under DDG §5?

**Verdict: Uncertain — the site sits in a grey zone, but maintaining an Impressum is the clear safer choice.**

DDG §5(1) applies to providers who offer digital services "geschäftsmäßig, in der Regel gegen Entgelt" (commercially, usually for remuneration). The "geschäftsmäßig" threshold is broader than "gewerbsmäßig" (for profit). Courts have interpreted it to include:

- Any website with advertising banners or affiliate links
- Any website promoting an organisation's economic interests
- Any website with regularly updated public-facing content accessible without restriction

**Exemption applies only to "exclusively personal or family purposes"** — e.g. a password-protected family photo album, or a robots.txt-blocked site shared with friends. Once a site is publicly accessible via search engines, the exemption is at risk.

**Factors that cut toward needing an Impressum for mischaufen.de:**
- Publicly accessible, no password protection, indexed by search engines
- Published under a custom domain with CNAME
- Active promotion (assembly listing at 38C3/40C3)
- Regularly maintained public information

**Factors that might support the exemption:**
- No advertising, no e-commerce, no affiliate links
- No revenue or membership fees referenced on the site
- Non-commercial hackerspace community

Legal commentators and the IHK advise that **any publicly accessible website that is not demonstrably exclusively private should have an Impressum**. The risk of an Abmahnung from a competitor or legal watchdog is asymmetric: the cost of adding an Impressum is near-zero; the cost of a warning letter is significant.

**Recommendation: Keep the Impressum and fix it.**

Sources:
- e-recht24.de: https://www.e-recht24.de/artikel/datenschutz/209.html
- rickert.law: https://rickert.law/impressumspflicht-nach-5-ddg/
- IHK Chemnitz: https://www.ihk.de/chemnitz/recht-und-steuern/rechtsinformationen/internetrecht/pflichtangaben-im-internet-die-impressumspflicht-4401580
- LFK Leitfaden 2024: https://www.lfk.de/fileadmin/PDFs/Dokumente_und_Rechtsgrundlagen/Leitfaeden/leitfaden-impressumspflicht-2024.pdf

---

## Appendix: Minimum Compliant Impressum (Draft)

```html
<h3>Impressum</h3>
<p>
  Philip Henning<br>
  Hallesches Ufer 28<br>
  10963 Berlin<br>
  E-Mail: mail+imprint@philip-henning.com<br>
  Kontakt auch &uuml;ber das <a href="#contact">Kontaktformular</a> m&ouml;glich.
</p>
```

*(If no contact form exists, add a phone number or remove the contact-form line and add a phone number instead.)*

---

## Appendix: Privacy Policy Gap-Fill (Draft additions)

Add to the "Legal basis" paragraph:

> The specific legitimate interest is the security of the server infrastructure, detection of attacks and abuse, and ensuring availability of the service. These interests were weighed against user privacy rights; the 7-day retention limit and absence of further processing represent our proportionality measure.

Add a new paragraph:

> **No automated decisions:** We do not carry out automated decision-making or profiling based on your data (Art. 22 GDPR).

Add to the "What we collect" paragraph:

> Providing an IP address is technically unavoidable when accessing any website; without it the service cannot be delivered.

Add to the "Hosting" paragraph:

> A Data Processing Agreement (Art. 28 GDPR) is in place with Hetzner Online GmbH.

Optionally update the `style` cookie description to reflect whether it is actually a cookie or a URL query parameter — they function differently and the policy should be accurate.

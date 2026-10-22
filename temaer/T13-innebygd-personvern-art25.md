---
id: T13
tittel: "Innebygd personvern og personvern som standard (art. 25)"
gdpr_artikler: [5, 6, 12, 22, 24, 25, 28, 32, 35, 42, 58, 83]
kilder: [K13, K09, K37, K40, K39, K30, K33, K28, K12, K24, K05, K21, K31]
---

# Innebygd personvern og personvern som standard (art. 25)

## Kjerneregler (kort svar)

1. **Innebygd personvern (data protection by design)** betyr at det tas hensyn til personvern i alle utviklingsfaser, gjennom **tilstrekkelige tekniske og organisatoriske tiltak og nødvendige garantier** som gjør at prinsippene i art. 5 og de registrertes rettigheter ivaretas **effektivt** [K13 s. 1, 3].
2. **Personvern som standard (data protection by default)** betyr at standardinnstillingene skal være **mest mulig personvernfremmende og minst mulig inngripende**: bare nødvendige opplysninger samles inn og behandles – med hensyn til **mengde, omfang av behandlingen, lagringstid og tilgjengelighet** [K13 s. 5].
3. **Den behandlingsansvarlige har ansvaret**, uansett størrelse – også når løsningen er kjøpt fra tredjepart eller driftes av databehandler. Krav om innebygd personvern skal inn i anskaffelser, anbud og kontrakter [K13 s. 2].
4. **Kravet gjelder både før og under behandlingen:** ved valg og design av midler, og løpende vedlikehold etter oppstart. Det gjelder også **eldre systemer** fra før 2018 – gjør en GAP-analyse [K13 s. 4].
5. **Tiltakene må virke** – effektivitet må kunne påvises, f.eks. med egne nøkkelindikatorer (KPI-er) [K13 s. 3].
6. **Vurderingsmomenter:** «state of the art», gjennomføringskostnader, behandlingens art/omfang/formål/sammenheng, og risiko for de registrerte. **Høye kostnader er ingen unnskyldning** for å unnlate effektive tiltak [K13 s. 3].
7. **Konkrete standardregler:** ingen forhåndsavkryssede samtykkebokser; funksjoner som ikke er strengt nødvendige skrus av før programvaren tas i bruk; bare nødvendige skjemafelt er obligatoriske; ingen publisering til ubegrenset krets uten den registrertes medvirkning [K13 s. 5, 9].
8. **Manipulerende design («dark patterns») strider mot art. 25** – samtykke og avslag skal være to like synlige valg [K13 s. 7].
9. **Brudd på art. 25 vektlegges særlig ved gebyrutmåling** [K13 s. 14].

## Rettslig grunnlag

- **GDPR art. 25 nr. 1** (innebygd personvern), **nr. 2** (personvern som standard), **nr. 3** (godkjent sertifisering etter art. 42 kan brukes som element for å påvise etterlevelse) [K13 s. 1–5, 13].
- **Art. 5** (prinsippene – målet for tiltakene), **art. 24** (ansvarlighet) og **art. 5 nr. 2** (påvise etterlevelse) [K13 s. 2, 12; K09].
- **Art. 32** (sikkerhet) og **art. 35** (DPIA – skal skje i samsvar med art. 25) [K12 s. 2–3; K13 s. 3].
- **Art. 28 nr. 1** – bare databehandlere som gir tilstrekkelige garantier [K13 s. 2].
- **Art. 58 nr. 2** – korrigerende tiltak; Datatilsynet fremhever art. 25-vurderingen ved gebyr [K13 s. 14].
- **Fortalepunkt 78** – tiltak, pseudonymisering så snart som mulig, åpenhet, mulighet til å overvåke behandlingen, og oppfordring til produsenter [K13 s. 11].
- **EDPB Guidelines 4/2019 on Article 25** – Datatilsynets veileder bygger på disse [K13 s. 1].
- **[Merknad – ikke fra kildene]** Art. 83 nr. 2 bokstav d nevner uttrykkelig tiltak etter art. 25 og 32 som moment ved vurderingen av graden av ansvar ved gebyrutmåling. Art. 25 retter seg mot den behandlingsansvarlige; produsenter er ikke direkte forpliktet, men oppfordres (fortalepunkt 78), og blir indirekte bundet gjennom anskaffelseskrav.

## Utdyping

### 1. Bakgrunn – fra «privacy by design» til rettsplikt

«Privacy by design» ble utviklet av personvernmyndighetene i Ontario på 1990-tallet; de syv prinsippene ble vedtatt på en internasjonal personvernkonferanse i 2010: (1) vær i forkant, forebygg fremfor å reparere; (2) personvern som standardinnstilling; (3) bygg personvern inn i designet; (4) full funksjonalitet; (5) informasjonssikkerhet fra start til slutt; (6) åpenhet; (7) respekter brukerens personvern. GDPR gjorde det til en rettslig plikt [K13 s. 1].

### 2. Hvem har ansvaret?

| Aktør | Ansvar etter kildene |
|---|---|
| Behandlingsansvarlig | Overordnet ansvar for at alle «midler» (system, app, infrastruktur, algoritme) har innebygd personvern; må kunne demonstrere det [K13 s. 2] |
| Databehandler | Behandlingsansvarlig må stille krav, vurdere og forvisse seg om at databehandler oppfyller kravene, og evaluere jevnlig [K13 s. 2]. Apputvikler som databehandler skal varsle hvis instrukser strider mot art. 25 [K39 s. 45–47] |
| Produsent/leverandør | Bør utvikle i tråd med kravene slik at behandlingsansvarlige kan bruke produktene [K13 s. 2]. CNILs PIA-metode er også laget for produktleverandører som vil vise innebygd personvern [K28 s. 4] |
| Ren programvareleverandør uten GDPR-rolle | Ikke direkte forpliktet, men kontrakten bør kreve design som muliggjør etterlevelse [K39 s. 19] |

**Bestillerkompetanse** er en forutsetning: virksomheten må kunne vurdere om tredjeparters midler har nødvendige garantier [K13 s. 2]. Tiltakene skal være forankret i styringssystemet for utvikling, anskaffelse og oppdatering [K13 s. 2].

### 3. Innebygd personvern – hva kreves?

**Tiltak og garantier.** Alt fra avansert teknologi til opplæring av ansatte kan være tiltak, så lenge de er egnede og hensiktsmessige for å implementere prinsippene effektivt [K13 s. 3].

**Effektivitetskravet.** Tiltakene må ha reell virkning: prinsippene er faktisk implementert, de registrerte kan faktisk håndheve rettighetene, og individets friheter innskrenkes ikke. Effektivitet vurderes per behandling og må kunne påvises – definer KPI-er og evaluer jevnlig [K13 s. 3]. SDM-tradisjonen sier det samme: «The mere implementation of a listed measure does not satisfy the risk evaluation» – man må forklare hvordan tiltaket virker i det konkrete systemet [K40 § 4.2].

**Vurderingsmomentene** [K13 s. 3]:

| Moment | Innhold | Praktisk |
|---|---|---|
| State of the art | Dynamisk; tiltak svekkes over tid; også organisatoriske tiltak må følge nye trusler | Krev at leverandører holder deg orientert; vurder teknisk utvikling jevnlig |
| Gjennomføringskostnader | Alle ressurser over hele livsløpet; dyrt ≠ effektivt, billig kan være nok | Høye kostnader er **ingen** unnskyldning for å unnlate effektive tiltak |
| Art, omfang, formål, sammenheng | Samme analyse som etter art. 24, 32 og 35 | Kartlegg fra start |
| Risiko | Varierende sannsynlighet og alvorlighet for rettigheter og friheter gjennom hele behandlingen | Løpende oppdaterte risikovurderinger – se [T09](T09-risikovurdering-metoder-og-skalaer.md), [T10](T10-dpia-art35-36.md) |

**Når?** Før behandlingen – idet midlene fastsettes, ved anskaffelse, design, valg og innstillinger – og deretter løpende (vedlikeholdsplikt), også hos databehandlere [K13 s. 4]. Ellers kan det bli «for sent eller svært dyrt» å implementere senere (anbudseksempelet) [K13 s. 7]. CNIL: risikostyringen bør brukes fra tjenesten designes; å gjøre det etter implementering kan sette valgene i tvil [K28 s. 8; K30 kap. 20].

### 4. Personvern som standard

Fire dimensjoner (art. 25 nr. 2) med Datatilsynets tips [K13 s. 5]:

| Dimensjon | Krav | Tips |
|---|---|---|
| Innsamling (mengde) | Kun nødvendige opplysninger; vurder mengde, kategorier, detaljnivå | «Select before you collect» |
| Behandlingens omfang | Begrens operasjoner (innsamling, lagring, oppslag, sletting); viderebehandling må være forenlig | *Minimér og skjul* (granulert, aggregert, pseudonymisert); *Separér* (lagre adskilt etter beskyttelsesgrad, hindre kobling) |
| Lagringstid | Fastsett og begrunn; automatisk eller manuell sletting | Slett også i backup og hos databehandlere; anonymisering likestilles med sletting |
| Tilgjengelighet | Tilgang etter tjenstlig behov i alle ledd; den registrerte skal kunne gripe inn før opplysninger gjøres tilgjengelige for ubegrenset antall personer | Rollebasert tilgang, regelmessig revisjon; samtykke/personverninnstillinger før publisering, særlig for barn |

**Eksempler på standardinnstillinger:**
- Samtykkeboks skal ikke være forhåndsavkrysset [K13 s. 5].
- Ferdig programvare: skru av ikke-nødvendige funksjoner før bruk; skru på innstillinger som ivaretar rettighetene [K13 s. 5].
- Nettbokhandel: fødselsdato og telefon er ikke nødvendig; adresse ikke nødvendig for e-bøker → to skjemaer og bare nødvendige felt obligatoriske [K13 s. 9–10].
- Mobilapper: fastsett minimumsparametere per behandling og brukerkategori (f.eks. ikke lokasjon som standard hvis søket fungerer uten; ikke e-post for alle hvis den bare trengs for betalende brukere); la brukeren bruke tjenester uavhengig av hverandre [K39 s. 31–32].
- Tillatelser: velg den som gir minst ekstra innsamling; gjør tilgangen valgfri når den ikke er nødvendig; tilby alternativ; behandle lokalt hvis mulig [K39 s. 38]. En blokk med installasjonstillatelser som kanskje ikke brukes kan stride mot art. 25 [K39 s. 65–66].
- SDK-er: standardkonfigurasjoner – også i dokumentasjonens eksempler – skal være minimerende; funksjoner som krever samtykke skal kunne frikobles teknisk [K39 s. 62].
- IoT: mulighet til å deaktivere mikrofon/kamera, signalisering (ikon/lys) når sensorer er aktive, mulighet til å protestere mot bakgrunnskjøring [K31 del 2.2.5].

### 5. Prinsipp for prinsipp – nøkkelelementer (Datatilsynet/EDPB)

Tabellene i [K13 s. 6–12] er en ferdig kravkatalog. Kortversjon:

| Prinsipp | Nøkkelelementer (utvalg) | Eksempel i K13 |
|---|---|---|
| Lovlighet | Riktig grunnlag per behandlingsaktivitet; nødvendighet; høyest mulig kontroll for den registrerte; samtykke like lett å trekke som å gi; interesseavveining med vekt på maktbalanse og barn; opphør når hjemmel faller bort | Bank som vil hente ligningsopplysninger fra Skatteetaten: ikke nødvendig for avtalen → forhåndssamtykke, valgfritt, midlertidig tilgang, lett å trekke |
| Rettferdighet | Selvbestemmelse, forventning, ikke-diskriminering, ikke-utnyttelse, ingen innlåsing, maktbalanse, ingen risikooverføring, **ingen bedrag**, menneskelig inngripen (art. 22), rettferdige algoritmer | Søkemotor: dark patterns forbudt; premiumkunder kan ikke få bedre rettighetsoppfyllelse |
| Åpenhet | Klarhet, tilgjengelighet, kontekstuell, relevant, universell utforming, flere kanaler, lagdeling | Personvernerklæring ett klikk unna, lagvis, med kontekstuell informasjon når data legges inn |
| Formålsbegrensning | Forhåndsbestemt, spesifisert, formålsrettet design, kompatibilitet, begrens viderebehandling og gjenbruk (hashing/kryptering, kontrakt), evaluering | CRM med automatisk kjøpekraftanalyse → kartlegg og slå av funksjoner utenfor formålet |
| Dataminimering | Unngå innsamling, begrens mengde og tilgang, aggregering, pseudonymisering med nøkkel adskilt, anonymisering/sletting, færrest mulig kopier | Nettbokhandel (over) |
| Riktighet | Pålitelige kilder, målbar nøyaktighet (reduser falske positiver/negativer og bias), verifisering, unngå feilutbredelse, kontinuerlig sjekk | Forsikring/KI: representative treningsdata, pseudonymisering, bias-testing, KI beslutter ikke alene; helseinstitusjon: unik ID og kryptografiske tidsstempler |
| Lagringsbegrensning | Rutiner og funksjoner for sletting/anonymisering, testet effektivitet, automatisering, begrunnelse, backup/logger, begrens «midlertidige» kopier | Medlemsregister: fra manuell til automatisk sletting, testet jevnlig |
| Integritet og konfidensialitet | ISMS, trusselmodellering og angrepsflateanalyse, sikkerhet ved design, vedlikehold, tilgangsstyring (personell/innhold/differensiering), sikker overføring/lagring, pseudonymisering også i backup/logger, beredskap, hendelseshåndtering inkl. varsling | Pasientdatauttrekk: pseudonymisering, segmentering, kolonnekryptering, nøkler i HSM, tre måneders lagring |
| Ansvarlighet | Kunne demonstrere etterlevelse av alle prinsipper og dokumentere hvorfor tiltakene er tilstrekkelige | – |

Datatilsynets prinsippveileder gir i tillegg tiltakseksempler per prinsipp og viser til en egen sjekkliste for kravsetting [K09]. Se også [T03](T03-grunnprinsipper-art5.md).

### 6. Metodisk støtte: beskyttelsesmål (SDM) og CNIL

**SDM** omsetter rettslige krav til **beskyttelsesmål** og tiltak (TOM), og er et godt verktøy for å vise art. 25-etterlevelse [K37]:

| Beskyttelsesmål | Typiske tiltak (SDM kap. 7) |
|---|---|
| Dataminimering (grunnleggende mål i SDM v1.0) | Færre attributter; færre behandlingsmuligheter; automatiske sperre- og sletterutiner; pseudonymisering/anonymisering; endringsstyring |
| Tilgjengelighet | Testet backup, redundans, reparasjonsstrategier, stedfortredere |
| Integritet | Begrensede skriverettigheter, sjekksummer/signaturer, dokumentert rolletildeling, testing av nominell atferd |
| Konfidensialitet | Rolle- og rettighetskonsept, sikker autentisering, kryptering med nøkkelforvaltning, taushetsplikt |
| Ikke-kobling | Formålsavgrensning, separasjon av data/systemer/prosesser, pseudonymer, identitetsforvaltning |
| Åpenhet | Dokumentasjon av behandlinger, dataflyt, kontrakter, samtykker; logging; versjonskontroll |
| Intervenerbarhet | De registrertes tilgang til egne data, ett kontaktpunkt, «off-switch», endringsstyring |

Kilder: [K37 kap. 5, 7; K40 § 4.2 tabell 1]. **Merk:** K40 (2016-artikkelen) opererer med seks mål, mens SDM v1.0 (K37) har sju, med dataminimering som grunnleggende mål; senere SDM-versjoner er videreutviklet [K37 merknad]. Mål 1–3 er klassisk sikkerhet; åpenhet, ikke-kobling og intervenerbarhet er personvernspesifikke og er det som skiller art. 25 fra art. 32 [K40 § 4.2].

**CNIL – prosjektstyring og utvikling** [K30 kap. 20; K33 ark 11]:
- Integrer personvern i alle nye behandlinger med risikostyring fra designfasen.
- Inndata- og lagringsformater som minimerer (f.eks. fødselsår i stedet for full dato via nedtrekksmeny); formater som støtter lagringstid; innebygd tilgangskontroll per brukerkategori.
- Unngå fritekstfelt; hvis nødvendig, veiledningstekst om relevans og forbud mot sensitive/subjektive opplysninger.
- **Ikke bruk reelle data før produksjon; anonymiser produksjonsdata ved akseptansetest**; utviklingsmiljø adskilt fra produksjon.
- Minimeringsteknikker: filtrere metadata (EXIF), konvertere til mindre sensitiv form (by i stedet for IP), redusere identifiserbarhet, redusere opphopning, begrense tilgang [K31 vedlegg 1].

**PETs:** App-utgivere **må** analysere om personvernfremmende teknologier (Privacy Enhancing Technologies) kan brukes, minimere data til partnere og helst bruke ende-til-ende-kryptering [K39 s. 31–32].

### 7. Art. 25 i anskaffelser og databehandleravtaler

Praktiske krav å ta inn i kravspesifikasjon/kontrakt [K13 s. 2–5, 8–9; K39 s. 19, 45–47]:
- Leverandøren skal dokumentere hvordan løsningen ivaretar prinsippene og rettighetene (innebygd personvern), inkl. standardinnstillinger.
- Konfigurerbarhet: mulighet til å skru av funksjoner, styre lagringstid og automatisk sletting (også i backup), rollebasert tilgang, logging, eksport for innsyn/portabilitet.
- Leverandøren skal kartlegge hvordan funksjoner bruker personopplysninger (CRM-eksempelet) og varsle om nye funksjoner som behandler data på nye måter.
- Leverandøren skal holde behandlingsansvarlig orientert om «state of the art» og oppdatere tiltak; sikkerhetsoppdateringer skilles fra funksjonelle oppdateringer [K39 s. 36].
- Rett til revisjon og evaluering av databehandlerens tiltak med jevne mellomrom [K13 s. 2; K39 s. 36].
- Se [T07](T07-databehandleravtale-art28.md) og [M01](../maler/M01-databehandleravtale-sjekkliste.md).

### 8. Forholdet til DPIA og art. 32

- DPIA skal gjennomføres i samsvar med innebygd personvern (art. 25, fortalepunkt 78) og bør starte så tidlig som mulig i designet [K12 s. 2–3; K24 s. 14].
- Datatilsynets DPIA-sjekkliste spør eksplisitt: «Er programvaren utviklet med innebygd personvern og personvern som standardinnstilling? Ble det tatt valg for å øke personvernet – i tilfelle hvilke?» [K21 s. 4].
- Art. 32 dekker sikkerhet (K-I-T + robusthet); art. 25 dekker alle prinsippene. En løsning kan være sikker, men likevel bryte art. 25 (f.eks. samler for mye, mangler slettefunksjon, uklare innstillinger) [K40 § 4.2; K13 s. 3].
- Dokumentasjonen av art. 25-vurderingen (risikoanalyser, DPIA, PVO-synspunkter, sikkerhetstester) skal tas vare på [K13 s. 2].

### 9. Eldre systemer – GAP-analyse

Kravet gjelder også systemer utviklet før 2018 som fortsatt er i bruk [K13 s. 4]. Fremgangsmåte:
1. Bruk nøkkelelementtabellene (pkt. 5) eller SDM-målene som kravliste.
2. Vurder for hvert krav: oppfylt / delvis / ikke oppfylt, med dokumentasjon.
3. Identifiser tiltak for gap (konfigurasjon, sletterutiner, tilgangsrevisjon, informasjon, pseudonymisering).
4. Prioriter etter risiko for de registrerte; fastsett ansvar og frister.
5. Gjenta jevnlig [K13 s. 4].

### 10. Sertifisering og håndhevelse

- Sertifisering etter art. 42 kan brukes som element for å påvise etterlevelse; ved sertifisering av innebygd personvern er designprosessen særlig relevant (valg av midler, tiltak og forvaltning av dem, kontinuerlig vurdering). Mer informasjon «kommer fortløpende» [K13 s. 13].
- Datatilsynet kan føre tilsyn og ilegge gebyr eller pålegg; vurderingen av brudd på innebygd personvern er «et spesielt viktig moment» ved gebyrutmåling [K13 s. 14].

## Vanlige feil og fallgruver

- **Personvern vurderes etter at løsningen er valgt** – kravene kom ikke med i anbudet [K13 s. 7].
- **Hyllevare tas i bruk med leverandørens standardinnstillinger** (alle moduler, sporing og deling på) [K13 s. 5].
- **Forhåndsavkryssede bokser og skjeve valg** (stor «Godta»-knapp, skjult «Avslå») [K13 s. 5, 7].
- **Obligatoriske felt uten begrunnet nødvendighet** [K13 s. 9–10].
- **Sletting bare i primærsystemet**, ikke i backup, logger, e-post eller hos databehandler [K13 s. 5, 10–11].
- **Ingen evaluering av om tiltakene virker** (ingen KPI-er, ingen testing av sletting/anonymisering) [K13 s. 3, 10].
- **Produksjonsdata brukes i test** [K30 kap. 20].
- **Art. 25 forveksles med sikkerhet** – tiltak for åpenhet, ikke-kobling og intervenerbarhet mangler [K40 § 4.2; K37].
- **«For dyrt» brukes som begrunnelse** for ikke å gjøre noe [K13 s. 3].
- **Eldre systemer glemmes** [K13 s. 4].

## Sjekkliste

- [ ] Styringssystemet for utvikling/anskaffelse har krav om innebygd personvern; bestillerkompetanse finnes [K13 s. 2].
- [ ] Art. 25-krav er tatt inn i anbud, kravspesifikasjon og kontrakt/DPA [K13 s. 2].
- [ ] Formål og nødvendige data er fastsatt før design; hver datakategori er begrunnet [K13 s. 8–9].
- [ ] Standardinnstillinger er minst inngripende; ingen forhåndsavkrysning; unødvendige funksjoner avslått [K13 s. 5].
- [ ] Ingen dark patterns; samtykke/avslag er like synlige [K13 s. 7].
- [ ] Lagringstid fastsatt og begrunnet; automatisk sletting, også i backup/logger/hos databehandler; sletting/anonymisering testet [K13 s. 10–11].
- [ ] Tilgang etter tjenstlig behov, differensiert og revidert regelmessig [K13 s. 5, 11].
- [ ] Den registrerte kan påvirke tilgjengeliggjøring/publisering [K13 s. 5].
- [ ] Pseudonymisering/anonymisering/aggregering vurdert; PETs vurdert [K13 s. 9; K39 s. 31–32].
- [ ] Rettigheter kan utøves effektivt (innsyn, retting, sletting, portabilitet, innsigelse) [K13 s. 6–8].
- [ ] Algoritmer/KI: bias-testing, menneskelig inngripen, løpende overvåking [K13 s. 7, 10].
- [ ] Tiltak dekker alle beskyttelsesmål, ikke bare sikkerhet [K37].
- [ ] KPI-er for effektivitet definert og fulgt opp [K13 s. 3].
- [ ] Dokumentasjon (vurderinger, DPIA, PVO-råd, tester) tatt vare på [K13 s. 2].
- [ ] Eldre systemer: GAP-analyse gjennomført [K13 s. 4].

## Se også

- Maler: [M04 DPIA-mal](../maler/M04-dpia-mal.md), [M09 Sikkerhetstiltak](../maler/M09-sikkerhetstiltak-sjekkliste.md), [M01 DPA-sjekkliste](../maler/M01-databehandleravtale-sjekkliste.md)
- Arbeidsflyter: [A02 Gjennomføre DPIA](../arbeidsflyter/A02-gjennomfore-dpia.md), [A01 Gjennomgå databehandleravtale](../arbeidsflyter/A01-gjennomga-databehandleravtale.md), [A03 Risikovurdering](../arbeidsflyter/A03-risikovurdering-informasjonssikkerhet.md)
- Temaer: [T03 Grunnprinsipper](T03-grunnprinsipper-art5.md), [T05 Rettigheter](T05-de-registrertes-rettigheter.md), [T07 Databehandleravtale](T07-databehandleravtale-art28.md), [T08 Informasjonssikkerhet](T08-informasjonssikkerhet-art32.md), [T10 DPIA](T10-dpia-art35-36.md)
- Kilder: [K13](../kilder/K13-dt-innebygd-personvern.md), [K09](../kilder/K09-dt-grunnleggende-prinsipper.md), [K37](../kilder/K37-sdm-standard-datavernmodell.md), [K40](../kilder/K40-dpia-prosess-uld.md), [K39](../kilder/K39-cnil-mobilapper.md), [K30](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K33](../kilder/K33-cnil-sikkerhetsguide.md)

---
id: A02
tittel: "Arbeidsflyt: Gjennomføre (eller kvalitetssikre) en DPIA"
gdpr_artikler: [5, 6, 9, 25, 28, 30, 32, 35, 36, 39]
kilder: [K12, K20, K21, K22, K24, K28, K29, K30, K31, K37, K40, K14, K38]
---

# Arbeidsflyt: Gjennomføre (eller kvalitetssikre) en DPIA

## Når brukes

- Brukeren planlegger en ny behandling, et nytt system eller en vesentlig endring, og spør om DPIA er nødvendig eller ber om hjelp til å lage en.
- Brukeren vil ha en eksisterende DPIA gjennomgått/kvalitetssikret (bruk steg 1–2 for å forstå behandlingen, deretter kvalitetskontrollen og Vedlegg A i [M04](../maler/M04-dpia-mal.md)).
- En databehandleravtale-gjennomgang ([A01](A01-gjennomga-databehandleravtale.md)) eller risikovurdering ([A03](A03-risikovurdering-informasjonssikkerhet.md)) avdekker høy risiko.
- En tidligere DPIA må revideres pga. endringer (nytt formål, nye data, nye mottakere/leverandører, ny teknologi, nye overføringer, avvik) [K24 s. 13–14].

Fagstoff: [T10](../temaer/T10-dpia-art35-36.md). Maler: [M05](../maler/M05-dpia-terskelvurdering.md) (screening), [M04](../maler/M04-dpia-mal.md) (DPIA).

## Input agenten trenger fra brukeren

Still spørsmålene i bolker; ikke alt trengs før man kan starte. Merk hva som er ukjent og må avklares.

**Om behandlingen**
1. Hva skal gjøres, og hvorfor (formål og forventede fordeler)? Ny behandling eller endring?
2. Hvem er de registrerte (ansatte, kunder, barn, pasienter, elever, innbyggere)? Omtrent hvor mange?
3. Hvilke opplysninger (liste variabler), og er det særlige kategorier, straffedommer, fødselsnummer, lokasjon, kommunikasjon, økonomi?
4. Hvor kommer opplysningene fra, og hvem får tilgang/utlevering?
5. Hvilken teknologi/løsning brukes? Hyllevare eller egenutviklet? Leverandør? Brukes KI, profilering eller automatiserte avgjørelser?
6. Lagringstid og sletting?
7. Behandles data, eller gis support/fjerntilgang, utenfor EØS?

**Om ansvar og organisering**
8. Hvem er behandlingsansvarlig? Er det felles behandlingsansvar? Hvilke databehandlere/underleverandører?
9. Finnes protokoll (art. 30), behandlingsgrunnlag og sikkerhetsrisikovurdering (art. 32) allerede?
10. Har virksomheten personvernombud? Hvem er beslutningstaker (ledelse)?
11. Er det tillitsvalgte, brukerråd eller andre representanter for de registrerte?

**Dokumenter å be om:** protokollutdrag, systembeskrivelse/arkitektur, dataflytdiagram, databehandleravtaler og underleverandørlister, sikkerhetsdokumentasjon (ISO-sertifikater, pentest), tidligere DPIA/risikovurderinger, personvernerklæring, ev. leverandørens egen DPIA.

## Steg

1. **Avklar lovlighet først.** Kontroller at formål og behandlingsgrunnlag ([art. 6](../kilder/K43-gdpr-kap02-prinsipper.md#art-6), ev. [9](../kilder/K43-gdpr-kap02-prinsipper.md#art-9)/[10](../kilder/K43-gdpr-kap02-prinsipper.md#art-10)) er på plass. Mangler det, gå til [A06](A06-vurdere-behandlingsgrunnlag.md) – en DPIA reparerer ikke en ulovlig behandling [K12 s. 1; K40 § 4.2]. *(Tema: [T02](../temaer/T02-behandlingsgrunnlag-og-samtykke.md).)*

2. **Terskelvurdering (screening).** Fyll ut [M05](../maler/M05-dpia-terskelvurdering.md):
   - unntak (lik behandling med DPIA, tidligere konsesjon, art. 35 nr. 10) [K24 s. 12–13; K12 s. 2];
   - art. 35 nr. 3 a–c (ordlyd: [art. 35](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-35));
   - Datatilsynets 14 punkter (husk tilleggskriterium for pkt. 1–4, 6, 7) [K20];
   - de ni WP29-kriteriene, vurdert uavhengig av tiltak [K24 s. 9–11];
   - kalibrer mot eksempeltabellen [K22].
   Konklusjon: ≥ 2 kriterier eller listetreff → DPIA; 1 kriterium eller tvil → anbefal DPIA [K12 s. 2; K24 s. 8]. Ved «nei» tross treff: dokumenter begrunnelse og PVOs syn [K24 s. 12] – og avslutt med henvisning til art. 32-vurdering ([A03](A03-risikovurdering-informasjonssikkerhet.md)).

3. **Planlegg DPIA-en.** Avklar omfang (én behandling eller flere like [K24 s. 7]), team (fagansvarlig, PVO, CISO/IT, jurist, databehandler) og RACI [K28 s. 9; K12 s. 3], tidsplan (før oppstart, tidlig i design [K24 s. 14]), metode og skalaer (standard: M04 med CNIL-skalaer; alternativt virksomhetens egne, se [T09](../temaer/T09-risikovurdering-metoder-og-skalaer.md)). Be databehandler(e) om bistand etter [art. 28 nr. 3 f](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-28) [K24 s. 15; K05]. Avgjør hvordan de registrertes syn skal innhentes (steg 9).

4. **Del 1 – Systematisk beskrivelse.** Fyll ut M04 del 1: oversikt, roller, art/omfang/formål/sammenheng, datakategorier med mottakere og lagringstid, dataflyt og støtteressurser for hele livssyklusen, databehandlere, overføringer, standarder/atferdsnormer, andre rettslige krav [K21 s. 2–5; K29 s. 4; K24 Annex 2]. Ta med data som genereres av tiltakene selv (logger, samtykkeregistrering) [K28 s. 11]. **Få PVO til å lese gjennom del 1** før dere går videre [K31 s. 5].

5. **Overføringer.** Er det overføring ut av EØS (inkl. support/fjerntilgang, leverandør underlagt tredjelands lov)? Kjør [A04](A04-overforing-og-tia.md) og legg TIA ([M06](../maler/M06-tia-mal.md)) ved DPIA-en [K21 s. 3–4; K14 s. 9–10].

6. **Del 2 – Nødvendighet og proporsjonalitet.** Fyll ut M04 del 2: grunnlag (også for utlevering), formålsbegrensning og mindre inngripende alternativer, **minimering per variabel**, riktighet, lagringstid per datatype, alle rettigheter i art. 12–22, EMK-friheter, databehandlere og overføringer. Avslutt med vurderingstabellen (akseptabelt / kan forbedres) og før korrigerende tiltak inn i handlingsplanen [K21 s. 6–7; K29 s. 5–12]. Bruk art. 25-kravene som kontroll ([T13](../temaer/T13-innebygd-personvern-art25.md)).

7. **Del 3 – Risikovurdering.**
   - Kartlegg risikokilder (inkl. interne, databehandlere, myndigheter, virksomheten selv) [K31 vedlegg 2; K40 § 4.2].
   - (A) Rettighetsrisikoer: gå gjennom Datatilsynets liste (grunnlag, rettferdighet, åpenhet, overinnsamling, riktighet, lagring, informert valg, innsyn, retting/sletting, portabilitet, profilering, diskriminering, ytrings-/religionsfrihet) og perspektivene medbestemmelse/åpenhet/forutsigbarhet [K12 s. 5–6; K21 s. 8].
   - (B) Sikkerhetsrisikoer: uautorisert tilgang, uønsket endring, forsvinning – med trusler, konsekvenser, eksisterende tiltak [K29 s. 20; K28 s. 14–15]. Kan bygge på art. 32-vurderingen ([M03](../maler/M03-risikovurdering-mal.md)).
   - Sett alvorlighet og sannsynlighet med skriftlig begrunnelse; plasser i risikokart (initial) [K28 s. 15; K29 s. 23].

8. **Del 4 – Tiltak og restrisiko.** Foreslå tiltak i alle fire kategorier (garantier, dataspesifikke sikkerhetstiltak, generelle sikkerhetstiltak, organisatoriske) i rekkefølgen styring → data → konsekvenser → kilder → støtteressurser [K21 s. 9; K28 s. 13]. Kontroller at tiltakene også dekker dataminimering, ikke-kobling, åpenhet og intervenerbarhet (SDM) [K37; K40]. Vurder om behandlingen bør endres i stedet for å legge på sikkerhetstiltak [K12 s. 5]. Beregn restrisiko og sammenlign med målene for risikobehandling [K31 vedlegg 6]. Tiltakskataloger: [K30](../kilder/K30-cnil-pia-kunnskapsbaser.md), [M09](../maler/M09-sikkerhetstiltak-sjekkliste.md).

9. **Involver interessenter.**
   - **De registrerte:** innhent synspunkter dersom det er relevant (art. 35 nr. 9; undersøkelse, tillitsvalgte/verneombud, brukerpanel); sørg for behandlingsgrunnlag; dokumenter hvordan de er fulgt opp, eller hvorfor de ikke er innhentet. Samtykke er ikke en tilbakemelding [K24 s. 15; K12 s. 3].
   - **PVO:** innhent skriftlig råd på den (nesten) ferdige DPIA-en; dokumenter om rådet følges og hvorfor ikke [K24 s. 14; K29 s. 24].

10. **Del 5 – Handlingsplan.** Alle korrigerende og nye tiltak med ansvarlig, kostnad, frist, vanskelighetsgrad, målekriterium og status [K21 s. 10; K31 s. 36; K40 § 4.3].

11. **Del 7 – Sammenstilling og ledelsens validering.** Lag sammendrag (M04 del 1 og 7.1) med risikokart før/etter, status for prinsipper og sikkerhet, handlingsplan, PVO-råd og registrertes syn. Ledelsen beslutter: godkjent / betinget (revidert DPIA tilbake) / avvist [K21 s. 10; K31 s. 38]. Bruk valideringsteksten i M04.

12. **Forhåndsdrøfting ved høy restrisiko.** Er restrisikoen fortsatt høy (betydelige/irreversible konsekvenser og/eller åpenbart at risikoen inntreffer [K24 s. 19]), eller har DPIA-en vært i ledelsen mer enn én gang uten at risikoen er redusert og viljen er stor [K21 s. 10]: be Datatilsynet om forhåndsdrøfting **før** behandlingen starter. Viser DPIA-en høy risiko som ikke reduseres med tiltak, er dette en plikt etter [art. 36 nr. 1](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-36), ikke et valg. Send hele DPIA-en og de fem dokumentasjonspunktene (kontaktinfo inkl. PVO; beskrivelse med fokus på høy risiko; nødvendighet/proporsjonalitet; risiko og tiltak – også vurderte men ikke gjennomførte; ledelsens validering), sikkert (TLS/PGP) [K12 s. 11]. Det lovpålagte innholdet står i [art. 36 nr. 3](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-36) a–f. Veiledningsønsker er ikke forhåndsdrøfting [K12 s. 11]. Mener tilsynet at behandlingen vil være i strid med forordningen, har det etter [art. 36 nr. 2](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-36) inntil åtte uker (kan forlenges med seks) til å gi skriftlig råd.

13. **Oppfølging.** Registrer DPIA-en (referanse i protokollen), fastsett revisjonsdato og utløsende hendelser, følg opp handlingsplanen, og kontroller at behandlingen skjer i tråd med DPIA-en ([art. 35 nr. 11](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-35)) [K24 s. 14, 17; K28 s. 7]. Vurder publisering av sammendrag [K24 s. 18].

## Output

- Utfylt terskelvurdering ([M05](../maler/M05-dpia-terskelvurdering.md)) – også ved «nei».
- Utfylt DPIA ([M04](../maler/M04-dpia-mal.md)) med risikokart før/etter, handlingsplan, PVO-råd, registrertes syn og ledelsens beslutning.
- Ved behov: TIA ([M06](../maler/M06-tia-mal.md)), interesseavveining ([M08](../maler/M08-interesseavveining-mal.md)), sikkerhetsrisikovurdering ([M03](../maler/M03-risikovurdering-mal.md)).
- Ved høy restrisiko: utkast til anmodning om forhåndsdrøfting.
- Kort sammendrag til ledelsen og forslag til eventuell offentlig versjon.
- Liste over åpne spørsmål og antakelser agenten har gjort.

## Kvalitetskontroll

- [ ] Alle punkter i WP248 Annex 2 er dekket (M04 vedlegg A) [K24 s. 22].
- [ ] Alle fire faser i Datatilsynets sjekkliste er dekket, inkl. ledelsens beslutning [K21].
- [ ] Ingen tomme felt – alt er utfylt eller merket «ikke relevant» med begrunnelse [K29 s. 2].
- [ ] Nødvendighet er begrunnet per variabel; alternativer (anonymt/pseudonymt/mindre inngripende) er vurdert [K21 s. 6].
- [ ] Risikovurderingen tar de registrertes perspektiv og omfatter rettighetsrisikoer, ikke bare informasjonssikkerhet [K12 s. 5; K24 s. 17].
- [ ] Hvert estimat av alvorlighet/sannsynlighet er begrunnet [K28 s. 14–15].
- [ ] Tiltakene er konkrete, har eier og frist, og dekker alle beskyttelsesmål [K37].
- [ ] Restrisiko er angitt for hver risiko; høy restrisiko har ført til forhåndsdrøfting [K24 s. 19].
- [ ] PVO-råd og registrertes syn er dokumentert, inkl. begrunnelser for avvik [K24 s. 14–15].
- [ ] Databehandleravtalen forplikter til bistand med DPIA [K05].
- [ ] Overføringer har TIA eller dokumentert adekvans/art. 49 [K14].
- [ ] Revisjonsdato er satt [K28 s. 7].
- [ ] Alle påstander som ikke bygger på kildene er merket, og usikker faktainformasjon (f.eks. adekvansstatus) er markert for verifisering.

## Når skal det eskaleres til jurist/personvernombud

- **Alltid til PVO** før ledelsens beslutning (art. 35 nr. 2) – og når screeningen konkluderer med «ikke DPIA» tross treff på kriterier [K24 s. 12, 14].
- Usikkert eller manglende behandlingsgrunnlag, særlig for særlige kategorier, art. 10, forskning uten samtykke, eller offentlig myndighetsutøvelse uten klar hjemmel → jurist.
- Art. 35 nr. 10-unntaket påberopes → jurist.
- Profilering/automatiserte avgjørelser med rettsvirkning (art. 22), overvåking av ansatte, kamera i skole/barnehage, barn, biometri, KI-trening på sensitive data → jurist og PVO.
- Høy restrisiko eller tvil om forhåndsdrøfting → PVO, jurist og ledelse.
- Overføring til tredjeland der TIA gir konklusjon (2) eller (3) → jurist (se [A04](A04-overforing-og-tia.md)).
- Felles behandlingsansvar eller uklare roller → jurist ([T01](../temaer/T01-roller-behandlingsansvarlig-databehandler.md)).
- Konflikt mellom PVOs råd og ledelsens ønske → dokumenter og løft til ledelsen.
- Sektorregelverk (helse, skole, NAV, finans, ekom) som kan stille egne krav → jurist.

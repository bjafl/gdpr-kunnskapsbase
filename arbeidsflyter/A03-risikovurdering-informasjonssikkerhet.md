---
id: A03
tittel: "Arbeidsflyt – gjennomføre risikovurdering av informasjonssikkerhet (art. 32)"
gdpr_artikler: [24, 25, 28, 32, 35, 36]
kilder: [K17, K18, K19, K28, K30, K31, K32, K33, K37, K40, K12, K21, K23, K05]
---

# Arbeidsflyt – gjennomføre risikovurdering av informasjonssikkerhet (art. 32)

## Når brukes

- Før en ny behandling, et nytt system eller en ny leverandør tas i bruk – [art. 32](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-32)-vurdering skal **alltid** gjøres før behandlingen starter [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md).
- Ved vesentlige endringer i system, formål, data, leverandører, overføringer eller trusselbilde, og ved periodisk revisjon (minst årlig) [K30 kap. 21](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K28 s. 7](../kilder/K28-cnil-pia-metode.md), [K24](../kilder/K24-wp248-dpia.md).
- Som risikodel i en DPIA ([A02](A02-gjennomfore-dpia.md)) – da brukes denne arbeidsflyten for steg 4–9, og resultatet føres inn i [M04](../maler/M04-dpia-mal.md).
- Ved gjennomgang av en databehandler ([A01](A01-gjennomga-databehandleravtale.md)) når leverandørens sikkerhet skal vurderes opp mot risikoen for de registrerte.
- Etter et sikkerhetsbrudd, som del av læringen [K32 4.4.2](../kilder/K32-nsm-grunnprinsipper.md), jf. [A05](A05-avvikshandtering.md).

**Ikke** når spørsmålet bare er *om* DPIA kreves – bruk [A02](A02-gjennomfore-dpia.md)/[T10](../temaer/T10-dpia-art35-36.md) først.

## Input agenten trenger fra brukeren

Still spørsmålene i blokker; marker hva som er ukjent i stedet for å gjette.

**Kontekst**
1. Hvilken behandling/hvilket system skal vurderes, og hva er formålet med vurderingen (ny behandling, endring, leverandørvalg, årlig revisjon, DPIA)?
2. Hvem er behandlingsansvarlig, og hvilke databehandlere/underdatabehandlere er involvert (tjeneste, land)?
3. Hva er behandlingsgrunnlaget? (Må være avklart – ellers eskaler, se nedenfor.)
4. Hvem er risikoeier, og hvem kan akseptere risiko på hvilket nivå? Finnes vedtatte akseptkriterier og skalaer?

**Data og registrerte**
5. Hvilke kategorier personopplysninger (særlige kategorier, fødselsnummer, økonomi, lokasjon, barn)? Omtrentlig antall registrerte og poster?
6. Er de registrerte avhengige av virksomheten (ansatte, pasienter, mottakere av ytelser)? Sårbare grupper?
7. Lagringstid og slettemekanisme?

**Teknisk og organisatorisk**
8. Systemarkitektur og dataflyt: hvor lagres data, hvilke integrasjoner, eksponering mot internett, tilgang hjemmefra/mobilt?
9. Hvilke sikkerhetstiltak finnes i dag? (Be om policy, sertifikater med scope, pentestrapporter, backuprutiner, loggoppsett – eller gå gjennom [M09](../maler/M09-sikkerhetstiltak-sjekkliste.md) sammen med brukeren.)
10. Tidligere hendelser/avvik, revisjonsfunn eller kjente sårbarheter?
11. Overføringer eller tilgang fra land utenfor EØS?

**Organisering**
12. Hvem deltar i arbeidsgruppen (fag, IT, sikkerhet, personvernombud, leverandør)? Tidsramme?

## Steg

1. **Avklar mandat, omfang og metode.**
   Skriv ned formål, omfang, avgrensninger, deltakere og styrende dokumenter (risikonotatets innledning) [K17 trinn 1](../kilder/K17-digdir-gjennomfore-risikovurdering.md). Velg metode etter tabellen i [T09 avsnitt 6](../temaer/T09-risikovurdering-metoder-og-skalaer.md): standard er Digdir 5-nivå med personvernkategori operasjonalisert med CNIL-beskrivelser ([M03](../maler/M03-risikovurdering-mal.md) kap. 4); for DPIA etter CNIL-mal brukes alternativet i M03 vedlegg A.
   → Fyll [M03](../maler/M03-risikovurdering-mal.md) kap. 0–1.

2. **Fastsett skalaer og akseptkriterier før analysen.**
   Bruk virksomhetens vedtatte kriterier; mangler de, bruk M03 kap. 4 (basert på [K18 vedlegg B–E](../kilder/K18-digdir-retningslinje-risiko.md)) og få risikoeier til å godkjenne dem. Skalaene skal ikke justeres underveis [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md). Påse at det finnes en konsekvensskala for **den registrerte** i tillegg til virksomheten [T09 avsnitt 1](../temaer/T09-risikovurdering-metoder-og-skalaer.md).

3. **Kartlegg verdier, støtteressurser og dataflyt; fastsett beskyttelsesnivå.**
   List informasjonstyper med K-I-T-behov, støtteressurser (maskinvare, programvare, kanaler, personer, papir, lokaler) og dataflyt [K30 §1.1–1.2](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K32 1.1.5–1.1.6](../kilder/K32-nsm-grunnprinsipper.md). Ta med logger og andre data tiltakene selv genererer [K28 s. 11](../kilder/K28-cnil-pia-metode.md). Fastsett SDM-beskyttelsesnivå (normal/høy/svært høy) og vurder kumulative effekter [K37 9.3–9.5](../kilder/K37-sdm-standard-datavernmodell.md).
   → M03 kap. 1.4, 2.

4. **Kartlegg eksisterende tiltak (grunnsikring).**
   Gå gjennom [M09](../maler/M09-sikkerhetstiltak-sjekkliste.md) gruppe A–R. For leverandører: be om dokumentasjon for gruppe K (NSM 2.1.10 a–j) [K32 2.1.10](../kilder/K32-nsm-grunnprinsipper.md) og CNIL ark 14/22 [K33](../kilder/K33-cnil-sikkerhetsguide.md). Noter for hvert tiltak om effekten er dokumentert – å ha et tiltak er ikke nok [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md).
   → M09 utfylt; M03 kap. 6.

5. **Identifiser risikokilder og uønskede hendelser.**
   Kartlegg risikokilder inkl. interne/legitime brukere, leverandører, virksomheten selv (formålsglidning) og ikke-menneskelige kilder [K30 §1.3](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K37 9.6](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md). Gjennomfør idédugnad i runder [K17 trinn 3](../kilder/K17-digdir-gjennomfore-risikovurdering.md) og kontroller mot trusselkatalogene per støtteressurs (observert, brukt upassende, endret, skadet, mistet, overbelastet) [K30 §1.7–1.9](../kilder/K30-cnil-pia-kunnskapsbaser.md). Dekk alle tre fryktede hendelser (uautorisert tilgang, uønsket endring, forsvinning) [K28 s. 14](../kilder/K28-cnil-pia-metode.md) **og** personvernmålene (dataminimering, ikke-kobling, åpenhet, intervenerbarhet) [K37 kap. 5](../kilder/K37-sdm-standard-datavernmodell.md). Formuler hver risiko tredelt (hendelse – brudd – konsekvens) og grovsorter A–D [K17 trinn 3](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
   → M03 kap. 3, 5.

6. **Analyser risikoene.**
   Ta risikoene i prioritert rekkefølge. For hver: estimer konsekvens for den registrerte og for virksomheten, tilhørende sannsynlighet (aldri høyere enn sannsynligheten for selve bruddet), og slå opp risikonivået i matrisen; velg den kombinasjonen som gir **høyest** risikonivå [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 vedlegg G](../kilder/K18-digdir-retningslinje-risiko.md). Bruk justeringsfaktorene for alvorlighet og sannsynlighet [K30 §1.5–1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md) og de tre sannsynlighetsfaktorene i sammenheng [K18 vedlegg H](../kilder/K18-digdir-retningslinje-risiko.md). Begrunn hvert estimat skriftlig [K28 s. 14–15](../kilder/K28-cnil-pia-metode.md).
   → M03 kap. 7 og matrise 7.1.

7. **Evaluer mot akseptkriteriene.**
   Marker «Kan aksepteres»/«Ikke akseptabel» per risiko [K17 trinn 5](../kilder/K17-digdir-gjennomfore-risikovurdering.md). Bruk GDPR-gulvet: høy alvorlighet for de registrerte aksepteres bare når sannsynligheten er ubetydelig [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md); høy restrisiko for de registrerte vurderes mot [art. 36](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-36) [K23](../kilder/K23-cnil-risikoark.md).
   → M03 kap. 7 siste kolonne.

8. **Foreslå tiltak og lag tiltaksplan.**
   Vurder først å **unngå** risikoen (mindre data, annen arbeidsmåte) [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md). Velg tiltak i rekkefølgen styring → data → konsekvenser → risikokilder → støtteressurser [K28 s. 13](../kilder/K28-cnil-pia-metode.md), hent konkrete tiltak fra [T08](../temaer/T08-informasjonssikkerhet-art32.md) (kryssreferansetabellen NSM ↔ CNIL ↔ SDM) og M09, og vurder nytte/kost og sideeffekter [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md), [K19](../kilder/K19-digdir-risikovurderingsverktoy.md). Sjekk at tiltakene samlet dekker alle sju SDM-mål [K37](../kilder/K37-sdm-standard-datavernmodell.md). Angi ansvar, frist, kostnad, vanskelighetsgrad og målekriterier [K30 §1.10](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K40 § 4.3](../kilder/K40-dpia-prosess-uld.md).
   → M03 kap. 8.

9. **Beregn restrisiko og konkluder om personvernkonsekvenser.**
   Estimer konsekvens og sannsynlighet etter tiltak og plott i matrise [K19](../kilder/K19-digdir-risikovurderingsverktoy.md). Besvar M03 kap. 10: DPIA-plikt ([art. 35](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-35))? Forhåndsdrøfting ([art. 36](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-36))? Oppdatering av databehandleravtale/sikkerhetsvedlegg ([M01](../maler/M01-databehandleravtale-sjekkliste.md), [K05](../kilder/K05-dt-databehandleravtale.md)) og protokoll [K12 s. 9](../kilder/K12-dt-dpia-veiledning.md)?
   → M03 kap. 9–10.

10. **Beskriv kvalitet og kunnskapsstyrke.**
    Angi tidsbruk, tilpasninger, hva som kunne vært grundigere, og kunnskapsstyrke (svak/middels/sterk), særlig for avvikende risikoer [K17 trinn 6](../kilder/K17-digdir-gjennomfore-risikovurdering.md). Før uanalyserte risikoer i restlisten [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
    → M03 kap. 11.

11. **Innhent råd og beslutning.**
    Presenter risikonotat (kort sammendrag), risikotabell og matriser for personvernombudet (råd) og risikoeier/ledelse (beslutning) på riktig nivå [K18 vedlegg B, kap. 5](../kilder/K18-digdir-retningslinje-risiko.md). Nye systemer tas som hovedregel ikke i bruk før valgte tiltak er gjennomført; for eksisterende systemer vurderes midlertidige tiltak eller stans [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md).
    → M03 kap. 12.

12. **Følg opp og planlegg revisjon.**
    Legg tiltakene inn i virksomhetens handlingsplan med oppfølging [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md). Sett dato for neste revisjon (minst årlig og ved endringer) [K30 kap. 21](../kilder/K30-cnil-pia-kunnskapsbaser.md). Sørg for at tiltak for regelmessig testing (pentest, gjenopprettingstest, tilgangsgjennomgang) er planlagt [K32 3.4, 2.9.3](../kilder/K32-nsm-grunnprinsipper.md), [K33 ark 5](../kilder/K33-cnil-sikkerhetsguide.md).

## Output

1. **Utfylt [M03](../maler/M03-risikovurdering-mal.md)**: risikonotat (kap. 0–1, 11–12), risikotabell før og etter tiltak, risikomatriser, tiltaksplan, restliste.
2. **Utfylt [M09](../maler/M09-sikkerhetstiltak-sjekkliste.md)** med avviksliste.
3. **Kort sammendrag til beslutningstaker** (maks én side): samlet risikonivå, høyeste risikoer for de registrerte og for virksomheten, nødvendige tiltak med frister, restrisiko som skal aksepteres og av hvem, og om DPIA/forhåndsdrøfting eller endring av DPA er nødvendig.
4. Ved leverandørvurdering: **liste over krav** som må inn i databehandleravtalen/sikkerhetsvedlegget før signering.

## Kvalitetskontroll

Agenten skal kontrollere at:
- [ ] Formål, omfang, deltakere og metode er dokumentert, og skalaer/akseptkriterier ble fastsatt **før** analysen [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md).
- [ ] Konsekvenser er vurdert for **de registrerte**, ikke bare for virksomheten [K33 ark 20 s. 49](../kilder/K33-cnil-sikkerhetsguide.md), [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md).
- [ ] Alle tre fryktede hendelser og alle relevante støtteressurser (inkl. papir, personer, leverandører, logger) er dekket [K28](../kilder/K28-cnil-pia-metode.md), [K30 §1.2](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- [ ] Personvernmålene (dataminimering, ikke-kobling, åpenhet, intervenerbarhet) er vurdert, ikke bare K-I-T [K37](../kilder/K37-sdm-standard-datavernmodell.md), [K40](../kilder/K40-dpia-prosess-uld.md).
- [ ] Hver risiko har tredelt beskrivelse, begrunnede estimater og risikonivå fra matrisen (ikke produkt) [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K19](../kilder/K19-digdir-risikovurderingsverktoy.md).
- [ ] Det verste relevante utfallet er vurdert, og tilhørende sannsynlighet er ikke høyere enn innledende [K18 vedlegg G](../kilder/K18-digdir-retningslinje-risiko.md).
- [ ] Eksisterende tiltak er dokumentert med bevis, ikke bare påstått [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md).
- [ ] Tiltaksplanen har ansvar, frist og målekriterier, og tiltakenes sideeffekter er vurdert [K40 § 4.3](../kilder/K40-dpia-prosess-uld.md), [K19](../kilder/K19-digdir-risikovurderingsverktoy.md).
- [ ] Restrisiko er beregnet og akseptert av riktig ledernivå [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md).
- [ ] Høy restrisiko for de registrerte er vurdert opp mot DPIA og art. 36 [K23](../kilder/K23-cnil-risikoark.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md).
- [ ] Kunnskapsstyrke og restliste er angitt [K17 trinn 6](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
- [ ] Alle påstander i rapporten som ikke bygger på kildene, er merket som vurderinger.
- [ ] Neste revisjonsdato er satt.

## Når skal det eskaleres til jurist/personvernombud

- **Behandlingsgrunnlag, formål eller nødvendighet er uavklart** – risikovurderingen kan ikke kompensere for mangler i grunnprinsippene [K28 s. 4](../kilder/K28-cnil-pia-metode.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md). Se [T02](../temaer/T02-behandlingsgrunnlag-og-samtykke.md).
- **Restrisiko «Høy» eller «Svært høy» i personvernkategorien**, eller CNIL-alvorlighet 3–4 med sannsynlighet over ubetydelig – personvernombudet skal gi råd; vurder DPIA og forhåndsdrøfting (art. 36) [K23](../kilder/K23-cnil-risikoark.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md), [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md).
- **Resultatet tilsier at DPIA er påkrevd** og ikke er gjennomført ([T10](../temaer/T10-dpia-art35-36.md)).
- **Særlige kategorier, barn, sårbare grupper, systematisk overvåking eller storskala profilering** inngår.
- **Overføring eller tilgang fra tredjeland**, eller leverandør som forbeholder seg tilgang for egne formål – overføringsvurdering ([T11](../temaer/T11-overforing-tredjeland-og-tia.md)) og avtalespørsmål ([T07](../temaer/T07-databehandleravtale-art28.md)).
- **Leverandøren nekter revisjon, dokumentasjon eller sentrale sikkerhetskrav** (gruppe K i M09), eller avtalen gir ikke tilstrekkelige garantier etter art. 28 [K05](../kilder/K05-dt-databehandleravtale.md).
- **Konflikt mellom sikkerhetstiltak og personvern**, f.eks. omfattende logging eller overvåking av ansatte – krever særskilt begrunnelse og ev. arbeidsrettslig vurdering [K37 9.4](../kilder/K37-sdm-standard-datavernmodell.md), [K32 s. 39](../kilder/K32-nsm-grunnprinsipper.md).
- **Pågående eller nylig sikkerhetsbrudd** avdekkes under vurderingen – start [A05](A05-avvikshandtering.md) umiddelbart (72-timersfristen, [art. 33](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33)) [K33 ark 19](../kilder/K33-cnil-sikkerhetsguide.md).
- **Ledelsen vil akseptere en risiko over sitt akseptnivå**, eller ønsker å starte behandlingen før nødvendige tiltak er på plass [K18 kap. 4–5](../kilder/K18-digdir-retningslinje-risiko.md).

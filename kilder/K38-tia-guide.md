---
id: K38
tittel: "Practical Guide – Transfer Impact Assessment (final version)"
utgiver: CNIL (Commission nationale de l'informatique et des libertés, Frankrike)
dato: "Januar 2025 (final version)"
spraak: en
fil: "ressurser/guide_tia.pdf"
type: metode
gdpr_artikler: [4, 5, 6, 9, 10, 13, 14, 23, 28, 44, 45, 46, 47, 49, 87]
emner: [overføring, tredjeland, tia, schrems-ii, scc, bcr, supplerende-tiltak, databehandler, underdatabehandler]
relevans: høy
---

# Practical Guide – Transfer Impact Assessment (CNIL, 2025)

## Sammendrag

Praktisk veileder fra den franske tilsynsmyndigheten CNIL (28 sider, endelig versjon januar 2025) for eksportører som skal gjennomføre en vurdering av overføringskonsekvenser (Transfer Impact Assessment, TIA). Dokumentet sier selv at «the CNIL has developed this guide for exporters, to help them carry out their TIA» (s. 4). Veilederen bygger på Schrems II-dommen (C-311/18) og EDPBs anbefalinger 01/2020 om supplerende tiltak, og følger EDPBs seks steg. Den består av (1) forutgående kontroller før en TIA (finnes det en overføring, kreves TIA, hvem har ansvaret, omfang/videreoverføringer, samsvar med GDPR-prinsippene) og (2) seks steg med utfyllbare tabeller: kjenn overføringen, identifiser overføringsgrunnlaget, vurder lovgivning og praksis i tredjelandet (inkl. «European Essential Guarantees»), identifiser supplerende tiltak (tekniske, organisatoriske, kontraktuelle), handlingsplan for gjennomføring, og periodisk revurdering. Veilederen er ikke obligatorisk og inneholder ingen vurdering av konkrete land (s. 4). Notatet gjengir tabellene fullstendig slik at det kan brukes direkte som mal for TIA.

## Når skal agenten bruke denne kilden

- Når en behandlingsansvarlig eller databehandler skal overføre personopplysninger til land utenfor EØS på grunnlag av et art. 46-verktøy (standardavtaler/SCC, BCR, atferdsnorm, sertifisering, ad hoc-klausuler) og trenger en TIA.
- Når brukeren spør om TIA i det hele tatt er nødvendig (adekvansbeslutning, art. 49-unntak, intern fjerntilgang).
- Ved gjennomgang av databehandleravtaler der leverandøren bruker underdatabehandlere utenfor EØS (hvem skal lage TIA, hva behandlingsansvarlig må kontrollere).
- Ved valg av supplerende tiltak (pseudonymisering, kryptering, kontraktuelle forpliktelser, organisatoriske rutiner for innsynsbegjæringer fra myndigheter).
- Ved oppfølging/revurdering av eksisterende overføringer.
- Som utgangspunkt for maler i `maler/` (TIA-mal) og arbeidsflyt for overføringer.

## Hovedinnhold

### 1. Innledning (s. 3–5)

**1.1 Bakgrunn (s. 3).** Mange behandlingsansvarlige og databehandlere, uansett størrelse og sektor, berøres av overføringer ut av EØS, særlig pga. skytjenester. Hovedprinsippet: ved overføring skal opplysningene fortsatt ha et beskyttelsesnivå som i det vesentlige tilsvarer (essentially equivalent) GDPR. Fortalepunkt 101 siteres. I Schrems II understreket EU-domstolen eksportørens og importørens ansvar for at behandlingen er og forblir i samsvar med EU-nivået, og at eksportøren må suspendere overføringen og/eller si opp kontrakten hvis importøren ikke (lenger) kan overholde forpliktelsene. Eksportører som bruker art. 46-verktøy har derfor plikt til å vurdere beskyttelsesnivået i tredjelandet og behovet for supplerende tiltak – dette kalles TIA.

Definisjon av «eksportør» (EDPB, fotnote 4): behandlingsansvarlig, felles behandlingsansvarlig eller databehandler som er underlagt GDPR for behandlingen, og som ved overføring eller på annen måte gjør personopplysningene tilgjengelige for en «importør» (behandlingsansvarlig, felles behandlingsansvarlig eller databehandler) i et tredjeland, uavhengig av om importøren selv er underlagt GDPR etter art. 3, eller en internasjonal organisasjon (EDPB Guidelines 05/2021).

**1.2 Formålet med TIA (s. 3–4).**
- TIA skal gjennomføres av eksportøren (som behandlingsansvarlig eller databehandler), **med bistand fra importøren**, **før** overføring til tredjeland når overføringen bygger på et **art. 46-verktøy**.
- Ikke påkrevd ved adekvansbeslutning eller ved overføring etter **art. 49-unntak**.
- Formål: vurdere og dokumentere om importøren vil være i stand til å oppfylle sine forpliktelser etter det valgte overføringsverktøyet. Eksportøren må vurdere beskyttelsesnivået i lokal lovgivning og ta hensyn til myndighetenes praksis i tredjelandet, og ved behov vurdere om supplerende tiltak kan avhjelpe mangler.

**1.3 Veilederens formål og oppbygning (s. 4–5).** Metode basert på EDPB Recommendations 01/2020 (versjon 2.0). Ikke en vurdering av lover og praksis i tredjeland; ikke obligatorisk; andre metoder kan brukes.

Forutgående vurderinger (kap. 2):
1. Foreligger en overføring av personopplysninger?
2. Er TIA nødvendig?
3. Hvem har ansvaret for å gjennomføre TIA?
4. Omfang av TIA, særlig videreoverføringer (onward transfers)
5. Samsvar med GDPR-prinsippene

De seks stegene (kap. 3), slik EDPB anbefaler:

| Steg | Innhold (s. 4–5) |
|---|---|
| 1 Kjenn overføringen (Know your transfer) | Eksportøren beskriver overføringen. |
| 2 Identifiser overføringsverktøyet | Dokumenter verktøyet som rammer inn overføringen, og konklusjon om TIA skal gjennomføres. |
| 3 Vurder lovgivning og praksis i mottakerlandet og verktøyets effektivitet | Identifiser forhold som kan svekke garantiene i verktøyet fra steg 2. |
| 4 Identifiser og vedta supplerende tiltak | Kartlegg eksisterende sikkerhetstiltak (tekniske, kontraktuelle, organisatoriske); hvis utilstrekkelige, identifiser supplerende tiltak som gir i det vesentlige tilsvarende beskyttelse. |
| 5 Implementer de supplerende tiltakene | Modell for handlingsplan for operativ gjennomføring og ev. prosessuelle steg. |
| 6 Revurder med passende intervaller | Planlegg fremtidige revurderinger og følg med på utvikling. |

Beskrivelsen i steg 1 og verktøyet i steg 2 gjør at overføringens egenskaper og sensitivitet tas med i vurderingen i steg 3 og valg av tiltak i steg 4 (s. 5).

### 2. Før TIA gjennomføres (s. 5–11)

Det anbefales å dokumentere analysen av forutsetningene (s. 5).

#### 2.1 Foreligger det en overføring av personopplysninger? (s. 5–6)

- Opplysningene må være **personopplysninger** etter art. 4 nr. 1.
- EDPBs tre **kumulative kriterier** for «overføring» (Guidelines 05/2021):
  1. En behandlingsansvarlig, felles behandlingsansvarlig eller databehandler («eksportøren») er underlagt GDPR for den aktuelle behandlingen.
  2. Eksportøren utleverer ved overføring eller på annen måte gjør personopplysningene tilgjengelige for en annen enhet («importøren»), som er behandlingsansvarlig, felles behandlingsansvarlig eller databehandler.
  3. Importøren befinner seg i et tredjeland (utenfor EØS), uavhengig av om importøren er underlagt GDPR etter art. 3, eller er en internasjonal organisasjon.
- Overføring krever **to rettslig atskilte enheter**. Overføring innenfor samme enhet er ikke overføring etter kap. V. Eksempel: en ansatt hos en behandlingsansvarlig i EU som på tjenestereise fjernaksesserer arbeidsgiverens database fra et tredjeland, er **ikke** overføring (s. 6).
- Overføring mellom to atskilte enheter i **samme konsern** kan være overføring.
- **Fjerntilgang** fra tredjeland til data lagret i EØS, og **skylagring** utenfor EØS, er overføring når det utføres av en enhet som er rettslig forskjellig fra eksportøren.

#### 2.2 Er TIA nødvendig? (s. 6–7)

TIA **kreves** før overføring basert på art. 46-verktøy, f.eks. Kommisjonens standardavtaler (SCC) eller bindende virksomhetsregler (BCR).

TIA er **ikke nødvendig** når:
- **Mottakerlandet har adekvansbeslutning.** Da trengs verken overføringsverktøy etter kap. V eller supplerende tiltak. EDPB Opinion 22/2024: Kommisjonen har ved adekvans allerede vurdert regler om videreoverføring, rettspraksis og effektive rettigheter og rettsmidler.
  - Adekvansbeslutninger kan ha **begrenset omfang**: Canada gjelder bare private organisasjoner som behandler personopplysninger i kommersiell virksomhet; Japan omfatter ikke kringkastere, avisutgivere, kommunikasjonsbyråer eller andre medier, profesjonelle skribenter, universiteter, religiøse institusjoner og politiske organer; USA (EU-US Data Privacy Framework, beslutning 2023/1795) omfatter bare sertifiserte enheter (s. 6–7). Faller overføringen utenfor adekvansbeslutningens omfang, må art. 46-verktøy (→ TIA) eller art. 49-unntak brukes.
  - Adekvansbeslutninger revideres periodisk – listen bør sjekkes jevnlig.
- **Overføringen bygger på et art. 49-unntak.** Da gjelder bare vilkårene i art. 49. Men: EDPB Guidelines 2/2018 – unntakene skal ikke bli «the rule» i praksis, men begrenses til spesifikke situasjoner, og hver eksportør må sikre at overføringen oppfyller et strengt nødvendighetskrav (s. 7).

#### 2.3 Partenes rolle og ansvar for TIA (s. 7–9)

Rollen (behandlingsansvarlig, felles behandlingsansvarlig, databehandler) til hver involvert enhet må fastslås, fordi den fordeler ansvar og plikter (EDPB Guidelines 07/2020). TIA gjennomføres av **eksportøren**, med **bistand fra importøren**, som har tilgang til mye nødvendig informasjon og kjenner lovgivningen.

| Tilfelle | Eksempel i kilden | Hvem gjør hva |
|---|---|---|
| **1** Behandlingsansvarlig i EØS (eksportør) → databehandler i tredjeland (importør) | Østerriksk selskap → chilensk selskap | Behandlingsansvarlig gjennomfører TIA; databehandler bistår. Etter art. 28 nr. 3 bokstav h plikter databehandleren å gi informasjon som viser etterlevelse, inkl. relevant materiale om lokal lovgivning og praksis, særlig myndighetstilgang (s. 8). |
| **2** Databehandler underlagt GDPR (eksportør) → underdatabehandler i tredjeland på vegne av behandlingsansvarlig | Tysk behandlingsansvarlig → fransk databehandler → indisk underdatabehandler | Databehandleren (eksportør) gjennomfører TIA; underdatabehandleren bistår; behandlingsansvarlig **verifiserer og ev. kompletterer** TIA (s. 8–9). |
| **3** Behandlingsansvarlig underlagt GDPR (eksportør) → behandlingsansvarlig i tredjeland | Irsk selskap → kinesisk selskap | Eksportøren gjennomfører TIA med hjelp fra importøren (s. 9). |

Konkrete bevis på lovgivning og praksis kan omfatte (s. 8): rapporter om tredjelandsmyndigheters tilgang til data overført fra EØS; rapporter om innsynsbegjæringer importøren, dens databehandler eller aktører i samme sektor har mottatt; informasjon om tredjelandets lovgivning med oversettelse til partenes arbeidsspråk; informasjon fra kompetente myndigheter om behandling av klager fra EØS-borgere. Pålitelige kilder kan hentes fra vedlegg 3 til EDPB Recommendations 01/2020.

Særlig om tilfelle 2 (s. 9):
- Etter art. 28 nr. 3 bokstav h skal databehandleren gi den behandlingsansvarlige informasjon, **herunder den gjennomførte TIA-en**.
- Å oversende bare en konklusjon eller et sammendrag av TIA eller lovvurderingen **uten konkrete bevis** oppfyller ikke databehandlerens forpliktelser.
- Den endelige beslutningen om å engasjere eller beholde databehandler og underdatabehandler ligger hos den **behandlingsansvarlige**, som har plikt etter art. 28 nr. 1 til å verifisere garantiene. Jo høyere risiko for de registrerte, desto grundigere kontroll. Behandlingsansvarlig kan bygge på databehandlerens TIA og supplere den hvis den er ufullstendig, unøyaktig eller reiser spørsmål.
- EDPB Opinion 22/2024 (fotnote 23–24): dokumentasjon om garantier, TIA og supplerende tiltak skal utarbeides av databehandleren/eksportøren (ev. i samarbeid med importøren); behandlingsansvarlig skal kunne vise den til tilsynsmyndigheten; for høyrisikobehandling skal behandlingsansvarlig øke verifiseringsnivået; plikten til å verifisere «sufficient guarantees» gjelder uansett risiko, men omfanget varierer med risikoen.

#### 2.4 TIA-ens omfang og videreoverføringer (s. 10)

- Første steg er å **kartlegge overføringene** (importør og tredjeland).
- Eksportøren må ta med **hele dataflyten, inkludert videreoverføringer**, slik at behandlingsansvarlig kan vurdere risikoen ved alle overføringer ut av EØS (EDPB Opinion 22/2024 para. 97: behandlingsansvarlig skal kunne vise dokumentasjon om videreoverføringer).
- En TIA kan omfatte én overføring eller et sett av overføringer; kan dokumenteres i ett eller flere dokumenter. Ved endring i overføringskjeden kan eksisterende analyse endres eller ny analyse lages og lenkes til tidligere. Er eksportøren databehandler, skal informasjonen deles med behandlingsansvarlig.
- Ved SCC: importøren forplikter seg til ikke å utlevere til tredjepart utenfor EU (i samme land eller annet ikke-adekvat land) med mindre tredjeparten er bundet av eller slutter seg til SCC (riktig modul); ellers kun hvis vilkårene i SCC er oppfylt (modul 1 klausul 8.7 og 8.8; modul 2 og 3 klausul 8.8) og dokumentasjonsplikten overholdes (modul 1 og 3 klausul 8.9; modul 2 klausul 8.8).
- Eksempel: italiensk behandlingsansvarlig → polsk databehandler (eksportør, gjennomfører TIA) → tyrkisk underdatabehandler → singaporsk 2. underdatabehandler; begge importører bistår; behandlingsansvarlig verifiserer/kompletterer.

#### 2.5 Samsvar med GDPR-prinsippene (s. 11)

- Overføringen er en behandling og må oppfylle alle prinsipper i art. 5; behandlingsansvarlig (direkte eller via databehandler) må sikre lovlig behandlingsgrunnlag etter art. 6 og ev. art. 9.
- **Dataminimering**: bare det som er strengt nødvendig for formålet med overføringen.
- **Informasjon** til de registrerte etter art. 13 og 14.
- Om mulig bør **anonymiserte** data overføres i stedet (GDPR gjelder da ikke), forutsatt effektiv anonymisering (WP29 Opinion 05/2014).

### 3. TIA-ens seks steg (s. 11–28)

#### Steg 1 – Kjenn overføringen (s. 11–15)

Beskrivelsen gjør at overføringens egenskaper og sensitivitet tas med i steg 3 og 4. Tabellen kan fylles ut med eksisterende dokumentasjon (protokoll over behandlingsaktiviteter, kontrakten), og informasjon kan innhentes fra importøren.

**Tabell – Eksportør**

| Felt | Svaralternativer / innhold |
|---|---|
| Navn på eksportør | |
| Kontaktpunkt og kontaktdetaljer (avdeling/person internt ansvarlig for overføringen) | |
| Eksportland | |
| Eksportørens rolle i overføringen | ☐ Behandlingsansvarlig ☐ Felles behandlingsansvarlig ☐ Databehandler. Ved databehandler/felles behandlingsansvarlig: oppgi navn på behandlingsansvarlig / øvrige felles behandlingsansvarlige |
| Annen nyttig informasjon | |

**Tabell – Importør**

| Felt | Svaralternativer / innhold |
|---|---|
| Navn på importør | |
| Kontaktpunkt og kontaktdetaljer | |
| Importland | |
| Importørens rolle i overføringen | ☐ Behandlingsansvarlig ☐ Felles behandlingsansvarlig ☐ Databehandler. Ved databehandler/felles: oppgi behandlingsansvarlig |
| Arten av importørens virksomhet (gjør det lettere å identifisere gjeldende lovgivning i tredjelandet) | Spesifiser arten. Er importøren særlig beskyttet av lovgivningen i mottakerlandet? (f.eks. for medisinsk behandling av pasient eller juridiske tjenester til klient – EDPB Rec. 01/2020 para. 91) |
| Annen nyttig informasjon | |

**Tabell – Overføringen**

| Felt | Svaralternativer / innhold |
|---|---|
| Importørens behandlingsaktiviteter på de overførte dataene | F.eks. IT-støtte, markedsføring, levering av skyprogramvare, hosting |
| **Type overføring** (hvordan dataene gjøres tilgjengelige) | ☐ **Fjerntilgang uten mulighet for nedlasting/lagring** – data hostes av eksportør i EØS; importøren kan ikke laste ned kopier, men kan aksessere fra ikke-adekvat land utenfor EØS. ☐ **Fjerntilgang med mulighet for nedlasting/lagring** – data hostes i EØS; importøren kan aksessere fra tredjeland og ved behov laste ned og lagre kopier i ikke-adekvat tredjeland. ☐ **Overføring og hosting/lokal lagring** – importøren hoster/lagrer dataene i ikke-adekvat land utenfor EØS. ☐ Annet |
| Overføringsmetode | F.eks. SFTP, e-post, API, tilkobling til ekstern server, fysisk lagringsmedium som sendes |
| Format på overførte data | ☐ I klartekst ☐ Kryptert ☐ Pseudonymisert ☐ Annet (spesifiser) |
| Frekvens | ☐ Enkeltoverføring ☐ Engangs/sporadisk (angi hyppighet) ☐ Regelmessig (angi hyppighet) |
| Mulighet for videreoverføring fra importør (jf. 2.4) | ☐ Ja (spesifiser) ☐ Nei |
| Kategorier personopplysninger | ☐ Identifikasjonsdata ☐ Kontaktopplysninger ☐ Familieliv ☐ Arbeidsliv ☐ Tjenestebruksdata ☐ Annet – alle med «spesifiser» |
| Særlige kategorier («sensitive data») | ☐ Rasemessig/etnisk opprinnelse ☐ Politisk oppfatning ☐ Religiøs/filosofisk overbevisning ☐ Fagforeningsmedlemskap ☐ Genetiske eller biometriske data for entydig identifisering ☐ Helseopplysninger ☐ Seksuelle forhold/legning ☐ Ingen av disse |
| Andre svært personlige opplysninger | ☐ Straffedommer og lovovertredelser (art. 10) ☐ Nasjonalt identifikasjonsnummer (art. 87) ☐ Geolokaliseringsdata ☐ Finansielle data som kan brukes til svindel (de to siste med henvisning til WP248, s. 11) ☐ Annet ☐ Ingen |
| Kategorier registrerte | |
| Sårbare personer blant de registrerte (f.eks. mindreårige, avhengige personer) | ☐ Ja (spesifiser) ☐ Nei |
| Hel eller delvis overføring (dvs. om overførte data utgjør alle eller bare del av de behandlede dataene) | ☐ Hel ☐ Delvis (angi prosent om mulig) |
| Volum overførte data (om mulig) | |
| Antall registrerte (om mulig) | |
| Planlagt startdato (om mulig) | |
| Planlagt sluttdato eller varighet (om mulig) | |

#### Steg 2 – Identifiser overføringsverktøyet (s. 16)

| Felt | Svaralternativer |
|---|---|
| Art. 46-verktøy som rammer inn overføringen | ☐ Standardavtaler (SCC) – angi modul ☐ BCR «Controller» ☐ BCR «Processor» ☐ Atferdsnorm (code of conduct) ☐ Sertifiseringsmekanisme ☐ Ad hoc-avtaleklausuler |
| Bevis og dokumentasjon for verktøyet | F.eks. signert kontrakt med importør, sertifikat for importørens sertifisering, kopi av BCR med liste over enheter (inkl. importøren) |

- Bygger overføringen på et art. 46-verktøy → TIA kreves → gå til steg 3.
- Er TIA ikke nødvendig (jf. 2.2) → anbefalt å **dokumentere beslutningen om ikke å gjennomføre TIA**.
- Fotnoter: Kommisjonen arbeider med et eget SCC-sett for importører som selv er underlagt GDPR (FAQ para. 25); BCR-C: EDPB Rec. 1/2022; BCR-P: WP265 og WP257 rev.01; atferdsnormer: EDPB Guidelines 04/2021; sertifisering: EDPB Guidelines 07/2022.

#### Steg 3 – Vurder lovgivning og praksis i mottakerlandet og verktøyets effektivitet (s. 17–22)

Formål: avgjøre om noe i tredjelandets lovgivning eller praksis kan undergrave garantiene i verktøyet eller hindre partene i å oppfylle forpliktelsene. Overføringens egenskaper og sensitivitet fra steg 1 skal tas med.

Metodiske råd (s. 17):
- **Importørens bistand er avgjørende**: eksportøren bør be importøren om en analyse av lovgivningen, særlig om myndighetstilgang, eller i det minste en liste over gjeldende lover. Importøren må følge eksportørens (og behandlingsansvarliges) instrukser.
- Bruk vedlegg 3 til EDPB Recommendations 01/2020 (ikke-uttømmende kildeliste). Kildene må være **relevante, objektive, pålitelige, etterprøvbare og offentlig tilgjengelige eller på annen måte tilgjengelige**.
- CNILs side «Data protection around the world» (personvernlov og tilsynsmyndighet i landet).
- Rapporter fra internasjonale organisasjoner og ekspertanalyser, f.eks. landanalyser bestilt av EDPB – suppleres og oppdateres ved behov.
- Del analyser via DPO-nettverk, bransjeforeninger, konsern- eller forvaltningsnettverk.

**Tabell 3A – Personvernlovgivning**

| Spørsmål | Svar |
|---|---|
| Hvilket personvernrammeverk gjelder for importøren? | Referanse til tekst(er) |
| Hva er virkeområdet? | ☐ Generelt rammeverk ☐ Sektoriell anvendelse (spesifiser) |
| Har tredjelandet sluttet seg til internasjonale personvernkonvensjoner? | ☐ Ja (spesifiser) ☐ Nei |
| Finnes en kompetent personvernmyndighet (eller forvaltningsorgan med tilsvarende myndighet)? | ☐ Ja (navn) ☐ Nei |
| Er myndigheten uavhengig? | ☐ Ja ☐ Nei – begrunn. Uavhengighet kan vurderes etter GDPR art. 52–54, art. 15 i Europarådets konvensjon 108+, Global Privacy Assemblys prosedyreregler art. 5.1, akkrediteringsprinsipp B.2 og arbeidsgruppedokumentet om autonomi og uavhengighet, samt OECD-publikasjonene «Being an Independent Regulator», «The Governance of Regulators», «Creating a Culture of Independence» (fotnote 41, s. 18) |

**Tabell 3B – De registrertes rettigheter** (for hver: ☐ Ja – referanse / ☐ Nei)

| Rettighet |
|---|
| Rett til innsyn |
| Rett til retting |
| Rett til sletting |
| Rett til å protestere mot behandling i særlige situasjoner |
| Rett til å protestere mot automatiserte avgjørelser |
| Andre rettigheter (spesifiser) |
| Er lovbestemte begrensninger av disse rettighetene nødvendige og forholdsmessige i et demokratisk samfunn? (spesifiser) |

**Tabell 3C – Rettsmidler og sanksjoner** (☐ Ja / ☐ Nei – begrunn)

| Spørsmål |
|---|
| Finnes effektive rettsmidler? |
| Finnes effektive og avskrekkende sanksjoner? |
| Kan disse rettighetene og rettsmidlene utøves av registrerte i EØS? |

**Tabell 3D – Lover og/eller praksis som gir tilgang til data**

| Spørsmål | Svar |
|---|---|
| Finnes **overvåkingslover** som gjelder for importøren og pålegger plikt til å utlevere de overførte personopplysningene eller gi offentlige myndigheter tilgang til dem? | ☐ Ja ☐ Nei. Hvis ja: liste med referanser og beskrivelse (virkeområde, berørt myndighet, pliktens art osv.) |
| Finnes **overvåkingspraksis** som gjelder for importøren og medfører slike plikter? | ☐ Ja ☐ Nei |

Lovene kan være generelle, gjelde strafferett eller nasjonal sikkerhet, og involvere f.eks. offentlige etater, reguleringsmyndigheter, skattemyndigheter, politi og etterretningstjenester (fotnote 42, s. 19).

**Tabell 3E – Vesentlige garantier (European Essential Guarantees, EDPB Recommendations 02/2020)** (☐ Ja / ☐ Nei – begrunn), s. 20

| Garanti |
|---|
| Er tilgangen til data styrt av **klare, presise og tilgjengelige regler**? |
| Er tilgangen **nødvendig og forholdsmessig** i et demokratisk samfunn for å ivareta et av formålene i **art. 23 nr. 1**? |
| Er tilgangen kontrollert av en **uavhengig tilsynsmekanisme**? |
| Er den berørte myndigheten underlagt **åpenhet og regelmessig kontroll**? |
| Har den registrerte **generelle (uavhengig av statsborgerskap) og effektive rettsmidler** for et uavhengig og upartisk organ? |

Formålene i art. 23 nr. 1 (fotnote 45): (a) nasjonal sikkerhet; (b) forsvar; (c) offentlig sikkerhet; (d) forebygging, etterforskning, avsløring eller rettsforfølgning av straffbare handlinger eller fullbyrding av straff, inkl. vern mot trusler mot offentlig sikkerhet; (e) andre viktige mål av allmenn interesse for Unionen eller en medlemsstat, særlig viktige økonomiske eller finansielle interesser (penge-, budsjett- og skattespørsmål, folkehelse, trygd); (f) vern av domstolenes uavhengighet og rettergang; (g) forebygging m.m. av brudd på yrkesetiske regler for lovregulerte yrker; (h) kontroll-, tilsyns- eller reguleringsoppgaver knyttet til offentlig myndighetsutøvelse i tilfellene (a)–(e) og (g); (i) vern av den registrerte eller andres rettigheter og friheter; (j) fullbyrding av sivilrettslige krav.

**Tabell 3F – Rettsstat (Rule of law)**, s. 21

| Spørsmål | Svar |
|---|---|
| Finnes rettsstatsproblemer som påvirker de registrertes mulighet til å søke oppreisning mot ulovlig tilgang til personopplysninger? | ☐ Ja ☐ Nei. Hvis ja: liste over problem og hvordan det påvirker utøvelsen av rettigheter |

**Tabell 3G – Mottatte begjæringer**, s. 21

| Spørsmål | Svar |
|---|---|
| Kan importøren dokumentere at den **ikke har mottatt begjæring om tilgang** eller vært utsatt for **direkte tilgang** fra tredjelandets myndigheter til personopplysninger om EØS-borgere (i hvert fall de siste årene)? | ☐ Ja – angi hvordan (f.eks. åpenhetsrapport om myndighetsbegjæringer) ☐ Nei – angi type begjæringer, antall, hvordan de ble behandlet og/eller hvorfor importøren tror den kan bli utsatt for slike i fremtiden |
| Kan det dokumenteres at det **ikke er grunn til å tro** at importøren vil motta begjæring eller bli utsatt for direkte tilgang, særlig fordi lovgivningen/problemene ikke i praksis vil gjelde de overførte dataene og importøren (sett hen til sektor og historikk)? | ☐ Ja – angi hvordan (f.eks. materiale publisert av aktører i samme/beslektet sektor) ☐ Nei. Hvis ja: det er mulig å beslutte å gjennomføre overføringen uten supplerende tiltak. |

Fotnote 47 (s. 21): Selv om verktøyet ikke er effektivt, kan man – når det ikke er grunn til å tro at den problematiske lovgivningen vil bli anvendt i praksis på dataene og/eller importøren – beslutte å overføre uten tilleggstiltak. Dette må **påvises og dokumenteres**, ev. i samarbeid med importøren, og ta hensyn til erfaringene til andre aktører i samme sektor og/eller sektorer med lignende data og andre kilder.

**Konklusjon steg 3** (s. 21–22) – kryss av én og begrunn:

| Nr. | Konklusjon | Videre |
|---|---|---|
| (1) | Verktøyet er effektivt i lys av vurderingen; overføring kan skje uten supplerende tiltak. | Gå til steg 6 |
| (2) | Verktøyet er ikke effektivt; supplerende tiltak må iverksettes. | Gå til steg 4 |
| (3) | Verktøyet er ikke effektivt, men det er ikke grunn til å tro at den problematiske lovgivningen vil bli anvendt i praksis, og det besluttes å overføre uten supplerende tiltak. | Gå til steg 6 |

#### Steg 4 – Identifiser og vedta supplerende tiltak (s. 22–26)

Prinsipper (s. 22):
- Tiltak identifiseres **konkret for hver overføring** og hvert tredjeland; beskrivelsen i steg 1 (egenskaper og sensitivitet) styrer valget. **Jo høyere risiko, desto grundigere kontroller og flere tiltak.**
- «Supplerende» fordi de supplerer overføringsverktøyet. Tabellen skal vise både **eksisterende** og **nye** tiltak.
- Vedlegg 2 til EDPB Rec. 01/2020 har ikke-uttømmende liste over tekniske, kontraktuelle og organisatoriske tiltak i form av brukstilfeller, og brukstilfeller der EDPB **ikke** finner effektive tiltak (use cases 6 og 7, para. 93–97).
- Det kan være nødvendig å kombinere flere tiltak. **Kontraktuelle og organisatoriske tiltak alene er som regel ikke tilstrekkelige** mot myndighetstilgang og må suppleres med korrekt implementerte tekniske tiltak (EDPB Rec. 01/2020 para. 53).
- I noen tilfeller finnes ingen tiltak som gir i det vesentlige tilsvarende beskyttelse → **avstå fra overføringen**.
- Prosessen skal skje med aktsomhet, i samarbeid med importøren, og dokumenteres. Involvering av **informasjonssikkerhetsleder (CISO)** er avgjørende. Uttalelser/analyser fra de som er konsultert (DPO, juridisk og teknisk rådgivning, IS-ansvarlig, tilsynsmyndighet) anbefales vedlagt TIA.

**Tabell 4A – Supplerende tiltak som allerede er implementert** (for hvert tiltak: beskrivelse, om det gjennomføres av importør eller eksportør, i hvilken grad det er i tråd med EDPBs anbefalinger, og hvilke risikoer det reduserer)

*Tekniske tiltak* («for at tekniske tiltak skal være effektive, verifiser alle kontrollpunktene i fotnotene»):

☐ **Pseudonymisering** – vilkår (EDPB Rec. 01/2020, use case 2, para. 85):
1. Eksportøren overfører personopplysninger behandlet slik at de ikke lenger kan knyttes til en bestemt registrert eller brukes til å skille ut den registrerte i en større gruppe uten tilleggsinformasjon.
2. Tilleggsinformasjonen holdes **utelukkende av eksportøren** og oppbevares separat i en medlemsstat eller i et tredjeland, av en enhet eksportøren stoler på i EØS eller under en jurisdiksjon med i det vesentlige tilsvarende beskyttelse.
3. Utlevering eller uautorisert bruk av tilleggsinformasjonen forhindres med egnede tekniske og organisatoriske garantier; eksportøren har **eneste kontroll** over algoritmen eller registeret som muliggjør re-identifisering.
4. Den behandlingsansvarlige har gjennom grundig analyse – også av informasjon mottakerlandets myndigheter kan forventes å ha og bruke – fastslått at de pseudonymiserte dataene ikke kan knyttes til en identifisert eller identifiserbar person selv om de krysses med slik informasjon.

☐ **Kryptering** – vilkår (EDPB Rec. 01/2020, use case 3, para. 90 – transportkryptering):
1. Ved overføring til jurisdiksjon der myndighetene kan få tilgang til data under transport uten de vesentlige garantiene: **transportkryptering** med protokoller som er state-of-the-art og gir effektiv beskyttelse mot aktive og passive angrep med ressurser myndighetene i tredjelandet er kjent for å ha.
2. Partene er enige om en pålitelig sertifikatutsteder/PKI.
3. Spesifikke, oppdaterte tiltak mot aktive og passive angrep på sende- og mottakssystemene, inkl. testing for sårbarheter og mulige bakdører.
4. Hvis transportkrypteringen ikke gir tilstrekkelig sikkerhet alene (erfaring med sårbarheter i infrastruktur/programvare), krypteres dataene også **ende-til-ende på applikasjonslaget**.
5. Algoritme og parametre (nøkkellengde, modus) er state-of-the-art og robuste mot kryptoanalyse fra myndighetene, gitt deres ressurser og tekniske kapasitet (f.eks. regnekraft for brute-force).
6. Krypteringsstyrken tar hensyn til hvor lenge konfidensialiteten må bevares.
7. Algoritmen er korrekt implementert i vedlikeholdt programvare uten kjente sårbarheter, med verifisert samsvar med spesifikasjonen (f.eks. sertifisering).
8. **Nøklene forvaltes pålitelig** (genereres, administreres, lagres, ev. knyttes til mottakers identitet, tilbakekalles) av eksportøren eller en enhet eksportøren stoler på under en jurisdiksjon med i det vesentlige tilsvarende beskyttelse.

☐ Annet (spesifiser).

*Organisatoriske tiltak* (EDPB Rec. 01/2020 avsnitt 2.3, para. 128–143):
- ☐ Dokumentasjon av innsynsbegjæringer (begjæringer mottatt, svar, juridisk begrunnelse, involverte aktører)
- ☐ Dataminimering (streng og granulær tilgang, personvernpolicyer, tilgang etter tjenstlig behov (need-to-know), kontroll gjennom revisjoner, disiplinærtiltak)
- ☐ Styring (informasjon til og involvering av personvernombud/GDPR-ansvarlig ved alle innsynsbegjæringer)
- ☐ Sikkerhets- og personvernstandarder (sertifisering og etterlevelse av sikkerhetsstandarder)
- ☐ Interne retningslinjer og prosedyrer for behandling av innsynsbegjæringer
- ☐ Ansvarsfordeling mellom enheter i konsernet, egne team for innsynsbegjæringer, opplæring av ansatte som håndterer slike begjæringer
- ☐ Annet (spesifiser)

*Kontraktuelle tiltak* (EDPB Rec. 01/2020 avsnitt 2.2, para. 98–127):
- ☐ Inntak av supplerende tekniske eller organisatoriske tiltak i en bindende kontrakt
- ☐ Åpenhetskrav: importørens plikt til å liste lover, praksis, tiltak for å hindre tilgang, innsynsbegjæringer, og å opplyse om den er rettslig forhindret fra å gi slik informasjon
- ☐ Forbud mot bakdører eller prosesser som letter tilgang til data
- ☐ Rett til revisjon for å verifisere etterlevelse
- ☐ Varsling av eksportøren (og de registrerte) ved myndighetstilgang
- ☐ Forpliktelse til å bestride innsynsbegjæringer
- ☐ Importørens forpliktelse til å vurdere lovligheten av enhver utleveringsordre og bestride den når det er grunn til det
- ☐ Forpliktelse til å søke midlertidige tiltak for å suspendere ordren til domstolen har avgjort saken
- ☐ Forpliktelse til å informere ved manglende evne til å overholde kontraktsforpliktelser
- ☐ Sanksjoner ved brudd, inkl. erstatning til de registrerte
- ☐ Oppsigelse av kontrakten ved brudd på forpliktelser knyttet til overføring
- ☐ Importørens forpliktelse til å gi myndighetene bare minimumsinformasjon ved svar på innsynsbegjæring
- ☐ Importørens forpliktelse til å informere tredjelandsmyndigheten om uforenlighet med personvernlovgivningen og samtidig varsle eksportøren
- ☐ Data i klartekst kan bare aksesseres med eksportørens uttrykkelige eller implisitte samtykke
- ☐ Annet (spesifiser)

*Konklusjon 4A:* ☐ Verktøyet kombinert med eksisterende tiltak er effektivt. ☐ Verktøyet kombinert med eksisterende tiltak er ikke effektivt – ytterligere supplerende tiltak må vurderes.

**Tabell 4B – Nye supplerende tiltak** (s. 26) – kolonner: beskrivelse (inkl. hvem som gjennomfører og samsvar med EDPBs anbefalinger) og virkning (hvilke risikoer reduseres), med rader for tekniske, organisatoriske og kontraktuelle tiltak (se eksemplene over).

*Konklusjon 4B:* ☐ Verktøyet kombinert med eksisterende og nye tiltak er effektivt. ☐ … er ikke effektivt.

Videre (s. 26):
- Effektivt → overføring kan skje **forutsatt effektiv implementering** av tiltakene. Er eksisterende tiltak nok → steg 6. Trengs nye tiltak → steg 5.
- Ikke mulig å få på plass nødvendige tiltak (ved TIA eller revurdering) → planlagt overføring skal **ikke gjennomføres**; pågående overføring må **avsluttes**. Importøren må da **slette alle data og bevise det overfor eksportøren**, eller **returnere alle data og slette eksisterende kopier**.

#### Steg 5 – Implementer de supplerende tiltakene (s. 26–27)

Det anbefales å liste handlinger for å implementere nye tiltak, og ev. prosessuelle steg, for å sikre effektivitet og forutse hindringer (f.eks. økonomi, manglende tilgjengelighet av kompetente team). Prosessuelle steg varierer med verktøy (EDPB Rec. 01/2020 avsnitt 2.5, para. 59–68), f.eks. må eksportøren søke tilsynsmyndigheten om **godkjenning** dersom SCC er endret slik at rettigheter og plikter begrenses, eller tilleggstiltakene motsier SCC (fotnote 56).

**Tabell 5 – Handlingsplan**

| Handling | Felt |
|---|---|
| Handling 1 – navn | Beskrivelse; estimert kostnad i dagsverk (valgfritt); ansvarlig(e) (f.eks. jurist, teknisk ekspert, fagavdeling); estimert ferdigdato |
| Handling 2 – navn | (samme felt) |
| … | … |

**Uttalelser og godkjenning** (s. 27):
- Uttalelse fra personvernansvarlig (eller personvernombud, om det finnes)
- Uttalelse fra ansvarlig for informasjonssikkerhet (eller CISO, om det finnes)
- Godkjenning av den som er ansvarlig for overføringen etter interne styringsregler

#### Steg 6 – Revurder med passende intervaller (s. 28)

- Overføringsverktøyet og ev. supplerende tiltak bør revurderes med passende intervaller, slik at overføringen suspenderes eller avsluttes hvis verktøy eller tiltak ikke lenger er effektive.
- Intervallene fastsettes konkret etter **mottakerland** og **risikonivå** for de registrerte.
- Tidligere revurdering kan være nødvendig ved f.eks. endring i tredjelandets lov eller praksis, importørens manglende evne til å overholde forpliktelser, eller endring i Kommisjonens vurdering av tredjelandets rett. Det anbefales å følge lovgivningsnyheter i landet.

**Tabell 6 – Revurdering av beskyttelsen**

| Felt | Innhold |
|---|---|
| Intervall mellom gjennomganger | F.eks. hvert 2. år |
| Dato for neste gjennomgang | |
| Ev. fremskyndet gjennomgang og begrunnelse | |

### Flyt i metoden (oppsummert)

```
Forutsetninger (2.1–2.5) → Er det overføring? → Adekvans/art. 49? (ja: ingen TIA, dokumenter)
  → Steg 1 Beskriv → Steg 2 Verktøy (art. 46) → Steg 3 Lov og praksis
      (1) effektivt → Steg 6
      (3) ikke effektivt, men ikke anvendt i praksis (dokumentert) → Steg 6
      (2) ikke effektivt → Steg 4 Tiltak
            eksisterende tiltak nok → Steg 6
            nye tiltak nødvendige og effektive → Steg 5 Handlingsplan → Steg 6
            ingen effektive tiltak → ikke overfør / avslutt (slett eller returner data)
```

## Praktiske sjekkpunkter

- Kontroller at det faktisk er en **overføring**: to rettslig atskilte enheter, eksportør underlagt GDPR, importør i tredjeland. Husk at fjerntilgang (f.eks. support) fra tredjeland og skylagring utenfor EØS er overføring når en annen enhet står for det.
- Kontroller om mottakerlandet har **adekvansbeslutning**, og om den konkrete importøren/sektoren faller innenfor beslutningens omfang (Canada: kommersiell privat sektor; Japan: unntak for media, akademia m.m.; USA: bare DPF-sertifiserte).
- Dersom art. 49 brukes: kontroller at det er en reell unntakssituasjon og at det strenge nødvendighetskravet er oppfylt.
- Dokumenter beslutningen også når TIA **ikke** gjennomføres.
- Kontroller at rollene er avklart og at riktig part (eksportøren) gjennomfører TIA, med importørens bistand.
- Når leverandøren (databehandler) er eksportør: krev **hele TIA-en med konkrete bevis**, ikke bare et sammendrag; den behandlingsansvarlige må vurdere og ev. supplere – grundigere ved høy risiko.
- Kontroller at TIA omfatter **hele kjeden**, inkl. videreoverføringer til underdatabehandlere, og at SCC-vilkårene for videreoverføring (modul 1 kl. 8.7–8.8; modul 2–3 kl. 8.8) er oppfylt.
- Kontroller at overføringen har behandlingsgrunnlag (art. 6/9), er minimert, og at de registrerte er informert (art. 13/14). Vurder anonymisering.
- Fyll ut alle tabellene i steg 1–3; begrunn hvert Ja/Nei i steg 3 med etterprøvbare kilder.
- Vurder alle fem «essential guarantees» eksplisitt.
- Bruk konklusjon (3) bare når det er **påvist og dokumentert** at problematisk lovgivning ikke vil anvendes i praksis.
- Ved behov for tiltak: sørg for at det finnes **tekniske** tiltak – kontraktuelle/organisatoriske alene er normalt ikke nok mot myndighetstilgang.
- Ved pseudonymisering/kryptering: sjekk alle EDPB-kontrollpunktene (eksportøren har eneste kontroll over nøkler/tilleggsinformasjon).
- Få uttalelse fra personvernombud og CISO og formell godkjenning; legg ved rådgivningsnotater.
- Sett revurderingsintervall og dato; definer hendelser som utløser tidligere revurdering.
- Hvis tiltak ikke kan gjøres effektive: stopp/avslutt overføringen og krev sletting (med bevis) eller retur.

## Viktige sitater

- «A TIA must be carried out by the exporter subject to the GDPR, whether acting as controller or processor, with the assistance of the importer, before transferring the data to a third country outside the EEA where such transfer is based on an Article 46 GDPR tool.» (s. 3)
- «The objective of a TIA is to assess and document whether the importer will be able to comply with its obligations as set out in the transfer tool chosen.» (s. 3)
- «This means that when an employee of a controller in the EU remotely accesses a database of their employer from a third country, for example during a business trip, this does not constitute a transfer within the meaning of the GDPR.» (s. 6)
- «the transmission by the exporting processor … of a simple conclusion or an executive summary of its TIA … without the provision of concrete evidence, does not enable it to fulfil its obligations.» (s. 9)
- «The exporter must take into account in its analysis the entire data flow, including onward transfers» (s. 10)
- «In most cases, contractual and organisational measures are not sufficient to prevent possible access to the data by the authorities of the third country and need to be complemented by properly implemented technical measures.» (s. 22)
- «In some cases, the conclusion will be that there are no supplementary measures to ensure a level of protection essentially equivalent to European law for the transfer in question, which should lead to a waiver of the transfer of the data in question.» (s. 22)
- «If the transfer is already ongoing, it needs to be terminated. In the latter case, the importer will have to erase all data and prove them to the exporter, or return all data and erase existing copies.» (s. 26)

## Kryssreferanser

- GDPR: art. 4 nr. 1, 7 og 8 (definisjoner); art. 5, 6, 9, 10 (prinsipper og grunnlag); art. 13–14 (informasjon); art. 23 nr. 1 (legitime formål for begrensninger); art. 28 nr. 1 og nr. 3 bokstav h (databehandlers garantier og informasjonsplikt); art. 44 (generelt prinsipp), art. 45 (adekvans), art. 46 (garantier), art. 47 (BCR), art. 49 (unntak); art. 52–54 (uavhengighet); art. 87 (nasjonalt ID-nummer); fortalepunkt 101.
- EDPB-dokumenter referert: Recommendations 01/2020 v2.0 (supplerende tiltak, vedlegg 2 og 3), Recommendations 02/2020 (European Essential Guarantees), Guidelines 05/2021 (art. 3 og kap. V), Guidelines 2/2018 (art. 49), Guidelines 07/2020 (roller), Opinion 22/2024 (databehandlere/underdatabehandlere), Guidelines 04/2021 og 07/2022 (atferdsnormer/sertifisering som overføringsverktøy); Kommisjonens SCC (beslutning 2021/914).
- Andre kilder:
  - [K14](K14-dt-overforing-utenfor-eos.md) – Datatilsynets norske veiledning om overføring ut av EØS; bruk sammen med denne for norsk kontekst.
  - [K05](K05-dt-databehandleravtale.md) og [K01](K01-dt-behandlingsansvarlig-og-databehandler.md) – databehandleravtale og rollefordeling (art. 28), relevant for tilfelle 1–2.
  - [K24](K24-wp248-dpia.md) – WP248 brukes for «svært personlige opplysninger» (geolokalisering, finansdata) i steg 1.
  - [K10](K10-dt-kryptering.md) – kryptering som teknisk tiltak.
  - [K11](K11-art30-protokollmaler.md) / [K04](K04-dt-fore-protokoll.md) – protokollen kan brukes som grunnlag for steg 1.

## Aktualitet og begrensninger

- Endelig versjon januar 2025; bygger på GDPR, Schrems II (2020), EDPB Rec. 01/2020 v2.0 og EDPB Opinion 22/2024 – oppdatert per publiseringstidspunktet.
- Utgitt av fransk tilsynsmyndighet (CNIL), men metoden er generell for hele EØS og følger EDPBs steg; ikke rettslig bindende, og den gir **ingen landvurderinger** (s. 4).
- Adekvanslisten endres over tid (bl.a. EU-US Data Privacy Framework 2023) – må sjekkes på vurderingstidspunktet.
- **[Merknad – ikke fra kilden]** I Norge gjelder adekvansbeslutninger og SCC via EØS-avtalen; Datatilsynet viser til EDPBs anbefalinger. Se [K14](K14-dt-overforing-utenfor-eos.md).
- **[Merknad – ikke fra kilden]** Kildeteksten bruker i én rad formuleringen «in an inadequate EEA third country» (s. 13) – dette er åpenbart ment som «non-EEA».

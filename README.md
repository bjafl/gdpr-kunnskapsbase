# GDPR-kunnskapsbase

Kunnskapsbase for en AI-agent som skal slå opp i personvernregelverket og bistå med **databehandleravtaler (DPA)**, **vurderinger av personvernkonsekvenser (DPIA)**, **risikovurderinger**, **overføringsvurderinger (TIA)**, **protokoll** og **avvikshåndtering**.

Basen er bygget fra 43 dokumenter i `../ressurser/` fra Datatilsynet, Digdir, DFØ, NSM, Artikkel 29-gruppen/EDPB, CNIL og ULD Schleswig-Holstein. Alt er skrevet på norsk bokmål.

---

## Slik bruker agenten basen

1. **Finn riktig inngang** i rutetabellen under. Bruk arbeidsflyten (A) når brukeren vil ha noe *gjort*, og temanotatet (T) når brukeren *spør* om noe.
2. **Les temanotatet.** Det gir kjernereglene og peker til kildene.
3. **Gå til kildenotatet (K)** når svaret må være presist: ordrette kriterier, tabeller, sidetall eller sitater.
4. **Bruk malen (M)** når noe skal produseres, for eksempel en DPIA, en DPA-gjennomgang eller en risikovurdering.
5. **Slå opp på artikkel** i [INDEKS-artikler.md](INDEKS-artikler.md) når spørsmålet gjelder en bestemt GDPR-artikkel.
6. **Sjekk [KJENTE-MOTSTRIDER.md](KJENTE-MOTSTRIDER.md)** når kildene kan spriker, for eksempel om skalaer, frister, aldersgrenser eller utdaterte retningslinjer.

Med Grep finner du raskt fram i hele basen: `grep -ril "underdatabehandler" gdpr-kunnskapsbase/`.

### Regler for svar

- **Henvis alltid til kilde**, for eksempel «[K05 s. 4]» eller «[T07]». Brukeren skal kunne etterprøve svaret.
- **Kildehierarki** når kildene er uenige: GDPR og lov går foran EDPB/WP29, deretter Datatilsynet (norsk praksis), andre tilsyn (CNIL, ULD) og til sist metodeverk (Digdir, NSM, SDM). Hvis en eldre kilde er erstattet, si det.
- **Skill kilde fra egen kunnskap.** Tekst merket **[Merknad – ikke fra kilden/kildene]** er tilført av den som skrev notatet og er ikke hentet fra dokumentene. Behandle det som mindre sikkert.
- **Aktualitet:** Kildene er fra 2011 til 2026. Status for adekvansbeslutninger (blant annet EU–US Data Privacy Framework), EDPB-retningslinjer og norsk lov kan ha endret seg. Si fra og anbefal verifisering når svaret avhenger av ferske forhold.
- **Ikke juridisk rådgivning.** Store beslutninger skal eskaleres til jurist eller personvernombud: forhåndsdrøfting etter art. 36, overføring basert på art. 49, høy restrisiko, melding om avvik. Kriteriene står i hver arbeidsflyt.
- **Norsk kontekst:** Personopplysningsloven gjennomfører GDPR i norsk rett via EØS-avtalen. Tilsynsmyndighet er Datatilsynet, og klageinstans er Personvernnemnda.

---

## Rutetabell: spørsmål → fil

| Brukeren vil / spør om … | Start her | Mal | Detaljkilder |
|---|---|---|---|
| Gjennomgå eller lage en **databehandleravtale** | [A01](arbeidsflyter/A01-gjennomga-databehandleravtale.md) | [M01](maler/M01-databehandleravtale-sjekkliste.md), [M09](maler/M09-sikkerhetstiltak-sjekkliste.md) | [T07](temaer/T07-databehandleravtale-art28.md), [K05](kilder/K05-dt-databehandleravtale.md), [K01](kilder/K01-dt-behandlingsansvarlig-og-databehandler.md) |
| Er leverandøren **databehandler eller behandlingsansvarlig**? Felles ansvar? | [T01](temaer/T01-roller-behandlingsansvarlig-databehandler.md) | – | [K01](kilder/K01-dt-behandlingsansvarlig-og-databehandler.md), [K39](kilder/K39-cnil-mobilapper.md) |
| **Trenger vi DPIA?** (terskelvurdering) | [T10](temaer/T10-dpia-art35-36.md) | [M05](maler/M05-dpia-terskelvurdering.md) | [K20](kilder/K20-dt-dpia-liste.md), [K24](kilder/K24-wp248-dpia.md), [K22](kilder/K22-dpia-eksempler.md) |
| **Gjennomføre en DPIA** | [A02](arbeidsflyter/A02-gjennomfore-dpia.md) | [M04](maler/M04-dpia-mal.md) | [K12](kilder/K12-dt-dpia-veiledning.md), [K21](kilder/K21-dt-sjekkliste-dpia-faser.md), [K28](kilder/K28-cnil-pia-metode.md)–[K31](kilder/K31-cnil-pia-tilkoblede-objekter.md), [K40](kilder/K40-dpia-prosess-uld.md) |
| **Risikovurdering** (informasjonssikkerhet/personvern) | [A03](arbeidsflyter/A03-risikovurdering-informasjonssikkerhet.md) | [M03](maler/M03-risikovurdering-mal.md) | [T09](temaer/T09-risikovurdering-metoder-og-skalaer.md), [K17](kilder/K17-digdir-gjennomfore-risikovurdering.md)–[K19](kilder/K19-digdir-risikovurderingsverktoy.md), [K30](kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Hvilke **sikkerhetstiltak** er «egnede» (art. 32)? | [T08](temaer/T08-informasjonssikkerhet-art32.md) | [M09](maler/M09-sikkerhetstiltak-sjekkliste.md) | [K32](kilder/K32-nsm-grunnprinsipper.md) NSM, [K33](kilder/K33-cnil-sikkerhetsguide.md) CNIL, [K37](kilder/K37-sdm-standard-datavernmodell.md) SDM, [K10](kilder/K10-dt-kryptering.md) |
| **Overføring ut av EØS**, sky, support fra tredjeland, **TIA** | [A04](arbeidsflyter/A04-overforing-og-tia.md) | [M06](maler/M06-tia-mal.md) | [T11](temaer/T11-overforing-tredjeland-og-tia.md), [K14](kilder/K14-dt-overforing-utenfor-eos.md), [K38](kilder/K38-tia-guide.md) |
| **Avvik / sikkerhetsbrudd**: skal det meldes? | [A05](arbeidsflyter/A05-avvikshandtering.md) | [M07](maler/M07-avviksvurdering-og-melding.md) | [T12](temaer/T12-avvik-og-brudd-art33-34.md), [K15](kilder/K15-dt-digitale-angrep.md), [K34](kilder/K34-cnil-cybersikkerhet-2024.md) |
| **Behandlingsgrunnlag**, samtykke, berettiget interesse | [A06](arbeidsflyter/A06-vurdere-behandlingsgrunnlag.md) | [M08](maler/M08-interesseavveining-mal.md) | [T02](temaer/T02-behandlingsgrunnlag-og-samtykke.md), [K02](kilder/K02-dt-behandlingsgrunnlag.md), [K25](kilder/K25-wp259-samtykke.md) |
| **Grunnprinsipper**, formål, viderebehandling | [T03](temaer/T03-grunnprinsipper-art5.md) | – | [K09](kilder/K09-dt-grunnleggende-prinsipper.md), [K03](kilder/K03-dt-fastsette-formal.md) |
| **Personvernerklæring** / informasjonsplikt | [T04](temaer/T04-apenhet-og-informasjonsplikt.md) | – | [K06](kilder/K06-dt-informasjon-og-apenhet.md), [K26](kilder/K26-wp260-apenhet.md) |
| **Innsyn, sletting, retting**, protest, portabilitet | [T05](temaer/T05-de-registrertes-rettigheter.md) | – | [K07](kilder/K07-dt-legge-til-rette-for-rettigheter.md), [K08](kilder/K08-dt-retting-og-sletting.md) |
| **Protokoll** over behandlingsaktiviteter | [T06](temaer/T06-protokoll-art30.md) | [M02](maler/M02-protokoll-art30.md) | [K04](kilder/K04-dt-fore-protokoll.md), [K11](kilder/K11-art30-protokollmaler.md), [K41](kilder/K41-dcat-ap-no.md) |
| **Innebygd personvern** / personvern som standard | [T13](temaer/T13-innebygd-personvern-art25.md) | – | [K13](kilder/K13-dt-innebygd-personvern.md), [K37](kilder/K37-sdm-standard-datavernmodell.md) |
| **Apper, SDK-er**, sporing, cookies | [T15](temaer/T15-apper-sdk-og-sporingsteknologi.md) | – | [K39](kilder/K39-cnil-mobilapper.md), [K31](kilder/K31-cnil-pia-tilkoblede-objekter.md) |
| **Hvilket tilsyn** har ansvaret (grenseoverskridende behandling)? | [T14](temaer/T14-tilsynsmyndighet-og-one-stop-shop.md) | – | [K27](kilder/K27-wp244-ledende-tilsynsmyndighet.md) |
| **Revisjon** / internkontroll av personvern | [T08](temaer/T08-informasjonssikkerhet-art32.md) | [M09](maler/M09-sikkerhetstiltak-sjekkliste.md) | [K35](kilder/K35-cnil-referentiel-audit.md), [K16](kilder/K16-dfo-veileder-informasjonssikkerhet.md), [K18](kilder/K18-digdir-retningslinje-risiko.md) |

---

## Innhold

### Temaer (`temaer/`): syntese på tvers av kilder

| ID | Tema | GDPR |
|---|---|---|
| [T01](temaer/T01-roller-behandlingsansvarlig-databehandler.md) | Roller: behandlingsansvarlig, databehandler, felles ansvar, underdatabehandlere | 4, 24, 26, 28, 29 |
| [T02](temaer/T02-behandlingsgrunnlag-og-samtykke.md) | Behandlingsgrunnlag og samtykke | 6–10 |
| [T03](temaer/T03-grunnprinsipper-art5.md) | Grunnprinsipper, formålsbegrensning, forenlighet | 5, 6(4) |
| [T04](temaer/T04-apenhet-og-informasjonsplikt.md) | Åpenhet og informasjonsplikt | 12–14 |
| [T05](temaer/T05-de-registrertes-rettigheter.md) | De registrertes rettigheter | 12, 15–22 |
| [T06](temaer/T06-protokoll-art30.md) | Protokoll over behandlingsaktiviteter | 30 |
| [T07](temaer/T07-databehandleravtale-art28.md) | Databehandleravtale | 28 |
| [T08](temaer/T08-informasjonssikkerhet-art32.md) | Informasjonssikkerhet, tiltakskatalog med kryssreferanser NSM ↔ CNIL ↔ SDM | 32 |
| [T09](temaer/T09-risikovurdering-metoder-og-skalaer.md) | Risikovurdering: metoder, skalaer, akseptkriterier | 24, 32, 35 |
| [T10](temaer/T10-dpia-art35-36.md) | DPIA og forhåndsdrøfting | 35–36 |
| [T11](temaer/T11-overforing-tredjeland-og-tia.md) | Overføring til tredjeland og TIA | 44–49 |
| [T12](temaer/T12-avvik-og-brudd-art33-34.md) | Avvik: melding og varsling | 33–34 |
| [T13](temaer/T13-innebygd-personvern-art25.md) | Innebygd personvern og personvern som standard | 25 |
| [T14](temaer/T14-tilsynsmyndighet-og-one-stop-shop.md) | Tilsynsmyndighet og one-stop-shop | 51–65 |
| [T15](temaer/T15-apper-sdk-og-sporingsteknologi.md) | Apper, SDK-er og sporingsteknologi | 5–7, 25, 26, 28 |

### Maler (`maler/`): utfyllbare dokumenter

| ID | Mal |
|---|---|
| [M01](maler/M01-databehandleravtale-sjekkliste.md) | Sjekkliste for gjennomgang av databehandleravtale (status OK/Mangler/Uklart) |
| [M02](maler/M02-protokoll-art30.md) | Protokoll etter art. 30 (behandlingsansvarlig og databehandler) |
| [M03](maler/M03-risikovurdering-mal.md) | Risikovurdering (Digdir-skala med alternativet CNIL 4×4) |
| [M04](maler/M04-dpia-mal.md) | DPIA, komplett mal (art. 35 nr. 7 + WP248 Annex 2) |
| [M05](maler/M05-dpia-terskelvurdering.md) | DPIA-terskelvurdering (screening) |
| [M06](maler/M06-tia-mal.md) | Overføringskonsekvensvurdering (TIA) |
| [M07](maler/M07-avviksvurdering-og-melding.md) | Avviksvurdering og melding |
| [M08](maler/M08-interesseavveining-mal.md) | Interesseavveining, trestegstest |
| [M09](maler/M09-sikkerhetstiltak-sjekkliste.md) | Sjekkliste for sikkerhetstiltak etter art. 32 (internt og mot leverandør) |

### Arbeidsflyter (`arbeidsflyter/`): steg for steg

| ID | Arbeidsflyt |
|---|---|
| [A01](arbeidsflyter/A01-gjennomga-databehandleravtale.md) | Gjennomgå databehandleravtale / leverandøravtale |
| [A02](arbeidsflyter/A02-gjennomfore-dpia.md) | Gjennomføre DPIA |
| [A03](arbeidsflyter/A03-risikovurdering-informasjonssikkerhet.md) | Risikovurdering av informasjonssikkerhet |
| [A04](arbeidsflyter/A04-overforing-og-tia.md) | Overføring til tredjeland og TIA |
| [A05](arbeidsflyter/A05-avvikshandtering.md) | Avvikshåndtering |
| [A06](arbeidsflyter/A06-vurdere-behandlingsgrunnlag.md) | Vurdere behandlingsgrunnlag |

### Kilder (`kilder/`): ett notat per dokument

| ID | Kilde | Utgiver | Relevans |
|---|---|---|---|
| [K01](kilder/K01-dt-behandlingsansvarlig-og-databehandler.md) | Behandlingsansvarlig og databehandler | Datatilsynet | høy |
| [K02](kilder/K02-dt-behandlingsgrunnlag.md) | Behandlingsgrunnlag | Datatilsynet | høy |
| [K03](kilder/K03-dt-fastsette-formal.md) | Fastsette formål | Datatilsynet | middels |
| [K04](kilder/K04-dt-fore-protokoll.md) | Føre protokoll | Datatilsynet | middels |
| [K05](kilder/K05-dt-databehandleravtale.md) | Hvordan lage en databehandleravtale | Datatilsynet | høy |
| [K06](kilder/K06-dt-informasjon-og-apenhet.md) | Informasjon og åpenhet | Datatilsynet | høy |
| [K07](kilder/K07-dt-legge-til-rette-for-rettigheter.md) | Legge til rette for rettigheter | Datatilsynet | middels |
| [K08](kilder/K08-dt-retting-og-sletting.md) | Retting og sletting | Datatilsynet | middels |
| [K09](kilder/K09-dt-grunnleggende-prinsipper.md) | De grunnleggende personvernprinsippene | Datatilsynet | høy |
| [K10](kilder/K10-dt-kryptering.md) | Kryptering (delvis utdatert teknisk) | Datatilsynet | middels |
| [K11](kilder/K11-art30-protokollmaler.md) | Protokollmaler art. 30 (Excel) | Datatilsynet | høy |
| [K12](kilder/K12-dt-dpia-veiledning.md) | Veiledning om DPIA | Datatilsynet | høy |
| [K13](kilder/K13-dt-innebygd-personvern.md) | Innebygd personvern og personvern som standard | Datatilsynet | høy |
| [K14](kilder/K14-dt-overforing-utenfor-eos.md) | Overføring av personopplysninger ut av EØS | Datatilsynet | høy |
| [K15](kilder/K15-dt-digitale-angrep.md) | Håndtering av personvernet ved digitale angrep | Datatilsynet | høy |
| [K16](kilder/K16-dfo-veileder-informasjonssikkerhet.md) | Veileder i informasjonssikkerhet | DFØ | middels |
| [K17](kilder/K17-digdir-gjennomfore-risikovurdering.md) | Gjennomføre risikovurdering | Digdir | høy |
| [K18](kilder/K18-digdir-retningslinje-risiko.md) | Eksempel-retningslinje: forstå, vurdere og håndtere risiko | Digdir | høy |
| [K19](kilder/K19-digdir-risikovurderingsverktoy.md) | Risikovurderingsverktøy (Excel) og brukerveiledning | Digdir | middels |
| [K20](kilder/K20-dt-dpia-liste.md) | Liste over behandlinger som alltid krever DPIA | Datatilsynet | høy |
| [K21](kilder/K21-dt-sjekkliste-dpia-faser.md) | Sjekkliste for DPIA-faser | Datatilsynet | høy |
| [K22](kilder/K22-dpia-eksempler.md) | Eksempeltabell: krever behandlingen DPIA? | Ukjent (trolig WP248) | middels |
| [K23](kilder/K23-cnil-risikoark.md) | Risikoark | CNIL | lav |
| [K24](kilder/K24-wp248-dpia.md) | WP248 rev.01: retningslinjer for DPIA | WP29/EDPB | høy |
| [K25](kilder/K25-wp259-samtykke.md) | WP259 rev.01: samtykke (erstattet av EDPB 05/2020) | WP29/EDPB | høy |
| [K26](kilder/K26-wp260-apenhet.md) | WP260 rev.01: åpenhet | WP29/EDPB | høy |
| [K27](kilder/K27-wp244-ledende-tilsynsmyndighet.md) | WP244 rev.01: ledende tilsynsmyndighet (erstattet av EDPB 8/2022) | WP29/EDPB | middels |
| [K28](kilder/K28-cnil-pia-metode.md) | PIA 1: metode (2015-utgave) | CNIL | høy |
| [K29](kilder/K29-cnil-pia-maler.md) | PIA 2: maler | CNIL | høy |
| [K30](kilder/K30-cnil-pia-kunnskapsbaser.md) | PIA 3: kunnskapsbaser (trussel- og tiltakskatalog) | CNIL | høy |
| [K31](kilder/K31-cnil-pia-tilkoblede-objekter.md) | PIA-eksempel: tilkoblede objekter (IoT) | CNIL | middels |
| [K32](kilder/K32-nsm-grunnprinsipper.md) | Grunnprinsipper for IKT-sikkerhet v2.1 | NSM | høy |
| [K33](kilder/K33-cnil-sikkerhetsguide.md) | Security of personal data: practice guide 2024 | CNIL | høy |
| [K34](kilder/K34-cnil-cybersikkerhet-2024.md) | Cybersecurity 2024 | CNIL | lav |
| [K35](kilder/K35-cnil-referentiel-audit.md) | Standard for revisjonsprosedyrer (2011) | CNIL | lav |
| [K36](kilder/K36-cnil-referentiel-digital-safe.md) | Standard for digitale safer (2014) | CNIL | lav |
| [K37](kilder/K37-sdm-standard-datavernmodell.md) | Standard-Datenschutzmodell v1.0 | DSK (DE) | middels |
| [K38](kilder/K38-tia-guide.md) | Practical guide: Transfer Impact Assessment (2025) | CNIL | høy |
| [K39](kilder/K39-cnil-mobilapper.md) | Anbefaling om mobilapper (2025) | CNIL | middels |
| [K40](kilder/K40-dpia-prosess-uld.md) | A Process for DPIA under GDPR (2016) | ULD/Fraunhofer | middels |
| [K41](kilder/K41-dcat-ap-no.md) | DCAT-AP-NO: beskrivelse av datasett | Digdir | lav |

Formatet for hver filtype står i [_KONVENSJONER.md](_KONVENSJONER.md).

---

## Vedlikehold

- **Ny kilde:** Legg filen i `ressurser/` og skriv et kildenotat `kilder/K42-….md` etter formatet i `_KONVENSJONER.md`. Oppdater deretter berørte temanotater og tabellen over.
- **Artikkelindeksen** genereres på nytt fra frontmatter (`gdpr_artikler`). Skriptet ligger i [_verktoy/build_index.py](_verktoy/build_index.py): `python _verktoy/build_index.py .`
- **Datatilsynet-PDF-ene** i `ressurser/Datatilsynet/` har ødelagt tekstlag (Type 3-fonter). De er derfor lest visuelt. Bruk nettadressen i frontmatter til kildenotatet hvis noe må kontrolleres.

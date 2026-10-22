---
id: K41
tittel: "Standard for beskrivelse av datasett, datatjenester og datakataloger (DCAT-AP-NO)"
utgiver: Digitaliseringsdirektoratet (Digdir)
dato: "v.3.0.7; publisert 2024-11-26 (v.3.0.0), gjeldende fra 2025-01-01, oppdatert 2026-03-20"
spraak: nb
fil: "ressurser/Digdir/dcat-ap-no_beskrivelse-av-datasett.pdf"
type: standard
gdpr_artikler: [30]
emner: [metadata, datakatalog, datasett, tilgangsnivå, informasjonsforvaltning, protokoll]
relevans: lav
---

# DCAT-AP-NO – Standard for beskrivelse av datasett, datatjenester og datakataloger (Digdir, 2024/2026)

## Sammendrag

DCAT-AP-NO er den norske applikasjonsprofilen av EUs DCAT-AP og W3Cs DCAT. Den angir hvilke opplysninger som skal, bør og kan tas med når offentlige virksomheter beskriver datasett, datatjenester (API-er) og datakataloger, og hvordan beskrivelsene representeres maskinlesbart i RDF. Standarden er en **metadatastandard** og ikke en personvernstandard: Søk i teksten etter «personopplysning», «behandlingsgrunnlag», «personvern» og «legal basis» gir ingen treff, bortsett fra én omtale av «begrensninger basert på personvern» i datatjenestens tilgangsrettigheter (s. 72–73). Standarden inneholder **ingen egne egenskaper for behandlingsgrunnlag** (som tidligere `dcatno:legalBasisFor…`). I stedet brukes **tilgangsrettigheter** (`dct:accessRights`: PUBLIC / RESTRICTED / NON_PUBLIC) og **gjeldende lovgivning** (`dcatap:applicableLegislation`, med ELI-lenke til Lovdata). Kilden er perifer for GDPR, men nyttig når virksomheten vil koble datakatalogen sin mot protokollen etter art. 30 eller dokumentere hvilke datasett som inneholder personopplysninger.

## Når skal agenten bruke denne kilden

- Når en offentlig virksomhet spør hvordan datasett med personopplysninger skal beskrives i Felles datakatalog (data.norge.no).
- Når man vil merke tilgangsnivå (åpne, begrensede, ikke-allmenne data) på datasett eller API-er.
- Når man vil knytte datasett til hjemmelslov/forskrift (gjeldende lovgivning).
- Når protokoll (art. 30), informasjonsforvaltning og datakatalog skal samordnes. Merk at dette er en egen tolkning – se merknadene.
- Ikke som kilde til materielle personvernkrav.

## Hovedinnhold

### 1. Formål, omfang og kravnivåer (kap. 1, s. 10–13)

- **Formål** (s. 10): legge til rette for utveksling av beskrivelser av datasett og datatjenester og gjøre det lettere å finne dem. Felles modell med kontrollerte vokabularer muliggjør maskinell utveksling, sammenstilling av metadata på tvers av kataloger og desentralisert publisering.
- Standarden **bør** benyttes når offentlige virksomheter skal etablere og utveksle oversikter over datasett og datatjenester i en katalog. Digitaliseringsrundskrivets krav om å registrere datasett i **Felles datakatalog (data.norge.no)** oppfylles ved å eksponere en DCAT-AP-NO-katalog på internett og administrere innhøsting via data.norge.no/publishing (s. 10).
- **Omfang** (s. 10): alle datasett (inkludert åpne data) og datatjenester i offentlig sektor som beskrives for oppføring i en katalog eller «inventarliste», intern eller ekstern. **Ikke** ment for å beskrive fagsystemer.
- Relaterte spesifikasjoner: HVD-DCAT-AP-NO (datasett med høy verdi), DQV-AP-NO (kvalitet), ModellDCAT-AP-NO (informasjonsmodeller, via `dct:conformsTo`), SKOS-AP-NO-Begrep (begreper, via `dct:subject`). Offentlige tjenester, organisasjoner og regler dekkes av **CPSV-AP-NO**, ikke av DCAT-AP-NO (s. 10–11, 154–155).
- **Kravnivåer** (s. 11, etter RFC 2119): SKAL/MÅ = absolutt krav; BØR = avvik bare av saklige grunner, med implikasjonene forstått og nøye vurdert; KAN = helt valgfritt.
- **Samsvar** (s. 12): en leverende applikasjon SKAL levere katalog, datasett, distribusjoner, datatjenester og aktører med minst de obligatoriske egenskapene og bruke de angitte kontrollerte vokabularene. En mottakende applikasjon SKAL kunne prosessere alle spesifiserte klasser, egenskaper og vokabularer. Egenskaper fra DCAT-AP/DCAT som ikke er tatt med i DCAT-AP-NO, kan brukes; andre egenskaper kan brukes, men det stilles ikke krav om at mottakere håndterer dem.
- Forvaltning: Digdir initierer nye versjoner; større versjoner sendes på høring og behandles av Arkitektur- og standardiseringsrådet (s. 11).

### 2. Forenklede minstekrav (kap. 2, s. 14–17)

| Ressurs | SKAL | BØR |
|---|---|---|
| **Katalog** | utgiver, kontaktpunkt, beskrivelse, tittel | inneholde datasett- og/eller datatjenestebeskrivelser (unngå tomme kataloger) |
| **Datasett** | utgiver, kontaktpunkt, beskrivelse, tittel, tema | tilgjengeliggjøres via distribusjoner og/eller datatjenester; opplysninger om **gjeldende lovgivning som gir mandat til opprettelse eller behandling** av datasettet |
| **Datatjeneste** | utgiver, kontaktpunkt, tittel, endepunktsURL | tilgjengeliggjøre datasett (unntak: rene prosesseringstjenester, inkl. lese-/skrive-API-er); opplysninger om gjeldende lovgivning som gir mandat til opprettelse eller forvaltning |

Eksempelet (s. 15–17) viser et datasett fra Statens vegvesen med `dcatap:applicableLegislation <https://lovdata.no/eli/forskrift/2016/12/15/1600>`.

### 3. Klassene (kap. 3, s. 18–134)

Klassene er sortert alfabetisk etter norsk navn, og egenskapene er gruppert som obligatoriske, anbefalte og valgfrie.

| Klasse | URI | Obligatoriske egenskaper | Anbefalte egenskaper (utvalg) |
|---|---|---|---|
| Aktør (s. 20) | foaf:Agent (subklasser org:Organization, foaf:Group, foaf:Person BØR brukes) | navn | identifikator (organisasjonsnummer fra Enhetsregisteret), type (ADMS publisher type) |
| **Datasett** (s. 23) | dcat:Dataset | beskrivelse, kontaktpunkt, tema (EU Data theme; Los BØR brukes i tillegg), tittel, utgiver (1..1) | begrep, ble generert ved, datasettdistribusjon, dekningsområde, **gjeldende lovgivning**, nøkkelord, tidsrom, **tilgangsrettigheter** |
| Datasettserie (s. 48) | dcat:DatasetSeries | beskrivelse, kontaktpunkt, tema, tittel, utgiver | dekningsområde, gjeldende lovgivning, siste, tidsrom |
| **Datatjeneste** (s. 59) | dcat:DataService | endepunktsURL, kontaktpunkt, tittel, utgiver | endepunktsbeskrivelse, format, gjeldende lovgivning, i samsvar med, nøkkelord, tema, tilgjengeliggjør datasett, tilgjengelighet (tilgangsrettigheter er *valgfri* her) |
| **Distribusjon** (s. 74) | dcat:Distribution | tilgangsURL | beskrivelse, format, lisens, status, tilgjengelighet (valgfritt: bl.a. policy `odrl:hasPolicy`, rettigheter, nedlastingslenke, gjeldende lovgivning) |
| Gebyr (s. 87) | cv:Cost | – | beløp, beskrivelse, dokumentasjon, valuta |
| Identifikator (s. 90) | adms:Identifier | notasjon | – |
| **Katalog** (s. 92) | dcat:Catalog | beskrivelse, kontaktpunkt, tittel, utgiver | datasett, datatjeneste, dekningsområde, endringsdato, hjemmeside, lisens, språk, temaer, utgivelsesdato |
| Katalogisert ressurs (s. 105) | dcat:Resource | – | – |
| Katalogpost (s. 106) | dcat:CatalogRecord (bruk er frivillig) | endringsdato, primærtema | i samsvar med, status, utgivelsesdato |
| Kontaktopplysning (s. 112) | vcard:Kind | navn | har e-post, har kontaktside |
| **Regulativ ressurs** (s. 115) | eli:LegalResource | – | beskrivelse, identifikator, referanse, språk, tittel, type (f.eks. direktiv, forordning) |
| Relasjon (s. 120) | dcat:Relationship | har rolle, relasjon | – |
| Rettighetserklæring (s. 121) | odrs:RightsStatement | – | anvendelsesretningslinjer, jurisdiksjon, krediteringstekst/-URL, opphavsrettserklæring, opphavsrettsinnehaver |
| Sjekksum, Standard, Tidsrom (s. 128–134) | spdx:Checksum, dct:Standard, dct:PeriodOfTime | (sjekksum: algoritme, verdi; standard: tittel) | – |

Forholdet mellom klassene (kap. 4.1, s. 135–136): Et **datasett** er den konseptuelle samlingen av data. En **distribusjon** er en spesifikk, nedlastbar representasjon (fil) av et datasett og skal alltid knyttes til et datasett. En **datatjeneste** gir tilgang til datasett (via `dcat:servesDataset`) eller tilbyr databehandlingsfunksjoner. Alt som ikke gir en nedlastbar representasjon, er en datatjeneste. Datatjenester bruker ofte autentisering og kryptering; distribusjoner bruker sjekksum.

### 4. Egenskaper som er relevante for personvern og tilgang

**Datasett – tilgangsrettigheter (`dct:accessRights`)** (s. 33–34)
- Brukes til å angi om det er allmenn tilgang, betinget tilgang eller ikke-allmenn tilgang til datasettet. Multiplisitet 0..1, **anbefalt** (norsk utvidelse: endret fra valgfri).
- Verdien SKAL være **PUBLIC**, **RESTRICTED** eller **NON_PUBLIC** fra EUs kontrollerte vokabular *Access right*. Tilsvarer tilgangsnivåene i steg 4 i Digdirs «Veileder for orden i eget hus»: allmenn tilgang («grønn») = PUBLIC, betinget tilgang («gul») = RESTRICTED, ikke-allmenn tilgang («rød») = NON_PUBLIC.
- Norsk utvidelse: Når verdien er RESTRICTED eller NON_PUBLIC, **BØR** «gjeldende lovgivning» (`dcatap:applicableLegislation`) brukes. Der RESTRICTED ikke er regulert av lovgivning, **BØR** «Distribusjon – policy (`odrl:hasPolicy`)» brukes.

**Datatjeneste – tilgangsrettigheter (`dct:accessRights`)** (s. 72–73)
- «Egenskapen brukes til å oppgi informasjon angående tilgang eller begrensninger basert på personvern, sikkerhet eller andre retningslinjer.» Valgfri, 0..1, samme tre verdier.

**Gjeldende lovgivning (`dcatap:applicableLegislation`)** (datasett s. 31–32; også på datasettserie, datatjeneste, distribusjon og katalog)
- For datasett: refererer til «lovgivningen som gir mandat til opprettelse eller behandling av datasettet». Verdiområde `eli:LegalResource`, 0..n, **anbefalt** (norsk utvidelse: endret fra valgfri). For Lovdata bør ELI-URI brukes.
- Klassen **Regulativ ressurs** (`eli:LegalResource`, s. 115) representerer lovgivning, retningslinjer eller politikk som regulerer katalogen eller ressursen.

**Ble generert ved (`prov:wasGeneratedBy`)** (s. 29–30)
- Anbefalt (norsk utvidelse). Refererer til aktiviteten som genererte datasettet eller gir forretningskontekst. Verdien BØR hentes fra Digdirs vokabular *Proveniensaktivitetstype*, f.eks. `administrative-decision` (vedtak), `collecting-from-third-party` (innhenting fra tredjepart) og `collecting-from-user` (innhenting fra brukeren).

**Kap. 4.3 – lisens, tilgangsrettigheter, rettigheter og policy** (s. 138)
1. `dct:license` SKAL brukes for lisens, med verdi fra EUs vokabular *Licence* (datatjeneste, distribusjon, katalog).
2. `dct:accessRights` SKAL brukes for tilgangsrettigheter (PUBLIC/RESTRICTED/NON_PUBLIC) (datasett, datatjeneste).
3. `dct:rights` KAN brukes for andre rettigheter og bruksvilkår, bl.a. opphavsrett; strukturert via `odrs:RightsStatement` anbefales (distribusjon, katalog).
- W3C/DCAT anbefaler ODRL for spesielle bruksvilkår, med referanse via `odrl:hasPolicy` på distribusjon.

**Andre relevante egenskaper:** utgiver (`dct:publisher`, organisasjonsnummer-URI, s. 27–28), kontaktpunkt (obligatorisk), tema, begrep (`dct:subject`), tidsrom, frekvens, eierskapshistorikk (`dct:provenance`), annen ansvarlig aktør (`prov:qualifiedAttribution`, f.eks. distributør).

### 5. Endringer fra v2.2 (Vedlegg C, s. 153–161)

- Versjon 3 er basert på summen av DCAT-AP 3.0 og DCAT (ikke lenger BRegDCAT-AP).
- Nytt: «gjeldende lovgivning» på datasett, datasettserie, datatjeneste, distribusjon og katalog; klassene Gebyr, Kontaktopplysning og Rettighetserklæring.
- Klassene Offentlig organisasjon, Offentlig tjeneste og Regel (`cpsv:Rule`) er ikke lenger spesifisert, fordi behovet er dekket av CPSV-AP-NO. Egenskapen `cpsv:follows` er tatt ut.
- `dct:identifier` er ikke lenger obligatorisk (URI-en er identifikator, kap. 4.5).
- Endringsloggen nevner ingen `dcatno`-egenskaper for behandlingsgrunnlag. Navnerommet `dcatno` er definert (Vedlegg A, s. 140), men den uttrukne teksten viser ingen egenskaper i det som gjelder personopplysninger.

## Praktiske sjekkpunkter

- Kontroller at hvert datasett har de obligatoriske egenskapene: tittel, beskrivelse, utgiver, kontaktpunkt og tema.
- Sett `dct:accessRights` på alle datasett. Datasett med personopplysninger vil normalt være RESTRICTED eller NON_PUBLIC **[Merknad – ikke fra kilden]**.
- Ved RESTRICTED/NON_PUBLIC: oppgi `dcatap:applicableLegislation` med ELI-lenke til Lovdata. Mangler lovregulering for RESTRICTED, bruk `odrl:hasPolicy` på distribusjonen.
- Bruk `prov:wasGeneratedBy` for å vise hvordan dataene oppsto (vedtak, innhenting fra tredjepart, innhenting fra brukeren).
- Bruk riktig egenskap til riktig formål: lisens (`dct:license`), tilgang (`dct:accessRights`) og øvrige vilkår (`dct:rights`).
- Bruk ikke standarden til å beskrive fagsystemer. Offentlige tjenester og regler hører til CPSV-AP-NO.

## Viktige sitater

- «Formålet med standarden er å legge til rette for utveksling av beskrivelser av datasett og datatjenester, og å lette søk etter datasett og datatjenester.» (s. 10)
- «Standarden er ikke tenkt brukt for å beskrive fagsystem.» (s. 10)
- «BØR inneholde opplysninger om gjeldende lovgivning som gir mandat til opprettelse eller behandling av datasettet» (s. 15)
- «Egenskapen brukes til å angi om det er allmenn tilgang, betinget tilgang eller ikke-allmenn tilgang til datasettet.» (s. 33)
- «Verdien SKAL være PUBLIC, RESTRICTED eller NON_PUBLIC fra EU's kontrollerte vokabular Access right.» (s. 34)
- «Egenskapen brukes til å oppgi informasjon angående tilgang eller begrensninger basert på personvern, sikkerhet eller andre retningslinjer.» (s. 73)

## Kryssreferanser

- GDPR: art. 30 (protokoll) – bare indirekte. Kilden nevner ikke GDPR.
- Andre kilder:
  - [K04](K04-dt-fore-protokoll.md) og [K11](K11-art30-protokollmaler.md) – protokollkrav og maler som datakatalogen kan kobles mot.
  - [K02](K02-dt-behandlingsgrunnlag.md) – behandlingsgrunnlag. DCAT-AP-NO har bare «gjeldende lovgivning», som ikke er det samme.
  - [K13](K13-dt-innebygd-personvern.md) – innebygd personvern og oversikt over dataflyt.

## Aktualitet og begrensninger

- Versjon 3.0.7 er gjeldende fra 2025-01-01 og ble oppdatert 2026-03-20. Standarden er norsk, primært rettet mot offentlig sektor, og bygger på DCAT-AP 3.0.
- Standarden regulerer metadata, ikke personvern. Den har ingen felt for behandlingsgrunnlag etter art. 6/9, formål, kategorier av registrerte, mottakere eller sletting.
- Figurene (1–21) er ikke med i tekstutdraget.
- **[Merknad – ikke fra kilden]** Mulig kobling mot protokollen etter art. 30: datasettets URI kan refereres fra protokollens behandlingsaktiviteter (eller omvendt). `dct:publisher` og `dcat:contactPoint` tilsvarer behandlingsansvarlig og kontaktopplysninger. `dcatap:applicableLegislation` kan peke på den supplerende rettslige hjemmelen (art. 6 nr. 3) eller særlovgivning, men erstatter ikke en vurdering av behandlingsgrunnlag. `dct:accessRights` og `odrl:hasPolicy` kan speile tilgangsstyring og utleveringsbegrensninger. `prov:wasGeneratedBy` med «innhenting fra tredjepart» eller «fra brukeren» kan støtte vurderingen av om art. 13 eller art. 14 gjelder. Behandlingsformål, kategorier av registrerte og personopplysninger, mottakere, overføringer, slettefrister og sikkerhetstiltak må dokumenteres i protokollen. Ev. egne utvidelser (egne egenskaper) er tillatt etter kap. 1.5.3, men mottakere som data.norge.no er ikke forpliktet til å prosessere dem.
- **[Merknad – ikke fra kilden]** Eldre versjoner av DCAT-AP-NO (1.x) hadde egenskaper for skjermingshjemmel, utleveringshjemmel og behandlingsgrunnlag (`dcatno:legalBasisForRestriction`, `…ForProcessing`, `…ForAccess`). Disse finnes ikke i denne versjonen. Sjekk på data.norge.no om eksisterende katalogdata fortsatt bruker dem.

---
id: K36
tittel: "Decision No. 2014-017 of 23 January 2014 adopting a standard for the delivery of privacy seals concerning digital safe boxes (référentiel coffres-forts numériques)"
utgiver: CNIL (Commission nationale de l'informatique et des libertés, Frankrike)
dato: "2014-01-23 (vedtak nr. 2014-017)"
spraak: en
fil: "ressurser/referentiel_cfn_en.pdf"
type: standard
gdpr_artikler: [5, 9, 13, 17, 20, 25, 28, 32, 33, 34, 42, 44]
emner: [digitalt-hvelv, skylagring, kryptering, ende-til-ende-kryptering, nøkkelhåndtering, sletting, portabilitet, sertifisering, personvernmerke, autentisering, logging]
relevans: lav
---

# CNIL-standard for personvernmerke for digitale hvelv (CNIL, 2014)

## Sammendrag

Vedtak nr. 2014-017 fastsetter CNILs standard for å tildele **personvernmerke (privacy seal/label)** til **digitale hvelv** («coffres-forts numériques», digital safe boxes) – tjenester som tilbyr privatpersoner sikker, digital lagring av dokumenter. Et digitalt hvelv skiller seg fra vanlig lagring ved at dokumentene og metadataene **bare er tilgjengelige for innehaveren og personer vedkommende uttrykkelig har gitt fullmakt**. Standarden har **22 kumulative krav**: 2 om søkerens etterlevelsestilnærming (ED01–ED02) og 20 om selve tjenesten (ES01–ES20) fordelt på behandlede data, tilgang, lagring/sletting, informasjon, risikostyring og kryptografi. Sentralt er krav om at kryptering kan gjøre data uleselige **også for leverandøren** (klientsidekryptering med brukerkontrollerte nøkler), sletting innen én måned i sikkerhetskopier, gratis eksportverktøy, varsel ved tredjepartstilgang, trusselvurdering og uavhengig kontroll hvert tredje år, og sterk autentisering.

For kunnskapsbasen er standarden et konkret eksempel på høye krav til en lagrings-/skytjeneste og kan brukes som inspirasjon for tekniske krav i databehandleravtaler og DPIA for tjenester som lagrer sensitive dokumenter.

## Når skal agenten bruke denne kilden

- Når en tjeneste for **lagring av privatpersoners dokumenter** (digital postkasse, dokumenthvelv, skylagring) skal vurderes eller kravspesifiseres.
- Ved formulering av krav om **kryptering der leverandøren ikke har tilgang** (nøkler kontrollert av brukeren), nøkkelgjenoppretting via betrodd tredjepart, og varsling ved tredjepartstilgang.
- Ved krav til **sletting i sikkerhetskopier** (frist) og **dataportabilitet/eksport** ved bytte av leverandør.
- Som referanse for periodiske krav (trusselvurdering, samsvarsanalyse og uavhengig verifisering minst hvert tredje år).

## Hovedinnhold

### Rettsgrunnlag og bakgrunn (s. 1–2)

- Hjemmel: Europarådets konvensjon 108, **direktiv 95/46/EF**, fransk personvernlov 78-17 art. 11 nr. 3 bokstav c og art. 13, dekret 2005-1309, CNILs internreglement (vedtak 2013-175) og **CNILs anbefaling 2013-270 av 19. september 2013 om digitale hvelv for privatpersoner**.
- En bransjeorganisasjon ba om et merke for digitale hvelv; CNIL fant at det svarte til et behov og ønsket å beskytte personopplysninger privatpersoner lagrer i slike hvelv.
- Internreglementet art. 33: CNIL vedtar standarder som definerer egenskapene produkter/prosedyrer må ha, vurderingsmåte og etterkontroll.

### Innledning (s. 3–4)

- **Definisjon:** tilbud til privatpersoner om dematerialisert og sikker lagring av data med formål å oppbevare dokumenter digitalt. Hvelvet skal sikre **integritet, tilgjengelighet og konfidensialitet** og ha egnede sikkerhetstiltak.
- **Skille mot vanlig lagring:** data, inkludert dokumenter og metadata, er tilgjengelig **kun for innehaveren** og ev. fysiske personer innehaveren har gitt særskilt fullmakt.
- **Målet med standarden:** sikker oppbevaring og beskyttelse av personopplysninger i hvelvet, tilgjengelig kun for brukeren og personer med fullmakt.
- Utarbeidet på grunnlag av CNILs anbefalinger, koherent med andre sertifiseringsprosesser.
- **22 kumulative krav** i to vurderingsfaser: søkerens etterlevelsestilnærming (ED, 2 krav) og beskyttelse av data i hvelvet (ES, 20 krav).
- **Bevis:** begrunnet dokumentasjon (utdrag fra intern standard, beskrivelse av systemets funksjon eller prosedyre o.l.); ikke bare gjentakelse av kravene. For ES15, ES17 og ES19 *(teksten angir disse; kryptokravene er i praksis ES16–ES20)* kan bevis gis ved beskrivelse av algoritmer og dimensjonering med henvisning til vedlegg B1 og B2 i det generelle sikkerhetsreferansedokumentet (RGS).
- **Roller:**
  - *produsent* – utformer og utvikler hvelvproduktet;
  - *operatør* (technical operator) – implementerer hvelvet og sikrer drift og sikkerhetstiltak;
  - *leverandør* (supplier) – tilbyr tjenesten til brukere som er fysiske personer.
- Søkeren må være **både teknisk operatør og leverandør** for å søke alene. Leverer operatøren tjenesten til en organisasjon som er leverandør overfor privatpersoner, må operatør og leverandør søke **sammen**.

### Terminologi (s. 4–5)

| Begrep | Definisjon |
|---|---|
| Digitalt lagringsområde | Tjeneste for lagring av dematerialiserte dokumenter |
| Digitalt hvelv (elektronisk hvelv) | Særlig form for lagringsområde der tilgjengelighet og integritet sikres og kun brukeren (og personer med særskilt fullmakt) har tilgang til dokumenter og metadata |
| Metadata | Data som beskriver eller styrer dokumentene. To typer: brukerskapte (navn, format, opprettelsesdato, beskrivelse, søkeord) og operatørskapte (arkiveringsdato, størrelse, hashverdi). I standarden menes bare **brukerskapte** metadata. |
| Teknisk operatør | Juridisk person som implementerer hvelvet og sikrer drift og sikkerhetstiltak |
| Leverandør | Juridisk person som tilbyr hvelvet til brukere |
| Bruker | Fysisk person som bruker hvelvet |

### Kapittel 1 – Søkerens etterlevelsestilnærming (s. 5)

| ID | Krav |
|---|---|
| ED01 | Søkeren har en tilnærming som sikrer etterlevelse av personvernloven for **alle** behandlinger i alle aktiviteter, inkludert hvelvet. |
| ED02 | Søkerens behandlinger, inkludert brukeradministrasjonen, har vært gjenstand for nødvendige forhåndsformaliteter overfor CNIL (melding/konsesjon). |

### Kapittel 2 – Personvern i det digitale hvelvet (s. 6–9)

#### 2.1 Behandlede data

| ID | Krav |
|---|---|
| ES01 | Ved kontoopprettelse samles kun **relevante og forholdsmessige** identifikasjonsdata. Innehaveren kan **aldri identifiseres ved personnummer** (fransk NIR/RNIPP). |
| ES02 | Uten godkjenning for lagring av helsedata (fransk «hébergeur de données de santé») skal brukeren informeres om at det er **forbudt å lagre helseopplysninger**; tjenesten skal ikke opprette standardmapper for helse. |
| ES03 | Brukeren informeres om at det er forbudt å lagre ulovlig innhold (f.eks. oppfordring til drap, rasehat, overgrepsmateriale mot barn). |

#### 2.2 Tilgang

| ID | Krav |
|---|---|
| ES04 | Hvelvet tillater kun at dokumentene konsulteres av brukeren og ev. personer med særskilt fullmakt (f.eks. notarius for å gi arvinger tilgang, ektefelle ved felles område). |

#### 2.3 Lagring og sletting

| ID | Krav |
|---|---|
| ES05 | Dokumenter brukeren har slettet endelig, og deres metadata, slettes **overalt**: **uten opphold** i løpende lagring og online-kopier (speiling/sanntidssynkronisering), og **innen maksimalt én måned** i sikkerhetskopier (inkrementelle, fulle). |
| ES06 | Kontinuitet i lagringen: brukerne varsles **minst én måned før** tjenesten legges ned, slik at de kan hente dokumentene. |
| ES07 | **Gratis verktøy** for å hente ut hele innholdet enkelt, uten komplekse eller repeterende handlinger, i **strukturert og vanlig brukt elektronisk format**, for å lette leverandørbytte – uten å samle inn konfidensiell informasjon (bankidentifikatorer, passord til nettjenester o.l.). |

#### 2.4 Informasjon til brukerne (ES08)

Søkeren informerer brukerne på forhånd om:
- identiteten til operatøren og leverandøren;
- formål(ene);
- at det **ikke finnes mottakere** av dataene (dokumenter og metadata);
- eventuell **overføring til stat utenfor EU**, og om denne staten etter egen lovgivning kan kreve **direkte tilgang** til dataene;
- retten til innsyn, retting og protest og hvordan de utøves;
- muligheten til å gi fullmakt (f.eks. gjenoppretting ved tapt nøkkel, arvingers tilgang ved dødsfall);
- type lagringsområde og bruksvilkår;
- tekniske mekanismer, særlig **krypteringsmekanismene**;
- prosedyrer for oppsigelse og uthenting av data;
- ved tjenester som henter dokumenter fra tredjepartstjenester: konsekvensene av at søkeren bruker brukerens brukernavn og passord for å logge inn i brukerens navn.

#### 2.5 Risikostyring og etterlevelse

| ID | Krav |
|---|---|
| ES09 | **Samsvarsanalyse** mot gjeldende referanser før idriftsetting og deretter **hvert tredje år**, med minst: liste over krav (EU, lov, forskrift, sektor, kontrakt), liste over beste praksis søkeren forplikter seg til (normer, sektorstandarder, interne regler), og forklaring på hvordan hver referanse oppfylles eller begrunnelse for hvorfor ikke. |
| ES10 | **Trusselvurdering**, revidert minst **hvert tredje år**, med minst: alle trusler mot tilgjengelighet, integritet og konfidensialitet via utnyttelse av IT-, fysiske, menneskelige eller organisatoriske sårbarheter, fra interne/eksterne, menneskelige/ikke-menneskelige, utilsiktede/tilsiktede kilder; tekniske og ikke-tekniske tiltak (eksisterende/planlagte) før, under og etter; anslag på **gjenværende sannsynlighet** for hver trussel. |
| ES11 | Verktøy for å **blokkere robotinnlogging** og forsinke og/eller blokkere illegitime innloggingsforsøk fra personer. |
| ES12 | Tiltak for integritet og tilgjengelighet (redundant lagringssenter, jevnlige sikkerhetskopier); søkeren sikrer **garantier for erstatning** til brukere om tiltakene svikter (f.eks. forsikring). |
| ES13 | **Logging** som lar brukeren se nylig aktivitet i hvelvet (f.eks. tidsstemplede vellykkede og mislykkede innlogginger, IP-adresse og protokoll, operasjoner på mapper og filer, hvem som utførte, hvilket objekt og hva slags operasjon). |
| ES14 | **Uavhengig verifisering** (ekstern revisor, internkontrollfunksjon) av tiltakenes effektivitet minst **hvert tredje år**, med korrigerende tiltak. |
| ES15 | Søkeren **varsler brukeren ved enhver tilgang til dataene fra tredjepart uten fullmakt**, selv om dataene er kryptert. |

#### 2.6 Kryptografiske mekanismer

| ID | Krav |
|---|---|
| ES16 | Funksjon for kryptering/dekryptering av lagrede data inkl. dokumenter og metadata som: kan gjøre dataene **uforståelige for tredjeparter uten fullmakt, inkludert søkeren selv** (f.eks. klientprogramvare som krypterer lokalt før opplasting slik at søkeren teknisk ikke kan dekryptere); lar brukeren og representanter dekryptere og vise data; følger ANSSIs regler og anbefalinger om valg og dimensjonering (RGS); er basert på **nøkler kontrollert av brukeren** og representantene; tillater økning av nøkkelstørrelse og bytte av algoritmer for **langsiktig konfidensialitet**. |
| ES17 | Funksjon for **sikkerhetskopi og gjenoppretting av nøkler** dersom brukeren mister dem: enten sikret hos brukeren, eller hos en **betrodd tredjepart** uavhengig av søkeren og valgt av brukeren – tredjeparten må sikre nøkkelkopiene, logge all bruk og informere brukeren om bruk. |
| ES18 | **Kryptering av all overføring** til og fra hvelvet, iht. ANSSIs regler for valg og dimensjonering. |
| ES19 | Autentiseringsmekanismer for: brukere; personer med særskilt fullmakt; tredjeparter brukeren bruker for å importere data; og IT-administratorer – **kun for administrasjon** av hvelvet. |
| ES20 | Kun **robust autentisering** (engangspassord, koder via SMS o.l.); brukeren og fullmektiger autentiseres av serveren som har dataene; alt iht. ANSSIs RGS. Ved passord: brukeren informeres om reglene (f.eks. visning av passordstyrke), og passord kontrolleres (blokkering hvis utilstrekkelig). |

## Praktiske sjekkpunkter

- Kontroller at en dokumentlagringstjeneste for privatpersoner kun gir tilgang til brukeren og personer med uttrykkelig fullmakt, og at også metadata beskyttes (ES04, ES16).
- Kontroller om leverandøren teknisk kan lese dataene; der høy konfidensialitet kreves, still krav om klientsidekryptering med brukerkontrollerte nøkler og mulighet for algoritmebytte (ES16).
- Kontroller at det finnes en trygg ordning for nøkkelgjenoppretting (hos bruker eller uavhengig betrodd tredjepart med logging og varsling) (ES17).
- Kontroller sletterutiner: umiddelbart i produksjon/speil og innen fastsatt frist (her én måned) i sikkerhetskopier (ES05).
- Kontroller at brukere kan eksportere alt innhold gratis i strukturert format og varsles i god tid før nedleggelse (ES06–ES07).
- Kontroller at brukerne informeres om overføringer utenfor EU/EØS og om tredjelands myndigheter kan kreve tilgang (ES08).
- Kontroller at brukeren varsles ved uautorisert tredjepartstilgang, selv til krypterte data (ES15).
- Kontroller at det finnes trusselvurdering, samsvarsanalyse og uavhengig verifisering med fast intervall (her minst hvert tredje år) (ES09, ES10, ES14).
- Kontroller sterk autentisering, robot-/brute force-beskyttelse og brukertilgjengelig aktivitetslogg (ES11, ES13, ES19–ES20).
- Kontroller at personnummer ikke brukes som identifikator der det ikke er nødvendig (ES01).

## Viktige sitater

- «A digital safe box is distinguished from an ordinary storage space by the fact that the data retained, including stored documents and their meta data, is accessible only to the holder of the safe box and, where applicable, natural persons whom the holder has specifically authorised for this purpose.» (s. 3)
- «It contains twenty-two requirements, all cumulative» (s. 3)
- «within a maximum period of one month for backups» (ES05, s. 6)
- «can make the data incomprehensible to third parties not mandated by the user, including to the applicant» (ES16, s. 8)
- «The applicant shall notify the user in case of any access to their data by a third-party not mandated by the user, even if this data is encrypted.» (ES15, s. 8)
- «indicating whether this State, based on its own legislation, can make requests to directly access the retained data» (ES08, s. 7)

## Kryssreferanser

- GDPR **[Merknad – ikke fra kilden: koblingen er utledet; standarden bygger på direktiv 95/46 og fransk lov]**: art. 5 nr. 1 bokstav c og e (minimering, lagringsbegrensning – ES01, ES05); art. 9 (helseopplysninger – ES02); art. 13 (informasjon – ES08); art. 17 (sletting – ES05); art. 20 (dataportabilitet – ES07, standarden foregriper denne retten); art. 25 (innebygd personvern – ES16); art. 28 (operatør som databehandler for leverandør); art. 32 (sikkerhet – ES10–ES20); art. 33–34 (varsling – ES15 går lenger); art. 42 (sertifisering); art. 44 flg. og art. 48 (overføring, tredjelands myndighetstilgang – ES08).
- Andre kilder:
  - [K10](K10-dt-kryptering.md) – Datatilsynet om kryptering.
  - [K33](K33-cnil-sikkerhetsguide.md) – CNILs sikkerhetsguide (ark 21 kryptografi, ark 22 sky – «server-side encryption» gir ikke konfidensialitet overfor leverandøren).
  - [K35](K35-cnil-referentiel-audit.md) – søsterstandard (revisjonsprosedyrer) fra samme merkeordning.
  - [K14](K14-dt-overforing-utenfor-eos.md), [K38](K38-tia-guide.md) – overføring og vurdering av tredjelands tilgang.

## Aktualitet og begrensninger

- **[Merknad – ikke fra kilden]** Standarden er fra 2014 og bygger på **direktiv 95/46/EF** og fransk lov før GDPR (bl.a. «prior formalities» i ED02, som ikke lenger finnes).
- **[Merknad – ikke fra kilden]** CNILs nasjonale merkeordning («labels») ble avviklet ved overgangen til GDPR i 2018; standarden gir ikke grunnlag for gyldig merke i dag. Sertifisering skjer nå etter GDPR art. 42–43. Frankrike har senere regulert «coffres-forts numériques» i lov (Loi pour une République numérique 2016) med ANSSI-/forskriftsbaserte krav.
- Henvisninger til ANSSIs RGS (vedlegg B1/B2), fransk personnummer (NIR/RNIPP) og fransk godkjenning for helsedatalagring er franske. **[Merknad – ikke fra kilden]** I Norge vil tilsvarende krav følge av bl.a. Normen for helsesektoren, NSMs kryptografiske anbefalinger og regler om bruk av fødselsnummer (popplyl. § 12).
- Kravene om én måneds sletting i backup og tre års intervaller er standardens egne valg, ikke GDPR-krav, men kan brukes som referansepunkt for «state of the art».
- Relevansen er satt til lav fordi standarden gjelder en snever tjenestetype og er historisk; enkeltkrav (ES05, ES07, ES15, ES16, ES17) er likevel nyttige som modellkrav.

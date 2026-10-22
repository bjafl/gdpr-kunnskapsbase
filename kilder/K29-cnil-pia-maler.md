---
id: K29
tittel: "PIA, templates"
utgiver: CNIL (Commission Nationale de l'Informatique et des Libertés, Frankrike)
dato: "Februar 2018 (February 2018 edition)"
spraak: en
fil: "ressurser/cnil-pia-2-en-templates.pdf"
type: mal
gdpr_artikler: [5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18, 20, 21, 28, 32, 35, 44, 45, 46, 47, 48, 49]
emner: [dpia, pia, mal, risikovurdering, grunnleggende-prinsipper, rettigheter, databehandler, overføring, sikkerhetstiltak, handlingsplan, validering]
relevans: høy
---

# PIA, templates (CNIL, 2018)

## Sammendrag

Andre av CNILs tre PIA-guider (2018-utgaven, GDPR-tilpasset): et sett **utfyllbare maltabeller** som følger strukturen i CNILs PIA-metode: 1. Kontekst, 2. Grunnleggende prinsipper, 3. Datasikkerhetsrisikoer, 4. Validering. Malene dekker beskrivelse av behandlingen, data/mottakere/lagringstid, prosesser og støtteressurser, behandlingsgrunnlag, minimering, kvalitet, lagringstid, informasjon, samtykke, innsyn/portabilitet, retting/sletting, begrensning/innsigelse, databehandlere, overføringer ut av EU, sikkerhetstiltak (data-spesifikke, generelle, organisatoriske), risikoanalyse for de tre fryktede hendelsene, risikokart, handlingsplan, DPO-råd, de registrertes syn og formell validering. Dokumentet er 25 sider. Malene er laget med et tilkoblet produkt i tankene (flere felt nevner enhet, app, smarttelefon), og valideringsteksten er lånt fra eksemplet med en tilkoblet leke ([K31](K31-cnil-pia-tilkoblede-objekter.md)). CNIL understreker at malene er et hjelpemiddel som bør tilpasses hver kontekst og brukes sammen med metodeguiden (s. 1–2).

## Når skal agenten bruke denne kilden

- Når agenten skal **sette opp eller fylle ut en DPIA-mal**: bruk tabellene under direkte som skjelett (de er gjengitt fullstendig, med norsk forklaring av hvert felt).
- Når agenten skal **kvalitetssikre en eksisterende DPIA**: sjekk at hver tabell/hvert felt er dekket.
- Når agenten skal lage **oppsummeringer for beslutningstaker** (vurderingstabeller, risikokart, handlingsplan, DPO-råd, validering).
- For hva som skal stå i feltene (tiltakskatalog, skalaer, trusler): se [K30](K30-cnil-pia-kunnskapsbaser.md). For utfylte eksempler: se [K31](K31-cnil-pia-tilkoblede-objekter.md).

## Hovedinnhold

### Forord (s. 2)

- Metodikken består av tre guider: én for tilnærmingen, én med maler for å formalisere analysen, én med kunnskapsbaser (tiltakskatalog og eksempler). Kan lastes ned fra https://www.cnil.fr/en/privacy-impact-assessments-cnil-publishes-its-pia-manual.
- «Privacy» = alle grunnleggende rettigheter og friheter (GDPR, EU-charteret art. 7 og 8, DP-Act art. 1). «PIA» = PIA og DPIA om hverandre.
- «Attention: the templates presented in this guide constitute an aid to the implementation of the approach. It is entirely possible and even desirable to adapt them to each particular context.»

Gjennomgående kolonnetyper:
- **«Implementation or justification why not»** – beskriv hvordan tiltaket gjennomføres, eller begrunn hvorfor ikke.
- **«Acceptable / can be improved on?»** – vurderers konklusjon.
- **«Corrective controls»** – tilleggstiltak vurderer krever.
- **«Internal data / External data»** (rettighetskapitlene) – tiltak for henholdsvis interne og eksterne data.

---

### Del 1 – Kontekst (s. 4)

#### 1.1 Oversikt over behandlingen

**Tabell: Beskrivelse av behandlingen**

| Felt | Forklaring |
|---|---|
| Description of the processing | Behandlingens art, omfang, kontekst m.m. (fotnote 1) |
| Processing purposes | Formålene |
| Processing stakes | Innsatser/forventede fordeler |
| Controller | Behandlingsansvarlig |
| Processor(s) | Databehandler(e) |

**Tabell: Sektorspesifikke standarder som gjelder behandlingen** (GDPR art. 35 nr. 8 – godkjente atferdsnormer m.m.)

| Standards applicable to the processing | Consideration |
|---|---|
| (standard/norm, f.eks. atferdsnorm, sertifisering, sikkerhetspolicy) | (hvordan den er tatt hensyn til) |

#### 1.2 Data, prosesser og støtteressurser

**Tabell: Data, mottakere og lagringstid**

| Data types | Recipients | Storage duration |
|---|---|---|

**Prosesser og støtteressurser** – «[insert a diagram of data flows and a detailed description of the processes carried out]»

| Processes | Detailed description of the process | Data supporting assets |
|---|---|---|

---

### Del 2 – Grunnleggende prinsipper (s. 5–12)

#### 2.1 Tiltak som sikrer behandlingens proporsjonalitet og nødvendighet

**Tabell: Formål**

| Purposes | Legitimacy |
|---|---|

**Tabell: Behandlingsgrunnlag (lawfulness)**

| Lawfulness criteria | Applicable | Justification |
|---|---|---|
| The data subject has given consent to the processing of his or her personal data for one or more specific purposes (art. 6 nr. 1 a) | | |
| Processing is necessary for the performance of a contract to which the data subject is party or in order to take steps at the request of the data subject prior to entering into a contract (b) | | |
| Processing is necessary for compliance with a legal obligation to which the controller is subject (c) | | |
| Processing is necessary in order to protect the vital interests of the data subject or of another natural person (d) | | |
| Processing is necessary for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller (e) | | |
| Processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject ..., in particular where the data subject is a child (f) – gjelder ikke offentlige myndigheter i utførelsen av sine oppgaver (fotnote 4) | | |

(Fotnote 3: om samtykke og informasjon, se kap. 2.2.)

**Tabell: Dataminimering** (overskrift «Minimization controls»)

| Details about the data processed | Data categories | Justification of the need and relevance of the data | Minimization controls |
|---|---|---|---|

**Tabell: Datakvalitet**

| Data quality controls | Justification |
|---|---|

**Tabell: Lagringstid**

| Data types | Storage duration | Justification of the storage duration | Erasure mechanism at the end of the storage duration |
|---|---|---|---|
| Common data (vanlige data) | | | |
| Archived data (arkiverte data) | | | |
| Functional traces (funksjonelle spor) | | | |
| Technical logs (tekniske logger) | | | |

**Tabell: Vurdering av tiltakene (proporsjonalitet og nødvendighet)**

| Controls guaranteeing the proportionality and necessity of the processing | Acceptable / can be improved on? | Corrective controls |
|---|---|---|
| Purposes: specified, explicit and legitimate | | |
| Basis: lawfulness of processing, prohibition of misuse | | |
| Data minimization: adequate, relevant and limited | | |
| Data quality: accurate and kept up-to-date | | |
| Storage durations: limited | | |

#### 2.2 Tiltak som beskytter de registrertes rettigheter (s. 7–12)

**Informasjon til de registrerte** – hvis unntak fra informasjonsplikten (DP-Act art. 32; GDPR art. 12, 13, 14):

| Exemption from having to inform the data subjects | Justification |
|---|---|

Ellers:

| Controls for the right to information | Implementation | Implementation justification or justification why not |
|---|---|---|
| Presentation of the terms & conditions for use/confidentiality | | |
| Possibility of accessing the terms & conditions for use/confidentiality | | |
| Legible and easy-to-understand terms | | |
| Existence of clauses specific to the device | | |
| Detailed presentation of the data processing purposes (specified objectives, data matching where applicable, etc.) | | |
| Detailed presentation of the personal data collected | | |
| Presentation of any access to the identifiers of the device, the smartphone/tablet or computer, by specifying whether these identifiers are communicated to third parties | | |
| Presentation of the user's rights (consent withdrawal, data erasure, etc.) | | |
| Information on the secure data storage method, particularly in the event of sourcing | | |
| Arrangements for contacting the company (identity and contact details) about confidentiality issues | | |
| Where applicable, information for the user on any change concerning the data collected, the purposes and confidentiality clauses | | |
| Regarding transmission of data to third parties: – detailed presentation of the purposes of transmission to third parties | | |
| – detailed presentation of the personal data transmitted | | |
| – indication of the identity of third-party bodies | | |

**Samtykke** (der behandlingsgrunnlaget er samtykke, fotnote 5):

| Controls for obtaining consent | Implementation | Implementation justification or justification why not |
|---|---|---|
| Express consent during registration | | |
| Consent segmented per data category or processing type | | |
| Express consent prior to sharing data with other users | | |
| Consent presented in an intelligible and easily accessible form, using clear and plain language adapted to the target user (particularly for children) | | |
| Obtaining parents' consent for minors under 13 years of age | | |
| For a new user, consent must once again be obtained | | |
| After a long period without use, the user must be asked to confirm his/her consent | | |
| Where the user has consented to the processing of special data (e.g. his/her location), the interface clearly indicates that said processing takes place (icon, light) | | |
| Where the user changes device, smartphone or computer, reinstalls the mobile app or deletes his/her cookies, the settings associated with his/her consent are maintained | | |

**Innsyn og dataportabilitet** – hvis unntak fra innsynsretten (DP-Act art. 39 og 41; GDPR art. 15):

| Exemption from the right of access | Justification | Arrangements for responding to the data subjects |
|---|---|---|

Ellers:

| Controls for the right of access | Internal data | External data | Justification |
|---|---|---|---|
| Possibility of accessing all of the user's personal data, via the common interfaces | | | |
| Possibility of securely consulting the traces of use associated with the user | | | |
| Possibility of downloading an archive of all the personal data associated with the user | | | |

Der portabilitet gjelder (GDPR art. 20):

| Controls for the right to data portability | Internal data | External data | Justification |
|---|---|---|---|
| Possibility of retrieving, in an easily reusable format, personal data provided by the user, so as to transfer them to another service | | | |

**Retting og sletting** – hvis unntak (DP-Act art. 41; GDPR art. 17):

| Exemption from the rights to rectification and erasure | Justification | Arrangements for responding to the data subjects |
|---|---|---|

Ellers:

| Controls for the rights to rectification and erasure | Internal data | External data | Justification |
|---|---|---|---|
| Possibility of rectifying personal data | | | |
| Possibility of erasing personal data | | | |
| Indication of the personal data that will nevertheless be stored (technical requirements, legal obligations, etc.) | | | |
| Implementing the right to be forgotten for minors | | | |
| Clear indications and simple steps for erasing data before scrapping the device | | | |
| Advice given about resetting the device before selling it | | | |
| Possibility of erasing the data in the event the device is stolen | | | |

**Begrensning og innsigelse** – hvis unntak (DP-Act art. 38; GDPR art. 21):

| Exemption from the rights to restriction and to object | Justification | Arrangements for responding to the data subjects |
|---|---|---|

Ellers:

| Controls for the rights to restriction and to object | Internal data | External data | Justification |
|---|---|---|---|
| Existence of "Privacy" settings | | | |
| Invitation to change the default settings | | | |
| "Privacy" settings accessible during registration | | | |
| "Privacy" settings accessible after registration | | | |
| Existence of a parental control system for children under 13 years of age | | | |
| Compliance in terms of tracking (cookies, advertising, etc.) | | | |
| Exclusion of children under 13 years of age from automated profiling | | | |
| Effective exclusion of processing the user's data in the event consent is withdrawn | | | |

**Databehandlere** (s. 11)

| Processor's name | Purpose | Scope | Contract reference | Compliance with Art. 28 |
|---|---|---|---|---|

Fotnote 6: det skal inngås en databehandleravtale med hver databehandler som fastsetter alle elementer i GDPR art. 28: varighet, omfang, formål, dokumenterte instrukser, forhåndsgodkjenning ved bruk av (under)databehandler, tilgang til dokumentasjon som viser etterlevelse, rask varsling av brudd m.m.

**Overføring ut av EU** (s. 12)

| Data sets and storage location | France | EU | Country recognized as providing adequate protection by the EU | Other country | Justification and supervision (standard contractual clauses, internal corporate regulations) |
|---|---|---|---|---|---|

(For norsk bruk: erstatt «France» med «Norge» og «EU» med «EU/EØS» – **[Merknad – ikke fra kilden]**.)

**Tabell: Vurdering av tiltak for de registrertes rettigheter**

| Controls to protect the rights of data subjects | Acceptable / can be improved on? | Corrective controls |
|---|---|---|
| Information for the data subjects (fair and transparent processing) | | |
| Obtaining consent | | |
| Exercising the rights of access and to data portability | | |
| Exercising the rights to rectification and erasure | | |
| Exercising the rights to restriction of processing and to object | | |
| Processors: identified and governed by a contract | | |
| Transfers: compliance with the obligations bearing on transfer of data outside the European Union | | |

---

### Del 3 – Datasikkerhetsrisikoer (s. 13–20)

#### 3.1 Vurdering av sikkerhetstiltak

Felles kolonner for alle tre tabeller: **Tiltak | Implementation or justification why not | Acceptable/can be improved on? | Corrective controls**. Tekst i klammer er CNILs veiledning for hva som skal fylles inn.

**Tabell A – Tiltak som gjelder spesifikt dataene som behandles (s. 13–14)**

| Tiltak | Veiledning for feltet «Implementation or justification why not» |
|---|---|
| Encryption | Beskriv midler for konfidensialitet for lagrede data (database, flate filer, sikkerhetskopier m.m.) og prosedyren for nøkkelhåndtering (opprettelse, lagring, bytte ved mistanke om kompromittering m.m.). Beskriv krypteringsmidler for dataflyter (VPN, TLS m.m.). |
| Anonymization | Angi om anonymiseringsmekanismer er implementert, hvilke og til hvilket formål. |
| Data partitioning (in relation to the rest of the information system) | Angi om partisjonering av behandlingen er planlagt og hvordan. |
| Logical access control | Angi om brukerprofiler er definert og tildelt. Spesifiser autentiseringsmidler. Angi passordregler der relevant (minimumslengde, tegnkrav, gyldighetstid, antall mislykkede forsøk før låsing m.m.). |
| Traceability (logging) | Angi om hendelser logges og hvor lenge sporene lagres. |
| Integrity monitoring | Angi om mekanismer for integritetsovervåking av lagrede data er implementert, hvilke og hvorfor. Spesifiser integritetskontroll på dataflyter. |
| Archiving | Beskriv arkivforvaltningsprosessene (avlevering, lagring, konsultasjon m.m.) under ditt ansvar. Spesifiser arkivroller (opprinnelseskontor, avleverende enheter m.m.) og arkivpolicy. Angi om data kan falle inn under offentlige arkiver. |
| Paper document security | Der papirdokumenter brukes: angi hvordan de skrives ut, lagres, destrueres og utveksles. |

**Tabell B – Generelle sikkerhetstiltak for systemet behandlingen skjer i (s. 15–17)**

| Tiltak | Veiledning |
|---|---|
| Operating security | Beskriv hvordan programvareoppdateringer (operativsystemer, applikasjoner m.m.) og sikkerhetsrettinger gjennomføres. |
| Clamping down on malicious software | Angi om antivirus er installert og oppdateres jevnlig på arbeidsstasjonene. |
| Managing workstations | Beskriv tiltak på arbeidsstasjoner (automatisk låsing, brannmur m.m.). |
| Website security | Angi om ANSSIs «recommendations for securing websites» er implementert. |
| Backups | Angi hvordan sikkerhetskopier håndteres og om de lagres på et sikkert sted. |
| Maintenance | Beskriv fysisk vedlikehold av maskinvare og om det er satt ut. Angi om fjernvedlikehold av applikasjoner er tillatt og på hvilke vilkår. Angi om defekt utstyr håndteres særskilt. |
| Security of computer channels (networks) | Angi nettverkstype (isolert, privat eller Internett). Spesifiser brannmur, inntrengingsdeteksjon eller andre aktive/passive enheter for nettverkssikkerhet. |
| Monitoring | Angi om sanntidsovervåking av lokalnettet er implementert og med hvilke midler. Angi om maskinvare- og programvarekonfigurasjoner overvåkes. |
| Physical access control | Angi fysisk adgangskontroll til lokalene (soner, eskorte av besøkende, adgangskort, låste dører m.m.) og om det finnes varslingsprosedyrer ved innbrudd. |
| Hardware security | Angi tiltak for fysisk sikkerhet for servere og arbeidsstasjoner (sikker lagring, sikkerhetskabler, personvernfiltre, sikker sletting før kassering m.m.). |
| Avoiding sources of risk | Angi om lokasjonen er utsatt for naturkatastrofer (flomsone, nærhet til kjemisk industri, jordskjelv- eller vulkansone m.m.) og om farlige produkter lagres i samme område. |
| Protecting against non-human sources of risks | Beskriv brannforebygging, -deteksjon og -slukking; tiltak mot vannskade; overvåking og reserve for strømforsyning. |

**Tabell C – Organisatoriske tiltak (styring/governance) (s. 18–19)**

| Tiltak | Veiledning |
|---|---|
| Organization | Angi om roller og ansvar for personvern er definert; om en person er ansvarlig for etterlevelse av personvernregelverket; om det finnes en oppfølgingskomité (eller tilsvarende) for styring og oppfølging av personverntiltak. |
| Policy (management of rules) | Angi om det finnes et IT-reglement (eller tilsvarende) om personvern og korrekt bruk av IT-ressurser. |
| Risk management | Angi om personvernrisikoen ved nye behandlinger vurderes, om det skjer systematisk og etter hvilken metode; om det finnes en organisasjonsomfattende kartlegging av personvernrisiko. |
| Project management | Angi om tester utføres på ikke-reelle/anonyme data. |
| Management of incidents and data breaches | Angi om IT-hendelser håndteres etter en dokumentert og testet prosedyre. |
| Personnel management | Angi bevisstgjøringstiltak for nyansatte og tiltak når personer med tilgang til data slutter. |
| Relations with third parties | For databehandlere som trenger tilgang til data: angi sikkerhetstiltak og ordninger for slik tilgang. |
| Supervision | Angi om personverntiltakenes effektivitet og egnethet overvåkes. |

#### 3.2 Risikovurdering: potensielle personvernbrudd (s. 20)

**Tabell: Analyse og vurdering av risiko**

| Risk | Main risk sources | Main threats | Main potential impacts | Main controls reducing the severity and likelihood | Severity | Likelihood |
|---|---|---|---|---|---|---|
| Illegitimate access to data (uautorisert tilgang) | | | | | | |
| Unwanted change of data (uønsket endring) | | | | | | |
| Disappearance of data (forsvinning) | | | | | | |

**Tabell: Vurdering av risikoene (residual risiko)**

| Risks | Acceptable / can be improved on? | Corrective controls | Residual severity | Residual likelihood |
|---|---|---|---|---|
| Illegitimate access to data | [Vurderer avgjør om eksisterende eller planlagte (allerede igangsatte) tiltak reduserer risikoen tilstrekkelig til at den kan aksepteres.] | [Eventuelle tilleggstiltak som er nødvendige.] | | |
| Unwanted change of data | [som over] | [som over] | | |
| Disappearance of data | [som over] | [som over] | | |

Skalaer for alvorlighet og sannsynlighet (1 Negligible, 2 Limited, 3 Significant, 4 Maximum): se [K30](K30-cnil-pia-kunnskapsbaser.md) §1.5–1.6.

---

### Del 4 – Validering av PIA (s. 21–25)

#### 4.1 Forberedelse av materialet for validering

**Syntese: etterlevelse av GDPR for tiltak som sikrer de grunnleggende prinsippene** – tegnforklaring (caption) med symboler for: *Non applicable*, *Unsatisfactory*, *Planned improvement*, *Acceptable*.

| Controls selected to ensure compliance with the fundamental principles | Assessment |
|---|---|
| *Controls guaranteeing the proportionality and necessity of the processing* | |
| Purpose(s): specified, explicit and legitimate | |
| Basis: lawfulness of processing, prohibition of misuse | |
| Data minimization: adequate, relevant and limited | |
| Quality of data: accurate and kept up-to-date | |
| Storage durations: limited | |
| *Controls to protect the personal rights of data subjects* | |
| Information for the data subjects (fair and transparent processing) | |
| Obtaining consent | |
| Exercising the right of access and right to data portability | |
| Exercising the rights to rectification and erasure | |
| Exercising the right to restriction of processing and right to object | |
| Processors: identified and governed by a contract | |
| Transfers: compliance with the obligations bearing on transfer of data outside the European Union | |

**Syntese: etterlevelse av god sikkerhetspraksis for tiltak mot datasikkerhetsrisiko** (s. 22)

| Controls implemented for treating the risks related to data security | Assessment |
|---|---|
| *Controls bearing specifically on the data being processed* | |
| Encryption | |
| Anonymization | |
| Data partitioning (in relation to the rest of the information system) | |
| Logical access control | |
| Traceability (logging) | |
| Integrity monitoring | |
| Archiving | |
| Paper document security | |
| *General security controls regarding the system in which the processing is carried out* | |
| Operating security | |
| Clamping down on malicious software | |
| Managing workstations | |
| Website security | |
| Backups | |
| Maintenance | |
| Security of computer channels (networks) | |
| Monitoring | |
| Physical access control | |
| Hardware security | |
| Avoiding sources of risk | |
| Protecting against non-human sources of risks | |
| *Organizational controls (governance)* | |
| Organization | |
| Policy (management of rules) | |
| Risk management | |
| Project management | |
| Management of incidents and data breaches | |
| Personnel management | |
| Relations with third parties | |
| Supervision | |

**Kartlegging av risiko (Mapping of risks related to data security)** (s. 23) – en 4×4-matrise:

| Alvorlighet \ Sannsynlighet | 1. Negligible | 2. Limited | 3. Significant | 4. Maximum |
|---|---|---|---|---|
| **4. Maximum** | | | | |
| **3. Significant** | | | | |
| **2. Limited** | | | | |
| **1. Negligible** | | | | |

De tre risikoene (Illegitimate access to data, Unwanted change to data, Disappearance of data) plasseres i matrisen (malen viser dem plassert både som initiale og residuale/korrigerte posisjoner; plasseringen i malen er illustrativ).

**Handlingsplan (Elaboration of action plan)** (s. 24)

| Additional controls requested | Manager | Frequency | Difficulty | Cost | Progress |
|---|---|---|---|---|---|

(Skalaer for vanskelighetsgrad, kostnad, termin og fremdrift: se [K30](K30-cnil-pia-kunnskapsbaser.md) §1.10.)

**Dokumentasjon av rådet fra den som har ansvar for personvern (DPO)** (GDPR art. 35 nr. 2) – fast tekst:

> «On dd/mm/yyyy, the Data Protection Officer of the company X issued the following opinion concerning the compliance of the processing and PIA study carried out: … [Signature]»

**Dokumentasjon av de registrertes eller deres representanters syn** (GDPR art. 35 nr. 9) – fast tekst:

> «The data subjects [were/were not] consulted [and expressed the following view on the compliance of the processing in light of the study performed]: …
> Justification of the data controller's decision: …»

#### 4.2 Formell validering av PIA (s. 25)

Eksempeltekst (fra tilkoblet leke-eksemplet):

> «On dd/mm/yyyy, the Managing Director of the company X validates the PIA for the processing of the connected toy, in light of the study carried out, in his capacity as data controller.
> The purposes of the processing are to enable the child to be interactive, through the possibility of dialogue with the toy (questions/answers in natural language by voice recognition), enable the child to communicate online (send voice messages, texts and photos) with his/her friends and/or parents and feed information back to the parents (surveillance device).
> This is because the controls planned for complying with the fundamental principles underpinning privacy protection and for addressing the risks to the privacy of data subjects have been deemed acceptable in light of these stakes. The implementation of additional controls will nevertheless have to be demonstrated, as will continuous improvement of the PIA. [Signature]»

Struktur for en valideringstekst: dato – hvem validerer (i egenskap av behandlingsansvarlig) – hvilken behandling – formålene – begrunnelse (tiltak for grunnprinsipper og risiko akseptable sett opp mot innsatsene) – forbehold (tilleggstiltak skal dokumenteres, kontinuerlig forbedring) – signatur.

---

### Samlet DPIA-skjelett (avledet av malene)

1. Kontekst: beskrivelse (behandling, formål, innsatser, behandlingsansvarlig, databehandlere) · standarder · data/mottakere/lagringstid · dataflytdiagram og prosesser/støtteressurser.
2. Grunnleggende prinsipper: formål · behandlingsgrunnlag · minimering · kvalitet · lagringstid · vurdering (5 linjer) · informasjon · samtykke · innsyn/portabilitet · retting/sletting · begrensning/innsigelse · databehandlere · overføringer · vurdering (7 linjer).
3. Risiko: sikkerhetstiltak A (8 data-tiltak), B (12 generelle), C (8 organisatoriske) · risikoanalyse for 3 fryktede hendelser · residualvurdering.
4. Validering: syntese prinsipper (12 linjer) · syntese sikkerhet (28 linjer) · risikokart · handlingsplan · DPO-råd · de registrertes syn · formell validering.

## Praktiske sjekkpunkter

- Kontroller at hvert tiltak har enten en beskrivelse av implementering **eller** en begrunnelse for hvorfor det ikke er implementert – tomme felt er ikke akseptable.
- Kontroller at lagringstid er fastsatt separat for vanlige data, arkiverte data, funksjonelle spor og tekniske logger, med slettemekanisme for hver.
- Kontroller at minst ett behandlingsgrunnlag er markert som «Applicable» med begrunnelse, og at grunnlag (e) eller (c) viser til rettsgrunnlag i unionsretten/nasjonal rett.
- Kontroller at hver databehandler er listet med formål, omfang, avtalereferanse og om avtalen oppfyller art. 28.
- Kontroller at hvert datasett har angitt lagringssted (land) og overføringsgrunnlag der det er utenfor EU/EØS.
- Kontroller at alle 28 sikkerhetstiltak i tabell A–C er vurdert (eller eksplisitt «ikke relevant»).
- Kontroller at risikotabellen har risikokilder, trusler, konsekvenser, tiltak, alvorlighet og sannsynlighet for alle tre fryktede hendelser, og at residual alvorlighet/sannsynlighet er angitt etter korrigerende tiltak.
- Kontroller at alle korrigerende tiltak fra vurderingstabellene er overført til handlingsplanen med ansvarlig, frekvens/frist, vanskelighetsgrad, kostnad og fremdrift.
- Kontroller at DPO-rådet er datert og signert, og at det er dokumentert om de registrerte ble konsultert – og begrunnelse hvis ikke, eller hvis behandlingsansvarlig går mot deres syn.
- Kontroller at valideringen er signert av behandlingsansvarlig (ledelsen), med formål og begrunnelse.
- Tilpass malene: felt knyttet til «device», «mobile app», «cookies» og «children under 13» er IoT-/forbrukerorienterte og kan være irrelevante for andre behandlinger.

## Viktige sitater

- «It is entirely possible and even desirable to adapt them to each particular context.» (s. 2)
- «these templates may have to be adapted, and should be used as a complement to the guide "PIA, methodology".» (gjentas på hver side)
- «A processing contract must be signed with each processor, setting out all of the aspects stipulated in Art. 28 of the [GDPR]» (s. 11, fotnote 6)
- «[The assessor must determine whether the existing or planned controls (already undertaken) sufficiently reduce this risk for it to be deemed acceptable.]» (s. 20)
- «The implementation of additional controls will nevertheless have to be demonstrated, as will continuous improvement of the PIA.» (s. 25)

## Kryssreferanser

- GDPR: art. 35 nr. 7 (minimumsinnhold), nr. 2 (DPO-råd), nr. 8 (atferdsnormer), nr. 9 (de registrertes syn); art. 5, 6, 7, 8, 12–21, 28, 32, 44–49.
- [K28](K28-cnil-pia-metode.md) – metoden malene følger.
- [K30](K30-cnil-pia-kunnskapsbaser.md) – innholdet i feltene: tiltakskatalog, skalaer, trusler.
- [K31](K31-cnil-pia-tilkoblede-objekter.md) – malene utfylt for en tilkoblet leke (samme struktur, med kolonner per enhet/app/konto).
- [K24](K24-wp248-dpia.md) – WP248 vedlegg 2: kriterier for en akseptabel DPIA (kan brukes til å sjekke malen).
- [K05](K05-dt-databehandleravtale.md) – databehandleravtale (art. 28-kolonnen).
- [K14](K14-dt-overforing-utenfor-eos.md), [K38](K38-tia-guide.md) – overføring og TIA (overføringstabellen).
- [K11](K11-art30-protokollmaler.md) – protokoll etter art. 30 (kilde for kontekstdelen).
- [K12](K12-dt-dpia-veiledning.md), [K21](K21-dt-sjekkliste-dpia-faser.md) – Datatilsynets DPIA-veiledning/sjekkliste.

## Aktualitet og begrensninger

- Utgaven er GDPR-tilpasset (februar 2018), men inneholder fortsatt henvisninger til den gamle franske DP-Act (art. 32, 38, 39, 41) og til ANSSI-anbefalinger; overføringstabellen har en egen kolonne for «France».
- Aldersgrensen «under 13 years» i samtykke- og innsigelsestabellene er CNILs valg i malen. **[Merknad – ikke fra kilden]** GDPR art. 8 setter 16 år som utgangspunkt med nasjonal adgang til å senke til 13; Norge har valgt 13 år (personopplysningsloven § 5), Frankrike 15 år.
- Overføringstabellen nevner standardkontrakter og «internal corporate regulations» (BCR). **[Merknad – ikke fra kilden]** Etter Schrems II (EU-domstolen C-311/18, 2020) må overføringer på standardkontrakter normalt suppleres med en overføringskonsekvensvurdering (TIA), og nye standardkontrakter (2021/914) gjelder.
- **[Merknad – ikke fra kilden]** CNILs PIA-programvare (åpen kildekode) implementerer i praksis samme struktur som disse malene.

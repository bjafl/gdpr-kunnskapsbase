---
id: K40
tittel: "A Process for Data Protection Impact Assessment under the European General Data Protection Regulation"
utgiver: "Bieker, Friedewald, Hansen, Obersteller, Rost – ULD Schleswig-Holstein (Unabhängiges Landeszentrum für Datenschutz) og Fraunhofer ISI; publisert i Rannenberg/Ikonomou (red.), Privacy Technologies and Policy, APF 2016 (Springer)"
dato: "2016 (Annual Privacy Forum 2016, Frankfurt)"
spraak: en
fil: "ressurser/apf2016.pdf"
type: artikkel
gdpr_artikler: [5, 25, 32, 33, 34, 35, 36, 40, 42]
emner: [dpia, risikovurdering, beskyttelsesmål, sdm, metode, grunnrettigheter]
relevans: middels
---

# A Process for Data Protection Impact Assessment under the European GDPR (ULD/Fraunhofer, 2016)

## Sammendrag

Fagartikkel (konferansebidrag til Annual Privacy Forum 2016) skrevet av forskere ved den tyske tilsynsmyndigheten ULD i Schleswig-Holstein og Fraunhofer ISI. Artikkelen analyserer kravene til vurdering av personvernkonsekvenser (DPIA) i GDPR art. 35 og foreslår en DPIA-prosess i tre faser: **forberedelse**, **evaluering** og **rapport og tiltak**. Prosessen bygger på erfaringer fra EU-prosjektene PIAF og SAPIENT og på Standard Data Protection Model (SDM, Standard-Datenschutzmodell) med seks **beskyttelsesmål** (tilgjengelighet, integritet, konfidensialitet, ikke-kobling, åpenhet, intervenerbarhet). Sentralt er at risikoen vurderes fra **den registrertes perspektiv** (ikke virksomhetens), at enhver behandling er et inngrep i grunnrettigheter som må begrunnes, at det **ikke finnes akseptabel restrisiko** i samme forstand som i ordinær risikostyring, og at beskyttelsesbehovet er minst «normalt». Risikoevalueringen gjøres som en mål/faktisk-sammenligning (target/actual) mot en katalog av referansetiltak. Målgruppen er behandlingsansvarlige og tilsynsmyndigheter.

## Når skal agenten bruke denne kilden

- Når en DPIA skal struktureres i faser og trinn, særlig med SDM-beskyttelsesmålene som analyseramme.
- Når brukeren spør om forskjellen mellom DPIA-risiko (risiko for den registrerte) og virksomhetens risikostyring, eller om «akseptabel restrisiko».
- Ved fastsettelse av beskyttelsesnivå (normal / høy / svært høy) for en behandling.
- Ved identifisering av mulige «angripere» – også interne og legitime aktører, inkl. den behandlingsansvarlige selv.
- Når man trenger generiske tiltak knyttet til hvert beskyttelsesmål (tabell 1).
- Som teoretisk bakgrunn for SDM-metoden (se [K37](K37-sdm-standard-datavernmodell.md)).

## Hovedinnhold

Artikkelen har ikke sidetall i den tilgjengelige teksten; henvisningene gjelder seksjonsnumre (§).

### 1. Innledning (§ 1)

- GDPR art. 35 innfører for første gang en rettslig plikt til DPIA. En DPIA er et instrument for å identifisere og analysere risiko for enkeltpersoner (i rollene som borgere, kunder, pasienter osv.) som følger av at en organisasjon bruker en teknologi eller et system; på bakgrunn av analysen velges og gjennomføres tiltak.
- Tilsynsmyndighetene beskrives som «logical proponents» av en helhetlig, operasjonell modell.

### 2. Tidligere PIA-modeller (§ 2)

- Under direktiv 95/46 fantes ingen DPIA-plikt, men WP29 stilte generelle krav til PIA (RFID- og smart grid-rammeverkene, WP175/WP209): evaluering av personvernrisiko og bruk av beskyttelsesmål; særlige krav for særlige kategorier; etterlevelse av rettslige krav kan ikke være valgfritt og gir ingen skjønnsmargin.
- ICO (UK) og til dels CNIL følger en **sjekklistetilnærming**, som gjør det lett å gjennomføre, men gir risiko for å fokusere på punktene fremfor de konkrete risikoene.

**ICOs PIA Code of Practice – seks faser (§ 2.1):**
1. Undersøke behovet for vurdering og omfang (avhenger av sensitivitet og ressurser).
2. Kartlegge dataflyter i alle faser, inkl. tilgangsrettigheter.
3. Identifisere personvernrisikoer og mulige løsninger.
4. Overvåking av brukere eller tap av data påvirker ikke bare brukernes rettigheter, men gir også finansiell risiko for organisasjonen.
5. Dataminimering, opplæring og tekniske sikkerhetstiltak; trinnvis risikohåndtering fra eliminering til aksept, men rettslige forpliktelser må oppfylles.
6. Resultatene sikres og innarbeides i prosjektplanen. Interne og eksterne konsultasjoner i alle faser.

**CNILs PIA-metode (§ 2.2):** Kontinuerlig syklus: definisjon av behandlingen (formål, berørte personer, forholdsmessighet, eksisterende/planlagte kontroller) → identifisere og vurdere risiko (hvor alvorlig handlinger, unnlatelser, omstendigheter og verktøy griper inn i rettighetene; rangert etter alvorlighet og sannsynlighet) → beslutte om resultatet er tilfredsstillende eller om vurderingen må gjentas; rapport til tilsynsmyndigheten på forespørsel. (Se [K28](K28-cnil-pia-metode.md).)

### 3. Rettslige krav (§ 3)

**3.1 Når DPIA skal gjennomføres:**
- Art. 35 nr. 1: når behandlingen, ut fra art, omfang, sammenheng og formål, sannsynligvis medfører **høy risiko** for de registrertes rettigheter og friheter. Art. 35 nr. 3: (a) systematisk og omfattende vurdering av personlige aspekter basert på automatisert behandling, inkl. profilering, med beslutninger som har rettsvirkning eller tilsvarende betydelig påvirkning; (b) storskala behandling av særlige kategorier eller opplysninger om straffedommer; (c) systematisk storskala overvåking av offentlige områder.
- **Risikobegrepet:** Vurderingen etter art. 35 nr. 1 må ikke forveksles med vanlig risikostyring, som gjelder risiko for organisasjonen. Art. 35 gjelder risiko for individets rettigheter og friheter. Derfor finnes **ingen akseptabel restrisiko**, og **enhver behandling av personopplysninger er et inngrep** som må begrunnes.
- Art. 35 nr. 11: gjennomgang ved behov, i det minste ved endret risiko. Europaparlamentets forslag om obligatorisk gjennomgang annethvert år ble ikke vedtatt, men endret risiko er bare én av grunnene; også ny teknologi (f.eks. som muliggjør dataminimering) og endrede behandlingsmåter kan utløse gjennomgang.
- Art. 35 nr. 4 og 5 (lister): forfatterne mener det kan være nyttig å liste flere høyrisikotilfeller (f.eks. stordata, enhver behandling av særlige kategorier etter art. 9 nr. 1), men at tilsynsmyndighetene **ikke bør** utarbeide unntakslister etter art. 35 nr. 5.
- Art. 35 nr. 10 (offentlige myndigheter der DPIA er gjort i lovgivningsprosessen): forfatterne advarer om at lovgivning er generell og ikke fanger risikoer på implementeringsstadiet, og at personvernfremmende teknologi kan ha kommet senere. **Hver konkrete implementering bør ha egen spesifikk DPIA**, som kan bygge på den generelle.

**3.2 Minstekrav til innholdet (art. 35 nr. 7):**
- (a) systematisk beskrivelse av behandlingen og formålene, inkl. ev. berettiget interesse;
- involvering av de registrerte der det er hensiktsmessig (art. 35 nr. 9);
- (b) nødvendighet og forholdsmessighet; (c) risikoen for de registrertes rettigheter;
- (d) tiltak for å håndtere risikoen, inkl. garantier, sikkerhetstiltak og mekanismer, og for å påvise etterlevelse av GDPR som helhet – f.eks. tiltak ved brudd på personopplysningssikkerheten (art. 33 og 34).
- Art. 35 nr. 8: etterlevelse av godkjente atferdsnormer (art. 40) skal tas i betraktning, men må også ta hensyn til de registrertes rettigheter og interesser.
- En DPIA-rapport kan lette **sertifisering** (art. 42), men ren lovetterlevelse bør ikke garantere sertifisering; innebygd personvern (art. 25) bør også være oppfylt.
- GDPR har ingen eksplisitte krav til dokumentasjonsform; art. 36 nr. 1 (forhåndsdrøfting) og art. 36 nr. 3 bokstav e (DPIA skal gis tilsynsmyndigheten).

### 4. DPIA-prosessen (§ 4)

Prosessen (figur 1 i artikkelen) er avledet fra analyse av eksisterende prosesser, testet i PIAF og SAPIENT (i samarbeid med Trilateral Research). Den skal gi **reproduserbare og etterprøvbare** resultater (slik at tilsynsmyndigheten kan kontrollere), gjøre det mulig å **sammenligne alternative løsninger**, og være **teknologinøytral**. Den har tre faser:

| Fase | Trinn |
|---|---|
| **A. Forberedelse** (Preparation Stage, § 4.1) | 0. Vurder om DPIA er påkrevd → 1. Planlegg vurderingen (mål, omfang, team, DPO) → 2. Bruk SDM som rammeverk → 3. Definer evalueringsobjektet (target of evaluation) → 4. Identifiser involverte aktører/berørte personer → 5. Identifiser relevante rettslige krav → 6. Dokumenter i en **scoping-rapport** |
| **B. Evaluering** (Evaluation Stage, § 4.2) | 7. Identifiser beskyttelsesmål → 8. Identifiser potensielle angripere, motiver og mål → 9. Fastsett evalueringskriterier og beskyttelsesnivå (normal/høy/svært høy) → 10. Evaluer risiko (mål/faktisk-sammenligning mot referansetiltak) → nødvendighet og forholdsmessighet |
| **C. Rapport og tiltak** (Report and Safeguards Stage, § 4.3) | 11. Identifiser og implementer egnede tiltak (handlingsplan) → 12. Dokumenter og publiser evalueringsrapport → 13. Revisjon av resultatene (uavhengig tredjepart) → 14. Oppfølging og videreføring (gjenta ved endringer) |

(Nummereringen av trinnene er lagt til her for oversikt; overskriftene følger artikkelen.)

#### A. Forberedelsesfasen (§ 4.1)

- **Plikt til DPIA:** Vurder art. 35 nr. 1 og 3 (profilering, særlige kategorier av personopplysninger, systematisk overvåking av offentlige steder) og tilsynsmyndighetenes lister etter art. 35 nr. 4 og 5.
- **Planlegging av vurderingen (Projecting the Assessment):** Fastsett mål og omfang. Personellet må ha tilstrekkelige ressurser og kompetanse for en objektiv analyse. **Ideelt bør den som er ansvarlig for utvikling og implementering, være ansvarlig for DPIA-en**, bistått av en nøytral part (f.eks. kvalitetssikring). Personvernombudet skal rådspørres (art. 35 nr. 2).
- **Standard Data Protection Model:** SDM er nyttig for å vise at et system oppfyller personvernkravene og for å finne egnede tiltak. En forhåndsdefinert liste over evalueringskriterier, referanseverdier og tiltak gjør resultatene sporbare for tilsyn og offentlighet. Hovedformålet er **åpenhet** (art. 35 nr. 9), **ikke** at den behandlingsansvarlige skal krysse av en liste i stedet for å vurdere de konkrete risikoene.
- **Evalueringsobjektet (Target of Evaluation):** definerer DPIA-ens omfang. Her utarbeides den systematiske beskrivelsen etter art. 35 nr. 7 bokstav a. Omfatter særlig: dataene og deres lagrings- og overføringsformater (protokoller), IT-systemene og grensesnittene, samt prosesser, prosedyrer og funksjonelle roller. En DPIA **kan ikke begrenses til én komponent eller funksjon**, men må beskrive objektet i sin helhet – teknisk og organisatorisk – inkl. alle brukstilfeller og formål. Prinsippene om formålsbegrensning (art. 5 nr. 1 b) og dataminimering (art. 5 nr. 1 c) må etterleves, og motstridende interesser avveies.
- **Involverte aktører og berørte personer:** Både de som deltar i utvikling/drift (og dermed er potensielle angripere) og alle som berøres, f.eks.:
  - produsenten av testobjektet,
  - operatører, f.eks. databehandlere (datasentre, internettleverandører),
  - den behandlingsansvarliges ansatte,
  - de registrerte i sine roller som borgere, pasienter, kunder, ansatte osv.,
  - tredjeparter som får kjennskap til opplysninger, tilfeldig (personer som er til stede) eller med vilje (sikkerhetstjenester).
- **Relevante rettslige krav:** GDPR regulerer ikke alt; nasjonalt handlingsrom (f.eks. offentlig sektor, helse og trygd art. 9 nr. 2 bokstav h) og sektorlovgivning (telekom, trygd, taushetsplikt, vern av mindreårige). Siden DPIA gjelder prosesser og teknikk, er slike regler bare relevante hvis de implementeres direkte i prosessen.
- **Dokumentasjon:** Resultatene dokumenteres etter standardisert prosedyre i en **scoping-rapport**.

#### B. Evalueringsfasen (§ 4.2)

**Beskyttelsesmål (SDM, figur 2).** Personvernkravene i lovverket operasjonaliseres som beskyttelsesmål, kjent fra informasjonssikkerhet:

| Nr. | Beskyttelsesmål | Definisjon i artikkelen |
|---|---|---|
| 1 | Tilgjengelighet (availability) | Data er tilgjengelige, forståelige og kan behandles i tide av autoriserte enheter |
| 2 | Integritet (integrity) | Pålitelighet og ikke-benektbarhet – uendrede, autentiske og korrekte data |
| 3 | Konfidensialitet (confidentiality) | Hemmelighold, dvs. at visse enheter i IT-systemet ikke røpes |
| 4 | Ikke-kobling (unlinkability) | Data kan ikke kobles på tvers av domener og/eller brukes til andre formål enn det opprinnelige |
| 5 | Åpenhet (transparency) | De registrerte kjenner alle relevante forhold ved behandlingen av sine opplysninger |
| 6 | Intervenerbarhet (intervenability) | Kontroll for de registrerte, den behandlingsansvarlige og tilsynsmyndigheten over personopplysningene |

- Mål 1–3 er de klassiske IT-sikkerhetsmålene; 4–6 er personvernspesifikke. Fotnote: art. 32 nr. 1 bokstav b nevner i tillegg **robusthet (resilience)**.
- Målene representerer **den registrertes perspektiv**: Brudd på åpenhet (f.eks. manglende informasjon) er en risiko som må håndteres i DPIA-en, selv om dataene er trygt lagret – å ikke vite hvem som behandler data til hvilket formål og ikke kunne gripe inn, krenker rettighetene.
- Hvert mål har avledede delmål som kan utledes fra GDPR; alternativt kan personvernprinsippene knyttes til et mål. **Lovlighetskontrollen (behandlingsgrunnlag) passer ikke inn i modellen og må gjøres før DPIA-en.**
- Målene står i et **dobbelt spenningsforhold** (styrking av ett kan svekke motparten); evalueringen må finne riktig balanse. Eksempel: høy konfidensialitet begrenser tilgjengelighet (fire-øyne-prinsipp, papirarbeid, spesiell maskinvare for klartekst).

**Potensielle angripere, motiver og mål.** I DPIA er perspektivet de berørtes, ikke organisasjonens. Angripere kan også være **regelfølgende interne brukere** (ansatte, kontraktører). Målet er å beskytte rettighetene og interessene til kunder, ansatte osv., ikke forretningsprosesser. Vurder om disse utgjør en risiko:
- *Offentlige myndigheter:* sikkerhetstjenester (departement, politi, etterretning, militære), velferdsforvaltning/trygd, statistikkbyråer, sviktende myndigheter som åpner rom for ulovlig virksomhet.
- *Virksomheter:* teknologiselskaper, systemintegratorer, IT-leverandører (tilgang, innhold osv.); banker, forsikring; kredittopplysning, adresse- og datahandlere; reklamebyråer; interessegrupper og lobbyister; arbeidsgivere.
- *Helsesektoren:* sykehus, leger; offentlige og private helseforsikrere.
- *Forskning:* medisinsk og samfunnsvitenskapelig forskning; universiteter.

Det er en interessekonflikt når organisasjonen som gjør DPIA-en selv er en alvorlig risiko; derfor bør det være minst **etterfølgende ekstern kontroll**. Personvernombudet skal per definisjon ta de berørtes perspektiv.

**Evalueringskriterier og beskyttelsesnivå.** Enhver behandling, også lovlig, er et inngrep i retten til privatliv og personvern (pakten art. 7 og 8). Derfor kan beskyttelsesnivået ikke bare måles i skadegrad og sannsynlighet slik som i BSI IT-Grundschutz. Siden behandlingen må begrunnes etter pakten art. 8 nr. 2 og 52 nr. 1, er beskyttelsesnivået **minst «normalt»** – et lavere nivå skal ikke vurderes. Tre nivåer:

| Nivå | Kriterier |
|---|---|
| **Normal** | Personopplysninger behandles, og det finnes ingen scenarier der behandlingens art viser potensial for høy inngrepsintensitet. |
| **Høy** | Særlige kategorier etter art. 9 behandles (krever høyt nivå etter loven) og/eller de berørte er avhengige av organisasjonens beslutninger/tjenester, dersom inngrepet kan få alvorlige konsekvenser for de berørte og/eller det ikke finnes effektive garantier og inngrepsmuligheter for de berørte (inkl. rettslig prøving). |
| **Svært høy** | Opplysninger som krever høyt nivå behandles, **og** den berørte er eksistensielt avhengig av organisasjonens beslutninger/tjenester, **og** det er tilleggsrisiko fra utilstrekkelig informasjonssikkerhet eller ulovlige formålsendringer som de berørte ikke selv kan oppdage og/eller rette. |

Høyt nivå kan også kreves ved **kumulativ effekt** av forhold som hver for seg ikke krever det, f.eks. data om en stor gruppe personer, eller data om færre personer til flere formål der personene berøres i flere roller.

**Risikoevaluering (figur 3: mål/faktisk-sammenligning).** Kjernen er å sammenligne den behandlingsansvarliges planlagte (eller under vurderingen fastsatte) tiltak med en **katalog av referansetiltak** (under utvikling i AK Technik i den tyske tilsynskonferansen – senere SDM-tiltakskatalogen).

Tabell 1 – Eksempler på generiske tiltak:

| Beskyttelsesmål | Komponent | Tiltak |
|---|---|---|
| Tilgjengelighet | Data, systemer, prosesser | Redundans, beskyttelse, reparasjonsstrategier |
| Integritet | Data | Sammenligning av hashverdier |
| | Systemer | Begrensning av skriverettigheter, regelmessige integritetskontroller |
| | Prosesser | Referanseverdier (min/maks), kontroll av regulering |
| Konfidensialitet | Data, systemer | Kryptering |
| | Prosesser | Rettighets- og rollekonsepter |
| Ikke-kobling (gjennom formålsdefinisjoner) | Data | Anonymitet, pseudonymitet, attributtbaserte legitimasjoner |
| | Systemer | Separasjon (isolasjon) av lagrede data, systemer og prosesser |
| | Prosesser | Identitetsforvaltning, anonymiseringsinfrastruktur, revisjoner |
| Åpenhet (se merknad) | Data | Dokumentasjon, logging |
| | Systemer | Systemdokumentasjon, logging av konfigurasjonsendringer |
| | Prosesser | Dokumentasjon av prosedyrer, logging |
| Intervenerbarhet (gjennom ankerpunkter) | Data | De berørtes tilgang til egne data (informasjon, retting, sperring, sletting) |
| | Systemer | Av-bryter (off-switch) |
| | Prosesser | Brukerstøtte/ett kontaktpunkt for endring/sletting, endringsstyring |

**[Merknad – ikke fra kilden]** I den tilgjengelige teksten er raden «Documentation, logging …» også merket «Ensuring unlinkability through definitions of purposes»; ut fra innholdet og rekkefølgen gjelder raden åpenhet (transparency).

Viktige presiseringer:
- Listen er generisk og må oppdateres med teknologiens stand (fortalepunkt 78 og 83, art. 25 nr. 1 og 32). Den kan **ikke brukes som ren sjekkliste**: Å ha et tiltak er ikke nok. Eksempel: Et rettighets- og rollekonsept sikrer ikke konfidensialitet hvis rettigheter tildeles for generøst og roller ikke er klart atskilt – den behandlingsansvarlige må forklare hvordan konseptet i det konkrete systemet sikrer konfidensialitet.
- Avvik fra referansetiltakene vurderes etter alvor og i hvilken grad de svekker beskyttelsesmålene. Mangler selv et grunnleggende tiltak, er det prima facie tvilsomt om målet nås. Slike funn gir (fra tilsynets ståsted) en **presumsjon for mangler** som må utbedres; tilsynsmyndigheten kan gi råd.
- Velges andre tiltak enn referansetiltakene, må det bevises at de er egnede og **minst likeverdige**.
- Med de riktige tiltakene identifisert vurderes **nødvendighet og forholdsmessighet** (art. 35 nr. 7 bokstav b og c).

#### C. Rapport- og tiltaksfasen (§ 4.3)

**Identifisere og implementere egnede tiltak.** På grunnlag av evalueringen lages en plan for risikohåndtering (art. 35 nr. 7 bokstav d). Det er **ikke akseptabelt med en de minimis-tilnærming** der risiko anses akseptabel fordi få personer berøres. Risikoer kan **prioriteres**, og tiltak med størst nytte for de berørte tas først, innenfor lovens krav. Handlingsplanen skal eksplisitt angi:
- hvilke tiltak som skal redusere alvorlighet eller unngå inngrep i grunnrettigheter eller konkret skade for de berørte,
- hvem som er ansvarlig for gjennomføring, og hvem som skal konsulteres,
- frist for gjennomføring og tilgjengelige ressurser,
- kriterier for å måle resultatene av tiltakene,
- hvem som er ansvarlig for å evaluere og dokumentere kriteriene.

**Dokumentasjon og publisering av rapport.** Funnene dokumenteres og **publiseres** i standardisert form (som scoping-rapporten), for sammenligning av tilsyn, virksomheter og offentlighet. En offentlig versjon uten forretningshemmeligheter kan lages, men må ikke skjule negative funn; utelatelser må ha legitime, dokumenterte grunner.

**Revisjon av resultatene.** DPIA-rapporten bør vurderes av en **uavhengig tredjepart** – ev. tilsynsmyndigheten. Dette omfatter håndtering av interessekonflikter, hensyn til de berørtes rettigheter ved valg av tiltak, tilstrekkelig informasjon til offentligheten og kontroll av at tiltakene faktisk gjennomføres.

**Oppfølging og videreføring.** DPIA er ikke en enkeltstående, lineær prosess, men gjentas gjennom hele levetiden. Art. 35 nr. 11 krever gjennomgang i hvert fall ved endret risiko, f.eks. ved endrede organisatoriske eller rettslige forhold eller nye generelle personvernrisikoer; tiltakene må kunne tilpasses.

### 5. Konklusjon (§ 5)

DPIA er et «early warning system» som gir bedre beslutninger på implementeringsstadiet, unngår kostbare etterfølgende forbedringer og datalekkasjer, viser etterlevelse og bygger tillit. En standardisert prosedyre hjelper også tilsynsmyndighetene å finne svakheter og beste praksis. Innarbeidingen av beskyttelsesmålene sikrer at grunnrettighetsvernet står sentralt.

## Praktiske sjekkpunkter

- Kontroller at lovlighet/behandlingsgrunnlag er vurdert **før** DPIA-en (passer ikke inn i beskyttelsesmålene).
- Kontroller at DPIA-en beskriver hele evalueringsobjektet (data, formater/protokoller, IT-systemer, grensesnitt, prosesser, roller, alle brukstilfeller) – ikke bare én komponent.
- Kontroller at alle aktører er kartlagt, inkl. databehandlere, egne ansatte og tredjeparter som myndigheter.
- Vurder risiko fra den registrertes perspektiv; ta med den behandlingsansvarlige selv og legitime interne brukere som mulige risikokilder.
- Fastsett beskyttelsesnivå (normal/høy/svært høy) – aldri lavere enn normal; vurder kumulative effekter.
- Vurder alle seks beskyttelsesmål, også åpenhet og intervenerbarhet, ikke bare informasjonssikkerhet.
- Sammenlign planlagte tiltak med referansetiltak (SDM-katalogen) og dokumenter hvordan hvert tiltak faktisk virker i det konkrete systemet; begrunn likeverdighet for alternative tiltak.
- Ikke godta restrisiko med begrunnelse i at få personer berøres.
- Handlingsplanen skal ha tiltak, ansvar, frist/ressurser, målekriterier og ansvar for evaluering.
- Lag scoping-rapport og sluttrapport i standardisert form; vurder offentlig versjon uten å skjule negative funn.
- Planlegg uavhengig gjennomgang og jevnlig revisjon av DPIA-en.
- Involver personvernombudet (art. 35 nr. 2).

## Viktige sitater

- «Thus, unlike in risk management, there is no acceptable residual risk and every processing of personal data is an interference with the individual rights and freedoms and has to be justified.» (§ 3.1)
- «A DPIA as required by Article 35 GDPR may not be limited to a single component or function, but must describe the predefined object of evaluation in its entirety» (§ 4.1)
- «Note that the protection goals are meant to represent the perspective of the data subject whose rights are at stake.» (§ 4.2)
- «attackers are not limited to third parties, but can also be rule-abiding internal users of the organization itself» (§ 4.2)
- «it follows that the level of protection has to be normal by default … a lower level must not be considered.» (§ 4.2)
- «The mere implementation of a listed measure does not satisfy the risk evaluation.» (§ 4.2)
- «Particularly with regard to the rights of individuals it is not acceptable to follow a de minimis approach and rank risks for these rights as acceptable when only few persons are concerned.» (§ 4.3)
- «A DPIA is not a singular and linear process, but rather has to be repeated to ensure continuous supervision over the lifetime of a project.» (§ 4.3)

## Kryssreferanser

- GDPR: art. 5 nr. 1 bokstav b og c; art. 25; art. 32 nr. 1 bokstav b; art. 33–34; art. 35 nr. 1–11; art. 36 nr. 1 og nr. 3 bokstav e; art. 40; art. 42; fortalepunkt 78 og 83. EUs pakt om grunnleggende rettigheter art. 7, 8 og 52 nr. 1.
- Andre kilder:
  - [K37](K37-sdm-standard-datavernmodell.md) – SDM-metoden i full form (beskyttelsesmål og tiltakskatalog) som denne artikkelen bygger på.
  - [K24](K24-wp248-dpia.md) – WP248, EDPB-godkjente kriterier for når DPIA kreves og minstekrav.
  - [K12](K12-dt-dpia-veiledning.md), [K21](K21-dt-sjekkliste-dpia-faser.md) – Datatilsynets DPIA-veiledning og fasesjekkliste.
  - [K28](K28-cnil-pia-metode.md) – CNILs PIA-metode, omtalt i § 2.2.
  - [K20](K20-dt-dpia-liste.md) – Datatilsynets liste etter art. 35 nr. 4.

## Aktualitet og begrensninger

- Skrevet i 2016, før GDPR fikk anvendelse (25.5.2018) og før WP248 (2017) og nasjonale DPIA-lister. Henvisninger til ICO- og CNIL-metoder gjelder versjonene fra 2014/2015.
- **[Merknad – ikke fra kilden]** «Sperring» (tysk *Sperrung*, «blocking» i direktiv 95/46) tilsvarer i GDPR «rett til begrensning av behandling» ([art. 18](K43-gdpr-kap03-den-registrertes-rettigheter.md#art-18)). Bruk lovens begrep, se [BEGREPSBANK](../BEGREPSBANK.md).
- Forskningsartikkel, ikke offisiell veiledning; standpunktene om at det ikke bør lages unntakslister etter art. 35 nr. 5, og at DPIA bør publiseres og revideres av uavhengig tredjepart, er forfatternes anbefalinger, ikke rettslige krav.
- Tysk kontekst (ULD, AK Technik, BSI IT-Grundschutz). SDM er senere videreutviklet (se [K37](K37-sdm-standard-datavernmodell.md)).
- Figurene (1–3) er ikke med i tekstutdraget; prosessbeskrivelsen er rekonstruert fra teksten.
- **[Merknad – ikke fra kilden]** Standpunktet «ingen akseptabel restrisiko» skiller seg fra den mer risikobaserte tilnærmingen i bl.a. WP248 og CNIL, der restrisiko vurderes og høy restrisiko utløser forhåndsdrøfting (art. 36). Agenten bør presentere dette som ULDs/SDM-perspektivet.

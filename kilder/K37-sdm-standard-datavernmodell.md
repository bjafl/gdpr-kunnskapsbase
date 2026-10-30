---
id: K37
tittel: "The Standard Data Protection Model (SDM) – A concept for inspection and consultation on the basis of unified protection goals, V.1.0 (trial version)"
utgiver: "Datenschutzkonferenz (DSK) – konferansen av uavhengige tyske personvernmyndigheter (føderale og delstater), AK Technik"
dato: "Vedtatt 9.–10. november 2016 (92. DSK, Kühlungsborn); engelsk oversettelse mars 2017"
spraak: en
fil: "ressurser/SDM-Methodology_V1.0.pdf"
type: metode
gdpr_artikler: [5, 6, 7, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 28, 29, 30, 32, 33, 35, 38, 40, 42, 46, 47]
emner: [beskyttelsesmål, tiltakskatalog, art32, art25, innebygd-personvern, dpia, risikovurdering, beskyttelsesnivå, revisjon, dataminimering, tilgjengelighet, integritet, konfidensialitet, ikke-kobling, åpenhet, intervenerbarhet]
relevans: høy
---

# Standard-Datenschutzmodell (SDM) v1.0 (DSK, 2016/2017)

## Sammendrag

Standard-Datenschutzmodell (SDM, «standard databeskyttelsesmodell») er en metode utviklet av de tyske tilsynsmyndighetene (DSK) for systematisk å omsette juridiske personvernkrav til **tekniske og organisatoriske tiltak (TOM)**, og for å etterprøve dem. Kjernen er **sju beskyttelsesmål (Gewährleistungsziele)**: *dataminimering* (grunnleggende mål), de tre klassiske informasjonssikkerhetsmålene *tilgjengelighet, integritet og konfidensialitet*, og de tre personvernspesifikke målene *ikke-kobling (unlinkability), åpenhet (transparency) og intervenerbarhet (intervenability)*. Modellen kobler hvert mål til lovbestemmelser (GDPR, BDSG, delstatslover), deler en behandling («procedure/Verfahren») i tre komponenter – **data, IT-systemer og prosesser** – og bruker tre **beskyttelsesnivåer** (normal, høy, svært høy) fastsatt ut fra **inngrepets intensitet for den registrerte**, ikke virksomhetens risiko. Tilsyn og rådgivning gjennomføres som en **mål–faktisk-sammenligning (target-actual comparison)** mellom referansetiltak og faktiske tiltak. Versjon 1.0 er en prøveversjon med generiske tiltak (kap. 7); selve referansetiltakskatalogen var under utarbeidelse.

Målgruppe: tilsynsmyndigheter (tilsyn/rådgivning) og behandlingsansvarlige/databehandlere og personvernombud (planlegging, drift og kontroll av behandlinger).

## Når skal agenten bruke denne kilden

- Når tiltak etter **art. 25 og 32** skal velges og begrunnes strukturert: bruk de sju beskyttelsesmålene som sjekkliste for at både sikkerhet (K-I-T) og personvernmål (minimering, ikke-kobling, åpenhet, intervenerbarhet) er dekket.
- I **DPIA** (art. 35 nr. 7 bokstav d): strukturere tiltakskapitlet etter beskyttelsesmål og vise kobling til GDPR-artikler (tabell 3).
- Ved fastsettelse av **beskyttelsesnivå** for en behandling (normal/høy/svært høy) med kriterier fra de registrertes perspektiv, inkl. kumulative effekter.
- Ved **revisjon/tilsyn** av tiltak: mål–faktisk-sammenligning og vurdering av funksjonell likeverdighet av alternative tiltak.
- Når man skal forklare forskjellen mellom informasjonssikkerhetsrisiko (virksomhetens perspektiv, f.eks. BSI IT-Grundschutz/NSM) og personvernrisiko (den registrertes perspektiv).
- Ved overføring til tredjeland: utlede tiltak som «nødvendige garantier» (art. 46) eller bindende virksomhetsregler (art. 47).

## Hovedinnhold

### Forord til oversettelsen og innledning (s. 3–5)

- SDM «sets the stage on which legal requirements and the selection and implementation of technical and organisational data protection measures systematically interrelate» (s. 3). Gir tilsynet mer transparente vurderinger og gir behandlingsansvarlige/databehandlere en metode for planlegging, gjennomføring og oppfølging av tiltak.
- Godkjent for publisering av DSK i november 2016 (med Bayern avstående); DSK anbefaler evaluering. Teksten er en ordrett oversettelse; en internasjonal versjon var under utarbeidelse. Versjonen viser både til GDPR og til tysk rett gjeldende frem til mai 2018.
- SDM omfatter også en **katalog over referansetiltak** (utkast fra oktober 2016) under kommentering blant tyske tilsyn; ferdige moduler publiseres fortløpende (s. 3).
- GDPR art. 5, 12, 25 og 32 inneholder vesentlige krav til sikker behandling; art. 32 nr. 1 krever egnede TOM og nr. 1 bokstav d regelmessig testing og evaluering; art. 40–43 åpner for atferdsnormer og sertifisering; kap. VII krever et koordinert, konsistent vurderingssystem mellom tilsyn (s. 4).
- SDM strukturerer de rettslige kravene i beskyttelsesmål og omsetter dem til en katalog over TOM; standardiserte kataloger er også et godt grunnlag for sertifisering (s. 4).
- Gir en systematisk, etterprøvbar sammenligning mellom målkrav (fra regelverk, standarder, kontrakter, samtykkeerklæringer, organisatoriske regler) og faktisk implementering (s. 5).
- Gjelder privat og offentlig sektor; støtter også den tyske nasjonale e-forvaltningsstrategien (NEGS), som krever TOM etter dataminimering og målene tilgjengelighet, konfidensialitet, integritet, åpenhet, ikke-kobling og intervenerbarhet (s. 4–5).

### Formål og virkeområde (kap. 2–3, s. 6–7)

- Utgangspunkt for analysen: fastslå **behandlingsansvarlig(e)**, **formålet** innenfor en forretningsprosess, og **rettslig grunnlag**. Først når de rettslige forutsetningene er avklart, kan funksjonalitet, nødvendig omfang og egnede tiltak etter «state of the art» spesifiseres (s. 6).
- Hovedanvendelse: planlegging, implementering og drift av enkeltbehandlinger («personenbezogene Verfahren») og tilsynets vurdering av dem. En behandling kjennetegnes av et spesifikt, avgrenset og lovlig formål og forretningsprosessene som realiserer det (s. 7).
- Tiltak er **behandlingsspesifikke** (f.eks. anonymisering når formålet er oppnådd, eller tiltak som følge av interesseavveiing) eller **tverrgående** (kryptering, integritetssikring, autentisering av kommunikasjonsparter og komponenter, logging, pseudonymisering/anonymisering, kontaktpunkt for klager, rollekonsepter). SDM systematiserer både obligatoriske og valgfrie, behandlingsspesifikke og tverrgående tiltak (s. 7).

### Oppbygning (kap. 4, s. 8)

SDM:
1. omsetter rettslige krav til en katalog av beskyttelsesmål;
2. strukturerer behandlingen i komponentene **data, IT-systemer og prosesser**;
3. klassifiserer data i **tre beskyttelsesnivåer**;
4. supplerer med betraktninger på behandlings- og systemnivå;
5. gir en systematisk utledet katalog over standardiserte tiltak (vedlegg).

### Beskyttelsesmålene (kap. 5, s. 9–14)

**Begrepet (5.1):** Beskyttelsesmål beskriver kategorier av krav avledet av personvernretten – egenskaper ved lovlig behandling som skal sikres ved TOM gjennom å utelukke avvik (f.eks. ingen uautorisert kjennskap til data). Graden av realisering avveies mellom beskyttelsesnivå og kostnad, med hensyn til state of the art; plikten er **ikke absolutt**, men relativ til omstendighetene og risikoen for de registrertes rettigheter og friheter. Begrepet «Gewährleistungsziel» knyttes til den tyske forfatningsdomstolens (BVerfG) dom av 27.2.2008 om grunnretten til konfidensialitet og integritet i IT-systemer.

**Sentrale rettslige krav som fanges opp (5.2):** formålsbegrensning; begrensning til det nødvendige (dataunngåelse); de registrertes rettigheter (informasjon, retting, sperring, sletting); åpenhet om behandlinger (etterprøvbart for virksomheten, de registrerte og tilsynet); informasjonssikkerhet i komponentene. SDM vurderer ikke materiell lovlighet eller sektorregler i detalj – kjennskap til regelverket er fortsatt nødvendig.

#### Oversikt over de sju beskyttelsesmålene

| # | Beskyttelsesmål | Kjerneinnhold i SDM | Type |
|---|---|---|---|
| 0 | **Dataminimering** (data minimisation) | Ikke behandle flere personopplysninger enn nødvendig for formålet – i hele livsløpet og i hvert behandlingssteg; påvirker omfanget av alle de andre målene | Grunnleggende mål |
| 1 | **Tilgjengelighet** (availability) | Data er tilgjengelige og kan brukes riktig i den tiltenkte prosessen av autoriserte; inkl. gjenfinnbarhet, teknisk tilgang og tolkbarhet (semantisk) | Klassisk sikkerhetsmål |
| 2 | **Integritet** (integrity) | Systemer og prosesser følger spesifikasjonene; data er intakte, fullstendige og oppdaterte; avvik utelukkes eller kan oppdages | Klassisk sikkerhetsmål |
| 3 | **Konfidensialitet** (confidentiality) | Ingen uautorisert tilgang – heller ikke ansatte hos tekniske tjenesteytere uten behov, eller enheter uten tilknytning til behandlingen | Klassisk sikkerhetsmål |
| 4 | **Ikke-kobling** (unlinkability) | Data behandles og analyseres kun for formålet de ble samlet inn for | Personvernmål |
| 5 | **Åpenhet** (transparency) | Registrerte, systemeiere og tilsyn kan i varierende grad forstå hvilke data som behandles for hvilket formål, med hvilke systemer, hvor data flyter og hvem som er ansvarlig – fra opprinnelse til sletting | Personvernmål |
| 6 | **Intervenerbarhet** (intervenability) | De registrerte får effektivt sine rettigheter (underretning, informasjon, retting, sperring, sletting), og behandlingsansvarlig kan gripe inn i behandlingen fra innsamling til sletting | Personvernmål |

*SDM nummererer de seks «fundamentale» målene 1–6 og omtaler dataminimering som det grunnleggende målet (5.3).*

#### 5.3 Dataminimering (s. 10–11)

- Konkretiserer **nødvendighetsprinsippet** (art. 5 nr. 1 bokstav c): begrensning «at the source and at each branch, in advance» – og til selve behandlingen (viktig ved «Big Data»).
- Proaktivt element i personvernvennlig design – fra produsentens design og konfigurasjon til bruk i kjerne- og hjelpeprosesser (f.eks. vedlikehold), fra innsamling til sletting/fullstendig anonymisering.
- Forutsetter vurdering av formålets legitimitet og dataenes relevans/nødvendighet; kan føre til at behandling ikke er nødvendig → **dataunngåelse** = optimal minimering.
- Hvis unngåelse ikke er mulig, vurderes behandlingsstegene i **tre dimensjoner**:
  1. omfanget av informasjon som behandles eller utleveres,
  2. antallet enheter og personer informasjonen utleveres til,
  3. graden av faktisk kontroll disse har over dataene.
- Målet er nådd når behandlingen er minimert i disse tre dimensjonene **globalt** (hele behandlingen) og **lokalt** (hvert steg). Eksempler: datafelt i søkemasker og grensesnitt, funksjoner tilgjengelige i menyer.
- **Viktigste og mest effektive tiltak: tidligst mulig sletting** av data som ikke lenger trengs. Før dette: utelukke felt fra visse behandlinger, begrense antall poster en funksjon gjelder, slette eller transformere identifiserende felt (anonymisering, pseudonymisering), eller skjule felt i skjermbilder når kjennskap ikke er nødvendig.

#### 5.4.1 Klassiske sikkerhetsmål (s. 11–12)

- **Tilgjengelighet:** data skal være tilgjengelige og kunne brukes riktig; metodene må håndtere dataformatene. Omfatter gjenfinnbarhet (adresseregistre, referanse-/saksnummer), at systemene gjør data tilgjengelige på adekvat måte, og at innholdet kan tolkes (semantisk).
- **Integritet:** (a) IT-prosesser og systemer oppfyller kontinuerlig spesifikasjonene for sine funksjoner; (b) dataene forblir intakte, fullstendige og oppdaterte. Avvik må utelukkes eller kunne fastslås. Forstått som riktighet etter art. 5 nr. 1 bokstav d innebærer det samsvar mellom normative krav og praksis, både teknisk og i behandlingens helhet.
- **Konfidensialitet:** ingen uautorisert tilgang. Uautoriserte er ikke bare eksterne tredjeparter (med eller uten kriminell hensikt), men også ansatte hos tekniske tjenesteytere som ikke trenger tilgang, og personer i organisatoriske enheter uten tilknytning til behandlingen eller den registrerte.
- Disse målene ble opprinnelig formulert for IT-sikkerhet og virksomhetens beskyttelse av egne forretningsprosesser mot angrep.

#### 5.4.2 Personvernmål (s. 12–13)

- Personvern tar et **utvidet perspektiv**: også risiko som skyldes virksomhetens *egen* aktivitet for de registrerte. «not only a person who has to prove trustworthy to an organisation […] but an organisation also has to prove that it is trustworthy to the person»; DPIA er særlig egnet til å vise dette (s. 12).
- **Ikke-kobling:** data skal kun behandles og analyseres for innsamlingsformålet. Større, kombinerte datasett øker misbrukspotensialet. Viderebehandling er bare lovlig under strenge vilkår (GDPR: arkiv i allmennhetens interesse, forskning, statistikk – med garantier). Tiltak: dataminimering, pseudonymisering, og separasjon organisatorisk og systemmessig mellom viderebehandling og opprinnelig behandling (f.eks. pseudonymisere eller redusere datagrunnlaget for nytt formål).
- **Åpenhet:** registrerte, systemoperatører og tilsyn skal i varierende grad kunne forstå hvilke data som samles og behandles for hvilket formål, hvilke systemer og prosesser, hvor data flyter og hvem som er rettslig ansvarlig i de ulike fasene. Nødvendig for kontroll fra opprinnelse til sletting og forutsetning for lovlig behandling; informert samtykke forutsetter åpenhet.
- **Intervenerbarhet:** de registrerte får effektivt rett til underretning, informasjon, retting, sperring og sletting til enhver tid, og behandlingsansvarlig må kunne gripe inn i behandlingen gjennom hele prosessen.

#### 5.5 Avledede mål (s. 13–14)

- **Autentisitet:** data kan spores entydig til opprinnelsen. Ved innsamling fra den registrerte: innsamlingsprosess, utløpsdato og ev. hvem som samlet inn; ved overføring/henting fra tredjepart: tidspunkt, anledning, formål og kilde; ved formålsendring: navn og revisjonsnivå på kildedatasettet med referanse til dokumentasjon. Avledet av åpenhet – «integrity-assured transparency».
- **Revisjonsevne (revisability):** mulig å kontrollere hvem som behandler personopplysninger når og hvordan – endring, bruk og ren lesing. Del av åpenhet; forutsetter integritet i koblingen mellom datasett og behandlingsinformasjon.

### Koblingen til gjeldende rett (kap. 6, s. 15–26)

**6.1 Forfatningsdomstolen (BVerfG):** Målene svarer til grunnprinsippene for retten til informasjonell selvbestemmelse fra folketellingsdommen (15.12.1983, 1 BvR 209/83): vern mot ubegrenset innsamling, lagring, bruk og utlevering; lovgiver må fastsette organisatoriske og prosessuelle sikringer (utleverings- og utnyttelsesforbud, plikt til opplysning, informasjon og sletting). Herfra utledes formålsbegrensning/ikke-kobling, nødvendighet, åpenhet, intervenerbarhet og sikkerhet. Dommen av 27.2.2008 (1 BvR 370/07) etablerte grunnretten til **integritet og konfidensialitet i IT-systemer** når den registrerte er avhengig av systemet, systemet inneholder data som kan gi innsikt i vesentlige deler av livet, og den registrerte bruker det som sitt eget – også når det driftes av tredjeparter (f.eks. skytjenester for privatpersoner, smarttelefoner).

**6.2 BDSG (gammel tysk lov):** § 9 BDSG med vedlegg (TOM, forholdsmessighet) er utgangspunktet; tiltak skal fastsettes på forhånd (planleggingsfasen) og kunne dokumenteres – jf. direktiv 95/46 fortalepunkt 46. Kravene kan «mappes» til målene, slik BSI IT-Grundschutz har gjort siden midten av 1990-tallet. Eksempler: dataminimering ← § 3a (dataunngåelse), slette-/anonymiseringsplikter; tilgjengelighet ← vedlegg nr. 7; integritet ← vedlegg nr. 3–4; konfidensialitet ← vedlegg nr. 3–4, § 5 (datahemmelighet); ikke-kobling ← formålsbinding, § 4a, vedlegg nr. 8 (dataseparasjon); åpenhet ← informasjons- og innsynsrett, prosedyreoversikt (§§ 4d, 4e, 4g); intervenerbarhet ← retting, sperring, sletting, innsigelse. Tabell 1 (s. 19–21) gir detaljert mapping av BDSG-paragrafer.

**6.3 Delstatslover:** Flere delstatslover har allerede «Schutzziele» (tilgjengelighet, integritet, konfidensialitet, åpenhet, autentisitet, sporbarhet); Schleswig-Holstein har hatt hele settet siden 2012. Delstatslovenes «åpenhet» er snevrere (kun dokumentasjon) enn SDMs. Tabell 2 (s. 22–23) mapper sachsisk personvernlov som eksempel.

#### 6.4 Kobling til GDPR (s. 23–26)

- Målene er i hovedsak forankret i **art. 5** (som igjen bygger på Charterets art. 8). Behandlingsansvarlig og databehandler skal velge TOM (særlig art. 32) og implementere og kontrollere dem innenfor innebygd personvern og personvernvennlige standardinnstillinger (art. 25). Ansvarlighet etter art. 5 nr. 2 og 24 nr. 1. DPIA (art. 35) bygger på systematisk beskrivelse og krever tiltak, garantier og sikkerhetsmekanismer (art. 35 nr. 7 og 11).
- SDM skal hjelpe overgangen til GDPR «in a transparent, controlled and resource-conserving way» og gi dokumentasjonen GDPR krever.
- **Tredjelandsoverføring:** SDM kan brukes til å utlede TOM som nødvendige garantier etter **art. 46** eller BCR etter **art. 47**, særlig dokumentasjon og logging.
- Integritet, tilgjengelighet, konfidensialitet, åpenhet og dataminimering finnes begrepsmessig i forordningsteksten; ikke-kobling og intervenerbarhet er tatt inn via bl.a. formålsbegrensning, sletting og dataportabilitet.

**Mål og GDPR-forankring (s. 24–25):**
- *Tilgjengelighet:* art. 32 nr. 1 bokstav b og c; art. 5 nr. 1 bokstav e (forutsetning for identifikasjon); grunnlag for informasjon og innsyn (art. 13, 15) og dataportabilitet (art. 20).
- *Integritet:* art. 5 nr. 1 bokstav f; art. 32 nr. 1 bokstav b – vern mot uautorisert endring og sletting.
- *Konfidensialitet:* art. 5 nr. 1 bokstav f; art. 32 nr. 1 bokstav b; art. 38 nr. 5 (personvernombudets taushetsplikt); art. 28 nr. 3 bokstav b (databehandlers taushetsplikt). «A violation of confidentiality in general constitutes a data processing without a legal basis.»
- *Ikke-kobling:* behandlingsgrunnlaget (art. 6) som målestokk; formålsbegrensning art. 5 nr. 1 bokstav b; art. 7 nr. 4 (samtykke kan være ugyldig hvis data ikke er nødvendige); typisk tiltak pseudonymisering (art. 40 nr. 2 bokstav d).
- *Åpenhet:* art. 5 nr. 1 bokstav a; særlig informasjons- og innsynsplikter.
- *Intervenerbarhet:* retting, sperring, sletting, protest (art. 16–17 m.fl.); behandlingsansvarlig må etter art. 5 nr. 1 bokstav d legge til rette organisatorisk og teknisk.

**Tabell 3 – GDPR-artikler per beskyttelsesmål (s. 25):**

| Beskyttelsesmål | GDPR-artikler |
|---|---|
| Dataminimering | 5 (1) (c), 5 (1) (e), 25, 32 |
| Tilgjengelighet | 5 (1) (e), 13, 15, 20, 25, 32 |
| Integritet | 5 (1) (f), 25, 32, 33 |
| Konfidensialitet | 5 (1) (f), 25, 28 (3) (b), 29, 32 |
| Ikke-kobling | 5 (1) (c), 5 (1) (e), 17, 22, 25, 40 (2) (d) |
| Åpenhet | 5 (1) (a), 13, 14, 15, 19, 25, 30, 32, 33, 40, 42 |
| Intervenerbarhet | 5 (1) (d), 5 (1) (f), 13 (2) (c), 14 (2) (d), 15 (1) (e), 16, 17, 18, 20, 21, 25, 32 |

**Tabell 4 – Fortalepunkter per beskyttelsesmål (s. 26):**

| Beskyttelsesmål | Fortalepunkter |
|---|---|
| Dataminimering | 28, 29, 30, 39, 78, 156 |
| Tilgjengelighet | 49, 78, 83 |
| Integritet | 39, 49, 78, 83 |
| Konfidensialitet | 39, 49, 78, 83 |
| Ikke-kobling | 31, 32, 33, 39, 50, 53, 71, 78 |
| Åpenhet | 32, 39, 42, 58, 60, 61, 63, 74, 78, 84, 85, 86, 87, 90, 91, 100 |
| Intervenerbarhet | 39, 59, 65, 66, 67, 68, 69, 70, 78 |

*Tabell 4 er rekonstruert fra et tekstuttrekk med forskjøvne kolonner; fordelingen mellom tilgjengelighet/integritet/konfidensialitet bør kontrolleres mot PDF.*

### Generiske tiltak per beskyttelsesmål (kap. 7, s. 27–30)

For hver komponent (data, systemer, prosesser) og hvert mål angis referansetiltak i vedlegget; tiltakets effekt på andre mål skal også vurderes (et tiltak kan bidra til flere mål). Tiltakene er «tried and tested» i tilsyn og revisjoner over mange år.

| Beskyttelsesmål | Typiske (generiske) tiltak |
|---|---|
| **Dataminimering** (7.1) | Redusere innsamlede attributter om den registrerte · Redusere behandlingsmuligheter i behandlingsstegene · Redusere mulighetene for å få kjennskap til eksisterende data · Foretrekke automatiserte behandlingsoperasjoner (ikke beslutningsprosesser) som gjør innsyn i data unødvendig, fremfor dialogstyrte prosesser · Automatiske sperre- og sletterutiner; pseudonymisering og anonymisering · Regler for styring av endringer i behandlinger |
| **Tilgjengelighet** (7.2) | Sikkerhetskopier av data, prosesstilstander, konfigurasjoner, datastrukturer, transaksjonshistorikk m.m. etter et testet konsept · Beskyttelse mot ytre påvirkning (skadevare, sabotasje, force majeure) · Dokumentasjon av datasyntaks · Redundans i maskinvare, programvare og infrastruktur · Reparasjonsstrategier og alternative prosesser · Stedfortrederordninger for fraværende ansatte |
| **Integritet** (7.3) | Begrense skrive- og endringsrettigheter · Sjekksummer, elektroniske segl og signaturer etter et kryptokonsept · Dokumentert tildeling av rettigheter og roller · Prosesser for å holde data oppdatert · Spesifikasjon av nominell prosessatferd og jevnlig testing for å dokumentere funksjonalitet, risiko, sikkerhetshull og sideeffekter · Spesifikasjon av nominell atferd for arbeidsflyt/prosesser og jevnlig testing av at nåtilstanden kan fastslås |
| **Konfidensialitet** (7.4) | Rettighets- og rollekonsept etter nødvendighetsprinsippet basert på identitetsforvaltning · Sikker autentisering · Begrense autorisert personell til de som er påviselig ansvarlige (lokalt, faglig), kvalifiserte, pålitelige (ev. sikkerhetsklarert) og formelt godkjent, uten interessekonflikt · Spesifikasjon og kontroll av godkjente ressurser, særlig kommunikasjonskanaler · Egnede omgivelser (bygg, rom) · Spesifikasjon og kontroll av organisatoriske prosedyrer, interne regler og kontraktsforpliktelser (taushetsplikt, konfidensialitetsavtaler) · Kryptering av lagrede og overførte data med prosesser for nøkkelforvaltning (kryptokonsept) · Beskyttelse mot ytre påvirkning (spionasje, hacking) |
| **Ikke-kobling** (7.5) | Begrense rettigheter til behandling, bruk og overføring · Utelate eller lukke grensesnitt i behandlinger og komponenter · Regler som forbyr bakdører og kvalitetssikring i programvareutvikling · Separasjon langs organisatoriske/avdelingsgrenser · Separasjon via rollekonsepter med differensierte tilganger basert på identitetsforvaltning og sikker autentisering · Godkjenning av brukerstyrt identitetsforvaltning · Formålsspesifikke pseudonymer, anonymiseringstjenester, anonyme legitimasjoner (credentials), behandling av pseudonyme/anonyme data · Regulerte prosedyrer for formålsendringer |
| **Åpenhet** (7.6) | Dokumentasjon av behandlinger, særlig forretningsprosesser, databeholdninger, dataflyt, IT-systemer, driftsprosedyrer, beskrivelse og samspill med andre behandlinger · Dokumentasjon av testing, godkjenning og ev. forhåndskontroll av nye/endrede behandlinger · Dokumentasjon av kontrakter med ansatte, eksterne tjenesteytere og tredjeparter data hentes fra/overføres til; ansvarsfordeling · Dokumentasjon av samtykker og protester · Logging av tilgang og endringer · Verifisering av datakilder (autentisitet) · Versjonskontroll · Dokumentasjon av behandlingen via protokoller basert på et loggings- og evalueringskonsept · Hensyn til de registrertes rettigheter i loggings- og evalueringskonseptet |
| **Intervenerbarhet** (7.7) | Differensierte valg for samtykke, tilbaketrekking og protest · Nødvendige datafelt, f.eks. for sperremerking, underretninger, samtykker, protester, tilsvarsrett · Dokumentert håndtering av feil, problemløsning og endringer i behandlingen og i sikkerhets-/personverntiltak · Mulighet for å deaktivere enkeltfunksjoner uten å påvirke hele systemet · Standardiserte spørre- og dialoggrensesnitt for de registrerte · Sporbarhet av behandlingsansvarliges aktiviteter for å innfri rettigheter · Ett kontaktpunkt (Single Point of Contact, SPoC) for de registrerte · Driftsmessig mulighet til å samle, konsistent rette, sperre og slette alle data om én person |

### Behandlingens komponenter (kap. 8, s. 31–32)

- «Procedure» = fullstendig behandling: formalisert, gjentakbar sekvens av behandlingssteg (innsamling, lagring, endring, overføring, sperring, sletting, bruk, anonymisering, pseudonymisering, kryptering) for en fagoppgave/forretningsprosess, manuelt eller IT-basert; kjennetegnet og avgrenset av **formålet**.
- Tre komponenter:
  1. **Personopplysninger** (data),
  2. **Tekniske systemer** (maskinvare, programvare, infrastruktur),
  3. **Prosesser** (organisasjon og personell som behandler data med systemene).
- Metodisk startes det med dataene, hvis beskyttelsesnivå fastsettes av behandlingsansvarlig; **systemer og prosesser arver nivået**. Referansekatalogen brukes til å kontrollere om tiltakene passer nivået.
- Viktige egenskaper: **dataformater** (skjulte gamle data i tekstfiler, metadata i bildefiler som kameramodell/sted/tid, tapsbasert komprimering); **grensesnitt** mot systemer utenfor systemgrensen definert av formålet (registrering og dokumentasjon er avgjørende for kontroll av dataflyt); **ansvar** per prosess i et rollekonsept (prosesseier; det må være klart hvem som aktivt sikrer lovligheten).

### Beskyttelsesnivåer (kap. 9, s. 33–37)

- Enhver behandling er et **inngrep** i retten til informasjonell selvbestemmelse – også lovlig behandling. Virksomheten må vise at inngrepet er begrenset til det absolutt nødvendige (art. 5 nr. 2, 24 nr. 1), ved å vise hvordan beskyttelsesmålene realiseres. «Organisasjon» omfatter både behandlingsansvarlig og databehandler.
- SDM tar **den registrertes perspektiv** og skiller seg fra BSI IT-Grundschutz, som primært beskytter den behandlende organisasjonen.

**9.1 Inngrepsintensitet:** Informasjonssikkerhet måler typisk skadeomfang × sannsynlighet. For personvern må inngrepet i grunnrettighetene vurderes; mål på inngrepsintensitet er bl.a. formålet (bestemt av rettsgrunnlaget), beskyttelsesnivå, lagringstid, type og antall mulige mottakere. SDM kan vise at en forretningsprosess' beskyttelsesnivå ikke svarer til det de registrertes grunnrettigheter krever.

**9.2 Konfidensialitetens særrolle:** Konfidensialitet må sikres selv ved lav inngrepsintensitet; her overlapper SDM og BSI-Grundschutz i stor grad – valget av tiltak er i stor grad likt grunnsikringstiltak.

**9.3 Tre kategorier (basert på BSI IT-Grundschutz):**

| Nivå | Kriterier |
|---|---|
| **Normal** | Minimum for all behandling av personopplysninger – nivået kan aldri være lavere enn normal; lavere nivå bare når det ikke behandles personopplysninger. |
| **Høy** | Eksempler: uforanderlige opplysninger som livslangt kan være anker for profilering (biometri, genetikk); spredning av entydig identifiserende, svært koblingsbare data (livslangt helseforsikringsnummer, skatte-ID); rettslig eller på annen måte begrunnet manglende åpenhet (statssikkerhet, estimerte verdier i scoring); potensielt alvorlige økonomiske konsekvenser; konsekvenser for status/omdømme; konsekvenser for fysisk integritet; realistisk påvirkning på mange registrertes utøvelse av grunnrettigheter (omfattende offentlig kameraovervåkning); risiko for diskriminering/stigmatisering (algoritmer, ikke-transparente beslutninger); inngrep i særlig beskyttede livsområder. Også når den registrerte er **avhengig** av organisasjonens beslutninger/tjenester (ytelsesforvaltning, helse) og organisasjonen behandler data med omfattende inngrep, behandler lovbestemt særlig beskyttede data, eller ikke gir reelle, effektive muligheter for inngripen og selvbeskyttelse. Også når tvister ikke realistisk kan løses for domstolene (f.eks. teletilbydere uten lokal tilstedeværelse – GDPR løser dette delvis med markedsstedsprinsippet). **Særlige kategorier** (jf. art. 35 nr. 3) gir som hovedregel uten skjønn **høyt** nivå. |
| **Svært høy** | Den registrerte er **direkte og vitalt avhengig** av organisasjonens beslutninger eller tjenester. Ytterligere risiko når virkningene av behandlingen ikke kan bli kjent for den registrerte. |

**9.4 Kollisjon mellom informasjonssikkerhet og grunnrettigheter:** BSI-Grundschutz og SDM kan gi ulikt nivå for samme behandling; en riktig gjennomført Grundschutz-vurdering bør gi samme konklusjon, men ved avvik **har SDM-nivået forrang**. Eksempel: logging av ansattes atferd eller overvåkning av eksterne brukere for å hindre angrep kan vurderes ulikt; slike tilfeller må behandles, dokumenteres og begrunnes særskilt.

**9.5 Kumulative effekter:** Nivået vurderes for data, systemer og prosesser; start med data (arves av systemer og prosesser). To kumulative effekter kan løfte normal → høy:
- **store datamengder** («Accumulation of a great number of data»);
- **mange roller med ulike rettigheter og formål** («Accumulation of a great number of rights»).

**9.6 Risikoanalyse:** I tillegg til inngrepsvurderingen trengs en risikoanalyse av sannsynligheten for at organisasjonen *ikke* etterlever reglene til tross for tiltakene, som kan utløse tilleggstiltak. Den omfatter også sikkerhetsaspekter (uautorisert tilgang, integritet) og ser på organisasjoner som er autorisert til å behandle data. Fire aspekter skal registreres og vurderes:
1. Styrken på organisasjonens **motivasjon** til uautorisert formålsendring.
2. Organisasjonens **operative muligheter** for uautorisert formålsendring (gitt motivasjon).
3. Virkningene av **overføring til tredjeland** – hvilke tilleggstiltak som trengs for overføring og behandling der, uavhengig av nasjonalt nivå.
4. Omfanget av **informasjonssikkerhetstiltak**, inkl. prosesser for å løse konflikter mellom sikring av forretningsprosessene og personvernet for de registrerte.

**9.7 Generell tilnærming ved høyt nivå:** Høyt nivå krever ofte tilleggstiltak (angitt i referansekatalogens moduler), mens tiltakene for normalt nivå videreføres og tilpasses. Skalering kan skje ved å øke **tiltakets virkning** (f.eks. lengre kryptonøkler) eller øke **påliteligheten** i utførelsen – identifisere forstyrrende faktorer (tekniske feil, brukerfeil, force majeure, ytre påvirkning) og gjøre tiltaket mer robust, ofte med organisatoriske tiltak. Iterativt til truslene mot beskyttelsesmålene er utelukket med tilstrekkelig sikkerhet; effekten dokumenteres i risikoanalysen.

### Tilsyn og rådgivning med SDM (kap. 10, s. 38–43)

**Fasene (figur 1, s. 38):**

| Fase | Innhold |
|---|---|
| Analyse av behandlingskonteksten | Ansvarlige, registrerte og rettsforholdet mellom dem; ev. samtykkets innhold og innhenting; operative prosesser; formål; datagrunnlag, dataflyt, behandlingsprosedyre |
| Materiell rettslig vurdering | Gjeldende rett og rettsgrunnlag; interesseavveiing; formålenes legitimitet; tillatt datagrunnlag og overføringshjemler; særlige krav |
| Anvendelse av SDM – utforming av beskyttelsesmålene | Forpliktelsesgrad (fra lovpålagt minimum til personvernvennlig design); kvalitative parametere (f.eks. hvem som har tilgang); beskyttelsesnivåanalyse; kvantitative parametere (f.eks. tilgjengelighetskrav) |
| Avviksanalyse / mål–plan-sammenligning | Institusjonell kontekst (ansvar, personvernstyring); fastslå TOM inkl. hjelpeprosesser og infrastruktur og sammenlign med referansetiltak; vurdere effektivitet, ev. verifisere risikoanalyser; fastslå mangler, aktuelle tilleggstiltak og deres forholdsmessighet |
| Tilbakemelding | Krav om ytterligere TOM; ev. sanksjoner ved brudd på materielle og prosessuelle krav |

- Formålet med gjennomgangen må være avklart på forhånd; tilsyn ser sjelden på alt. I rådgivning kan fasene gjennomløpes syklisk. To forutsetninger: klarhet om faktum og en materiell vurdering. Til slutt vurderes restrisiko for de registrertes informasjonelle selvbestemmelse og forholdsmessige tilleggstiltak; kan ikke risiko reduseres tilstrekkelig, kan konklusjonen være å **avstå fra behandlingen** (s. 39).

**10.1 Forberedelse – faktumspørsmål (s. 39–40):** Hvem er ansvarlig? Utføres behandlingen for en offentlig myndighetsoppgave? Finnes avtale/rettsforhold mellom behandlingsansvarlig og registrert? Er samtykke grunnlaget, og hvordan innhentes det? Hvordan er rettsforholdet mellom flere behandlingsansvarlige/databehandlere regulert? Hvilke formål og forretningsprosesser? Hvilke data i hvilke steg, via hvilke systemer og nett, under hvilke personers kontroll? Hvilke hjelpeprosesser? Hvilken teknisk infrastruktur?
**Materielle spørsmål:** Hvilken lov gjelder? Hvilke formål er legitime og hvilke formålsendringer tillatt? Hvilke data er nødvendige? Hvilke overføringshjemler finnes mellom aktørene og til tredjeparter? Hvilke begrensninger på utlevering? Hvilke særlige krav må TOM oppfylle (fra lov eller fra interesseavveiing)?

**10.2 Utforming av beskyttelsesmålene – sju spørsmål (s. 41–42):**
1. *Tilgjengelighet:* For hvem, i hvilke prosesser, må tilgjengeligheten av hvilke data sikres? Målestokk er de registrertes interesse; gjelder bare der tap av tilgjengelighet strider mot deres interesser.
2. *Integritet:* Hvilke data skal holdes intakte og hvilke oppdatert? Oppdatering krever ofte mer innsamling, som kan stride mot de registrertes interesser. Integritet i prosesser og systemer avledes av de øvrige målene.
3. *Konfidensialitet:* Overfor hvem må utlevering av hvilke data nektes? Autorisert tilgang utledes teknologinøytralt fra forretningsprosessene; utlevering til tredjeparter følger av overføringshjemmelen.
4. *Åpenhet:* For hvem og i hvilken form skal behandlingen være åpen? Krav til prosessdokumentasjon, intern dokumentasjon, evaluerbarhet og revisjonsevne.
5. *Intervenerbarhet:* Hvilke rettigheter i hvilket omfang? Hvem skal underrettes om automatisert behandling? Hvilke data omfattes av innsyn? Når må data slettes eller sperres?
6. *Ikke-kobling:* Hvilke formålsendringer er tillatt? Hvilke formål for hjelpeprosesser kan legitimt avledes av kjerneprosessene? Tiltak skal utelukke bruk for andre enn de spesifiserte legitime formålene.
7. *Dataminimering:* Kunnskap om og disposisjonsmakt over hvilke data hos hvilke personer og myndigheter må minimeres?

Deretter beskyttelsesnivåanalyse (kap. 9), som brukes på tre måter: (1) **kvantitativ** presisering (hvor lenge og i hvilken grad er tap av tilgjengelighet akseptabelt? med hvilken forsinkelse må aktualitet sikres? hvor presist i tid må behandling kunne etterspores? innen hvilken frist må rettigheter innfris?); (2) grunnlag for **avveiing** mellom de registrertes interesser og kostnad (resultat: referansetiltak i kap. 7); (3) vurdering av **restrisiko**, som ofte avhenger av tredjeparters eller involverte parters interesse i å bryte målene.

**10.3 Mål–faktisk-sammenligning (s. 42–43):** Kjerneelementet er å sammenligne referansetiltak (utledet av de spesifiserte målene) med planlagte eller faktiske tiltak. Avvik vektes etter hvor mye de truer måloppnåelsen; i tilsyn kan manglende måloppnåelse gi (ev. sanksjonerbare) mangler. Ofte er tiltak åpenbart fraværende; mer komplekst når det er valgt andre tiltak enn referansetiltakene – da må det vurderes om de er **funksjonelt likeverdige** og svarer til det spesifiserte nivået.

### Driftskonsept (kap. 11, s. 44–45)

- DSK er oppdragsgiver, eier og utgiver av SDM (metode og referansekatalog); **AK Technik** (DSKs teknologiarbeidsgruppe) utvikler, vedlikeholder og leder prosjektet.
- Brukergruppe 1: de 16 delstatstilsynene, Bayerns tilsyn for privat sektor og den føderale personvernkommissæren (rådgivning, tilsyn, sanksjoner). Brukergruppe 2: behandlingsansvarlige, særlig personvernombud (planlegging og drift).
- Videreutvikling: vedlikehold av SDM og katalog, endringsforespørsler (CR) fra begge brukergrupper (DSK avgjør), kvalitetssikring, versjonskontroll, prosjektledelse (service desk/SPoC, CR-sporing, moderering, nettsted), PR.

### Referansetiltakskatalog (kap. 12, s. 46)

Katalogen skal bli en integrert del av SDM, men revideres i kortere sykluser i takt med teknologisk utvikling. **Selve katalogen er ikke inkludert i v1.0** – dokumentet inneholder bare de generiske tiltakene i kap. 7.

## Praktiske sjekkpunkter

- Kontroller at tiltakskapitlet i DPIA/risikovurdering dekker **alle sju beskyttelsesmål** – ikke bare K-I-T. Mangler det tiltak for dataminimering, ikke-kobling, åpenhet eller intervenerbarhet, er tiltakene ufullstendige fra et personvernperspektiv.
- Kontroller at beskyttelsesnivået er fastsatt fra **den registrertes perspektiv** (inngrepsintensitet), at det aldri er lavere enn «normal», og at særlige kategorier gir minst «høy» (9.3).
- Kontroller om **kumulative effekter** (store datamengder, mange roller/rettigheter) løfter nivået (9.5).
- Kontroller at beskyttelsesnivået er fastsatt for dataene og arvet av systemer og prosesser (kap. 8, 9.5).
- Kontroller at behandlingen er beskrevet i tre komponenter (data, systemer, prosesser) med dataformater, grensesnitt over systemgrensen og prosessansvar (kap. 8).
- Kontroller at risikoanalysen også vurderer organisasjonens egen motivasjon og mulighet for formålsendring, tredjelandsoverføring og konflikter mellom informasjonssikkerhet og personvern (9.6) – f.eks. at sikkerhetslogging av ansatte ikke blir uforholdsmessig.
- Kontroller at dataminimering er vurdert i tre dimensjoner (informasjonsmengde, antall mottakere, grad av kontroll) både globalt og per behandlingssteg, og at tidligst mulig sletting er implementert (5.3).
- Kontroller for intervenerbarhet at systemet teknisk kan samle, rette, sperre og slette alle data om én person, og at det finnes ett kontaktpunkt for de registrerte (7.7).
- Kontroller for åpenhet at det finnes dokumentasjon av dataflyt, systemer, kontrakter, samtykker/protester, versjonskontroll og et loggings- og evalueringskonsept (7.6).
- Kontroller for ikke-kobling at grensesnitt er lukket/dokumentert, at formålsendringer er regulert, og at pseudonymisering/separasjon brukes ved viderebehandling (7.5).
- Ved høyt nivå: kontroller at tiltak er skalert (sterkere virkning eller mer robust utførelse) og at effekten er dokumentert (9.7).
- Ved revisjon: bruk mål–faktisk-sammenligning, og krev dokumentasjon av **funksjonell likeverdighet** når andre tiltak enn referansetiltak er valgt (10.3).

## Viktige sitater

- «The SDM uses these data protection goals to transfer the legal requirements of the GDPR into a catalogue of technical and organisational measures» (s. 4)
- «The obligation to implement the protection goals through technical and organisational measures is thus not to be regarded as absolute, but must always be regarded in the context of the specific circumstances of the processing and the associated risks for the rights and freedoms of the data subjects.» (s. 9)
- «not only a person who has to prove trustworthy to an organisation through verifiable characteristics, but an organisation also has to prove that it is trustworthy to the person» (s. 12)
- «The earliest possible time of erasure of personal data that are no longer required is one such measure, certainly the most important and most effective.» (s. 11)
- «A violation of confidentiality in general constitutes a data processing without a legal basis.» (s. 25)
- «Any processing of personal data by an organisation constitutes an interference with the right to informational self-determination.» (s. 33)
- «the level of protection can – according to the SDM – never be below `normal'» (s. 34)
- «In exceptional cases of deviating assessments, however, the level for protection must be given priority in accordance with the data protection principles of SDM.» (s. 36)

## Kryssreferanser

- GDPR: art. 5 (alle prinsipper → beskyttelsesmål), art. 24 nr. 1 og 5 nr. 2 (ansvarlighet/dokumentasjon), art. 25 (innebygd personvern – alle mål), art. 32 (sikkerhet – tilgjengelighet, integritet, konfidensialitet; nr. 1 bokstav d testing), art. 35 nr. 7 og 11 (DPIA-tiltak og gjennomgang), art. 12–22 (rettigheter – intervenerbarhet/åpenhet), art. 28 nr. 3 bokstav b, art. 29, art. 38 nr. 5 (taushetsplikt), art. 40 nr. 2 bokstav d (pseudonymisering), art. 42 (sertifisering), art. 46–47 (overføringsgarantier, BCR). Se tabell 3 og 4.
- Andre kilder:
  - [K32](K32-nsm-grunnprinsipper.md) – NSMs tiltakskatalog dekker særlig tilgjengelighet/integritet/konfidensialitet (virksomhetsperspektiv, jf. SDM 9.2/9.4 om IT-Grundschutz).
  - [K33](K33-cnil-sikkerhetsguide.md) – CNILs sikkerhetstiltak (konkretiserer særlig K-I-T og deler av åpenhet/logging).
  - [K13](K13-dt-innebygd-personvern.md) – innebygd personvern og personvern som standard (art. 25).
  - [K12](K12-dt-dpia-veiledning.md), [K24](K24-wp248-dpia.md), [K28](K28-cnil-pia-metode.md), [K40](K40-dpia-prosess-uld.md) – DPIA-metoder; K40 (ULD Schleswig-Holstein) bygger på samme tyske tradisjon med beskyttelsesmål.
  - [K09](K09-dt-grunnleggende-prinsipper.md) – de grunnleggende prinsippene i art. 5.
  - [K35](K35-cnil-referentiel-audit.md) – revisjonsstandard (sammenlign med SDMs mål–faktisk-sammenligning).

## Aktualitet og begrensninger

- **[Merknad – ikke fra kilden]** Versjon 1.0 (prøveversjon, 2016; engelsk 2017) er **erstattet av nyere versjoner**: SDM v2.0 (2019/2020, tilpasset GDPR) og **v3.0 (2022)** og senere oppdateringer (v3.1), med publisert **referansetiltakskatalog i moduler (Bausteine)**, bl.a. for sletting, logging, dokumentasjon, separasjon, planlegging/spesifikasjon, rettigheter for registrerte m.m. Ved praktisk bruk bør gjeldende versjon på datenschutzzentrum.de / datenschutzkonferenz-online.de benyttes. Nyere versjoner har også en mer GDPR-basert risikomodell i stedet for primært «inngrepsintensitet».
- **[Merknad – ikke fra kilden]** «Sperring» (tysk *Sperrung*, «blocking» i direktiv 95/46) tilsvarer i GDPR «rett til begrensning av behandling» ([art. 18](K43-gdpr-kap03-den-registrertes-rettigheter.md#art-18)). Bruk lovens begrep, se [BEGREPSBANK](../BEGREPSBANK.md).
- Mange henvisninger gjelder **tysk rett før 2018** (gamle BDSG §§ 3a, 4, 9 med vedlegg, delstatslover, tabell 1–2) og direktiv 95/46; disse er historiske.
- Beskyttelsesnivåene (normal/høy/svært høy) bygger på BSI IT-Grundschutz' kategorier. **[Merknad – ikke fra kilden]** GDPR og EDPB bruker i stedet risikovurdering (sannsynlighet × alvorlighet for de registrerte) og terskelen «høy risiko» for DPIA; SDM-nivåene kan brukes som støtte, men erstatter ikke GDPR-risikovurderingen.
- Selve referansetiltakskatalogen (kap. 12) er ikke med i dette dokumentet; tiltakene i kap. 7 er generiske.
- Tabell 4 (fortalepunkter) er rekonstruert fra et tekstuttrekk med usikker kolonneplassering.
- **[Merknad – ikke fra kilden]** SDM er tysk, men metoden er anerkjent internasjonalt (ENISA har omtalt beskyttelsesmålene) og er egnet i norsk sammenheng som struktur for art. 25/32-tiltak.

---
id: K31
tittel: "PIA, application to connected objects (Privacy Impact Assessment Framework for IoT devices)"
utgiver: CNIL (Commission Nationale de l'Informatique et des Libertés, Frankrike)
dato: "Februar 2018 (February 2018 edition)"
spraak: en
fil: "ressurser/cnil-pia-piaf-connectedobjects-en.pdf"
type: metode
gdpr_artikler: [5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 28, 32, 35, 40, 42, 44, 45, 46, 47, 48, 49]
emner: [dpia, pia, eksempel, iot, tilkoblede-objekter, barn, mobilapp, sky, risikovurdering, risikokart, handlingsplan, mål-for-risikobehandling]
relevans: høy
---

# PIA, application to connected objects (CNIL, 2018)

## Sammendrag

Anvendelse av CNILs PIA-metode på tilkoblede objekter (IoT), utformet som en PIA-rapport (48 sider). Dokumentet er dels mal, dels **utfylt eksempel**: grå felt er fylt ut for et fiktivt produkt – en **interaktiv leke med mikrofon og kamera som også kan brukes som babycall**, med mobilapp og nettjeneste, der data lagres hos en tredjeparts vertsleverandør som bruker underleverandører (interaktivitet, bruksanalyse, reklame). Merknader («Note», «NB») gir IoT-spesifikke råd, og beige rammer gir metodestøtte. Strukturen følger 2018-metoden: 1. Kontekst, 2. Grunnleggende prinsipper, 3. Datasikkerhetsrisikoer, 4. Validering, pluss seks vedlegg (minimeringstiltak, risikokilder med kapabiliteter og motiver, alvorlighetsskala, sannsynlighetsskala og trusselkatalog, skalaer for handlingsplan, **typologi av mål for risikobehandling**). Eksemplet viser konkrete risikovurderinger (f.eks. uautorisert tilgang: alvorlighet «Significant», sannsynlighet «Maximum», redusert til «Negligible» sannsynlighet etter tiltak), korrigerende tiltak, risikokart, handlingsplan og valideringstekst. Særlig fokus på barn (formålsbegrensning, ingen profilering, foreldresamtykke).

## Når skal agenten bruke denne kilden

- Når agenten trenger et **utfylt eksempel** på hvordan en DPIA ser ut i praksis (formuleringer, nivå på detaljer, hvordan alvorlighet/sannsynlighet begrunnes, hvordan handlingsplan og validering skrives).
- Ved DPIA for **IoT-produkter, mobilapper, smarthjem, wearables, leker** eller annet med enhet + app + skytjeneste – bruk kolonnestrukturen «Device / Mobile app / Personal account».
- Ved behandling av **barns** personopplysninger.
- Når agenten skal sette **mål for risikobehandling** ut fra risikonivå (vedlegg 6) eller beskrive **risikokilder med kapabiliteter og motiver** (vedlegg 2).
- For fullstendige skalaer og trusselkataloger: se også [K30](K30-cnil-pia-kunnskapsbaser.md) (identiske tabeller).

## Hovedinnhold

### Forord (s. 1)

- Anvendelse av CNILs PIA-guider på IoT. En PIA gjennomføres i prinsippet av behandlingsansvarlig eller leverandør, for å bygge og vise etterlevelse av personvernprinsipper og gi de registrerte kontroll. Metodikken er iterativ.
- Dokumentet er bygget opp som en PIA-rapport (jf. WP29s DPIA-retningslinjer).
- Eksempelprodukt: interaktiv leke/babycall + mobilapp + nettjeneste; data hos tredjeparts vertsleverandør som bruker tjenesteleverandører (interaktivitet, bruksanalyse, reklameselskap).

### Del 1 – Kontekst (s. 2–5)

Utføres normalt av prosjekteier med hjelp fra den som har ansvar for personvern (f.eks. DPO). Mål: klart overblikk over behandlingene.

**1.1 Oversikt** – presenter produktet, art, omfang, kontekst, formål og innsatser («Hva er de forventede fordelene for organisasjonen, de registrerte, samfunnet?»); identifiser behandlingsansvarlig og databehandlere; list relevante referanser – særlig godkjente atferdsnormer (GDPR art. 40) og sertifiseringer (art. 42), sikkerhetspolicy, sektorstandarder.

**1.1.1 Produktbeskrivelse – utfylt eksempel:**

| Felt | Eksempel |
|---|---|
| Product description | Leke med mikrofon, kamera og enkle funksjonsknapper (av/på, handling, reset). Kobles via Wi-Fi og kommuniserer med en dedikert mobilapp (smarttelefon/nettbrett) eller en nettjeneste. |
| Processing purposes | Gi barnet interaktivitet gjennom dialog med leken (spørsmål/svar i naturlig språk via talegjenkjenning). La barnet kommunisere på nett (sende talemeldinger, tekster og bilder) med venner og/eller foreldre. Gi informasjon tilbake til foreldrene (overvåkingsfunksjon). |
| Processing stakes | Skape en ny kategori leker for barn og foreldre ved å utnytte tilkobling, innenfor rettslige rammer og med datasikkerhet. |
| Controller | Firmaet Fab (produsent) |
| Processor(s) | Firmaene Héb (vertskap), Int (interaktiv plattform) og AnaPub (bruksanalyse og reklameselskap) |

**1.1.2 Sektorspesifikke referanser** (art. 35 nr. 8) – tabell «Standards applicable to the processing | Consideration» (f.eks. atferdsnorm, sertifisering, generell sikkerhetspolicy eller PIA-rammeverk).

**1.2 Data, prosesser og støtteressurser** – personopplysninger, mottakere (GDPR art. 4 nr. 9) og lagringstid; prosesser og støtteressurser for hele livssyklusen.

**1.2.1 Data som behandles – utfylt eksempel:**

| Personopplysninger | Kategorier | Mottakere | Personer med tilgang |
|---|---|---|---|
| Brukerinformasjon: fornavn, fødselsdato, kjønn, e-post, telefonnummer | Vanlige data: identifikasjonsdata | Héb | Autorisert personell hos Fab og Héb |
| Data lagt inn i tredjepartsapp (Twitter, Facebook m.m.) via kobling til brukerkontoen | Vanlige data: identifikasjonsdata | Héb | Autorisert personell hos Fab og Héb |
| Registrerte data: tekster/meldinger, lyd, bilder, bevegelser, temperatur, fuktighet; brukerlogger på enhet, app og nettjeneste | Vanlige data: levevaner; data oppfattet som sensitive: bilde og stemme (muliggjør biometrisk behandling); sensitive data (i GDPR-forstand): data om mindreårige | Héb + Int og AnaPub | Autorisert personell hos Fab og Héb + Int og AnaPub |
| Beregnede data: svar på barnas spørsmål og identifisering av interesser for mer relevante svar | Vanlige data: levevaner | Int og AnaPub (+ Héb) | Autorisert personell hos Int og AnaPub (+ Fab og Héb) |
| Bruksanalyse og målrettet reklame | Sensitive data (GDPR): data om mindreårige | Héb + … | Autorisert personell hos Fab og Héb + … |

(Tabellcellene er delvis forskjøvet i tekstuttrekket; tilordningen over er den mest sannsynlige.)

**1.2.2 Livssyklus og prosesser** – dataflytdiagram (ikke gjengitt i tekstuttrekket) og prosesstabell:

| Prosess | Beskrivelse |
|---|---|
| 1. Opprette konto | Brukeren oppgir identifikasjonsdata for å opprette konto |
| 2. Fange data | Data registreres via sensorer |
| 3. Overføre til mobilen | Data overføres til mobilappen, direkte fra enheten eller via skyserverne |
| 4. Legge inn data | Data legges inn i mobilappen |
| 5. Lagre i mobilen | Data lagres i mobilappen |
| 6. Sende til serverne | Data sendes til skyserverne, direkte fra enheten eller via appen |
| 7. Generere interaktivitet | Den interaktive plattformen i skyen genererer svar basert på tidligere dialoger og oppdagede interesser |
| 8. Sende data til leken | Interaktive data sendes tilbake til enheten, direkte eller via appen |
| 9. Lagre på serverne | Fangede og beregnede data lagres på skyserverne |
| 10. Analysere data | Analysealgoritmer kjøres i skyen for bruksstatistikk og reklamemålretting |
| 11. Konsultere skydata | Deler av fangede og beregnede data kan ses via appen eller et personlig nettområde |
| 12. Dele data | Noen data kan overføres til tredjepartsapper eller publiseres i sosiale medier |

**1.2.3 Støtteressurser – utfylt eksempel:**

| IT-systemer (maskinvare, programvare, datakanaler) | Andre støtteressurser (personer, papir, papirkanaler) |
|---|---|
| Enheten (kamera, mikrofon, høyttaler, bevegelsessensorer, temperatur, fuktighet) | Brukeren |
| Brukerens smarttelefon/nettbrett/PC | Brukerens hjem |
| Mobilapp/nettleser | Lokalene til Fab og Héb |
| Wi-Fi-nett | Personell hos Fab og Héb |
| Internett | Lokalene til Int og AnaPub |
| Skyservere hos Héb, Int og AnaPub | Personell hos Int og AnaPub |

NB: Hele del 1 må leses gjennom av DPO for å sikre at den er fullstendig og samsvarer med virkeligheten, siden resten av analysen bygger på den (s. 5).

### Del 2 – Grunnleggende prinsipper (s. 6–19)

Utføres normalt av prosjekteier og vurderes av den som har ansvar for personvern. Mål: bygge systemet som sikrer etterlevelse. Prinsippene: spesifiserte og uttrykkelige formål, lovlighet, minimering, kvalitet, begrenset lagringstid, informasjon, samtykke, innsyn, portabilitet, retting og sletting, protest (retten til å protestere) og begrensning, regulering av databehandlere, overføring ut av EU. Forklar og begrunn valgene; kontroller at forbedring ikke er nødvendig eller mulig; foreslå ev. tilleggstiltak.

**2.1.1 Formål** (art. 5 nr. 1 b) – tabell «Purposes | Legitimacy» (legitimitet: se WP29-uttalelse WP203).
- Note: forklar formål med deling med tredjeparter, særlig reklame og «partnertilbud», og formål om tjenesteforbedring; forklar vilkår for sammenstilling.
- NB (WP29 02/2013 om apper): pga. barns sårbarhet må formålsbegrensning etterleves enda strengere; **behandlingsansvarlige må ikke bruke barnets data til profilering (f.eks. målrettet reklame), direkte eller indirekte**, fordi barnet ikke kan forstå konsekvensene og det går utover det som er rimelig behandling (s. 7).

**2.1.2 Behandlingsgrunnlag** (art. 6) – tabell med de seks grunnlagene, «Applicable | Justification» (identisk med [K29](K29-cnil-pia-maler.md)). Notes: angi rettsgrunnlag ved rettslig plikt/allmenn interesse; flere grunnlag mulig (avtale for primærbruk ved kjøp, samtykke for sekundærformål ved aktivering); forenlighetsvurdering ved viderebehandling (kobling mellom formål, kontekst, opplysningenes art, konsekvenser, nødvendige garantier som kryptering/pseudonymisering).

**2.1.3 Dataminimering** (art. 5 nr. 1 c) – reduser alvorlighet ved å begrense antall data og deretter redusere sensitiviteten (vedlegg 1). Utfylt eksempel:

| Type | Kategori | Data som behandles | Begrunnelse | Minimeringstiltak |
|---|---|---|---|---|
| Vanlige | Sivilstatus, identitet | Fornavn, fødselsdato, e-post, telefon, kobling til sosiale medier | Nødvendig for å lage profil for kommunikasjon | **Ikke etternavn**; **fødselsdato erstattet med alder eller aldersgruppe**; identifiserende data lagret separat i kryptert base |
| Vanlige | Privatliv (levevaner) | Tekster/meldinger, lyd, bilder, bevegelser, temperatur, fuktighet; svar på spørsmål og identifiserte interesser, målrettet reklame | Del av kommunikasjonsfunksjonene | (pseudonymisering for statistisk bruk – se under) |
| Vanlige | Yrkesliv | Ikke samlet inn | | |
| Vanlige | Økonomi og finans | Ikke samlet inn | | |
| Vanlige | Tilkoblingsdata | Applikasjonsspor, tekniske logger | Nødvendig av sikkerhetshensyn og for å kontrollere etterlevelse av vilkår | **Pseudonymisering for statistisk bruk** |
| Vanlige | Lokasjonsdata | Smarttelefonens lokasjon i bilder (hvis aktivert) | **Ikke nødvendig** | **Lokasjon fjernes før bilder sendes** |
| Oppfattet som sensitive | Personnummer | Ikke samlet inn | | |
| Oppfattet som sensitive | Biometri | Rådata: stemme og bilder | Del av kommunikasjonsfunksjonene | |
| Oppfattet som sensitive | Bankdata | Ikke samlet inn | | |
| Sensitive (art. 9/10) | Helse, opinioner m.m.; straffedommer | Ikke samlet inn, men kan fremgå direkte eller indirekte av tekst-, lyd- og videodata | Del av kommunikasjonsfunksjonene | |

(Celletilordningen er rekonstruert fra et forskjøvet tekstuttrekk.)
- Notes: begrunn tydelig innsamling av lokasjon, fødselsdato, alder, vekt m.m.; skill anonyme og pseudonyme data. Tips: unngå fritekstfelt. **NB: for mindreåriges data anses dataene samlet sett som sensitive etter GDPR** (s. 9). NB: behandlingsansvarlige bør særlig avstå fra å samle inn data om foreldre eller familie (f.eks. finansiell informasjon eller helsedata).

**2.1.4 Datakvalitet** (art. 5 nr. 1 d) – tabell med kolonner **Device | Mobile app | Personal account | Justification** for tiltakene: regelmessig kontroll av riktighet; oppfordring til brukeren om å kontrollere/oppdatere; sporbarhet av endringer.

**2.1.5 Lagringstid** (art. 5 nr. 1 e) – lagringstid per datatype, begrunnet; skill vanlige og arkiverte data; slettemekanisme for arkivering/purging; funksjonelle spor og tekniske logger kan ikke lagres i det uendelige. Automatisk mekanisme basert på opprettelses-/sist brukt-dato anbefales. NB: for sensitive og høyrisikodata – sikre sletteverktøy som gjør data uopprettelige. Tabell: Data types (common, archived, functional traces, technical logs) | Storage duration | Justification | Erasure mechanism.

**2.2 Rettigheter** – alle tabeller har kolonnene **Device | Mobile app | Personal account | Justification**, og man oppfordres til å legge ved skjermbilder og dokumentutdrag.

**2.2.1 Informasjon** (art. 12–14) – unntakstabell, ellers tiltak (i tillegg til listen i [K29](K29-cnil-pia-maler.md), IoT-tillegg i kursiv): presentasjon *ved aktivering av enheten* av vilkår for bruk/personvern; tilgang til vilkårene *etter aktivering*; lesbare, forståelige vilkår; enhetsspesifikke klausuler; detaljerte formål; detaljert liste over data; tilgang til identifikatorer i enhet/telefon/PC og om de deles; brukerens rettigheter; *informasjon om at appen kan kjøre i bakgrunnen*; sikker lagringsmetode (særlig ved utkontraktering); *informasjon om beskyttelse av tilgang til enheten*; kontaktinformasjon; *informasjon om muligheten til å gi instrukser om dataenes skjebne etter død* (fransk rett); informasjon om endringer; ved overføring til tredjeparter: formål, data, tredjepartenes identitet.
- NB: ved overføring til tilknyttede tredjeparter – mottakerliste med datakategorier, formål og lenke til deres personvernerklæring, med prosess for oppdatering.
- NB (WP29 02/2013): informasjonen skal presenteres enkelt, på et alderstilpasset språk for små barn – eventuelt som lydmelding.
- Anbefaling: **QR-kode med informasjon på enheten**, og gjør brukerne (foreldrene) oppmerksomme på ansvaret for å informere tredjeparter om at deres data kan bli samlet inn (f.eks. andre barn som snakker med leken eller er med på bilder).

**2.2.2 Samtykke** (art. 7 og 8) – behandlingsansvarlig må kunne vise samtykke; det skal være lett å trekke tilbake. Tiltak: uttrykkelig samtykke ved aktivering; segmentert per datakategori/behandlingstype; uttrykkelig samtykke før deling med andre brukere; forståelig, klart språk tilpasset brukeren (særlig barn); foreldresamtykke for barn under 13; nytt samtykke for hver ny bruker; bekreftelse etter lang inaktivitet; ikon/lys ved behandling av spesielle data (f.eks. lokasjon); samtykkeinnstillinger bevares ved bytte av enhet, reinstallasjon av app eller sletting av cookies.
- NB (art. 8): for informasjonssamfunnstjenester direkte til mindreårige kreves samtykke fra forelder for barn **under 16 år**, med nasjonal adgang til å senke grensen, men ikke under 13; behandlingsansvarlig må gjøre rimelige anstrengelser for å verifisere foreldresamtykket; bevisbyrden ligger hos behandlingsansvarlig/databehandler.
  - **[Merknad – ikke fra kilden]** GDPR art. 8 nr. 2 legger plikten til å treffe rimelige tiltak for å kontrollere foreldresamtykket på den behandlingsansvarlige, ikke på databehandleren (jf. [K43](K43-gdpr-kap02-prinsipper.md#art-8)).
- NB (WP29 02/2013): der mindreårige kan samtykke selv, ta hensyn til begrenset forståelse og oppmerksomhet.

**2.2.3 Innsyn og portabilitet** (art. 15, 20) – unntakstabell; tiltak: tilgang til alle brukerens data via vanlige grensesnitt; sikker visning av bruksspor; nedlasting av arkiv med alle data; portabilitet i lett gjenbrukbart format.

**2.2.4 Retting og sletting** (art. 16, 17, 19) – tiltak: retting; sletting; opplysning om data som likevel lagres; retten til å bli glemt for mindreårige; klare instruksjoner for sletting før kassering av enheten; råd om tilbakestilling før salg; mulighet for sletting ved tyveri av enheten. NB: én måned til å slette eller svare, deretter klage til tilsynsmyndigheten; bruker under 18 ved publisering/kontoopprettelse kan kreve sletting uten begrunnelse (fransk lov om en digital republikk 2016).

**2.2.5 Begrensning og protest** (art. 18, 21) – tiltak: «Privacy»-innstillinger; oppfordring til å endre standardinnstillinger; innstillinger tilgjengelige ved aktivering og etter aktivering; foreldrekontroll for barn under 13; *system for å be om begrensning*; *tekniske midler for å låse tilgang til og bruk av data under begrensning*; *mulighet til å deaktivere funksjoner i enheten (mikrofon, nettleser m.m.)*; *alternative apper for tilgang til enheten*; *mulighet til å protestere mot at appen kjører i bakgrunnen*; etterlevelse ved sporing (cookies, reklame); ekskludering av barn under 13 fra automatisert profilering; effektiv stans av behandling når samtykke trekkes.

**2.2.6 Databehandlere** (art. 28) – tabell «Processor's name | Purpose | Scope | Contract reference | Compliance with Art. 28»; avtale med alle art. 28-elementer.

**2.2.7 Overføringer** (art. 44–50) – tabell per datasett: **Device data / Mobile app data / Personal account data** × France / EU / adekvat land / annet land / begrunnelse og garantier (standardkontrakter, BCR).

**2.3 Vurdering av etterlevelse av grunnprinsippene** – oppsummeringstabell med «Justification | Acceptable/can be improved on? | Corrective controls» for de 12 punktene (5 proporsjonalitet/nødvendighet + 7 rettigheter). Vurderer estimerer om tiltakene gir etterlevelse og angir ev. tilleggstiltak.

### Del 3 – Datasikkerhetsrisikoer (s. 20–31)

Risikodefinisjon (s. 20): hypotetisk scenario med en fryktet hendelse og alle trusler som gjør den mulig – risikokilder (f.eks. ansatt bestukket av konkurrent) utnytter sårbarheter i støtteressurser (filsystem som tillater manipulering) i en kontekst av trusler (misbruk ved e-post) og lar fryktede hendelser inntreffe (uautorisert tilgang) på personopplysninger (kundefil), med konsekvenser (uønskede henvendelser, følelse av krenket privatliv, personlige eller yrkesmessige problemer).

**3.1 Eksisterende eller planlagte tiltak** – utføres normalt av leverandøren/prime contractor og vurderes av informasjonssikkerhetsleder. Tre former: (1) tiltak på dataene (kryptering, anonymisering, partisjonering, tilgangskontroll, sporbarhet), (2) generelle sikkerhetstiltak (driftssikkerhet, backup, maskinvaresikkerhet), (3) organisatoriske tiltak (policy, prosjektstyring, personal, hendelser og brudd, tredjeparter). Kategoriene tilsvarer CNILs sikkerhetsguide; sektorstandarder (art. 35 nr. 8) skal tas hensyn til.

IoT-spesifikke notater (s. 21–22):
- **Kryptering:** tenk på Wi-Fi-sikkerhet (kryptering, lagring av Wi-Fi-passord) og sikring av sertifikater lagret på enheten eller smarttelefonen for autentisering og kryptering av forbindelser.
- **Anonymisering:** skill tydelig anonyme og pseudonyme data.
- **Logisk tilgangskontroll:** tenk på sikkerheten for brukerens passord på enhet, telefon og i skyen – **passord skal lagres hashet med robust algoritme og salt**; beskytt tilgang til appen med eget passord; sikre paringen mellom enhet, app og personlig konto; beskytt data, inkludert metadata (EXIF) og tekniske spor, ved direkte fysisk tilkobling til enheten eller telefonen. Passordregler: CNIL-delib. 2017-012.
- **Driftssikkerhet:** tenk på muligheten for å **oppdatere enheten**.
- Ellers samme veiledningstekster som malene ([K29](K29-cnil-pia-maler.md)): sporbarhet, integritet, arkivering, papir; generelle tiltak (der «Managing workstations» og «Clamping down on malicious software» er slått sammen); organisatoriske tiltak.

**3.1.4 Vurdering av sikkerhetstiltak** – tabell med «Implementation or justification why not | Acceptable/can be improved on? | Corrective controls» for 8 data-tiltak, 11 generelle og 8 organisatoriske tiltak. Vurderer sjekker mot CNILs anbefalte god praksis.

**3.2 Risikovurdering** – utføres normalt av prosjekteier og vurderes av personvernansvarlig. For hver fryktet hendelse: bestem konsekvenser («Hva frykter vi kan skje med de registrerte?»), estimer alvorlighet; identifiser trusler («Hvordan kan det skje?») og risikokilder; estimer sannsynlighet; avgjør om risikoene er akseptable; ellers foreslå tilleggstiltak og vurder residual risiko.
- NB: tiltakene i del 2 og 3.1 må være vurdert (fullstendige og realistiske) før del 3.2, fordi de inngår i risikovurderingen.
- NB: korrigerende tiltak fra 2.3 og 3.1.4 skal tas med i beregningen av residual risiko i 3.2.1–3.2.3, sammen med risikospesifikke tiltak. Alle korrigerende tiltak samles i handlingsplanen (4.1).
- NB: et tilleggstiltak mot én risiko kan påvirke andre risikoer positivt eller negativt.

**3.2.1 Uautorisert tilgang – utfylt eksempel (s. 28–29):**

| Felt | Eksempel |
|---|---|
| Hovedrisikokilder | Ondsinnede bekjente; ondsinnet nabo; ondsinnet ansatt; autorisert tredjepartsselskap; hacker rettet mot en bruker eller ett av selskapene |
| Hovedtrusler | Datatyveri/-innsyn på serveren; kontokapring (via smarttelefon); gjenfinning av kassert enhet |
| Hovedkonsekvenser | Følger av avsløring av potensielt sensitiv informasjon (diskriminering, trusler, angrep, tap av arbeid, tap av tilgang til tjenester m.m.); phishing; målrettet reklame |
| Hovedtiltak som reduserer alvorlighet og sannsynlighet | Minimering; lagringstid; logisk tilgangskontroll; strømkryptering (SSL); maskinvareautentisering; privat sky; klarering av ansatte; tilgangslogging; loggrevisjon; underretning av de registrerte ved brudd på personopplysningssikkerheten med anbefaling av forebyggende tiltak |
| Alvorlighet | **Significant (3)** |
| Sannsynlighet | **Maximum (4)** |

Scenario: «Data could be stolen by an employee with a profit motive or malicious intent, consulted by family or friends taking over the account via the smartphone, or retrieved on a scrapped device by neighbors or a hacker with a view to characterizing a situation bearing on the data subjects' private life.» (s. 28)

Residualvurdering (s. 29):
- **Kan forbedres:** planlagte tiltak reduserer ikke risikoen tilstrekkelig til at den kan aksepteres.
- **Korrigerende tiltak:** kryptere dataene lagret i databasen; informere brukeren om god praksis ved kassering av enheten; utarbeide IT-reglement og taushetserklæring for ansatte.
- **Residual risiko:** data kan ses av familie eller venner som overtar kontoen via smarttelefonen. **Alvorlighet: Significant; Sannsynlighet: Negligible.**

**3.2.2 Uønsket endring – utfylt eksempel (s. 30):**

| Felt | Eksempel |
|---|---|
| Hovedrisikokilder | Uaktsom eller ondsinnet bruker/familiemedlem/venn; ondsinnet nabo; uaktsom eller ondsinnet ansatt; hacker rettet mot ett av selskapene |
| Hovedtrusler | Endring av data på serveren |
| Hovedkonsekvenser | Identitetstyveri; svekket tjenestekvalitet |
| Hovedtiltak | Backup av skyserveren; strømkryptering (SSL); maskinvareautentisering; privat sky; logisk tilgangskontroll; klarering av ansatte; tilgangslogging; loggrevisjon; underretning av de registrerte ved brudd med anbefaling av forebyggende tiltak |
| Alvorlighet | **Limited (2)** |
| Sannsynlighet | **Limited (2)** |

Residualvurdering er ikke utfylt i eksemplet (tomme felt: akseptabel?, korrigerende tiltak, residual alvorlighet/sannsynlighet).

**3.2.3 Forsvinning – utfylt eksempel (s. 31):**

| Felt | Eksempel |
|---|---|
| Hovedrisikokilder | Uaktsom eller ondsinnet bruker/familiemedlem/venn; uaktsom eller ondsinnet ansatt; hacker rettet mot en bruker eller ett av selskapene; skade hos ett av selskapene |
| Hovedtrusler | Sletting av data (via app eller server); skade på servere; fysisk skade på enheten |
| Hovedkonsekvenser | Må opprette brukerkonto på nytt; tap av historikk og personlige tjenesteinnstillinger; svekket tjenestekvalitet |
| Hovedtiltak | Backup av skyserveren; privat sky; fysisk beskyttelse av skyservere; vedlikehold; midlertidig lokal lagring av data; logisk tilgangskontroll; klarering av ansatte; sterk autentisering av ansatte; tilgangslogging; garanti på enheten |
| Alvorlighet | **Limited (2)** |
| Sannsynlighet | **Limited (2)** |

Residualvurdering ikke utfylt i eksemplet.

### Del 4 – Validering (s. 32–38)

Utføres normalt av behandlingsansvarlig med hjelp fra personvernansvarlig. Mål: beslutte om PIA kan aksepteres.

**4.1 Forberedelse** – konsolider funnene:
1. visuell fremstilling av tiltakene for grunnprinsippene etter GDPR-etterlevelse (f.eks. «betinget av forbedring» eller «ansett i samsvar»);
2. visuell fremstilling av sikkerhetstiltakene etter god sikkerhetspraksis;
3. risikokart (initial og residual) etter alvorlighet og sannsynlighet;
4. handlingsplan for tilleggstiltakene: for hvert tiltak minst ansvarlig, kostnad (økonomisk eller arbeidsmengde) og estimert tidsramme.

Formaliser interessentenes bidrag: DPO-råd (art. 35 nr. 2) og de registrertes eller deres representanters syn (art. 35 nr. 9). Alle deler må være vurdert før beslutning.

**4.1.1 og 4.1.2 Kartlegging av etterlevelse** – radardiagrammer («Existing or planned» vs. «With corrective controls») for de 12 grunnprinsipp-punktene og de 27 sikkerhetstiltakene. Skala: **0 Ikke relevant, 1 Kan forbedres, 2 Akseptabelt, 3 God praksis.** (Verdiene i eksemplets diagram fremgår ikke av tekstuttrekket.)

**4.1.3 Risikokart – eksempel (s. 35):** Hvis tilleggstiltakene implementeres korrekt, blir de residuale risikoene:

| Alvorlighet \ Sannsynlighet | 1. Negligible | 2. Limited | 3. Significant | 4. Maximum |
|---|---|---|---|---|
| 4. Maximum | | | | |
| 3. Significant | Uautorisert tilgang (residual) | | | Uautorisert tilgang (initial) |
| 2. Limited | Uønsket endring, forsvinning (plassering usikker i uttrekket) | Uønsket endring, forsvinning (initial) | | |
| 1. Negligible | | | | |

(Uttrekket viser uønsket endring og forsvinning plassert i to celler på nivå 2 alvorlighet; den nøyaktige plasseringen av residualverdiene for disse fremgår ikke sikkert – de ble ikke utfylt i 3.2.2–3.2.3.)

**4.1.4 Handlingsplan – utfylt eksempel (s. 36):**

| Tilleggstiltak | Ansvarlig | Frist | Vanskelighet | Kostnad | Fremdrift |
|---|---|---|---|---|---|
| Informere brukeren om god praksis ved kassering av maskinvaren | Kundeservice og CISO | Måned | Lav | Ingen | Ikke startet |
| Utarbeide IT-reglement for ansatte | Juridisk avdeling og CISO | Måned | Lav | Ingen | Pågår |
| Innføre taushetserklæring for ansatte | Juridisk avdeling og CISO | Måned | Lav | Ingen | Ikke startet |
| Kryptere dataene lagret i databasen | Leverandør (prime contractor) og CISO | Kvartal | Moderat | Moderat | Ikke startet |

NB: alle tiltak i handlingsplanen skal formaliseres, implementeres, følges opp jevnlig og forbedres kontinuerlig.

**4.1.5 DPO-råd** – fast tekst («On dd/mm/yyyy, the Data Protection Officer of the company X issued the following opinion …»). Note: rådet kan gå imot behandlingen uten å binde behandlingsansvarliges beslutning.

**4.1.6 De registrertes syn** (art. 35 nr. 9) – behandlingsansvarlig skal innhente synspunkter der det er relevant, f.eks. via intern/ekstern undersøkelse om behandlingens metoder og formål, spørsmål til tillitsvalgte/fagforeninger, eller undersøkelse blant fremtidige kunder. Går behandlingsansvarlig mot synspunktene, eller anser innhenting som ikke relevant, skal begrunnelsen noteres. Fast tekst: «The data subjects [were/were not] consulted … Justification of the data controller's decision: …»

**4.2 Formell validering** – beslutt om valgte tiltak, residual risiko og handlingsplan er akseptable, med begrunnelse, sett opp mot innsatsene og interessentenes syn. PIA kan bli:
- **validert**;
- **betinget av forbedring** (forklar hvordan);
- **avvist** (sammen med behandlingen).

Gjenta stegene ved behov (se vedlegg 6). Beslutningen foregriper ikke tilsynsmyndighetens vurdering. Eksempeltekst: daglig leder i selskap X validerer PIA for den tilkoblede leken som behandlingsansvarlig; formålene gjentas; tiltakene er ansett akseptable sett opp mot innsatsene; implementering av tilleggstiltak og kontinuerlig forbedring av PIA må dokumenteres (s. 38).

### Vedlegg (s. 39–48)

**Vedlegg 1 – Minimeringstiltak**

| Tiltak | Beskrivelse |
|---|---|
| Filtrering og fjerning | Metadata (f.eks. EXIF i bildefiler) kan samles utilsiktet ved import; identifiser og fjern dem hvis de ikke trengs. |
| Redusere sensitivitet ved konvertering | Sensitive data mottatt som del av generell informasjon eller kun for statistikk kan konverteres til mindre sensitiv form eller pseudonymiseres: slett IP-adressen når by/bydel er utledet; gjenkjenn og sløre personer i overvåkingsvideo; smartmåler aggregerer forbruk over en periode i stedet for sanntid. |
| Redusere identifiserbarhet | Sikre: 1) anonyme data, 2) pseudonyme data (identifiserbar og ansvarlig, men uten å avsløre identitet), 3) ikke-sammenkoblbarhet, 4) ikke-observerbarhet. Valg ut fra truslene; pseudonymisering kan være bedre ved behov for sporbarhet; kombinasjoner mulig. |
| Redusere opphopning | Uavhengige delsystemer med separat tilgangskontroll; kompromittering av ett delsystem begrenser konsekvensene. |
| Begrense tilgang | Need-to-know; egne tilgangspolicyer for sensitive data; kryptering ved overføring og lagring; beskytt midlertidige skyggefiler. |

**Vedlegg 2 – Risikokilder (eksempel for leken)**

| Type | Relevant risikokilde | Kapabiliteter | Motiver | Beslutning |
|---|---|---|---|---|
| Interne menneskelige, tilfeldig eller tilsiktet | Uaktsom eller ondsinnet ansatt | Nærhet til systemet, kompetanse, privilegier og tilgjengelig tid potensielt høye; mulig mangel på opplæring og bevissthet | Klossethet, feil, uaktsomhet; hevn, ønske om å varsle, ondsinnethet; profitt, spionasje | Tatt med |
| Eksterne menneskelige | Uaktsom eller ondsinnet bruker/familiemedlem/venn | Direkte tilgang til enheten og appen | Klossethet, feil, uaktsomhet; lek, ondsinnethet; hevn, spionasje | Tatt med |
| Eksterne menneskelige, tilsiktet | Ondsinnet nabo | Fysisk nærhet som gjør det mulig å hacke enhetens data | Lek, ondsinnethet; hevn, spionasje | Tatt med |
| | Hacker rettet mot en bruker | Kunnskap om brukeren og noe informasjon om vedkommende | Lek, forstyrrelse, ondsinnethet; hevn, spionasje | Tatt med |
| | Hacker rettet mot ett av selskapene | Kunnskap om selskapene som kan skade deres omdømme | Lek, forstyrrelse, ondsinnethet; hevn, spionasje / profitt | Tatt med |
| | Autorisert tredjepartsselskap | Privilegert tilgang kan brukes til urettmessig å få tilgang til informasjon | Profitt, ønske om å få tak i store datamengder og bruke dem | Tatt med |
| Eksterne menneskelige, tilfeldig | Naiv nabo | Fysisk nærhet som gjør det mulig å sende på enhetens kommunikasjonskanal | Uvitenhet | Ikke tatt med |
| Ikke-menneskelige | Hendelse eller skade hos brukeren (strømbrudd, brann, flom m.m.) | Diverse | – | Ikke tatt med |
| | Skade hos ett av selskapene (strømbrudd, brann, flom m.m.) | Diverse | – | Tatt med |

(Tabellen er sterkt forskjøvet i tekstuttrekket. Kildene, kapabilitetene og rekkefølgen av beslutningene – seks «Adopted», to «Not adopted», én «Adopted» – er gjengitt i kildens rekkefølge; tilordningen av motiver og beslutninger til enkeltkilder er rekonstruert og bør kontrolleres mot PDF s. 40. At «skade hos ett av selskapene» er tatt med, støttes av at den brukes som risikokilde i 3.2.3.)

**Vedlegg 3 – Alvorlighetsskala og eksempler på konsekvenser** – identisk med [K30](K30-cnil-pia-kunnskapsbaser.md) §1.5 (nivå 1 Negligible – 4 Maximum, med eksempler på fysiske, materielle og moralske konsekvenser). «Important: these are only examples, which can be very different depending on the context» (s. 41).

**Vedlegg 4 – Sannsynlighetsskala og eksempler på trusler** – samme 4-nivå-skala som [K30](K30-cnil-pia-kunnskapsbaser.md) §1.6 (papirtyveri-eksemplene). I tillegg definisjoner av handlinger på støtteressurser (s. 43):
- **brukt upassende** (used inappropriately): brukt utenfor eller avledet fra tiltenkt kontekst uten å bli endret eller skadet;
- **observert** (observed): observert eller spionert på uten å bli skadet;
- **overbelastet** (overloaded): driftsgrensene overskrides; overbelastet, overutnyttet eller brukt under forhold som hindrer korrekt funksjon;
- **skadet** (damaged): helt eller delvis skadet;
- **endret** (altered): transformert;
- **mistet** (lost): tapt, stjålet, solgt eller gitt bort, slik at eiendomsrett ikke lenger kan utøves.

«The generic threats that follow are designed to be exhaustive, independent and applied to the specific features of privacy protection.» Trusselkatalogene for uautorisert tilgang, uønsket endring og forsvinning (s. 43–47) er de samme som i K30 §1.7–1.9 (med små tillegg, f.eks. «virus» under programvare-skadet).

**Vedlegg 5 – Skalaer for handlingsplanen**

| Kriterium | Nivå 1 | Nivå 2 | Nivå 3 |
|---|---|---|---|
| Vanskelighet | Lav | Moderat | Høy |
| Økonomisk kostnad | Ingen | Moderat | Betydelig (Significant) |
| Frist (Deadline) | År | Kvartal | Måned |
| Fremdrift | Ikke startet | Pågår | Fullført |

(Merk avvik fra K30 §1.10: der er tidsskalaen Kvartal/År/3 år.)

**Vedlegg 6 – Typologi av mål for risikobehandling (s. 48)**

| Risikoprofil | Mål |
|---|---|
| 1. Høy alvorlighet og høy sannsynlighet (nivå 3–4) | **Må absolutt unngås eller reduseres** med tiltak som reduserer både alvorlighet og sannsynlighet. Ideelt sett adresseres med uavhengige tiltak for **forebygging** (før hendelsen), **beskyttelse** (under) og **gjenoppretting** (etter). |
| 2. Høy alvorlighet, lav sannsynlighet (nivå 1–2) | Må unngås eller reduseres med tiltak som reduserer både alvorlighet og sannsynlighet; vekt på **forebyggende** tiltak. Kan aksepteres **bare hvis** det er vist at alvorligheten ikke kan reduseres **og** sannsynligheten er ubetydelig. |
| 3. Lav alvorlighet, høy sannsynlighet | Må reduseres med tiltak som reduserer sannsynligheten; vekt på **gjenopprettings**tiltak. Kan aksepteres **bare hvis** det er vist at sannsynligheten ikke kan reduseres **og** alvorligheten er ubetydelig. |
| 4. Lav alvorlighet og lav sannsynlighet | Bør kunne aksepteres, særlig siden behandlingen av andre risikoer også vil adressere disse. |

Notes: Risikoer kan generelt reduseres, overføres eller beholdes. Noen risikoer kan imidlertid ikke aksepteres, særlig ved behandling av sensitive data eller når skadene for de registrerte kan bli svært betydelige; da kan det være nødvendig å **unngå** dem, f.eks. ved ikke å gjennomføre hele eller deler av behandlingen.

## Praktiske sjekkpunkter

- Kontroller at konteksten er gjennomgått av DPO for fullstendighet og realisme før analysen fortsetter.
- For IoT/app: kontroller at hvert rettighets- og informasjonstiltak er vurdert separat for **enhet, mobilapp og personlig konto/nettjeneste**.
- Kontroller at enheter uten skjerm gir informasjon (QR-kode, app ved første aktivering, eventuelt lydmelding for barn).
- Kontroller at brukeren kan deaktivere mikrofon/kamera/funksjoner, at aktive sensorer signaliseres (ikon/lys), og at bakgrunnskjøring kan avslås.
- Kontroller at barns data ikke brukes til profilering eller målrettet reklame, og at data om foreldre/familie ikke samles inn unødig.
- Kontroller minimeringsgrep som: ikke etternavn, alder/aldersgruppe i stedet for fødselsdato, fjerning av lokasjon/EXIF før bilder sendes, pseudonymisering av logger til statistikk, separat kryptert lagring av identifiserende data.
- Kontroller at passord lagres saltet og hashet med robust algoritme, at paringen enhet–app–konto er sikret, og at enheten kan oppdateres.
- Kontroller at sletting ved kassering/salg/tyveri av enheten er mulig og forklart for brukeren.
- Kontroller at korrigerende tiltak fra vurderingene av prinsipper og sikkerhetstiltak inngår i residualrisikoen og i handlingsplanen.
- Kontroller at hver risiko har et begrunnet scenario (kilder, trusler, konsekvenser) – ikke bare nivåer.
- Kontroller at residual risiko med høy alvorlighet bare aksepteres der sannsynligheten er ubetydelig og alvorligheten ikke kan reduseres (vedlegg 6); ellers vurder å unngå (deler av) behandlingen eller forhåndsdrøfting (art. 36).
- Kontroller at valideringen ender i én av tre utfall: validert, betinget av forbedring, avvist.
- Kontroller at de registrertes syn er innhentet, eller at det er begrunnet hvorfor ikke.

## Viktige sitater

- «the controllers must not use the child's data for profiling purposes (e.g. for targeted advertising), whether directly or indirectly, insofar as it is not possible for a child to understand the implications of this» (s. 7)
- «NB: for processing of minors' details, the data are considered overall to be sensitive pursuant to the [GDPR].» (s. 9)
- «Passwords must be stored properly hashed by a robust algorithm with a salt applied beforehand.» (s. 21)
- «Data could be stolen by an employee with a profit motive or malicious intent, consulted by family or friends taking over the account via the smartphone, or retrieved on a scrapped device by neighbors or a hacker» (s. 28)
- «NB: an additional control carried out to deal with one of the risks can also have a positive or negative effect on the other risks.» (s. 29)
- «this view may be against the processing being implemented, without restricting the decision of the data controller for all that.» (s. 36)
- «validated; conditional on improvement (explain in what way); refused (along with the processing under consideration).» (s. 38)
- «some risks cannot be taken, especially when sensitive data are processed or when the damages that data subjects may sustain are very significant. In such cases it may be necessary to avoid them» (s. 48)

## Kryssreferanser

- GDPR: art. 35 (særlig nr. 2, 7, 8, 9), art. 36, art. 8 (barns samtykke), art. 5, 6, 7, 12–21, 28, 32, 40, 42, 44–50; fortalepunkt 38 (barn), 58 (informasjon til barn), 71 (profilering av barn), 75 (risiko).
- [K28](K28-cnil-pia-metode.md) – metodikken.
- [K29](K29-cnil-pia-maler.md) – tomme maler (samme struktur, uten Device/App/Account-kolonner).
- [K30](K30-cnil-pia-kunnskapsbaser.md) – fullstendig tiltakskatalog, skalaer og trusselkataloger.
- [K39](K39-cnil-mobilapper.md) – CNILs anbefalinger for mobilapper.
- [K24](K24-wp248-dpia.md) – WP248 (DPIA-plikt; innhenting av de registrertes syn).
- [K25](K25-wp259-samtykke.md) – samtykke, inkl. barn.
- [K26](K26-wp260-apenhet.md) – åpenhet, informasjon til barn.
- [K13](K13-dt-innebygd-personvern.md) – innebygd personvern og personvern som standard (personverninnstillinger, minimering).
- [K22](K22-dpia-eksempler.md) – andre DPIA-eksempler.

## Aktualitet og begrensninger

- Utgitt februar 2018, før GDPR fikk anvendelse; viser til WP29-dokumenter (senere videreført/erstattet av EDPB) og til fransk rett (DP-Act, lov 2016-1321 om en digital republikk – instrukser om data etter død, rett til å bli glemt for mindreårige).
- Eksemplet er fiktivt og illustrativt; flere tabeller (risikovurdering for endring og forsvinning, residualnivåer) er bevisst ikke ferdig utfylt.
- Påstanden om at mindreåriges data «overall» anses som sensitive etter GDPR er CNILs formulering. **[Merknad – ikke fra kilden]** Barns personopplysninger er ikke en særlig kategori etter GDPR art. 9, men barn er sårbare registrerte som krever særlig beskyttelse (fortalepunkt 38) og øker risikoen; dette er et kriterium i WP248.
- Aldersgrense for foreldresamtykke: kilden gjengir GDPR art. 8 (16 år, nasjonalt ned til 13) men bruker 13 år i tiltakslistene. **[Merknad – ikke fra kilden]** Norge: 13 år (personopplysningsloven § 5).
- Overføringstabellen bruker «France» som egen kolonne og nevner standardkontrakter/BCR. **[Merknad – ikke fra kilden]** Lovens begreper er «standard personvernbestemmelser» (art. 46 nr. 2 bokstav c) og «bindende virksomhetsregler» (art. 47), og «adekvat land» forutsetter en beslutning om tilstrekkelig beskyttelsesnivå (art. 45) (jf. [K43](K43-gdpr-kap05-overforing-av-personopplysninger-til-tredjestater.md#art-46)). Etter Schrems II (2020) kreves normalt TIA i tillegg; nye standardkontrakter 2021/914; EU–US Data Privacy Framework fra 2023.
- **[Merknad – ikke fra kilden]** CNIL har et eget PIA-verktøy (åpen kildekode) som implementerer samme metodikk, og har senere publisert flere sektorspesifikke anbefalinger (bl.a. for mobilapper, 2024). EU-forordningen om cyberrobusthet (Cyber Resilience Act, 2024) og radioutstyrsdirektivets delegerte forordning stiller nå egne sikkerhetskrav til tilkoblede produkter, som er relevante i tillegg til DPIA.
- Deler av tabellene (data, minimering, risikokilder, risikokart) er rekonstruert fra et tekstuttrekk med forskjøvne kolonner og bør kontrolleres mot PDF ved presis gjengivelse.

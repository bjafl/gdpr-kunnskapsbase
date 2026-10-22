---
id: K32
tittel: "NSMs grunnprinsipper for IKT-sikkerhet, versjon 2.1"
utgiver: Nasjonal sikkerhetsmyndighet (NSM)
dato: "2024-05-31 (v2.1; v1.0 2017-08-28, v1.1 2018-11-01, v2.0 2020-04-15)"
spraak: nb
fil: "ressurser/NSMs Grunnprinsipper for IKT-sikkerhet v2.1.pdf"
type: standard
gdpr_artikler: [5, 24, 25, 28, 32, 33, 34]
emner: [informasjonssikkerhet, sikkerhetstiltak, tiltakskatalog, art32, risikostyring, hendelseshåndtering, tjenesteutsetting, sky, logging, kryptering, tilgangsstyring, sikkerhetskopiering]
relevans: høy
---

# NSMs grunnprinsipper for IKT-sikkerhet v2.1 (NSM, 2024)

## Sammendrag

NSMs grunnprinsipper for IKT-sikkerhet er et sett med prinsipper og konkrete tiltak «for å beskytte informasjonssystemer mot uautorisert tilgang, skade eller misbruk» (s. 3). Dokumentet er organisert i fire kategorier – **1 Identifisere og kartlegge, 2 Beskytte og opprettholde, 3 Oppdage, 4 Håndtere og gjenopprette** – med til sammen 21 grunnprinsipper og ca. 118 nummererte tiltak (f.eks. 2.3.1). Hovedmålgruppen er virksomheter med kritiske samfunnsfunksjoner/kritisk infrastruktur, men prinsippene er relevante for alle offentlige og private virksomheter, både de som drifter selv og de som har satt ut IKT-tjenester (s. 4). Primærlesere er forretnings- og IT-ledelse (systemeiere, sikkerhetsledere, prosesseiere). Tiltakene er teknologiske og organisatoriske; fysisk sikkerhet og menneskelige faktorer omtales i liten grad; hovedfokus er tilsiktede handlinger (s. 5). Grunnprinsippene erstatter ikke sikkerhetsstyring, og valg av tiltak skal baseres på risikovurdering; et anbefalt tiltak som ikke gjennomføres kan gi økt risiko som må vurderes mot risikotoleransen, og eventuelt kompenseres (s. 5).

For kunnskapsbasen er dette den norske **tiltakskatalogen** for «egnede tekniske og organisatoriske tiltak» etter GDPR art. 32 og for tiltaksvurdering i DPIA/risikovurdering og databehandleravtaler (DPA).

## Når skal agenten bruke denne kilden

- Når en DPIA, risikovurdering eller ROS skal foreslå konkrete **sikkerhetstiltak** (art. 32) – bruk tiltaks-ID-ene (f.eks. «NSM 2.6.7 MFA») som referanse.
- Når en **databehandleravtale** skal ha et sikkerhetsvedlegg, eller når en leverandørs sikkerhet skal vurderes: se særlig 2.1.9–2.1.10 (tjenesteutsetting, minimumsundersøkelser av leverandør) og kapitlet om tjenesteutsetting og skytjenester.
- Ved gap-analyse/modenhetsvurdering av en virksomhets IKT-sikkerhet (kartlegge hvilke tiltak som er innført).
- Ved spørsmål om logging/sikkerhetsovervåkning (3.2), hendelseshåndtering og avvik (4.1–4.4, kobles til art. 33/34), sikkerhetskopiering (2.9), kryptering (2.7) og tilgangsstyring (1.3, 2.6).
- Når norsk offentlig sektor ber om «anerkjent norsk rammeverk» for informasjonssikkerhet.

## Hovedinnhold

### Introduksjon (s. 3–9)

**Målgruppe og roller (s. 4–5, figur 1).** Tre nivåer:
- *Toppledelsen* – fokus på organisatorisk risiko, fastsetter forretningsprioritet, kommuniserer risikotoleranse, tildeler budsjett; må ta eierskap. Kategoriene/prinsippene kan brukes som styringsparametere.
- *Forretnings- og IT-ledelsen* – fastsetter retningslinjer for informasjonssikkerhet og fordeler budsjett; kommuniserer status- og risikobilde oppover. Hovedmålgruppen.
- *Implementasjons- og driftsnivå* – etablerer og vedlikeholder tiltakene; rapporterer status oppover.

**Hva grunnprinsippene er (s. 5).** Basert på NSMs erfaringer og tilbakemeldinger fra virksomheter. Gir «et godt forsvar mot cybertrusler, men det er ingen garanti». Suksessfaktorer: ledelsesinvolvering, IKT-sikkerhetskompetanse og etablerte styrings- og rapporteringslinjer. Store virksomheter: de fleste tiltak relevante; mindre virksomheter må prioritere (s. 3). Ulike lovverk kan ha andre krav (f.eks. sikkerhetsloven har flere og strengere krav) (s. 1).

**De fire kategoriene (s. 5–6):**
1. *Identifisere og kartlegge* – forstå virksomheten: styringsstrukturer, ledelsesprioriteringer, leveranser, IKT-systemer og brukere; grunnlaget for de øvrige prinsippene.
2. *Beskytte og opprettholde* – etablere sikker tilstand og opprettholde den over tid og ved endringer (anskaffelse, planlegging, bygging, konfigurasjon).
3. *Oppdage* – oppdage og fjerne kjente sårbarheter og trusler; sikkerhetsovervåkning og analyse for å finne avvik fra normaltilstand.
4. *Håndtere og gjenopprette* – forberede, vurdere, kontrollere og håndtere hendelser, gjenopprette normaltilstand og lære.

**Oppbygning av hvert prinsipp (s. 7):** Grunnprinsippet (overskrift) → Mål med prinsippet → Hvorfor er dette viktig? → Anbefalte tiltak (tabell med ID) → Utdypende informasjon og lenker. Hvert prinsipp er en kontinuerlig aktivitet i hele systemets levetid, fra planlegging til avhending.

**Andre rammeverk (s. 7):** Styringsrammeverk: NSMs veileder i sikkerhetsstyring (for virksomheter under sikkerhetsloven), Digdirs internkontrollveileder (offentlig sektor), ISO/IEC 27001, ITIL. Tiltaksrammeverk: ISO/IEC 27002, CIS Controls, UK NCSC Cyber Essentials og Cyber Assessment Framework (CAF), NIST CSF, NIST SP 800-53, Australian ISM.

**Begreper (s. 8–9):**

| Begrep | Definisjon i kilden |
|---|---|
| Enhet | F.eks. klient, server, skriver, sensor (IoT) eller nettverksutstyr; fysisk eller virtuell |
| Forvaltede enheter | Kontrolleres og driftes av virksomheten; brukeren bør ikke kunne endre sikkerhetskonfigurasjonen på klient |
| Ikke-forvaltede enheter | Ikke kontrollert av virksomheten (BYOD, IoT, besøkende m.m.); bør kun ha tilgang til begrenset del av infrastrukturen |
| Mobile enheter | Alle flyttbare enheter (primært klienter) brukt både innenfor og utenfor lokalene |
| Klient | Datamaskin for sluttbrukere (PC, Mac, mobil, nettbrett, virtuell klient) |
| Server/tjener | Kjører applikasjoner/infrastrukturtjenester; fysisk eller virtuell (hypervisor, containere) |
| Virtuelle enheter | Virtuelle servere, klienter, nettverkskomponenter |
| Godkjentlisting | Tillatte handlinger spesifiseres, alt annet sperres automatisk; regnes som mer effektivt enn blokkeringslisting (v2.1 endret begrepet fra «hvitelisting») |
| IaaS/PaaS/SaaS | Modeller for virtualiserings-/skytjenester |
| IKT-system | Maskinvare, programvare og tilknyttet infrastruktur |
| Informasjonssystem | IKT-system, data og tjenester, bruken av dette og menneskers interaksjon med det |
| Sikkerhetshendelse | Avvikssituasjon med potensial for tap av konfidensialitet, integritet og/eller tilgjengelighet; kan skyldes dataangrep, teknisk svikt eller utilsiktede feilhandlinger |
| Sikker tilstand | Det virksomhetsbestemte normalnivået for sikkerhet |
| Sårbarheter | Alt av organisatorisk og teknisk art som kan utnyttes av en angriper; summen er angrepsflaten |

**Tjenesteutsetting og skytjenester (s. 9).** Sikkerhetstiltak er nødvendige uavhengig av hvem som forvalter tjenestene; grunnprinsippene er like relevante for utsatte tjenester – forskjellen er om kravene stilles til interne eller eksterne leverandører. Før strategisk beslutning om tjenesteutsetting anbefales:
1. Oversikt og kontroll på hele livsløpet
2. God bestillerkompetanse
3. Gode risikovurderinger for å ta riktig beslutning
4. Riktige og gode krav til IKT-tjenesten og til leverandør
5. Riktig beslutning på riktig nivå

«Det man ikke får gjort i forkant av tjenesteutsettingen kan bli utfordrende å få gjennomført senere i kontraktens varighet» (s. 9).

**Endringer fra v2.0 til v2.1 (s. 1):** oppdaterte lenker; «hvitelisting» → «godkjentlisting»; 3.1 presisert til «kjente» sårbarheter og trusler; 2.3.2 presisert om eksekvering/installering; 2.4.1 presisert om nettverksporter.

### Oversikt over prinsippene

| Kategori | Prinsipp | Side | Antall tiltak |
|---|---|---|---|
| 1 Identifisere og kartlegge | 1.1 Kartlegg styringsstrukturer, leveranser og understøttende systemer | 10 | 6 |
| | 1.2 Kartlegg enheter og programvare | 13 | 4 |
| | 1.3 Kartlegg brukere og behov for tilgang | 15 | 3 |
| 2 Beskytte og opprettholde | 2.1 Ivareta sikkerhet i anskaffelses- og utviklingsprosesser | 17 | 10 |
| | 2.2 Etabler en sikker IKT-arkitektur | 20 | 7 |
| | 2.3 Ivareta en sikker konfigurasjon | 22 | 10 |
| | 2.4 Beskytt virksomhetens nettverk | 26 | 4 |
| | 2.5 Kontroller dataflyt | 27 | 8 |
| | 2.6 Ha kontroll på identiteter og tilganger | 29 | 7 |
| | 2.7 Beskytt data i ro og i transitt | 31 | 5 |
| | 2.8 Beskytt e-post og nettleser | 32 | 4 |
| | 2.9 Etabler evne til gjenoppretting av data | 34 | 4 |
| | 2.10 Integrer sikkerhet i prosess for endringshåndtering | 35 | 4 |
| 3 Oppdage | 3.1 Oppdag og fjern kjente sårbarheter og trusler | 37 | 3 |
| | 3.2 Etabler sikkerhetsovervåkning | 38 | 7 |
| | 3.3 Analyser data fra sikkerhetsovervåkning | 41 | 7 |
| | 3.4 Gjennomfør inntrengingstester | 43 | 6 |
| 4 Håndtere og gjenopprette | 4.1 Forbered virksomheten på håndtering av hendelser | 45 | 6 |
| | 4.2 Vurder og klassifiser hendelser | 47 | 3 |
| | 4.3 Kontroller og håndter hendelser | 48 | 6 |
| | 4.4 Evaluer og lær av hendelser | 50 | 4 |

*Merk: Tiltaks-ID-ene i tekstuttrekket er forskjøvet i forhold til beskrivelsene; nummereringen under er rekonstruert ut fra rekkefølge og dokumentets egne kryssreferanser (f.eks. «2.3.1 (sikkerhetsoppdateringer)», «2.6.4.a (unngå admin-rettigheter)», «2.5.4» om isolering). Kontroller mot PDF ved behov for eksakt sitering.*

---

### Kategori 1 – Identifisere og kartlegge

#### 1.1 Kartlegg styringsstrukturer, leveranser og understøttende systemer (s. 10–12)

**Mål:** Virksomheten identifiserer strukturer og prosesser for sikkerhets- og risikostyring, kartlegger leveranser, informasjonssystemer og understøttende funksjoner og vurderer dem opp mot fastsatte toleransegrenser for risiko for å etablere og justere tiltak.

**Hvorfor:** Uten styringsstrukturer og risikoprosesser får ledelsen ikke informasjon til å prioritere. Ved manglende oversikt kan mindre viktige deler være godt sikret mens vitale deler er eksponert. Tilgjengelighet, integritet og konfidensialitet må vurderes.

| ID | Tiltak |
|---|---|
| 1.1.1 | Identifiser virksomhetens strategi og prioriterte mål, samt regelverk, bransjenormer og avtaler som kan ha innvirkning på sikring av informasjonssystemer. |
| 1.1.2 | Identifiser strukturer og prosesser for sikkerhetsstyring: a) policyer fra ledelsen, b) ledelsesstruktur med veldefinert ansvar og ansvarslinjer, c) prosesser for risikostyring (1.1.3), d) fastsatte toleransegrenser for risiko (1.1.4), e) tilstrekkelige ressurser og fagkompetanse. f) Etabler dette dersom det mangler, tilpasset og integrert i virksomhetsstyringen. |
| 1.1.3 | Identifiser prosesser for risikostyring knyttet til IKT: a) verdivurdering, b) trusselvurdering, c) kartlegge eksisterende tiltak, d) risikoidentifisering, e) risikovurdering, f) risikorapportering, g) risikohåndtering, h) etablere/justere tiltak, i) verifisere at tiltakene fungerer etter hensikt. j) Etabler prosesser dersom de mangler. |
| 1.1.4 | Identifiser toleransegrenser for risiko knyttet til IKT. Ledelsen fastsetter hva som aksepteres og hva som er uakseptabelt; kommuniseres på tvers. Vanlig å fastsette grenser basert på konsekvens ved tap av konfidensialitet, integritet og tilgjengelighet. Se 4.1.1, 4.1.2. |
| 1.1.5 | Kartlegg leveranser, informasjonssystemer og understøttende IKT-funksjoner: a) IKT-systemer, data og tjenester inkl. eierskap, b) kritiske forretningsroller, c) interne og eksterne IKT-avhengigheter, d) grupper etter risikoaksept (1.1.4) og bruk som grunnlag for sikker IKT-arkitektur (2.2). |
| 1.1.6 | Kartlegg informasjonsbehandling og dataflyt – informasjonsflyt mellom arbeidsprosesser, brukere, enheter og tjenester – som grunnlag for sikker IKT-arkitektur (2.2). |

**Utdypende (s. 11–12):** Tilpass sikkerhetsstyringen til virksomhetens størrelse. Velg en overkommelig risikometode (eksempler: ISO/IEC 27005, NIST SP 800-30, OCTAVE Allegro). Kartlegging av leveranser brukes som utgangspunkt for sikkerhetsarkitektur, soneinndeling, tilgangsstyring, konfigurasjon, logging og overvåkning. Se tiltak i sammenheng; vurder effekt av eksisterende tiltak opp mot verdiene. «Sikkerhetstiltakene er riktig implementert, men er de riktige tiltakene implementert på rett sted?» (s. 12). Lenker bl.a. til NSMs veileder i sikkerhetsstyring, Digdirs internkontroll i praksis, DSBs «Risikostyring i digitale verdikjeder», ISO/IEC 27001.

#### 1.2 Kartlegg enheter og programvare (s. 13–15)

**Mål:** Oversikt over forvaltede (og ikke-forvaltede) enheter og programvare på nettverket og gjeldende konfigurasjon.

**Hvorfor:** Kartleggingen skal avdekke virksomhetsstyrte enheter, legitime enheter med begrensede rettigheter (IoT) og ukjente enheter (private eller ondsinnede), og all programvare inkl. uautorisert. Virksomheten må få oversikt før angriperne gjør det.

| ID | Tiltak |
|---|---|
| 1.2.1 | Etabler en prosess for å kartlegge enheter og programvare. Bruk fortrinnsvis automatiserte, sentraliserte verktøy som viser hvilken programvare som er på hvilke enheter. Inkluder eierskap, eldre ikke-støttede produkter (merkes eksplisitt), og enheter/programvare som ikke er koblet til nettverket (f.eks. USB). |
| 1.2.2 | Fastsett retningslinjer for godkjente enheter og programvare: a) avgjør i) hva ansatte har behov for, ii) hva som ikke er tjenstlig nødvendig men likevel lov, iii) hva som er uønsket, iv) hvordan dette håndteres; b) utarbeid og vedlikehold oversikt over godkjente enheter og programvare (evt. versjonsnummer), vurdert mot 2.1–2.3; c) kommuniser retningslinjene, beskriv formål og lovlig bruk. |
| 1.2.3 | Kartlegg enheter: a) f.eks. nettverksadresse, maskinvareadresse, enhetsnavn, avdeling, om forvaltet; alle enheter med IP-adresse (PC-er, servere, nettverksutstyr, skrivere, lagringsnett, IP-telefoner, IoT); b) alle mobile enheter og lagringsmedier med virksomhetsinformasjon brukt utenfor nettet; c) plan for håndtering av ikke-godkjente enheter (se 2.4.1.b); d) oversikt over virtuelle enheter (egne eller i leverandørs sky – for leverandør primært ved IaaS). Konsekvent godkjentlisting av enheter/forbindelser forenkler kartleggingen (se 2.4). |
| 1.2.4 | Kartlegg programvare: a) firmware, operativsystem og applikasjoner (navn, versjon, produsent, installasjonsdato, om støttet) på servere, klienter, nettverksutstyr m.m.; b) plan for håndtering av programvare som skal godkjennes. Godkjentlisting av applikasjoner (eller applikasjonsbutikk) forenkler. |

**Utdypende (s. 14):** Angripere leter etter ubeskyttede systemer og sårbare versjoner; ikke-forvaltede enheter (BYOD) gir liten kontroll og kan være kompromittert. «Én kompromittert maskin blir raskt til mange.» Der full kontroll ikke er mulig: vurder kompenserende tiltak som forsterket deteksjon, segregering og lavere eksponering av verdifull informasjon. Lenker: NCSC CAF A3, CIS Controls 1 og 2.

#### 1.3 Kartlegg brukere og behov for tilgang (s. 15–16)

**Mål:** Oversikt over brukergrupper, brukere og tilgangsbehov, og kartlagt ansvar for IKT-sikkerhet. Leses sammen med 2.6.

**Hvorfor:** Angriperes første mål er ofte å øke tilgang (overta kontoer, eskalere rettigheter). Hvis alle har tilgang til for mye, kan én kompromittert bruker kompromittere hele systemet; tilgang må deles opp for å begrense skade fra kompromittering eller utro ansatte.

| ID | Tiltak |
|---|---|
| 1.3.1 | Kartlegg brukere: a) brukeridentitet, b) arbeidslokasjon(er), c) tilgangsbehov til IKT-systemer, tjenester/applikasjoner, d) spesielle rettighetsbehov (1.3.2). Se 2.2 og 2.6. |
| 1.3.2 | Kartlegg og definer brukerkategorier for tilgangsnivåer og oppfølging, f.eks.: normale brukere (kun kontorstøtte); brukere med spesialbehov/utvidede rettigheter (utviklere); driftsbrukere; leverandører og konsulenter; systembrukere (bakgrunnsprosesser som sikkerhetskopiering). |
| 1.3.3 | Kartlegg ansvar og roller knyttet til IKT-sikkerhet: a) internt (sikkerhetssjef, IT-sjef, applikasjonsansvarlig, plattformansvarlig m.m.), b) hvem som skal kontaktes ved hendelser (4.1.1, 4.1.3), c) roller og oppgaver hos eksterne leverandører og partnere. |

**Utdypende (s. 16):** Bevisste brudd (innsider som utnytter rettigheter, ekstern angriper som tar over konto) og ubevisste (ansatt endrer innstillinger, sletter informasjon, åpner skadevare). Lenker: NSM temarapport innsiderisiko, NCSC CAF B2, CIS Control 14.

---

### Kategori 2 – Beskytte og opprettholde

#### 2.1 Ivareta sikkerhet i anskaffelses- og utviklingsprosesser (s. 17–19)

**Mål:** Sikkerhet er integrert i anskaffelse og utvikling, og risiko for at nye IKT-produkter/-tjenester innfører konfigurasjons- og arkitektursårbarheter minimeres.

**Hvorfor:** Produkter med svak sikkerhet eller dårlig integrasjon øker sårbarheten. Uten gode prosesser for utvikling, test og verifisering oppdages ikke sårbarheter; å rette i etterkant er ofte dyrere.

| ID | Tiltak |
|---|---|
| | *Anskaffelse av IKT-produkter* |
| 2.1.1 | Integrer sikkerhet i anskaffelsesprosessen. Fastsett krav til IKT-sikkerhet ved anskaffelse av alle IKT-produkter og -tjenester (se 2.2). Inkluder sikkerhet i hele livsløpet fra anskaffelse til avhending. |
| 2.1.2 | Kjøp moderne og oppdatert maskin- og programvare: a) bruk kun produkter som støttes og mottar sikkerhetsoppdateringer, b) anskaff kun produkter med nyere sikkerhetsfunksjonalitet og protokoller, c) fas ut eldre produkter, d) be der det er hensiktsmessig leverandøren i) informere om risikoer og sårbarheter og ii) spesifisere hvordan produktet kan herdes. |
| 2.1.3 | Foretrekk produkter som er sertifisert og evaluert av tiltrodd tredjepart (f.eks. Common Criteria). |
| 2.1.4 | Reduser risiko for målrettet manipulasjon i leverandørkjeden: a) vurder risiko for slike angrep, b) be nasjonale forhandlere/importører vise diskresjon om kundeinformasjon (kundenavn, bruk, brukere, sted), c) beskytt produktintegritet for fysiske produkter så tidlig som mulig; inspiser for brutte forseglinger og begrens fysisk adgang, d) last ned programvare kun fra leverandørens offisielle nettside (https); oppbevar installasjonsprogramvare der kun installasjonsansvarlig har skrivetilgang, e) reguler og kontroller leverandørers fysiske adgang ved vedlikehold. |
| | *Utvikling og test (egen programvareutvikling)* |
| 2.1.5 | Bruk en metode for sikker programvareutvikling: a) planlegging (behov, rammebetingelser, sikkerhet, opplæring), b) analyse av brukerbehov inkl. sikkerhetskrav, c) design basert på krav, d) utvikling inkl. sikker koding og testing (2.1.6, 2.1.7), e) implementasjon og idriftsetting, f) sikkerhetsmessig forvaltning: i) planlegge sikkerhetsoppdateringer og distribusjon, ii) støtte for nyere sikkerhetsfunksjonalitet. |
| 2.1.6 | Bruk separate miljøer for utvikling, test og produksjon. Vurder soneinndeling (2.2.3). **Sensitive produksjonsdata bør bare benyttes på utviklings- og testmiljø som er sikret.** |
| 2.1.7 | Test tilstrekkelig gjennom hele utviklingsprosessen slik at feil og sårbarheter rettes før idriftsetting: a) test av at sikkerhetsfunksjoner fra ulike produkter fungerer sammen, enhetstest, integrasjonstest, systemtest, akseptansetest, pilottest, inntrengingstest (3.4) og stresstest; b) kontroller at kun tillatte handlinger virker, stikkprøver på at andre avvises. |
| 2.1.8 | Vedlikehold programvarekode: a) metodisk sikkerhetsvurdering av koden, b) særlig oppmerksomhet på sikkerhetskritisk kode: i) tilgangskontroll, ii) kryptering av trafikk, iii) logging, iv) parsing av brukerinput, v) buffer overflow (jf. OWASP Top Ten), c) sjekk regelmessig (helst automatisk) for nye versjoner av open source og kommersielle toolkits, d) automatiser sikkerhetssjekk av egen kode ved DevOps/DevSecOps; kvalitetssikre sikkerhetsrelevant kode. |
| | *Tjenesteutsetting – herunder skytjenester* |
| 2.1.9 | Ta ansvar for sikkerheten også ved tjenesteutsetting: a) oversikt og kontroll på hele livsløpet, b) bestillerkompetanse (forvaltning, administrasjon, IT-arkitektur) gjennom hele livsløpet, c) gode risikovurderinger som inkluderer IKT og hele livsløpet, d) kravdokument for alle faser der krav kan verifiseres, e) avtaler og endringer behandles iht. fullmaktsstrukturen. «Det understrekes at virksomhetens ansvar for sikkerheten ikke forsvinner selv om man tjenesteutsetter.» |
| 2.1.10 | Undersøk sikkerheten hos tjenesteleverandøren. **Som minimum** om leverandøren: a) har styringssystem for informasjonssikkerhet og evt. sertifisering (f.eks. ISO/IEC 27001), b) gir innsyn i sikkerhetsarkitekturen, c) har utviklingsplaner for fremtidig sikkerhetsfunksjonalitet, d) har oversikt over hvem som skal ha innsyn i virksomhetens informasjon, hvor og hvordan den behandles og lagres, og grad av segregering fra andre kunder, e) har sikkerhetsfunksjonalitet som dekker behovene, f) har sikkerhetsovervåkning, g) har rutiner for hendelseshåndtering og avviks- og sikkerhetsrapportering, h) har krise- og beredskapsplaner som harmonerer med virksomhetens, i) har godkjenningsprosedyrer for underleverandører og deres underleverandører, j) har spesifisert aktiviteter ved terminering, bl.a. tilbakeføring/flytting/sletting av informasjon. |

**Utdypende (s. 19):** DevOps/DevSecOps visker ut skillet mellom utvikling og drift; vær ekstra påpasselig, automatiser sikkerhetsprosedyrer for kode. Lenker bl.a.: NSMs sikkerhetsfaglige anbefalinger ved tjenesteutsetting, NSM «Nasjonal kontroll av IKT-tjenester», Datatilsynets veileder om programvareutvikling med innebygd personvern, DFØ om anskaffelser, regjeringens veileder om sikkerhet i offentlige anskaffelser, NCSC secure development, CIS Control 16, Common Criteria, OWASP Top Ten.

#### 2.2 Etabler en sikker IKT-arkitektur (s. 20–21)

**Mål:** Helhetlig sikkerhetsarkitektur som gir ønsket sikkerhetsnivå gjennom sikkerhetsfunksjoner og -strukturer med mulighet for etterprøvbarhet.

**Hvorfor:** En angriper går minste motstands vei. Momenter: mange sikkerhetsfunksjoner og produkter fra ulike produsenter må fungere sammen (klassisk feil: egen brukerdatabase i en applikasjon i stedet for felles); drift og konfigurasjon bør skje sentralt og likt per enhetstype; systemet bør deles opp etter tillitsnivå (nettverk og logiske deler/domener).

| ID | Tiltak |
|---|---|
| 2.2.1 | Etabler og vedlikehold en helhetlig sikkerhetsarkitektur. Følgende funksjoner bør implementeres, sikres og fungere godt sammen: a) styring av brukere og kontoer, b) kontroll og oversikt over enheter, c) styring av tilgang til ressurser og tjenester, d) kontroll på programvare (særlig klienter), e) operativsystemer, f) verktøy for drift og virtualisering (on-prem og sky), g) nettverksenheter og brannmurer, h) håndtering av skadevare, i) kryptografiske moduler, j) digitale sertifikater og PKI, k) databaser, l) systemovervåkning, m) styring av sikkerhetskonfigurasjoner, n) IDS/IPS, o) sikkerhetskopiering og gjenoppretting, p) maskinvare og fastvare. Mest mulig sentralisert og automatisert drift. |
| 2.2.2 | Bygg med produkter som fungerer godt sammen sikkerhetsmessig: a) modulbaserte (aktiver kun nødvendig funksjonalitet), b) følger bransjestandarder for tilgangskontroll, logging, drift, kodekontroll, ressursstyring og tilgjengelighet, c) fungerer sammen på tvers av leverandører; gjenbruk identiteter fra felles kilde i stedet for produktspesifikke identiteter. |
| 2.2.3 | Del opp nettverket etter risikoprofil i soner (f.eks. systemadministrasjon, applikasjonsservere, virksomhetsdriftede klienter, industriell produksjon/SCADA, internett-aksess, trådløst, gjesteklienter, eksternt tilgjengelige tjenester; i datasentre data-, kontroll- og driftssone). Kan gjøres med VLAN, virtualiserte nett, mikrosegmentering. Sentral drift av soner. Bruk soneinndelingen til å styre dataflyt (2.5). |
| 2.2.4 | Skill fysisk de mest kritiske delnettverkene; særskilt sensitive delnett vurderes fysisk adskilt («air gap»). |
| 2.2.5 | Del opp domenearkitekturen etter behov; som minimum holdes klienter adskilt fra servere. |
| 2.2.6 | Reguler tilgang til tjenester basert på kjennskap til både bruker og enhet (ikke-forvaltet enhet gir tilgang til færre tjenester enn forvaltet). |
| 2.2.7 | Etabler en robust og motstandsdyktig arkitektur for tilgjengelighet til kritiske funksjoner: a) risikovurder maskinvarefeil, menneskelige driftsfeil, dataangrep, internett-tilgjengelighet (bl.a. tjenestenekt), leverandørtilgjengelighet, strøm, naturskade og geopolitisk situasjon; b) gjør deler mer robuste – duplisert internettforbindelse, duplisert datasenter, dupliserte domenekontrollere, delvis tjenesteutsetting, reservestrøm, lager av reservedeler m.m. |

Lenker: NSM om IT-modernisering, NCSC Cyber security design principles, «Secure by design», NCSC CAF B4, ISO/IEC 27033.

#### 2.3 Ivareta en sikker konfigurasjon (s. 22–25)

**Mål:** Maskin- og programvare konfigureres etter virksomhetens sikkerhetsbehov, med rutiner for sporing, rapportering og korrigering av sikkerhetskonfigurasjon.

**Hvorfor:** Standardkonfigurasjoner er laget for enkel installasjon, ikke sikkerhet (åpne porter, standardkontoer og -passord, eldre protokoller, forhåndsinstallert programvare). Virksomheter må herde produktene. Gjelder både fysiske og virtuelle enheter.

| ID | Tiltak |
|---|---|
| 2.3.1 | Etabler sentralt styrt regime for sikkerhetsoppdatering; installer oppdateringer så fort som mulig. a) Prioriteringsliste (klientenes OS og applikasjoner først, deretter servere med standardapplikasjoner/OS, skrivere, nettverksenheter), b) rutine med klare ansvarsforhold for i) hyppighet (automatiser) og ii) ansvarlig når oppdatering ikke kan gjennomføres/utsettes, c) isoler det som er vanskelig å holde oppdatert (2.5.4), d) automatiser og forenkle. |
| 2.3.2 | Konfigurer klienter slik at kun kjent programvare kjører (programvare trenger ikke være installert for å kjøre). a) Godkjentlist alle programmer, helst ved signering av tiltrodd part/applikasjonsbutikk; stram inn med MDM; b) uten applikasjonsbutikk: applikasjons-godkjentlisting, fortrinnsvis filmappebasert; c) finkorn ved å sperre uønskede leverandørsignerte programmer, f.eks. skriptmotorer (powershell*.exe) for sluttbrukere; d) makroer/dokumentkode: i) fjern uønsket kode fra eksterne dokumenter og e-post før de når brukerne, ii) deaktiver for brukere som ikke trenger det, iii) godkjentlist nødvendig kode (signering). |
| 2.3.3 | Deaktiver unødvendig funksjonalitet i OS og applikasjoner på klienter, servere og nettverksutstyr: i) eldre/ubrukte protokoller, ii) innebygd støtte for personlige skytjenester, iii) andre tjenester som ikke brukes. |
| 2.3.4 | Etabler og vedlikehold standard sikkerhetskonfigurasjoner, ideelt én per enhetstype (OS, brannmurer, nettverksutstyr, applikasjoner, maskinvare): a) sentralisert og standardisert drift, b) jevnlig gjennomgang og oppdatering, c) endringer via endringshåndtering og av autoriserte, d) kun autorisert driftspersonale kan endre, ikke sluttbrukere. |
| 2.3.5 | Verifiser at aktivert konfigurasjon er i henhold til godkjent konfigurasjon: a) regelmessig sammenligning, b) uautoriserte endringer undersøkes, rapporteres og håndteres, c) godkjent konfigurasjon integritetsbeskyttes; kun IT- og sikkerhetsansvarlige har innsyn, d) automatiser, kjør f.eks. hver natt. |
| 2.3.6 | Utfør konfigurasjon, installasjon og drift på en trygg måte: a) over tiltrodde kanaler – i) betrodde TLS-sertifikater på administrative grensesnitt (2.7.1, 2.7.2), ii) ikke eksponer administrative grensesnitt mot internett eller tjenestebrukere; b) bruk tiltrodde, dedikerte klienter til drift; c) minimer interaktiv pålogging på servere og klienter (risiko for «Pass the hash»). |
| 2.3.7 | Endre alle standardpassord før produksjonssetting (applikasjoner, OS, rutere, brannmurer, skrivere, aksesspunkter). Bruk sertifikatbasert autentisering der mulig og reduser passordbasert autentisering over nettverk. |
| 2.3.8 | Ikke deaktiver kodebeskyttelsesfunksjoner («exploit protection» som DEP, SEHOP, ASLR). Lag unntaksregler for eldre applikasjoner i stedet for å slå av beskyttelsen; kontakt leverandøren. |
| 2.3.9 | Etabler sikker tid: velg tidskilder med høyere tillit og kontroller at alle enheter bruker tid med ønsket kvalitet. |
| 2.3.10 | Reduser risiko ved IoT-enheter: a) plan for innføring med risikovurdering, inkl. skyen enhetene kobler seg til; b) kjøp kun enheter som i) kan sikkerhetsoppdateres, ii) kan bytte alle standardpassord, iii) kan tvinges til kun å bruke nett virksomheten kontrollerer; c) monitorer trafikken (3.2); d) isoler i egne soner (2.2, 2.5); e) vurder fysisk tilgjengelighet. |

**Utdypende (s. 24–25):** Manglende herding er ofte årsak til at angripere får fotfeste. Konfigurasjonen svekkes over tid; må oppdateres og verifiseres jevnlig. Støtt deg på leverandørens «best practice» og andre nasjoners sikkerhetsmyndigheter. Lenker: NSM «Fem effektive tiltak mot dataangrep» (nsm.no/5tiltak), NCSC configuration management, CIS Control 4, CIS IoT Companion Guide, CIS Benchmarks.

#### 2.4 Beskytt virksomhetens nettverk (s. 26)

**Mål:** Virksomheten kontrollerer og beskytter nettverkene mot interne og eksterne trusler.

**Hvorfor:** Skillet mellom innside og utside blir mindre (mobile enheter, hjemmekontor, eksterne tjenester). Angrep kan komme innenfra (kompromittert klient/server, utro tjener, kompromittert leverandør, svakt trådløst nett, manglende fysisk sikring). Enheter bør ikke ukritisk stole på alt på eget nett; tilgang sikres og trafikk krypteres.

| ID | Tiltak |
|---|---|
| 2.4.1 | Etabler tilgangskontroll på flest mulig nettverksporter (fysiske, trådløse eller virtuelle): a) trafikk kun på godkjente porter (godkjentlisting), b) kun forvaltede enheter, c) ikke-forvaltede enheter kun på gjestenett e.l. |
| 2.4.2 | Krypter alle trådløse og kablede forbindelser: a) trådløst med tidsriktige protokoller som WPA2/WPA3 «enterprise», b) kablede i egne nett – minst de som ikke er fysisk kontrollert av virksomheten. |
| 2.4.3 | Kartlegg fysisk tilgjengelighet for svitsjer og kabler (mellom bygninger, etasjer delt med andre, lokasjoner, resepsjoner) dersom ikke alle forbindelser autentiseres og krypteres. |
| 2.4.4 | Aktiver brannmur på alle klienter og servere: a) reguler inn-/utgående trafikk, b) logg sikkerhetsrelevante hendelser, integrert med sikkerhetsovervåkning, c) integrer klient/server-logging med sentral logging. |

Lenker: NSM «Sikkerhetstiltak mot digital utpressing og andre angrep», CIS Control 12.

#### 2.5 Kontroller dataflyt (s. 27–28)

**Mål:** Kontroll på informasjonsflyten mellom systemdeler (enheter kommuniserer kun etter vedtatte regler) og inn og ut av virksomheten.

**Hvorfor:** Angrep starter ofte på en mindre viktig maskin og beveger seg videre. Kontrollert dataflyt hindrer spredning, tvinger trafikk gjennom sikkerhetstiltak og isolerer kritiske/sårbare/eksponerte enheter.

| ID | Tiltak |
|---|---|
| 2.5.1 | Styr dataflyt mellom nettverkssoner: a) filtrer godkjentlistet trafikk mellom soner og mot internett (kriterier: IP, sone-ID, protokoll, applikasjon, bruker m.m.), b) dokumenter og begrunn reglene (inkl. endringer), c) sjekk regelmessig at faktisk konfigurasjon samsvarer med ønsket dataflyt. |
| 2.5.2 | Begrens tilgang til interne tjenester fra eksterne lokasjoner: a) kun forvaltede enheter til kritiske interne tjenester, b) ikke-forvaltede/private enheter kun etter kritikalitetsvurdering (f.eks. e-post, timeregistrering) med risikoreduserende tiltak (mindre funksjonalitet, kortere historikk, ekstra autentisering). |
| 2.5.3 | Sperr all direktetrafikk mellom klienter; peer-to-peer bør gå via servertjeneste, alternativt minimeres etter tjenstlig behov. |
| 2.5.4 | Isoler sårbart utstyr med lav tillit: a) utdaterte applikasjoner og gamle servere med ikke-støttet OS (kun én godt sikret server/proxy har direkte tilgang), b) skrivere med svak konfigurasjon og manglende oppdatering. |
| 2.5.5 | Styr dataflyten til spesielt eksponerte tjenester (web, e-post med eksternt innhold); ingen direkte dataflyt mellom disse og de mest kritiske tjenestene. |
| 2.5.6 | Beskytt spesielt kritiske tjenester med egen dataflyt (f.eks. sikkerhetskopiering); vurder validering på applikasjonslaget (applikasjonsbrannmur). |
| 2.5.7 | Ha kontroll på trafikk mellom virksomheten og samarbeidspartnere/tjenesteleverandører; styr trafikken kun til relevante deler. |
| 2.5.8 | Styr all trafikk til/fra forvaltede mobile klienter via virksomhetens nett, ikke direkte til internett – for å hindre og detektere datalekkasje fra kompromitterte klienter. |

**Utdypende (s. 28):** Verktøy: svitsjer, rutere, brannmurer (også vertsbrannmurer), domeneskiller, proxyer, DMZ, IDS/IPS; høyt sikkerhetsbehov → forsvar i dybden. Dataflyten må oppleves hensiktsmessig, ellers finner brukerne usikre løsninger (minnepinner, privat skylagring).

#### 2.6 Ha kontroll på identiteter og tilganger (s. 29–30)

**Mål:** Oversikt over identiteter og kontoer, og effektiv tilgangsstyring iht. retningslinjer. Leses sammen med 1.3.

**Hvorfor:** Angripere søker kontroll over legitime brukere og eskalerer rettigheter. Mange ansatte har flere rettigheter enn nødvendig (skrive/slette alt, kjøre all programvare). Ubrukte kontoer (leverandører, tidligere ansatte) misbrukes.

| ID | Tiltak |
|---|---|
| 2.6.1 | Etabler retningslinjer for tilgangskontroll: a) dekk flest mulig ressurser (brukere, klienter, fellesmapper, serverapplikasjoner, servere, nettverks- og sikkerhetsenheter, databaser), b) **minste privilegiums prinsipp** – ofte holder leserettigheter, c) alle kontoer sporbare til ansvarlig bruker (også upersonlige), d) alle kontoer, tilganger og rettigheter sporbare til rolle/person som godkjente, e) revider jevnlig – særlig drifts- og spesialbrukere, f) gjenbruk identiteter på tvers (ideelt single sign-on), g) passord er personlige og hemmelige og deles aldri, heller ikke med kolleger/overordnede; klienter låses når de forlates. |
| 2.6.2 | Formell prosess for administrasjon av kontoer, tilganger og rettigheter: a) i) kontoer for brukere, enheter og systemprosesser, ii) tilganger til systemer og applikasjoner, iii) rettigheter i OS (admin) og felles brukerdatabase; b) hele livssyklusen: opprettelse, vedlikehold og deaktivering – **deaktiver fremfor å slette** for å bevare revisjonsspor iht. lover og regler; c) retningslinjer og prosess dokumenteres og gjøres kjent. |
| 2.6.3 | Sentralisert, automatiserbart verktøy for kontoer, tilganger og rettigheter: a) helst ett verktøy for hele virksomheten, b) oversikt over alle kontoer, c) foreløpige utløpsdatoer for f.eks. innleide, d) detekter og følg opp kontoer som ikke er brukt på lenge (overvåk unntak som leverandørs vedlikeholdskonto), e) sentral kontroll av passordkvalitet – minimum hindre vanlige ord og navn på norsk og engelsk, årstall og årstider. |
| 2.6.4 | Minimer rettigheter for sluttbrukere og spesialbrukere: a) ikke admin-rettigheter til sluttbrukere, b) spesialbrukere (utviklere) med reelt behov får to kontoer – én for kontorbruk (e-post, nett) og én for forhøyede rettigheter, med tilstrekkelig skille og som minimum ulikt passord. |
| 2.6.5 | Minimer rettigheter på driftskontoer: a) ulike kontoer for ulike driftsoperasjoner (backup, brukeradministrasjon, klientdrift, serverdrift), b) domene-admin kun til et minimum av operasjoner og **aldri interaktivt** på klienter/servere («pass the hash»), c) unngå upersonlige kontoer («backup_arne» er bedre enn «backup»); hvis uunngåelig, logg først inn med personlig bruker. |
| 2.6.6 | Styr tilganger til enheter: a) identifiser enheter sikkert og unikt (f.eks. sertifikater), særlig ansattes klienter, b) klare regler for hvilke soner, ressurser og tjenester enheter får tilgang til. |
| 2.6.7 | Bruk **multifaktorautentisering** (smartkort, sertifikater, engangspassord): a) som minimum for kontoer med tilgang til kritiske data eller systemer og for driftsbrukere; der MFA ikke støttes, sterke passord; b) biometri på klienter som brukes mye i offentlige rom – merk personvernutfordringer ved biometri (lenke til Datatilsynet). |

Lenker: NSMs råd om passord, UK GOV Password Guidance, CIS Control 6.

#### 2.7 Beskytt data i ro og i transitt (s. 31)

**Mål:** Data beskyttes på ulike lagringsmedier og når de formidles over ulike kanaler.

**Hvorfor:** «Kryptering er en forutsetning for beskyttelse av IKT-systemer.» Uten kryptering kan uvedkommende lese eller manipulere data; samme risiko ved sårbar implementasjon eller svakt beskyttede nøkler.

| ID | Tiltak |
|---|---|
| 2.7.1 | Etabler en strategi for kryptografi: valg av verktøy, sertifikathåndtering, sikker nøkkelgenerering, oppbevaring av nøkler/passord, sikkerhetskopiering og fornyelse av nøkler, håndtering av kompromitterte nøkler. Skill langtidsnøkler (særskilt beskyttet) og sesjonsnøkler. |
| 2.7.2 | Aktiver kryptering i tjenester som tilbyr det, og bruk kun anbefalte algoritmer og nøkkellengder (NSM Cryptographic Recommendations). |
| 2.7.3 | Krypter lagringsmedier med konfidensielle data som lett kan mistes/kompromitteres (f.eks. mobile klienter); definer hvordan ulike data beskyttes (enkeltfiler, partisjoner, hele disker). |
| 2.7.4 | Bruk kryptering ved overføring av konfidensiell informasjon eller når tilliten til kanalen er lav; bestem nivå (applikasjon/TLS, nettverk/IPsec, datalink/MACsec). |
| 2.7.5 | Definer krav til sikringsnivå for ulike typer informasjon med ulikt konfidensialitetsbehov – både lagret og overført. |

Lenker: NSM Cryptographic Recommendations, Digdirs referansekatalog for IT-standarder.

#### 2.8 Beskytt e-post og nettleser (s. 32–33)

**Mål:** Minimere angriperes mulighet til å manipulere menneskelig atferd ved bruk av e-postklienter og nettlesere.

**Hvorfor:** E-post og infiserte nettsider er vanlige inngangsporter; vedlegg og lenker er blant de vanligste distribusjonsveiene for skadevare og utnytter ofte sårbarheter i andre applikasjoner eller misvisende filtyper.

| ID | Tiltak |
|---|---|
| 2.8.1 | Verifiser at innkommende e-post er fra legitim avsender (avslør spoofing) med DMARC, DKIM, SPF og DNSSEC. |
| 2.8.2 | Aktiver STARTTLS på e-postserveren for autentisering og konfidensialitet mot andre virksomheter som har aktivert STARTTLS. |
| 2.8.3 | Bruk kun støttede e-postklienter, nettlesere og programtillegg i siste versjon; avinstaller/deaktiver nettlesere i OS som ikke lenger støttes. |
| 2.8.4 | Tillat kun virksomhetsgodkjente programtillegg (plugins); unødvendige tillegg kan utgjøre sårbarhet. |

Merk (s. 33): Dette er «viderekommende» tiltak; innfør først applikasjonsgeneriske tiltak: 2.1.2 (moderne maskin-/programvare), 2.3.1 (sikkerhetsoppdateringer), 2.3.2 (styring av klientapplikasjoner), 2.6.4.a (ikke admin til sluttbrukere) og 2.5.1 (styrt dataflyt). E-post bør sikres i flest mulig ledd (protokoller, internettilkobling, server, klient-OS/applikasjoner og mottakeren). Lenker: Norid om DNSSEC, Digdirs referansekatalog, CIS «CSC 7 – Email and Web Browser Protections».

#### 2.9 Etabler evne til gjenoppretting av data (s. 34)

**Mål:** Metode for sikkerhetskopiering og gjenoppretting av kritiske data for å hindre tap.

**Hvorfor:** Angrep (f.eks. kryptovirus) kan endre eller gjøre utilgjengelig kritiske konfigurasjoner, programvare og informasjon.

| ID | Tiltak |
|---|---|
| 2.9.1 | Plan for regelmessig sikkerhetskopiering av alle virksomhetsdata, som minimum: a) hvilke data, b) hyppighet basert på verdi, c) ansvar, d) prosedyrer ved feilet kopiering, e) oppbevaringsperiode, f) logiske og fysiske krav til sikring av kopiene, g) krav til gjenopprettingstid (se 4.1), h) godkjenningsansvarlig(e) for planen. |
| 2.9.2 | Ta sikkerhetskopi av programvare: a) sikkerhetskonfigurasjon (2.3), b) maler for virtuelle maskiner og «master-images», c) installasjonsprogramvare. |
| 2.9.3 | Test sikkerhetskopier regelmessig med gjenopprettingstest. |
| 2.9.4 | Beskytt sikkerhetskopier mot tilsiktet og utilsiktet sletting, manipulering og avlesning: a) separert fra produksjonsmiljøet, b) tilgang kun for ansatte/prosesser som skal gjenopprette, c) jevnlige **offline**-kopier som ikke kan nås via nettverket, d) krypter ved lagring og flytting (også ekstern kopiering og sky). |

Lenker: NSM sikkerhetstiltak mot digital utpressing (tiltaksgruppe 2), NCSC Backing up your data, CIS Control 3, ISO/IEC 27040.

#### 2.10 Integrer sikkerhet i prosess for endringshåndtering (s. 35–36)

**Mål:** Opprettholde etablert sikkerhetstilstand ved planlagte endringer.

**Hvorfor:** Endrede forretningsprosesser, oppgraderinger, vekst, tjenesteutsetting/hjemtaking, oppkjøp/fusjon og opprydding etter angrep påvirker sikkerhetstilstanden.

| ID | Tiltak |
|---|---|
| 2.10.1 | Integrer sikkerhet i endringsprosessen: a) vurder endringsforslag for påvirkning på etablerte tiltak (f.eks. alle tabellene i grunnprinsippene), b) krav til testing før og etter idriftsetting (2.1), c) informasjon til og involvering av berørte interessenter, d) dokumentasjon av vurderinger, anbefalinger, avgjørelser og tester. |
| 2.10.2 | Involver nødvendig IKT-sikkerhetspersonell (vurderinger, gjennomganger, testing, godkjenning/signering, varsling). |
| 2.10.3 | Gjennomfør nødvendig endring, konfigurering og testing av påvirkede sikkerhetsfunksjoner før og etter idriftsetting. |
| 2.10.4 | Integrer sikkerhet i prosessen for **hasteendringer**; fastsett minimumskrav til involvering, vurderinger, testing og dokumentasjon før og etter (jf. 2.10.1–2.10.3). |

**Utdypende (s. 36):** Endringer har etterlatt store sikkerhetshull; offentlig annonserte endringer (fusjoner, store anskaffelser) kan gjøre virksomheten til mer attraktivt mål. Sikkerhet tatt inn sent blir dyrere og mindre effektiv. Lenker: ITIL 4, ISO 10007.

---

### Kategori 3 – Oppdage

#### 3.1 Oppdag og fjern kjente sårbarheter og trusler (s. 37)

**Mål:** Oppdage og fjerne kjente sårbarheter og kjent skadelig kode.

**Hvorfor:** Selv de beste produkter har sårbarheter; skadevare beveger seg raskt via sluttbrukerutstyr, vedlegg, nettsider, sky og flyttbare medier. En «kjent» sårbarhet er typisk at a) en sikkerhetsoppdatering er publisert men ikke anvendt, b) en vanlig feilkonfigurasjon er gjort, eller c) vanlige/offentliggjorte passord er brukt. En «kjent» trussel er typisk skadevare registrert av de fleste sikkerhetsprodukter.

| ID | Tiltak |
|---|---|
| 3.1.1 | Jevnlig automatisert sårbarhetskartlegging av klienter, servere og nettverk: a) prioriter funn og verifiser at de håndteres, b) hold verktøyene oppdatert. |
| 3.1.2 | Abonner på tjenester for sårbarhetsetterretning; bruk informasjonen i kartleggingsverktøyene. |
| 3.1.3 | Automatisert, sentralisert verktøy mot kjente trusler: a) antivirus/antiskadevare, helst sentralt styrt, b) IDS/IPS-funksjonalitet på klienter og servere, c) logg hendelser fra verktøyene (3.2). |

Utdypende: forsvar mot skadevare må støtte automatisering, raske oppdateringer og integrasjon med hendelseshåndtering; NSM publiserer varsler (NCSC-varsler).

#### 3.2 Etabler sikkerhetsovervåkning (s. 38–40)

**Mål:** Overvåke IKT-systemene og samle inn relevante data for å oppdage hendelser og gi grunnlag for analyse.

**Hvorfor:** Tidlig oppdagelse, vurdering av skadeomfang, forståelse av forløp, gjenoppretting, hindre gjentakelse, etterforskning. Uten overvåkning er virksomheten «blind for detaljene».

| ID | Tiltak |
|---|---|
| 3.2.1 | Fastsett strategi og retningslinjer for sikkerhetsovervåkning: a) formål og bruksområde for innsamlede data, b) hvilke data, c) sikker oppbevaring (også i rettslige prosesser), d) kapasitetsplanlegging, e) tilgangsstyring, f) sammenstilling av logger, g) **sletting av data**, h) revisjonsintervall – minst årlig og etter større hendelser. |
| 3.2.2 | Følg lover, reguleringer og retningslinjer: a) undersøk hvilke lover som gjelder, b) ta stilling til hvor lenge data skal og kan lagres, c) **informer ansatte** om hva som samles inn, hva det brukes til og hvordan det behandles. |
| 3.2.3 | Avgjør hvilke deler som overvåkes, f.eks.: a) de mest kritiske/mest konfidensielle delene (OS, database, applikasjon), b) enheters OS, c) interne nøkkelpunkter for dataflyt, d) nøkkelpunkter mot eksterne systemer/internett, e) sikkerhetsprodukter (AVS, IDS, IPS, FW), f) system for sikkerhetskopiering og gjenoppretting. |
| 3.2.4 | Beslutt hvilke data som samles inn – som minimum: a) tilgangskontrolldata (vellykkede og mislykkede pålogginger), b) administrasjons- og sikkerhetslogger; for klienter i tillegg c) forsøk på kjøring av ukjent programvare (2.3.2) og d) forsøk på rettighetseskalering. |
| 3.2.5 | Verifiser at innsamlingen fungerer: a) logginnstillinger virker, b) tilstrekkelig lagringsplass, c) standardisert format for tredjeparts analyseverktøy. |
| 3.2.6 | Påse at innsamlede data ikke kan manipuleres: a) arkiver og signer logger digitalt jevnlig, b) tilgangsstyring og deteksjon av forsøk på manipulering/sletting, c) synkroniser alle komponenter mot én tidskilde, d) konsolider i database for analyse (3.3). |
| 3.2.7 | Gjennomgå og konfigurer innsamling og sentral loggdatabase jevnlig slik at kun relevante data samles og lagres; **fjern data som ikke lenger har operasjonell eller sikkerhetsmessig relevans.** |

**Utdypende (s. 39–40):** Kartlegg kritiske systemer for å overvåke riktige steder. Ende-til-ende-kryptering gjør endepunktdata viktigere. «Sikkerhetsrelevant data kan inneholde konfidensiell informasjon om den enkelte medarbeider og behovet for lagring og tilgang må til enhver tid veies opp mot behovet for personvern» (s. 39). Klientovervåkning blir ofte oversett. Data skal kun brukes til å ivareta sikkerheten og lagres lenge nok til å kartlegge uønsket aktivitet i etterkant; behov for etterforskning, skadevurdering og trendanalyse inngår i lagringstidsvurderingen. Lenker: NCSC logging and monitoring, ACSC Guidelines for System Monitoring.

#### 3.3 Analyser data fra sikkerhetsovervåkning (s. 41–42)

**Mål:** Oppdage skadelige aktiviteter gjennom analyse av sikkerhetsrelevante data.

**Hvorfor:** Oppdagelse avhenger ellers ofte av flaks, observante brukere eller eksterne tips. Verktøy bør bruke innsamlede data og «Indicators of Compromise» (IoC).

| ID | Tiltak |
|---|---|
| 3.3.1 | Plan for analyse: egen kompetanse eller kjøp; prioritet, frekvens og ressursbruk; verktøy og mekanismer for søk og analyse; forvaltning av fagområdet (signaturbaserte verktøy, normaltilstand, metodikk og automatisering, rekonfigurering av innhenting, maskinlæring); rapportering; hendelseshåndtering. |
| 3.3.2 | Etabler og vedlikehold kompetanse om **normaltilstanden** for å oppdage avvik, f.eks. dataflyt i strid med vedtatt dataflyt (2.5), trafikk på unormale tidspunkter, unormalt store datamengder. Normaltilstanden må forvaltes ved omstillinger, oppkjøp, nedbemanning, endret driftskonsept. |
| 3.3.3 | Verktøy for manuelle og automatiske søk og alarmering i alle innsamlede data; automatisk sammenstilling fra flere kilder (avklare falske positiver, omfang og karakter); bruk kunnskap om normaltilstand og trusler for å forbedre søk og alarmkriterier. |
| 3.3.4 | Innhent og bearbeid trusselinformasjon fra relevante kilder (tidligere angrep, myndigheter, sektor-CERT-er, sammenlignbare virksomheter, åpne kilder). |
| 3.3.5 | Vurder fortløpende om innhentet data er tilstrekkelig relevant og detaljert. |
| 3.3.6 | Rutine for eskalering av alarmer: hvem det rapporteres til, og hvilke data som gjøres tilgjengelig for hvem ved hendelseshåndtering. |
| 3.3.7 | Bruk analyseverktøy, teknologi og algoritmer («anvendt maskinlæring») for å oppdage ukjente trusler og unormaliteter. |

Utdypende: knytt deg til relevant sektor-CERT; avanserte angripere unngår AV og signaturbasert IDS; analyseverktøy bør kalibreres kontinuerlig mot terskelverdier, normalnivå og trusselkunnskap. Lenke: NCSC CAF C1.

#### 3.4 Gjennomfør inntrengingstester (s. 43–44)

**Mål:** Teste egne forsvarsmekanismer (teknologi, prosesser og personell) ved å simulere en angripers mål og handlinger.

**Hvorfor:** Angripere utnytter svakheter som for langt tidsvindu fra sårbarhetsvarsel til installasjon, vide tilganger kombinert med svak autentisering, mangelfull sikker konfigurasjon og manglende forståelse av egne verdikjeder.

| ID | Tiltak |
|---|---|
| 3.4.1 | Planlegg tester med tydelig mål og omfang: a) identifiser viktige deler som vektlegges, b) identifiser systemer som er så kritiske at de må unntas (f.eks. sentrale industrielle kontrollsystemer). |
| 3.4.2 | Involver relevante interesseparter i forkant; tilpass informasjon (f.eks. informer ekstern driftsovervåkning, men ikke nødvendigvis brukere/driftspersonell). |
| 3.4.3 | Bruk verktøy for sårbarhetskartlegging (utgangspunkt) og angrepsverktøy (utnytte sårbarheter). |
| 3.4.4 | Gjennomfør jevnlige inntrengingstester – **minst årlig** – a) fra utsiden (internett, trådløst nær lokalene) og b) fra innsiden (simulere kompromittert klient/server eller utro tjener). |
| 3.4.5 | Test rutiner for deteksjon og beredskap – **minst annethvert år**. |
| 3.4.6 | Kommuniser resultater: a) rapportering tilpasset behov, b) dokumentasjon med ledelsesoppsummering, oversikt over funn og forslag til forbedringer. |

Utdypende: to typer tester – (1) finne og utnytte flest mulig sårbarheter innen tid/omfang, (2) teste deteksjons- og responsevne gjennom målrettet simulering. Lenker: NSM inntrengingstesting, NCSC penetration testing, CIS Control 18.

---

### Kategori 4 – Håndtere og gjenopprette

#### 4.1 Forbered virksomheten på håndtering av hendelser (s. 45–46)

**Mål:** Effektive prosesser for hendelseshåndtering slik at hendelser oppdages hurtig, kontrolleres, skaden minimeres og årsaken fjernes, inkl. gjenoppretting av integriteten.

**Hvorfor:** «Spørsmålet er ikke «om» en virksomhet blir offer for et vellykket dataangrep, men «når».» Når hendelsen inntreffer er det for sent å lage prosedyrer, rapporteringsrutiner, ledelsesansvar og kommunikasjonsstrategi.

| ID | Tiltak |
|---|---|
| 4.1.1 | Planverk for hendelseshåndtering som ivaretar virksomhetskontinuitet: a) krav til gjenoppretting av IKT-funksjoner/-tjenester/-systemer basert på konsekvensanalyse (BIA), b) rolle- og ansvarsbeskrivelser, c) opplæringskrav, d) **klassifiseringsregime** for hendelser og grenseverdier for å aktivere krisestab, e) krav til testing og øving, f) revider minst årlig og etter øvelser og større hendelser. |
| 4.1.2 | Analyse av virksomhetskritiske effekter: a) prioritering av vitale forretningsfunksjoner og krav til sikkerhetsnivå, b) avhengigheter til IKT, c) krav til gjenopprettingstid, tap av data og tjenestenivå. |
| 4.1.3 | Rolle- og ansvarsbeskrivelser for hendelseshåndtering: a) personell med sentrale oppgaver (IT-sjef, applikasjons-/plattformansvarlig), b) ledere med beslutningsansvar, c) beredskapsvakter utenom arbeidstid og i ferier, d) opplæring og øving. |
| 4.1.4 | Avtaler med relevante tredjeparter som kan yte støtte (sektorvise responsmiljøer, IT-spesialister, leverandører). |
| 4.1.5 | Kommunikasjonskanaler: a) distribuer kontaktinformasjon, b) plan for alternative kanaler, c) plan for intern og ekstern kommunikasjon. |
| 4.1.6 | Test og øv planene jevnlig: a) inkluder underleverandører, b) inkluder test av deteksjon og beredskap (3.4.5). |

**Utdypende (s. 46):** Forhåndsgodkjente handlingsmønstre (f.eks. kutte internett ved situasjon X), godkjent av forretningen, ikke bare IT. Spørsmål for angrep utenfor arbeidstid (mobilisering, oppdatert telefonliste, betalte underleverandører, nøkkelpersoner på ferie). Ved selvspredende skadevare har man ofte bare «en time eller to» før beslutning (stenge brannmurer, ta strømmen, isolere tjenester, virker responsfunksjoner og sikkerhetskopier?). Lenker: NSMs rammeverk for håndtering av hendelser, NCSC incident management, ISO/IEC 27035-1/-2.

#### 4.2 Vurder og klassifiser hendelser (s. 47)

**Mål:** Korrekt og hurtig vurdering og klassifisering slik at hendelser håndteres med riktig prioritet og ressurser.

**Hvorfor:** Lang tid fra oppdagelse til varsling/prioritering øker skadeomfang og gjenopprettingstid; feilklassifisering gir feil ressursbruk; riktige beslutningstakere må involveres; ofte behov for ekstern kompetanse.

| ID | Tiltak |
|---|---|
| 4.2.1 | Gjennomgå loggdata og samle relevante data om hendelsen for beslutningsgrunnlag (sammenstilling fra flere kilder, tester/målinger for å verifisere eller avkrefte). |
| 4.2.2 | Avgjør alvorlighetsgrad iht. planverk (4.1.1): a) mulig/bekreftet hendelse eller falsk alarm, b) klassifiser iht. regimet (4.1.1.d), c) involver relevante roller (4.1.3), d) iverksett beredskapsplan om nødvendig. |
| 4.2.3 | Informer relevante interesseparter (responsmiljøer, spesialister, leverandører, ledelsen, sluttbrukere, media) – se 4.1.3–4.1.4. |

Utdypende: vanskelig avveining mellom å stenge ned, sette inn tiltak eller observere; alle relevante ressurser bør sitte rundt bordet.

#### 4.3 Kontroller og håndter hendelser (s. 48–49)

**Mål:** Hendelser håndteres korrekt med riktige ressurser slik at spredning og konsekvenser minimeres og normaltilstand opprettholdes eller gjenopprettes.

**Hvorfor:** Behold roen, varsle riktige personer hurtig; følg prosedyrer etter klassifisering; hold situasjonsbildet oppdatert; logg alle aktiviteter og avgjørelser; hold berørte oppdatert.

| ID | Tiltak |
|---|---|
| 4.3.1 | Kartlegg omfang og påvirkning på forretningsprosesser og underliggende IKT-funksjoner/-tjenester/-systemer (4.1.2). |
| 4.3.2 | Undersøk om hendelsen er under kontroll og gjennomfør reaktive tiltak; eskaler til krisehåndtering ved alvorlige konsekvenser. Eksempler: allokere personell, innkapsle og blokkere inntrenger, terminere truende aktiviteter (f.eks. stenge kompromitterte interne servere). |
| 4.3.3 | Loggfør alle aktiviteter, resultater og avgjørelser: a) tidslinje for egne og trusselaktørens aktiviteter, b) oppdater hendelsesdata og situasjonsbilde, c) sikre elektroniske bevis for skadevareanalyse og eventuelle rettslige prosesser (3.2). |
| 4.3.4 | Iverksett gjenopprettingsplan: reaktivere redundante ressurser, reinstallere maskin- og programvare, gjenopprette konfigurasjon, gjenopprette stoppede tjenester. Bygg opp bedre enn før («build back better»). |
| 4.3.5 | Koordiner og kommuniser med interne og eksterne interessenter (drift, ledelse, avdelinger, andre berørte virksomheter); ha klar mediestrategi. |
| 4.3.6 | Aktiviteter i etterkant: etterforskning av rotårsak (type skadevare, trusselaktør, angrepsvektor, verktøy, forløp), oppsummerende rapport til ledelsen, kommunikasjon med sektorvise responsmiljøer og/eller NSM NCSC. |

**Utdypende (s. 49):** Scenario 1 – omfattende spredning av selvspredende kryptovirus: «kast deg rundt og stopp angrepet!». Scenario 2 – aktør med langvarig fotfeste: «vent, observer, forstå, handle»; feil handling kan få aktøren til å gå i dvale. Tommelfingerregel: ca. 2 timer fra «noe» skjer i Europa til egen beslutning må tas.

#### 4.4 Evaluer og lær av hendelser (s. 50)

**Mål:** Lære av hendelser og forbedre tiltak, prosesser, opplæring og prosedyrer.

| ID | Tiltak |
|---|---|
| 4.4.1 | Identifiser erfaringer og læringspunkter («lessons learned») – både det som virket og det som kan forbedres. |
| 4.4.2 | Kartlegg og gjennomgå kompromitterte sikkerhetstiltak; oppdater/forny for å hindre gjentakelse; vurder om tiltakene dekker risikobildet. |
| 4.4.3 | Vurder effektiviteten av prosesser, prosedyrer, rapporteringsformater og organisatoriske strukturer for respons; gjennomgå regelmessig og etter hendelser. |
| 4.4.4 | Kommuniser og del erfaringer med relevante interessenter; bruk reelle historier i opplæring og bevisstgjøring. |

Utdypende: forbedringer deles ofte i tre: 1) oppdaterte/nye risikovurderinger, 2) organisatoriske og prosessuelle tiltak, 3) teknologiske, fysiske eller menneskelige tiltak.

## Praktiske sjekkpunkter

- Kontroller at det finnes en fastsatt risikotoleranse (1.1.4) og en risikoprosess (1.1.3) før tiltak velges; dokumenter begrunnelse når et anbefalt NSM-tiltak velges bort, og vurder kompenserende tiltak (s. 5).
- Kontroller at det finnes oversikt over systemer, data, eierskap og dataflyt (1.1.5–1.1.6) – dette er også grunnlag for protokoll (art. 30) og DPIA-systembeskrivelse.
- Ved tjenesteutsetting/databehandler: kontroller de ti minimumspunktene i 2.1.10 a–j (ISMS/sertifisering, innsyn i arkitektur, hvem har innsyn og hvor data lagres, segregering, overvåkning, hendelses- og avviksrutiner, beredskap, godkjenning av underleverandører, sletting/tilbakeføring ved terminering) og ta dem inn i DPA/sikkerhetsvedlegg.
- Kontroller at produksjonsdata (personopplysninger) ikke brukes i utvikling/test uten tilsvarende sikring (2.1.6).
- Kontroller minste privilegium, sporbarhet av kontoer, jevnlig tilgangsrevisjon og deaktivering (2.6.1–2.6.3).
- Kontroller MFA for tilgang til kritiske data/systemer og driftsbrukere (2.6.7), og at sluttbrukere ikke har admin-rettigheter (2.6.4).
- Kontroller kryptering av mobile enheter/lagringsmedier og av overføringer over kanaler med lav tillit, og at det finnes kryptostrategi med nøkkelhåndtering (2.7).
- Kontroller sikkerhetskopiplan med gjenopprettingstid, gjenopprettingstester og offline-kopier (2.9) – jf. art. 32 nr. 1 bokstav c.
- Kontroller at loggstrategien omfatter formål, lagringstid, tilgangsstyring og sletting, og at ansatte informeres om loggingen (3.2.1–3.2.2, 3.2.7) – logging av ansatte er selv behandling av personopplysninger.
- Kontroller loggintegritet (signering, tidssynkronisering, manipulasjonsdeteksjon) (3.2.6).
- Kontroller årlig inntrengingstest og test av deteksjon/beredskap minst annethvert år (3.4.4–3.4.5) – jf. art. 32 nr. 1 bokstav d om regelmessig testing.
- Kontroller planverk for hendelseshåndtering med klassifiseringsregime, roller, beredskapsvakter og øvelser (4.1); koble klassifiseringen til vurdering av melding etter art. 33/34 **[Merknad – ikke fra kilden]**.
- Kontroller at hendelser loggføres med tidslinje og at bevis sikres (4.3.3) – jf. dokumentasjonsplikten i art. 33 nr. 5 **[Merknad – ikke fra kilden]**.
- Kontroller at endringer og hasteendringer har sikkerhetsvurdering (2.10) – jf. at DPIA/risikovurdering skal oppdateres ved endringer.

## Viktige sitater

- «NSMs grunnprinsipper for IKT-sikkerhet er et sett med prinsipper og tiltak for å beskytte informasjonssystemer mot uautorisert tilgang, skade eller misbruk.» (s. 3)
- «Ved å implementere de anbefalte tiltakene vil virksomheter etablere et godt forsvar mot cybertrusler, men det er ingen garanti for at de ikke blir rammet.» (s. 5)
- «En virksomhet som ikke implementerer et anbefalt sikkerhetstiltak kan ha en økt risiko som må håndteres.» (s. 5)
- «Sikkerhetstiltak er nødvendig, uavhengig av hvem som forvalter tjenestene.» (s. 9)
- «Det understrekes at virksomhetens ansvar for sikkerheten ikke forsvinner selv om man tjenesteutsetter.» (s. 18–19)
- «Sikkerhetstiltakene er riktig implementert, men er de riktige tiltakene implementert på rett sted?» (s. 12)
- «Kryptering er en forutsetning for beskyttelse av IKT-systemer.» (s. 31)
- «Sikkerhetsrelevant data kan inneholde konfidensiell informasjon om den enkelte medarbeider og behovet for lagring og tilgang må til enhver tid veies opp mot behovet for personvern.» (s. 39)
- «Spørsmålet er ikke «om» en virksomhet blir offer for et vellykket dataangrep, men «når».» (s. 45)

## Kryssreferanser

- GDPR: art. 32 (sikkerhet ved behandlingen – hele tiltakskatalogen; nr. 1 b konfidensialitet/integritet/tilgjengelighet/robusthet → 2.2.7, 2.6, 2.7; nr. 1 c gjenoppretting → 2.9, 4.3.4; nr. 1 d regelmessig testing → 2.3.5, 2.9.3, 3.4), art. 24 og 25 (organisatoriske tiltak, innebygd personvern → 2.1), art. 28 nr. 1 og 3 bokstav c, d og h (tilstrekkelige garantier fra databehandler, underdatabehandlere, revisjon → 2.1.9–2.1.10), art. 33–34 (brudd og varsling → 4.1–4.4), art. 5 nr. 1 bokstav c og e og nr. 2 (dataminimering/lagringsbegrensning for logger → 3.2.1, 3.2.7). **[Merknad – ikke fra kilden: koblingene til GDPR-artikler er utledet; NSM-dokumentet nevner ikke GDPR.]**
- Andre kilder:
  - [K16](K16-dfo-veileder-informasjonssikkerhet.md) – DFØs veileder om informasjonssikkerhet (styringssystem rundt tiltakene).
  - [K17](K17-digdir-gjennomfore-risikovurdering.md), [K18](K18-digdir-retningslinje-risiko.md), [K19](K19-digdir-risikovurderingsverktoy.md) – Digdirs risikometodikk; NSM 1.1.3–1.1.4 forutsetter slik prosess.
  - [K10](K10-dt-kryptering.md) – Datatilsynet om kryptering (utdyper 2.7).
  - [K15](K15-dt-digitale-angrep.md) – Datatilsynet om personvern ved digitale angrep (utdyper kategori 4 i personvernperspektiv).
  - [K05](K05-dt-databehandleravtale.md) – databehandleravtaler (bruk 2.1.10 som sikkerhetskrav til leverandør).
  - [K33](K33-cnil-sikkerhetsguide.md) og [K34](K34-cnil-cybersikkerhet-2024.md) – CNILs tilsvarende tiltakskatalog med personvernfokus.
  - [K37](K37-sdm-standard-datavernmodell.md) – SDM kobler tiltak til beskyttelsesmål og GDPR-krav.
  - [K30](K30-cnil-pia-kunnskapsbaser.md) – CNILs katalog over tiltak og trusler i PIA.

## Aktualitet og begrensninger

- Versjon 2.1 er datert 31. mai 2024 og er i tekstuttrekket den gjeldende versjonen; NSM omtaler dokumentet som «levende» og oppdateres ved behov (s. 3). Støtteprodukter (regneark med tiltak, mal for risikovurdering) finnes på nsm.no/gp-ikt (s. 1).
- Dokumentet er et anbefalingsdokument, ikke regelverk; sikkerhetsloven og sektorregelverk kan stille strengere krav (s. 1).
- Fysisk sikkerhet og menneskelige faktorer dekkes i liten grad (s. 5); personvernspesifikke tiltak (dataminimering, rettigheter, åpenhet) er ikke tema.
- **[Merknad – ikke fra kilden]** Dokumentet nevner verken GDPR eller personopplysningsloven. Ved bruk som art. 32-katalog må tiltakene velges ut fra risiko for *de registrertes* rettigheter og friheter (ikke bare virksomhetsrisiko), og suppleres med personvernspesifikke tiltak, f.eks. fra [K37](K37-sdm-standard-datavernmodell.md) (SDM) og [K33](K33-cnil-sikkerhetsguide.md).
- **[Merknad – ikke fra kilden]** Noen eksterne referanser kan være utdatert (f.eks. vises «ISO/IEC 27001:2017»; gjeldende utgave er ISO/IEC 27001:2022). Ved bruk i virksomheter under NIS2/ny digitalsikkerhetslov bør det kontrolleres om NSM har utgitt nyere versjon.
- Tiltaks-ID-ene er rekonstruert fra et tekstuttrekk der ID-kolonnen er forskjøvet; se merknad under «Oversikt over prinsippene».

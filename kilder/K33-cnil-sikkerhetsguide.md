---
id: K33
tittel: "Security of personal data – Practice guide (GDPR), version 2024"
utgiver: CNIL (Commission nationale de l'informatique et des libertés, Frankrike)
dato: "Mars 2024 (versjon 2024)"
spraak: en
fil: "ressurser/cnil_guide_securite_personnelle_ven_0.pdf"
type: veileder
gdpr_artikler: [5, 9, 24, 25, 28, 32, 33, 34, 35, 44]
emner: [informasjonssikkerhet, sikkerhetstiltak, tiltakskatalog, art32, passord, autentisering, tilgangsstyring, logging, sikkerhetskopiering, databehandler, sky, kryptering, risikovurdering, avvik, ki, api, mobilapper, sjekkliste]
relevans: høy
---

# Security of personal data – practice guide 2024 (CNIL, 2024)

## Sammendrag

CNILs praktiske sikkerhetsguide (versjon 2024, 63 s.) skal hjelpe virksomheter å gjennomføre sikkerhetstiltak for personopplysninger etter GDPR art. 32. Målgruppen er særlig personvernombud (DPO), informasjonssikkerhetsleder (CISO) og IT-personell, men også jurister (s. 1). Guiden består av **25 faktaark (factsheets)** gruppert i fem deler – sikkerhetsstyring, brukere, IT og utstyr, kontroll over data, forberedelse på hendelser, og «Focus»-ark (risikoanalyse, kryptografi, sky, mobilapper, KI, API) – pluss en **sjekkliste** for egenvurdering (s. 60–62). Hvert ark har tre deler: **grunnleggende forholdsregler** (basic precautions), **hva man bør unngå** (what should be avoided) og **for å gå videre** (to go further). Guiden anbefaler to komplementære tilnærminger: et sikkerhetsfundament av god praksis (adresserer de vanligste risikoene) og en risikoanalyse for de registrerte for behandlingsspesifikke risikoer (s. 4). Guiden er et «levende verktøy»; CNIL publiserer endringslogg (s. 1).

## Når skal agenten bruke denne kilden

- Når konkrete **art. 32-tiltak** skal foreslås eller vurderes, særlig med personvernvinkel (passordregler med entropikrav, loggingsinnhold og lagringstid, kryptoalgoritmer, BYOD, fjernvedlikehold).
- Ved utforming eller gjennomgang av **databehandleravtaler** og sikkerhetskrav til leverandører (ark 14, 15, 22).
- Ved **DPIA/risikovurdering**: forenklet tre-trinns risikoanalyse med tre fryktede hendelser (ark 20).
- Ved spørsmål om **logging** (hva logges, 6–12 måneders lagring, forbud mot formålsglidning), **sikkerhetskopiering** (3-2-1), **avvikshåndtering** (72 timer).
- Ved sikkerhetskrav til **sky, mobilapper, KI-systemer og API-er**.
- Som **egenvurderingssjekkliste** (s. 60–62).

## Hovedinnhold

### Forord (s. 4)

Sikkerhet er bindende for behandlingsansvarlig og databehandler via GDPR art. 32; fransk personvernlov art. 121 krever «useful precautions, having regard to the nature of the data and the risks presented by the processing». To tilnærminger: (1) sikkerhetsfundament basert på god praksis/hygiene (regelverk, standarder, guider) mot de vanligste risikoene, (2) risikoanalyse for de berørte personene (særlig nødvendig når DPIA kreves). «Additional measures» kan over tid bli grunnleggende forholdsregler (fotnote 4).

---

### Ark 1 – Managing data security / Styring av datasikkerhet (s. 5–7)

*Mål: Implementere og opprettholde personvernet som GDPR og sektorregler krever; integrere det i beslutningsprosesser.*

**Grunnleggende forholdsregler:**
- Involver ledelsen; formaliser overordnede mål for sikkerhet og personvern, godkjent av ledelsen.
- Identifiser (via protokollen/registeret) behandlinger, data og støttemedier: maskinvare, programvare, skyressurser (SaaS/PaaS/IaaS), logiske/fysiske kommunikasjonskanaler (kablet, Wi-Fi, internett, muntlig, kurer), papirdokumenter, fysiske lokaler. Formaliser sammenkoblings- og dataflytdiagrammer; oppdater ved strukturelle endringer.
- Lag en handlingsplan for IT-sikkerhet: grunnleggende forholdsregler fra guiden + spesifikke tiltak fra risikoanalyse (ark 20). Nye tiltak inn i planen; fremdrift følges opp jevnlig.
- Kontroller periodisk at tiltakene virker (f.eks. indikatorer); prioriter tiltak mot identifiserte sårbarheter eller tidligere hendelser.
- **Ledelsens gjennomgang minst én gang i året**, som tar hensyn til: endret kontekst og interessenters forventninger (kunder, partnere, tilsyn), endrede mål, utvikling i cybertrusler, nye sikkerhetsteknologier, utvikling i systemer og behandlinger, endrede personvernrisikoer, fremdrift i juridisk handlingsplan (f.eks. kontrakter) og teknisk handlingsplan, hendelser og brudd med konsekvenser for virksomhet og registrerte, henvendelser og klager om personopplysninger.
- Forbedre beskyttelsen over tid; ledelsens gjennomgang skal avgjøre ressurser og budsjett.

**Unngå:** sikkerhet som ettertanke etter at behandlingen er i drift; avanserte tiltak uten grunnleggende på plass; enkeltstående tiltak uten helhetssyn (innsamling, partnere, livsløpsslutt); kun tekniske tiltak uten organisatoriske; handlingsplan uten frist og ansvarlig per tiltak; å delegere all IT-sikkerhet til en leverandør.

**Videre:** Utnevn CISO og personvernombud (DPO) – kvalifisert til å rapportere til øverste ledelse, med ressurser, og involvert tidlig og systematisk (innebygd personvern). Generell personvernpolicy godkjent av ledelsen, utdypet i tematiske policyer og prosedyrer. Periodiske sikkerhetsrevisjoner med handlingsplan fulgt opp på høyeste nivå. Styringssystem med kontinuerlig forbedring: ISO/IEC 27701 (PIMS) basert på ISO/IEC 27001 (ISMS). ANSSIs «Guide for a healthy information system in 42 measures».

### Del: Brukere

### Ark 2 – Defining a framework for users / Rammeverk for brukere (s. 9–10)

*Mål: Gi bindende kraft til hovedreglene for bruk av IT-verktøy.*

**Grunnleggende:**
- Utarbeid et **IT-reglement (IT charter)** med bindende kraft (f.eks. vedlegg til arbeidsreglementet).
- Reglementet skal minst inneholde:
  1. Påminnelse om personvernregler og sanksjoner ved brudd.
  2. Virkeområde, herunder: hvordan IT-teamene intervenerer; autentiseringsmetoder og passordpolicy; sikkerhetsregler – melde mistenkt brudd/forsøk på kontoen, tap/tyveri av utstyr og feil; aldri gi passord til tredjepart; aldri installere/kopiere/endre/slette/konfigurere programvare uten tillatelse; låse/slå av maskinen når man forlater den; ikke aksessere/forsøke/slette informasjon utenfor eget ansvar; følge prosedyrer for kopiering til flyttbare medier (forhåndsgodkjenning fra overordnet).
  3. Prosedyrer for bruk av arbeidsstasjoner, mobilt utstyr (hjemmekontor), individuelle lagringsområder, lokalnett, private enheter (vilkår), internett, e-post, telefoni.
  4. Vilkår for administrasjon av IT-systemet og eventuell automatisk filtrering, automatisk logging og administrasjonssystemer for arbeidsstasjoner.
  5. Ansvar og sanksjoner ved brudd på reglementet.

**Unngå:** reglement uten bindende kraft eller uten håndheving; å ignorere brukernes reelle praksis og behov («shadow IT sometimes reveals essential needs»); manglende brukerstøtte.

**Videre:** Taushets-/konfidensialitetserklæring eller klausul i arbeidskontrakt; eget reglement for administratorer. Guiden har en **eksempelklausul for konfidensialitetserklæring** (s. 10): den ansatte erkjenner konfidensialiteten, forplikter seg iht. art. 32 til å: ikke bruke data til andre formål enn fullmaktene tilsier; kun utlevere til autoriserte; ikke ta kopier utover det nødvendige; hindre misbruk; ivareta fysisk og logisk sikkerhet; bruke sikre kommunikasjonsmidler; levere tilbake alle data og medier ved fratreden. Gjelder under og etter ansettelsen; brudd kan gi disiplinære og strafferettslige sanksjoner (fransk straffelov art. 226-13, 226-16 til 226-24).

### Ark 3 – Involving and training users / Involvere og lære opp brukere (s. 11–12)

*Mål: Gjøre hver bruker bevisst personvern- og sikkerhetsutfordringer. Menneskelige feil og sosial manipulering står bak mange hendelser.*

**Grunnleggende:** Bevisstgjør interne og eksterne brukere om personvernrisiko, tiltak og konsekvenser av brudd (sesjoner om phishing, løsepengevirus, identitetstyveri, årvåkenhet, hva gjøre ved hendelse; jevnlige påminnelser knyttet til aktuelle hendelser). Tilpass kampanjer til roller (HR, mobile arbeidstakere). Sikre at saksbehandlere har tilegnet seg god praksis (f.eks. kunnskapstest). Lær opp IT-personell i sikkerhet og personvern. Dokumenter driftsprosedyrer i klart språk tilpasset hver kategori, hold dem oppdatert og tilgjengelige.

**Unngå:** innføre verktøy uten å følge opp brukerne; ikke kreve personvernopplæring for nyansatte der kjernevirksomheten er behandling av personopplysninger (helse, kundeservice); undervurdere effekten av informerte ansatte; glemme bevisstgjøring av eksterne leverandører (direkte eller via kontrakt).

**Videre:** Informasjonsklassifisering (f.eks. offentlig, intern, konfidensiell) med merking; synlig merking på hver side med sensitive data (art. 9); øvelser og simuleringer av sikkerhetshendelser/kriser.

### Ark 4 – Authenticating users / Autentisering av brukere (s. 13–15)

*Mål: Gjenkjenne brukere slik at de får nødvendig tilgang.*

**Faktorer:** kunnskap (passord), besittelse (smartkort), iboende (fingeravtrykk, tastetrykkdynamikk). Biometri for unik identifisering er særlige kategorier (art. 9). **Multifaktor** = minst to faktorer av ulike kategorier. **Sterk** = basert på kryptografisk mekanisme med robuste parametere (s. 13).

**Grunnleggende:**
- Unik identifikator per bruker; forby delte kontoer. Hvis generiske/delte kontoer er uunngåelig: godkjenning fra ledelse, logging av handlinger, og nytt passord så snart en person ikke lenger trenger tilgang.
- Følg CNILs passordanbefaling:
  - lagre kun passord-fingeravtrykk (hash) med moderne teknikker;
  - **ikke krev periodisk passordbytte for vanlige brukere** (i motsetning til administratorer);
  - krev bytte av tildelt passord ved første innlogging;
  - kompleksitet etter brukstilfelle:

| Scenario | Minimum entropi | Eksempler |
|---|---|---|
| Standard (passord alene) | 80 bit | Min. 12 tegn med store/små bokstaver, tall og spesialtegn; eller min. 14 tegn med store/små bokstaver og tall |
| Med tilleggstiltak (forsinkelse etter feil, Captcha, sperring etter 10 feil) | 50 bit | Min. 8 tegn av 3 typer; eller 16 sifre |
| Utstyr i brukerens besittelse (SIM-kort, enhet med sertifikat) med sperring etter 3 feil | 13 bit | 4 sifre |

- Hjelp brukere: huskeregler (mnemotekniske metoder), **passordhåndterere** (med sterkt hovedpassord, nøye valg av løsning).
- Kommuniser forbudt praksis (dele passord, kontekst-utledbare passord, lagre passord i nettleser uten hovedpassord).

**Unngå:** standardpassord; passord i klartekst; utdaterte hashfunksjoner (MD5, SHA-1) eller hjemmelagde; å blokkere «lim inn»/autoutfylling (hindrer passordhåndterere).

**Videre:** Multifaktor der mulig, særlig ved tilgang utenfra; begrens antall forsøk og sperr kontoen; høyere entropi og fornuftig fornyelse for administratorer; teknisk håndheving (f.eks. sperre admin-konto ved manglende bytte); CNILs verktøy for å beregne passordkompleksitet; unngå at brukernavn er like standardkontoer, deaktiver standardkontoer; lagre passord med dedikert hashfunksjon og alltid **salt eller nøkkel** – nøkkelen skal ikke lagres i samme database som fingeravtrykkene; ANSSI/CNILs anbefalinger om MFA og passord; for forvaltningen gjelder RGS (vedlegg B1 og B2).

### Ark 5 – Access management / Tilgangsstyring (s. 16)

*Mål: Kun tilgang til data brukeren faktisk trenger (minste privilegium).*

**Grunnleggende:** Definer autorisasjonsprofiler med oppgave- og ansvarsdeling; alle tilgangsforespørsler godkjennes av leder; trekk tilbake rettigheter straks de ikke lenger er nødvendige (rolleendring, kontraktslutt); **gjennomgang av rettigheter minst årlig** med fagansvarlige for å slette ubrukte kontoer og justere rettigheter.

**Unngå:** delte kontoer uten sporing, godkjenning og gjennomgang; admin-rettigheter til brukere som ikke trenger det; flere privilegier enn nødvendig; glemme midlertidige tilganger (vikariater); glemme å slette kontoer for de som har sluttet/byttet rolle.

**Videre:** Dokumentert og jevnlig revidert tilgangskontrollpolicy med automatiske prosedyrer ved ankomst/avgang/rolleendring, konsekvenser ved misbruk av legitim tilgang, og tiltak for å begrense og kontrollere tildeling og bruk (jf. ark 16).

### Del: IT og utstyr

### Ark 6 – Securing workstations / Sikre arbeidsstasjoner (s. 18–19)

*Mål: Hindre uautorisert tilgang, skadevare og fjernstyring.*

**Grunnleggende:** automatisk skjermlås etter inaktivitet; programvarebrannmur med kun nødvendige porter; jevnlig oppdatert antivirus; sikkerhetsoppdateringer så snart som mulig etter testing – **oppdateringer for offentlig kjente kritiske sårbarheter installeres uten opphold**; minimale brukerrettigheter; lagre data på sikkerhetskopiert nettverkslagring fremfor lokalt (ev. synkronisering/backup og opplæring); sikker sletting før omfordeling; flyttbare medier – bevisstgjøring, begrens tilkobling, deaktiver «autorun»; fjernhjelp – brukerens samtykke før inngrep, og brukeren skal kunne se om fjernstyring pågår eller er avsluttet.

**Unngå:** operativsystemer uten leverandørstøtte; administratorrettigheter (lokalt/nettverk) til brukere som ikke trenger dem.

**Videre:** godkjentlisting av applikasjoner fra trygge kilder; begrens applikasjoner som krever admin; sikkert (virtualisert) miljø for risikable operasjoner; løsning for analyse/rensing av flyttbare medier («sas et station blanche»); ved kompromittering – let etter kilde og spor i resten av systemet; følg CERT-FR-varsler; ukentlig automatisk sjekk av kritiske OS-oppdateringer; funksjonell oppdateringspolicy; tyverisikring (kabel); alle brukere skal vite hva de skal gjøre og hvem de skal kontakte ved hendelser; CERT-FRs «gode reflekser ved inntrenging».

### Ark 7 – Securing mobile computing / Mobil databehandling (s. 20–21)

*Mål: Forebygge brudd utenfor lokalene, inkl. tyveri/tap.*

**Grunnleggende:** bevisstgjøring om risiko (tyveri, ukontrollerte nett, offentlig utstyr, privat utstyr); tilgangskontroll med egnet autentisering (sertifikat, smartkort) og **kryptering av alle informasjonsflyter (f.eks. VPN)**; fjerntilgjengelig delt lagring; **kryptering av mobile/flyttbare lagringsmedier** (full diskkryptering, fil-for-fil, krypterte containere); smarttelefoner – i tillegg til SIM-PIN: automatisk låsing og hemmelighet for opplåsing; kontaktinformasjon ved tap/tyveri; **BYOD** – vurder og håndter risiko, tillat kun ut fra identifiserte risikoer, begrens tilgang etter kritikalitet, regulert i IT-reglementet.

**Unngå:** forhåndsinstallerte skytjenester for backup/synk uten analyse av vilkår og sikkerhet (oppfyller normalt ikke ark 14); MDM-tiltak på privat telefon som hindrer privat bruk; å krenke brukerens privatliv ved å aksessere data i den personlige delen av BYOD-enheten.

**Videre:** CNILs faktaark om BYOD; MDM (også på BYOD om tillatt); personvernfilter på skjerm; ikke etterlate utstyr/dokumenter, ikke diskutere sensitive opplysninger offentlig; begrens lokal lagring (ev. forby ved utenlandsreiser); tyverisikring og skadebegrensning (lås, kryptering, fjernsletting – fjernsletting på BYOD må reguleres i IT-reglementet); partisjoner jobbdel av privat utstyr.

### Ark 8 – Protecting the computer network / Beskytte nettverket (s. 22–23)

**Grunnleggende:** blokker unødvendige internettjenester (VoIP, peer-to-peer); Wi-Fi med moderne kryptering (**WPA3 eller WPA2** iht. ANSSI), gjestenett adskilt fra internt nett; **VPN for fjerntilgang**, helst med sterk autentisering (smartkort, TOTP); **ingen administrasjonsgrensesnitt direkte på internett** – administrasjon og vedlikehold via VPN; nettverksadministrasjon via korrekt konfigurert SSH eller fysisk tilgang; begrens flyter til det strengt nødvendige (filtrering i brannmur/proxy – f.eks. kun port 443 for ren HTTPS-server); **segmentering: minst to soner** – internt nett uten internettforbindelse og DMZ tilgjengelig fra internett, adskilt med gatewayer.

**Unngå:** Telnet til nettverksutstyr; ufiltrert internettilgang for brukere; Wi-Fi med WEP.

**Videre:** administrasjon fra utstyr under eksklusiv kontroll av behandlingsansvarlig eller dennes underleverandører; maskinvareautentisering (802.1X) eller minst godkjentliste av MAC-adresser; IDS/IPS – informer brukerne i IT-reglementet etter konsultasjon med ansattrepresentanter; ANSSI-anbefalinger om internettilkobling, brannmurvalg og 802.1X (med referansediagram, s. 23).

### Ark 9 – Securing servers / Sikre servere (s. 24–25)

**Grunnleggende:** avinstaller/deaktiver unødvendige tjenester og grensesnitt; admin-verktøy kun for autorisert personell, og uprivilegerte kontoer til rutineoppgaver; egen passordpolicy for administratorer – bytt minst når en administrator slutter og ved mistanke om kompromittering; kritiske oppdateringer uten opphold (etter testing) med **ukentlig automatisk sjekk**; antiskadevare; navngitte kontoer for databasetilgang og applikasjonsspesifikke tekniske kontoer; sikkerhetskopier med jevnlig integritets- og gjenopprettingskontroll (ark 17); **TLS (ikke SSL)** eller tilsvarende protokoll minst for all utveksling over internett, verifisert med verktøy (f.eks. SSL Labs); ikke utdaterte krypteringsalgoritmer; loggsystem (ark 16).

**Unngå:** behandle personopplysninger på utdaterte servere uten å erstatte dem; usikre protokoller (ukryptert autentisering, klartekst); bruke servere til surfing/e-post; **databaser på server direkte tilgjengelig fra internett**; generiske (delte) kontoer.

**Videre:** systemer med sensitive data (art. 9) i dedikert, logisk isolert miljø; administrasjon via dedikert, isolert nett med sterk autentisering; krypter også interne flyter (TLS, IPsec, SSH); isoler utdaterte men nødvendige servere og begrens personopplysninger der; sårbarhetsskanning (nmap, Nessus, Nikto) eller revisjon for de mest kritiske; IDS/IPS; begrens fysisk og forby logisk fjerntilgang til diagnose-/konfigurasjonsporter; **TLS 1.3, minst 1.2** (ANSSI); ANSSI om sikker administrasjon og systempartisjonering.

### Ark 10 – Securing websites / Sikre nettsteder (s. 26–27)

**Grunnleggende:** TLS – sertifikater på riktig nivå (domene, organisasjon, utvidet) fra sertifiseringsinstans, kun nyeste versjoner, **obligatorisk TLS på alle autentiseringssider og sider der personopplysninger vises eller overføres**; kun nødvendige porter (f.eks. 443); admin-verktøy kun for autorisert personell/interne IT-team; **«HttpOnly» og «secure» på alle informasjonskapsler**; samtykke før ikke-nødvendige informasjonskapsler lagres; begrens, overvåk og oppdater komponenter; **begrens informasjon ved kontoopprettelse/tilbakestilling** så angriper ikke kan avgjøre om en konto finnes; god utviklingspraksis (ark 11), beskytt mot OWASP Top 10 (SQL-injeksjon, XSS, URL-manipulering).

**Unngå:** personopplysninger i URL (brukernavn, passord); usikre tjenester; webservere som arbeidsstasjoner; databaser direkte tilgjengelig fra internett; generiske kontoer.

**Videre:** CNILs dossier om informasjonskapsler; OWASP-nivå L1 og L2; sårbarhetsverktøy (OWASP ZAP, nmap, nikto) – regelmessig og før hver ny versjon i produksjon; ANSSI om TLS og nettstedssikkerhet.

### Ark 11 – Managing IT developments / IT-utvikling (s. 28–29)

*Mål: Integrere sikkerhet og personvern så tidlig som mulig (innebygd personvern og personvern som standard).*

**Grunnleggende:** personvern og sikkerhetskrav fra design (arkitekturvalg – desentralisert/sentralisert; funksjoner – anonymisering kort etter innsamling, dataminimering; teknologi – kryptering); anerkjente og sikre komponenter/biblioteker; tiltak mot vanlige databaseangrep (SQL-injeksjon, skript); for tjenester rettet mot allmennheten – særlig vurdering av personvernparametere og **standardinnstillinger**; unngå fritekstfelt (kilde til unødvendig innsamling); omfattende tester (enhet, integrasjon, funksjon, sikkerhet) før lansering/oppdatering; **utvikling og test i miljø adskilt fra produksjon, med fiktive eller anonymiserte data**; ingen hemmeligheter (autentisering/kryptering) i versjonskontroll (Git/svn) – bytt hemmeligheter ved produksjonssetting; regresjonstest og/eller kodegjennomgang før produksjon.

**Unngå:** ekte personopplysninger i utvikling og test; tenke sikkerhet etter at applikasjonen er utviklet.

**Videre:** CNILs GDPR-guide for utviklingsteam; forsvar i dybden (frontend-tiltak må forsterkes i backend); inndataformater som minimerer (f.eks. kun fødselsår via nedtrekksmeny); kodekonvensjoner og dokumentasjon; dataformater kompatible med lagringstid (åpne formater ved lang lagring); brukerprofiler med differensierte tilganger fra design; **pre-produksjon med ekte data** tillatt når fiktive data ikke er nok – men sikret på produksjonsnivå og etter alle tester; kodesignering for integritet.

### Ark 12 – Protecting the premises / Beskytte lokaler (s. 30–31)

**Grunnleggende:** låste dører; innbruddsalarm med periodisk test; røykvarslere og brannslukking, årlig inspeksjon; beskytt nøkler og alarmkoder; soner etter risiko (egen adgangskontroll til serverrom); oppdatert liste over autoriserte per sone, periodisk gjennomgått; regler for besøkende – minst følge dem utenfor publikumsområder (fra ankomst til de forlater); beskytt nettverksuttak og tillat kun autorisert utstyr; fysisk beskyttelse av IT-utstyr (dedikert brannslukking, heving mot flom, redundant strøm og kjøling).

**Unngå:** underdimensjonert/forsømt vedlikehold av serverrommiljø (kjøling, UPS) – feil fører ofte til at dører åpnes for luftsirkulasjon; synlige/tilgjengelige konfidensielle data (skjermer lesbare for besøkende, dokumenter i resepsjonen).

**Videre:** logg adgang til rom med utstyr som behandler data der en hendelse kan få alvorlige konsekvenser for registrerte (informer brukerne etter konsultasjon med ansattrepresentanter); synlig identifikasjon (kort) i regulerte soner; begrenset tilgang for besøkende med registrering av tid inn/ut; jevnlig gjennomgang av adgangsrettigheter.

### Del: Kontroll over data

### Ark 13 – Securing exchanges with the outside world / Sikker utveksling (s. 33–34)

*Forbrukerkanaler (e-post, chat, fildeling) er sjelden sikre uten tilleggstiltak; servere data passerer kan gi tilgang til innhold eller metadata.*

**Grunnleggende:** krypter data før de lagres på fysisk medium til tredjepart (USB, disk, optisk); ved nettverksoverføring – krypter sensitive deler (ark 21), bruk protokoll med konfidensialitet og autentisering av mottakerserver (SFTP, HTTPS) i nyeste versjoner, **send hemmeligheter (nøkkel/passord) via separat kanal** (f.eks. fil på e-post, passord via telefon/SMS); åpne eksterne filer kun fra kjent avsender og etter antivirusskanning; faks – kontrollert rom, vis mottakers identitet, send også originaldokumenter, forhåndsregistrer mottakernumre.

**Unngå:** ukrypterte filer med personopplysninger via meldingstjenester/forbrukerplattformer; manglende (helst automatisk) sletting av filer på filoverføringsplattformer.

**Videre:** offentlig nøkkel-infrastruktur (PKI) mellom aktører; elektronisk signatur fra avsender; midlertidig fildelingsserver med begrenset tilgjengelighetstid, tilgang kun for autoriserte, og kryptering før opplasting om løsningen ikke gjør det; verktøy som også beskytter metadata; for de mest sensitive systemene – isolerte soner for eksterne filer.

### Ark 14 – Managing data processors / Styring av databehandlere (s. 35–36)

*Behandling hos databehandler skal ha tilstrekkelige garantier, særlig for sikkerhet; behandlingsansvarlig må kjenne detaljene for å kunne påvise etterlevelse (art. 5 nr. 2, 24 nr. 1).*

**Grunnleggende:**
- Bruk kun databehandlere med tilstrekkelige garantier (fagkunnskap, pålitelighet, ressurser).
- Kontrakt som fastsetter gjenstand, varighet, formål og partenes plikter, særlig sikkerhet, med bestemmelser om:
  - fordeling av ansvar og plikter knyttet til konfidensialitet;
  - minimumskrav til brukerautentisering;
  - vilkår for **tilbakelevering og destruksjon** av data ved avtaleslutt;
  - regler for håndtering og varsling av hendelser – behandlingsansvarlig informeres ved oppdaget sikkerhetsbrudd/hendelse, **så snart som mulig** ved brudd på personopplysningssikkerheten;
  - bistand for å sikre etterlevelse av sikkerhetsplikter (art. 32; EDPB Guidelines 07/2020 avsn. 41);
  - jevnlig gjennomgang av sikkerhetstiltak og vilkår for revisjon av dem.
- Midler til å verifisere garantiene (sikkerhetsrevisjoner, stedlige besøk), f.eks.: kryptering etter sensitivitet eller prosedyrer som sikrer at leverandøren ikke har tilgang når det ikke er nødvendig; kryptert overføring (HTTPS, VPN); garantier for nettverksbeskyttelse, sporbarhet, autorisasjonsstyring, autentisering, administratorpraksis, revisjoner.

**Unngå:** starte behandling uten signert kontrakt med art. 28-kravene; skytjenester uten garanti for faktisk geografisk plassering og uten å sikre lovlige vilkår for overføring ut av EU.

**Videre:** CNILs guide for databehandlere; art. 28; nøye valg av skyleverandør (ark 22); **hele underleverandørkjeden** (underdatabehandlere) skal vurderes; sertifisering (ISO/IEC 27001, 27701) som første indikator; helsedata krever HDS-sertifisert vertsleverandør (Frankrike); krev sertifikater og kontroller omfanget (scope). Kommisjonens standardavtaleklausuler mellom behandlingsansvarlig og databehandler kan brukes (fotnote 61).

### Ark 15 – Supervising maintenance and end-of-life / Vedlikehold og utfasing (s. 37–38)

**Grunnleggende:** loggbok over vedlikeholdsinngrep; fjernvedlikeholdstilgang åpnes kun på leverandørens forespørsel, for forhåndsdefinert periode, og lukkes etterpå; sikkerhetsklausuler i vedlikeholdskontrakter; tredjepartsinngrep overvåkes av en leder i virksomheten; ikke la eksterne være alene (særlig serverrom); **sikker sletting før kassering, reparasjon hos tredjepart eller slutt på leieavtale**.

**Unngå:** fjernvedlikeholdsprogrammer med kjente sårbarheter (f.eks. ukryptert); gjenbruk/salg/kassering av medier uten sikker sletting; full eller permanent fjernvedlikeholdstilgang.

**Videre:** skriftlig prosedyre for sikker sletting; kvalifisert/sertifisert slette-programvare (ANSSI CSPN); sanntids- eller etterfølgende overvåkning (opptak, «4-eye»-sesjoner) av fjernvedlikehold – med lovlig grunnlag og informasjon til de berørte; ANSSIs kapittel om tredjepartsvedlikehold.

**Eksempelklausul for tredjepartsvedlikehold (s. 38):** hvert inngrep beskrives (dato, art, navn på deltakere) og sendes X; ved fjernvedlikehold kan Y kun intervenere etter at X har autorisert tilgangen (alternativt: etter at X er informert og kan identifisere og overvåke tilgangen); tilgang lukkes etter hvert inngrep; begge parter fører register med dato, detaljert art og navn. Må kombineres med en konfidensialitetsklausul for databehandlere.

### Del: Forberedelse på hendelser

### Ark 16 – Logging operations / Logging (s. 40–41)

*Formål: oppdage avvik, feil eller hendelser, ha informasjon til håndtering eller tvister; loggene er også bevis for etterlevelse (art. 5 nr. 2, 24 nr. 1).*

**Grunnleggende:**
- Loggsystem for brukeres forretningsaktivitet (applikasjonslogger), tekniske inngrep (inkl. administratorer), avvik og sikkerhetshendelser (tekniske/systemlogger).
- **Lagringstid: rullerende periode på mellom seks måneder og ett år** (unntak: rettslig plikt, tvisthåndtering, internkontroll eller identifisert behov for etterhendelsesanalyse).
- Applikasjonslogger: registrer opprettelse, oppslag, deling, endring og sletting – med forfatterens identifikator, dato, tid, type operasjon og referanse til dataene (for å unngå duplisering).
- Informer brukerne (f.eks. ved innlogging) om loggingen, etter informasjon og konsultasjon med ansattes representanter.
- Beskytt loggutstyr og logger mot uautoriserte operasjoner (utilgjengelig for de som logges), misbruk fra autoriserte kontoer (bruksreglement, varsler) og overskriving.
- Overvåk at loggsystemet fungerer og kontroller jevnlig at logger finnes.
- Databehandlere skal kontraktsmessig forpliktes til logging iht. dette og til å varsle behandlingsansvarlig så snart som mulig om avvik/hendelser.
- Analyser loggene aktivt, i sanntid eller på kort sikt, for å oppdage hendelser (ark 19).

**Unngå:** duplisering og overdreven lagring av personopplysninger i logger (f.eks. lagre passord eller hash ved autentisering); **bruke logger til andre formål enn å sikre riktig bruk av systemet** (f.eks. telle arbeidstimer – «a misuse of purpose, punishable by law»); logger uten tidsbegrensning.

**Videre:** CNILs anbefaling om loggingstiltak; involver brukeren (vis f.eks. de tre siste innloggingene); automatisk overvåkning med varsler; sentral loggenklave mot endring; ANSSI om loggarkitektur og Active Directory.

### Ark 17 – Saving / Sikkerhetskopiering (s. 42)

**Grunnleggende:** hyppige sikkerhetskopier (papir og elektronisk) – f.eks. daglige inkrementelle og jevnlige fulle; **minst én kopi på geografisk adskilt sted**; **minst én offline-kopi** frakoblet nettverket; samme sikkerhetsnivå på kopier som i drift (kryptering, sikkert lagringssted, kontraktsregulert ekstern tjeneste); krypter overføringskanalen når den ikke er intern; test jevnlig integritet og gjenopprettingsevne.

**Unngå:** lavere sikkerhet på backupsystemet; kopier på samme system uten isolering (løsepengevirus kan ramme begge); kopier på samme sted som maskinene; aldri teste.

**Videre:** brann- og vanntett safe for minst én kopi; replikering til sekundært anlegg ved høye tilgjengelighetskrav; **«3-2-1»-regelen: 3 kopier, på 2 ulike medier, hvorav 1 offline**; ANSSI om sikkerhetskopiering.

### Ark 18 – Business continuity and resumption / Kontinuitet og gjenoppretting (s. 43)

**Grunnleggende:** kontinuitetsplan (BCP) og katastrofegjenopprettingsplan (DRP), også summariske, med liste over interessenter – **personvernnivået skal ikke reduseres i nødmodus**; brukere, leverandører og underleverandører vet hvem de skal varsle; test jevnlig gjenoppretting og planene; avbruddsfri strøm (inverter) for vesentlig utstyr; redundant lagring (RAID).

**Unngå:** å tro man er trygg; senke sikkerheten i degradert drift uten å vurdere nye risikoer; ikke planlegge retur til normal drift; ikke teste.

**Videre:** SGDSNs guide til kontinuitetsplan; krisehåndteringsorganisasjon; øvelser med alle interessenter; målrettede tester av komponenter, men test innimellom de mest kritiske elementene og vurder test av full nedstengning.

### Ark 19 – Managing incidents and violations / Hendelser og brudd (s. 44–45)

**Grunnleggende:** analyser loggene jevnlig; loggforvaltere (interne/eksterne) varsler behandlingsansvarlig så snart som mulig; spre til alle brukere hva de skal gjøre og hvem de skal kontakte, og viktigheten av å melde mistenkelige hendelser; prosedyrer for alarmgenerering fra ulike kilder (automatisk, brukere), behandling og tiltak ved bekreftet hendelse; **inkluder brudd på personopplysningssikkerheten i hendelsesprosessen og definer kriterier for å klassifisere en hendelse som slikt brudd**; vurder risikoen for personer (alvorlighet og sannsynlighet for konsekvenser for rettigheter og friheter); **intern oversikt over alle brudd**; **meld til tilsynsmyndigheten (CNIL) innen 72 timer** ved risiko, og **informer de registrerte ved høy risiko** (med unntak i GDPR) slik at de kan begrense konsekvensene.

**Unngå:** vente på at registrerte/tredjeparter oppdager hendelsen; utelate risikovurdering for de registrerte; **vente på presis informasjon før melding når det er klart at et brudd har skjedd** – meldingen kan sendes i to trinn: innledende innen 72 timer, deretter supplerende.

**Videre:** automatisk loggovervåkning med varsler; obligatorisk opplæring av alle ansatte i å identifisere og melde brudd; EDPB Guidelines 01/2021 (18 eksempler på brudd); WP29/WP250 rev.01 om melding av brudd; cybermalveillance.gouv.fr. Merk: plikten til å melde brudd fritar ikke fra andre meldeplikter (fotnote 82).

### Del: Fokus

### Ark 20 – Risk analysis / Risikoanalyse (s. 47–49)

*Grunnlag for tilleggstiltak tilpasset konteksten for å begrense konsekvenser for de registrerte.*

**Grunnleggende:**
- Identifiser behandlinger som krever DPIA (art. 35). En DPIA har både en risikodel og en juridisk del.
- Gjennomfør en risikoanalyse, selv minimal, i **tre trinn**:
  1. **Identifiser** behandlinger, data og støttemedier (maskinvare, programvare, sky, kanaler, papir, lokaler) – bør gjøres uavhengig av risikoanalysen (jf. ark 1).
  2. **Vurder risiko** for hver behandling:
     - a) Mulige virkninger på de registrertes rettigheter og friheter for **tre fryktede hendelser**: *uautorisert tilgang* (f.eks. identitetstyveri etter lekkasje av alle lønnsslipper), *uønsket endring* (f.eks. urettmessig beskyldning etter endrede adgangslogger), *midlertidig eller permanent tap* (f.eks. uoppdaget legemiddelinteraksjon fordi pasientjournal er utilgjengelig).
     - b) **Risikokilder**: interne/eksterne menneskelige (IT-administrator, bruker, ekstern angriper, konkurrent) og ikke-menneskelige (vann, epidemi, farlige stoffer, ikke-målrettet virus).
     - c) **Trusler** mot støttemediene, som kan bli: brukt på upassende måte (rettighetsmisbruk, feil), endret (keylogger, skadevare), tapt (tyveri, mistet USB), observert (skjerm på tog, geolokalisering), skadet (hærverk, slitasje), overbelastet (full lagring, tjenestenekt).
     - d) Eksisterende eller planlagte tiltak (tilgangskontroll, backup, sporbarhet, lokalsikring, kryptering, anonymisering).
     - e) Vurder **alvorlighet** (konsekvens for registrerte) og **sannsynlighet**; eksempelskala: ubetydelig, moderat, stor, maksimal (negligible, moderate, large, maximum).
  3. **Iverksett og kontroller** tiltakene; er de ikke tilstrekkelige, identifiser tilleggstiltak som reduserer alvorlighet og/eller sannsynlighet.
- Revider risikoanalysen jevnlig og ved endringer i system eller kontekst.

**Tabellmal (s. 48):** kolonner *Fryktet hendelse | Virkninger for personer | Hovedrisikokilder | Hovedtrusler | Eksisterende/planlagte tiltak | Alvorlighet | Sannsynlighet*; rader: uautorisert tilgang, uønsket endring, tap av data.

**Unngå:** kun se på konsekvenser for virksomheten og glemme de registrerte; utelate deler av behandlingen (innsamling, partnere, livsløpsslutt); **justere skalaene underveis** i stedet for å fastsette dem på forhånd ut fra virksomhetens kontekst.

**Videre:** innholdskrav til DPIA etter art. 35 nr. 7; CNILs PIA-guider og PIA-programvare; CNILs lister over behandlinger som krever/ikke krever DPIA; periodiske sikkerhetsrevisjoner; informasjonssikkerhetsrisiko (f.eks. EBIOS RM) kan vurderes samtidig – tilnærmingene er kompatible; avsett budsjett til tiltakene.

### Ark 21 – Encryption, hash, signature / Kryptering, hash, signatur (s. 50–51)

*Hash sikrer integritet; signatur sikrer integritet, autentisitet og ikke-benekting; kryptering sikrer konfidensialitet.*

**Grunnleggende – anerkjente algoritmer:**

| Formål | Anbefalte algoritmer |
|---|---|
| Hashfunksjoner | SHA-2, SHA-3 |
| Passordlagring | bcrypt, scrypt, Argon2, PBKDF2 |
| Symmetrisk kryptering | AES med egnet modus (CCM, GCM, EAX) eller ChaCha20 (med Poly1305) |
| Asymmetrisk kryptering | RSA-OAEP, ECIES-KEM, DLIES-KEM |
| Signatur | RSA-SSA-PSS, ECDSA |

**Nøkkellengder:** AES 128, 192 eller 256 bit; RSA-baserte – modulus minst 2048 eller 3072 bit, offentlig eksponent større enn 65536 for kryptering. Følg bruksanbefalinger for algoritmen (implementasjonsfeil har stor betydning). Beskytt private nøkler (begrensede rettigheter og sikkert passord). Skriftlig prosedyre for håndtering av nøkler og sertifikater, inkl. glemte passord.

**Unngå:** DES, 3DES, MD5, SHA-1; å tro at hash alene gir konfidensialitet (raske funksjoner kan brute-forces); hashing av passord uten salt.

**Videre:** CNILs side om kryptologi; ANSSI-guider; verifiser mottatte sertifikater (bruksindikasjon, gyldighet, ikke tilbakekalt, korrekt tillitskjede); tredjepartsverifiserte biblioteker; løsninger: ANSSI-sertifiserte/-kvalifiserte, VeraCrypt (krypterte containere), GnuPG; RGS vedlegg B1/B2 for forvaltningen.

### Ark 22 – Cloud computing / Skytjenester (s. 52–53)

*Kunden må også sikre data mot ondsinnede tredjeparter og mot skyleverandøren selv.*

**Grunnleggende:** kartlegg data, behandlinger og skytjenester i bruk (inkl. SaaS), fjern ubrukte/uovervåkede ressurser; vurder sikkerhetsbehov og velg driftsmodell (offentlig, privat, hybrid, community, multi-sky) og leverandør etter garantert sikkerhetsnivå (backup, redundans, kryptering, fysisk sikkerhet, vedlikehold) iht. anerkjente skysikkerhetskrav; ta skytjenester med i risikoanalyse og BCP/DRP; sikkerhetskrav og ansvarsfordeling i kontrakt (ark 14); sikre at alle ledd (leverandør og underleverandører) faktisk holder avtalt nivå; konfigurer leverandørens sikkerhetsverktøy (kryptering, IAM, brannmur, anti-DDoS) iht. egen policy; anvend guidens grunnleggende tiltak – krypter data i ro og i transitt med egnet nøkkelhåndtering (**merk: bruker man leverandørens nøkkelhåndtering, kan leverandøren også få tilgang til data**), minste privilegium, autentisering, tilgangskonfigurasjon, sikkerhetskopier og kontroller at leverandøren har flere geografisk adskilte datasentre.

**Unngå:** flytte alt til sky uten å identifisere sensitive data som ikke bør dit; neglisjere sikkerhet ved leverandørvalg; anta at ansvaret ligger kun hos leverandøren; lavere sikkerhet enn lokalt; glemme telemetri, diagnosedata og behandlingsdata som leverandøren samler inn; tro at **serverside-kryptering gir konfidensialitet overfor leverandøren**; ikke- eller feilkonfigurerte sikkerhetsverktøy; hardkodede ukrypterte nøkler/identifikatorer i kildekode; skytjenester uten garanti om fysisk/geografisk plassering og uten sjekk av overføringsregler; backup i samme datasenter; **kontrakt som lar leverandøren få tilgang til data/systemer for visse formål (inkl. sikkerhet eller rettslig plikt) uten kundens tillatelse**.

**Videre:** jevnlige sikkerhetsrevisjoner av leverandøren; prioriter leverandører som følger GDPR-atferdsnormer med sikkerhetskrav – CISPE-koden og EU Cloud Code of Conduct; SecNumCloud-kvalifisert leverandør for særlig sensitive data (påbudt for enkelte aktører etter «cloud au centre», regel R9); HDS for helsedata; CNIL-ark om kryptering i offentlig sky og om websikkerhetsverktøy i sky.

### Ark 23 – Mobile applications / Mobilapper (s. 54–55)

**Grunnleggende:** minimer data (hver datatype må være nødvendig); velg minst mulig inngripende tillatelser og tilby alternativer (f.eks. manuell adresse i stedet for geolokalisering); TLS minst mot servere (ANSSI TLS-guide); lagre kryptografiske hemmeligheter via OS-API-er med maskinvarebeskyttelse (Android Hardware Keystore, Apple Secure Enclave); ta hensyn til OS-ets automatiske backup – deaktiver eller krypter uten nøkkel i backup; autentisering tilpasset sikkerhetsnivå (ikke biometri hvis enheten kan registrere flere personers maler når sikker identifisering kreves).

**Unngå:** kontrahere utvikler uten å definere sikkerhetsmål og -tiltak, også for underleverandører; integrere tredjepartskode/SDK-er (også fra OS-leverandører) uten å sikre at de følger beste praksis.

**Videre:** OWASP MAS L1/L2; sikkerhetsmodellen bør ikke basere seg på terminalens integritet (tjenesten skal tåle kompromitterte enheter); API-praksis (ark 25); behandle og lagre data lokalt på terminalen der mulig; endringskontroll; vedlikehold over tid: CI/CD, informere om kritiske oppdateringer eller blokkere usikre versjoner, årvåkenhet mot ondsinnede SDK-/bibliotekendringer (forsyningskjede), sikkerhetsnivå uavhengig av OS-versjon.

### Ark 24 – Artificial intelligence / Kunstig intelligens: design og læring (s. 56–57)

**Grunnleggende:** tverrfaglig utviklingsteam (dataanalyse/-teknikk, UI/UX, kvalitetskontroll, infrastruktur, fagteam) med opplæring i sikkerhet og KI-sårbarheter; obligatorisk prosedyre for kontinuerlig utvikling/integrasjon med robuste tester og autorisert/autentisert tilgang, særlig for endringer i produksjonskode; kontroller kvalitet på data og annotasjoner, skjevheter (bias), pålitelige kilder – hindre manipulering («poisoning»); unngå hel/delvis kopiering av databaser, begrens tilgang, bruk fiktive/syntetiske data til sikkerhetstesting, integrasjon og enkelte revisjoner; dokumentasjon for utviklere og brukere (design, data og modeller med begrunnelse og analyser; drift gjennom livsløpet, ytelse, bias-analyse, bruksbegrensninger; utstyrskrav, forventet latens, maks kapasitet for SaaS); verifiser legitime brukere ved tjenestetilgang (mot **modellinversjonsangrep** – rekonstruksjon av treningsdata – og tjenestenekt); revisjonsplan som dekker programvare, maskinvare og organisatoriske tiltak inkl. menneskelig tilsyn.

**Unngå:** trene på data med ukjent/upålitelig kilde eller uverifisert kvalitet/annotasjon; publisere/dele en modell uten å kontrollere output, særlig for problematisk innhold (hat) og **personopplysninger** (unntatt test/revisjon); bruke et system uten å kjenne begrensningene eller konsekvensene av feil/bias.

**Videre:** CNILs KI-faktaark; LINC-artikler om angrep og sikkerhetspraksis (føderert læring, differensielt personvern); minimering via dataaugmentering eller syntetiske data; overvåk datadrift; konfidensscore/salience-kart; utdatafiltre, RLHF, vannmerking av generert innhold.

### Ark 25 – API / Programmeringsgrensesnitt (s. 58–59)

**Grunnleggende:** identifiser aktører og roller (datainnehaver, API-forvalter, gjenbruker) og ansvarsområder; del kun strengt nødvendige data, til rette personer og formål (dataminimering); skill vanlige API-kall fra administrasjonskall (robust autentisering for sistnevnte); relevante logger for sporing og deteksjon av misbruk, ulovlig tilgang og kapasitetsoverskridelse (ark 16, 19); oppdatert dokumentasjon inkl. spørre- og dataformater.

**Unngå:** gamle API-versjoner aktive som ikke holder sikkerhetsnivået; neglisjere sikkerhet for API-nøkler (bruk f.eks. digitale hvelv/«secret vaults»).

**Videre:** test mot OWASP API Security Top 10 før lansering; CNILs anbefaling om sikker datadeling via API; standard sikkerhetstiltak (autentisering, periodisk rettighetsstyring, kryptering); sandkasse-versjon med fiktive data.

---

### Sjekkliste: «Assess the security level of my organisation's personal data» (s. 60–62)

| Ark | Tiltak («Have you thought about…») |
|---|---|
| 1 Styring av datasikkerhet | Gjøre sikkerhet til felles sak og involvere ledelsen · Jevnlig kontrollere effekten av tiltak og kontinuerlig forbedring |
| 2 Rammeverk for brukere | IT-reglement med prosedyrer for bruk av utstyr, sikkerhetsregler og administrasjonsmidler · Bindende kraft og påminnelse om sanksjoner |
| 3 Involvere og lære opp | Bevisstgjøre interne og eksterne brukere om personvernrisiko · Tilpasse innhold og språk til mottakernes roller |
| 4 Autentisering | Unik identifikator per bruker · Passordpolicy iht. CNILs anbefalinger · Kreve bytte av tildelt passord |
| 5 Tilgangsstyring | Definere autorisasjonsprofiler · Trekke tilbake utdaterte tilganger · Minst årlig gjennomgang av rettigheter |
| 6 Arbeidsstasjoner | Automatisk skjermlås · Programvarebrannmur · Oppdatert antivirus · Brukerens samtykke før fjernhjelp |
| 7 Mobil databehandling | Bevisstgjøring om mobile risikoer · Kryptering av mobile/flyttbare lagringsmedier · Hemmelighet for å låse opp smarttelefoner |
| 8 Nettverk | Begrense internettflyter · Styre Wi-Fi, bl.a. WPA3 · VPN for fjerntilgang · Segmentere nettet, minst med DMZ |
| 9 Servere | Fjerne/deaktivere unødvendige tjenester · Admin-verktøy kun for autoriserte · Kritiske oppdateringer uten opphold (etter test) |
| 10 Nettsteder | Sikre datautvekslingsflyter · Ingen hemmeligheter eller personopplysninger i URL · Kontrollere at brukerinndata er som forventet |
| 11 IT-utvikling | Innebygd personvern · Personvernvennlige standardinnstillinger · Regresjonstest/kodegjennomgang før produksjon · Fiktive/anonymiserte data i utvikling og test |
| 12 Lokaler | Låste dører · Innbruddsalarm med periodisk test |
| 13 Utveksling med omverdenen | Kryptere før overføring · Sikre at det er rett mottaker · Hemmeligheter via separat kanal |
| 14 Databehandlere | Spesifikke klausuler i databehandleravtaler · Vilkår for tilbakelevering og destruksjon · Midler til å verifisere garantiene |
| 15 Vedlikehold og utfasing | Loggbok for vedlikehold · Tredjepartsinngrep overvåket av leder · Sikker sletting før kassering |
| 16 Logging | Loggsystem · Informere brukerne · Beskytte loggutstyr og logger · Aktivt analysere logger |
| 17 Sikkerhetskopiering | Hyppige kopier · Beskytte kopier ved lagring og transport · Jevnlig teste integritet og gjenoppretting |
| 18 Kontinuitet | Kontinuitets- og gjenopprettingsplan · Jevnlige tester |
| 19 Hendelser og brudd | Behandle varsler fra loggsystemet · Interne prosedyrer og ansvar for hendelseshåndtering, inkl. melding av brudd til tilsynsmyndighet |
| 20 Risikoanalyse | Risikoanalyse, selv minimal, av fremtidig behandling · Sikre at planlagte tiltak gjennomføres og følges opp · Jevnlig revidere analysen |
| 21 Kryptografi | Anerkjente og sikre algoritmer, programvare og biblioteker · Beskytte hemmeligheter og nøkler |
| 22 Sky | Skytjenester i risikoanalysen · Vurdere leverandørens garanterte sikkerhetsnivå · Krav og ansvar i kontrakt · Samme sikkerhetsnivå i sky som lokalt |
| 23 Mobilapper | Ta hensyn til OS-spesifikke forhold for å redusere data og tillatelser · TLS · OS-ets kryptosuiter og maskinvarebeskyttelse av hemmeligheter |
| 24 KI | God sikkerhetspraksis i utvikling · Kvalitet og integritet i data og annotasjoner for læring og inferens · Revisjonsplan |
| 25 API | Organisere og dokumentere ansvarsområder for sikkerhet og datatilgang · Begrense deling til strengt nødvendige data, personer og formål |

## Praktiske sjekkpunkter

- Kontroller at det finnes en protokoll/oversikt over behandlinger og støttemedier, med dataflytdiagram som oppdateres ved endringer (ark 1).
- Kontroller at handlingsplanen har frist og ansvarlig for hvert tiltak, og at ledelsen gjennomgår sikkerhet og personvern minst årlig (ark 1).
- Kontroller passordpolicy mot entropikravene (80/50/13 bit) og at vanlige brukere ikke tvinges til periodisk bytte; passord lagres med bcrypt/scrypt/Argon2/PBKDF2 med salt (ark 4, 21).
- Kontroller at tilgangsrettigheter gjennomgås minst årlig og trekkes tilbake ved rolleendring/fratreden (ark 5).
- Kontroller at det ikke brukes ekte personopplysninger i utvikling/test, og at pre-produksjon med ekte data er sikret som produksjon (ark 11).
- Kontroller at databehandleravtalen har: konfidensialitetsansvar, minimumskrav til autentisering, tilbakelevering/destruksjon, varsling av hendelser «så snart som mulig», bistand, jevnlig gjennomgang av tiltak, revisjonsrett, loggingsplikt (ark 14, 16).
- Kontroller at skyavtalen ikke gir leverandøren tilgang uten kundens tillatelse, at dataplassering er garantert og overføringer ut av EU/EØS er vurdert, og at nøkkelhåndtering er vurdert (ark 22).
- Kontroller at applikasjonslogger registrerer opprett/les/del/endre/slett med bruker-ID, tid, type og datareferanse; lagres 6–12 måneder; ikke brukes til andre formål (f.eks. arbeidstidskontroll); og at brukerne er informert (ark 16).
- Kontroller sikkerhetskopiering etter 3-2-1, med geografisk adskilt og offline kopi, og gjenopprettingstester (ark 17).
- Kontroller at hendelsesprosessen har kriterier for når en hendelse er et brudd på personopplysningssikkerheten, intern bruddlogg, og 72-timers melding (ev. i to trinn) (ark 19).
- Kontroller at risikoanalysen dekker de tre fryktede hendelsene, ser på konsekvenser for de registrerte, og at skalaene er fastsatt på forhånd (ark 20).
- Kontroller at fjernvedlikehold er tidsbegrenset, autorisert per inngrep og logget (ark 15).
- For KI-systemer: kontroller datakvalitet/bias, beskyttelse mot modellinversjon, og at output testes for personopplysninger før deling (ark 24).

## Viktige sitater

- «Security is an essential part of the protection of personal data. It is binding on any data controller and data processor through Article 32» (s. 4)
- «Delegating the management of all IT security to a provider.» – oppført under det som bør unngås (s. 6)
- «do not request a periodic renewal of passwords for simple users (unlike administrators)» (s. 13)
- «Keep these logs for a rolling period of between six months and one year» (s. 40)
- «using logs to count hours worked is a misuse of purpose, punishable by law» (s. 40)
- «Waiting for accurate information to notify the CNIL when it is clearly established that a breach has occurred.» – under det som bør unngås (s. 44)
- «Forgetting the impact for data subjects and only considering the impact for the organisation.» (s. 49)
- «Believing that server-side encryption ensures confidentiality with the provider.» (s. 53)
- «Using real personal data for the development and testing phases. Fictitious datasets should be used as much as possible.» (s. 28)
- «3 copies of the data, storing on 2 different media, including 1 offline» (s. 42)

## Kryssreferanser

- GDPR: art. 32 (hele guiden); art. 5 nr. 1 bokstav c og nr. 2, art. 24 nr. 1 (ansvarlighet – logger som bevis, ark 14, 16); art. 25 (innebygd personvern, ark 11, 23); art. 28 (databehandleravtale, ark 14, 22); art. 9 (biometri, sensitive data, ark 4, 9); art. 33–34 (brudd, ark 19); art. 35 nr. 7 (DPIA-innhold, ark 20); art. 44 flg. (overføring ut av EU, ark 14, 22).
- Andre kilder:
  - [K34](K34-cnil-cybersikkerhet-2024.md) – CNILs kortere cybersikkerhetsanbefalinger 2024.
  - [K32](K32-nsm-grunnprinsipper.md) – NSMs tiltakskatalog; overlappende tiltak (sikkerhetskopier, MFA, logging, segmentering).
  - [K28](K28-cnil-pia-metode.md), [K30](K30-cnil-pia-kunnskapsbaser.md) – CNILs PIA-metode og kunnskapsbaser; samme terminologi (fryktede hendelser, risikokilder, støttemedier) som ark 20.
  - [K23](K23-cnil-risikoark.md) – CNILs risikoark.
  - [K10](K10-dt-kryptering.md) – Datatilsynet om kryptering (jf. ark 21).
  - [K05](K05-dt-databehandleravtale.md) – Datatilsynet om databehandleravtale (jf. ark 14).
  - [K15](K15-dt-digitale-angrep.md) – personvern ved digitale angrep (jf. ark 19).
  - [K39](K39-cnil-mobilapper.md) – CNILs anbefaling om mobilapper (utdyper ark 23).
  - [K36](K36-cnil-referentiel-digital-safe.md) – digitale hvelv.

## Aktualitet og begrensninger

- Versjon 2024 (mars 2024) – oppdatert og GDPR-basert. Erstatter tidligere utgaver (2018 m.fl.). CNIL oppdaterer guiden løpende med endringslogg (s. 1).
- Enkelte henvisninger er franske: fransk personvernlov (art. 121, art. 6), arbeidsreglement og konsultasjon med ansattrepresentanter, fransk straffelov, ANSSI-anbefalinger, RGS, HDS-sertifisering for helsedata, SecNumCloud, «cloud au centre». **[Merknad – ikke fra kilden]** I Norge svarer dette bl.a. til arbeidsmiljølovens regler om kontrolltiltak og drøfting med tillitsvalgte, forskrift om arbeidsgivers innsyn i e-post, Normen for helsesektoren og NSMs anbefalinger ([K32](K32-nsm-grunnprinsipper.md)).
- Tilsynsmyndigheten for melding av brudd er i Norge Datatilsynet, ikke CNIL. **[Merknad – ikke fra kilden]**
- Fotnote 83/84 omtaler «EDPS» men mener EDPB (European Data Protection Board) – guiden bruker begrepene om hverandre (s. 45).
- Lagringstiden for logger (6–12 måneder) er en fransk anbefaling, ikke et GDPR-krav; lagringstid må fastsettes konkret. **[Merknad – ikke fra kilden]**

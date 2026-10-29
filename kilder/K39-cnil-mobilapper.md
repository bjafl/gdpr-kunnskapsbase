---
id: K39
tittel: "Recommendation on mobile applications"
utgiver: CNIL
dato: "2025-04-08 (deliberation nr. 2025-024 av 27.03.2025, som endrer anbefalingen og opphever deliberation nr. 2024-061 av 18.07.2024)"
spraak: en
fil: "ressurser/recommendation-mobiles-app.pdf"
type: retningslinje
gdpr_artikler: [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 26, 28, 30, 32, 33, 34, 35, 36, 37]
emner: [mobilapper, sdk, tredjepartskomponenter, rollefordeling, felles-behandlingsansvar, databehandler, samtykke, eprivacy, informasjonskapsler, tillatelser, sporing, reklame-id, innebygd-personvern, sikkerhet, dpia, databehandleravtale, app-butikk, operativsystem]
relevans: høy
---

# Anbefaling om mobilapplikasjoner (CNIL, 2025)

## Sammendrag

CNILs anbefaling om mobilapplikasjoner (93 sider, engelsk «courtesy translation» – bare den franske versjonen er rettslig bindende, s. 1) klargjør hvordan personvernforordningen (GDPR) og ePrivacy-reglene (fransk personvernlov art. 82, som gjennomfører ePrivacy-direktivet 2002/58/EF art. 5(3)) gjelder for mobilapper. Dokumentet beskriver fem aktører i app-økosystemet – **app-utgiver** (publisher), **apputvikler** (developer), **SDK-leverandør**, **operativsystemleverandør (OS-leverandør)** og **app-butikkleverandør** – og gir (1) kriterier for å avgjøre om GDPR gjelder (inkl. husholdningsunntaket), (2) rolleavklaring (behandlingsansvarlig, felles behandlingsansvarlig, databehandler eller ingen rolle) per aktør med eksempler, og (3) egne kapitler med plikter, anbefalinger og god praksis for hver aktør, hver avsluttet med en sjekkliste. Sentrale tema er tillatelser (permissions) og forholdet mellom tillatelse og gyldig samtykke, samtykkehåndtering (CMP) i apper, valg og kontraktsregulering av SDK-er, dataminimering (lokal behandling, redusert presisjon), informasjon og rettigheter, og sikkerhet (TLS, nøkkellagring, OWASP MASVS L1, oppdateringer). Den versjonen som er gjengitt, er publisert 8. april 2025 og erstatter 2024-versjonen.

## Når skal agenten bruke denne kilden

- **DPA-vurdering mot SDK-/tredjepartsleverandører i en app**: om leverandøren er databehandler, felles behandlingsansvarlig eller selvstendig behandlingsansvarlig; hva kontrakten bør inneholde (dokumentasjon, behandlingsprotokoll, samtykkeblokkering, rettighets-API-er, revisjon, fjerndeaktivering, underleverandører/«russiske dukker»).
- **DPA med ekstern apputvikler/byrå**: når utvikleren er databehandler, ingen rolle eller egen behandlingsansvarlig; krav til instrukser, kontaktpunkt, akseptansetest, sikkerhetskrav og varsling.
- **DPIA og risikovurdering for en mobilapp**: kartlegging av behandlinger inkl. tredjeparter/OS-API-er, behandlingsgrunnlag, lese-/skriveoperasjoner på terminalutstyr, tillatelser, sensitive data, mindreårige, sikkerhetstiltak.
- **Spørsmål om samtykke i apper**: når samtykke kreves for tilgang til terminalutstyr (reklame-ID, sensorer, kontakter, bilder), unntak (strengt nødvendig / kommunikasjon), forholdet OS-tillatelse vs. samtykke, CMP, granularitet, tilbaketrekking.
- **Valg av tillatelser** (lokasjon, kontakter, mikrofon, kamera) og innebygd personvern.
- **Spørsmål om husholdningsunntaket** for apper som kun behandler lokalt.
- Krav til **OS-leverandører** og **app-butikker** (god praksis), f.eks. ved vurdering av hvilke garantier plattformen gir.

## Hovedinnhold

### 1. Innledning (s. 4)

- Smarttelefonen er en personlig terminal i den private og intime sfære; behandlinger i apper kan være eller fremstå som ugjennomsiktige; tillatelser er vanskelige å forstå; mange sensorer (kamera, GPS, kontaktliste, akselerometer) gir tilgang til svært inngripende data (s. 4).
- Bruk av SDK-er som behandler personopplysninger ulovlig, og ulovlig bruk av mobile identifikatorer, har allerede ført til pålegg og sanksjoner fra CNIL (MED 2018-022, -023, -042, -043; SAN-2022-025 og SAN-2022-026) (s. 4).
- Anbefalingen bygger på CNILs retningslinjer og anbefaling om informasjonskapsler og andre sporingsteknologier (deliberation 2020-091 og 2020-092) og er uten forbehold for annen rett, særlig konkurranserett og forordning (EU) 2022/1925 (Digital Markets Act, DMA) (s. 4).

### 2. Virkeområde (s. 5–8)

**Målgruppe** (s. 5): app-utgivere, apputviklere, SDK-leverandører, OS-leverandører og app-butikkleverandører – særlig personvernombud og andre som gir personvernråd. Hver aktør oppfordres til også å lese anbefalingene til partnerne sine.

**«Mobilapplikasjon»** (s. 5): programvare distribuert i smarttelefon-/nettbrettmiljø (individuelle, bærbare terminaler med internett og ofte telefonnett), privat eller profesjonell bruk. Kjøres isolert fra hverandre (sandkassemodell) og får tilgang til systemfunksjoner via API-er fra OS-leverandøren. Omfatter:
- **native** apper (Kotlin/Java for Android, Swift/Objective-C for iOS),
- **hybride** apper (webteknologi transformert via f.eks. React Native eller Flutter),
- **Progressive Web Apps (PWA)**.

**Lignende miljøer** (s. 6) – anbefalingene kan overføres så langt de passer: smartklokker, smarthøyttalere, tilkoblede bildashbord, tilkoblet personlig medisinsk utstyr, IoT generelt, PC-miljøer (Windows, macOS, Linux) og enkelte dedikerte miljøer (f.eks. spill på Steam).

**Aktørene** (s. 6–8):

| Aktør | Rolle i økosystemet | Typiske personopplysninger |
|---|---|---|
| OS-leverandør | Leverer operativsystemet som definerer alle tillatte interaksjoner mellom bruker, terminal og tredjepartsapper. Flere kan bidra: en tredjepart kan bygge på en annen OS-kodebase (f.eks. AOSP) og legge til programvarelag (tastatur, taleassistent), og produsent/mobiloperatør kan forhåndsinstallere apper. | OS genererer terminal- eller kontospesifikke identifikatorer brukt til teknisk drift, reklamesporing m.m., for egen del eller videreformidlet til tredjeparter (inkl. utgivere). Gir via API-er utgivere tilgang til sensorer (kamera, mikrofon, lokasjon, akselerometer) og lagrede data (kontakter, bilder, liste over installerte apper). |
| App-butikk | Distribusjonsplattform (App Store, Play Store, produsentbutikker, F-Droid, Aurora Store m.fl.). Ofte, men ikke alltid, samme aktør som OS. Kan fastsette regler for publisering (sikkerhet, brukerinformasjon). | Selve fastsettelsen av regler for verifisering/godkjenning innebærer ikke behandling av personopplysninger. Butikken behandler data for egne formål som enhver app (typisk brukerkonto, oppdateringer). |
| App-utgiver | Gjør appen tilgjengelig (vanligvis via butikk) for å tilby varer/tjenester; fastsetter forretningsmodellen. | Tekniske tilkoblingsdata, data fra bruker eller terminal, data utledet fra bruk; data nødvendige for tjenesten (kontakt, betaling, lokasjon) og for drift (kompatibilitet); kan overføre data til tredjeparter for monetisering (sporing, reklame-ID). |
| Apputvikler | Intern (sammenfaller med utgiver) eller ekstern kontraktspart. Bidrar til arkitektur, SDK-valg, hosting. | Konfigurerer fremtidig behandling; ved vedlikehold (testing, dataanalyse, feilrapporter) kan utvikleren bli involvert i behandlingen og få ansvar etter GDPR. |
| SDK-leverandør | Leverer tredjeparts programvareklosser installert i appen; kan kjøre lokalt, men kaller ofte nettbaserte tjenester og overfører data fra terminalen (ID, IP-adresse, konfigurasjon). | Eksempler: funksjoner (bildeanalyse, QR, AR, betaling, deling i sosiale medier); sporing for analyse på vegne av utgiver; reklameformidling der utgiver sporer brukere og bygger profiler for tredjeparts annonsører. |

### 3. Gjelder personvernreglene? (s. 10–15)

Anbefalingene gjelder (s. 10):
- **lese- og skriveoperasjoner på mobilterminalen** etter fransk personvernlov art. 82 (ePrivacy-direktivet art. 5(3)) – uavhengig av om det gjelder personopplysninger;
- **behandling av personopplysninger** etter GDPR art. 4.

#### 3.1 ePrivacy-direktivet (s. 10–11)

Art. 82 gjelder når det skjer «any action to gain access, over an electronic communications network, to information already stored in his electronic communications terminal equipment, or to store information in that equipment» (s. 10). Særlig, når det overføres over et nett:
- bruk av mobilspesifikke identifikatorer (unik terminal-ID, MAC-adresse m.m.) eller andre sporingsteknikker som **fingeravtrykk (fingerprinting)** – sporing via identifikator beregnet fra terminalens tekniske informasjon;
- tilgang til informasjon lagret i terminalen (bildegalleri, kontakter);
- tilgang til sensorer (kamera, mikrofon, lokasjon).

**Mobile identifikatorer** (s. 10–11):
- Kan være knyttet til terminalen (inkl. reklame-ID: Apples **IDFA** og **IDFV** – felles for samme utgivers apper; Googles **AAID**), til brukerens konto i OS-miljøet (f.eks. **UDID** i iOS), eller til en installasjon av appen.
- Terminalknyttede identifikatorer lar reklamepartnere/utgivere unikt identifisere terminalen i hver app. Til forskjell fra informasjonskapsler (verdi satt separat per tredjepart) genereres reklame-ID tilfeldig ved første oppstart og er **lik for alle tredjeparter**, noe som letter kobling av data mellom tredjeparter og – kombinert med innlogget miljø – på tvers av brukerens terminaler (fotnote 7, s. 10).
- Kontoknyttede identifikatorer brukes av OS-leverandøren for egne formål og kan normalt ikke brukes av tredjeparter.
- Identifikatorer kan være unike på tvers av apper (letter sporing på tvers) eller spesifikke per utgiver.

**Konsekvens** (s. 11): Informasjon og **forhåndssamtykke** kreves før lagring/tilgang, med mindre operasjonen (a) utelukkende har som formål å utføre eller lette overføring av en kommunikasjon over et elektronisk kommunikasjonsnett, eller (b) er strengt nødvendig for å levere en informasjonssamfunnstjeneste som brukeren uttrykkelig har bedt om. Den **etterfølgende behandlingen** av data hentet gjennom slike operasjoner må i tillegg ha et behandlingsgrunnlag etter GDPR.

**[Merknad – ikke fra kilden]** I Norge er ePrivacy-direktivet art. 5(3) gjennomført i ekomloven (lov 2024-12-13 nr. 76 om elektronisk kommunikasjon) § 3-15 (tidligere ekomloven 2003 § 2-7 b). Tilsynsmyndighet for denne bestemmelsen er Nasjonal kommunikasjonsmyndighet (Nkom), mens Datatilsynet fører tilsyn med den etterfølgende behandlingen etter GDPR. CNILs tolkning av art. 82 er ikke bindende i Norge, men gir veiledning om et felles EU/EØS-regelverk. Lovteksten står i [K44](K44-ekomloven-3-15.md).

#### 3.2 GDPR (s. 11)

- **Materielt**: all behandling av personopplysninger i appen.
- **Territorielt (art. 3)**: (i) behandling i forbindelse med virksomheten til behandlingsansvarlig/databehandler etablert i EU, uansett hvor behandlingen skjer; (ii) behandling av personer i EU utført av aktører utenfor EU når behandlingen gjelder tilbud av varer/tjenester til dem eller overvåking av deres atferd i EU – f.eks. en app rettet mot personer i EU.

#### 3.3 Husholdningsunntaket (s. 11–15)

- GDPR gjelder ikke behandling som en fysisk person foretar som ledd i rent personlige aktiviteter eller familieaktiviteter (art. 2 nr. 2 bokstav c, fortalepunkt 18). Fortalepunkt 18 presiserer likevel at forordningen gjelder for behandlingsansvarlige/databehandlere som stiller midler til rådighet for slik behandling (s. 12).
- **CNILs to kumulative kriterier** for at tredjepart som stiller behandlingsmidler til rådighet **ikke** omfattes av GDPR (s. 12):
  1. behandlingen settes i gang etter personens (brukerens) eget skjønn, under personens kontroll og utelukkende på personens vegne;
  2. behandlingen skjer i et **avskottet miljø** (compartmentalised), uten mulig involvering av tredjepart i dataene – tredjeparten har levert midlene, men kan ikke lenger påvirke dataene nedstrøms.
  Da leverer aktøren bare programvare; GDPR gjelder ikke programvaren. I andre tilfeller vil tredjeparten sannsynligvis ha et ansvar som behandlingsansvarlig eller databehandler.
- **Eksempler der CNIL har ansett GDPR ikke å gjelde** (s. 12): biometrisk autentisering i smarttelefon med kun lokal, kryptert lagring etter brukerens beslutning; helseapp som bare lagrer lokalt uten ekstern tilkobling og kun til personlige formål, uten fjerntjenestefunksjoner.
- **Samme resonnement kan gjelde** (s. 12–13): peer-to-peer-deling uten lagring/transitt via sentral server; apper som ren programvare uten datautveksling med tredjepart utover sporadiske oppdateringer (f.eks. tastatur med lokal «læring» uten føderering; funksjoner med kun statiske forhåndsinnlagte data).
- **Eksempel – bildegalleri uten overføring** (s. 13): app leser bilder for retusjering lokalt; verken utgiver eller OS-leverandør kan påvirke dataene → begge er «mere third parties».
- **God praksis** (s. 14): CNIL anser apper basert på behandling helt på personens initiativ og under dennes kontroll som innebygd personvern, og oppfordrer utgivere/utviklere til å holde appene oppdatert, avpublisere apper med sårbarheter som ikke lenger skal brukes, og designe etter dataminimering og sikkerhet.
- Hvis vilkårene ikke er oppfylt, gjelder GDPR for utgiverens midler, og utgiver kan være behandlingsansvarlig (s. 14). **Eksempel – delt familiealbum** (s. 14): familiens deling er husholdningsaktivitet, men utgiveren kan få ansvar hvis albumet lagres på dens eller tredjeparts servere; rolle (behandlingsansvarlig/databehandler) avgjøres konkret.
- **Beslutningsflyt** (s. 15): Behandles personopplysninger? Nei → GDPR gjelder ikke. Ja → Utføres behandlingen av en fysisk person til personlige/husholdningsformål? Nei → GDPR gjelder. Ja → GDPR gjelder ikke for personens behandling; deretter: er behandlingen (i) initiert etter personens skjønn, under personens kontroll og kun på personens vegne, OG (ii) i avskottet miljø? Ja → GDPR gjelder ikke for behandlingen som helhet; tredjeparter som leverer midler er verken behandlingsansvarlig eller databehandler (anbefalt design). Nei → GDPR gjelder; tredjeparter kan få ansvar som behandlingsansvarlig eller databehandler.

### 4. Rolleavklaring per aktør (s. 16–26)

#### 4.1 Hvorfor og hvordan (s. 16–17)

| Rolle | Definisjon | Ikke-uttømmende indikatorer (s. 16) |
|---|---|---|
| Behandlingsansvarlig | Fastsetter formål og midler (art. 4 nr. 7) | Jeg beslutter å opprette behandlingen; jeg definerer «hvorfor» og «hvordan»; jeg har beslutningsmyndighet |
| Felles behandlingsansvarlige | Fastsetter i fellesskap formål og midler for samme behandling | Beslutningene er konvergerende, komplementære og nødvendige; behandlingen er ikke mulig uten de identifiserte felles behandlingsansvarliges deltakelse |
| Databehandler | Behandler på vegne av, etter instruks fra og under myndighet av behandlingsansvarlig (art. 4 nr. 8) | Jeg leverer tjenesten på oppdrag fra behandlingsansvarlig; behandlingsansvarlig nevner spesifikt behandlingen av personopplysninger i kontraktsgrunnlaget; behandlingen er en sentral del av tjenesten jeg yter; behandlingsansvarlig kontrollerer hvordan jeg yter tjenesten |

- Andre aktører kan være kontraktsmessig involvert i design, utvikling, distribusjon og drift uten noen av disse rollene (s. 17).
- Etter ansvarsprinsippet må hver aktør fastsette rollen ut fra **faktisk rolle per behandling**, etter EDPBs kriterier (retningslinjer 07/2020), og kunne forklare begrunnelsen – særlig: **hvem besluttet å opprette behandlingen? hvem definerte formålet? hvem bestemmer hvilke personopplysninger som samles inn, lagringstid og sikkerhetstiltak?** Vurderingen skal kunne dokumenteres og **formaliseres i DPIA** når en slik gjennomføres (s. 17).
- Kvalifiseringen skjer konkret; tilsynsmyndighetene er **ikke bundet** av partenes kvalifisering i kontrakter (s. 17).

#### 4.2 App-utgiveren (s. 17–18)

Når utgiveren ikke bare leverer programvare, men deltar i driften (f.eks. dataoverføring mellom terminal og egne servere), er utgiveren **behandlingsansvarlig** for behandlingen i appen. Utgiveren er ansvarlig for:

1. **Behandling knyttet til bruk av appen**: kontodata (navn, e-post, telefon), data nødvendig for tjenesten (leveringsadresse, bankopplysninger, kundekortnummer).
2. **Lese-/skriveoperasjoner utgiveren selv utfører**, og etterfølgende behandling, f.eks.:
   - lesing av mobile identifikatorer (reklame-ID for at tredjeparts annonsører skal kunne følge brukeratferd; app-butikk som leser kontoidentifikator for å tilpasse forslag; OS-leverandør som leser kontoidentifikator for å forbedre egne systemapper);
   - tilgang til sensorer når data overføres over nett (lokasjon i ruteplanlegger; kamera for QR-skanning);
   - tilgang til lagrede data (filer for sikkerhetskopi; galleri for profilbilde; kontaktliste for kontaktoppdagelse i meldingstjeneste).
3. **Lese-/skriveoperasjoner utført av tredjeparter** (sammen med tredjepartene hvis de i fellesskap fastsetter formål og midler):
   - tredjeparts-SDK leser reklame-ID for reklameprofilering på vegne av utgiver → utgiver ansvarlig for operasjonen (eventuelt felles med SDK-leverandør);
   - tredjeparts-SDK leser teknisk identifikator på tredjepartens vegne for statistikk til forbedring av egen tjeneste → utgiver er **felles ansvarlig** for (lese)operasjonen.
4. **Lese-/skriveoperasjoner og etterfølgende behandling utført av tredjeparter på utgiverens vegne** (f.eks. SDK som leser reklame-ID og profilerer brukere for utgiveren).

Utgiveren er **ikke** ansvarlig for tredjeparters behandling **for egen regning** av data fra lese-/skriveoperasjoner via appen (f.eks. tredjepartens statistikkbehandling for å forbedre egen tjeneste; tredjepartens sammenstilling av reklame-ID med data fra andre apper for egne reklameformål). Slik innsamling via appen **må likevel være regulert i kontrakt** mellom utgiver og tredjepart (s. 18).

Bakgrunn (fotnote 16, s. 18): fransk Conseil d'État, «Éditions Croque Futur» (nr. 412589, 6.6.2018) – nettstedsutgiver som tillater tredjeparts informasjonskapsler er behandlingsansvarlig; CNIL SAN-2021-013 – utgiver har en innsatsforpliktelse (obligation of means) for samtykke til tredjeparts informasjonskapsler.

#### 4.3 Apputvikleren (s. 18–19)

| Situasjon | Rolle |
|---|---|
| Utvikler kun leverer kode og deretter ikke har rolle i drift eller kontroll over data | **Verken behandlingsansvarlig eller databehandler** |
| Utvikler implementerer infrastruktur for behandling og lagring; utfører operasjoner på data på appserveren for vedlikehold eller utkontraktering | **Databehandler** for utgiver |
| Utvikler behandler for egne formål: forbedre sikkerhet i andre apper den utvikler; statistikk for å forbedre egne tjenester; sammenstille data fra ulike apper for nye tjenester | **Egen behandlingsansvarlig** (unntaksvis) |
| Intern utvikling | Utgiver og utvikler sammenfaller – samme ansvar |

- Selv uten GDPR-rolle er utviklerens valg avgjørende for sikkerheten. **God praksis**: kontrakten krever at utvikleren designer en app som muliggjør GDPR-etterlevelse (innebygd personvern), og utgiveren involveres i strukturerende valg inkl. sikkerhet gjennom hele designet (s. 19).
- Å levere en app som i seg selv bryter GDPR gir utvikleren **sivilrettslig ansvar** overfor utgiveren; kontrakten kan kjennes ugyldig ved feil om vesentlige egenskaper (CA Grenoble 12.1.2023, nr. 21/03701) (s. 19).
- Gjenbruk for egne formål av data utvikleren har som databehandler: må informere utgiveren om formålene og få **forhåndssamtykke**; utgiveren må vurdere forenlighet med opprinnelig formål (art. 6 nr. 4) (s. 19).

#### 4.4 SDK-leverandøren (s. 19–20)

**Databehandler** når SDK-en behandler på vegne av utgiveren, særlig når (s. 19–20):
- SDK-en utfører lese-/skriveoperasjoner utelukkende på utgiverens vegne;
- SDK-en muliggjør en betalingstjeneste i appen;
- SDK-en analyserer brukeratferd for reklameprofilering på vegne av utgiveren, ved å lese reklame-ID;
- SDK-en analyserer brukerens lokasjon for profilering på vegne av utgiveren.

Hvis utvikleren er databehandler og bruker en SDK-leverandør til deler av oppdraget, er SDK-leverandøren **underdatabehandler**, og må gi samme garantier som den opprinnelige databehandleren (s. 20).

**Behandlingsansvarlig** for behandlinger der SDK-leverandøren fastsetter formål og midler (s. 20):
- **lese-/skriveoperasjoner** den utfører – **felles med utgiveren som tillater innsamlingen** – når den henter data for **egne formål**, f.eks. lesing av reklame-ID for reklameprofilering og for å forbedre profileringstjenesten; lesing av teknisk terminalidentifikator for diagnostikk/telemetri og statistikk for å forbedre SDK-en;
- **etterfølgende behandling** for egne formål (f.eks. statistikk om bruken av egen tjeneste). SDK-leverandøren må sørge for at utgiveren er godt informert om slike behandlinger, særlig i kontraktsdokumentene.

#### 4.5 OS-leverandøren (s. 20–21)

- I mange tilfeller er OS-leverandøren ikke involvert i behandlingen i appene.
- OS-leverandøren er **behandlingsansvarlig** for behandlinger for sikring/drift av OS (søk etter oppdateringer, telemetri, tjenesteforbedring, svindeldeteksjon) når den fastsetter formål og midler. Disse er i stor grad uavhengige av apper, men noen er knyttet til dem fordi de gir apper informasjon og identifikatorer.
- Situasjoner som må analyseres: (1) lokal opprettelse av mobil identifikator; (2) utlevering av mobil identifikator til tredjepart, særlig utgiver; (3) utlevering av annen terminalinformasjon (lokasjon, kontaktliste, bildegalleri) til tredjeparter.
- Miljøspesifikt: **iOS** – andre aktører har bare Apple å forholde seg til, og App Store er eneste butikk på iOS/iPadOS. **Android** – flere enheter (AOSP, Google Play Services, GMS, produsentsuiter), som kan dele ansvar avhengig av gjenbruk, særlig mellom Google og produsentene (s. 20–21, fotnote 19).
- Selv når OS-leverandører bare leverer verktøy, betinger deres tekniske valg utgivernes behandling – derfor god praksis i kap. 8.
- **OS-leverandør som app-utgiver** (systemapper): samme roller og plikter som enhver utgiver; behandlingsansvarlig for egne formål.
- **OS-leverandør som SDK-leverandør**: samme roller og plikter som enhver SDK-leverandør; behandlingsansvarlig (eventuelt felles med utgiver) for egne formål.

#### 4.6 App-butikkleverandøren (s. 21)

- Å fastsette regler for verifisering/godkjenning innebærer ikke i seg selv behandling av personopplysninger → **intet GDPR-ansvar i den sammenheng**. Det utelukker ikke ansvar på annet grunnlag, f.eks. behandling av brukeres IP-adresser i driften av butikken.
- Fotnote 20: at en kontraktspart pålegger kontraktsforpliktelser som påvirker den andres behandling, er ikke nok for felles ansvar; det avgjørende er om parten gjennom forpliktelsene påvirker behandlingen **for egne formål** (EU-domstolen C-604/22, 7.3.2024, IAB Europe).
- **Butikken som app-utgiver**: samme roller og plikter som enhver utgiver; behandlingsansvarlig for egne formål (behandling av utviklerdata i gjennomgangsprosessen, eventuell unik identifikator, liste over installerte apper og status).

#### 4.7 Eksempler på rollefordeling (s. 21–25)

**Eksempel 1 – SDK leser reklame-ID både for utgiveren og for egen regning** (s. 21–22): Utgiveren integrerer en SDK som, etter samtykke, leser reklame-ID, måler interaksjoner og analyserer for at utgiveren skal kjenne sitt publikum og monetisere annonseplass. SDK-leverandøren vil også, med utgiverens kontraktsmessige samtykke, bruke dataene til å forbedre profileringstjenesten for alle kunder.

| Behandling | Rolle |
|---|---|
| Tilgang til reklame-ID (lese-/skriveoperasjon etter art. 82) | Utgiver og SDK-leverandør er **felles behandlingsansvarlige** |
| Behandling av data på vegne av utgiver (monetisering av annonseplass) | Utgiver **behandlingsansvarlig**, SDK-leverandør **databehandler** |
| SDK-leverandørens behandling for egne formål (forbedre profileringstjeneste) | SDK-leverandør **behandlingsansvarlig** – bare tillatt hvis utgiveren er godt informert og integrerer SDK-en med kunnskap om behandlingen (f.eks. via kontrakt) |

**Eksempel 2 – Lokasjon via SDK utelukkende på utgiverens vegne** (s. 24): SDK henter lokasjon fra OS-leverandørens presise lokasjonstjeneste (basert på IP, Wi-Fi-tilgangspunkter, Bluetooth-identifikatorer). Lokasjon gir brukeren funksjoner (navigasjon, interessepunkter) og brukes av SDK-leverandøren til publikumsanalyse/monetisering for utgiveren.

| Behandling | Rolle |
|---|---|
| Integrering av SDK som får tilgang til lokasjon (lese-/skriveoperasjon) | Utgiver behandlingsansvarlig, SDK-leverandør **databehandler** (forfølger ikke eget formål) |
| SDK-leverandørens behandling av lokasjonsdata for utgiveren | Utgiver behandlingsansvarlig, SDK-leverandør databehandler |
| Presis lokasjonsberegningstjeneste tilbudt tredjeparter | OS-leverandør **behandlingsansvarlig** |

**Eksempel 3 – Kontaktliste lagret hos OS-leverandør, overført til appens server** (s. 25):

| Behandling | Rolle |
|---|---|
| Lagring av brukerens data på OS-leverandørens servere | OS-leverandør behandlingsansvarlig |
| Tilgang til dataene (lese-/skriveoperasjon) og etterfølgende behandling | Utgiver behandlingsansvarlig |

### 5. Anbefalinger til app-utgiveren (s. 27–43)

**Lesenøkkel for kap. 5–9** (s. 27): «må» (the controller must) = rettslig forpliktelse; «CNIL anbefaler» = anbefaling for å etterleve (alternativer mulig, men må begrunnes); «som god praksis oppfordrer CNIL» = utover lovkrav. Målgruppe hos utgiver: personvernombud og app-team, særlig produkteier.

#### 5.1 Design av appen (s. 28–32)

**1. Identifiser om personopplysninger behandles** (s. 28)
- Personopplysninger omfatter navn, men også alias, geografisk posisjon, aktivitetsdata i appen og tekniske identifikatorer for terminalen.
- Noen apper kan levere tjenesten uten personopplysninger (lommelykt, vater, kompass, kalkulator, stoppeklokke, metronom, stemmeapparat, enkelte spill).
- Vurder husholdningsunntaket (kap. 3.3). **Husk behandlinger utført av tredjeparter.**

**2. Sikre lovlig behandling** (s. 28–31)
- Formålet korrekt definert?
- **Behandlingsgrunnlag** etter art. 6 nr. 1 per formål; i apper særlig samtykke, avtale eller berettiget interesse:
  - Samtykke: må innhentes korrekt (5.3).
  - **Avtale**: bare hvis objektivt nødvendig – objektivt uunnværlig for et formål som er en integrert del av avtaleytelsen; behandlingsansvarlig må kunne vise at hovedformålet ikke kan oppnås uten behandlingen, og at det ikke finnes praktiske, mindre inngripende alternativer.
  - **Berettiget interesse**: krever formalisert interesseavveining. WP29 (WP251): «it would be difficult for controllers to justify using legitimate interests as a lawful basis for intrusive profiling and tracking practices for marketing or advertising purposes» (s. 28–29).
- **Lese-/skriveoperasjoner på terminalen** må identifiseres: mobile identifikatorer (reklame- eller ikke), fingeravtrykksresultater, unike identifikatorer som maskinvare-ID, sensorer, lagrede data (kontakter, bilder). Samtykke kreves med mindre unntak gjelder. CNIL anbefaler at analysen gjøres sammen med utvikleren slik at presise instrukser kan gis (s. 29).

**Tabell: Lese-/skriveoperasjoner og samtykke (s. 30)**

| Hovedregel: samtykke kreves | Unntak 1: eneste formål er å utføre/lette overføring av kommunikasjon | Unntak 2: strengt nødvendig for tjeneste uttrykkelig bedt om av brukeren |
|---|---|---|
| Eksempler: innsamling av reklame-ID for reklameformål; innsamling av kontaktdata for kontaktoppdagelse; innsamling av lokasjon for innholdsanbefaling | Eksempel: identifikatorer for lastbalansering eller ruting | (a) **Funksjon uttrykkelig etterspurt**: GPS-tilgang for en etterspurt lokasjonsfunksjon; autentiseringsidentifikatorer (WP29 Opinion 04/2012, use case 3.2). (b) **Sikring av tjenesten med fokus på å beskytte brukeren** (use case 3.3): sporingsteknologi mot tjenestenektangrep (DoS) og mot «credential stuffing». (c) **Begrenset publikumsmåling**: f.eks. enkel telling av daglige brukere for dimensjonering av tjenesten |

- **Dataminimering (art. 5 nr. 1 bokstav c)** (s. 30–31): kun nødvendige data (f.eks. ikke full fødselsdato hvis bare året trengs). Velg mellom tekniske data fra terminalen og data brukeren oppgir manuelt (f.eks. værapp: manuelt oppgitt sted vs. terminallokasjon). **CNIL anbefaler å foretrekke manuelt oppgitte data** når mulig; alle mottakere (også tredjeparter) bør vite at data er manuelt oppgitt (samme status som skjemadata på et nettsted). Anbefalt å la brukeren velge mellom manuell inntasting og automatisk overføring.
- **Lagringsbegrensning (art. 5 nr. 1 bokstav e)**: strengt nødvendig periode.
- **Særlige kategorier av personopplysninger («sensitive data», art. 9)** (s. 31): forbudt med mindre unntak i art. 9 nr. 2 (f.eks. uttrykkelig samtykke). Kategorisering/segmentering basert på slike data for reklameprofilering er **forbudt** (DSA art. 26). Ved samtykke: på forhånd, fritt, spesifikt, informert; CNIL anbefaler advarsel/egen informasjon før samtykke eller egen avkrysningsboks for separat samtykke (jf. SAN-2023-006 avsn. 56 om helsedata).
- **Mindreårige** (s. 31): ikke særskilt behandlet; se CNILs arbeid om mindreåriges digitale rettigheter. Ekstra tiltak kreves. Reklame basert på profilering er **forbudt** når mottakeren er mindreårig (DSA art. 28).

**3. Innebygd personvern og personvern som standard (art. 25)** (s. 31–32)
- Minst inngripende standardinnstillinger: fastsett minimumsparametere per behandling (f.eks. ikke lokasjon som standard hvis søkeverktøyet fungerer uten); analyser per brukerkategori (f.eks. ikke samle e-post systematisk hvis den bare trengs for betalende brukere til fakturering); ved mange tjenester, la brukeren bruke hver tjeneste uavhengig.
- Utgiveren **må** analysere om personvernfremmende teknologier (Privacy Enhancing Technologies, PETs) kan brukes (se OECD og ICO-veiledning).
- Utgiveren **må minimere data til partnere**; anbefalt å ikke overføre identifiserende data (navn, alias, unik ID) når det ikke er nødvendig; anbefalt **ende-til-ende-kryptering**.

**4. Dokumentasjon (art. 5 nr. 2 og 24)** (s. 32)
- Behandlingsprotokoll (plikt med mindre unntak i art. 30 nr. 5; ellers anbefalt).
- Begrunn og dokumenter lagringstider.
- **DPIA** når behandlingen sannsynligvis innebærer høy risiko.
- Personvernombud når påkrevd; ellers anbefalt.

#### 5.2 Kartlegging av partnere (s. 32–33)

Utgiveren må, som behandlingsansvarlig, ha fullstendig oversikt over aktører og deres tiltak (art. 24 nr. 1).

**1. Regulere forholdet til utviklere**
- Identifiser presist og på forhånd hvilke behandlinger utvikleren utfører på utgiverens vegne (utvikler = databehandler). Reguler i **databehandleravtale (DPA)**.
- Hvis utvikleren behandler for egne formål kan den være behandlingsansvarlig, men utgiveren som oppdragsgiver må være informert og ha akseptert dette, f.eks. i kontrakt.
- Utgiveren kan være behandlingsansvarlig selv uten å delta i utviklingen, hvis den har bestilt appen og deltatt i å fastsette formål og midler – selv om den ikke selv behandler, ikke uttrykkelig samtykker til konkrete operasjoner, ikke publiserer og ikke erverver appen. Avbrytes utviklingen, må utgiveren **uttrykkelig motsette seg** publisering og behandling, ellers anses den som behandlingsansvarlig (EU-domstolen C-683/21, 5.12.2023) (s. 32–33).
- Utgiveren **må** gi klare instrukser (art. 28 nr. 3 bokstav a). Anbefalt: tydelig kontaktpunkt for personvern (f.eks. personvernombud); klare, dokumenterte instrukser om sikkerhet og etterlevelsesprosesser (6.4); **akseptansetest** i kontrakten om etterlevelse av disse punktene (s. 33).

**2. Identifisere andre tredjeparter** (s. 33)
- Utgiveren må kunne sikre etterlevelse for alle databehandlere – komplisert ved tredjeparts-SDK-er, OS-API-kall, ytelsesanalyse, batteribruk og OS-telemetri. CNIL anbefaler å bruke kap. 4 for å identifisere alle tredjepartsbehandlinger.
- Utgiveren kan kreve av alle databehandlere (inkl. utvikleren) en garanti for at eneste behandling er den som følger av dokumenterte instrukser (art. 28 nr. 3).
- CNIL anbefaler at utgiveren ber utvikleren bruke **SDK-utvelgelsesmekanismene i 6.3.1**, fordi utgiveren vil ha **minst felles ansvar** for sporingsteknologi brukt av en SDK i appen.

#### 5.3 Samtykke og rettigheter (s. 33–35)

**1. Informasjon (art. 12–14)**
- Må inneholde de obligatoriske elementene i art. 13/14 og om hver behandling er obligatorisk eller valgfri (og eventuelt hvordan avslag påvirker bruken).
- CNIL anbefaler å ta med **listen over tillatelser**, om de er obligatoriske/valgfrie og formålene (s. 34).
- Overføring til forretningspartnere (f.eks. monetisering) må gjøres eksplisitt kjent. Ved samtykke må informasjonen gjøre det mulig å vurdere konsekvensene; CNIL anbefaler å fremheve **antall og bransje** for partnerne som mottar data.
- Personvernerklæringen **må** være lett tilgjengelig før behandling starter, direkte fra appen. CNIL anbefaler også tilgjengelighet **før nedlasting** (nettsted eller appens side i butikken) med erklæringen og hovedelementene (utgivers identitet, formål, hvordan rettigheter utøves).
- God praksis: presentere tillatelser i **to kategorier** – de som bare tjener tjenesten brukeren får, og de som også har andre formål.
- Erklæringen må være kortfattet og forståelig, i klart språk; kan lagdeles og ha visuelle elementer. Én samlet erklæring er ofte utilstrekkelig i mobilkontekst – CNIL anbefaler **kontekstuell informasjon** ved hver innsamling.
- God praksis: egen informasjon i grensesnittet ved tilgang til/deling av særlig inngripende data (lokasjon, kontaktliste, mikrofon), f.eks. **vedvarende indikatorer** når funksjonen er aktiv.

**2. Gyldig samtykke (art. 4 og 7)** (s. 34–35)
- Samtykke kan kreves for lese-/skriveoperasjoner (art. 82) eller som behandlingsgrunnlag (art. 6 nr. 1 bokstav a).
- CNILs retningslinjer og anbefaling om informasjonskapsler gjelder også i apper. Ta hensyn til begrenset skjermplass.
- Utgiveren er ansvarlig for innhenting av samtykke; anbefalt å forklare forventningene tydelig til utvikleren og kontrollere at instruksene følges (se 6.2.3).

**3. Rettigheter (art. 15–22)** (s. 35)
- Innsyn, sletting, protest, dataportabilitet, retting, begrensning; noen gjelder ikke avhengig av behandlingsgrunnlag.
- Ingen formkrav i regelverket. CNIL anbefaler et **rettighetssenter i appen** der alle rettigheter kan utøves.
- Svar må være fullstendige, også for databehandlernes behandling; databehandlere må ha tiltak for å bistå.
- God praksis: automatisk svar (f.eks. via rettighets-API-er).

#### 5.4 Etterlevelse gjennom appens livssyklus (s. 36–37)

**1. Sikkerhet over tid (art. 32–34)**
- Sikkerhetstiltak sikres via databehandleravtalen (art. 28 nr. 3 bokstav c).
- Utgiveren **må** be databehandlere sende sikkerhetsvarsler slik at avvik (brudd på personopplysningssikkerheten) kan meldes innen **72 timer** (art. 33).
- CNIL anbefaler: formalisere tekniske sikkerhetskrav med utvikleren (art. 32), med krav om at de også gjelder underdatabehandlere (f.eks. krav om etterlevelse av kap. 6); kontraktsfeste **oppdatering ved sårbarhet** i tredjepartskomponent eller egen kode; **skille kritiske sikkerhetsoppdateringer fra funksjonelle oppdateringer** så de kan rulles ut raskest mulig.

**2. Revisjon av partneres forpliktelser** (s. 36)
- Utgiveren må ha tilstrekkelige midler til å kontrollere at databehandleren følger instruksene (art. 28 nr. 1); databehandleravtalen må gi rett til **revisjon**.
- Tekniske tiltak alene er ikke nok; suppler med organisatoriske tiltak (5.2).
- God praksis: bruke **OWASP Mobile Application Security Testing Guide (MASTG)**; **statisk analyseverktøy** for å kontrollere at inkluderte SDK-er og tillatelser samsvarer med instruksene (be utvikleren begrunne avvik); **testbenk** (egen eller tredjepart) – testtelefon eller emulator med avlytting av nettverkstrafikk – for å kontrollere at ingen sporingsforespørsler skjer før samtykke er gitt.

**3. Robuste etterlevelsesprosesser** (s. 37)
- Utgiveren **må** oppdatere behandlingsprotokoll, DPIA og personvernerklæring ved endringer.
- CNIL anbefaler en **godkjenningsprosess** for endringer i behandlingen (valg av databehandler, SDK, funksjoner, samtykkemåte), også ved vedlikehold.
- Utgiveren må regulere databehandleres tilgang. CNIL anbefaler **loggført tilgangskontroll** (jf. CNILs anbefaling om logging, deliberation 2021-122); fiktive/syntetiske data hos databehandler er et alternativ. CNIL anbefaler at utgiveren følger opp og verifiserer **sletting** av data når lagringstiden er utløpt.

#### 5.5 Tillatelser og innebygd personvern (s. 37–41)

- Tillatelsessystemer for tilgang til ressurser (lokasjon, kontakter, kamera, bilder/film) etter brukerens valg anses som **god praksis uavhengig av rettslige krav**. Valg av tillatelser er et avgjørende steg for personvernet (s. 37).
- **Tillatelser er i seg selv et selvstendig teknisk tiltak**, ikke en oppfyllelse av rettslige plikter. Fjerntilgang til en ressurs etter tillatelse kan likevel utløse art. 82 (samtykke med mindre unntak) og GDPR (samtykke som behandlingsgrunnlag). Disse to samtykkene kan slås sammen; samspillet med tillatelse behandles i 6.2.3 (s. 38).
- Når tillatelsen gjelder personopplysninger, **må** utgiveren: sikre at personen gir tillatelsen med full kunnskap – anbefalt å angi klart om funksjonen er (i) nødvendig for appens drift, (ii) en tilleggsfunksjon til fordel for brukeren (navigasjon, QR-skanning, talememo) eller (iii) behandling til fordel for utgiveren eller tredjepart utenfor tjenesten (reklame); og la brukeren **samtykke separat** når formålene er forskjellige (granularitet). Vurderingen gjøres helhetlig; prinsippene om åpenhet og rettferdighet kan under visse forutsetninger gjøre en svært vagt formulert tillatelsesforespørsel, brukt for å styre en senere samtykkeinnhenting, ulovlig (s. 38).

**Prosess for valg av tillatelse (flytdiagram, s. 38)**:
1. Identifiser formålet og dataene som er nødvendige.
2. List tillatelser som gir tilgang til dataene; velg den med **minst ekstra innsamling**.
3. Er tilgangen obligatorisk for appens funksjon? Nei → gjør tilgangen **valgfri**.
4. Er et alternativ til tillatelsen mulig? Ja → **tilby alternativet** til brukerne.
5. Kan dataene behandles **lokalt**? Ja → bruk tillatelsen og behandle lokalt.
6. Ellers: innhent gyldig samtykke der det er påkrevd.
7. Kan metoder redusere inngripen? Ja → bruk dem. Deretter implementer tillatelsen.

**Praktiske brukstilfeller (s. 39–41)**

| Ressurs | Anbefalinger |
|---|---|
| **Lokasjon** (s. 39) | Velg tillatelsen som oppfyller minimering: **omtrentlig fremfor presis**; **engangs fremfor permanent**; **kun i forgrunnen** fremfor alltid; helst tillatelse som ikke gir informasjon til tredjeparter (f.eks. kun GPS, ikke analyse av nettverksomgivelser). God praksis: alternativ som manuell inntasting av postnummer/adresse – merk overfor mottakere at data er manuelt oppgitt. CNIL anbefaler å **behandle lokasjon på terminalen** (f.eks. nærmeste sted beregnes lokalt fra liste i appen). Uten at innsamling er nødvendig for uttrykkelig etterspurt tjeneste, **må** gyldig samtykke innhentes for fjerninnsamling. Før sending til server **må** minste nødvendige presisjon identifiseres og koordinatene **avkortes lokalt**. Anbefalt: ikke lagre brukt lokasjon på server, men i appen («min siste posisjon»); ikke samle lokasjon når appen ikke er i aktiv bruk. God praksis ved permanent tillatelse: synlig påminnelse i appen og periodisk bekreftelse. |
| **Kontakter** (s. 39–40) | Fastslå presist behov og om tilgang er nødvendig. Velg tillatelse etter minimering – ikke be om skriverett hvis lesing er nok. Valg av kontakt anbefales gjort **lokalt på terminalen**. Krysskobling av kontaktdata mellom brukere (kontaktoppdagelse i meldingstjeneste) krever **samtykke** (art. 82) og informasjon til **alle berørte** (jf. EDPB bindende beslutning 1/2021 WhatsApp om ikke-brukere og ugyldig anonymisering ved hashing). God praksis: alternativ (manuell inntasting av nummer for stikkprøve) med tak på antall/frekvens for å hindre skraping. Ved visning av kontakter som allerede bruker appen: anbefalt **samtykke fra hver bruker** til å bli funnet via egne kontaktdata – tillatelse til «kontakter» er **ikke** samtykke til at tredjeparter bruker egne kontaktdata; standard synlighet på **laveste nivå** med valg («Only me», «Friends», «Friends of friends», «All registered», «Everyone, including non-registered»); bruk minst inngripende metoder (f.eks. **Private Set Intersection**); slett lagrede kontaktdata etter analysen; tidsbegrens samtykket til slik sammenligning. |
| **Mikrofon** (s. 40) | Fastslå behov og om obligatorisk. Velg tillatelse etter minimering (særlig mulighet for parallelle lydstrømmer – betydelig risiko). Anbefalt **lokal lydbehandling** (f.eks. stemmeapparat). Uten nødvendighet for uttrykkelig etterspurt tjeneste **må** gyldig samtykke innhentes for fjerninnsamling, og personen må forstå at innholdet sendes til servere. Anbefalt: ikke lagre lyd på server uten spesifikk, begrunnet bruk; sikkerhetskopi på server valgfritt og basert på fritt, spesifikt, informert samtykke. God praksis: tilbakekall tillatelsen etter opptak ved punktvis behov; tydelig ikon når mikrofonen er aktiv; la brukeren avkorte/lytte på nytt før sending. |
| **Kamera** (s. 40–41) | Fastslå behov og om obligatorisk. Anbefalt: skille tilgang til **kamera** fra tilgang til **lagrede bilder** når bare én trengs; **ikke** be om tilgang til alt medieinnhold når det ikke trengs – bruk tillatelser der brukeren velger konkret innhold; hvis ikke mulig (interaktiv videostrøm), be om absolutt minimum (f.eks. ikke lydopptak); foretrekk å delegere opptak til **systemapper**. God praksis: alternativ uten kameratilgang. Anbefalt lokal bildebehandling; fjern metadata (lokasjon, tidsstempel, **EXIF**) som ikke trengs. Uten nødvendighet for uttrykkelig etterspurt tjeneste **må** samtykke i prinsippet innhentes for fjerninnsamling (art. 82). Før sending: vurder om hele bildet trengs, ellers tilby utsnitt/sladding. Ikke lagre bilder på server uten spesifikk, begrunnet bruk; serversikkerhetskopi valgfri og **ikke som standard**. |

#### 5.6 Sjekkliste for app-utgiver (s. 41–43)

Sjekklistene er veiledende; noen punkter er god praksis/anbefalinger, ikke plikter (s. 41). (ID-er rekonstruert fra tekstuttrekk der kolonnene var forskjøvet; rekkefølge og antall stemmer.)

| ID | Kategori / underkategori | Kontrollpunkt |
|---|---|---|
| 1.1.1 | Design – identifisere behandling | Alle personopplysninger og tilhørende behandlinger er identifisert |
| 1.2.1 | Design – lovlig behandling | Hver behandling har identifisert behandlingsgrunnlag |
| 1.2.2 | 〃 | Lese-/skriveoperasjoner på terminalen i appen er identifisert |
| 1.2.3 | 〃 | Ingen unødvendig innsamling; nødvendige data er minimert |
| 1.2.4 | 〃 | Lagringstid er knyttet til hver behandling |
| 1.2.5 | 〃 | Sensitive data er identifisert |
| 1.2.6 | 〃 | Ekstra tiltak for mindreåriges data |
| 1.3.1 | Design – art. 25 | Liste over minimumsparametere er fastsatt og er standard |
| 1.3.2 | 〃 | Parameterne er analysert per brukerkategori |
| 1.3.3 | 〃 | Personvernmekanismer er vurdert fra designfasen |
| 1.4.1 | Design – dokumentasjon | Behandlingsprotokoll er utarbeidet |
| 1.4.2 | 〃 | Lagringstider er begrunnet og dokumentert |
| 1.4.3 | 〃 | DPIA gjennomføres hvis kriteriene er oppfylt |
| 1.4.4 | 〃 | Personvernombud er utpekt |
| 2.1.1 | Partnere – utviklere | Utviklerens rolle er avtalt mellom partene |
| 2.1.2 | 〃 | Alle elementer etter art. 28 er med i kontrakten med utvikleren |
| 2.1.3 | 〃 | Instruksene er klare og dokumenterte; kontaktpunkt for personvern er tilgjengelig |
| 2.2.1 | Partnere – andre tredjeparter | Alle tredjeparter i appen er analysert for behandling av personopplysninger |
| 2.2.2 | 〃 | Hver SDK er analysert (ev. med utviklerens hjelp) for behandling av personopplysninger |
| 3.1.1 | Rettigheter – informasjon | Fullstendig, kortfattet og forståelig personvernerklæring |
| 3.1.2 | 〃 | Erklæringen er tilgjengelig før nedlasting (f.eks. nedlastingssiden) og i appen |
| 3.2.1 | Rettigheter – samtykke | Samtykkekravene i CNILs retningslinjer/anbefaling om informasjonskapsler er gjennomført |
| 3.3.1 | Rettigheter – utøvelse | Analyse av hvilke rettigheter som gjelder |
| 3.3.2 | 〃 | Rettighetssenter i appen |
| 4.1.1 | Livssyklus – sikkerhet | Forventede tekniske sikkerhetstiltak er formalisert med databehandlere |
| 4.1.2 | 〃 | Databehandlere er minnet på plikt til sikkerhetsvarsling for avviksmelding |
| 4.1.3 | 〃 | Oppdateringsprosess ved sårbarhet er avtalefestet med tredjeparter |
| 4.2.1 | Livssyklus – revisjon | Revisjon av databehandlere når risikoen tilsier det |
| 4.3.1 | Livssyklus – prosesser | Endringer reflekteres i protokoll, DPIA og personvernerklæring |
| 4.3.2 | 〃 | Instruks til databehandlere om at personvernrelevante endringer godkjennes før implementering |
| 4.3.3 | 〃 | Personopplysninger er beskyttet og tilgang loggført |
| 4.3.4 | 〃 | Sletting ved utløpt lagringstid er organisert |
| 5.1.1 | Tillatelser | For hver nødvendig opplysning velges tillatelsen med minst ekstra innsamling |
| 5.1.2 | 〃 | Alternativer til tillatelser tilbys der mulig |
| 5.1.3 | 〃 | Data behandles lokalt der mulig |
| 5.1.4 | 〃 | Samtykke innhentes gyldig der påkrevd (se 3.2.1) |
| 5.1.5 | 〃 | Presisjonen reduseres til nødvendig minimum før fjerninnsamling |

### 6. Anbefalinger til apputvikleren (s. 44–59)

Målgruppe: personvernombud i utviklingsbyrå, prosjektledere, utviklingsteam. Utvikleren er definert som den som utfører de tekniske utviklingsoperasjonene på vegne av og etter instruks fra utgiveren. Ved intern utvikling gjelder både kap. 5 og 6 (s. 44). Bruk av underleverandører krever at anbefalingene anvendes «i kaskade» (s. 45).

#### 6.1 Formalisere forholdet til utgiveren (s. 45–47)

**1. Ansvar og plikter** (s. 45–46)
- Kontrakten mellom behandlingsansvarlig (utgiver) og databehandler (utvikler) må fastsette hver parts ansvar.
- Utvikleren er databehandler når den behandler på vegne av og etter instruks. At utvikleren tar visse tekniske valg gjør den ikke nødvendigvis til behandlingsansvarlig – en databehandler kan fastsette **ikke-vesentlige midler** (EDPB 07/2020).
- Anbefalt å be utgiveren om **eksplisitt kvalifisering av rollen per behandling**. Ved databehandling **må** utvikleren be om instrukser i kravspesifikasjonen som definerer hvilke data som brukes; kontrakten må begrense behandlingen til instruksene (art. 28). Anbefalt **kontaktpunkt** hos utgiver (f.eks. personvernombud) for å godkjenne valg som påvirker behandlingen.
- Utviklerens plikter som databehandler (art. 28), særlig: **åpenhet og sporbarhet** (god praksis: gjøre kildekoden tilgjengelig for utgiveren); **bistå** med rettighetsforespørsler; **sikkerhet**; **varsle** utgiveren hvis instrukser strider mot GDPR, særlig art. 25.
- **Protokoll** over behandlinger utført for utgiveren (art. 30 nr. 3, med forbehold).
  - **[Merknad – ikke fra kilden]** Databehandlerens protokollplikt følger av art. 30 nr. 2; nr. 3 gjelder bare at protokollene skal være skriftlige (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-30)).
- Kontroller at data som behandles samsvarer med utgiverens protokoll eller kravspesifikasjon; ellers anbefalt å varsle så dokumentet oppdateres.
- Alltid handle etter dokumenterte instrukser; godkjenne bruk av **underdatabehandlere** etter art. 28.
- Underleverandører som utfører lese-/skriveoperasjoner **på egne vegne** kan bli behandlingsansvarlige eller felles behandlingsansvarlige med utgiveren; bruk og kvalifisering etter GDPR og ePrivacy må godkjennes av utgiveren (s. 46).
- Utviklerspesifikke miljøer (f.eks. delt utviklingsmiljø for flere kunder): ved behandling for egen regning (f.eks. testdata brukt på tvers av apper) gjelder plikter som behandlingsansvarlig; gjenbruk av data holdt som databehandler for egne formål bare med utgiverens forhåndssamtykke og ved forenlighet (art. 6 nr. 4).

**2. Prosjektstyring avtalt av begge** (s. 46–47)
- Beslutninger med personvernkonsekvens (tekniske valg, grensesnittdesign) skal **ikke tas alene**; involver utgiveren via kontaktpunktet. Utvikleren bør også ha en egen kontaktperson (f.eks. personvernombud).
- Presenter problemstillingene klart og be om **skriftlige instrukser** (for å kunne dokumentere at man handler etter instruks).
- Særlig oppmerksomhet: valg av partnere og SDK-er; valg av tillatelser og alternativer ved avslag; valg av samtykkeordning; informasjon og rettigheter.
- Oppretthold prosessen i hele levetiden, særlig ved eksterne endringer eller varsler (SDK-oppdatering, sikkerhetsbrudd); informer utgiveren **proaktivt**. Verktøy kan hjelpe å analysere endringer i partneres bruksvilkår. God praksis: foreslå oppdatering når nye OS-tillatelser gir bedre vern.
- **Publisering**: ofte gjør utvikleren dette i praksis. God praksis: sikre at alle elementer for brukerinformasjon i butikken foreligger. Opplastingskontoen **må være sikret, uten deling av passord**. Ved distribusjon utenom butikk må utvikleren kunne garantere **integriteten** til innholdet.

**3. Identifisere all behandling** (s. 47)
- Utviklingsvalg kan medføre ekstra behandlinger; anbefalt å informere utgiveren og i fellesskap fastsette ansvar.
- **OS-funksjoner**: databehandler-utvikler **må** analysere om OS-verktøy innebærer behandling, f.eks. **sikkerhetskopiering (ofte aktivert som standard)** – informer og bistå utgiveren med kvalifisering og spørsmål som **tredjelandsoverføring** (kap. V). Analyser alle OS-API-er (varsler/notifikasjoner, betaling, single sign-on, helseovervåking av systemet, sikkerhet, feilhåndtering) for å unngå behandling uten instruks. Følg OS-utviklingen, særlig mht. minimering.
- **SDK-er**: databehandler-utvikler **må** analysere om SDK-er behandler personopplysninger (unik maskinvare-ID, IP-adresser, omkringliggende Wi-Fi-identifikatorer m.m.). Anbefalt å innhente **liste over data som samles inn, og formål, art og hensikt med behandlingen** for valgt konfigurasjon, og kvalifisere tredjeparten etter kap. 4. Hvis tvil består: informer utgiveren og vurder å **avstå fra SDK-en**. Mener utvikleren at SDK-ens behandling bryter GDPR, har den **plikt** til å informere behandlingsansvarlig. Gjelder også SDK-er fra OS-leverandøren.

#### 6.2 Rådgiverrollen overfor utgiveren (s. 47–52)

Som databehandler må utvikleren bistå (art. 28 nr. 3 bokstav e og f) og informere hvis en instruks bryter GDPR; CNIL anbefaler at utgiveren informeres om tekniske valg og konsekvenser, som utvikleren har kontraktsansvar for (s. 47–48).

**1. Rettigheter** (s. 48)
- Databehandler-utvikler må ha tekniske/organisatoriske tiltak, særlig i **databasestrukturen**; retten til sletting må respekteres **uavhengig av tekniske begrensninger**.
- Anbefalt å foreslå en **dedikert side i appen** for rettigheter – unngår ekstra innsamling for identifisering (bruk de identifikatorene som allerede brukes).
- Ved innsyn/portabilitet må **alle** data overleveres; hvis SDK-er behandler data og utgiveren ønsker automatiske svar, må tredjepartene tilby **rettighets-API-er**.
- God praksis: minne utgiveren på å gjøre personvernerklæringen tilgjengelig i appen; **informasjonsskjerm ved første oppstart**.

**2. Utvikling i tråd med personvernprinsipper** (s. 48–49)
- Databehandler-utvikler må sikre at behandling følger instruksene, særlig om minimering.
- Når data er tilgjengelige for tredjeparter (OS, SDK), anbefaler CNIL å:
  - **begrense data i varsler (notifikasjoner)** – bare angi at noe er tilgjengelig i appen; når mulig **kryptere varselinnhold** slik at OS-leverandøren ikke får tilgang;
  - **kryptere sikkerhetskopier** slik at bare brukeren kontrollerer nøklene;
  - unngå å sende **identifikatorer på tvers av apper** til SDK-leverandører; hvis nødvendig, **hashe** dem.
- Innebygd nettleser i appen: skal ikke samle mer data enn vanlig nettleser; respekter terminalens innstillinger ved å bruke brukerens valgte nettleser.
- Uten instrukser om tillatelser må utvikleren sikre at de samsvarer med utgiverens forventninger. Anbefalt: bare nødvendige tillatelser; råd om minimering per tillatelsesnivå; frivillige alternativer ved avslag (5.5). God praksis: varsle brukeren når de mest inngripende tillatelsene er aktive.
- Tillatelsesbruk må være forenlig med kravet om gyldig samtykke før lese-/skriveoperasjoner. Anbefalt å begrense **«install-time permissions»** og foretrekke **«runtime permissions»**.
- God praksis: anbefale vernende løsninger – PETs (ICO-veiledning), lokal beregning fremfor fjern-API-er; analysere om instruerte data faktisk er nødvendige og foreslå å utelate data.
- **Særlige kategorier av personopplysninger (art. 9)** (s. 49): bare etter **uttrykkelig instruks** (art. 28 nr. 3 bokstav a); ellers informere utgiveren. Varsle ved irrelevant eller ulovlig bruk (f.eks. reklamemålretting – forbudt etter DSA art. 26). Ved SDK-integrasjon anbefalt å sikre at **SDK-er ikke har tilgang** til sensitive data. Anbefalt klart skille mellom sensitive og andre data i **arkitekturen**.

**3. Samtykkeinnhenting** (s. 49–52)
- Anbefalt å varsle utgiveren når kravspesifikasjonen krever samtykke (art. 82 eller GDPR) og bidra til korrekt implementering.
- CNILs retningslinjer om informasjonskapsler gjelder. Grensesnitt må tilpasses mobil lesbarhet; vektlegg **tilgjengelighet (universell utforming)**.
- Figurer (s. 50–51) viser akseptable mobile samtykkegrensesnitt: (1) formålsdetaljer bak en rulleknapp på første nivå; (2) detaljer via lenke på første nivå; (3) granulært samtykke på andre nivå via knappen **«tilpass mine valg»** på samme nivå som **«godta alle»** og **«avvis alle»**.
- Anbefalt å avtale samtykkeordningen med utgiveren på forhånd, implementere etter instruks og **dokumentere**. God praksis: **kontekstuell samtykkeinnhenting** knyttet til handlinger i stedet for én startskjerm (redusere samtykketretthet).
- **Samtykke vs. tillatelse** (s. 51–52): tillatelse gir teknisk tilgang, men fører **ikke nødvendigvis** til gyldig samtykke etter GDPR eller art. 82. Anbefalt å avtale behov for **Consent Management Platform (CMP)** i tillegg til tillatelsesvinduet. Samtykke kan innhentes før eller etter tillatelsesforespørselen; velg det som er enklest å forstå (f.eks. etterligne eller annotere tillatelsesgrensesnittet) uten unødig mas; brukeren skal så tidlig som mulig få relevant informasjon om hva og hvorfor. (Kilden har en infografikk/tabell om samspill CMP–tillatelse på s. 52 som ikke var lesbar i tekstuttrekket.)
- Noen OS-leverandører har mekanismer for å innhente godkjenning for et bestemt formål. Slike skjermer er **bare** gyldig samtykke når de oppfyller GDPR-kravene til informasjon (formål, **identiteten til aktørene som baserer seg på samtykket**) og til at det er like lett å avslå/trekke tilbake som å gi. Hvis ikke må utvikleren bistå utgiveren og ev. implementere en **ekstra CMP**. Brukes CMP for **samme formål**, er samtykket bare gyldig hvis valget er utvetydig – **ikke** tilfellet hvis valget i tillatelsen og i CMP-en **avviker** for samme formål. **CMP kreves uansett** for formål som ikke dekkes av tillatelsen (s. 52).

**[Merknad – ikke fra kilden]** Eksempel på OS-mekanisme for formålsspesifikk godkjenning er Apples App Tracking Transparency (ATT); kilden navngir den ikke.

#### 6.3 Riktig bruk av SDK-er (s. 52–54)

- Utvikleren foreslår SDK-er; **utgiveren tar endelig beslutning**. Databehandler-utvikler må ikke engasjere underdatabehandler uten utgiverens spesifikke eller generelle skriftlige godkjenning (art. 28 nr. 2). Integrerer utvikleren en SDK som underdatabehandler, må den videreføre **samme forpliktelser** i kontrakten (art. 28 nr. 4) og er ansvarlig ved svikt. Selv om utvikleren ikke er databehandler, må utgiveren informeres, og en **databehandleravtale må binde utgiveren og SDK-leverandøren direkte** når SDK-leverandøren er databehandler (s. 52–53).

**1. Velge SDK etter riktige kriterier** (s. 53) – vurderingsmetodikk før forslag:
- **Dokumenter fra SDK-leverandør**: utvikleren må sikre at SDK-en bare behandler innenfor utgiverens dokumenterte instrukser. Anbefalt: dokumentasjon av **alle** behandlinger ved integrasjon etter valgte innstillinger (f.eks. behandlingsprotokoll). Utvikleren **må** sikre at elementer som avdekker mulige uautoriserte **overføringer/utleveringer** (kap. V) er tilgjengelige (art. 28 nr. 4 og nr. 3 bokstav a).
- **Analyse**: SDK-en **må** kunne håndtere rettighetsforespørsler, særlig **tilbaketrekking av samtykke** (art. 28 nr. 3 bokstav e); foretrekk SDK-er med **API-er for automatisk svar**. Anbefalt: SDK-en kan **blokkere** behandling, terminaltilgang eller tillatelser til gyldig samtykke er innhentet. Gjelder også SDK-er fra OS-leverandører og SDK-er anbefalt som standard i Apples og Googles dokumentasjon.
- God praksis: vektlegg personvern som kriterium, f.eks. løsninger som **ikke finansieres ved å tjene penger på brukerdata**.
- **SDK som behandlingsansvarlig**: behandling for egen regning via SDK-en gjør leverandøren ansvarlig, og **innsamlingen må reguleres i kontrakt med utgiveren**. Når SDK-leverandøren gjenbruker data mottatt som databehandler for egne formål, må den ha **spesifikk skriftlig tillatelse** fra opprinnelig behandlingsansvarlig. Anbefalt å innhente fra SDK-leverandøren grunnlag for rollevurderingen.
- **«Russiske dukker»-effekten**: når én SDK trekker inn andre SDK-er, anbefales det å sikre at den første SDK-en gir samme garantinivå for sine egne underleverandører.

**2. Samtykkehåndtering** (s. 54)
- Vurder SDK-ens evne til korrekt samtykkeinnhenting ved sporing (art. 82) eller samtykkebasert behandling som databehandler (art. 28 nr. 4).
- Konfigurasjonen **skal** tillate samtykke **før** samtykkebasert behandling eller lese-/skriveoperasjon fra SDK-en; særlig må samtykkepliktige lese-/skriveoperasjoner **ved første oppstart forbys**.
- Utvikleren **må** velge SDK-er som tillater **tilbaketrekking**.
- Hevder SDK-en å innhente samtykke lovlig på vegne av utgiveren: god praksis å **kontraktsfeste** forpliktelsen og **revidere** den.
- **Granularitet**: ved flere formål anbefalt at SDK-en støtter granulært samtykke (normalt nødvendig for frivillighet); samtykke til ett formål begrenser SDK-ens operasjoner til det formålet. Flere tekniske operasjoner for samme formål kan dekkes av ett samtykke (f.eks. målrettet reklame: annonseutvelgelse, frekvenskontroll, måling av annonser, bekjempelse av reklamesvindel).
- Anbefalt å bare beholde SDK-er som teknisk kan **suspendere egen kjøring ved signal fra appen**.

**3. Revisjon av SDK-ers funksjon** (s. 54) – god praksis, f.eks. ved **avlytting av nettverkstrafikk**; kontroller at:
- SDK-en ikke leser/skriver (ikke-unntatt) før samtykke;
- SDK-en respekterer valg ved samtykke for ulike formål;
- SDK-en ikke samler mer data enn angitt i protokollen;
- SDK-en ikke får tilgang til beskyttede ressurser når tilgang er gitt for andre funksjoner;
- SDK-en respekterer tilbaketrekking.
Analysene oppdateres når SDK-en endres. SDK-leverandør som databehandler/underdatabehandler har **plikt til å legge til rette for revisjon**.

#### 6.4 Sikkerhet i appen (s. 55–56)

Sikkerhet er en plikt for databehandler-utvikler (art. 28); minst tiltakene etter art. 32.

**1. Minimumstiltak (systematisk)** (s. 55):
- All kommunikasjon med servere i **TLS** med eksplisitt fastsatte kryptosuiter (ANSSI TLS-veiledning).
- Lagring av kryptografiske hemmeligheter via API-er som bruker telefonens kryptosuiter, med prioritet til maskinvarebeskyttelse (**Android Hardware Keystore**, **Apple Secure Enclave**).
- **Deaktivere som standard** serversikkerhetskopier gjort av tredjeparter (f.eks. OS), ellers kryptere data uten å inkludere nøkkelen.
- Autentisering tilpasset sikkerhetsnivået (f.eks. ikke biometri hvis enheten tillater biometriske maler for flere personer når man må vite sikkert hvem brukeren er).
- Generelt: oppfylle **OWASP-nivå L1** (OWASP MAS-sjekklisten).

**2. Sikkerhetsmodell** (s. 55):
- Ikke bygge sikkerhetsmodellen på **terminalens integritet** unntatt i begrunnede tilfeller (f.eks. bankapper); da anbefalt å **rapportere** manglende integritet **uten å blokkere**.
- Ikke bygge sikkerhetsmodellen på **certificate pinning** eller **kodeobfuskering**.
- Design tjenesten slik at sikkerhetsnivået opprettholdes selv med kompromitterte terminaler.
- Følg CNILs anbefalinger om API-er for å sikre servere mot misbruk.
- Beskytt mot uautorisert tilgang fra databehandlere; loggbasert tilgangskontroll mot intern misbruk.

**3. Sikkerhet over tid** (s. 55–56):
- Utrullingsprosesser: **CI/CD** for hyppige oppdateringer, særlig sikkerhetsoppdateringer; **kodegjennomgang (peer review)** før utrulling.
- Eksterne komponenter: nyeste versjoner; overvåke ondsinnede endringer i SDK-er/biblioteker (**supply-chain security**); bruke færrest mulig tredjepartselementer.
- Holde versjoner i butikkene oppdatert: vurdere krav om nyere OS-versjon ut fra datasensitivitet og økodesignreferanser (RGESN 2024) – og i så fall bare la gjenværende versjoner for eldre OS være tilgjengelige hvis risikoen er minimal; vurdere **tvungen oppdatering**, f.eks. ved å blokkere funksjoner på serversiden for usikre versjoner.
- Ved konstatert eller **mistenkt** avvik: varsle utgiveren **så snart som mulig** (art. 28).
- Følge CNILs GDPR-veiledning for utviklingsteam.

#### 6.5 Sjekkliste for apputvikler (s. 56–59)

| ID | Kategori / underkategori | Kontrollpunkt |
|---|---|---|
| 1.1.1 | Formalisere forholdet – ansvar og plikter | Fullstendige, klare instrukser om behandlingen gis ved kontraktsinngåelse, inkl. hver aktørs rolle |
| 1.1.2 | 〃 | Kontaktpunkt hos utgiver for godkjenning av valg som påvirker behandlingen |
| 1.1.3 | 〃 | Data behandles kun etter spesifikke instrukser |
| 1.1.4 | 〃 | Utviklerens plikter som databehandler (art. 28) er identifisert og gjennomført |
| 1.2.1 | Formalisere – prosjektstyring | Beslutninger som påvirker personvern godkjennes **skriftlig** av utgiver etter informasjon og råd fra utvikler |
| 1.2.2 | 〃 | Prosess for å følge eksterne endringer som påvirker behandlingen, inkl. varsling av utgiver |
| 1.2.3 | 〃 | Alle elementer for brukerinformasjon er mottatt fra utgiver når publisering i butikk er delegert |
| 1.3.1 | Formalisere – identifisere behandling | Behandlinger via OS-funksjoner er identifisert og godkjent av utgiver |
| 1.3.2 | 〃 | Behandlinger via SDK-er er identifisert og godkjent av utgiver; nødvendig informasjon (dataliste, formål, art) er innhentet fra SDK-en |
| 1.3.3 | 〃 | Utgiver varsles straks hvis slike behandlinger bryter GDPR |
| 2.1.1 | Rådgiverrolle – rettigheter | Rettigheter kan utøves enkelt, f.eks. via side i appen |
| 2.1.2 | 〃 | Rettighetsutøvelsen omfatter all behandling i appen, også tredjeparter som SDK-er |
| 2.1.3 | 〃 | Mobillesbar personvernerklæring fra utgiver er tilgjengelig i appen |
| 2.2.1 | Rådgiverrolle – personvernprinsipper | Moderne tekniske løsninger for minimering og begrensning av tredjeparts tilgang er analysert og foreslått |
| 2.2.2 | 〃 | Tillatelser er strengt nødvendige; alternativer finnes |
| 2.2.3 | 〃 | Sensitive data er skilt fra andre data, særlig i arkitekturen |
| 2.2.4 | 〃 | Sensitive data er ikke tilgjengelige for tredjeparter (f.eks. SDK-er) |
| 2.3.1 | Rådgiverrolle – samtykke | Samtykkepliktige operasjoner er identifisert og innhentingsmåten forhåndsgodkjent av utgiver |
| 2.3.2 | 〃 | Samtykker oppfyller kravene i anbefalingen om informasjonskapsler, tilpasset mobil |
| 2.3.3 | 〃 | Når samtykke og tillatelse gis for samme operasjon, skaper samspillet ikke forvirring eller overdreven mas |
| 3.1.1 | SDK – utvelgelse | SDK-leverandøren gjør tilgjengelig dokumentasjon av all behandling og alle data ved integrasjon |
| 3.1.2 | 〃 | SDK-en gjør det mulig å svare på rettighetsforespørsler |
| 3.1.3 | 〃 | Ansvar er kvalifisert for hver behandling ved SDK-integrasjonen og godkjent skriftlig av utgiver |
| 3.2.1 | SDK – samtykke | SDK-en gir informasjon om formålene for korrekt samtykkeinformasjon |
| 3.2.2 | 〃 | SDK-en tillater granularitet og tilbaketrekking |
| 3.2.3 | 〃 | SDK-en kan konfigureres til ingen lesing/skriving før samtykke (særlig ved første oppstart) |
| 3.4.1 (trolig 3.3.1) | SDK – revisjon | Etterlevelse av SDK-leverandørens forpliktelser revideres, med leverandørens bistand |
| 4.1.1 | Sikkerhet – minimumstiltak | Kommunikasjon alltid i TLS |
| 4.1.2 | 〃 | OS-ets kryptosuiter og fysisk beskyttelse av hemmeligheter brukes |
| 4.1.3 | 〃 | Sikkerhetskopier (også automatiske) krypteres med lokalt lagret nøkkel |
| 4.1.4 | 〃 | OWASP MAS nivå L1 er nådd |
| 4.2.1 | Sikkerhet – modell | Sikkerhetsmodellen bygger ikke på terminalens integritet |
| 4.2.2 | 〃 | Påvist integritetsfeil vises til brukeren og brukes ikke til å blokkere |
| 4.2.3 | 〃 | API-er har elementer for å sikre tjenestene |
| 4.2.4 | 〃 | Personopplysninger er beskyttet mot intern misbruk og misbruk hos databehandlere |
| 4.3.1 | Sikkerhet over tid | Appen oppdateres så ofte som nødvendig av sikkerhetshensyn |
| 4.3.2 | 〃 | Ondsinnede endringer i SDK-er/biblioteker overvåkes («supply-chain security») |
| 4.3.3 | 〃 | Appen oppdateres ved OS-endringer som følge av sikkerhetsbrudd, avhengig av sensitivitet |
| 4.3.4 | 〃 | Mistenkte eller faktiske avvik meldes til utgiver |

### 7. Anbefalinger til SDK-leverandøren (s. 60–70)

SDK-leverandør: den som gjør én eller flere SDK-er tilgjengelige for integrasjon i apper, ofte med tilhørende servere og integrasjonsdokumentasjon. Målgruppe: personvernombud, tekniske team og kommersielle team (integrasjon og kontrakt). Data kan behandles for egen regning, for utgiveren eller i fellesskap; roller må identifiseres **på forhånd**, særlig fordi samme SDK-leverandør kan være både databehandler og behandlingsansvarlig. SDK-er med kun lokale funksjoner gjør leverandøren til ren programvareleverandør uten GDPR-rolle, men den oppfordres til et design som ikke hindrer etterlevelse (s. 60).

#### 7.1 Utforme tjenesten (s. 61–62)

**1. Plikter etter rolle** (s. 61)
- Kvalifiser hver behandling etter kap. 4 og EDPB 07/2020 (databehandler eller felles behandlingsansvarlig m.m.). Er leverandøren behandlingsansvarlig/felles ansvarlig, gjelder også utgiverkapitlet.
- Innsamling via SDK-en må **aldri skje uten at de registrerte vet om det**.
- Som (felles) behandlingsansvarlig: særlig oppmerksomhet på **informasjon** og identifisering av **særlige kategorier av personopplysninger** (art. 9).
- Som databehandler: sikre at behandlingsansvarlig kjenner til **tredjelandsoverføringer** (kap. V) for å etablere kontraktsmessig og/eller teknisk rammeverk (jf. EDPB-anbefaling 01/2020 om supplerende tiltak).

**2. Innebygd personvern og personvern som standard** (s. 62)
- Analyse for alle behandlinger SDK-en utfører.
- **Minimering**: begrens data til leverandørens og partneres servere til det strengt nødvendige. **Standardkonfigurasjoner** – også i dokumentasjonens eksempler – må være i tråd med minimering. Unngå innsamling/lagring av terminal- og nettverksidentifikatorer (IP-adresse, omgivende nettverksutstyr) som ikke trengs. God praksis: følge med på nyere funksjoner (f.eks. omtrentlig lokasjon) og oppdatere SDK-en.
- **Oppdeling av tjenester**: anbefalt at funksjoner kan **frikobles** og konfigureres separat, særlig når de innebærer ulikt ansvar. Eksempel: publikumskvalifisering (som databehandler) og retargeting-innsamling for egen regning (som behandlingsansvarlig) bør kunne velges uavhengig av utgiveren – eventuelt med **betalt alternativ** hvis valget påvirker forretningsmodellen. **Når funksjonene krever samtykke, er teknisk frikobling nødvendig.** Anbefalt å unngå å samle alle tjenester i én SDK, eller lage den **modulær** (begrenser også sårbarheter).
- **Systemtillatelser**: skill mellom **strengt nødvendige** og **ønskede, men ikke uunnværlige** (f.eks. taleinput i chatassistent krever mikrofon, men assistenten skal fungere uten). Anbefalt: minst inngripende tillatelsesnivå eller konfigurasjonsvalg. Skill tillatelser for tjenesten til appen fra tillatelser/behandling for leverandørens egne formål (forretningsmodell). Gjør SDK-en minst mulig avhengig av tillatelser; vurder alternativer (5.5).

#### 7.2 Dokumentere riktig informasjon (s. 62–64)

**1. Hva som skal dokumenteres** (s. 62–63)
- Anbefalt: utarbeide og gjøre tilgjengelig en **analyse av behandlingene** ved bruk av SDK-en (både som ren programvareleverandør og ved operativ rolle) – gjør det mulig for utgiveren å besvare butikkenes krav ved publisering/oppdatering.
- Ved sannsynlig høy risiko har SDK-leverandøren **plikt til DPIA** (art. 35).
- Identifiser rolle per behandling (anbefalt fastsatt i samråd med partnere). Som behandlingsansvarlig: egen **protokoll** (art. 30). Som databehandler med underdatabehandler: innhent behandlingsansvarliges godkjenning og videreføre samme forpliktelser (art. 28).
- **Sporingsteknologi**: **må** informere partnerne (behandlingsansvarlig hvis databehandler; ev. felles ansvarlige) presist om lese-/skriveoperasjoner på terminalen og formålet med hver. Uten GDPR-rolle: god praksis å dokumentere funksjoner med sporingsteknologi.
- **Tillatelser**: **må** informere om tillatelsene SDK-en krever, og for hver om den er knyttet til lese-/skriveoperasjon etter art. 82 som kan kreve samtykke. Anbefalt å angi om operasjonene er **valgfrie eller obligatoriske** per funksjon.

**2. Tilgjengelig format** (s. 63–64)
- Informasjonen må være oppdatert og lett tilgjengelig for alle partnere. Roller, plikter og samtykkeinnhenting **må formaliseres i kontraktsdokumentasjonen**.
- Anbefalt at alle endringer med personvernbetydning **uttrykkelig meldes** til partnerne; som databehandler må endringene **godkjennes av behandlingsansvarlig før implementering**.
- **Protokollformat** (s. 64): (art. 30-plikt for virksomheter med over 250 ansatte, med unntak etter nr. 5): hver behandling skilles etter formål; hvis behandlingen avhenger av innstillinger, anbefales en **dynamisk protokoll** etter SDK-konfigurasjon (ellers angi hvilke parametere som utløser hvilken behandling); dataene per behandling angis eksplisitt, gjerne i **regneark**; **behandlingsgrunnlag** og avledede plikter **må** angis per behandling; god praksis: utforme protokollen slik at partnerrelevant informasjon kan trekkes ut, med angivelse av forretningshemmeligheter.
  - **[Merknad – ikke fra kilden]** Art. 30 nr. 5 er et unntak for foretak med færre enn 250 ansatte, og unntaket gjelder ikke dersom behandlingen sannsynligvis vil medføre en risiko for de registrertes rettigheter og friheter, ikke skjer leilighetsvis eller omfatter særlige kategorier (art. 9 nr. 1) eller opplysninger om straffedommer og lovovertredelser (art. 10). Protokollplikt kan derfor gjelde også under 250 ansatte (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-30)).
- God praksis for (felles) behandlingsansvarlig SDK-leverandør – **tabell over lese-/skriveoperasjoner**, per linje: operasjonen, tilknyttet tillatelse, formål (ev. protokollreferanse), **teknisk middel for å blokkere/aktivere** lesingen (for partnernes samtykkeverktøy); **eksempelformuleringer** for samtykkeinformasjon; **hvilke SDK-versjoner** som bruker hver linje.

#### 7.3 Samtykke og rettigheter (s. 65–66)

**1. Rettigheter** (s. 65)
- Som behandlingsansvarlig: svare direkte; som databehandler: bistå.
- **Informasjon**: som (felles) behandlingsansvarlig **plikt** å sørge for at de registrerte informeres; anbefalt integrert i utgiverens informasjon. Overføring til forretningspartnere må gjøres eksplisitt kjent; ved samtykke må konsekvenser og omfang fremgå – anbefalt å fremheve **antall og bransje** for mottakerpartnere. Anbefalt å **kontraktsfeste** at utgiver/utvikler skal gi informasjon om SDK-leverandørens behandlinger og samtykkeinformasjon. Leverandøren kan tilby en grensesnittkomponent (som en CMP). Anbefalt å følge med på partneres personvernerklæringer; som databehandler rapportere manglende eller for generell informasjon til behandlingsansvarlig (art. 28 nr. 3).
- **Rettighetsutøvelse**: som databehandler plikt til å legge til rette etter avtalt funksjon; for egne behandlinger fullt ansvar. Tenk rettigheter fra start, særlig databasestruktur; **sletting uavhengig av tekniske begrensninger**. Særlig oppmerksomhet ved overføring til forretningspartnere. Anbefalt å vurdere **automatisering via API-er** (i appen eller på kundens server), med **færrest mulig ekstra identifikatorer** – f.eks. kan reklame-ID være tilstrekkelig. Etter art. 11 kan en forespørsel bli uten effektivt svar, f.eks. hvis personen har nullstilt reklame-ID og ikke kjenner den gamle – ekstra informasjon kan da trengs.

**2. Sporingsteknologi og samtykke** (s. 66)
- Som databehandler anbefales praktiske råd til behandlingsansvarlig om behov for samtykke, og tekniske midler for å ta hensyn til samtykke og tilbaketrekking.
- **Tillatelse gitt til appen er ikke samtykke til SDK-ens behandling**: når SDK-ens tilgang krever samtykke, må behandlingsansvarlig sikre gyldig samtykke **per formål**; samtykke kan ikke anses gitt bare ved tillatelse, særlig ikke når tillatelsen ble gitt for et annet formål enn SDK-ens.
- Anbefalt tekniske og organisatoriske midler som **blokkerer** all behandling og terminaltilgang (eller tillatelser) til gyldig samtykke; SDK-en bør kunne **suspendere kjøring** til samtykke foreligger.
- Gyldig samtykke må være **spesifikt** (atskilt fra aksept av bruksvilkår) og **fritt** (kunne velge per formålstype); samtykkesignaler må respekteres granulært per formål, **uavhengig av status for tillatelser**.
- Design og dokumentasjon bør forutse funksjonelle konsekvenser av manglende samtykke for å unngå unødig blokkering ved avslag.
- **Tilbaketrekking** må respekteres; den skal ikke gi ustabil app eller **gjentatte forespørsler** om tilbakekalt tillatelse (ville undergrave frivilligheten).
- God praksis: begrense **install-time permissions**, foretrekke **runtime permissions** for integrasjon med utgiverens verktøy og kontekstuelle forespørsler; ubrukt funksjon → tillatelsen skal ikke vises. En blokk av tillatelser ved installasjon som kanskje ikke brukes, kan stride mot **art. 25**.

#### 7.4 Etterlevelse over tid (s. 66–67)

- **Sikre SDK-er**: som databehandler samme sikkerhetskrav som ekstern utvikler (6.4); ren programvareleverandør oppfordres til det samme.
- **Revisjon**: som databehandler **må** kontrakten gi rett til revisjon (art. 28 nr. 3 bokstav h); gjøre tilgjengelig all informasjon som viser etterlevelse (inkl. oppdatert teknisk dokumentasjon, også for egne underdatabehandlere). Anbefalt å få SDK-en **revidert jevnlig på eget initiativ**. God praksis: **deaktiveringsfunksjon** som utgiveren enkelt kan aktivere **eksternt og i produksjon** for å pause bare SDK-ens behandling (etter revisjon, rettslig usikkerhet, feil m.m.) uten å sette hele appen ut av drift.
- **Robuste prosesser**: anbefalt verktøy/metodikk for **sårbarhetsrapportering**; som databehandler plikt til å informere behandlingsansvarlig (art. 32–36). Ved brudd er SDK-leverandør som (felles) behandlingsansvarlig selv forpliktet til å melde til tilsynsmyndighet (og ev. informere registrerte) eller sikre at felles ansvarlig har meldt (art. 33–34).
- Følge med på OS-API-endringer; god praksis å oppdatere SDK-en for mer personvernvennlig behandling og oppfordre til bruk av nyeste versjon.

#### 7.5 Sjekkliste for SDK-leverandør (s. 67–70)

| ID | Kategori / underkategori | Kontrollpunkt |
|---|---|---|
| 1.1.1 | Utforme tjenesten – plikter | GDPR-rolle (behandlingsansvarlig, felles ansvarlig, databehandler) er fastsatt per behandling i SDK-en |
| 1.1.2 | 〃 | Sensitive data er identifisert og behandlingen tilpasset |
| 1.2.1 | Utforme – art. 25 | Data samlet inn av SDK-en og overført til partnere er minimert |
| 1.2.2 | 〃 | Funksjoner kan integreres og kjøres frikoblet, særlig ved ulike ansvar/formål |
| 1.2.3 | 〃 | Ulike funksjoner er delt i separate SDK-er fremfor én samlet |
| 1.2.4 | 〃 | Tillatelser er minimert; skille mellom strengt nødvendige og ønskede |
| 1.2.5 | 〃 | Ved flere mulige tillatelser velges den med minst inngripende tekniske egenskaper |
| 2.1.1 | Dokumentere – informasjon | Klar, tilgjengelig analyse av behandlingene ved bruk av SDK-en |
| 2.1.2 | 〃 | Aktørenes rolle er identifisert per behandling |
| 2.1.3 | 〃 | For behandling med (under)databehandler er formålsanalyse gjort og behandlingsansvarliges godkjenning innhentet |
| 2.1.4 | 〃 | Sporingsteknologi (lesing/skriving på terminalen) er angitt presist og eksplisitt med formål |
| 2.1.5 | 〃 | Valgfri/obligatorisk karakter for hver tillatelse er angitt per funksjon |
| 2.2.1 | Dokumentere – format | Dokumentasjonen er oppdatert |
| 2.2.2 | 〃 | Informasjonen er formalisert i kontraktsdokumentasjonen der det kreves |
| 2.2.3 | 〃 | Egen informasjon ved SDK-oppdateringer som endrer behandlingen |
| 2.2.4 | 〃 | Protokollen skiller tydelig formålene per behandling |
| 2.2.5 | 〃 | Dynamisk eller separat protokoll når formål avhenger av konfigurasjonen |
| 2.2.6 | 〃 | Protokollformat (f.eks. tabell) gjør det enkelt å identifisere hver opplysning med rettslige (grunnlag, formål, plikter) og tekniske (lesing, skriving) elementer |
| 2.2.7 | 〃 | Eksempelformuleringer for samtykke tilbys partnerne |
| 3.1.1 | Samtykke og rettigheter – rettigheter | API-er gjør at partneres rettighetsforespørsler automatisk reflekteres i SDK-infrastrukturen |
| 3.1.2 | 〃 | API-ene bruker ingen eller færrest mulig ekstra identifikatorer |
| 3.2.1 | Samtykke og rettigheter – sporing/samtykke | Tillatelse alene anses ikke som gyldig samtykke for SDK-ens behandling |
| 3.2.2 | 〃 | SDK-en kan suspenderes til gyldig samtykke per formål foreligger |
| 3.2.3 | 〃 | Ved flere formål tas eget signal per formål hensyn til, uavhengig av systemtillatelser |
| 3.2.4 | 〃 | Alternativer tilbys partnere ved avslag, så appen fungerer |
| 3.2.5 | 〃 | Tilbaketrekking påvirker ikke appens funksjon eller brukeropplevelse (f.eks. samtykkeforespørsel i løkke) |
| 3.2.6 | 〃 | Systemtillatelser bes om under kjøring fremfor ved installasjon der mulig |
| 4.1.1 | Etterlevelse over tid – sikre SDK-er | Se utviklersjekklisten 4.1.1–4.3.4 |
| 4.2.1 | 〃 – revisjon | Revisjonsrapporter for SDK-en utarbeides jevnlig og gjøres tilgjengelige for utgivere og tilsynsmyndigheter på forespørsel |
| 4.2.2 | 〃 | Utgiveren kan pause SDK-en eksternt og i produksjon ved rettslig usikkerhet eller teknisk feil |
| 4.3.1 | 〃 – prosesser | Teknisk og organisatorisk prosess for avvik, med informasjon til behandlingsansvarlige og format for avviksmelding |
| 4.3.2 | 〃 | Jevnlig oppfølging av OS-utvikling og API-er for å styrke art. 25 |

### 8. Anbefalinger til OS-leverandøren (s. 71–83)

OS-leverandør: den som gjør et OS tilgjengelig på en terminal – helt egenutviklet for egne terminaler (iOS), egenutviklet for lisensiert bruk på tredjeparts terminaler (Android), eller basert på eksisterende OS (fork, f.eks. LineageOS på AOSP). OS-leverandør som utgiver av systemapper eller SDK-leverandør følger de kapitlene. Kapitlet består i stor grad av **god praksis**. Designvalg i åpen kildekode-OS forplanter seg til alle som gjenbruker koden – derfor bør innebygd personvern legges inn der. Integrering av tredjepartsapper i OS medfører behandlinger som må identifiseres (s. 71–72).

#### 8.1 Etterlevelse for egen behandling (s. 72–74)

- **Ansvarsanalyse** per leverandør ut fra faktisk levering av funksjonelle byggeklosser; ansvar kan foreligge (konkret vurdering) for enhet som utvikler OS for egne terminaler, enhet som gjenbruker tredjeparts byggeklosser for nytt OS, og enhet som utvikler OS for tredjeparts terminaler der kjøringen innebærer behandling for egen regning. OS som bare leverer verktøy med behandling begrenset til terminalen, er a priori verken behandlingsansvarlig eller databehandler (s. 72).
- Berørte behandlinger: sensorbruk (f.eks. forhåndsbehandling av lokasjon); funksjoner til apper (varsler, krasjhåndtering, fjernsikkerhetskopier); OS-spesifikk behandling (telemetri, feilrapportering) (s. 72–73).
- **Standardinnstillinger** (s. 73): OS-leverandøren **må** sikre at ingen samtykkepliktig egen behandling og ingen ikke-unntatt lese-/skriveoperasjon skjer før gyldig samtykke; samtykket må innhentes **spesifikt og atskilt fra aksept av bruksvilkårene**; ikke strengt nødvendige formål skal tydelig merkes som valgfrie. Anbefalt at terminalen og apper kan brukes **uten å opprette konto**, og at «dark patterns» for å presse frem konto unngås (jf. SAN-2019-001).
- **Minimering** (god praksis, s. 73–74):
  - Varsler: tillate **tredjeparts varslingsservere** (optimalisert for batteri); tilby oppdaterte verktøy for å **kryptere varselinnhold** uavhengig av overføringssystem, med dokumentasjon.
  - Telemetri/feilrapporter: feil- og krasjsystem uten ny behandling – ideelt bare utgiver og dens databehandlere har tilgang; la utgivere/tredjeparter innhente samtykke før hver innhenting/overføring.
  - Fjernsikkerhetskopier: **må** bare skje ved eksplisitt forespørsel fra appen, **ikke som standard**; bes om å tillate kryptering, helst som standard, med nøkkel OS-leverandøren ikke har tilgang til.
  - Lokasjon: enkelt å begrense til **kun GPS** uten Wi-Fi/Bluetooth-tjenester; for nettverksbasert lokasjon foretrekkes beregning **på terminalen** (f.eks. server sender data om tilkoblinger i et større område, terminalen beregner lokalt); enkel mulighet for å **suspendere kontinuerlig lokasjonsinnsamling** slik at den bare er aktiv når en app faktisk trenger det.

#### 8.2 Informere partnere (s. 74–75)

- **Dokumentasjon**: omfattende teknisk dokumentasjon som gjør det mulig for utgivere/utviklere å kvalifisere sitt ansvar; god praksis med generell påminnelse om regelverket – men **uten å pålegge partnerne bestemte etterlevelsesprosedyrer**. Inkluder EUs rettslige rammeverk for dem som retter seg mot EU-markedet; samle juridisk og teknisk; på et **språk målgruppen forstår**. Varsle om behovet for å fastsette ansvar og tiltak (formål, informasjon, rettigheter, sikkerhet); egne veiledninger/verktøy for personvernombud til risikoanalyse. Ved flere API-er for samme formål (f.eks. lokasjon): beskriv tekniske og rettslige egenskaper (bakoverkompatibilitet, slutt på støtte, sårbarhet, energi, hvor beregningen skjer, overføringer). Angi om verktøy oppfyller rettslige krav (f.eks. GDPR-samtykke) og med hvilken konfigurasjon.
- **OS-ets egne behandlinger**: partnere skal kunne kjenne, forstå og dokumentere behandlingen; for aktiverte funksjoner angi **uttømmende data** for valgt konfigurasjon, **rettslig kvalifisering** (innsamling, lagring, gjenbruk for OS-leverandøren) og varselpunkter, særlig **tredjelandsoverføringer**. Detaljert informasjon om sikkerhetskopier, varsler, telemetri; risiko for sensitive data; virkning av standardinnstillinger.
- **Fremme de mest personvernvennlige funksjonene** (s. 75): informere SDK-utgivere, utviklere og leverandører om mer vernende funksjoner (f.eks. omtrentlig lokasjon); liste endringer med praktiske eksempler; forklare rettslige konsekvenser; angi art. 25-konforme implementasjoner; statistikk over bruk av nye funksjoner for målrettet kommunikasjon; **gradvis utfasing** av de mest inngripende funksjonene med tilstrekkelig overgangstid; dialog med utviklere, eksperter og tilsyn.

#### 8.3 Verktøy for rettigheter og samtykke (s. 76–79)

**1. Tillatelsessystemer etter innebygd personvern** (s. 76–77)
- Gjelder **tekniske tillatelser** (gi/blokkere tilgang til ressurser uavhengig av formål), ikke tillatelser for handlinger med et bestemt formål (f.eks. innsamling av reklame-ID).
- Konkurranserett/DMA: tillatelser må ikke favorisere OS-leverandørens egne eller forhåndsinstallerte apper og må presenteres likt for alle apper; de skal ikke utformes for å hindre utgivere i å få tilgang til relevante data, men sikre brukerkontroll.
- God praksis: tillatelser for **sensorer** (kamera, GPS, miljøsensorer), **funksjoner** (nettverk, Bluetooth, NFC) og **lagring** (kontakter, bilder, masselagring); informasjon og tillatelse for alle, synlige tillatelser; tillatelse **uavhengig av** om art. 82 krever samtykke.
- **Tre akser for tillatelsens omfang**: (1) **presisjon** (f.eks. GPS-nivåer; fysiske sensorer som barometer, termometer, fotometer, gyroskop, akselerometer); presisjonsnivået bør angis for den som bruker dataene; (2) **materielt omfang** (unngå globale filtillatelser, foretrekk per fil/mappe); (3) **tidsmessig omfang** (engangs eller tidsbestemt; kontekst som forgrunn/aktiv/inaktiv). CNIL oppfordrer til finest mulig brukerkontroll langs alle tre akser.
- **Tilleggstiltak** (god praksis): tillatelse aldri før oppstart, bare når appen trenger den; oppfordre til kontekstuelle forespørsler; la brukeren velge informasjonsnivå (f.eks. **delvis kontaktliste**) – i **samme tekniske format** uansett valg, på transparente, rettferdige og ikke-diskriminerende vilkår; tillate **engangs** eller **kun når appen er aktiv/i forgrunnen** for de mest inngripende (lokasjon, kamera, mikrofon), med styrket informasjon ved «alltid»; **periodisk tilbakekalle** permanente tillatelser for ubrukte apper med varsel og brukerstyrt frekvens (f.eks. én måned, seks måneder, ett år) eller av; **isolasjon mellom app og SDK-er** slik at en SDK ikke drar nytte av tillatelse gitt bare til appen.

**2. Informasjon og samtykke** (s. 77–78)
- Tillatelsessystemer må teknisk la utgiveren gi relevant informasjon om tillatelsens omfang.
- God praksis: informasjon også under og etter behandling – **visuelle indikatorer** ved sensortilgang (hvilken app), **historikk** over sensoraktivering filtrert per app/systemprosess, indikator i statuslinjen; for de mest inngripende tillatelsene (mikrofon, kamera, lokasjon, filer, kontakter, kalender) **gjenta forespørselen** etter en tid (også for forhåndsinstallerte apper), med brukerstyrt frekvens.
- **Tillatelsesvindu som gyldig samtykke** – bare i begrensede tilfeller, f.eks. tillatelser som gjelder **én behandling, ett formål og én mottaker**. Vinduet må da inneholde: eneste formål; lenker til all lovpålagt informasjon (GDPR art. 13–14, art. 82); hvordan tilgang tilbakekalles. Utvikleren må sikre godt samspill (6.2.3). Utgiveren bør få noe spillerom i informasjonen i tillatelsesforespørselen.
- God praksis: lenke til konkrete eksempler og risiko (f.eks. SMS-tillatelse: legitim henting av engangskode ved flerfaktorautentisering, men også mulighet for at ondsinnet app leser, sender eller endrer SMS). Enkel tilbakekalling/endring.
- **Dataportabilitet**: god praksis også uten behandlingsansvar; **plikt** hvis OS-leverandøren er behandlingsansvarlig; kan omfatte konfigurasjon og installerte apper; «structured, commonly used and machine-readable format» (art. 20).

**3. Mindreårige (art. 8)** (s. 78–79)
- Foreldrekontroll med API/annen ikke-inngripende metode som gir apper **aldersintervall** basert på OS-parametere (satt av foresatte), brukt lokalt uten å gi informasjon til tredjepart eller kreve konto. Hjelper utviklere å fastslå om brukeren er mindreårig og minimerer fjernbehandling. Mindreårig-status kan påvirke tillatelsessvar. Flere biometriske profiler gjør det mulig å skille mindreårig og foresatt, slik at noen handlinger krever foresattes tillatelse.

#### 8.4 Sikker plattform (s. 79–80)

- **Sandkasse**: streng separasjon mellom apper og OS (minne, særlig tillatelser). God praksis: skille **privat og jobb** på samme terminal (separate brukerprofiler; flere avskottede instanser av samme app); **skille app fra tredjepartskode** mht. tillatelser – tillatelse til appen skal ikke automatisk gjelde alle innebygde SDK-er.
- **Tiltak som anses som «state of the art»**: sikker lagring av hemmeligheter (enclave/«Secure Element») når maskinvaren har det; kreve kryptering av nettverksforbindelser, ellers rapportere ukrypterte; tvinge **TLS** eller vise fravær til brukere; moderne kryptofunksjoner for apper; lokale delingsverktøy mellom apper på samme enhet; **kryptere standard sikkerhetskopier** (lokale eller hos tredjepart) med nøkler **kun på terminalen**; formidle beste praksis for sikkerhet med trusseleksempler.
- **Revisjonsverktøy**: god praksis med verktøy for detaljert analyse av nettverkstrafikk, kjørende prosesser og all kommunikasjon, **inkl. til/fra OS-leverandørens servere**; formelle revisjonsmetodikker for utgivere/utviklere til å revidere SDK-er (reduserer informasjonsasymmetri); forenklede **personvernrapporter** til brukere.
- **Sikkerhet over tid**: støtte OS-versjoner så lenge som mulig; god praksis å tilby **sikkerhetsoppdateringer i minst 7 år etter kjøp** av terminalen – at funksjoner ikke lenger er kompatible er ikke grunn til å stanse sikkerhetsoppdateringer (jf. RGESN). Etter utløp: informere brukerne om risiko og ev. vise til alternative, sikre OS.

#### 8.5 Sjekkliste for OS-leverandør (s. 80–83)

(Enkelte ID-er i del 3.2 og 4 var forskjøvet i tekstuttrekket – disse er merket «usikker».)

| ID | Kategori / underkategori | Kontrollpunkt |
|---|---|---|
| 1.1.1 | Egen behandling – ansvarsandel | Ansvarsanalyse som dekker OS-basen, tilførte byggeklosser og behandling apper kan utføre |
| 1.2.1 | Egen behandling – art. 25 | Ingen behandling for OS-leverandøren før gyldig samtykke, også ved første oppstart |
| 1.2.2 | 〃 | Konto er ikke nødvendig for å bruke forhåndsinstallert OS og apper |
| 1.2.3 | 〃 | Tredjeparts varslingsservere kan brukes, optimalisert for bakgrunnsytelse og batteri |
| 1.2.4 | 〃 | Verktøy for kryptering av varselinnhold uavhengig av varslingsserver, med klar dokumentasjon |
| 1.2.5 | 〃 | Krasj-/feilrapportering i tråd med minimering, inkl. samtykke til rapportering |
| 1.2.6 | 〃 | Fjernsikkerhetskopi av OS-innstillinger/innhold er ikke standard, krever samtykke og krypteres med nøkkel OS-leverandøren ikke har |
| 1.2.7 | 〃 | Lokasjon kan begrenses til GPS-sensoren uten videre behandling |
| 2.1.1 | Informere partnere – dokumentasjon | Dokumentasjon for utviklere og sluttbrukere er oppdatert, forståelig, fullstendig, med eksempler |
| 2.1.2 | 〃 | Juridiske elementer med praktiske eksempler finnes i dokumentasjonen |
| 2.1.3 | 〃 | Dokumentene finnes på målgruppenes språk |
| 2.2.1 | Informere – OS-ets behandling | Partnere (utviklere, utgivere, butikker, produsenter) kan kjenne, forstå og dokumentere behandlingen ved bruk av OS-et |
| 2.3.1 | Informere – vernende funksjoner | OS-API-ene er dokumentert for informert valg |
| 2.3.2 | 〃 | Egen dokumentasjon for nye/mer vernende API-er eller API-versjoner |
| 3.1.1 | Rettigheter/samtykke – tillatelser | Tilgang til fysiske sensorer, nettverksutstyr og lagring bare etter brukerens tillatelse |
| 3.1.2 | 〃 | Presisjonsnivå velges av sluttbrukeren, ikke bare av utvikleren |
| 3.1.3 | 〃 | Brukeren kan begrense tillatelser i tid og antall ganger |
| 3.1.4 | 〃 | Brukeren kan velge informasjonsnivå, f.eks. dele deler av kontaktliste/mediebibliotek |
| 3.1.5 | 〃 | Tillatelser tilbakekalles når appen ikke har vært i bruk en tid; brukeren varsles |
| 3.2.1 | Rettigheter/samtykke – informasjon | Tillatelsessystemet lar utgiveren gi relevant informasjon om omfanget |
| 3.2.2 | 〃 | Pågående sensortilgang gir visuelt/lydsignal (fargemerke, lyd, vibrasjon) som viser hvilken app som bruker hvilken sensor |
| 3.2.3 | 〃 | Brukeren har tidsstemplet historikk over sensortilgang per app |
| 3.2.4 | 〃 | Brukeren kan enkelt velge påminnelse/automatisk deaktivering av tillatelser etter en tids ubruk |
| 3.2.6 (usikker) | 〃 | Tillatelser kan enkelt tilbakekalles; menyene er intuitive |
| 3.2.7 (usikker) | 〃 | OS-et tilbyr dataportabilitet slik at brukeren kan flytte data og konfigurasjon til annet OS eller samme OS på ny terminal |
| 3.3.1 | Rettigheter – mindreårige | Foreldrekontroll er tilgjengelig for sluttbrukere |
| 3.3.2 | 〃 | Verktøyene gir utviklere et mindreårig-signal slik at bruk kan begrenses/blokkeres etter alder kjent av OS-et |
| 4.1.1 | Sikker plattform – sandkasse | Sandkasse begrenser og kontrollerer interaksjoner, minnetilgang og tillatelsesbruk mellom OS og apper |
| 4.1.2 | 〃 | Teknisk og grensesnittmessig skille mellom privat og jobb på samme terminal |
| 4.1.3 | 〃 | Lokal lagring av hemmeligheter bruker dedikert maskinvare (enclave/Secure Element) når mulig |
| 4.1.4 | 〃 | Tekniske/grensesnittkrav til nettverksforbindelser (rapportere ukryptert, utdaterte sertifikater, tvinge TLS) |
| 4.1.5 | 〃 | Lokale delingssystemer mellom apper (f.eks. API) uten overføring til eksterne servere |
| 4.1.6 | 〃 | Sikkerhetskopier krypteres som standard med nøkkel kun under brukerens kontroll |
| 4.1.x (usikker; trykt «4.1.1») | 〃 | God sikkerhetspraksis for design og utvikling formidles til tredjepartsutviklere |
| 4.2.x (usikker; trykt «4.2.2») | Sikker plattform – revisjonsverktøy | Dokumentasjon av revisjonsverktøy og -metodikk gjøres tilgjengelig |
| 4.3.1 | Sikker plattform – over tid | Hver OS-versjon støttes så lenge som mulig |
| 4.3.2 | 〃 | Sikkerhetsoppdateringer så lenge som mulig, minst 7 år, uavhengig av funksjonelle oppdateringer |
| 4.3.3 | 〃 | Ved end-of-life gis klar informasjon til utviklere og sluttbrukere |

### 9. Anbefalinger til app-butikkleverandøren (s. 84–91)

App-butikkleverandør: den som utvikler og vedlikeholder en butikk (en app som indekserer, fremhever og muliggjør nedlasting av andre apper); kan være kommersiell eller ikke, ev. knyttet til produsent, utgiver eller OS-leverandør. Butikken som app følger utgiverkapitlet. Butikken er normalt ikke ansvarlig for behandlingen i appene, men påvirker hvilke apper folk velger; den bør derfor ha en **reléfunksjon** for informasjon og legge til rette for etterlevelse. Kapitlet er i hovedsak god praksis, uten forbehold for konkurranserett (s. 84–85).

#### 9.1 Analysere innsendte apper (s. 85–86)

- **Innhente etterlevelsesdata** fra utgiver (s. 85): kategorier av data og formål per behandling; tredjeparter med (mulig) tilgang, **inkl. liste over SDK-leverandører**; **uttømmende liste over systemtillatelser** med obligatorisk/valgfri karakter og formål slik de vises brukeren; ev. **tredjeland** for lagring/behandling; **oppdateringshistorikk** med oppdateringsnotater. Foreslått også: kontaktpunkt for personvern og personvernerklæring; angivelse av om appen retter seg **utelukkende, hovedsakelig eller potensielt mot mindreårige**.
- Ingen av disse opplysningene er **konfidensielle** – de skal uansett gis etter GDPR art. 13–14 – og portvoktere kan ikke bruke dem i konkurranse med forretningsbrukere (DMA art. 6 nr. 2). Bør være mest mulig oppdatert.
- **Fremme god praksis** (s. 85–86): oppfordre til **runtime-tillatelser** fremfor blokkerende installasjonstillatelser – ev. kun slippe inn apper med **kontekstuelle tillatelsesforespørsler**; motivere til å unngå for brede eller utdaterte OS-API-er; oppfordre til informative **oppdateringsnotater** (sikkerhetsrettinger, ny behandling) slik at brukeren kan velge informert.
- **Sårbarhetsanalyse** (s. 86): **statisk analyse** før hver publisering/oppdatering, automatisk og manuell (særlig over et visst antall nedlastinger eller ved særlig inngripende tillatelser); **dynamisk analyse** for de mest sensitive appene – f.eks. dynamisk lasting av biblioteker i etterkant, bakgrunnsaktivitet (batteri), atferd kjent fra ondsinnede apper (litteratur, fagpresse, CVE).

#### 9.2 Transparente gjennomgangsprosesser (s. 86–88)

- Maksimal åpenhet, kommunikasjon på utgivernes språk. Ved konkurranserett/DMA: når én enhet har flere roller, må verifisering **ikke være mer komplisert for tredjepartsapper enn for egne apper** (s. 86).
- **Grunnleggende personvernkontroll** (s. 86–87): for apper rettet mot EU-markedet kan utgiver spørres om appen behandler personopplysninger; i så fall bør butikken kontrollere at informasjonen til brukerne inneholder: identitet og kontaktinfo for behandlingsansvarlig og ev. representant (art. 13/14 nr. 1 bokstav a); formål og behandlingsgrunnlag (bokstav c); lagringstid (nr. 2 bokstav a); avhengig av grunnlag, hvordan rettigheter utøves (nr. 2 bokstav b); rett til å klage til tilsynsmyndighet (nr. 2 bokstav d). Kan f.eks. fylles inn i et skjema. **CNIL oppfordrer butikker til å avvise** apper rettet mot EU-markedet som behandler personopplysninger og ikke kan gi disse elementene. God praksis: generell påminnelse om regelverket.
  - **[Merknad – ikke fra kilden]** Bokstavhenvisningene i nr. 2 passer for art. 13. I art. 14 står tilsvarende opplysninger i nr. 2 bokstav c (rettighetene) og nr. 2 bokstav e (klagerett) (jf. [K43](K43-gdpr-kap03-den-registrertes-rettigheter.md#art-14)).
- **Tydelige forventninger** (innenfor DMA art. 6 nr. 12 – rettferdige, rimelige og ikke-diskriminerende vilkår): fullstendig dokumentasjon av krav; konkrete eksempler på problematisk atferd og løsninger; presis beskrivelse av valideringsprosess, steg og tidsfrister, inkl. utbedring ved avslag; proaktiv varsling av regelendringer med rimelig frist, og eksempler på utbedring hvis tidligere aksepterte løsninger nå avvises.
- **Verktøy** (s. 87–88): finkornet tilgangsstyring til utgiverkontoer (separat tilgang til kodelager, versjonssignaturer, oppdateringsnotater, brukerinformasjon); identifiserbar kommunikasjonskanal, helst i publiseringsplattformen; ved avslag/suspensjon: varsle utgiver raskt ved oppdaget sikkerhetsbrudd (særlig hvis det kan føre til deaktivering eller varsling av brukere), transparent kommunikasjon, begrunnelse og klageadgang, generelle tilgangsvilkår med **utenrettslig tvisteløsning** (DMA art. 6 nr. 12).

#### 9.3 Informere brukere og rapporteringsverktøy (s. 88–89)

- Gi brukeren all informasjon fra 9.1 – inkl. **liste over tredjeparts-SDK-er** per app – helst før kjøp/installasjon; bruk ikoner og tabeller som fremhever det mest personvernrelevante; informasjon om **kommersiell bruk av personopplysninger** før avtaleinngåelse (fransk forbrukerlov L. 221-5 / forbrukerrettighetsdirektivet 2011/83) direkte på appsiden; nøytral og kontekstualisert presentasjon.
- Søkegrensesnitt (god praksis): **personvernfiltre** (tillatelser, datainnsamling, ev. personvern-«score»). En score bør ha metodikk fastsatt på forhånd og transparent av en **tredjepart** (helst omforent i økosystemet og med sivilsamfunnet), beregning av tredjepart eller tredjepartssertifisert, kildedata i åpent format; DMA art. 6 nr. 5 – portvokter skal ikke favorisere egne tjenester i rangering; apper fra aktører som også leverer OS/SDK skal følge samme regler.
- **Rapportering** (s. 88–89): DSA art. 16 krever varslingsmekanisme for ulovlig innhold hos vertstjenester, inkl. app-butikker. CNIL **anbefaler** at mekanismen også omfatter mulige GDPR-brudd som kan være ulovlig innhold etter DSA art. 3 bokstav h (f.eks. rettigheter ikke oppfylt, samtykkebrudd inkl. villedende design/dark patterns – unntatt det som dekkes av DSA art. 25 – SDK-funksjoner kjørt uten forhåndssamtykke, uregulerte overføringer). God praksis: bruke rapportene til å styre kontroller.
- **Sårbarheter** (s. 89): protokoll ved sårbarheter i utbredte apper/SDK-er; analyser (inkl. statisk) for å finne berørte apper; tiltak: **suspendere automatiske oppdateringer** for hele/deler av brukermassen; **midlertidig fjerne sårbare apper** til oppdatering består sikkerhetstesten; ved høy risiko vurdere **systemvarsel** til brukere om sårbare apper.

#### 9.4 Sjekkliste for app-butikk (s. 89–91)

| ID | Kategori / underkategori | Kontrollpunkt |
|---|---|---|
| 1.1.1 | Analysere apper – etterlevelsesdata | Opplysninger om behandling, tillatelser og tredjeparter med tilgang kreves ved gjennomgang |
| 1.1.2 | 〃 | Personvernerklæring og kontaktpunkt er definert og tilgjengelig for hver utgiver med minst én publisert app |
| 1.1.3 | 〃 | Apper rettet utelukkende, hovedsakelig eller potensielt mot mindreårige er merket på appsiden |
| 1.2.1 | Analysere – god praksis | Utgivere rådes til ikke å be om tillatelser i bulk ved installasjon og oppfordres til runtime-tillatelser |
| 1.2.2 | 〃 | Utgivere kan oppfordres til å unngå for brede eller utdaterte OS-API-er |
| 1.2.3 | 〃 | Utgivere oppfordres til informative oppdateringsnotater |
| 1.3.1 | Analysere – sårbarheter | Statisk analyse av hver ny app/versjon før publisering |
| 1.3.2 | 〃 | Dynamisk analyse av mer sensitive apper for å avdekke unormal atferd |
| 2.1.1 | Gjennomgangsprosess – personvernkontroll | Ved behandling av personopplysninger kontrolleres at brukerinformasjonen inneholder: behandlingsansvarliges identitet og kontaktinfo; formål og behandlingsgrunnlag; lagringstid; etter grunnlag, hvordan rettigheter utøves; retten til å klage til tilsynsmyndighet |
| 2.1.2 | 〃 | Apper rettet mot EU-markedet som ikke kan gi disse elementene, publiseres ikke |
| 2.2.1 | Gjennomgangsprosess – forventninger | Utgivere er godt informert om etterlevelseskravene i butikkens kriterier, og om endringer over tid |
| 2.3.1 | Gjennomgangsprosess – verktøy | Finkornet tilgangsstyring til utgiverkontoer (kodelager, versjonssignaturer, oppdateringsnotater) |
| 2.3.2 | 〃 | Tydelig kommunikasjonskanal mellom utgivere og butikk, helst innebygd i butikken |
| 2.3.3 | 〃 | Avslag, nødvendige korrigerende tiltak og klageadgang angis tydelig og bygger på relevant dokumentasjon |
| 3.1.1 | Informere brukere – etterlevelsesdata | All personvernrelatert informasjon fra utgivere eller kjent for butikken er tilgjengelig før kjøp/nedlasting |
| 3.1.2 | 〃 | Informasjon vises i format egnet for systemet den leses i |
| 3.1.3 | 〃 | Personvernfiltre finnes blant søkevalgene |
| 3.2.1 | Informere brukere – rapportering | Sluttbrukere kan rapportere apper som ikke oppfyller pliktene, direkte fra butikken |
| 3.3.1 | Informere brukere – sårbarheter | Protokoll for tiltak når statisk/dynamisk analyse avdekker sårbarhet i publisert app |
| 3.3.2 | 〃 | Egen visning på appsiden om potensiell sikkerhetsrisiko |

### 10. Ordliste (s. 92–93)

| Begrep | Definisjon i kilden (kortfattet) |
|---|---|
| Mobilapplikasjon | Programvare distribuert i smarttelefon/nettbrettmiljø, kjørt isolert (sandkasse) av et OS som begrenser funksjoner via tillatelser |
| SDK | Utviklingsverktøy; kode lagt inn i appen som kobler mot leverandørens infrastruktur; vanligst publikumsanalyse, annonseutvelgelse/-levering, e-handel |
| Sandkasse (sandboxing) | Sikkerhetsmekanisme som isolerer en app fra OS-kjernen og andre apper; begrenset standardfunksjonalitet, kun OS-API-er med brukerens tillatelse |
| API | Programvaregrensesnitt for utveksling av data og funksjoner; i mobil er det måten OS eksponerer funksjoner på |
| Operativsystem (OS) | Programvarelaget nærmest maskinvaren; definerer interaksjoner mellom bruker, terminal og apper; implementerer sandkasse og tillatelsessystem |
| Tilgangstillatelse (access permission) | OS-mekanisme der brukeren velger hvilke funksjoner apper får tilgang til. **Tekniske tillatelser** gir/blokkerer tilgang til ressurser uavhengig av formål; **andre tillatelser** godkjenner/avslår handlinger for et bestemt formål |
| Publikumsmåling (analytics) | Fra enkle, ofte uunnværlige målinger til komplekse verktøy (A/B-tester, varmekart, «session replay»). Noen kommersielle verktøy (trafikkilder, målrettet reklame) presenteres feilaktig som publikumsmåling |
| Reklame-ID | Digital identifikator generert av OS og knyttet til terminalen, tilgjengelig for apper under visse vilkår; laget for at én bruker skal kunne identifiseres av ulike apper (umulig ellers pga. sandkasse); muliggjør reklamemålretting, f.eks. ved at sosiale mediers målrettingsmodul i tredjepartsapper bruker profildata |
| Geolokalisering | Bestemmelse av posisjon som koordinater, via GPS eller kommunikasjonsgrensesnitt, med varierende presisjon; del av bredere lokasjonsteknikker (f.eks. bare tettsted) |

## Praktiske sjekkpunkter

**Rolleavklaring (for DPA og DPIA)**
- Kontroller at rollen er vurdert **per behandling** (ikke per leverandør) og at begrunnelsen er dokumentert (hvem opprettet behandlingen, formål, data, lagringstid, sikkerhet) – og tatt inn i DPIA (s. 17).
- Kontroller at kontraktens rollebetegnelse samsvarer med faktisk rolle; tilsynet er ikke bundet av kontrakten (s. 17).
- For hver SDK: skill mellom (a) lese-/skriveoperasjonen på terminalen, (b) behandling på utgiverens vegne og (c) SDK-leverandørens behandling for egne formål. (a) kan være felles behandlingsansvar, (b) databehandling, (c) selvstendig behandlingsansvar – og (c) er bare tillatt når utgiveren er informert og det er regulert i kontrakt (s. 18, 20, 22).
- Kontroller at utgiveren har regulert i kontrakt også den innsamlingen tredjeparter gjør via appen for egne formål, selv om utgiveren ikke er ansvarlig for den etterfølgende behandlingen (s. 18).
- Kontroller om ekstern utvikler har driftsoppgaver (infrastruktur, vedlikehold på servere) → databehandler med databehandleravtale; ren kodelevering → ingen GDPR-rolle, men kontrakten bør kreve innebygd personvern (s. 19).
- Ved avbrutt utviklingsprosjekt: kontroller at utgiveren uttrykkelig har motsatt seg publisering (C-683/21) (s. 33).

**Databehandleravtale med SDK-leverandør / utvikler – innhold å kreve**
- Dokumentasjon av alle behandlinger og data per konfigurasjon (gjerne dynamisk protokoll i regneark) med formål og behandlingsgrunnlag (s. 53, 64).
- Liste over lese-/skriveoperasjoner, tilknyttede tillatelser, formål, og teknisk middel for å blokkere/aktivere hver; hvilke SDK-versjoner som gjør hva (s. 64).
- Opplysning om tredjelandsoverføringer (s. 53, 61).
- Teknisk mulighet til å blokkere/suspendere SDK-en til samtykke foreligger, granulært per formål, og ingen samtykkepliktig lesing ved første oppstart (s. 54, 66).
- Støtte for tilbaketrekking uten ustabilitet eller gjentatte forespørsler (s. 54, 66).
- API-er for rettighetsforespørsler med færrest mulig ekstra identifikatorer (s. 53, 65).
- Revisjonsrett og tilgjengelige revisjonsrapporter; samarbeid om nettverksbasert revisjon (s. 54, 67).
- Fjerndeaktivering av SDK-en i produksjon (s. 67).
- Varsling om sikkerhetsbrudd/sårbarheter i tide for 72-timersfristen (s. 36, 67).
- Forhåndsvarsling og (for databehandler) forhåndsgodkjenning av endringer med personvernbetydning (s. 63).
- Underdatabehandlere / innebygde SDK-er («russiske dukker») med samme garantinivå, og forhåndsgodkjenning (s. 53, 63).
- Kontraktsfesting av påstått samtykkeinnhenting på utgiverens vegne, med revisjonsmulighet (s. 54).
- For utvikler: klare instrukser, kontaktpunkt, akseptansetest, sikkerhetskrav (TLS, nøkkellagring, kryptert backup, OWASP MASVS L1), oppdateringsplikt ved sårbarhet, skriftlig godkjenning av personvernrelevante valg (s. 33, 36, 45–46, 55).

**Samtykke og tillatelser**
- Kontroller at alle lese-/skriveoperasjoner (reklame-ID, fingeravtrykk, maskinvare-ID, sensorer, kontakter, bilder) er kartlagt og vurdert mot unntakene (kommunikasjon / strengt nødvendig for etterspurt tjeneste) (s. 29–30).
- Kontroller at OS-tillatelse ikke behandles som samtykke for SDK-formål eller andre formål enn den ble gitt for (s. 52, 66).
- Kontroller at OS-mekanismer for formålsspesifikk godkjenning bare brukes som samtykke når de oppfyller GDPR-kravene; ellers CMP – og at valg i CMP og tillatelse ikke kan avvike for samme formål (s. 52).
- Kontroller at CMP finnes for alle formål som ikke dekkes av tillatelser (s. 52).
- Kontroller at samtykkegrensesnittet har «godta alle», «avvis alle» og «tilpass» på første nivå, og er tilgjengelig (s. 50–51).
- Kontroller med testbenk/nettverksavlytting at ingen sporing skjer før samtykke (s. 36, 54).
- Kontroller at runtime-tillatelser brukes fremfor install-time (s. 49, 66).

**Minimering og innebygd personvern**
- Kontroller at minst inngripende tillatelse er valgt (omtrentlig, engangs, forgrunn, kun GPS; les i stedet for skriv; utvalgte bilder i stedet for hele galleriet) (s. 39–41).
- Kontroller at manuell inntasting tilbys som alternativ der mulig, og at data behandles lokalt der mulig (s. 30–31, 39).
- Kontroller at presisjonen reduseres før data sendes til server, og at lokasjon/lyd/bilder ikke lagres på server uten begrunnet behov; serverbackup valgfri og ikke standard (s. 39–41).
- Kontroller at varselinnhold og sikkerhetskopier ikke eksponerer data for OS-leverandør (s. 48, 55).
- Kontroller at identifikatorer på tvers av apper ikke sendes til SDK-er (ev. hashet) (s. 48).
- Kontroller at sensitive data er arkitektonisk atskilt og utilgjengelige for SDK-er, og at de ikke brukes til reklameprofilering (DSA art. 26) eller at mindreårige ikke får profileringsbasert reklame (DSA art. 28) (s. 31, 49).

**Informasjon og rettigheter**
- Kontroller at personvernerklæringen er tilgjengelig før nedlasting og i appen, med liste over tillatelser, formål og om de er obligatoriske (s. 34).
- Kontroller at mottakere for monetisering er opplyst, med antall og bransje (s. 34, 65).
- Kontroller at det finnes et rettighetssenter i appen som også dekker SDK-enes behandling (s. 35, 48).

**Sikkerhet og livssyklus**
- Kontroller CI/CD, kodegjennomgang, supply-chain-overvåking, oppdaterte avhengigheter, separate sikkerhetsoppdateringer, mulighet for tvungen oppdatering (s. 36, 55–56).
- Kontroller at sikkerhetsmodellen ikke hviler på terminalintegritet, certificate pinning eller obfuskering (s. 55).
- Kontroller at protokoll, DPIA og personvernerklæring oppdateres ved endringer, og at det finnes godkjenningsprosess for nye SDK-er/funksjoner (s. 37).

## Viktige sitater

- «For its users, the smartphone, a personal terminal by definition, falls within the private and intimate sphere.» (s. 4)
- «The supervisory authorities are not bound by the qualifications chosen by the parties, in particular within the contracts» (s. 17)
- «On the other hand, the publisher is not responsible for the processing carried out by third parties on their own account on personal data resulting from storing and/or acessing operations that they carry out through the application.» (s. 18)
- «as a controller, the publisher will assume at least co-responsibility for the use of tracking devices by an SDK included in its application.» (s. 33)
- «the request for permission does not necessarily lead to a valid consent under the GDPR or Article 82 of the French Data Protection Act.» (s. 51)
- «In any event, a CMP will be required to collect consent for purposes not covered by permission.» (s. 52)
- «Attention should be paid to the `Russian dolls' effect: where the integration of one SDK involves the integration of other SDKs» (s. 53)
- «if permission is granted to the application for a purpose other than that of the SDK, that permission cannot be regarded as valid consent of the data subject.» (s. 66)
- «The collection of personal data by the SDK must never be carried out without the knowledge of the data subjects.» (s. 61)
- «The CNIL considers it a good practice to systematically offer OS security updates at least up to 7 years after the purchase of the terminal.» (s. 80)

## Kryssreferanser

- GDPR: art. 2 nr. 2 bokstav c og fortalepunkt 18 (husholdningsunntaket); art. 3 (territorielt virkeområde); art. 4 nr. 7 og 8 (behandlingsansvarlig/databehandler); art. 5 (prinsipper); art. 6 nr. 1 og nr. 4 (behandlingsgrunnlag, forenlighet); art. 7 (samtykke); art. 8 (barn); art. 9 (særlige kategorier); art. 11; art. 12–14 (informasjon); art. 15–22 (rettigheter); art. 24, 25 (ansvar, innebygd personvern); art. 26 (felles behandlingsansvar); art. 28 (databehandler, særlig nr. 2, 3 bokstav a, c, e, f, h og nr. 4); art. 30 (protokoll); art. 32–34 (sikkerhet, avvik); art. 35–36 (DPIA); kap. V (overføring).
- Annet regelverk i kilden: ePrivacy-direktivet 2002/58/EF art. 5(3) / fransk personvernlov art. 82; DSA (forordning 2022/2065) art. 3 bokstav h, 16, 25, 26, 28; DMA (forordning 2022/1925) art. 6 nr. 2, 5 og 12; forbrukerrettighetsdirektivet 2011/83/EU.
- Rettspraksis i kilden: EU-domstolen C-683/21 (5.12.2023, Nacionalinis visuomenės sveikatos centras), C-604/22 (7.3.2024, IAB Europe); Conseil d'État nr. 412589 (Éditions Croque Futur); EDPB bindende beslutning 1/2021 (WhatsApp); CNIL SAN-2022-025, SAN-2022-026, SAN-2021-013, SAN-2023-006, SAN-2019-001.
- Andre kilder:
  - [K01](K01-dt-behandlingsansvarlig-og-databehandler.md) – generell rolleavklaring; supplerer kap. 4.
  - [K05](K05-dt-databehandleravtale.md) – innhold i databehandleravtale; brukes sammen med SDK-/utviklerkravene her.
  - [K02](K02-dt-behandlingsgrunnlag.md) – behandlingsgrunnlag (avtale, berettiget interesse).
  - [K25](K25-wp259-samtykke.md) – samtykkekrav (fritt, spesifikt, informert, utvetydig, tilbaketrekking).
  - [K26](K26-wp260-apenhet.md) – lagdelt og kontekstuell informasjon.
  - [K13](K13-dt-innebygd-personvern.md) – art. 25.
  - [K12](K12-dt-dpia-veiledning.md), [K20](K20-dt-dpia-liste.md), [K24](K24-wp248-dpia.md) – når DPIA kreves og hvordan.
  - [K31](K31-cnil-pia-tilkoblede-objekter.md) – CNILs PIA for tilkoblede objekter; overlapp med «lignende miljøer» (IoT).
  - [K14](K14-dt-overforing-utenfor-eos.md), [K38](K38-tia-guide.md) – overføring utenfor EØS via SDK-/OS-tjenester.
  - [K33](K33-cnil-sikkerhetsguide.md), [K10](K10-dt-kryptering.md) – sikkerhetstiltak og kryptering.
  - [K07](K07-dt-legge-til-rette-for-rettigheter.md), [K08](K08-dt-retting-og-sletting.md) – rettighetsutøvelse.

## Aktualitet og begrensninger

- Versjonen er publisert **8. april 2025** (deliberation 2025-024 av 27.03.2025), som endrer anbefalingen og opphever deliberation 2024-061 av 18.07.2024. Engelsk «courtesy translation» – bare fransk versjon er rettslig bindende (s. 1).
- Anbefalingen er en **fransk** tilsynsmyndighets tolkning; den viser til fransk personvernlov art. 82, fransk forbrukerlov og franske avgjørelser. GDPR-delene er felles for EØS, men ePrivacy-delene må leses mot nasjonal gjennomføring.
- Kilden skiller mellom «må» (plikt), «anbefaler» og «god praksis». Kapitlene om OS-leverandører og app-butikker er i stor grad god praksis, ikke rettslige krav.
- Mindreårige er bare behandlet kort; kilden viser til CNILs eget arbeid (s. 31).
- Eksemplene på roller er illustrative; kvalifiseringen skal skje konkret (s. 17).
- Infografikken på s. 52 om samspill mellom CMP og tekniske tillatelser og figurene på s. 50–51 var ikke fullt lesbare i tekstuttrekket; innholdet er gjengitt ut fra omkringliggende tekst og figurtekster. Enkelte sjekkliste-ID-er var forskjøvet i uttrekket (merket «usikker»/«trolig» over).
- **[Merknad – ikke fra kilden]** I Norge gjelder ePrivacy-regelen om lagring av og tilgang til informasjon i brukerens terminalutstyr i ekomloven § 3-15 (ny ekomlov 2024, i kraft 1.1.2025; tidligere § 2-7 b), med Nkom som tilsynsmyndighet. Norsk praksis aksepterte tidligere samtykke via nettleserinnstillinger. Etter § 3-15 første ledd skal samtykket nå «oppfylle kravene til samtykke i personvernforordningen». Unntak gjelder blant annet for lagring eller tilgang som er «strengt nødvendig» for en tjeneste brukeren uttrykkelig har bedt om (annet ledd bokstav b). Lovteksten står i [K44](K44-ekomloven-3-15.md).
- **[Merknad – ikke fra kilden]** DSA og DMA er EØS-relevante, men innlemmingen i EØS-avtalen og norsk gjennomføring bør kontrolleres før kildens henvisninger til DSA art. 26/28 og DMA brukes som rettslige krav i Norge.

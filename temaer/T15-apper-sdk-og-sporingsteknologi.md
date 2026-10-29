---
id: T15
tittel: "Apper, SDK-er og sporingsteknologi"
gdpr_artikler: [2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 20, 21, 24, 25, 26, 28, 30, 32, 33, 35]
kilder: [K39, K25, K26, K33, K09, K13, K01, K05, K14, K31]
---

# Apper, SDK-er og sporingsteknologi

## Kjerneregler (kort svar)

1. **To regelsett gjelder parallelt:** ePrivacy-regelen om lagring av/tilgang til informasjon i terminalutstyret (uansett om det er personopplysninger), og GDPR for den etterfølgende behandlingen [K39 s. 10–11]. I Norge: ekomloven § 3-15 (Nkom, lovtekst i [K44](../kilder/K44-ekomloven-3-15.md)) og GDPR (Datatilsynet).
2. **Forhåndssamtykke kreves** for lese-/skriveoperasjoner på terminalen (reklame-ID, fingeravtrykk, maskinvare-ID, sensorer, kontakter, bilder), med mindre operasjonen utelukkende er for å overføre kommunikasjon eller er strengt nødvendig for en tjeneste brukeren uttrykkelig har bedt om [K39 s. 11, 30].
3. **OS-tillatelse er ikke det samme som samtykke.** En tillatelse gitt for ett formål er ikke samtykke til en SDKs behandling for andre formål; en CMP trengs for formål som ikke dekkes av tillatelsen [K39 s. 51–52, 66].
4. **Roller vurderes per behandling:** utgiveren er behandlingsansvarlig og **minst felles ansvarlig** for sporing utført av SDK-er i appen; SDK-leverandører kan samtidig være databehandler, felles ansvarlig og selvstendig behandlingsansvarlig [K39 s. 17–22, 33]. Se [T01](T01-roller-behandlingsansvarlig-databehandler.md).
5. **Kontraktsregulering av hver SDK** er nødvendig – DPA der SDK-leverandøren er databehandler, og regulering også av innsamling SDK-leverandøren gjør for egne formål [K39 s. 18, 52–53].
6. **Dataminimering via tillatelser:** omtrentlig fremfor presis, engangs fremfor permanent, forgrunn fremfor alltid, lokal behandling, manuell inntasting som alternativ, redusert presisjon før sending [K39 s. 38–41].
7. **Informasjon før nedlasting og i appen**, maks «to trykk» unna, kontekstuell informasjon ved hver innsamling og liste over tillatelser [K26 avsn. 11; K39 s. 34].
8. **Sikkerhet:** TLS, maskinvarebeskyttet nøkkellagring, kryptert/deaktivert OS-backup, OWASP MASVS L1, oppdateringsprosess og forsyningskjedesikkerhet [K39 s. 55–56; K33 ark 23].
9. **Husholdningsunntaket:** apper som behandler kun lokalt på brukerens initiativ og i et avskottet miljø kan falle utenfor GDPR for leverandøren – CNIL anbefaler dette som design [K39 s. 12–15].

## Rettslig grunnlag

- **ePrivacy-direktivet 2002/58/EF art. 5 nr. 3** – i Frankrike gjennomført i personvernloven art. 82 [K39 s. 10]. **[Merknad – ikke fra kildene, gjengitt fra merknad i K39]** I Norge: ekomloven (lov 13. desember 2024 nr. 76) § 3-15, tidligere ekomloven 2003 § 2-7 b; Nkom fører tilsyn. Samtykket skal «oppfylle kravene til samtykke i personvernforordningen» (§ 3-15 første ledd). Unntak gjelder for ren overføring av kommunikasjon og for det som er «strengt nødvendig» for en tjeneste brukeren uttrykkelig har bedt om (annet ledd). Lovtekst: [K44](../kilder/K44-ekomloven-3-15.md).
- **GDPR:** [art. 2](../kilder/K43-gdpr-kap01-alminnelige-bestemmelser.md#art-2) nr. 2 c og [fortalepunkt 18](../kilder/K43-gdpr-fortale.md#fp-18) (husholdningsunntaket), [art. 3](../kilder/K43-gdpr-kap01-alminnelige-bestemmelser.md#art-3) (territorielt virkeområde), [art. 4](../kilder/K43-gdpr-kap01-alminnelige-bestemmelser.md#art-4) nr. 7–8, art. 5, 6, [7](../kilder/K43-gdpr-kap02-prinsipper.md#art-7), [8](../kilder/K43-gdpr-kap02-prinsipper.md#art-8), 9, 12–22, 24–[26](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-26), [28](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-28), 30, 32–35 [K39]. Aldersgrensen for barns samtykke til informasjonssamfunnstjenester (art. 8 nr. 1) er 13 år i Norge ([popplyl. § 5](../kilder/K42-personopplysningsloven.md#p5)).
- **Samtykke:** WP259 [K25] / EDPB Guidelines 05/2020 (se [T02](T02-behandlingsgrunnlag-og-samtykke.md)). Samtykke etter ePrivacy bruker GDPRs samtykkebegrep [K25 s. 4].
- **Annet regelverk nevnt i K39:** DSA art. 26 (forbud mot reklame basert på profilering med særlige kategorier) og art. 28 (forbud mot profileringsbasert reklame til mindreårige), DMA [K39 s. 31]. **[Merknad – fra kildenotatet K39]** EØS-innlemmelse og norsk gjennomføring av DSA/DMA må kontrolleres før de brukes som rettslige krav i Norge.
- **[Merknad – ikke fra kildene]** EDPB Guidelines 2/2023 om det tekniske virkeområdet til ePrivacy art. 5 nr. 3 gir utfyllende tolkning av hva som er «tilgang» og «lagring» (bl.a. piksler, URL-sporing, IoT); verifiser før sitering.

## Utdyping

### 1. Aktørene og deres roller

| Aktør | Typisk rolle | Kilde |
|---|---|---|
| App-utgiver | Behandlingsansvarlig for appens behandling og for lese-/skriveoperasjoner den eller tredjeparter utfører på dens vegne; minst felles ansvarlig for SDK-sporing; ikke ansvarlig for tredjeparters etterfølgende behandling for egen regning (men må regulere innsamlingen i kontrakt) | [K39 s. 17–18, 33] |
| Apputvikler | Ingen rolle ved ren kodelevering; databehandler ved drift/vedlikehold; unntaksvis behandlingsansvarlig ved egne formål | [K39 s. 18–19] |
| SDK-leverandør | Databehandler (behandling kun for utgiver); felles ansvarlig (lese-/skriveoperasjoner for egne formål); behandlingsansvarlig (etterfølgende behandling for egne formål); underdatabehandler (når utvikleren er databehandler) | [K39 s. 19–20] |
| OS-leverandør | Behandlingsansvarlig for egne formål (telemetri, oppdateringer, lokasjonstjenester) | [K39 s. 20–21] |
| App-butikk | Publiseringsregler er ikke behandling; behandlingsansvarlig for egne formål | [K39 s. 21] |

Eksempeltabeller med rollefordeling per behandling (reklame-ID, lokasjon, kontaktliste) finnes i [K39 s. 21–25] og er gjengitt i [T01](T01-roller-behandlingsansvarlig-databehandler.md) avsnitt 7.

### 2. Når kreves samtykke for lesing/skriving på terminalen?

| Hovedregel: samtykke | Unntak 1: kun kommunikasjon | Unntak 2: strengt nødvendig for uttrykkelig etterspurt tjeneste |
|---|---|---|
| Reklame-ID for reklame; kontakter for kontaktoppdagelse; lokasjon for innholdsanbefaling | Identifikatorer for lastbalansering eller ruting | (a) Funksjon brukeren ber om (GPS for lokasjonsfunksjon; autentiseringsidentifikatorer); (b) sikkerhet som beskytter brukeren (mot DoS, credential stuffing); (c) begrenset publikumsmåling (enkel telling av daglige brukere for dimensjonering) |

Kilde: [K39 s. 30].

**Mobile identifikatorer** [K39 s. 10–11]: reklame-ID (IDFA/IDFV hos Apple, AAID hos Google) er lik for alle tredjeparter og letter kobling på tvers av apper og enheter; kontoknyttede identifikatorer (f.eks. UDID) brukes av OS-leverandøren. Fingeravtrykk (fingerprinting) regnes også som lese-/skriveoperasjon.

Den etterfølgende behandlingen krever i tillegg behandlingsgrunnlag etter GDPR [K39 s. 11]. Berettiget interesse er vanskelig å bruke for inngripende sporing og profilering for markedsføring [K39 s. 28–29].

### 3. Samtykke i apper – krav

- Alle GDPR-vilkår gjelder: frivillig, spesifikt, informert, utvetydig, før behandling, dokumenterbart, enkel tilbaketrekking [K25; K39 s. 34–35]. Se [T02](T02-behandlingsgrunnlag-og-samtykke.md).
- **Grensesnitt:** formålsdetaljer på første nivå (rulleknapp eller lenke), og granulære valg via «tilpass mine valg» på **samme nivå** som «godta alle» og «avvis alle» [K39 s. 50–51].
- **Kontekstuell samtykkeinnhenting** knyttet til handlinger reduserer samtykketretthet (god praksis) [K39 s. 51].
- **Tillatelse vs. samtykke** [K39 s. 51–52, 66, 77]:
  - En tillatelse gir teknisk tilgang, men er ikke nødvendigvis gyldig samtykke.
  - OS-mekanismer for formålsspesifikk godkjenning er bare gyldig samtykke når de oppfyller GDPR-kravene (formål, identiteten til aktørene som bygger på samtykket, like lett å avslå/trekke tilbake). **[Merknad – ikke fra kildene]** Apples App Tracking Transparency er et eksempel (jf. merknad i K39).
  - Brukes både CMP og tillatelse for samme formål, er samtykket bare gyldig hvis valgene er samstemte.
  - Et tillatelsesvindu kan bare være gyldig samtykke i begrensede tilfeller: én behandling, ett formål, én mottaker, med lenker til lovpålagt informasjon og tilbakekalling.
- **Testing:** testbenk/emulator med nettverksavlytting for å kontrollere at ingen sporingsforespørsler skjer før samtykke [K39 s. 36, 54].
- **Barn:** reklame basert på profilering er forbudt overfor mindreårige (DSA art. 28); ekstra tiltak kreves [K39 s. 31]. Norsk aldersgrense for samtykke til informasjonssamfunnstjenester: 13 år [K02 s. 4] ([popplyl. § 5](../kilder/K42-personopplysningsloven.md#p5)).

### 4. Tillatelser og innebygd personvern

**Prosess for valg av tillatelse** [K39 s. 38]:
1. Identifiser formålet og nødvendige data.
2. Velg tillatelsen med minst ekstra innsamling.
3. Ikke obligatorisk for appens funksjon → gjør tilgangen valgfri.
4. Finnes alternativ (f.eks. manuell inntasting) → tilby det.
5. Kan dataene behandles lokalt → gjør det.
6. Ellers: innhent gyldig samtykke der påkrevd.
7. Reduser inngrep (presisjon, varighet) før implementering.

| Ressurs | Hovedanbefalinger | Kilde |
|---|---|---|
| Lokasjon | Omtrentlig, engangs, forgrunn, kun GPS; avkort koordinater lokalt før sending; ikke lagre på server; manuell postnummer som alternativ | [K39 s. 39] |
| Kontakter | Kun lesing; velg kontakt lokalt; kontaktoppdagelse krever samtykke og informasjon til alle berørte; laveste synlighet som standard; Private Set Intersection; slett etter analyse | [K39 s. 39–40] |
| Mikrofon | Lokal lydbehandling; samtykke for fjerninnsamling; ikke lagre lyd uten begrunnet behov; ikon når aktiv | [K39 s. 40] |
| Kamera/bilder | Skill kamera fra galleri; la brukeren velge konkrete bilder; fjern EXIF/metadata; serverbackup ikke standard | [K39 s. 40–41] |

Andre art. 25-krav for utgiveren [K39 s. 31–32]: minst inngripende standardinnstillinger; analyse per brukerkategori; plikt til å vurdere PETs; minimere data til partnere (ikke identifiserende data når unødvendig; ende-til-ende-kryptering anbefalt). Datatilsynets kart-app-eksempel illustrerer samme prinsipp [K09 s. 3]. Se [T13](T13-innebygd-personvern-art25.md).

### 5. SDK-er: utvelgelse, kontrakt og revisjon

**Utvelgelse** [K39 s. 53–54]:
- Krev dokumentasjon av **alle** behandlinger og data for valgt konfigurasjon, inkl. eventuelle tredjelandsoverføringer.
- SDK-en må støtte rettighetsforespørsler og **tilbaketrekking**; foretrekk API-er for automatiske svar.
- SDK-en bør kunne **blokkere** behandling/tilgang til samtykke foreligger, og **suspendere** egen kjøring ved signal fra appen; ingen samtykkepliktig lesing ved **første oppstart**.
- Granulært samtykke per formål.
- Se etter «russiske dukker» (SDK-er som trekker inn andre SDK-er).
- God praksis: velg løsninger som ikke finansieres ved å tjene penger på brukerdata.
- Er tvilen stor: vurder å avstå fra SDK-en [K39 s. 47].

**Kontraktsinnhold med SDK-leverandør / utvikler** (fra praktiske sjekkpunkter i [K39]):

| Krav | Kilde |
|---|---|
| Rolle kvalifisert per behandling og godkjent skriftlig av utgiveren | [K39 s. 53, 61] |
| DPA (art. 28) der SDK-leverandøren er databehandler – direkte mellom utgiver og SDK-leverandør | [K39 s. 52–53] |
| Regulering av innsamling for SDK-leverandørens egne formål (felles ansvar/selvstendig ansvar) | [K39 s. 18, 22] |
| Dokumentasjon/dynamisk protokoll per konfigurasjon; tabell over lese-/skriveoperasjoner med tillatelse, formål og teknisk blokkeringsmiddel; SDK-versjoner | [K39 s. 64] |
| Opplysning om tredjelandsoverføringer | [K39 s. 53, 61] |
| Samtykkeblokkering og granulære signaler; støtte for tilbaketrekking uten ustabilitet | [K39 s. 54, 66] |
| Rettighets-API-er med færrest mulig ekstra identifikatorer | [K39 s. 65] |
| Revisjonsrett og revisjonsrapporter | [K39 s. 54, 67] |
| Fjerndeaktivering av SDK-en i produksjon | [K39 s. 67] |
| Brudd- og sårbarhetsvarsling i tide for 72-timersfristen | [K39 s. 36, 67] |
| Forhåndsvarsling og godkjenning av endringer med personvernbetydning | [K39 s. 63] |
| Underdatabehandlere med forhåndsgodkjenning og samme garantier | [K39 s. 53] |
| Kontraktsfesting og revisjon dersom SDK-en innhenter samtykke på utgiverens vegne | [K39 s. 54] |
| For utvikler: instrukser, kontaktpunkt, akseptansetest, sikkerhetskrav, oppdateringsplikt, skriftlig godkjenning av personvernvalg | [K39 s. 33, 36, 45–47, 55] |

**Revisjon av SDK-er** (god praksis) [K39 s. 36, 54]: statisk analyse av inkluderte SDK-er og tillatelser; nettverksanalyse av at SDK-en ikke leser/skriver før samtykke, respekterer valg per formål, ikke samler mer enn dokumentert, ikke bruker tillatelser gitt for andre funksjoner, og respekterer tilbaketrekking. Gjenta ved SDK-oppdateringer.

### 6. Informasjon og rettigheter i apper

- Personvernerklæring tilgjengelig **før nedlasting** (appbutikken/nettsted) og i appen; appspesifikk [K26 avsn. 11; K39 s. 34].
- Liste over **tillatelser**, obligatorisk/valgfri, formål; god praksis å dele i (i) nødvendige for tjenesten og (ii) med andre formål [K39 s. 34].
- Overføring til forretningspartnere (monetisering) eksplisitt; fremhev **antall og bransje** for partnerne [K39 s. 34, 65].
- Kontekstuell informasjon ved hver innsamling; vedvarende indikatorer ved lokasjon/mikrofon [K39 s. 34].
- **Rettighetssenter i appen** som dekker også SDK-enes behandling; sletting uavhengig av tekniske begrensninger [K39 s. 35, 48].
- Se [T04](T04-apenhet-og-informasjonsplikt.md) og [T05](T05-de-registrertes-rettigheter.md).

### 7. Sikkerhet

**Minimumstiltak** [K39 s. 55; K33 ark 23]:
- TLS med fastsatte kryptosuiter for all serverkommunikasjon.
- Kryptografiske hemmeligheter i maskinvarebeskyttet lager (Android Hardware Keystore, Apple Secure Enclave).
- Deaktiver eller krypter OS-sikkerhetskopier (nøkkel ikke i backup).
- Autentisering tilpasset nivået (ikke biometri når enheten tillater flere personers maler og sikker identifisering kreves).
- OWASP MAS nivå L1.

**Sikkerhetsmodell** [K39 s. 55]: ikke bygg på terminalens integritet (unntatt begrunnet, f.eks. bank – rapporter uten å blokkere), certificate pinning eller kodeobfuskering; tjenesten skal tåle kompromitterte terminaler; beskytt mot misbruk fra databehandlere med loggført tilgang.

**Over tid** [K39 s. 36, 55–56]: CI/CD og kodegjennomgang; oppdaterte avhengigheter og overvåking av ondsinnede endringer i SDK-er/biblioteker (supply-chain); skille kritiske sikkerhetsoppdateringer fra funksjonelle; vurder tvungen oppdatering; varsle utgiver ved mistenkt eller faktisk avvik så snart som mulig.

Minimer data i **varsler** (notifikasjoner) og krypter innholdet; unngå å sende identifikatorer på tvers av apper til SDK-er (ev. hash) [K39 s. 48].

### 8. Dokumentasjon og DPIA

- Protokoll, begrunnede lagringstider, DPIA ved sannsynlig høy risiko, personvernombud der påkrevd [K39 s. 32].
- Rollevurderinger formaliseres i DPIA [K39 s. 17].
- Endringer (nye SDK-er, funksjoner, samtykkemåte) skal gjennom en godkjenningsprosess og reflekteres i protokoll, DPIA og personvernerklæring [K39 s. 37].
- SDK-leverandøren har selv DPIA-plikt ved sannsynlig høy risiko [K39 s. 62].
- Se [T10](T10-dpia-art35-36.md), [M05](../maler/M05-dpia-terskelvurdering.md), [A02](../arbeidsflyter/A02-gjennomfore-dpia.md).

### 9. Lignende miljøer

Anbefalingene kan overføres til smartklokker, smarthøyttalere, tilkoblede biler, medisinsk utstyr, IoT, PC-miljøer og spillplattformer [K39 s. 6]. For tilkoblede objekter finnes også CNILs PIA-mal [K31]. For enheter uten skjerm: QR-koder, trykt informasjon, lyd [K26 avsn. 19].

### 10. Kildenes vekt og begrensninger

- K39 (CNIL 2025) er nyest og mest detaljert, men er en fransk tilsynsmyndighets tolkning; ePrivacy-delen bygger på fransk lov, og bare den franske versjonen er bindende [K39 aktualitet]. GDPR-delene er felles for EØS.
- K39 skiller mellom «må» (plikt), «anbefaler» og «god praksis»; kapitlene om OS-leverandører og app-butikker er i stor grad god praksis [K39 s. 27 og aktualitet].
- Norsk ePrivacy-rett (ekomloven) er bare omtalt i merknader – verifiser.

## Vanlige feil og fallgruver

- SDK-er som starter sporing ved første oppstart før samtykke [K39 s. 54].
- Å behandle OS-tillatelse som samtykke for reklame/analyse [K39 s. 66].
- Ingen oversikt over hvilke SDK-er (og SDK-er i SDK-er) som er i appen og hva de samler inn [K39 s. 33, 53].
- Å anta at SDK-leverandøren «tar ansvaret» – utgiveren er minst felles ansvarlig [K39 s. 33].
- Presis lokasjon og «alltid»-tillatelse uten behov [K39 s. 39].
- Én generell personvernerklæring for hele selskapet, ikke tilgjengelig før nedlasting [K26 avsn. 11; K39 s. 34].
- Tilbaketrekking som gjør appen ustabil eller gir gjentatte forespørsler [K39 s. 66].
- Ingen avtalefestet oppdateringsplikt ved sårbarheter i tredjepartskomponenter [K39 s. 36].
- Kontaktopplasting for «finn venner» uten samtykke og uten hensyn til ikke-brukere [K39 s. 39–40].

## Sjekkliste

- [ ] Alle personopplysninger og behandlinger er identifisert, inkl. tredjeparter og OS-API-er [K39 s. 28, 47]
- [ ] Husholdningsunntaket vurdert (lokal, avskottet behandling) [K39 s. 12–15]
- [ ] Rolle per behandling for hver SDK/utvikler/OS-tjeneste – dokumentert [K39 s. 17]
- [ ] Alle lese-/skriveoperasjoner kartlagt og vurdert mot unntakene [K39 s. 29–30]
- [ ] Behandlingsgrunnlag for etterfølgende behandling per formål [K39 s. 28]
- [ ] CMP med «godta alle / avvis alle / tilpass»; samspill med tillatelser gir ikke motstridende valg [K39 s. 50–52]
- [ ] Ingen sporing før samtykke – testet med nettverksanalyse [K39 s. 36]
- [ ] Minst inngripende tillatelser, alternativer, lokal behandling, redusert presisjon [K39 s. 38–41]
- [ ] DPA/kontrakt med hver SDK-leverandør og utvikler med innhold som i tabellen over [K39]
- [ ] Personvernerklæring før nedlasting og i appen; liste over tillatelser og partnere [K39 s. 34]
- [ ] Rettighetssenter som dekker SDK-er [K39 s. 35]
- [ ] Sikkerhetsminimum (TLS, nøkkellager, backup, MASVS L1) og oppdateringsprosess [K39 s. 55–56]
- [ ] Særlige kategorier atskilt og utilgjengelige for SDK-er; ingen profileringsreklame mot mindreårige [K39 s. 31, 49]
- [ ] Protokoll, DPIA og personvernerklæring oppdateres ved endringer [K39 s. 37]

## Se også

- [T01 Roller](T01-roller-behandlingsansvarlig-databehandler.md) – rollevurdering i app/SDK-økosystemet
- [T02 Behandlingsgrunnlag og samtykke](T02-behandlingsgrunnlag-og-samtykke.md)
- [T07 Databehandleravtale](T07-databehandleravtale-art28.md), [M01](../maler/M01-databehandleravtale-sjekkliste.md), [A01](../arbeidsflyter/A01-gjennomga-databehandleravtale.md)
- [T13 Innebygd personvern](T13-innebygd-personvern-art25.md)
- [T08 Informasjonssikkerhet](T08-informasjonssikkerhet-art32.md)
- [T10 DPIA](T10-dpia-art35-36.md)
- [T14 Tilsynsmyndighet](T14-tilsynsmyndighet-og-one-stop-shop.md) – Nkom vs. Datatilsynet
- Kilder: [K39](../kilder/K39-cnil-mobilapper.md), [K25](../kilder/K25-wp259-samtykke.md), [K33](../kilder/K33-cnil-sikkerhetsguide.md), [K26](../kilder/K26-wp260-apenhet.md), [K31](../kilder/K31-cnil-pia-tilkoblede-objekter.md)

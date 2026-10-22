---
id: M09
tittel: "Sjekkliste – sikkerhetstiltak etter art. 32 (intern bruk og leverandørgjennomgang)"
gdpr_artikler: [5, 25, 28, 32, 33, 34]
kilder: [K32, K33, K30, K37, K10, K05, K34, K35, K36]
---

# Sjekkliste – sikkerhetstiltak etter art. 32

*Bruk: Sjekklisten er en grunnsikringsliste for «egnede tekniske og organisatoriske tiltak» (art. 32). Den kan brukes (1) **internt** som gap-analyse før eller under en risikovurdering ([M03](M03-risikovurdering-mal.md)), og (2) **mot leverandør/databehandler** som spørreskjema og som utkast til sikkerhetsvedlegg i databehandleravtalen ([M01](M01-databehandleravtale-sjekkliste.md), [A01](../arbeidsflyter/A01-gjennomga-databehandleravtale.md)). Tiltakene og kryssreferansene er forklart i [T08](../temaer/T08-informasjonssikkerhet-art32.md).*

*Referansene peker til: **NSM** = tiltaks-ID i NSMs grunnprinsipper v2.1 [K32](../kilder/K32-nsm-grunnprinsipper.md); **ark** = faktaark i CNILs sikkerhetsguide 2024 [K33](../kilder/K33-cnil-sikkerhetsguide.md); **PIA** = kapittel i CNILs PIA-tiltakskatalog [K30](../kilder/K30-cnil-pia-kunnskapsbaser.md); **SDM** = beskyttelsesmål i [K37](../kilder/K37-sdm-standard-datavernmodell.md) (DM dataminimering, T tilgjengelighet, I integritet, K konfidensialitet, IK ikke-kobling, Å åpenhet, IV intervenerbarhet).*

*Kolonnen **Nivå**: **G** = grunnsikring som normalt forventes for all behandling av personopplysninger; **H** = forventes særlig ved høyt beskyttelsesbehov (særlige kategorier, mange registrerte, sårbare grupper, kritiske tjenester) eller etter risikovurdering. **[Merknad – ikke fra kildene: inndelingen G/H er malens egen, basert på CNILs skille mellom «basic precautions» og «to go further» [K33](../kilder/K33-cnil-sikkerhetsguide.md) og SDMs beskyttelsesnivåer [K37 9.3–9.7](../kilder/K37-sdm-standard-datavernmodell.md).]** Et G-tiltak som velges bort skal begrunnes og vurderes i risikovurderingen; NSM påpeker at et tiltak som ikke gjennomføres kan gi økt risiko som må vurderes og eventuelt kompenseres [K32 s. 5](../kilder/K32-nsm-grunnprinsipper.md).*

*Kolonnen **Status**: ✔ Implementert · ◐ Delvis · ✘ Ikke implementert · N/A Ikke relevant (begrunn) · ? Ukjent/ikke dokumentert. **Ansvar**: rolle/person (internt) eller part (BA = behandlingsansvarlig, DB = databehandler, UDB = underdatabehandler). **Kommentar/bevis**: dokumentasjon, konfigurasjon, rapport, sertifikat, dato for siste test.*

---

## Hode

| Felt | Verdi |
|---|---|
| Objekt som vurderes | [system / behandling / leverandør og tjeneste] |
| Brukes som | [ ] Intern gap-analyse  [ ] Leverandørgjennomgang (DPA)  [ ] Vedlegg til DPA |
| Beskyttelsesnivå (fra M03 kap. 1.4) | [Normal / Høy / Svært høy] |
| Utfylt av / dato | [ ] |
| Bekreftet av leverandør (ved DPA-bruk) | [navn, rolle, dato] |
| Dokumentasjon mottatt | [ISMS-policy, ISO 27001-sertifikat med scope, SOC 2-rapport, pentestrapport, underleverandørliste, …] |

---

## A. Styring og organisering

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| A1 | Ledelsesforankret policy for informasjonssikkerhet og personvern, med mål og ansvar | G | NSM 1.1.2 · ark 1 · PIA 28 · SDM Å | | | |
| A2 | Prosess for risikostyring (verdier, trusler, eksisterende tiltak, vurdering, håndtering, verifisering) | G | NSM 1.1.3 · ark 1, 20 · PIA 21 | | | |
| A3 | Fastsatte toleransegrenser/akseptkriterier for risiko | G | NSM 1.1.4 · K18 vedlegg B | | | |
| A4 | Handlingsplan for sikkerhet med ansvarlig og frist per tiltak | G | ark 1 · PIA 21 | | | |
| A5 | Ledelsens gjennomgang minst årlig (trusler, hendelser, klager, fremdrift) | G | ark 1 · PIA 27, 35 | | | |
| A6 | Utpekt CISO/sikkerhetsansvarlig og personvernombud med tilgang til ledelsen | G | ark 1 · PIA 27 · NSM 1.3.3 | | | |
| A7 | Oversikt over systemer, data, eierskap, avhengigheter og dataflyt (dataflytdiagram) | G | NSM 1.1.5–1.1.6 · ark 1 · SDM Å | | | |
| A8 | Inventar over enheter og programvare inkl. sky/SaaS og ikke-støttede produkter | G | NSM 1.2.1–1.2.4 · ark 22 · PIA 37 | | | |
| A9 | Styringssystem (ISMS) etter anerkjent standard, f.eks. ISO/IEC 27001 (ev. 27701) | H | NSM 2.1.10a · ark 1, 14 · K16 | | | |

## B. Identitet, tilgang og autentisering

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| B1 | Unik brukeridentitet; ingen delte kontoer (unntak godkjent og logget) | G | NSM 2.6.1c · ark 4 · PIA 8.1 · SDM K | | | |
| B2 | Tilgang etter tjenstlig behov og minste privilegium; rollebaserte profiler | G | NSM 2.6.1b · ark 5 · PIA 8.1, 5 · SDM K, IK | | | |
| B3 | MFA for administratorer, fjerntilgang og tilgang til kritiske/sensitive data | G | NSM 2.6.7 · ark 4, 8 · PIA 8.2 | | | |
| B4 | Formell livssyklus for kontoer (opprettelse, endring, deaktivering ved fratreden/rolleendring); utløpsdato for midlertidige | G | NSM 2.6.2–2.6.3 · ark 5 · PIA 8.1 | | | |
| B5 | Gjennomgang av tilgangsrettigheter minst årlig, særlig privilegerte kontoer | G | NSM 2.6.1e · ark 5 · PIA 8.1 | | | |
| B6 | Ingen admin-rettigheter for sluttbrukere; separate kontoer for forhøyede rettigheter | G | NSM 2.6.4–2.6.5 · ark 5, 6 · PIA 8.1 | | | |
| B7 | Passordpolicy etter CNIL: ≥ 80 bit entropi for passord alene (f.eks. 12 tegn med fire tegntyper), ingen tvungen periodisk bytte for vanlige brukere, bytte ved første innlogging | G | ark 4 · NSM 2.6.3e | | | |
| B8 | Passord lagret med bcrypt/scrypt/Argon2/PBKDF2 og salt; aldri i klartekst eller sendt i klartekst | G | ark 4, 21 · K34 s. 2 · PIA 8.4 | | | |
| B9 | Alle standardpassord endret før produksjon | G | NSM 2.3.7 · ark 4 · PIA 8.4 | | | |
| B10 | Begrensning av innloggingsforsøk (forsinkelse/sperring) | G | ark 4 · PIA 8.2 · K36 ES11 | | | |
| B11 | Sentral identitetsforvaltning/SSO; deaktivering fremfor sletting (revisjonsspor) | H | NSM 2.6.1f, 2.6.2b, 2.6.3 | | | |
| B12 | Phishing-resistent/sertifikatbasert autentisering for administrasjon | H | NSM 2.3.7, 2.6.7 · K36 ES20 | | | |

## C. Logging, sporbarhet og overvåking

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| C1 | Dokumentert loggstrategi: formål, hvilke data, lagringstid, tilgang, sletting | G | NSM 3.2.1 · ark 16 · PIA 36, 43 · SDM Å | | | |
| C2 | Logging av vellykkede og mislykkede pålogginger, administrasjons- og sikkerhetshendelser | G | NSM 3.2.4 · ark 16 · PIA 19.1 | | | |
| C3 | Applikasjonslogg av opprett/les/del/endre/slett med bruker-ID, tid, operasjon og datareferanse | G | ark 16 · PIA 43 · SDM Å | | | |
| C4 | Fastsatt lagringstid for logger (CNIL: rullerende 6–12 mnd. som utgangspunkt) og sletting etterpå | G | ark 16 · PIA 36 · NSM 3.2.2, 3.2.7 · SDM DM | | | |
| C5 | Brukere/ansatte informert om logging; logger brukes ikke til andre formål (f.eks. arbeidstidskontroll) | G | NSM 3.2.2c · ark 16 | | | |
| C6 | Logger beskyttet mot endring/sletting og innsyn fra de som logges; tidssynkronisering (NTP/UTC) | G | NSM 3.2.6, 2.3.9 · ark 16 · PIA 36 | | | |
| C7 | Aktiv analyse og varsling (sanntid eller kort sikt); eskaleringsrutine | G | NSM 3.3.1–3.3.6 · ark 16, 19 | | | |
| C8 | Sentral loggløsning/SIEM med normaltilstand og trusseletterretning | H | NSM 3.3.2–3.3.4, 3.3.7 | | | |
| C9 | Brukeren kan se egen innloggingshistorikk/aktivitet | H | ark 16 · K36 ES13 | | | |

## D. Kryptering og nøkkelhåndtering

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| D1 | Kryptering ved overføring over åpne nett – TLS 1.2 eller 1.3; aldri SSL/HTTP for personopplysninger | G | NSM 2.7.4 · ark 9, 10 · PIA 4.9, 41 · K10 · K34 s. 2 | | | |
| D2 | Obligatorisk kryptering ved overføring av særlige kategorier, fødselsnummer, opplysninger om mange og beskyttelsesverdige opplysninger | G | K10 | | | |
| D3 | Full diskkryptering på bærbare enheter og flyttbare medier | G | NSM 2.7.3 · ark 7 · PIA 4.4, 40.3 · K10 | | | |
| D4 | Kryptering av lagrede data (database/lagring/backup) etter risiko | G | NSM 2.7.5, 2.9.4d · ark 17, 22 · PIA 4.5 | | | |
| D5 | Kun anerkjente algoritmer (AES, ChaCha20, SHA-2/3, RSA ≥ 2048/3072, ECDSA); ikke DES/3DES/MD5/SHA-1 | G | NSM 2.7.2 · ark 21 · K10 | | | |
| D6 | Kryptostrategi med nøkkelhåndtering (generering, lagring, rotasjon, kompromittering); hemmeligheter ikke i kildekode | G | NSM 2.7.1 · ark 11, 21, 25 · PIA 4 | | | |
| D7 | Nøkkel/passord sendes separat fra krypterte data | G | ark 13 · PIA 38.1 · K10 | | | |
| D8 | Kryptering der leverandøren ikke har tilgang til nøklene (kundestyrte nøkler/klientsidekryptering) | H | ark 22 · K36 ES16–ES17 | | | |
| D9 | Pseudonymisering eller anonymisering der formålet tillater det | H | ark 11 · PIA 2, 26.2 · SDM IK, DM | | | |
| D10 | Integritetsbeskyttelse (hash/MAC/signatur) av kritiske data og logger | H | NSM 3.2.6a · ark 21 · PIA 7 · SDM I | | | |

## E. Sikkerhetskopiering, kontinuitet og gjenoppretting

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| E1 | Dokumentert backupplan (data, hyppighet, ansvar, oppbevaring, gjenopprettingstid, godkjenner) | G | NSM 2.9.1 · ark 17 · PIA 33 · SDM T | | | |
| E2 | Minst én kopi geografisk adskilt og minst én offline/isolert (3-2-1) | G | NSM 2.9.4c · ark 17 · PIA 33 | | | |
| E3 | Backup beskyttet som produksjon (kryptert, tilgangsbegrenset, separert) | G | NSM 2.9.4 · ark 17 | | | |
| E4 | Gjenopprettingstester gjennomføres jevnlig (CNIL: utvalg månedlig, full årlig) | G | NSM 2.9.3 · ark 17 · PIA 33 | | | |
| E5 | Kjent lagringsland for backup | G | PIA 33 · ark 22 | | | |
| E6 | Kontinuitets- og gjenopprettingsplan (BCP/DRP) basert på BIA; personvernnivået opprettholdes i nødmodus | G | NSM 4.1.1–4.1.2 · ark 18 · PIA 37 | | | |
| E7 | Redundans (RAID, UPS, dupliserte komponenter/datasentre) etter tilgjengelighetskrav | H | NSM 2.2.7 · ark 18 · PIA 37, 29 · SDM T | | | |
| E8 | Sletting av data i backup innen fastsatt frist | H | K36 ES05 · PIA 26.2 | | | |

## F. Sikker konfigurasjon, sårbarheter og skadevare

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| F1 | Sentralt styrt patching; kritiske sårbarheter lukkes uten opphold; ukentlig sjekk | G | NSM 2.3.1 · ark 6, 9 · PIA 37 | | | |
| F2 | Kun støttede operativsystemer og programvare; utdatert utstyr isolert | G | NSM 2.1.2, 2.5.4 · ark 6, 9 | | | |
| F3 | Herdede standardkonfigurasjoner; unødvendige tjenester deaktivert | G | NSM 2.3.3–2.3.4 · ark 9 · PIA 19.1 | | | |
| F4 | Antiskadevare sentralt styrt, kan ikke slås av av bruker | G | NSM 3.1.3 · ark 6 · PIA 23 | | | |
| F5 | Automatisk skjermlås (maks 15 min) | G | ark 6 · PIA 19.1 · K34 s. 2 | | | |
| F6 | Jevnlig automatisert sårbarhetsskanning | G | NSM 3.1.1 · ark 9 | | | |
| F7 | Godkjentlisting av applikasjoner; makrokontroll | H | NSM 2.3.2 · ark 6 | | | |
| F8 | Verifisering av konfigurasjon mot godkjent baseline (automatisert) | H | NSM 2.3.5 | | | |

## G. Nettverk og dataflyt

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| G1 | Segmentering (minst internt nett og DMZ); klienter adskilt fra servere | G | NSM 2.2.3, 2.2.5 · ark 8 · PIA 38.1 | | | |
| G2 | Administrasjonsgrensesnitt ikke eksponert mot internett; fjernadministrasjon via VPN/sterk autentisering | G | NSM 2.3.6 · ark 8 · PIA 38.3 | | | |
| G3 | Databaser ikke direkte tilgjengelige fra internett | G | ark 9, 10 | | | |
| G4 | Brannmur med kun nødvendige flyter (godkjentlisting); vertsbrannmur | G | NSM 2.4.4, 2.5.1 · ark 6, 8 | | | |
| G5 | Trådløst nett med WPA2/WPA3 (enterprise); gjestenett adskilt | G | NSM 2.4.2 · ark 8 | | | |
| G6 | Kontrollert trafikk mot leverandører/partnere | G | NSM 2.5.7 | | | |
| G7 | IDS/IPS og nettverksovervåking (brukere informert) | H | NSM 3.1.3b · ark 8 · PIA 38.1 | | | |
| G8 | Nettverkstilgangskontroll (802.1X) – kun forvaltede enheter | H | NSM 2.4.1 · ark 8 | | | |

## H. Arbeidsstasjoner, mobile enheter og BYOD

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| H1 | Forvaltede enheter; ikke-forvaltede/BYOD kun med begrenset tilgang etter risikovurdering | G | NSM 2.2.6, 2.5.2 · ark 7 | | | |
| H2 | Mobil enhetsstyring (MDM): lås, kryptering, fjernsletting | G | ark 7 · PIA 19.3 | | | |
| H3 | Flyttbare medier begrenset; autorun deaktivert | G | ark 6 · PIA 40.4 | | | |
| H4 | Fjernhjelp kun med brukerens samtykke og synlig indikasjon | G | ark 6 · PIA 24.2, 38.3 | | | |
| H5 | Data lagres på sikkerhetskopiert sentral lagring, ikke lokalt | G | ark 6 · PIA 19.1 | | | |

## I. Nettsteder, e-post og API

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| I1 | TLS på alle sider med innlogging eller personopplysninger; HttpOnly/Secure/SameSite på informasjonskapsler | G | ark 10 · PIA 41 | | | |
| I2 | Ingen personopplysninger eller hemmeligheter i URL; tilgangskontroll på objektnivå (ikke forutsigbare URL-er) | G | ark 10 · K34 s. 2 | | | |
| I3 | Beskyttelse mot OWASP Top 10 (injeksjon, XSS m.m.); inndatavalidering | G | ark 10, 11 · PIA 7.1 · NSM 2.1.8 | | | |
| I4 | E-post: SPF, DKIM, DMARC; STARTTLS | G | NSM 2.8.1–2.8.2 · PIA 38.14 | | | |
| I5 | API: autentisering, skille mellom vanlige og administrative kall, logging, dataminimering, nøkler i hvelv | G | ark 25 | | | |
| I6 | Kontoopprettelse/tilbakestilling avslører ikke om en konto finnes | H | ark 10 | | | |
| I7 | Content-Security-Policy; test mot OWASP (ev. API Security Top 10) før hver versjon | H | ark 10, 25 · PIA 41 | | | |

## J. Anskaffelse, utvikling og endring

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| J1 | Sikkerhets- og personvernkrav i anskaffelser gjennom hele livsløpet | G | NSM 2.1.1 · ark 11 · PIA 20 | | | |
| J2 | Separate miljøer for utvikling, test og produksjon | G | NSM 2.1.6 · ark 11 · PIA 20.2 | | | |
| J3 | Fiktive eller anonymiserte data i utvikling og test; ekte data bare i miljø sikret som produksjon | G | NSM 2.1.6 · ark 11 · PIA 20.2 | | | |
| J4 | Sikkerhetstesting (inkl. sårbarhetstest) før produksjonssetting og ved nye versjoner | G | NSM 2.1.7 · ark 10, 11 · K34 s. 2 | | | |
| J5 | Endringshåndtering med sikkerhetsvurdering, også for hasteendringer | G | NSM 2.10.1–2.10.4 · PIA 28 | | | |
| J6 | Personvernvennlige standardinnstillinger; minimal datainnsamling i skjema (unngå fritekst) | G | ark 11 · PIA 20.2, 26.1 · SDM DM | | | |
| J7 | Sikker utviklingsmetode, kodegjennomgang, avhengighetskontroll (SDK/biblioteker) | H | NSM 2.1.5, 2.1.8 · ark 11, 23 | | | |
| J8 | KI-systemer: datakvalitet, beskyttelse mot modellinversjon, kontroll av output for personopplysninger | H | ark 24 | | | |

## K. Leverandører, databehandlere og sky

*Denne delen er særlig for DPA-gjennomgang. Punktene LV1–LV10 svarer til NSMs minimumsundersøkelser [K32 2.1.10 a–j](../kilder/K32-nsm-grunnprinsipper.md).*

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| LV1 | Leverandøren har ISMS og ev. sertifisering – **scope kontrollert** mot den aktuelle tjenesten | G | NSM 2.1.10a · ark 14 · PIA 34.2 | | | |
| LV2 | Innsyn i sikkerhetsarkitektur og -dokumentasjon (sikkerhetspolicy vedlagt avtalen) | G | NSM 2.1.10b · PIA 34.2 | | | |
| LV3 | Oversikt over hvem hos leverandøren som har tilgang, **hvor data lagres og hvorfra de aksesseres**, segregering fra andre kunder | G | NSM 2.1.10d · PIA 34.3 · ark 22 | | | |
| LV4 | Sikkerhetsfunksjonalitet dekker behovene (MFA, kryptering, logging, tilgangsstyring kan konfigureres av kunden) | G | NSM 2.1.10e · ark 22 | | | |
| LV5 | Leverandøren har sikkerhetsovervåking og logging, og logging er kontraktsfestet | G | NSM 2.1.10f · ark 16 | | | |
| LV6 | Hendelseshåndtering med varsling av behandlingsansvarlig **uten ugrunnet opphold** ved brudd (frist og innhold avtalt) | G | NSM 2.1.10g · ark 14 · PIA 34.1 · K05 | | | |
| LV7 | Beredskaps- og kontinuitetsplaner som harmonerer med kundens | G | NSM 2.1.10h · ark 22 | | | |
| LV8 | Godkjenning og oversikt over underdatabehandlere; samme krav videreført i kjeden | G | NSM 2.1.10i · ark 14 · PIA 34.2 · K05 | | | |
| LV9 | Avtalt tilbakelevering, flytting og sletting ved opphør (med bekreftelse) | G | NSM 2.1.10j · ark 14 · PIA 34.2 | | | |
| LV10 | Utviklingsplaner for sikkerhetsfunksjonalitet | H | NSM 2.1.10c | | | |
| LV11 | Revisjonsrett og jevnlig gjennomgang av sikkerhetstiltak; bistand med art. 32–36 | G | ark 14 · K05 · K35 | | | |
| LV12 | Minimumskrav til sikkerhet i eget vedlegg til databehandleravtalen | G | K05 · ark 14 | | | |
| LV13 | Leverandøren får ikke tilgang til data/systemer for egne formål (inkl. «sikkerhet», telemetri) uten kundens tillatelse | G | ark 22 | | | |
| LV14 | Overføring/tilgang fra land utenfor EØS kartlagt og rettslig forankret | G | ark 14, 22 · PIA 42 · se T11 | | | |
| LV15 | Kundens egen konfigurasjon av skytjenesten (IAM, kryptering, logging) etter egen policy | G | ark 22 | | | |
| LV16 | Personell hos leverandøren med taushetsplikt og opplæring | G | ark 3, 14 · PIA 32.2 · SDM K | | | |

## L. Vedlikehold, fjerntilgang og avhending

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| L1 | Loggbok over vedlikeholdsinngrep | G | ark 15 · PIA 24.1 | | | |
| L2 | Fjernvedlikehold kun etter forespørsel, tidsbegrenset, kryptert og lukket etterpå; ingen permanent tilgang | G | ark 15 · PIA 24.1 · NSM 2.6.3d | | | |
| L3 | Sikker sletting/destruksjon før kassering, ekstern reparasjon eller retur av leasingutstyr (med dokumentasjon) | G | ark 15 · PIA 24.3, 40.1 | | | |
| L4 | Tredjepartsinngrep på stedet overvåkes | H | ark 15 · NSM 2.1.4e | | | |

## M. Fysisk sikring

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| M1 | Låste lokaler, innbruddsalarm med periodisk test, brannvern | G | ark 12 · PIA 6, 29 | | | |
| M2 | Soneinndeling med egen adgangskontroll til serverrom; oppdatert liste over autoriserte | G | ark 12 · PIA 6 | | | |
| M3 | Besøkende eskorteres utenfor publikumssoner; skjermer og dokumenter ikke synlige | G | ark 12 · PIA 6 | | | |
| M4 | Miljøvern for IT-utstyr (UPS, kjøling, vann, brann) | G | ark 12 · PIA 29 | | | |
| M5 | Beskyttelse av nettverksuttak og kabler/svitsjer | G | NSM 2.4.3 · ark 12 | | | |
| M6 | Adgangslogg for kritiske rom (brukere informert; begrenset lagringstid) | H | ark 12 · PIA 6 | | | |

## N. Personell og opplæring

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| N1 | IT-reglement/retningslinjer med bindende kraft (passord, melding av hendelser, låsing, programvare, flyttbare medier) | G | ark 2 · NSM 2.6.1g | | | |
| N2 | Taushets-/konfidensialitetserklæring for ansatte, innleide og leverandørpersonell | G | ark 2 · PIA 32.2 · SDM K | | | |
| N3 | Opplæring i sikkerhet og personvern tilpasset roller, inkl. nyansatte og IT-personell | G | ark 3 · PIA 18 | | | |
| N4 | Bevisstgjøring om phishing og sosial manipulering; jevnlige påminnelser | G | ark 3 · PIA 18 | | | |
| N5 | Instruks om at personopplysninger kun behandles etter instruks (art. 32 nr. 4) | G | **[Merknad – ikke fra kildene]** · ark 2 | | | |
| N6 | Øvelser/simuleringer av hendelser | H | ark 3 · NSM 4.1.6 | | | |

## O. Hendelseshåndtering og brudd

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| O1 | Planverk for hendelseshåndtering med roller, kontaktinformasjon og klassifisering | G | NSM 4.1.1, 4.1.3, 4.1.5 · ark 19 · PIA 17 | | | |
| O2 | Kriterier for når en hendelse er brudd på personopplysningssikkerheten – også tap av tilgjengelighet/integritet | G | ark 19 · K34 s. 1 | | | |
| O3 | Rutine for melding til Datatilsynet innen 72 timer (ev. i to trinn) og varsling av registrerte ved høy risiko | G | ark 19 · PIA 17 · se T12 | | | |
| O4 | Intern oversikt (avviksregister) over alle brudd | G | ark 19 · PIA 17 · K34 s. 2 | | | |
| O5 | Loggføring av tidslinje og sikring av bevis | G | NSM 4.3.3 · PIA 17 | | | |
| O6 | Læring etter hendelser og oppdatering av tiltak/risikovurdering | G | NSM 4.4.1–4.4.4 · PIA 17 | | | |
| O7 | Test av planer og beredskap minst annethvert år | H | NSM 3.4.5, 4.1.6 · PIA 17 | | | |
| O8 | Avtaler med eksterne støttespillere (hendelsesrespons, sektor-CERT) | H | NSM 4.1.4 | | | |

## P. Testing, revisjon og evaluering (art. 32 nr. 1 bokstav d)

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| P1 | Plan for regelmessig testing og evaluering av tiltakenes effekt (indikatorer) | G | ark 1 · PIA 35 | | | |
| P2 | Inntrengingstest minst årlig (utsiden og innsiden) for systemer med personopplysninger av betydning | H | NSM 3.4.1–3.4.6 | | | |
| P3 | Periodisk sikkerhetsrevisjon (intern/ekstern) med oppfølging av funn på ledelsesnivå | G | ark 1 · PIA 21, 35 · K35 | | | |
| P4 | Risikovurderingen revideres minst årlig og ved vesentlige endringer | G | ark 20 · PIA 21 · K28 s. 7 | | | |
| P5 | Revisor har både juridisk og teknisk kompetanse; konfidensialitet i revisjonen avtalt | H | K35 EM11–EM22 | | | |

## Q. Dataminimering, lagringstid og sletting

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| Q1 | Kun nødvendige opplysninger samles inn; hver datakategori begrunnet | G | PIA 26.1 · ark 11 · SDM DM | | | |
| Q2 | Lagringstid fastsatt per datakategori (inkl. logger og arkiv) | G | PIA 9 · SDM DM | | | |
| Q3 | Automatisk sletting/anonymisering ved utløp; logisk sletting (statusflagg) regnes ikke som sletting | G | PIA 9 · SDM DM | | | |
| Q4 | Tilgang til eldre data begrenset (mellomlagring/arkiv for begrenset krets) | H | PIA 9 · SDM IK | | | |
| Q5 | Partisjonering/separasjon av data per formål og prosess | H | PIA 5 · SDM IK | | | |

## R. Åpenhet og intervenerbarhet (tekniske forutsetninger)

| ID | Kontrollpunkt | Nivå | Referanse | Status | Ansvar | Kommentar/bevis |
|---|---|---|---|---|---|---|
| R1 | Systemdokumentasjon, dataflyt og konfigurasjonsendringer dokumentert og versjonskontrollert | G | SDM Å · K40 tabell 1 | | | |
| R2 | Systemet kan finne, rette, sperre, utlevere og slette alle data om én person (inkl. hos databehandlere) | G | SDM IV · PIA 11–13 | | | |
| R3 | Ett kontaktpunkt for de registrerte; sporbarhet av hvordan forespørsler er håndtert | G | SDM IV | | | |
| R4 | Mulighet til å deaktivere enkeltfunksjoner uten å stoppe hele systemet | H | SDM IV · K40 tabell 1 | | | |

---

## Oppsummering og oppfølging

| Gruppe | Antall ✔ | Antall ◐ | Antall ✘ | Antall ? | Viktigste avvik |
|---|---|---|---|---|---|
| A–R | | | | | |

| Avvik-ID | Kontrollpunkt | Risiko (fra M03) | Tiltak / krav til leverandør | Ansvar | Frist | Status |
|---|---|---|---|---|---|---|
| | | | | | | |

*Veiledning for vurderingen:*
- *Ett avvik er ikke automatisk uakseptabelt – vurder det i risikovurderingen ([M03](M03-risikovurdering-mal.md)), og dokumenter eventuelle kompenserende tiltak [K32 s. 5](../kilder/K32-nsm-grunnprinsipper.md). Mangler et grunnleggende tiltak, er det likevel en presumsjon for mangel [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md).*
- *Alternative tiltak må være funksjonelt likeverdige med referansetiltaket [K37 10.3](../kilder/K37-sdm-standard-datavernmodell.md).*
- *Ved leverandørgjennomgang: krev dokumentasjon fremfor egenerklæring for G-punktene i gruppe B, D, E, K og O; sertifikat er bare første indikator [K33 ark 14](../kilder/K33-cnil-sikkerhetsguide.md). Punkter merket ✘ eller ? i gruppe K skal enten løses i avtalen eller tas inn i risikovurderingen før signering. Se [A01](../arbeidsflyter/A01-gjennomga-databehandleravtale.md) og [T07](../temaer/T07-databehandleravtale-art28.md).*
- *Som vedlegg til DPA: omformuler G-punktene (og relevante H-punkter) til forpliktelser («Databehandleren skal …») og angi hvordan etterlevelse dokumenteres [K05](../kilder/K05-dt-databehandleravtale.md).*
- *Sjekklisten dekker ikke rettslige forhold (behandlingsgrunnlag, informasjon, overføringsgrunnlag) – se [T02](../temaer/T02-behandlingsgrunnlag-og-samtykke.md), [T11](../temaer/T11-overforing-tredjeland-og-tia.md).*

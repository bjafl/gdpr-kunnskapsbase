---
id: T08
tittel: "Informasjonssikkerhet – sikkerhet ved behandlingen (art. 32)"
gdpr_artikler: [5, 24, 25, 28, 29, 32, 33, 34, 35, 40, 42]
kilder: [K32, K33, K30, K37, K10, K16, K17, K18, K12, K05, K34, K35, K36, K40, K21, K24, K31]
---

# Informasjonssikkerhet – sikkerhet ved behandlingen (art. 32)

Dette notatet samler kravene til informasjonssikkerhet etter personvernforordningen (GDPR) art. 32 og gir en samlet, tematisk tiltaksoversikt med koblinger til de tre tiltakskatalogene i kunnskapsbasen: **NSMs grunnprinsipper for IKT-sikkerhet** ([K32](../kilder/K32-nsm-grunnprinsipper.md)), **CNILs sikkerhetsguide 2024** ([K33](../kilder/K33-cnil-sikkerhetsguide.md), 25 faktaark) med CNILs PIA-tiltakskatalog ([K30](../kilder/K30-cnil-pia-kunnskapsbaser.md)), og **Standard-Datenschutzmodell (SDM)** ([K37](../kilder/K37-sdm-standard-datavernmodell.md)) med sine beskyttelsesmål. Kryssreferansetabellen i avsnittet «Kryssreferanse NSM ↔ CNIL ↔ SDM» er laget for direkte oppslag i DPA-gjennomganger, DPIA-er og risikovurderinger.

Metodevalg for selve risikovurderingen står i [T09](T09-risikovurdering-metoder-og-skalaer.md). Utfyllbar tiltakssjekkliste: [M09](../maler/M09-sikkerhetstiltak-sjekkliste.md).

## Kjerneregler (kort svar)

1. **Plikten gjelder både behandlingsansvarlig og databehandler.** Begge skal gjennomføre egnede tekniske og organisatoriske tiltak (art. 32 nr. 1) [K33 s. 4](../kilder/K33-cnil-sikkerhetsguide.md). Databehandleravtalen skal pålegge databehandleren alle tiltak etter art. 32 (art. 28 nr. 3 bokstav c); minimumskrav bør stå i et eget sikkerhetsvedlegg [K05](../kilder/K05-dt-databehandleravtale.md).
2. **«Egnet» betyr risikobasert.** Tiltaksnivået skal stå i forhold til risikoen for *de registrertes* rettigheter og friheter, sett opp mot teknisk utvikling, kostnad og behandlingens art, omfang, formål og sammenheng **[Merknad – ikke fra kildene: ordlyden i art. 32 nr. 1]**. Plikten er ikke absolutt, men relativ til omstendighetene [K37 s. 9](../kilder/K37-sdm-standard-datavernmodell.md). NSM understreker at tiltaksvalg skal bygge på risikovurdering, og at et anbefalt tiltak som velges bort gir økt risiko som må vurderes og eventuelt kompenseres [K32 s. 5](../kilder/K32-nsm-grunnprinsipper.md).
3. **Det skal alltid gjøres en sikkerhetsrisikovurdering før behandlingen starter**, og den skal oppdateres regelmessig og ved endringer – uavhengig av om DPIA kreves [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md).
4. **To komplementære lag:** (a) et *sikkerhetsfundament* av god praksis som dekker de vanligste risikoene, og (b) tilleggstiltak fra en *risikoanalyse for de registrerte* [K33 s. 4](../kilder/K33-cnil-sikkerhetsguide.md). Avanserte tiltak uten grunnleggende på plass er en kjent feil [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md).
5. **Konfidensialitet, integritet, tilgjengelighet og robusthet** skal sikres vedvarende, og evnen til **gjenoppretting i rett tid** skal finnes (art. 32 nr. 1 bokstav b og c) – jf. sikkerhetskopiering og kontinuitet [K32 2.9, 4.1](../kilder/K32-nsm-grunnprinsipper.md), [K33 ark 17–18](../kilder/K33-cnil-sikkerhetsguide.md).
6. **Regelmessig testing og evaluering** av tiltakenes effektivitet er et eget krav (art. 32 nr. 1 bokstav d) – inntrengingstest minst årlig og test av deteksjon/beredskap minst annethvert år etter NSM [K32 3.4.4–3.4.5](../kilder/K32-nsm-grunnprinsipper.md); årlig ledelsesgjennomgang etter CNIL [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md).
7. **Kryptering og pseudonymisering** er nevnt i art. 32 nr. 1 bokstav a. Datatilsynet mener kryptering er *nødvendig* ved overføring av særlige kategorier, fødselsnummer, opplysninger om mange og opplysninger klassifisert som beskyttelsesverdige [K10](../kilder/K10-dt-kryptering.md). Kryptering er likevel ikke automatisk «egnet» – det avhenger av kontekst [K24 fotnote 30](../kilder/K24-wp248-dpia.md).
8. **Ansvaret forsvinner ikke ved tjenesteutsetting.** «Virksomhetens ansvar for sikkerheten forsvinner ikke selv om man tjenesteutsetter» [K32 2.1.9](../kilder/K32-nsm-grunnprinsipper.md); å delegere all IT-sikkerhet til en leverandør er en feil [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md).
9. **Personvernmålene kommer i tillegg til K-I-T.** En art. 32-vurdering som bare dekker konfidensialitet, integritet og tilgjengelighet, mangler dataminimering, ikke-kobling, åpenhet og intervenerbarhet [K37 kap. 5](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md). Sikkerhetstiltak alene reduserer ikke nødvendigvis personvernrisiko [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md).
10. **Sikkerhetstiltak er også behandling.** Logging og overvåking av ansatte og brukere er egen behandling av personopplysninger og krever formål, lagringstid, informasjon og formålsbegrensning [K32 3.2.1–3.2.2, s. 39](../kilder/K32-nsm-grunnprinsipper.md), [K33 ark 16](../kilder/K33-cnil-sikkerhetsguide.md).

## Rettslig grunnlag

**GDPR art. 32** – sikkerhet ved behandlingen **[Merknad – ikke fra kildene: gjengivelse av forordningsteksten i hovedtrekk]**:

| Nr. | Innhold |
|---|---|
| 1 | Behandlingsansvarlig og databehandler skal, idet det tas hensyn til den tekniske utviklingen, gjennomføringskostnadene og behandlingens art, omfang, formål og sammenheng, samt risikoene av varierende sannsynlighet og alvorlighet for fysiske personers rettigheter og friheter, gjennomføre egnede tekniske og organisatoriske tiltak for å oppnå et sikkerhetsnivå som er egnet med hensyn til risikoen, herunder blant annet, alt etter hva som er egnet: **a)** pseudonymisering og kryptering; **b)** evne til å sikre vedvarende konfidensialitet, integritet, tilgjengelighet og robusthet i behandlingssystemer og -tjenester; **c)** evne til å gjenopprette tilgjengeligheten og tilgangen til personopplysninger i rett tid ved en fysisk eller teknisk hendelse; **d)** en prosess for regelmessig testing, analyse og vurdering av hvor effektive tiltakene er. |
| 2 | Ved vurderingen av egnet sikkerhetsnivå skal det særlig tas hensyn til risikoene ved behandlingen, særlig ved utilsiktet eller ulovlig tilintetgjøring, tap, endring, ikke-autorisert utlevering av eller tilgang til personopplysninger. |
| 3 | Godkjente atferdsnormer (art. 40) eller sertifiseringsmekanismer (art. 42) kan brukes som et element for å påvise samsvar med nr. 1. |
| 4 | Behandlingsansvarlig og databehandler skal sikre at enhver som handler under deres myndighet og har tilgang til personopplysninger, bare behandler dem etter instruks, med mindre unionsretten eller nasjonal rett krever det. |

**Tilgrensende bestemmelser:**

- **Art. 5 nr. 1 bokstav f** (integritet og konfidensialitet) og **nr. 2** (ansvarlighet) – sikkerhet er et grunnprinsipp; logger og dokumentasjon er bevis for etterlevelse [K33 ark 14, 16](../kilder/K33-cnil-sikkerhetsguide.md). Se [T03](T03-grunnprinsipper-art5.md).
- **Art. 24** – behandlingsansvarliges ansvar for egnede tiltak; **art. 25** – innebygd personvern og personvern som standard (sikkerhet fra design) [K33 ark 11](../kilder/K33-cnil-sikkerhetsguide.md), [K13](../kilder/K13-dt-innebygd-personvern.md). Se [T13](T13-innebygd-personvern-art25.md).
- **Art. 28 nr. 1 og nr. 3 bokstav c, f og h** – tilstrekkelige garantier fra databehandler, art. 32-tiltak, bistand med art. 32–36, revisjon [K05](../kilder/K05-dt-databehandleravtale.md), [K32 2.1.10](../kilder/K32-nsm-grunnprinsipper.md). Se [T07](T07-databehandleravtale-art28.md).
- **Art. 29** – behandling under behandlingsansvarliges myndighet (instruks) **[Merknad – ikke fra kildene]**.
- **Art. 33–34** – melding og varsling ved brudd; kryptering kan etter art. 34 nr. 3 bokstav a fjerne plikten til å varsle de registrerte [K10](../kilder/K10-dt-kryptering.md). Se [T12](T12-avvik-og-brudd-art33-34.md).
- **Art. 35** – DPIA; tiltak etter art. 35 nr. 7 bokstav d omfatter «sikkerhetstiltak og mekanismer» [K24](../kilder/K24-wp248-dpia.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md). Se [T10](T10-dpia-art35-36.md).
- **Fortalepunkt 83** (tiltak ut fra risiko og teknologiens stand), 75–77 (risikobegrepet), 78 (innebygd personvern) [K37 tabell 4](../kilder/K37-sdm-standard-datavernmodell.md), [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
- **Sanksjoner:** Brudd på art. 32 faller under art. 83 nr. 4 (inntil 10 mill. euro / 2 % av global omsetning), mens brudd på art. 5 – som omfatter integritet og konfidensialitet – faller under nr. 5 (20 mill. / 4 %) **[Merknad – ikke fra kildene, jf. merknad i K34]**. En tredjedel av CNILs sanksjoner i 2023 gjaldt sikkerhetsplikten [K34 s. 1](../kilder/K34-cnil-cybersikkerhet-2024.md).

**Norsk rett og offentlig sektor:** Personopplysningsloven inkorporerer GDPR. For statlige virksomheter krever eForvaltningsforskriften § 15 internkontroll på informasjonssikkerhetsområdet basert på anerkjente standarder og tilpasset risiko; økonomiregelverket og sikkerhetsloven kan gi tilleggskrav [K16 s. 10–12](../kilder/K16-dfo-veileder-informasjonssikkerhet.md). NSMs grunnprinsipper er anbefalinger, ikke regelverk; sikkerhetsloven og sektorregelverk kan stille strengere krav [K32 s. 1](../kilder/K32-nsm-grunnprinsipper.md).

## Utdyping

### 1. Hva betyr «egnede tiltak»? Den risikobaserte tilnærmingen

**Risikoen som skal styres er risikoen for den registrerte.** Art. 32 viser til risiko for «fysiske personers rettigheter og friheter». NSM-katalogen ([K32](../kilder/K32-nsm-grunnprinsipper.md)) er skrevet ut fra virksomhetens perspektiv (beskytte informasjonssystemer mot uautorisert tilgang, skade eller misbruk, s. 3) og nevner ikke GDPR [K32, Aktualitet](../kilder/K32-nsm-grunnprinsipper.md). SDM påpeker at informasjonssikkerhetsmodeller som BSI IT-Grundschutz primært beskytter organisasjonen, mens personvern tar den registrertes perspektiv – og at SDM-nivået går foran ved avvik [K37 9.4](../kilder/K37-sdm-standard-datavernmodell.md). CNIL advarer mot å «glemme konsekvensene for de registrerte og bare vurdere konsekvensene for virksomheten» [K33 ark 20 s. 49](../kilder/K33-cnil-sikkerhetsguide.md). Se [T09](T09-risikovurdering-metoder-og-skalaer.md) for hvordan de to perspektivene kombineres.

**Momenter i vurderingen av «egnet»:**

| Moment | Hvordan det påvirker tiltaksnivået | Kilde |
|---|---|---|
| Opplysningenes art | Særlige kategorier, fødselsnummer, opplysninger om mange → kryptering ved overføring nødvendig; særlige kategorier gir som hovedregel «høyt» beskyttelsesnivå | [K10](../kilder/K10-dt-kryptering.md), [K37 9.3](../kilder/K37-sdm-standard-datavernmodell.md) |
| Omfang | Store datamengder og mange roller/rettigheter kan løfte beskyttelsesnivået fra normal til høy (kumulativ effekt) | [K37 9.5](../kilder/K37-sdm-standard-datavernmodell.md) |
| Den registrertes avhengighet | Avhengighet av virksomhetens beslutninger/tjenester (helse, ytelser) → høyt/svært høyt nivå | [K37 9.3](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md) |
| Eksponering | Åpent mot internett, utveksling med utlandet, sammenkoblinger, heterogent/variabelt system → høyere sannsynlighet | [K30 §1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Risikokilder | Trusselaktørers intensjon og kapasitet; interne og legitime brukere er også risikokilder | [K18 vedlegg H](../kilder/K18-digdir-retningslinje-risiko.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md) |
| Teknologiens stand | Tiltakene må oppdateres med «state of the art»; referansekataloger revideres løpende | [K37 kap. 12](../kilder/K37-sdm-standard-datavernmodell.md), [K35 EC02](../kilder/K35-cnil-referentiel-audit.md) |
| Kostnad | Nytte/kost-prinsippet: tiltak velges hvis de har vesentlig positiv nytte/kost; ALARP for liv og helse | [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md) |

**Grunnsikring først.** CNIL anbefaler et sikkerhetsfundament basert på god praksis, supplert med behandlingsspesifikke tiltak fra risikoanalysen [K33 s. 4](../kilder/K33-cnil-sikkerhetsguide.md). SDM fremhever at konfidensialitet må sikres selv ved lav inngrepsintensitet, og at tiltaksvalget da i stor grad tilsvarer grunnsikringstiltak [K37 9.2](../kilder/K37-sdm-standard-datavernmodell.md). Praktisk betyr dette: **M09-sjekklisten gir grunnsikringen, risikovurderingen (M03) gir tilleggstiltakene.**

**Rekkefølge for tiltaksvalg** (CNIL) [K28 s. 13](../kilder/K28-cnil-pia-metode.md):
1. Styring (organisering, policy, risikostyring, prosjektstyring).
2. Personopplysningene (minimere, anonymisere) – forebygger bruddet.
3. Potensielle konsekvenser (sikkerhetskopier, integritetskontroll, avvikshåndtering).
4. Risikokildene (fysisk og logisk tilgangskontroll, kryptering, logging, tredjepartsstyring, skadevarevern).
5. Støtteressursene (drift, overvåking, kanaler, sårbarheter i programvare, maskinvare, papir).

**Skalering ved høyere beskyttelsesbehov** (SDM): øk tiltakets *virkning* (f.eks. lengre nøkler) eller *påliteligheten* i utførelsen (robusthet mot tekniske feil, brukerfeil, force majeure, ofte med organisatoriske tiltak) [K37 9.7](../kilder/K37-sdm-standard-datavernmodell.md).

**Å ha et tiltak er ikke nok.** Et rettighets- og rollekonsept sikrer ikke konfidensialitet hvis rettigheter tildeles for generøst; virksomheten må forklare *hvordan* tiltaket virker i det konkrete systemet [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md). NSM: «Sikkerhetstiltakene er riktig implementert, men er de riktige tiltakene implementert på rett sted?» [K32 s. 12](../kilder/K32-nsm-grunnprinsipper.md).

### 2. Organisatoriske tiltak vs. tekniske tiltak

DFØ skiller **styringsaktiviteter** (vurdere og håndtere risiko, beslutte, prioritere, følge opp – ISO/IEC 27001 kap. 4–10) fra **sikkerhetstiltak** (varige tiltak – organisatoriske, menneskelige, tekniske; ISO/IEC 27002, NSMs grunnprinsipper) [K16 s. 9](../kilder/K16-dfo-veileder-informasjonssikkerhet.md). Digdirs internkontrollmodell har syv områder: ledelsens styring og oppfølging, risikovurdering, risikohåndtering, overvåking og hendelseshåndtering, måling/evaluering/revisjon, kompetanse og kulturutvikling, kommunikasjon [K16 s. 5](../kilder/K16-dfo-veileder-informasjonssikkerhet.md). CNIL deler tiltak i *organisatoriske*, *logiske* og *fysiske* [K28 s. 12](../kilder/K28-cnil-pia-metode.md), og PIA-malene i *data-spesifikke*, *generelle* og *organisatoriske* sikkerhetstiltak [K30 kap. 2–43, kolonnen «Mal»](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md).

**[Merknad – ikke fra kildene]** ISO/IEC 27001:2022 Annex A grupperer tiltakene i fire temaer – organisatoriske, menneskelige (personellrelaterte), fysiske og teknologiske – som svarer godt til inndelingen over. ISO/IEC 27701 utvider ISMS til et styringssystem for personvern (PIMS); CNIL nevner 27701 som vei til kontinuerlig forbedring [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md).

### 3. Samlet tiltaksoversikt per tema

Under er tiltakene per tema. Hvert tema har (a) kjernetiltak, (b) konkrete terskler/parametere fra kildene, (c) typiske feil. Full kryssreferanse finnes i tabellen i avsnitt 4.

#### 3.1 Styring, policy og risikostyring

- Ledelsen skal fastsette mål, policy, ansvar og **toleransegrenser for risiko** (risikoaksept), og det skal finnes en risikoprosess (verdivurdering, trusselvurdering, eksisterende tiltak, risikoidentifisering, -vurdering, -rapportering, -håndtering, verifisering av at tiltakene virker) [K32 1.1.2–1.1.4](../kilder/K32-nsm-grunnprinsipper.md).
- **Handlingsplan** med frist og ansvarlig for hvert tiltak; **ledelsens gjennomgang minst årlig** (endret kontekst, trusler, hendelser, klager, fremdrift i juridisk og teknisk handlingsplan) [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md).
- Personvernpolicy med tematiske retningslinjer; formell prosedyre for unntak; etterlevelseskontroll **minst årlig** [K30 kap. 28](../kilder/K30-cnil-pia-kunnskapsbaser.md). Oppfølgingskomité minst årlig; risikokart oppdatert minst årlig og ved hver ny behandling [K30 kap. 21, 27](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- Utnevn CISO og personvernombud med reell tilgang til ledelsen [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md), [K30 kap. 27](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- Statlige virksomheter: internkontroll etter eForvaltningsforskriften § 15 [K16](../kilder/K16-dfo-veileder-informasjonssikkerhet.md).
- *Feil:* sikkerhet som ettertanke; tiltak uten helhetssyn; kun tekniske tiltak; handlingsplan uten frist/ansvarlig [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md).

#### 3.2 Oversikt over behandlinger, systemer, enheter og dataflyt

- Kartlegg leveranser, systemer, data og eierskap, interne og eksterne avhengigheter, og **informasjonsflyt/dataflyt** [K32 1.1.5–1.1.6](../kilder/K32-nsm-grunnprinsipper.md); enheter og programvare inkl. ikke-støttede produkter og virtuelle enheter i sky [K32 1.2.1–1.2.4](../kilder/K32-nsm-grunnprinsipper.md).
- Identifiser via protokollen behandlinger, data og støtteressurser (maskinvare, programvare, sky, kanaler, papir, lokaler); formaliser **dataflytdiagrammer** og oppdater ved endringer [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md). Kartlegg også SaaS og fjern ubrukte skyressurser [K33 ark 22](../kilder/K33-cnil-sikkerhetsguide.md).
- Inventar med OS, IP/MAC, versjoner og patcher [K30 kap. 37, 40.1](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- SDM: åpenhet krever dokumentasjon av forretningsprosesser, databeholdninger, dataflyt, IT-systemer og grensesnitt [K37 7.6, kap. 8](../kilder/K37-sdm-standard-datavernmodell.md).
- Dette grunnlaget brukes også i protokollen (art. 30) og DPIA-ens systematiske beskrivelse [K32 Praktiske sjekkpunkter](../kilder/K32-nsm-grunnprinsipper.md).

#### 3.3 Tilgangsstyring (autorisasjon)

- **Minste privilegium** og tjenstlig behov; alle kontoer sporbare til person og til den som godkjente; jevnlig revisjon [K32 2.6.1](../kilder/K32-nsm-grunnprinsipper.md). Formell livssyklusprosess – **deaktiver fremfor å slette** for revisjonsspor [K32 2.6.2](../kilder/K32-nsm-grunnprinsipper.md). Sentralt verktøy, utløpsdato for innleide, oppfølging av ubrukte kontoer [K32 2.6.3](../kilder/K32-nsm-grunnprinsipper.md).
- Ingen admin-rettigheter til sluttbrukere; separate kontoer for forhøyede rettigheter; domeneadmin aldri interaktivt på klienter/servere («pass the hash») [K32 2.6.4–2.6.5](../kilder/K32-nsm-grunnprinsipper.md).
- Autorisasjonsprofiler med oppgavedeling; leder godkjenner; **gjennomgang minst årlig** [K33 ark 5](../kilder/K33-cnil-sikkerhetsguide.md), [K30 kap. 8.1](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- Partisjonering av data per prosess (f.eks. statistikkavdelingen får ikke navn) [K30 kap. 5](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- SDM: rettighets- og rollekonsept etter nødvendighetsprinsippet, begrensning av skriverettigheter (integritet), separasjon via rollekonsepter (ikke-kobling) [K37 7.3–7.5](../kilder/K37-sdm-standard-datavernmodell.md).
- *Feil:* delte kontoer uten sporing; glemte midlertidige tilganger og kontoer for sluttede [K33 ark 5](../kilder/K33-cnil-sikkerhetsguide.md).

#### 3.4 Autentisering og passord

- **MFA** minst for tilgang til kritiske data/systemer og for driftsbrukere [K32 2.6.7](../kilder/K32-nsm-grunnprinsipper.md); MFA der mulig, særlig ved tilgang utenfra [K33 ark 4](../kilder/K33-cnil-sikkerhetsguide.md). Bytt alle standardpassord før produksjon; foretrekk sertifikatbasert autentisering [K32 2.3.7](../kilder/K32-nsm-grunnprinsipper.md).
- **CNILs passordregler (2024)** [K33 ark 4](../kilder/K33-cnil-sikkerhetsguide.md): entropi **80 bit** for passord alene (f.eks. min. 12 tegn med fire tegntyper, eller 14 tegn med store/små bokstaver og tall); **50 bit** med tilleggstiltak (forsinkelse, captcha, sperring etter 10 feil); **13 bit** for utstyr i brukerens besittelse med sperring etter 3 feil. **Ikke periodisk passordbytte for vanlige brukere** (men for administratorer). Passordhåndterere skal støttes (ikke blokker «lim inn»).
- Lagring: bare hash med dedikert funksjon (**bcrypt, scrypt, Argon2, PBKDF2**) med salt; aldri MD5/SHA-1 [K33 ark 4, 21](../kilder/K33-cnil-sikkerhetsguide.md). NSM: sentral kontroll av passordkvalitet (hindre vanlige ord, årstall, årstider) [K32 2.6.3e](../kilder/K32-nsm-grunnprinsipper.md).
- Biometri er særlig kategori (art. 9) [K33 ark 4](../kilder/K33-cnil-sikkerhetsguide.md), jf. NSMs henvisning til Datatilsynet [K32 2.6.7b](../kilder/K32-nsm-grunnprinsipper.md).
- Motstrid: se «Motstrid mellom kildene» nedenfor (periodisk bytte, sperregrense).

#### 3.5 Logging, sporbarhet og sikkerhetsovervåking

- **Strategi for sikkerhetsovervåking**: formål, hvilke data, sikker oppbevaring, tilgangsstyring, **sletting**, revisjon minst årlig [K32 3.2.1](../kilder/K32-nsm-grunnprinsipper.md). Følg regelverket, avgjør lagringstid, **informer ansatte** [K32 3.2.2](../kilder/K32-nsm-grunnprinsipper.md). Minimum: vellykkede og mislykkede pålogginger, administrasjons- og sikkerhetslogger; på klienter også kjøring av ukjent programvare og rettighetseskalering [K32 3.2.4](../kilder/K32-nsm-grunnprinsipper.md). Loggintegritet: signering, tilgangsstyring, deteksjon av manipulering, felles tidskilde [K32 3.2.6](../kilder/K32-nsm-grunnprinsipper.md). Fjern data uten operasjonell eller sikkerhetsmessig relevans [K32 3.2.7](../kilder/K32-nsm-grunnprinsipper.md). Analyse mot normaltilstand og eskaleringsrutiner [K32 3.3](../kilder/K32-nsm-grunnprinsipper.md).
- **Applikasjonslogger** (CNIL): registrer opprett, les, del, endre og slett med bruker-ID, dato, tid, type operasjon og datareferanse; lagringstid **rullerende 6–12 måneder**; informer brukerne; beskytt mot de som logges; databehandlere skal kontraktsmessig forpliktes til logging [K33 ark 16](../kilder/K33-cnil-sikkerhetsguide.md). K30 anbefaler **seks måneder** for hendelseslogger [K30 kap. 36, 43](../kilder/K30-cnil-pia-kunnskapsbaser.md), tidsstempling i UTC med NTP [K30 kap. 36](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- **Formålsbegrensning:** Å bruke logger til f.eks. å telle arbeidstimer er formålsglidning [K33 ark 16](../kilder/K33-cnil-sikkerhetsguide.md). Logging av ansattes atferd kan gi konflikt mellom sikkerhet og personvern og må begrunnes særskilt [K37 9.4](../kilder/K37-sdm-standard-datavernmodell.md). NSM: «behovet for lagring og tilgang må til enhver tid veies opp mot behovet for personvern» [K32 s. 39](../kilder/K32-nsm-grunnprinsipper.md).
- SDM: logging og et «loggings- og evalueringskonsept» som tar hensyn til de registrertes rettigheter er tiltak for **åpenhet** og revisjonsevne [K37 5.5, 7.6](../kilder/K37-sdm-standard-datavernmodell.md).
- **[Merknad – ikke fra kildene]** I Norge gjelder i tillegg arbeidsmiljølovens kapittel 9 om kontrolltiltak og forskrift om innsyn i e-post og annet elektronisk lagret materiale, jf. merknad i [K33](../kilder/K33-cnil-sikkerhetsguide.md).

#### 3.6 Kryptering, pseudonymisering og integritetsbeskyttelse

- **Kryptostrategi** (verktøy, sertifikater, nøkkelgenerering, oppbevaring, fornyelse, kompromitterte nøkler) [K32 2.7.1](../kilder/K32-nsm-grunnprinsipper.md); kun anbefalte algoritmer og nøkkellengder (NSM Cryptographic Recommendations) [K32 2.7.2](../kilder/K32-nsm-grunnprinsipper.md); krypter mobile lagringsmedier [K32 2.7.3](../kilder/K32-nsm-grunnprinsipper.md); krypter overføring av konfidensiell informasjon eller ved lav kanaltillit [K32 2.7.4](../kilder/K32-nsm-grunnprinsipper.md); definer sikringsnivå per informasjonstype [K32 2.7.5](../kilder/K32-nsm-grunnprinsipper.md). Krypter alle trådløse og kablede forbindelser utenfor fysisk kontroll [K32 2.4.2](../kilder/K32-nsm-grunnprinsipper.md).
- **Når kryptering er nødvendig** (Datatilsynet): overføring av særlige kategorier, fødselsnummer, opplysninger om mange og opplysninger klassifisert som beskyttelsesverdige; samtykke fra kunden kan *ikke* senke kravet [K10](../kilder/K10-dt-kryptering.md). Tre elementer må alle være gode: algoritme, tillit til kryptomodul, nøkkelforvaltning [K10](../kilder/K10-dt-kryptering.md).
- **Algoritmer** (CNIL 2024): SHA-2/SHA-3; bcrypt/scrypt/Argon2/PBKDF2; AES (CCM/GCM/EAX) eller ChaCha20-Poly1305; RSA-OAEP; RSA-SSA-PSS/ECDSA; AES 128–256, RSA ≥ 2048/3072. Unngå DES, 3DES, MD5, SHA-1 [K33 ark 21](../kilder/K33-cnil-sikkerhetsguide.md). TLS 1.3, minst 1.2 [K33 ark 9](../kilder/K33-cnil-sikkerhetsguide.md).
- **Sky:** Bruker man leverandørens nøkkelhåndtering, kan leverandøren få tilgang; «serverside-kryptering gir ikke konfidensialitet overfor leverandøren» [K33 ark 22 s. 53](../kilder/K33-cnil-sikkerhetsguide.md). Der konfidensialitet overfor leverandøren kreves, er klientsidekryptering med brukerkontrollerte nøkler modellkravet [K36 ES16–ES17](../kilder/K36-cnil-referentiel-digital-safe.md).
- **Hemmeligheter separat:** send nøkkel/passord via en annen kanal enn dataene [K33 ark 13](../kilder/K33-cnil-sikkerhetsguide.md), [K10](../kilder/K10-dt-kryptering.md), [K30 kap. 38.1](../kilder/K30-cnil-pia-kunnskapsbaser.md); passord for krypterte filer skal ikke være fødselsnummer [K10](../kilder/K10-dt-kryptering.md).
- **Integritet:** hash mot feil, MAC mot endring fra personer uten nøkkel, e-signatur mot endring fra andre enn signataren [K30 kap. 7](../kilder/K30-cnil-pia-kunnskapsbaser.md); sjekksummer, segl og signaturer etter et kryptokonsept [K37 7.3](../kilder/K37-sdm-standard-datavernmodell.md).
- **Pseudonymisering/anonymisering** er SDM-tiltak for ikke-kobling og dataminimering [K37 7.1, 7.5](../kilder/K37-sdm-standard-datavernmodell.md), [K30 kap. 2, 26.2](../kilder/K30-cnil-pia-kunnskapsbaser.md).

#### 3.7 Sikkerhetskopiering og gjenoppretting

- **Plan** som minimum: hvilke data, hyppighet etter verdi, ansvar, prosedyre ved feilet kopiering, oppbevaringsperiode, sikring av kopiene, **krav til gjenopprettingstid**, godkjenner [K32 2.9.1](../kilder/K32-nsm-grunnprinsipper.md). Kopier også konfigurasjon, maler og installasjonsprogramvare [K32 2.9.2](../kilder/K32-nsm-grunnprinsipper.md). **Test** med gjenopprettingstest [K32 2.9.3](../kilder/K32-nsm-grunnprinsipper.md). Beskytt kopiene: separert fra produksjon, begrenset tilgang, jevnlige **offline-kopier**, kryptert lagring og flytting [K32 2.9.4](../kilder/K32-nsm-grunnprinsipper.md).
- CNIL: minst én kopi **geografisk adskilt** og minst én **offline**; samme sikkerhetsnivå som drift; **3-2-1-regelen** (3 kopier, 2 medier, 1 offline) [K33 ark 17](../kilder/K33-cnil-sikkerhetsguide.md). Daglig inkrementell/ukentlig full som eksempel; test **utvalg månedlig, full gjenoppretting årlig**; bekreft lagringsland [K30 kap. 33](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- Sletting i backup: modellkrav om sletting i sikkerhetskopier innen én måned [K36 ES05](../kilder/K36-cnil-referentiel-digital-safe.md); slett også i backup der relevant [K30 kap. 26.2](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- *Feil:* backup på samme system uten isolering (løsepengevirus rammer begge), backup i samme datasenter, aldri teste [K33 ark 17, 22](../kilder/K33-cnil-sikkerhetsguide.md).

#### 3.8 Kontinuitet, robusthet og tilgjengelighet

- Robust arkitektur for kritiske funksjoner: risikovurder maskinvarefeil, driftsfeil, angrep, tjenestenekt, leverandørtilgjengelighet, strøm, naturskade og geopolitikk; dupliser kritiske komponenter [K32 2.2.7](../kilder/K32-nsm-grunnprinsipper.md). Konsekvensanalyse (BIA) med krav til gjenopprettingstid, tap av data og tjenestenivå [K32 4.1.1–4.1.2](../kilder/K32-nsm-grunnprinsipper.md).
- Kontinuitetsplan (BCP) og katastrofegjenopprettingsplan (DRP); **personvernnivået skal ikke reduseres i nødmodus**; UPS, RAID [K33 ark 18](../kilder/K33-cnil-sikkerhetsguide.md). PRA/PCA ut fra tilgjengelighetsmål [K30 kap. 37](../kilder/K30-cnil-pia-kunnskapsbaser.md); beskyttelse mot brann, vann (utstyr minst 15 cm over gulv), temperatur og strøm [K30 kap. 29](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- SDM: tilgjengelighet = backup etter testet konsept, redundans, reparasjonsstrategier, alternative prosesser, stedfortredere [K37 7.2](../kilder/K37-sdm-standard-datavernmodell.md). Tilgjengelighet måles etter de registrertes interesse [K37 10.2](../kilder/K37-sdm-standard-datavernmodell.md).

#### 3.9 Sikker konfigurasjon, sårbarhetshåndtering og skadevarevern

- Sentralt styrt **patching** så fort som mulig, med prioriteringsliste og ansvar når oppdatering utsettes; isoler det som ikke kan oppdateres [K32 2.3.1, 2.5.4](../kilder/K32-nsm-grunnprinsipper.md). Kun kjent programvare kjører (godkjentlisting), makrokontroll [K32 2.3.2](../kilder/K32-nsm-grunnprinsipper.md). Deaktiver unødvendig funksjonalitet, standard sikkerhetskonfigurasjoner, verifisering mot godkjent konfigurasjon (helst nattlig) [K32 2.3.3–2.3.5](../kilder/K32-nsm-grunnprinsipper.md). Sikker tid [K32 2.3.9](../kilder/K32-nsm-grunnprinsipper.md); IoT-tiltak [K32 2.3.10](../kilder/K32-nsm-grunnprinsipper.md).
- **Sårbarhetsskanning** og etterretning, antiskadevare/IDS [K32 3.1.1–3.1.3](../kilder/K32-nsm-grunnprinsipper.md).
- CNIL: oppdateringer for offentlig kjente kritiske sårbarheter **uten opphold** (etter testing), **ukentlig automatisk sjekk** [K33 ark 6, 9](../kilder/K33-cnil-sikkerhetsguide.md); automatisk skjermlås; programvarebrannmur; ingen OS uten leverandørstøtte [K33 ark 6](../kilder/K33-cnil-sikkerhetsguide.md). Antivirus som brukeren ikke kan slå av, full skanning minst ukentlig [K30 kap. 23](../kilder/K30-cnil-pia-kunnskapsbaser.md). Skjermsparer maks 15 min [K30 kap. 19.1](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- SDM: beskyttelse mot ytre påvirkning (skadevare, sabotasje) er tilgjengelighets- og konfidensialitetstiltak [K37 7.2, 7.4](../kilder/K37-sdm-standard-datavernmodell.md).

#### 3.10 Nettverk, segmentering og dataflytkontroll

- Soneinndeling etter risikoprofil; klienter adskilt fra servere; tilgang basert på både bruker og enhet [K32 2.2.3–2.2.6](../kilder/K32-nsm-grunnprinsipper.md). Tilgangskontroll på nettverksporter; WPA2/WPA3 enterprise; vertsbrannmur med logging [K32 2.4](../kilder/K32-nsm-grunnprinsipper.md). Styr dataflyt mellom soner, sperr klient-til-klient-trafikk, isoler sårbart utstyr, kontroller trafikk mot leverandører [K32 2.5](../kilder/K32-nsm-grunnprinsipper.md).
- CNIL: **ingen administrasjonsgrensesnitt direkte på internett**; VPN med sterk autentisering for fjerntilgang; minst to soner (internt nett og DMZ); ingen Telnet; ingen WEP [K33 ark 8](../kilder/K33-cnil-sikkerhetsguide.md). **Databaser skal ikke være direkte tilgjengelige fra internett** [K33 ark 9–10](../kilder/K33-cnil-sikkerhetsguide.md).
- SDM: lukke eller dokumentere grensesnitt (ikke-kobling); kontroll av godkjente kommunikasjonskanaler (konfidensialitet) [K37 7.4–7.5, kap. 8](../kilder/K37-sdm-standard-datavernmodell.md).

#### 3.11 Arbeidsstasjoner, mobile enheter og BYOD

- Forvaltede vs. ikke-forvaltede enheter; ikke-forvaltede får begrenset tilgang [K32 begreper s. 8, 2.2.6, 2.5.2](../kilder/K32-nsm-grunnprinsipper.md). Trafikk fra mobile klienter via virksomhetens nett [K32 2.5.8](../kilder/K32-nsm-grunnprinsipper.md).
- CNIL: kryptering av mobile/flyttbare lagringsmedier; VPN; autolås på smarttelefoner; BYOD bare ut fra identifiserte risikoer og regulert i IT-reglementet; ikke krenke privatlivet i den personlige delen [K33 ark 7](../kilder/K33-cnil-sikkerhetsguide.md). Fjernhjelp bare med brukerens samtykke og synlig indikasjon [K33 ark 6](../kilder/K33-cnil-sikkerhetsguide.md), [K30 kap. 24.2](../kilder/K30-cnil-pia-kunnskapsbaser.md). Autolås 1–5 min på telefoner [K30 kap. 19.3](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- Harddiskkryptering er standard i moderne OS (BitLocker, FileVault) [K10](../kilder/K10-dt-kryptering.md).

#### 3.12 Nettsteder, e-post og API

- E-post: DMARC, DKIM, SPF, DNSSEC, STARTTLS; kun støttede klienter/nettlesere og godkjente programtillegg [K32 2.8](../kilder/K32-nsm-grunnprinsipper.md). Disse er «viderekommende» – innfør først 2.1.2, 2.3.1, 2.3.2, 2.6.4a og 2.5.1 [K32 s. 33](../kilder/K32-nsm-grunnprinsipper.md).
- Nettsted: TLS på alle sider med autentisering eller personopplysninger; HttpOnly og Secure på informasjonskapsler; ingen personopplysninger i URL; ikke avsløre om en konto finnes; beskytt mot OWASP Top 10 [K33 ark 10](../kilder/K33-cnil-sikkerhetsguide.md). Cookies maks 13 måneder, SameSite, Content-Security-Policy [K30 kap. 41](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- API: skill vanlige kall fra administrasjonskall, dataminimering, logging mot misbruk, digitale hvelv for API-nøkler, test mot OWASP API Security Top 10 [K33 ark 25](../kilder/K33-cnil-sikkerhetsguide.md).
- **Vanligste tilsynsfunn hos CNIL:** data tilgjengelig ved å endre URL; passordpolicy; passord i klartekst; HTTP; manglende skjermlås; manglende sårbarhetstesting før produksjon [K34 s. 2](../kilder/K34-cnil-cybersikkerhet-2024.md).

#### 3.13 Anskaffelse, utvikling og endringshåndtering

- Sikkerhetskrav i anskaffelser gjennom hele livsløpet; moderne, støttede produkter; sertifiserte produkter; vern mot manipulasjon i leverandørkjeden [K32 2.1.1–2.1.4](../kilder/K32-nsm-grunnprinsipper.md). Sikker utviklingsmetode, separate miljøer, testing, kodevedlikehold (OWASP) [K32 2.1.5–2.1.8](../kilder/K32-nsm-grunnprinsipper.md).
- **Testdata:** Sensitive produksjonsdata bare i sikret test-/utviklingsmiljø [K32 2.1.6](../kilder/K32-nsm-grunnprinsipper.md); CNIL: fiktive eller anonymiserte data i utvikling og test, pre-produksjon med ekte data bare sikret som produksjon [K33 ark 11](../kilder/K33-cnil-sikkerhetsguide.md); forby reelle data før produksjon [K30 kap. 20.2](../kilder/K30-cnil-pia-kunnskapsbaser.md). Se motstrid nedenfor.
- Ingen hemmeligheter i versjonskontroll; personvernvennlige standardinnstillinger; unngå fritekstfelt [K33 ark 11](../kilder/K33-cnil-sikkerhetsguide.md). KI: datakvalitet, beskyttelse mot modellinversjon, kontroll av output for personopplysninger [K33 ark 24](../kilder/K33-cnil-sikkerhetsguide.md). Mobilapper: OS-nøkkellager, minimere tillatelser, kontroll av SDK-er [K33 ark 23](../kilder/K33-cnil-sikkerhetsguide.md).
- **Endringshåndtering:** vurder endringsforslag mot etablerte tiltak, test før/etter, involver sikkerhetspersonell, minimumskrav også for **hasteendringer** [K32 2.10](../kilder/K32-nsm-grunnprinsipper.md). Endringer skal utløse oppdatert risikovurdering/DPIA [K24](../kilder/K24-wp248-dpia.md), [K12 s. 3–4](../kilder/K12-dt-dpia-veiledning.md).
- Innebygd personvern: [T13](T13-innebygd-personvern-art25.md), [K13](../kilder/K13-dt-innebygd-personvern.md).

#### 3.14 Leverandørstyring, databehandlere og sky

- **NSM 2.1.10 – minimumsundersøkelser av tjenesteleverandør:** a) ISMS/sertifisering (f.eks. ISO/IEC 27001), b) innsyn i sikkerhetsarkitektur, c) utviklingsplaner for sikkerhetsfunksjonalitet, d) hvem som har innsyn, hvor og hvordan data behandles og lagres, segregering fra andre kunder, e) sikkerhetsfunksjonalitet som dekker behovene, f) sikkerhetsovervåking, g) hendelseshåndtering og avviksrapportering, h) beredskapsplaner som harmonerer, i) godkjenning av underleverandører, j) aktiviteter ved terminering (tilbakeføring, flytting, sletting) [K32 2.1.10](../kilder/K32-nsm-grunnprinsipper.md). Bestillerkompetanse og risikovurdering før tjenesteutsetting [K32 2.1.9, s. 9](../kilder/K32-nsm-grunnprinsipper.md).
- **CNIL ark 14 – kontraktsinnhold:** konfidensialitetsansvar, minimumskrav til autentisering, tilbakelevering og destruksjon, varsling av hendelser «så snart som mulig», bistand med art. 32, jevnlig gjennomgang og revisjon av tiltak; midler til verifisering (revisjon, stedlige besøk); vurder hele underleverandørkjeden; sertifisering (27001/27701) er bare første indikator – kontroller scope [K33 ark 14](../kilder/K33-cnil-sikkerhetsguide.md). Logging skal kontraktsfestes [K33 ark 16](../kilder/K33-cnil-sikkerhetsguide.md).
- **CNIL K30 kap. 34:** sikkerhetspolicy og sertifiseringer vedlagt avtalen; eksakte operasjoner, lagringstid, sluttoperasjoner; regulering av underdatabehandlere; for sky i tillegg logisk separasjon og **både lagringsland og land administratorene aksesserer fra** [K30 kap. 34.3](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- **Sky (ark 22):** konfigurer leverandørens sikkerhetsverktøy etter egen policy; ingen kontrakt som lar leverandøren få tilgang for egne formål uten kundens tillatelse; glem ikke telemetri; backup ikke i samme datasenter [K33 ark 22](../kilder/K33-cnil-sikkerhetsguide.md).
- **Datatilsynet:** minimumskrav til sikkerhetstiltak i eget vedlegg til databehandleravtalen [K05](../kilder/K05-dt-databehandleravtale.md).
- **Revisjon av leverandør:** kompetanse (juridisk og teknisk), konfidensialitetsklausul, anonymisering av bevis, sletting av revisjonsdokumentasjon [K35 EM11–EM37](../kilder/K35-cnil-referentiel-audit.md); innholdskrav EC29–EC32 om sikkerhet [K35](../kilder/K35-cnil-referentiel-audit.md).
- Overføring utenfor EØS: [T11](T11-overforing-tredjeland-og-tia.md).

#### 3.15 Vedlikehold, fjerntilgang og avhending

- Loggbok over vedlikehold; fjernvedlikehold bare på forespørsel, tidsbegrenset og lukket etterpå; ingen permanent fjerntilgang; tredjepartsinngrep overvåket; **sikker sletting før kassering, reparasjon eller retur av leasingutstyr** [K33 ark 15](../kilder/K33-cnil-sikkerhetsguide.md). Eksempelklausul for tredjepartsvedlikehold [K33 ark 15 s. 38](../kilder/K33-cnil-sikkerhetsguide.md).
- Krypterte kanaler for fjernvedlikehold; krypter/slett data før ekstern reparasjon; destruksjonsrapport oppbevares 10 år [K30 kap. 24, 40](../kilder/K30-cnil-pia-kunnskapsbaser.md). SSD/flash: krypter, formater, krypter på nytt med annen nøkkel [K30 kap. 40.4](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- NSM: regulere leverandørers fysiske adgang [K32 2.1.4e](../kilder/K32-nsm-grunnprinsipper.md); overvåk leverandørs vedlikeholdskonto [K32 2.6.3d](../kilder/K32-nsm-grunnprinsipper.md).

#### 3.16 Fysisk sikring og miljø

- NSM dekker fysisk sikkerhet «i liten grad» [K32 s. 5](../kilder/K32-nsm-grunnprinsipper.md); relevante NSM-punkter er fysisk tilgjengelighet for svitsjer/kabler [K32 2.4.3](../kilder/K32-nsm-grunnprinsipper.md) og fysisk adskilte nett [K32 2.2.4](../kilder/K32-nsm-grunnprinsipper.md).
- CNIL: låste dører, innbruddsalarm med periodisk test, brannsikring, soner etter risiko, liste over autoriserte per sone, eskorte av besøkende, beskyttelse av nettverksuttak; logg adgang til kritiske rom (etter informasjon) [K33 ark 12](../kilder/K33-cnil-sikkerhetsguide.md). Sonemodell publikum/tjeneste/sikkerhet, adgangslogg maks tre måneder tilbake [K30 kap. 6](../kilder/K30-cnil-pia-kunnskapsbaser.md). Avstand til farlige produkter og områder [K30 kap. 10](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- SDM: «egnede omgivelser (bygg, rom)» [K37 7.4](../kilder/K37-sdm-standard-datavernmodell.md).

#### 3.17 Personell, opplæring og bevissthet

- IT-reglement med bindende kraft (passord, melde brudd, låse maskin, ikke installere programvare, kopiering til flyttbare medier) [K33 ark 2](../kilder/K33-cnil-sikkerhetsguide.md); konfidensialitetserklæring – eksempelklausul [K33 ark 2 s. 10](../kilder/K33-cnil-sikkerhetsguide.md). **Art. 32 nr. 4** (instruksbundet behandling) kan oppfylles gjennom slike instrukser og taushetserklæringer **[Merknad – ikke fra kildene: koblingen er utledet]**.
- Opplæring og bevisstgjøring tilpasset roller, inkl. eksterne leverandører; kunnskapstest; øvelser [K33 ark 3](../kilder/K33-cnil-sikkerhetsguide.md). Kvalifisert personell, tilstrekkelige ressurser, bevissthet om sosial manipulering [K30 kap. 18](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- NSM: opplæringskrav i hendelsesplanverk og reelle historier i opplæring [K32 4.1.1c, 4.4.4](../kilder/K32-nsm-grunnprinsipper.md); passord er personlige og deles aldri [K32 2.6.1g](../kilder/K32-nsm-grunnprinsipper.md).
- SDM: autorisert personell skal være påviselig ansvarlige, kvalifiserte, pålitelige og uten interessekonflikt; taushetsplikt og konfidensialitetsavtaler [K37 7.4](../kilder/K37-sdm-standard-datavernmodell.md).
- Papir: merking, sikker oppbevaring, makulering (DIN 32757 minst nivå 3), sporing i papirkanaler [K30 kap. 39](../kilder/K30-cnil-pia-kunnskapsbaser.md).

#### 3.18 Hendelseshåndtering og brudd på personopplysningssikkerheten

- **Planverk** med BIA, roller, opplæring, **klassifiseringsregime**, test/øving, revisjon minst årlig [K32 4.1.1](../kilder/K32-nsm-grunnprinsipper.md); avtaler med eksterne støttespillere [K32 4.1.4](../kilder/K32-nsm-grunnprinsipper.md); vurder og klassifiser [K32 4.2](../kilder/K32-nsm-grunnprinsipper.md); logg tidslinje og sikre bevis [K32 4.3.3](../kilder/K32-nsm-grunnprinsipper.md); lær av hendelser [K32 4.4](../kilder/K32-nsm-grunnprinsipper.md).
- Datatilsynet: typiske digitale angrep (DDoS, phishing, e-postangrep/credential stuffing, direktørsvindel, løsepengevirus), når de skal meldes, og fire steg ved mistanke om brudd [K15](../kilder/K15-dt-digitale-angrep.md). Se også [T12](T12-avvik-og-brudd-art33-34.md).
- CNIL: inkluder brudd på personopplysningssikkerheten i hendelsesprosessen og **definer kriterier for når en hendelse er et brudd**; intern oversikt over alle brudd; melding innen 72 timer (gjerne i to trinn); varsling av registrerte ved høy risiko [K33 ark 19](../kilder/K33-cnil-sikkerhetsguide.md). Kategorier hendelse/incident/skadelig hendelse/krise; responsplan testes minst hvert annet år [K30 kap. 17](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- Tap av **tilgjengelighet og integritet** er også brudd (f.eks. løsepengevirus, sletting uten backup) – behandlingsansvarlige er lite bevisste på dette [K34 s. 1](../kilder/K34-cnil-cybersikkerhet-2024.md). For sen melding er selv et brudd [K34 s. 2](../kilder/K34-cnil-cybersikkerhet-2024.md).
- Detaljer: [T12](T12-avvik-og-brudd-art33-34.md), [A05](../arbeidsflyter/A05-avvikshandtering.md).

#### 3.19 Testing, revisjon og evaluering (art. 32 nr. 1 bokstav d)

| Aktivitet | Frekvens/innhold | Kilde |
|---|---|---|
| Verifisering av konfigurasjon mot godkjent baseline | Regelmessig, helst automatisk (f.eks. nattlig) | [K32 2.3.5](../kilder/K32-nsm-grunnprinsipper.md) |
| Sårbarhetsskanning | Jevnlig, automatisert | [K32 3.1.1](../kilder/K32-nsm-grunnprinsipper.md) |
| Inntrengingstest | **Minst årlig**, fra utsiden og innsiden | [K32 3.4.4](../kilder/K32-nsm-grunnprinsipper.md) |
| Test av deteksjon og beredskap | **Minst annethvert år** | [K32 3.4.5](../kilder/K32-nsm-grunnprinsipper.md) |
| Gjenopprettingstest av backup | Regelmessig; CNIL: utvalg månedlig, full årlig | [K32 2.9.3](../kilder/K32-nsm-grunnprinsipper.md), [K30 kap. 33](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Ledelsens gjennomgang | Minst årlig | [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md) |
| Sikkerhetsrevisjon | Årlig der mulig, handlingsplan fulgt opp på høyeste nivå | [K30 kap. 21](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Gjennomgang av tilgangsrettigheter | Minst årlig | [K33 ark 5](../kilder/K33-cnil-sikkerhetsguide.md), [K30 kap. 8.1](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Gjennomgang av loggstrategi | Minst årlig og etter større hendelser | [K32 3.2.1h](../kilder/K32-nsm-grunnprinsipper.md) |
| Responsplan for brudd | Test minst hvert annet år | [K30 kap. 17](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Trusselvurdering og uavhengig verifisering (digitale hvelv) | Minst hvert tredje år | [K36 ES10, ES14](../kilder/K36-cnil-referentiel-digital-safe.md) |
| Sårbarhetstesting av nye systemer | Før produksjonssetting | [K34 s. 2](../kilder/K34-cnil-cybersikkerhet-2024.md), [K33 ark 10](../kilder/K33-cnil-sikkerhetsguide.md) |

SDM bruker **mål–faktisk-sammenligning** mot referansetiltak; alternative tiltak må vises å være **funksjonelt likeverdige** [K37 10.3](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md). Revisjonskrav og revisorkompetanse: [K35](../kilder/K35-cnil-referentiel-audit.md).

#### 3.20 Dataminimering, lagringstid og sletting som sikkerhetstiltak

- Ikke dekket av NSM (unntatt sletting av loggdata og bruk av produksjonsdata i test) [K32 3.2.7, 2.1.6](../kilder/K32-nsm-grunnprinsipper.md).
- SDM: dataminimering er det **grunnleggende** beskyttelsesmålet; «tidligst mulig sletting» er det viktigste og mest effektive tiltaket [K37 5.3 s. 11](../kilder/K37-sdm-standard-datavernmodell.md).
- CNIL: tidsbegrenset lagringstid per datakategori; **logisk sletting (statusflagg) er ikke tilstrekkelig** [K30 kap. 9](../kilder/K30-cnil-pia-kunnskapsbaser.md); minimering av innsamling og av selve dataene (EXIF, aggregering, pseudonymisering) [K30 kap. 26](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- Mindre data → lavere alvorlighet ved brudd [K30 kap. 9, 26](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K28 s. 13](../kilder/K28-cnil-pia-metode.md).

### 4. Kryssreferanse NSM ↔ CNIL ↔ SDM per tema

Tabellen viser hvor hvert tema dekkes. **NSM** = tiltaks-ID i [K32](../kilder/K32-nsm-grunnprinsipper.md). **CNIL ark** = faktaark i [K33](../kilder/K33-cnil-sikkerhetsguide.md) (2024). **CNIL PIA** = kapittel i tiltakskatalogen [K30](../kilder/K30-cnil-pia-kunnskapsbaser.md) (2018). **SDM** = beskyttelsesmål i [K37](../kilder/K37-sdm-standard-datavernmodell.md) kap. 7 (DM = dataminimering, T = tilgjengelighet, I = integritet, K = konfidensialitet, IK = ikke-kobling, Å = åpenhet, IV = intervenerbarhet). **Art. 32** = bokstav i art. 32 nr. 1 eller nr. 4 tiltaket særlig støtter **[Merknad – ikke fra kildene: koblingen til art. 32-bokstaver og SDM-mål per tema er utledet]**.

| # | Tema | NSM (K32) | CNIL ark (K33) | CNIL PIA (K30) | SDM-mål (K37) | Art. 32 | Andre |
|---|---|---|---|---|---|---|---|
| 1 | Styring, policy, risikostyring, ledelsens gjennomgang | 1.1.1–1.1.4 | 1, 20 | 21, 27, 28, 35 | Å (dokumentasjon), alle mål (styring) | nr. 1 (innledning), d | [K16](../kilder/K16-dfo-veileder-informasjonssikkerhet.md), [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18](../kilder/K18-digdir-retningslinje-risiko.md) |
| 2 | Oversikt over systemer, data, enheter, dataflyt | 1.1.5–1.1.6, 1.2.1–1.2.4 | 1, 22 | 21, 37, 40.1 | Å (dokumentasjon av dataflyt, systemer, grensesnitt) | nr. 1 b | [K11](../kilder/K11-art30-protokollmaler.md) protokoll |
| 3 | Brukerkartlegging og tilgangsstyring | 1.3.1–1.3.3, 2.6.1–2.6.6 | 5 | 8.1, 5 | K (rolle-/rettighetskonsept), I (begrense skriverettigheter), IK (separasjon) | nr. 1 b, nr. 4 | [K35 EC22–EC23](../kilder/K35-cnil-referentiel-audit.md) |
| 4 | Autentisering, MFA, passord | 2.6.3e, 2.6.7, 2.3.7 | 4, 21 | 8.2–8.4 | K (sikker autentisering) | nr. 1 b | [K36 ES19–ES20](../kilder/K36-cnil-referentiel-digital-safe.md) |
| 5 | Logging, sporbarhet, sikkerhetsovervåking | 3.2.1–3.2.7, 3.3.1–3.3.7, 2.4.4 | 16, 19 | 36, 43 | Å (logging, loggings- og evalueringskonsept), revisjonsevne | nr. 1 b, d | [K36 ES13](../kilder/K36-cnil-referentiel-digital-safe.md) |
| 6 | Kryptering (lagring og overføring) og nøkkelhåndtering | 2.7.1–2.7.5, 2.4.2, 2.3.6 | 7, 9, 13, 21, 22 | 4, 38 | K (kryptokonsept), I (signaturer) | nr. 1 a | [K10](../kilder/K10-dt-kryptering.md), [K36 ES16–ES18](../kilder/K36-cnil-referentiel-digital-safe.md) |
| 7 | Integritetskontroll (hash, MAC, signatur, inndatavalidering) | 2.3.5, 3.2.6 | 10, 11, 21 | 7, 30 | I | nr. 1 b | – |
| 8 | Pseudonymisering, anonymisering, partisjonering | – | 11 | 2, 5, 26.2 | IK, DM | nr. 1 a | [K40 tabell 1](../kilder/K40-dpia-prosess-uld.md) |
| 9 | Sikkerhetskopiering og gjenoppretting | 2.9.1–2.9.4 | 17 | 33 | T | nr. 1 c | [K36 ES05, ES12](../kilder/K36-cnil-referentiel-digital-safe.md) |
| 10 | Kontinuitet, redundans, BIA | 2.2.7, 4.1.1–4.1.2 | 18 | 37, 29 | T (redundans, reparasjonsstrategier, stedfortredere) | nr. 1 b (robusthet), c | – |
| 11 | Sikker konfigurasjon, herding, patching | 2.3.1–2.3.10, 2.1.2 | 6, 9 | 19, 37 | I, T | nr. 1 b | [K34 s. 2](../kilder/K34-cnil-cybersikkerhet-2024.md) |
| 12 | Sårbarhetshåndtering og skadevarevern | 3.1.1–3.1.3 | 6, 9 | 23, 19.1 | T, K (beskyttelse mot ytre påvirkning) | nr. 1 b, d | – |
| 13 | Nettverk, segmentering, dataflytkontroll | 2.2.3–2.2.6, 2.4.1–2.4.4, 2.5.1–2.5.8 | 8 | 38 | K (kontroll av kanaler), IK (lukke grensesnitt) | nr. 1 b | – |
| 14 | Arbeidsstasjoner, mobile enheter, BYOD, flyttbare medier | 1.2.3, 2.2.6, 2.5.2, 2.5.8, 2.7.3 | 6, 7 | 19, 40.3–40.4 | K, T | nr. 1 a, b | [K10](../kilder/K10-dt-kryptering.md) |
| 15 | Nettsteder, e-post, API | 2.8.1–2.8.4 | 10, 13, 25 | 38.14, 41 | K, I | nr. 1 b | [K34 s. 2](../kilder/K34-cnil-cybersikkerhet-2024.md) |
| 16 | Anskaffelse, sikker utvikling, testdata | 2.1.1–2.1.8 | 11, 23, 24 | 20 | I (spesifikasjon og testing), DM, IK (forby bakdører) | nr. 1 b, d | [K13](../kilder/K13-dt-innebygd-personvern.md), art. 25 |
| 17 | Endringshåndtering | 2.10.1–2.10.4 | 1 | 20, 28 | I, IV (dokumentert håndtering av endringer) | nr. 1 d | [K24](../kilder/K24-wp248-dpia.md) (DPIA ved endring) |
| 18 | Leverandørstyring, databehandlere, sky | 2.1.9–2.1.10, 2.5.7, 4.1.4 | 14, 22 | 32, 34 | Å (dokumentasjon av kontrakter), K (kontraktsforpliktelser) | nr. 1 (hele), nr. 4 | [K05](../kilder/K05-dt-databehandleravtale.md), [K35](../kilder/K35-cnil-referentiel-audit.md), [K36](../kilder/K36-cnil-referentiel-digital-safe.md) |
| 19 | Vedlikehold, fjerntilgang, avhending | 2.1.4e, 2.3.6, 2.6.3d | 15 | 24, 40 | K, DM (sletting) | nr. 1 b | – |
| 20 | Fysisk sikring og miljøvern | 2.2.4, 2.4.3 (begrenset dekning) | 12 | 6, 10, 29 | K (egnede omgivelser), T (force majeure) | nr. 1 b, c | – |
| 21 | Personell, IT-reglement, opplæring, taushetsplikt | 2.6.1g, 4.1.1c, 4.1.3d, 4.4.4 | 2, 3 | 18, 32.2 | K (kvalifisert, pålitelig personell; taushetsplikt) | nr. 4 | – |
| 22 | Hendelseshåndtering og brudd | 4.1.1–4.1.6, 4.2.1–4.2.3, 4.3.1–4.3.6, 4.4.1–4.4.4 | 19 | 17 | I, IV (dokumentert håndtering av feil), Å | nr. 1 c, d | [K34](../kilder/K34-cnil-cybersikkerhet-2024.md), art. 33–34 |
| 23 | Testing, revisjon, evaluering | 2.3.5, 2.9.3, 3.1.1, 3.4.1–3.4.6 | 1, 10, 20 | 21, 35 | Alle (mål–faktisk-sammenligning) | nr. 1 d | [K35](../kilder/K35-cnil-referentiel-audit.md), [K36 ES09–ES14](../kilder/K36-cnil-referentiel-digital-safe.md) |
| 24 | Lagringstid og sletting | 3.2.7 (logger) | 11, 15, 16 | 9, 26 | DM, IV (sletting) | – (art. 5 nr. 1 e) | [K36 ES05](../kilder/K36-cnil-referentiel-digital-safe.md) |
| 25 | Papirdokumenter | – | 3 (merking) | 39 | K, T | nr. 1 b | – |
| 26 | Rettigheter og intervenerbarhet (teknisk tilrettelegging) | – | – | 11–13 | IV (samle, rette, sperre, slette alle data om én person; SPoC) | – (art. 12–22, 25) | [T03](T03-grunnprinsipper-art5.md) |

**Lesehjelp:** NSM er sterkest på tema 1–18 og 22–23 (teknisk og organisatorisk IKT-sikkerhet) men mangler tema 8, 24–26 (personvernspesifikt) og er svak på 20–21 (fysisk og menneskelig). CNIL-arkene dekker alle tema og har konkrete terskler. SDM gir *hvorfor* (beskyttelsesmål og GDPR-forankring) og dekker de personvernspesifikke målene som NSM mangler [K32 Aktualitet](../kilder/K32-nsm-grunnprinsipper.md), [K37 tabell 3](../kilder/K37-sdm-standard-datavernmodell.md).

### 5. Beskyttelsesmål og GDPR-forankring (SDM)

| Beskyttelsesmål | GDPR-artikler (SDM tabell 3) | Typiske tiltak |
|---|---|---|
| Dataminimering | 5(1)(c), 5(1)(e), 25, 32 | Færre attributter, automatiske slette-/sperrerutiner, pseudonymisering |
| Tilgjengelighet | 5(1)(e), 13, 15, 20, 25, 32 | Backup, redundans, reparasjonsstrategier |
| Integritet | 5(1)(f), 25, 32, 33 | Begrense skriverettigheter, sjekksummer/signaturer, testing |
| Konfidensialitet | 5(1)(f), 25, 28(3)(b), 29, 32 | Rollekonsept, sikker autentisering, kryptering, taushetsplikt |
| Ikke-kobling | 5(1)(c), 5(1)(e), 17, 22, 25, 40(2)(d) | Separasjon, formålsspesifikke pseudonymer, lukkede grensesnitt |
| Åpenhet | 5(1)(a), 13, 14, 15, 19, 25, 30, 32, 33, 40, 42 | Dokumentasjon, logging, versjonskontroll |
| Intervenerbarhet | 5(1)(d), 5(1)(f), 13(2)(c), 14(2)(d), 15(1)(e), 16–18, 20, 21, 25, 32 | SPoC, sperre-/slettefunksjoner, deaktivere enkeltfunksjoner |

Kilde: [K37 s. 25, kap. 7](../kilder/K37-sdm-standard-datavernmodell.md). Art. 32 nr. 1 bokstav b nevner i tillegg **robusthet** [K40 § 4.2 fotnote](../kilder/K40-dpia-prosess-uld.md).

### 6. Art. 32 i databehandlerforhold

- Behandlingsansvarlig må bruke databehandlere med **tilstrekkelige garantier** og kjenne detaljene for å kunne påvise etterlevelse [K33 ark 14](../kilder/K33-cnil-sikkerhetsguide.md). Databehandleravtalen skal pålegge art. 32-tiltak og bistand med art. 32–36; minimumskrav bør stå i et sikkerhetsvedlegg [K05](../kilder/K05-dt-databehandleravtale.md).
- **Praktisk metode:** Bruk [M09](../maler/M09-sikkerhetstiltak-sjekkliste.md) som spørreskjema/vedlegg mot leverandøren, NSM 2.1.10 a–j som minimumsundersøkelse, og [M01](../maler/M01-databehandleravtale-sjekkliste.md) for avtalen. Arbeidsflyt: [A01](../arbeidsflyter/A01-gjennomga-databehandleravtale.md).
- Leverandørens egen risikovurdering dekker typisk *leverandørens* risiko; behandlingsansvarlig må selv vurdere risikoen for de registrerte i sin behandling **[Merknad – ikke fra kildene]**.
- Sertifisering (ISO/IEC 27001/27701, SOC 2 o.l.) er en indikator, men kontroller **omfanget (scope)** [K33 ark 14](../kilder/K33-cnil-sikkerhetsguide.md). Etter art. 32 nr. 3 kan godkjente atferdsnormer og sertifiseringer brukes som *et element* i påvisningen **[Merknad – ikke fra kildene]**.

### 7. Motstrid og forskjeller mellom kildene

| Spørsmål | Kilde A | Kilde B | Anbefalt håndtering |
|---|---|---|---|
| Periodisk passordbytte | K33 (2024): ikke for vanlige brukere | K30 (2018): ev. hver 6./12. måned, gjenbruksforbud 5 siste | Følg K33 (nyere); K30 er utdatert på dette punktet [K30 Aktualitet](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Kontosperring | K30: etter 5 feil | K33: 10 feil gir grunnlag for 50-bits passord; 3 feil for 13-bits PIN | Velg etter passordstyrke; K33 er nyest |
| Lagringstid for logger | K33: rullerende 6–12 mnd. | K30: 6 mnd.; NSM: ingen tall, men lagringstid skal fastsettes og vurderes | Fastsett konkret; 6–12 mnd. er fransk praksis, ikke GDPR-krav [K33 Aktualitet](../kilder/K33-cnil-sikkerhetsguide.md) |
| RSA-nøkkellengde | K10 (2017): 3072 | K33: minst 2048 eller 3072 | Følg NSMs kryptografiske anbefalinger [K32 2.7.2](../kilder/K32-nsm-grunnprinsipper.md), [K10](../kilder/K10-dt-kryptering.md) |
| Wi-Fi | K30: WPA/WPA2 | K32/K33: WPA2/WPA3 | Følg K32/K33 |
| Ekte data i test | K32 2.1.6: sensitive produksjonsdata bare i sikret miljø | K33 ark 11/K30 kap. 20: fiktive/anonymiserte data, unntak for sikret pre-produksjon | Utgangspunkt fiktive/anonymiserte data; ekte data bare i miljø sikret som produksjon |
| Restrisiko | K18/K19: kan aksepteres av riktig ledernivå | K40: «ingen akseptabel restrisiko» i DPIA-forstand | Se [T09](T09-risikovurdering-metoder-og-skalaer.md); GDPR art. 36 gjelder uansett ved høy restrisiko |

Etter kildehierarkiet går GDPR foran tilsynsveiledning, og Datatilsynet går foran CNIL/ULD, som igjen går foran metodeverk (NSM, Digdir, SDM) [_KONVENSJONER](../_KONVENSJONER.md)(../_KONVENSJONER.md)(../_KONVENSJONER.md)(../_KONVENSJONER.md)(../_KONVENSJONER.md). Ved tekniske detaljer (algoritmer, protokoller) bør man likevel bruke det nyeste faglige rådet (NSM, CNIL 2024), siden Datatilsynets krypteringsside er fra 2017 og selv viser til NSM [K10](../kilder/K10-dt-kryptering.md).

## Vanlige feil og fallgruver

- **Bare virksomhetsrisiko:** Sikkerhetsvurderingen ser kun på konsekvenser for virksomheten (økonomi, omdømme) og glemmer de registrerte [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md), [K37 9.4](../kilder/K37-sdm-standard-datavernmodell.md).
- **Bare K-I-T:** Tiltakskapitlet mangler dataminimering, ikke-kobling, åpenhet og intervenerbarhet [K37](../kilder/K37-sdm-standard-datavernmodell.md), [K40](../kilder/K40-dpia-prosess-uld.md).
- **Avkryssing i stedet for vurdering:** Tiltak listes uten forklaring på hvordan de virker i systemet [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md), [K29 – tomme felt ikke akseptable](../kilder/K29-cnil-pia-maler.md).
- **Avanserte tiltak før grunnleggende** (f.eks. SIEM uten MFA og patching) [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md), [K32 s. 33](../kilder/K32-nsm-grunnprinsipper.md).
- **Overlate alt til leverandøren** eller tro at serverside-kryptering beskytter mot leverandøren [K33 ark 1, 22](../kilder/K33-cnil-sikkerhetsguide.md), [K32 2.1.9](../kilder/K32-nsm-grunnprinsipper.md).
- **Sertifikat uten scope-kontroll** [K33 ark 14](../kilder/K33-cnil-sikkerhetsguide.md).
- **Backup som ikke testes** eller som ligger i samme miljø som produksjon [K33 ark 17](../kilder/K33-cnil-sikkerhetsguide.md).
- **Logger uten formål og lagringstid**, eller brukt til kontroll av ansatte [K33 ark 16](../kilder/K33-cnil-sikkerhetsguide.md), [K32 3.2.2](../kilder/K32-nsm-grunnprinsipper.md).
- **Logisk sletting** regnet som sletting [K30 kap. 9](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- **Ekte personopplysninger i test** [K33 ark 11](../kilder/K33-cnil-sikkerhetsguide.md).
- **Hendelsesprosess som bare fanger konfidensialitetsbrudd** – tap av tilgjengelighet/integritet er også brudd [K34 s. 1](../kilder/K34-cnil-cybersikkerhet-2024.md).
- **Ingen oppdatering ved endring:** risikovurderingen skal oppdateres ved endringer i system og kontekst [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md), [K32 2.10](../kilder/K32-nsm-grunnprinsipper.md).
- **Glemme papir, muntlig informasjon og fysiske lokaler** – NSM dekker dette svakt [K32 s. 5](../kilder/K32-nsm-grunnprinsipper.md), [K30 kap. 39](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- **Glemme de typiske tilsynsfunnene**: URL-manipulering, klartekstpassord, HTTP-skjema, manglende skjermlås [K34 s. 2](../kilder/K34-cnil-cybersikkerhet-2024.md).

## Sjekkliste

- [ ] Er det gjennomført og dokumentert en sikkerhetsrisikovurdering for behandlingen før oppstart, med konsekvenser for de registrerte? ([M03](../maler/M03-risikovurdering-mal.md), [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md))
- [ ] Finnes risikotoleranse/akseptkriterier fastsatt av ledelsen? [K32 1.1.4](../kilder/K32-nsm-grunnprinsipper.md), [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md)
- [ ] Finnes oversikt over systemer, data, dataflyt og leverandører? [K32 1.1.5–1.1.6](../kilder/K32-nsm-grunnprinsipper.md), [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md)
- [ ] Er grunnsikringen vurdert punkt for punkt (M09), med begrunnelse for tiltak som velges bort? [K32 s. 5](../kilder/K32-nsm-grunnprinsipper.md)
- [ ] Er alle sju SDM-mål dekket i tiltakene? [K37](../kilder/K37-sdm-standard-datavernmodell.md)
- [ ] Minste privilegium, årlig tilgangsrevisjon, MFA for kritiske/privilegerte tilganger? [K32 2.6](../kilder/K32-nsm-grunnprinsipper.md), [K33 ark 4–5](../kilder/K33-cnil-sikkerhetsguide.md)
- [ ] Kryptering i ro og i transitt etter risiko, med nøkkelhåndtering? Obligatorisk ved overføring av særlige kategorier/fødselsnummer? [K10](../kilder/K10-dt-kryptering.md), [K32 2.7](../kilder/K32-nsm-grunnprinsipper.md)
- [ ] Logging med formål, lagringstid, beskyttelse, informasjon til brukerne og aktiv analyse? [K32 3.2](../kilder/K32-nsm-grunnprinsipper.md), [K33 ark 16](../kilder/K33-cnil-sikkerhetsguide.md)
- [ ] Backup etter 3-2-1 med offline-kopi og testet gjenoppretting innen definert tid? [K33 ark 17](../kilder/K33-cnil-sikkerhetsguide.md), [K32 2.9](../kilder/K32-nsm-grunnprinsipper.md)
- [ ] Planverk for hendelser med kriterier for brudd på personopplysningssikkerheten og 72-timers rutine? [K33 ark 19](../kilder/K33-cnil-sikkerhetsguide.md), [K32 4.1](../kilder/K32-nsm-grunnprinsipper.md)
- [ ] Årlig inntrengingstest, sårbarhetsskanning, test av beredskap annethvert år? [K32 3.1, 3.4](../kilder/K32-nsm-grunnprinsipper.md)
- [ ] Databehandleravtale med sikkerhetsvedlegg, revisjonsrett, logging- og varslingsplikt, underleverandørkontroll? [K05](../kilder/K05-dt-databehandleravtale.md), [K33 ark 14](../kilder/K33-cnil-sikkerhetsguide.md), [K32 2.1.10](../kilder/K32-nsm-grunnprinsipper.md)
- [ ] IT-reglement, taushetserklæring og rollebasert opplæring? [K33 ark 2–3](../kilder/K33-cnil-sikkerhetsguide.md)
- [ ] Fysisk sikring av lokaler og serverrom? [K33 ark 12](../kilder/K33-cnil-sikkerhetsguide.md)
- [ ] Lagringstid og reell sletting (også i backup)? [K30 kap. 9](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K37 5.3](../kilder/K37-sdm-standard-datavernmodell.md)
- [ ] Er det plan for regelmessig evaluering (art. 32 nr. 1 d) og ledelsens årlige gjennomgang? [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md)

## Se også

- [T09 – Risikovurdering: metoder og skalaer](T09-risikovurdering-metoder-og-skalaer.md)
- [T03 – Grunnprinsipper (art. 5)](T03-grunnprinsipper-art5.md) · [T13 – Innebygd personvern (art. 25)](T13-innebygd-personvern-art25.md)
- [T07 – Databehandleravtale (art. 28)](T07-databehandleravtale-art28.md) · [T01 – Roller](T01-roller-behandlingsansvarlig-databehandler.md)
- [T10 – DPIA (art. 35–36)](T10-dpia-art35-36.md) · [T11 – Overføring til tredjeland](T11-overforing-tredjeland-og-tia.md) · [T12 – Avvik og brudd (art. 33–34)](T12-avvik-og-brudd-art33-34.md)
- Maler: [M03 – Risikovurdering](../maler/M03-risikovurdering-mal.md) · [M09 – Sikkerhetstiltak-sjekkliste](../maler/M09-sikkerhetstiltak-sjekkliste.md) · [M01 – DPA-sjekkliste](../maler/M01-databehandleravtale-sjekkliste.md) · [M04 – DPIA-mal](../maler/M04-dpia-mal.md)
- Arbeidsflyter: [A03 – Risikovurdering informasjonssikkerhet](../arbeidsflyter/A03-risikovurdering-informasjonssikkerhet.md) · [A01 – DPA-gjennomgang](../arbeidsflyter/A01-gjennomga-databehandleravtale.md) · [A02 – DPIA](../arbeidsflyter/A02-gjennomfore-dpia.md) · [A05 – Avvikshåndtering](../arbeidsflyter/A05-avvikshandtering.md)

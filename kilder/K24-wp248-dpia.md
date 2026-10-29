---
id: K24
tittel: "Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is \"likely to result in a high risk\" for the purposes of Regulation 2016/679 (WP 248 rev.01)"
utgiver: Artikkel 29-gruppen (WP29), godkjent av EDPB 25.05.2018
dato: "Vedtatt 2017-04-04, sist revidert og vedtatt 2017-10-04"
spraak: en
fil: "ressurser/20171013_wp248_rev01_enpdf_4.pdf"
type: retningslinje
gdpr_artikler: [24, 25, 28, 30, 35, 36, 39, 40, 42, 83]
emner: [dpia, risikovurdering, høy risiko, forhåndsdrøfting, metode, personvernombud]
relevans: høy
---

# Retningslinjer om vurdering av personvernkonsekvenser (DPIA) – WP 248 rev.01 (WP29, 2017)

## Sammendrag

WP248 er Artikkel 29-gruppens (WP29) sentrale retningslinje om vurdering av personvernkonsekvenser (Data Protection Impact Assessment, DPIA) etter GDPR art. 35 og forhåndsdrøfting med tilsynsmyndigheten etter art. 36. Dokumentet forklarer hva en DPIA er («a process for building and demonstrating compliance»), når den er obligatorisk, når den ikke kreves, hvordan den skal gjennomføres, og når tilsynsmyndigheten skal konsulteres. Kjernen er **de ni kriteriene** for å vurdere om en behandling «sannsynligvis vil medføre høy risiko», med tommelfingerregelen om at **to eller flere kriterier** normalt utløser DPIA-plikt. Retningslinjen inneholder en eksempeltabell, en liste over situasjoner der DPIA ikke kreves, og to vedlegg: eksempler på eksisterende DPIA-rammeverk (Annex 1) og kriterier for en akseptabel DPIA (Annex 2). Målgruppen er behandlingsansvarlige, personvernombud og tilsynsmyndigheter (som skal lage nasjonale lister etter art. 35 nr. 4). Retningslinjen er grunnlaget for Datatilsynets DPIA-liste og veiledning.

## Når skal agenten bruke denne kilden

- Når det skal avgjøres om en behandling krever DPIA (bruk de ni kriteriene og eksempeltabellen).
- Når det skal dokumenteres hvorfor DPIA *ikke* gjennomføres.
- Når en eksisterende DPIA eller metode skal kvalitetssikres mot minimumskravene (Annex 2).
- Ved spørsmål om hvem som skal gjennomføre DPIA, rollen til personvernombud (DPO), databehandler og CISO, og om de registrertes synspunkter skal innhentes.
- Ved spørsmål om forhåndsdrøfting med Datatilsynet (art. 36) – «høy restrisiko».
- Ved spørsmål om publisering av DPIA, felles DPIA for flere behandlinger/behandlingsansvarlige, eller DPIA for eksisterende behandlinger.
- Når databehandler skal bistå behandlingsansvarlig med DPIA (art. 28 nr. 3 bokstav f) – relevant ved gjennomgang av databehandleravtaler.

## Hovedinnhold

### I. Innledning (s. 4)

- En DPIA er «a process designed to describe the processing, assess its necessity and proportionality and help manage the risks to the rights and freedoms of natural persons resulting from the processing of personal data» (s. 4).
- DPIA er et verktøy for ansvarlighet (accountability, art. 24): den hjelper både med å etterleve og med å *påvise* etterlevelse.
- Begrepet «Privacy Impact Assessment» (PIA) brukes ofte om det samme (fotnote 2). Direktiv 2016/680 (politidirektivet) art. 27 har en tilsvarende plikt.
- **Sanksjoner:** Unnlatt DPIA når den kreves (art. 35 nr. 1, 3–4), feil gjennomført DPIA (art. 35 nr. 2 og 7–9), eller unnlatt forhåndsdrøfting (art. 36 nr. 3 bokstav e) kan gi overtredelsesgebyr på inntil 10 mill. EUR eller 2 % av global årsomsetning, det høyeste av dem (s. 4).
  - **[Merknad – ikke fra kilden]** Plikten til forhåndsdrøfting følger av art. 36 nr. 1; art. 36 nr. 3 bokstav e gjelder bare at vurderingen av personvernkonsekvenser skal framlegges ved drøftingen. Gebyrrammen følger av art. 83 nr. 4 bokstav a (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-36) og [K43](K43-gdpr-kap08-rettsmidler-ansvar-og-sanksjoner.md#art-83)).
- GDPR definerer ikke DPIA formelt, men minimumsinnholdet følger av art. 35 nr. 7 (se nedenfor), og fortalepunkt 84 forklarer formålet: å vurdere «the origin, nature, particularity and severity of that risk».

### II. Retningslinjenes virkeområde (s. 4–5)

Retningslinjene bygger på WP29 Statement WP 218 (risikobasert tilnærming), WP29-retningslinjene om personvernombud (WP 243), WP29 Opinion 03/2013 om formålsbegrensning (WP 203) og internasjonale standarder (ISO 31000:2009, ISO/IEC 29134).

DPIA er ikke obligatorisk for alle behandlinger – bare der behandlingen «sannsynligvis vil medføre høy risiko» (art. 35 nr. 1). Retningslinjene skal:
- klargjøre begrepet høy risiko og gi kriterier for listene tilsynsmyndighetene skal vedta etter art. 35 nr. 4;
- fremme utvikling av en felles EU-liste over behandlinger som krever DPIA (art. 35 nr. 4);
- en felles EU-liste over behandlinger som ikke krever DPIA (art. 35 nr. 5);
- felles kriterier for DPIA-metodikk (art. 35 nr. 5);
  - **[Merknad – ikke fra kilden]** Art. 35 nr. 5 gjelder bare tilsynsmyndighetens liste over behandlinger som *ikke* krever DPIA; forordningen har ingen egen bestemmelse om metodikk utover minimumsinnholdet i nr. 7 (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-35)).
- felles kriterier for når tilsynsmyndigheten skal konsulteres (art. 36 nr. 1);
- anbefalinger basert på erfaringer i medlemsstatene.

### III. DPIA: forordningen forklart (s. 6–19)

**Risiko og risikostyring (s. 6):**
- «A "risk" is a scenario describing an event and its consequences, estimated in terms of severity and likelihood.» Risikostyring er «the coordinated activities to direct and control an organization with regard to risk».
- «Rettigheter og friheter» gjelder primært retten til personvern og privatliv, men også andre grunnleggende rettigheter: ytringsfrihet, tankefrihet, bevegelsesfrihet, forbud mot diskriminering, rett til frihet, samvittighets- og religionsfrihet.
- Selv om DPIA-plikten ikke utløses, gjelder den generelle plikten til å håndtere risiko. Den behandlingsansvarlige må **løpende** vurdere risikoen for å identifisere når en behandling blir høyrisiko.
- Fotnote 10: Risiko må identifiseres, analyseres, estimeres, evalueres, behandles (f.eks. reduseres) og gjennomgås jevnlig. **Behandlingsansvarlig kan ikke fraskrive seg ansvaret ved å forsikre seg mot risiko.**

#### A. Hva omfatter en DPIA? (s. 7–8)

- En DPIA kan gjelde én behandling, men «a single assessment may address a set of similar processing operations that present similar high risks» (art. 35 nr. 1). Fortalepunkt 92 nevner felles plattformer for offentlige myndigheter og felles applikasjoner i en bransje.
- Én DPIA kan dekke flere behandlinger som er like med hensyn til art, omfang, sammenheng, formål og risiko. Det er ikke nødvendig å gjøre DPIA for tilfeller som allerede er studert.
- **Eksempler:** En gruppe kommuner som hver setter opp lignende kameraovervåking kan gjøre én felles DPIA; en jernbaneoperatør (én behandlingsansvarlig) kan dekke kameraovervåking på alle stasjoner med én DPIA.
- Ved felles DPIA for flere behandlingsansvarlige: en referanse-DPIA bør deles eller gjøres offentlig tilgjengelig, tiltakene i den må gjennomføres, og det må gis en begrunnelse for at én DPIA brukes.
- **Felles behandlingsansvarlige** (joint controllers) må presist definere sine respektive plikter. DPIA-en bør angi hvem som er ansvarlig for hvilke risikoreduserende tiltak. Hver part bør dele nyttig informasjon uten å kompromittere hemmeligheter (forretningshemmeligheter, immaterielle rettigheter, konfidensiell forretningsinformasjon) eller avsløre sårbarheter.
- **Teknologiprodukter:** En DPIA kan være nyttig for å vurdere et maskin- eller programvareprodukt som brukes av ulike behandlingsansvarlige. Den behandlingsansvarlige som tar produktet i bruk må likevel gjøre sin egen DPIA for den konkrete implementasjonen, men kan bygge på leverandørens DPIA. Eksempel: forholdet mellom produsenter av smarte strømmålere og energiselskaper. Produktleverandør eller databehandler bør dele nyttig informasjon uten å kompromittere hemmeligheter eller skape sikkerhetsrisiko.

#### B. Hvilke behandlinger krever DPIA? (s. 8–13)

##### a) Når er DPIA obligatorisk? (s. 8–12)

- DPIA er obligatorisk der behandlingen «sannsynligvis vil medføre høy risiko» (art. 35 nr. 1, illustrert av nr. 3 og supplert av nr. 4). Særlig relevant ved innføring av ny teknologi.
- **Er det uklart om DPIA kreves, anbefaler WP29 at DPIA gjennomføres likevel** (s. 8).
- Art. 35 nr. 3 gir eksempler (ikke uttømmende, jf. «in particular»):
  - (a) systematisk og omfattende vurdering av personlige forhold basert på automatisert behandling, herunder profilering, som danner grunnlag for avgjørelser med rettsvirkning eller tilsvarende betydelig påvirkning (jf. fortalepunkt 71);
  - (b) behandling i stor skala av særlige kategorier (art. 9 nr. 1) eller opplysninger om straffedommer og lovovertredelser (art. 10) (jf. fortalepunkt 75);
  - (c) systematisk overvåking i stor skala av et offentlig tilgjengelig område.

**De ni kriteriene (s. 9–11)** – bygget på art. 35 nr. 1 og nr. 3 bokstav a–c, nasjonale lister etter art. 35 nr. 4 og fortalepunkt 71, 75, 91:

| Nr. | Kriterium | Forklaring og eksempler fra kilden |
|---|---|---|
| 1 | **Evaluering eller poengsetting (scoring)**, herunder profilering og prediksjon | Særlig ut fra «aspects concerning the data subject's performance at work, economic situation, health, personal preferences or interests, reliability or behavior, location or movements» (fortalepunkt 71 og 91). Eksempler: finansinstitusjon som sjekker kunder mot kredittopplysningsregister eller AML/CTF- eller svindeldatabase; bioteknologiselskap som tilbyr gentester direkte til forbrukere for å forutsi sykdomsrisiko; selskap som bygger atferds- eller markedsføringsprofiler basert på bruk/navigering på nettstedet. |
| 2 | **Automatiserte avgjørelser med rettsvirkning eller tilsvarende betydelig virkning** | Behandling som tar sikte på avgjørelser med «legal effects» eller som «similarly significantly affects» den registrerte (art. 35 nr. 3 bokstav a). Kan f.eks. føre til utestengelse eller diskriminering. Behandling med liten eller ingen virkning for individet oppfyller ikke kriteriet. |
| 3 | **Systematisk overvåking** | Behandling for å observere, overvåke eller kontrollere registrerte, inkludert data samlet gjennom nettverk eller «a systematic monitoring of a publicly accessible area» (art. 35 nr. 3 bokstav c). Kriterium fordi registrerte kanskje ikke vet hvem som samler inn eller hvordan data brukes, og det kan være umulig å unngå behandlingen i offentlig rom. |
| 4 | **Sensitive opplysninger eller opplysninger av svært personlig karakter** | Særlige kategorier (art. 9, f.eks. politisk oppfatning) og straffedommer/lovovertredelser (art. 10). Eksempler: sykehus med pasientjournaler; privatetterforsker med opplysninger om lovbrytere. I tillegg: data knyttet til hjem og privatliv (f.eks. elektronisk kommunikasjon), data som påvirker utøvelse av grunnleggende rettigheter (f.eks. lokasjonsdata – bevegelsesfrihet), data der krenkelse gir alvorlige konsekvenser i dagliglivet (f.eks. finansielle data som kan brukes til betalingssvindel). Om data allerede er offentliggjort av den registrerte eller tredjeparter kan være relevant. Omfatter også personlige dokumenter, e-post, dagbøker, notater fra lesebrett med notatfunksjon og svært personlig informasjon i «life-logging»-apper. |
| 5 | **Behandling i stor skala** | GDPR definerer ikke «stor skala» (se fortalepunkt 91). Faktorer (fra WP 243): (a) antall registrerte – som tall eller andel av relevant populasjon; (b) datamengde og/eller spekteret av dataelementer; (c) varighet eller permanens; (d) geografisk utstrekning. |
| 6 | **Sammenstilling eller kombinasjon av datasett** | F.eks. data fra to eller flere behandlinger med ulike formål og/eller ulike behandlingsansvarlige, på en måte som overstiger den registrertes rimelige forventninger (jf. WP 203 s. 24). |
| 7 | **Opplysninger om sårbare registrerte** (fortalepunkt 75) | Begrunnet i økt maktubalanse – den registrerte kan ha vanskelig for å samtykke, motsette seg eller utøve rettigheter. Omfatter barn, **arbeidstakere**, mer sårbare grupper som trenger særlig beskyttelse (psykisk syke, asylsøkere, eldre, pasienter osv.), og ethvert tilfelle med ubalanse mellom den registrerte og den behandlingsansvarlige. |
| 8 | **Innovativ bruk eller anvendelse av nye teknologiske eller organisatoriske løsninger** | F.eks. kombinasjon av fingeravtrykk og ansiktsgjenkjenning for adgangskontroll. Ny teknologi «in accordance with the achieved state of technological knowledge» (fortalepunkt 91) kan utløse DPIA fordi personlige og samfunnsmessige konsekvenser kan være ukjente. Eksempel: visse tingenes internett (IoT)-applikasjoner. |
| 9 | **Behandlingen i seg selv hindrer registrerte i å utøve en rettighet eller bruke en tjeneste eller avtale** (art. 22, fortalepunkt 91) | Behandling som skal tillate, endre eller nekte tilgang til en tjeneste eller inngåelse av avtale. Eksempel: bank som sjekker kunder mot kredittregister for å avgjøre om de skal få lån. |

Fotnote 15 (s. 9) – tolkning av begreper:
- **«Systematisk»** betyr ett eller flere av: skjer etter et system; forhåndsarrangert, organisert eller metodisk; del av en generell plan for datainnsamling; utført som del av en strategi.
- **«Offentlig tilgjengelig område»**: ethvert sted åpent for allmennheten, f.eks. torg, kjøpesenter, gate, markedsplass, togstasjon eller offentlig bibliotek.

**Terskelregel (s. 11):**
- «In most cases, a data controller can consider that a processing meeting two criteria would require a DPIA to be carried out.»
- Jo flere kriterier som er oppfylt, desto mer sannsynlig er høy risiko – **uavhengig av hvilke tiltak den behandlingsansvarlige planlegger**.
- I noen tilfeller kan **ett kriterium** være nok til å kreve DPIA.

**Eksempeltabell (s. 11–12):**

| Eksempel på behandling | Mulige relevante kriterier | DPIA sannsynligvis påkrevd? |
|---|---|---|
| Sykehus som behandler pasienters genetiske og helseopplysninger (pasientinformasjonssystem) | Sensitive/svært personlige opplysninger; sårbare registrerte; stor skala | **Ja** |
| Kamerasystem for å overvåke kjøreatferd på motorveier, med intelligent videoanalyse for å skille ut biler og automatisk gjenkjenne skilt | Systematisk overvåking; innovativ bruk/nye teknologiske eller organisatoriske løsninger | **Ja** |
| Virksomhet som systematisk overvåker ansattes aktiviteter, inkludert arbeidsstasjon, internettaktivitet osv. | Systematisk overvåking; sårbare registrerte | **Ja** |
| Innsamling av offentlige sosiale medier-data for å generere profiler | Evaluering eller scoring; stor skala; sammenstilling av datasett; sensitive/svært personlige opplysninger | **Ja** |
| Institusjon som oppretter nasjonal kredittvurderings- eller svindeldatabase | Evaluering eller scoring; automatiserte avgjørelser med rettsvirkning e.l.; hindrer utøvelse av rettighet/bruk av tjeneste eller avtale; sensitive/svært personlige opplysninger | **Ja** |
| Arkivlagring av pseudonymiserte sensitive personopplysninger om sårbare registrerte fra forskningsprosjekter eller kliniske studier | Sensitive opplysninger; sårbare registrerte; hindrer utøvelse av rettighet/bruk av tjeneste eller avtale | **Ja** |
| Behandling av «personal data from patients or clients by an individual physician, other health care professional or lawyer» (fortalepunkt 91) | Sensitive/svært personlige opplysninger; sårbare registrerte | **Nei** |
| Nettmagasin som bruker e-postliste til å sende et generisk daglig sammendrag til abonnenter | Stor skala | **Nei** |
| Nettbutikk som viser annonser for veteranbildeler med begrenset profilering basert på varer sett eller kjøpt på eget nettsted | Evaluering eller scoring | **Nei** |

**Avvik fra kriteriene (s. 12):**
- En behandling kan treffe kriteriene og likevel av den behandlingsansvarlige vurderes å ikke medføre høy risiko. Da skal den behandlingsansvarlige **begrunne og dokumentere** hvorfor DPIA ikke gjennomføres, og **inkludere/registrere personvernombudets synspunkter**.
- Som del av ansvarlighetsprinsippet skal behandlingsprotokoll føres (art. 30 nr. 1), og det må vurderes om høy risiko er sannsynlig, selv om DPIA ikke gjennomføres.
- Tilsynsmyndighetene skal lage, offentliggjøre og sende EDPB en liste over behandlinger som krever DPIA (art. 35 nr. 4). Kriteriene kan brukes til dette. Behandling av **enhver type biometriske data** eller **barns** opplysninger nevnes som relevante for slike lister. Ved grenseoverskridende behandling skal konsistensmekanismen (art. 63) brukes (art. 35 nr. 6, fotnote 18).

##### b) Når kreves ikke DPIA? (s. 12–13)

WP29 mener DPIA ikke kreves:
1. der behandlingen ikke «sannsynligvis vil medføre høy risiko» (art. 35 nr. 1);
2. når art, omfang, sammenheng og formål er svært like en behandling det allerede er gjort DPIA for – resultatene fra den kan brukes (art. 35 nr. 1);
3. når behandlingen er forhåndskontrollert av en tilsynsmyndighet før mai 2018 under spesifikke vilkår som ikke er endret (fortalepunkt 171, se III.C);
4. der behandlingen etter art. 6 nr. 1 bokstav c eller e har rettslig grunnlag i EU- eller nasjonal rett, loven regulerer den konkrete behandlingen, og en DPIA allerede er gjort som del av etableringen av rettsgrunnlaget (art. 35 nr. 10) – med mindre en medlemsstat har bestemt at DPIA skal gjøres før behandlingen. Fotnote 21: En DPIA gjort under lovarbeidet må sannsynligvis gjennomgås før behandlingen starter, fordi vedtatt lov kan avvike fra forslaget og tekniske detaljer kan mangle; en egen DPIA kan fortsatt være nødvendig;
5. der behandlingen står på tilsynsmyndighetens valgfrie liste over behandlinger som ikke krever DPIA (art. 35 nr. 5). Slike lister kan omfatte behandlinger som oppfyller vilkår fastsatt i veiledninger, vedtak, tillatelser, regler osv. (f.eks. i Frankrike: tillatelser, unntak, forenklede regler, «compliance packs»). Gjelder bare hvis behandlingen faller **strengt innenfor** prosedyrens virkeområde og fortsatt fullt ut oppfyller GDPR.

#### C. Eksisterende behandlinger (s. 13–14)

- DPIA-plikten gjelder for eksisterende behandlinger som sannsynligvis medfører høy risiko og der **risikoen har endret seg**, sett hen til art, omfang, sammenheng og formål.
- DPIA trengs ikke for behandlinger forhåndskontrollert etter direktiv 95/46 art. 20 som utføres uendret (fortalepunkt 171).
- Behandlinger der gjennomføringsvilkårene (omfang, formål, innsamlede opplysninger, identitet til behandlingsansvarlige eller mottakere, lagringstid, tekniske og organisatoriske tiltak osv.) har endret seg siden forhåndskontrollen og som sannsynligvis gir høy risiko, skal ha DPIA.
- DPIA kan kreves etter endring av risiko, f.eks. ny teknologi eller nytt formål. Fotnote 22 lister endringsdimensjoner: kontekst, innsamlede data, formål, funksjonalitet, personopplysninger, mottakere, datakombinasjoner, risiko (støtteressurser, risikokilder, potensielle konsekvenser, trusler osv.), sikkerhetstiltak og internasjonale overføringer.
- Organisatorisk eller samfunnsmessig kontekst kan også endre seg, f.eks. at virkningene av automatiserte avgjørelser blir mer betydelige, eller at nye grupper blir sårbare for diskriminering.
- Endringer kan også **senke** risikoen (f.eks. avgjørelser ikke lenger automatiserte, overvåking ikke lenger systematisk), slik at DPIA ikke lenger kreves.
- God praksis: DPIA bør gjennomgås løpende og revurderes jevnlig. Selv om DPIA ikke kreves 25.05.2018, må den gjennomføres på passende tidspunkt som del av ansvarlighetsplikten.

#### D. Hvordan gjennomføre en DPIA? (s. 14–18)

##### a) Tidspunkt – før behandlingen (s. 14)

- DPIA skal gjøres «prior to the processing» (art. 35 nr. 1 og 10, fortalepunkt 90 og 93), i tråd med innebygd personvern (art. 25, fortalepunkt 78). Unntak (fotnote 23): eksisterende forhåndskontrollert behandling – DPIA før vesentlige endringer.
- Start så tidlig som praktisk mulig i utformingen, selv om noe er ukjent. Oppdater gjennom hele livsløpet; enkelte trinn må kanskje gjentas fordi valg av tiltak påvirker alvorlighet og sannsynlighet.
- At DPIA må oppdateres etter oppstart er ikke en gyldig grunn til å utsette den. «Carrying out a DPIA is a continual process, not a one-time exercise» (s. 14).

##### b) Hvem – behandlingsansvarlig, med DPO og databehandlere (s. 14–15)

- Behandlingsansvarlig er ansvarlig for at DPIA gjennomføres (art. 35 nr. 2). Andre (internt eller eksternt) kan utføre den, men ansvaret ligger hos behandlingsansvarlig.
  - **[Merknad – ikke fra kilden]** Plikten til å foreta vurderingen påhviler den behandlingsansvarlige etter art. 35 nr. 1; nr. 2 gjelder plikten til å rådføre seg med personvernombudet (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-35)).
- **Personvernombudet** (DPO), der det er utnevnt, skal gi råd (art. 35 nr. 2); rådet og behandlingsansvarliges beslutninger skal dokumenteres i DPIA-en. DPO skal overvåke gjennomføringen (art. 39 nr. 1 bokstav c).
- **Databehandler** skal bistå og gi nødvendig informasjon (art. 28 nr. 3 bokstav f).
- **De registrertes synspunkter** skal innhentes «where appropriate» (art. 35 nr. 9). WP29:
  - kan skje på ulike måter (generell studie om formål og midler, spørsmål til tillitsvalgte/ansattrepresentanter, vanlige spørreundersøkelser til fremtidige kunder), forutsatt behandlingsgrunnlag for eventuelle personopplysninger. Samtykke til behandlingen er «obviously not a way for seeking the views of the data subjects»;
  - avviker endelig beslutning fra de registrertes syn, skal begrunnelsen dokumenteres;
  - beslutter man å ikke innhente synspunkter, skal begrunnelsen dokumenteres (f.eks. at det ville kompromittere konfidensielle forretningsplaner, eller være uforholdsmessig eller upraktisk).
- **God praksis – roller og ansvar:**
  - forretningsenheter som foreslår DPIA bør bidra og delta i valideringen;
  - råd fra uavhengige eksperter fra ulike fagfelt (jurister, IT-eksperter, sikkerhetseksperter, sosiologer, etikere osv.);
  - databehandlers roller og ansvar skal være kontraktsfestet, og DPIA gjøres med databehandlers hjelp (art. 28 nr. 3 bokstav f);
  - informasjonssikkerhetsleder (CISO) og DPO kan foreslå DPIA, bistå med metodikk, vurdere kvaliteten på risikovurderingen og om restrisiko er akseptabel;
  - CISO og/eller IT-avdelingen bør bistå og kan foreslå DPIA ut fra sikkerhets- eller driftsbehov.

##### c) Metodikk – ulike metoder, felles kriterier (s. 15–17)

**Minimumsinnhold** (art. 35 nr. 7, fortalepunkt 84 og 90):
- (a) en systematisk beskrivelse av planlagte behandlinger og formålene, herunder eventuelt den berettigede interessen som forfølges;
- (b) en vurdering av om behandlingen er nødvendig og forholdsmessig sett opp mot formålene;
- (c) en vurdering av risikoene for de registrertes rettigheter og friheter;
- (d) tiltakene som planlegges for å håndtere risikoene, herunder garantier, sikkerhetstiltak og mekanismer for å sikre vern av personopplysninger og påvise etterlevelse.

Øvrig:
- Kilden har en figur over den generiske, **iterative** DPIA-prosessen; hvert trinn vil i praksis bli gjennomgått flere ganger (fotnote 25). [Figuren er ikke gjengitt i tekstuttrekket.]
- **Atferdsnormer** (art. 40) skal tas i betraktning (art. 35 nr. 8). Sertifiseringer, segl og merker (art. 42) og bindende virksomhetsregler (BCR) bør også tas i betraktning.
- DPIA er **skalerbar** – også små behandlingsansvarlige kan utforme en egnet DPIA.
- Fortalepunkt 90 overlapper med risikostyring (ISO 31000): fastsette konteksten («nature, scope, context and purposes of the processing and the sources of the risk»), vurdere risikoen («particular likelihood and severity of the high risk»), behandle risikoen («mitigating that risk», «ensuring the protection of personal data», «demonstrating compliance»).
- **Perspektiv:** DPIA styrer risiko for de *registrertes* rettigheter og tar deres perspektiv – i motsetning til informasjonssikkerhet, som fokuserer på organisasjonen (s. 17).
- Behandlingsansvarlig har fleksibilitet i struktur og form, men «a DPIA must be a genuine assessment of risks».
- Behandlingsansvarlig velger metode, men metoden bør oppfylle kriteriene i Annex 2.
- WP29 oppfordrer til **sektorspesifikke DPIA-rammeverk**.
- Behandlingsansvarlig skal gjennomgå om behandlingen skjer i samsvar med DPIA-en, i det minste når risikoen endres (art. 35 nr. 11).

##### d) Publisering (s. 18)

- Publisering er ikke lovpålagt, men behandlingsansvarlige bør vurdere å publisere i det minste deler, f.eks. sammendrag eller konklusjon, for å bygge tillit og vise åpenhet. Særlig god praksis når allmennheten berøres, f.eks. når en offentlig myndighet gjør DPIA.
- Publisert versjon trenger ikke inneholde hele vurderingen (sikkerhetsrisiko, forretningshemmeligheter); kan være et sammendrag av hovedfunn, eller bare en erklæring om at DPIA er gjennomført.
- Ved høy restrisiko kreves forhåndsdrøfting (art. 36 nr. 1), og hele DPIA-en skal da oversendes (art. 36 nr. 3 bokstav e). Tilsynsmyndigheten vil ikke kompromittere forretningshemmeligheter eller avsløre sårbarheter, med forbehold om nasjonale regler om innsyn.

#### E. Når skal tilsynsmyndigheten konsulteres? Når restrisikoen er høy (s. 18–19)

- DPIA kreves når behandlingen sannsynligvis gir høy risiko (eksempel: helseopplysninger i stor skala). Behandlingsansvarlig skal identifisere tiltak som reduserer risikoen til et akseptabelt nivå.
- **Laptop-eksempelet:** For lagring av personopplysninger på bærbare PC-er kan tiltak være effektiv fulldiskkryptering, robust nøkkelhåndtering, tilgangskontroll, sikrede sikkerhetskopier osv., i tillegg til eksisterende rutiner (informasjon, samtykke, innsyn, rett til å protestere osv.). Er risikoen tilstrekkelig redusert, kan behandlingen fortsette uten forhåndsdrøfting.
- **Eksempler på uakseptabel høy restrisiko (s. 19):** registrerte kan få betydelige eller irreversible konsekvenser de ikke kan overvinne (f.eks. ulovlig tilgang som truer liv, oppsigelse, økonomisk risiko), og/eller det er åpenbart at risikoen vil inntreffe (f.eks. kan ikke begrense antall personer med tilgang pga. delings-/bruks-/distribusjonsmåte, eller en kjent sårbarhet er ikke patchet).
- Når behandlingsansvarlig ikke finner tilstrekkelige tiltak (restrisikoen er fortsatt høy), kreves forhåndsdrøfting.
- Fotnote 30: Pseudonymisering og kryptering (samt dataminimering, tilsynsmekanismer osv.) er ikke nødvendigvis egnede tiltak – de er bare eksempler; egnede tiltak avhenger av kontekst og risiko.
- Forhåndsdrøfting kreves også når nasjonal rett krever konsultasjon/forhåndstillatelse for oppgaver i allmennhetens interesse, herunder sosial trygghet og folkehelse (art. 36 nr. 5).
- Fotnote 28: Skriftlig råd fra tilsynsmyndigheten er bare nødvendig når den mener behandlingen ikke er i tråd med forordningen (art. 36 nr. 2).
- Uansett om forhåndsdrøfting kreves: plikten til å oppbevare DPIA-en og oppdatere den gjelder fortsatt.

### IV. Konklusjoner og anbefalinger (s. 19–20)

- DPIA er nyttig, kan være obligatorisk, er skalerbar og kan ha ulike former. Intern policy kan utvide listen ut over lovkravene.
- **Der høyrisikobehandling planlegges, må den behandlingsansvarlige:**
  - velge en DPIA-metode (eksempler i Annex 1) som oppfyller kriteriene i Annex 2, eller spesifisere og gjennomføre en systematisk DPIA-prosess som:
    - oppfyller kriteriene i Annex 2;
    - er integrert i eksisterende prosesser for design, utvikling, endring, risiko og driftsgjennomgang;
    - involverer relevante parter med klart definert ansvar (behandlingsansvarlig, DPO, registrerte eller deres representanter, virksomhet, tekniske tjenester, databehandlere, informasjonssikkerhetsansvarlig osv.);
  - gi DPIA-rapporten til tilsynsmyndigheten når det kreves;
  - konsultere tilsynsmyndigheten når tilstrekkelige tiltak ikke er funnet;
  - jevnlig gjennomgå DPIA-en og behandlingen, i det minste når risikoen endres;
  - dokumentere beslutningene.

### Annex 1 – Eksempler på eksisterende EU-rammeverk for DPIA (s. 21)

GDPR angir ikke hvilken prosess som skal følges; rammeverket kan være skreddersydd eller felles for en bransje, forutsatt at art. 35 nr. 7 dekkes.

**Generiske rammeverk:**
- **DE:** Standard Data Protection Model (SDM), V.1.0 – prøveversjon, 2016 (enstemmig anerkjent – med Bayern avstående – av 92. konferanse for tyske datatilsyn, Kühlungsborn 9.–10. nov. 2016). Se [K37](K37-sdm-standard-datavernmodell.md).
- **ES:** Guía para una Evaluación de Impacto en la Protección de Datos Personales (EIPD), AGPD, 2014.
- **FR:** Privacy Impact Assessment (PIA), CNIL, 2015. Se [K28](K28-cnil-pia-metode.md)–[K30](K30-cnil-pia-kunnskapsbaser.md).
- **UK:** Conducting privacy impact assessments code of practice, ICO, 2014.

**Sektorspesifikke rammeverk:**
- Privacy and Data Protection Impact Assessment Framework for RFID Applications (WP 180 annex; se også Kommisjonsrekommandasjon 12.05.2009 om RFID og WP29 Opinion 9/2011).
- Data Protection Impact Assessment Template for Smart Grid and Smart Metering systems (2014; se også WP29 Opinion 07/2013, WP 209).

**Internasjonal standard:** ISO/IEC 29134 (den gang under utarbeidelse) – Privacy impact assessment – Guidelines.

### Annex 2 – Kriterier for en akseptabel DPIA (s. 22)

Kriterier for å vurdere om en DPIA, eller en DPIA-metode, er tilstrekkelig omfattende til å oppfylle GDPR:

**1. Systematisk beskrivelse av behandlingen er gitt (art. 35 nr. 7 bokstav a):**
- art, omfang, sammenheng og formål med behandlingen er tatt i betraktning (fortalepunkt 90);
- personopplysninger, mottakere og lagringstid er registrert;
- en funksjonell beskrivelse av behandlingen er gitt;
- ressursene (assets) personopplysningene er avhengige av (maskinvare, programvare, nettverk, personer, papir eller papirbaserte overføringskanaler) er identifisert;
- etterlevelse av godkjente atferdsnormer er tatt i betraktning (art. 35 nr. 8).

**2. Nødvendighet og forholdsmessighet er vurdert (art. 35 nr. 7 bokstav b):**
- tiltak for å etterleve forordningen er fastsatt (art. 35 nr. 7 bokstav d og fortalepunkt 90), sett hen til:
  - tiltak som bidrar til forholdsmessighet og nødvendighet på grunnlag av:
    - spesifikke, uttrykkelig angitte og berettigede formål (art. 5 nr. 1 bokstav b);
    - behandlingens lovlighet (art. 6);
    - adekvate, relevante og begrensede opplysninger (art. 5 nr. 1 bokstav c);
    - begrenset lagringstid (art. 5 nr. 1 bokstav e);
  - tiltak som bidrar til de registrertes rettigheter:
    - informasjon til den registrerte (art. 12, 13 og 14);
    - rett til innsyn og dataportabilitet (art. 15 og 20);
    - rett til retting og sletting (art. 16, 17 og 19);
    - rett til å protestere og til begrensning (art. 18, 19 og 21);
    - forhold til databehandlere (art. 28);
    - garantier ved internasjonale overføringer (kapittel V);
    - forhåndsdrøfting (art. 36).

**3. Risikoene for de registrertes rettigheter og friheter er håndtert (art. 35 nr. 7 bokstav c):**
- opprinnelse, art, særtrekk og alvorlighet er vurdert (jf. fortalepunkt 84), eller mer spesifikt for hver risiko (**ulovlig tilgang, uønsket endring og forsvinning av data**) fra de registrertes perspektiv:
  - risikokilder er tatt i betraktning (fortalepunkt 90);
  - potensielle konsekvenser for de registrertes rettigheter og friheter ved hendelser (ulovlig tilgang, uønsket endring, forsvinning) er identifisert;
  - trusler som kan føre til ulovlig tilgang, uønsket endring og forsvinning er identifisert;
  - sannsynlighet og alvorlighet er estimert (fortalepunkt 90);
- tiltak for å behandle risikoene er fastsatt (art. 35 nr. 7 bokstav d og fortalepunkt 90).

**4. Berørte parter er involvert:**
- råd fra personvernombudet er innhentet (art. 35 nr. 2);
- synspunkter fra de registrerte eller deres representanter er innhentet der det er hensiktsmessig (art. 35 nr. 9).

## Praktiske sjekkpunkter

- Kontroller behandlingen mot alle ni kriterier; dokumenter hvilke som er oppfylt. To eller flere → DPIA er normalt påkrevd; ett kriterium kan være nok.
- Kontroller i tillegg Datatilsynets nasjonale liste etter art. 35 nr. 4 (se [K20](K20-dt-dpia-liste.md)).
- Er det tvil om DPIA kreves: gjennomfør DPIA (WP29s anbefaling).
- Velges det å ikke gjøre DPIA tross treff på kriterier: dokumenter begrunnelsen og personvernombudets syn.
- Kontroller at DPIA gjennomføres **før** behandlingen starter og så tidlig som mulig i designfasen.
- Kontroller at DPIA-en minst inneholder de fire elementene i art. 35 nr. 7, og vurder den mot hele sjekklisten i Annex 2.
- Kontroller at risiko vurderes fra **de registrertes perspektiv** (ikke bare virksomhetens), for ulovlig tilgang, uønsket endring og forsvinning, med risikokilder, trusler, konsekvenser, sannsynlighet og alvorlighet.
- Kontroller at personvernombudets råd og beslutningen om å følge/ikke følge det er dokumentert.
- Kontroller at de registrertes synspunkter er innhentet, eller at det er dokumentert hvorfor ikke; avvik fra synspunktene skal begrunnes.
- Kontroller at databehandleravtalen pålegger databehandler å bistå med DPIA og gi nødvendig informasjon (art. 28 nr. 3 bokstav f).
- Ved felles behandlingsansvar: kontroller at DPIA-en fordeler ansvar for hvert tiltak.
- Ved produkt-/leverandør-DPIA: kontroller at behandlingsansvarlig likevel har en egen DPIA for sin implementasjon.
- Kontroller om restrisikoen er høy etter tiltak; i så fall forhåndsdrøfting med Datatilsynet med fullstendig DPIA.
- Kontroller at DPIA-en revideres ved endringer i kontekst, data, formål, funksjonalitet, mottakere, kombinasjoner, risiko, sikkerhetstiltak eller overføringer – og ellers jevnlig.
- Vurder å publisere et sammendrag, særlig for offentlige virksomheter.
- Ikke regn forsikring som risikoreduserende tiltak overfor de registrerte.

## Viktige sitater

- «In other words, a DPIA is a process for building and demonstrating compliance.» (s. 4)
- «A "risk" is a scenario describing an event and its consequences, estimated in terms of severity and likelihood.» (s. 6)
- «In cases where it is not clear whether a DPIA is required, the WP29 recommends that a DPIA is carried out nonetheless» (s. 8)
- «In most cases, a data controller can consider that a processing meeting two criteria would require a DPIA to be carried out.» (s. 11)
- «However, in some cases, a data controller can consider that a processing meeting only one of these criteria requires a DPIA.» (s. 11)
- «Carrying out a DPIA is a continual process, not a one-time exercise.» (s. 14)
- «whatever its form, a DPIA must be a genuine assessment of risks, allowing controllers to take measures to address them.» (s. 17)
- «Whenever the data controller cannot find sufficient measures to reduce the risks to an acceptable level (i.e. the residual risks are still high), consultation with the supervisory authority is required.» (s. 19)
- «Controllers cannot escape their responsibility by covering risks under insurance policies.» (s. 6, fotnote 10)

## Kryssreferanser

- GDPR: art. 24, 25, 28 nr. 3 bokstav f, 30, 35 (særlig nr. 1, 3, 4, 5, 7, 8, 9, 10, 11), 36, 39 nr. 1 bokstav c, 40, 42, 83 nr. 4; fortalepunkt 71, 75, 76, 78, 84, 89, 90, 91, 92, 93, 94, 171.
- [K12](K12-dt-dpia-veiledning.md) – Datatilsynets DPIA-veiledning, bygger på WP248.
- [K20](K20-dt-dpia-liste.md) – Datatilsynets liste etter art. 35 nr. 4 (utfyller de ni kriteriene).
- [K21](K21-dt-sjekkliste-dpia-faser.md) – sjekkliste for DPIA-faser.
- [K22](K22-dpia-eksempler.md) – eksempler.
- [K28](K28-cnil-pia-metode.md), [K29](K29-cnil-pia-maler.md), [K30](K30-cnil-pia-kunnskapsbaser.md) – CNIL PIA-metoden (nevnt i Annex 1).
- [K37](K37-sdm-standard-datavernmodell.md) – Standard-Datenschutzmodell (nevnt i Annex 1).
- [K40](K40-dpia-prosess-uld.md) – DPIA-prosess (ULD).
- [K05](K05-dt-databehandleravtale.md) – databehandlers bistandsplikt ved DPIA.
- [K25](K25-wp259-samtykke.md) – samtykke er ikke en måte å innhente registrertes synspunkter på.

## Aktualitet og begrensninger

- Vedtatt under GDPR (ikke direktiv 95/46), men før GDPR trådte i kraft; referanser til «mai 2018» og forhåndskontroll etter direktivets art. 20 er nå stort sett historiske.
- Henvisningen til «upcoming WP29 Guidelines on Profiling» gjelder WP 251 rev.01 (vedtatt senere).
- Figurene (grunnprinsipper og iterativ prosess) er ikke med i tekstuttrekket.
- **[Merknad – ikke fra kilden]** WP248 rev.01 ble formelt godkjent (endorsed) av EDPB på første plenumsmøte 25. mai 2018 og gjelder fortsatt som EDPB-retningslinje. EDPB har senere avgitt uttalelser om de nasjonale DPIA-listene etter art. 35 nr. 4 (inkl. for Norge, 2019), og Datatilsynets liste ([K20](K20-dt-dpia-liste.md)) er basert på disse kriteriene.
- **[Merknad – ikke fra kilden]** ISO/IEC 29134 ble publisert som ferdig standard i 2017 (revidert 2023). ICOs PIA code of practice (2014) er erstattet av ICOs DPIA-veiledning under UK GDPR; Spanias AGPD heter nå AEPD og har nye veiledere. CNIL har oppdatert sin PIA-metode (2018), jf. K28–K30.
- **[Merknad – ikke fra kilden]** For behandling som involverer KI-systemer bør vurderingen i dag også ses i sammenheng med EUs KI-forordning (AI Act), som bl.a. krever konsekvensvurdering for grunnleggende rettigheter for visse høyrisikosystemer.

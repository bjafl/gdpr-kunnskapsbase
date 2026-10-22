---
id: K14
tittel: "Overføring av personopplysninger ut av EØS"
utgiver: Datatilsynet
dato: "Udatert i utskriften; refererer til EDPB-anbefaling 1/2026 (BCR-P), dvs. oppdatert 2026 (nettside skrevet ut 2026-09-22)"
spraak: nb
fil: "ressurser/Datatilsynet/Overføring av personopplysninger ut av EØS _ Datatilsynet.pdf"
url: "https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/overforing-av-personopplysninger-ut-av-eos/"
type: veileder
gdpr_artikler: [3, 6, 9, 28, 30, 32, 44, 45, 46, 47, 48, 49, 58]
emner: [overforing, tredjeland, adekvans, scc, bcr, schrems-ii, tia, data-privacy-framework, skytjenester, unntak-art49]
relevans: høy
---

# Overføring av personopplysninger ut av EØS (Datatilsynet)

## Sammendrag
Datatilsynets samlede veileder (15 sider i utskrift) om GDPR kapittel V. Den forklarer hva en «overføring» er (EDPBs tre vilkår), hvem som har plikt (både behandlingsansvarlig og databehandler), adekvansbeslutninger (fullstendig liste over land/områder/organisasjoner, inkl. USA via EU-U.S. Data Privacy Framework), de åtte overføringsgrunnlagene i art. 46 (SCC, BCR m.fl.), EU-kommisjonens SCC 2021/914 med fire moduler, BCR-innhold og godkjenningsprosess, «tilleggskrav» etter Schrems II (fem-stegs vurdering, vurdering av tredjelandets lover og praksis, krav til informasjonskilder, ytterligere tekniske/juridiske/organisatoriske tiltak), behandling i EØS hos leverandør underlagt tredjelands lov (fire-stegs vurdering med flytskjema, eksempler fra Sverige, Frankrike og Danmark), unntakene i art. 49 enkeltvis, art. 48, og eksempelsaker fra norske veiledningsmøter (Vestre Viken HF, Sikt/FISA 702). Målgruppe: behandlingsansvarlige, databehandlere og rådgivere.

## Når skal agenten bruke denne kilden
- Avgjøre om et dataflyt-scenario (inkl. fjerntilgang, support, skytjenester, underleverandører) er en «overføring».
- Finne riktig overføringsgrunnlag (adekvans → art. 46-garantier → art. 49-unntak) og vilkårene for hvert.
- Velge SCC-modul (1–4) og vite at SCC dekker art. 28-kravene.
- Strukturere en overføringskonsekvensvurdering (Transfer Impact Assessment, TIA) etter Schrems II: steg, vurderingsmomenter, krav til kildene, ytterligere tiltak (kryptering, pseudonymisering, kontraktstiltak).
- Vurdere bruk av amerikanske/ikke-europeiske skyleverandører med datasenter i EØS.
- Gjennomgå databehandleravtaler (DPA) med forbehold om utlevering/overføring til tredjeland.
- Vurdere BCR-søknad.

## Hovedinnhold

### 1. Innledning (s. 1)
- All overføring ut av EØS krever et særskilt grunnlag. Virksomheten må ha identifisert overføringsgrunnlaget **før** overføring til tredjeland eller internasjonal organisasjon; finnes det ikke – eller **vil det ikke fungere i praksis** – er overføringen ulovlig.
- Innad i EØS kan opplysninger deles over landegrensene med behandlingsgrunnlag, fordi samme regler (GDPR) gjelder.
- Reglene gjelder ikke for privatpersoner som sender egne opplysninger ut av EØS.
- Land utenfor EØS og internasjonale organisasjoner (FN, OECD, WTO) kan ha andre regler; overføringsgrunnlaget skal sikre at opplysningene fortsatt er like godt vernet. Virksomheten må vurdere **i forkant** om grunnlaget faktisk fungerer; hvis ikke må det iverksettes andre tiltak (Schrems II-kapitlet).
- Adekvansbeslutning eller unntak etter art. 49 → ikke behov for særskilt overføringsgrunnlag eller ytterligere vurderinger.
- Kapittel V kommer i tillegg til alle andre forpliktelser; bl.a. må **protokollen** vise hvilke typer opplysninger som overføres og til hvem.

**Hvem har plikt (s. 1):** Både behandlingsansvarlig og databehandler må oppfylle kapittel V. Reglene kan også gjelde virksomheter utenfor EØS (art. 3; EDPB Guidelines 3/2018 om territorialt virkeområde). Bruker en behandlingsansvarlig en databehandler som overfører ut av EØS, må den forsikre seg om at databehandleren oppfyller pliktene; behandlingsansvarlig har rett og plikt til å gi dokumenterte skriftlige instrukser, og databehandler må omgående varsle hvis en instruks strider mot regelverket.

**Hva er en overføring? (s. 1)** «Overføring» er ikke definert i GDPR; EDPB Guidelines 05/2021 (samspill art. 3 og kap. V) oppstiller **tre kumulative vilkår**:
1. En behandlingsansvarlig eller databehandler er underlagt GDPR for den aktuelle behandlingen.
2. Denne (dataeksportøren) tilgjengeliggjør eller sender opplysningene til en annen behandlingsansvarlig, felles behandlingsansvarlig eller databehandler (dataimportøren).
3. Dataimportøren er i et land utenfor EØS eller er en internasjonal organisasjon.

Presiseringer (s. 1):
- Det er en overføring selv om importøren i tredjeland selv er direkte underlagt GDPR etter art. 3 nr. 2.
- **Ikke** overføring: ansatte i norsk virksomhet på forretningsreise utenfor EØS med fjerntilgang (ansatt er ikke en annen behandlingsansvarlig/databehandler). **Er** overføring: ansatt i datterselskap utenfor EØS i samme konsern med fjerntilgang til den norske virksomhetens opplysninger. Øvrige krav (f.eks. informasjonssikkerhet) gjelder uansett.
- Innsamling direkte fra personer i EØS på personens eget initiativ er ikke en overføring (EDPB).
- Alle opplysninger skal beskyttes uansett om personene er i eller utenfor EØS eller nasjonalitet.
- Definisjoner: **dataeksportør** = behandlingsansvarlig/databehandler som overfører; **dataimportør** = den som mottar.

### 2. Områder med tilstrekkelig beskyttelsesnivå (adekvans, art. 45) (s. 2)
EU-kommisjonen kan beslutte at en stat, et territorium, en sektor i en stat eller en internasjonal organisasjon har tilsvarende vern. Da trengs verken overføringsgrunnlag eller godkjenning fra Datatilsynet; overføringen er sammenlignbar med overføring innen EØS, og virksomheten trenger ikke gjøre egne vurderinger av beskyttelsesnivået eller ytterligere tiltak.

**Stater med adekvansbeslutning (per utskriften):**
| Stat | Forbehold |
|---|---|
| Andorra | – |
| Argentina | – |
| Brasil | – |
| Canada | Hvis importøren er underlagt PIPEDA (føderal lov for privat sektor) |
| Israel | – |
| Japan | Hvis importøren er underlagt APPI (privat sektor) – noen bransjer unntatt, bl.a. presse og universiteter |
| New Zealand | – |
| Sveits | – |
| Storbritannia | – |
| Sør-Korea | Hvis importøren er underlagt den sørkoreanske personopplysningsloven |
| Uruguay | – |
| USA | Hvis importøren står på listen over virksomheter sertifisert under **EU-U.S. Data Privacy Framework** |

**Områder:** Færøyene (hvis importøren er underlagt den færøyske personopplysningsloven), Guernsey, Isle of Man, Jersey.
**Internasjonale organisasjoner:** Den europeiske patentorganisasjonen (European Patent Organisation).

Merknader (s. 2):
- Enkelte adekvansbeslutninger kan ha unntak – sjekk EU-kommisjonens oversikt.
- USA: står en amerikansk virksomhet på listen på dataprivacyframework.gov, kan det overføres som til en europeisk virksomhet (Datatilsynets nyhetssak juli 2023 med spørsmål og svar).
- EDPB har veiledning om hva Kommisjonen bør vektlegge i adekvansvurderingen.
- For overføringer under direktiv (EU) 2016/680 (LED) gjelder adekvansbeslutninger etter direktivets art. 36 – foreløpig kun Storbritannia.

### 3. Ulike overføringsgrunnlag (art. 46) (s. 3)
Uten adekvans kan overføring bare skje hvis behandlingsansvarlig/databehandler har gitt «nødvendige garantier», og den registrerte har **håndhevbare rettigheter og effektive rettsmidler** (art. 46 nr. 1–2). Virksomheten er selv ansvarlig for å velge best egnet grunnlag. Listen i kilden (mest praktiske først):

1. **Standard personvernbestemmelser (SCC)** vedtatt av EU-kommisjonen (art. 46 nr. 2 c) – mest brukt.
2. **Bindende virksomhetsregler (BCR)** (art. 46 nr. 2 b og art. 47) – internasjonale konsern og grupper.
3. **Bindende avtale mellom offentlige myndigheter eller organer** innen og utenfor EØS (art. 46 nr. 2 a). EDPB Guidelines 2/2020 beskriver innholdet.
4. **Administrative ordninger** mellom offentlige myndigheter/organer og deres gjenpart utenfor EØS (art. 46 nr. 3 b). Må gi håndhevbare rettigheter og effektive rettsmidler; må godkjennes av Datatilsynet med tilslutning fra EDPB. EDPB Guidelines 2/2020; EDPB-uttalelse 4/2019 om administrativ avtale for ESMA kan brukes som mal.
5. **Godkjente atferdsnormer** (art. 46 nr. 2 e) sammen med bindende og håndhevbar avtale med importøren. EDPB Guidelines 04/2021. **Per i dag ingen godkjente atferdsnormer** for overføring.
6. **Godkjent sertifiseringsmekanisme** (art. 46 nr. 2 f) sammen med bindende og håndhevbar avtale med importøren. EDPB Guidelines 07/2022. **Per i dag ingen godkjente sertifiseringsmekanismer** for overføring.
7. **Egne avtalevilkår** (ad hoc-klausuler) (art. 46 nr. 3 a) – må godkjennes av Datatilsynet med EDPBs tilslutning; ingen presedens, tidkrevende.
8. **Datatilsynets egne standard personvernbestemmelser** (art. 46 nr. 2 d) – må godkjennes av EU-kommisjonen; ingen presedens, tidkrevende.

Formålet er å pålegge importøren plikter slik at opplysningene er like godt beskyttet som i EØS. Mottaker kan likevel være underlagt lokale lover som går foran → eksportøren må i tillegg undersøke om beskyttelsesnivået i praksis er tilsvarende. «Overføringsmekanisme nødvendig, men gir ikke alltid tilstrekkelig beskyttelse» (s. 3).

**Eksempel (s. 3):** Norsk virksomhet med datterselskaper i Israel, Thailand og Brasil. Israel har adekvans → ingen ytterligere tiltak. Thailand og Brasil → overføringsgrunnlag, f.eks. SCC. Vil brasiliansk mottaker ikke signere SCC, kan man utforme egen kontrakt med håndhevbare rettigheter, men den må godkjennes av Datatilsynet og EDPB (tidkrevende). Beskyttelsesnivået i Thailand og Brasil må vurderes og ev. ytterligere tiltak iverksettes. **[Merknad – ikke fra kilden]** Utskriften lister Brasil som adekvat på s. 2, mens eksemplet på s. 3 behandler Brasil som ikke-adekvat; eksemplet er trolig skrevet før adekvansbeslutningen for Brasil.

### 4. Standard personvernbestemmelser (SCC) (s. 4)
- EU-kommisjonens SCC (beslutning 2021/914), vedtatt **4. juni 2021**. Eldre SCC (2001/497/EC og 2010/87/EU) basert på direktiv 95/46/EF kan ikke lenger inngås. Avtaler på gamle SCC signert før 27. september 2021 var gyldige til 27.12.2022 (2021/914 art. 4); virksomheter skulle oppdatere senest før 27. desember 2022.
- Importøren forplikter seg til å behandle i samsvar med EØS-krav. Eksportøren må **sjekke at opplysningene faktisk får tilstrekkelig beskyttelse** og at rettssystemet i mottakerlandet gjør det mulig å følge SCC i praksis. Plikten er **bakt inn som eget kontraktsvilkår** – SCC forutsetter at nødvendige vurderinger er gjort **før signering**.
- Importøren skal snarest informere eksportøren om hindringer (f.eks. nasjonal lov som gir myndigheter tilgang utover det som er proporsjonalt og nødvendig i et demokratisk samfunn, jf. fortalepunkt 22 i 2021/914). Da skal eksportøren ikke overføre. Ved tvil kan Datatilsynet konsulteres. Datatilsynet har rett og kan ha plikt til å suspendere eller forby overføring (art. 58 nr. 2 j; Schrems II, C-311/18).
- Brukes SCC **uendret**: ingen forhåndsgodkjenning eller varsel til Datatilsynet.
- SCC kan inkorporeres i en større avtale; klausuler kan tilføyes uten varsel så lenge de ikke direkte eller indirekte motsier SCC. Har eksportøren konkludert med at ytterligere tiltak trengs, **må** disse tilføyes SCC.

**Fire moduler:**
| Modul | Eksportør (i EØS) | Importør (tredjeland) |
|---|---|---|
| 1 | Behandlingsansvarlig | Behandlingsansvarlig |
| 2 | Behandlingsansvarlig | Databehandler |
| 3 | Databehandler | Databehandler (underdatabehandler) |
| 4 | Databehandler | Behandlingsansvarlig |
SCC der databehandler er eksportør er en nyvinning.

**Husk (s. 4):** Ved overføring fra behandlingsansvarlig til databehandler kreves databehandleravtale (art. 28). **De nyeste SCC oppfyller kravene i art. 28** – ikke nødvendig med egen databehandleravtale i tillegg.

### 5. BCR som overføringsgrunnlag (art. 46 nr. 2 b, art. 47) (s. 5–6)
- Interne regler for overføringer i multinasjonale selskaper, konsern eller gruppe av foretak med felles økonomisk virksomhet. Søknad sendes Datatilsynet; godkjenning krever uttalelse fra EDPB.
- Før overføring må eksportøren likevel gjøre en selvstendig vurdering av om beskyttelsesnivået faktisk er tilsvarende, og om rettssystemet gjør det mulig å følge reglene. Er nivået lavere og ingen ytterligere tiltak hjelper → ikke overfør.

**Minimumsinnhold (art. 47 nr. 2):**
- konsernets struktur og kontaktopplysninger
- omfang («scope»)
- element som viser at reglene er bindende for alle i konsernet/gruppen
- anvendelse av de allmenne personvernprinsippene (f.eks. åpenhet, datakvalitet og sikkerhet)
- de registrertes rettigheter
- ansvarlighet til enheten etablert i EØS
- hvordan informasjon om BCR gis til de registrerte
- personvernombud
- fremgangsmåte for å klage
- mekanismer for å sikre overholdelse, f.eks. personvernrevisjoner
- rapportering og registrering av endringer til selskapene og tilsynsmyndigheten
- samarbeid med tilsynsmyndigheten
- rapportering til tilsynsmyndigheten av regler i tredjestat som sannsynligvis har betydelig negativ virkning på garantiene
- opplæring

**Fordeler:** 1) lettere å demonstrere etterlevelse av GDPR og kap. V; 2) mindre papirarbeid – ikke nye SCC for hver overføring; 3) fungerer som interne retningslinjer – klare og bindende instrukser; 4) konkurransefortrinn – BCR offentliggjøres.
- Lang saksbehandlingstid – regn med **et par år**. Ikke alle selskapsformer egner seg. Kontakt: bcr@datatilsynet.no. CNILs «BCR Self Assessment Tool» anbefales før innsending.

**Godkjenningsprosess (WP263rev.01), s. 5:**
1. Selskapet utpeker ledende tilsynsmyndighet (hovedkvarter i Norge → sannsynligvis Datatilsynet).
2. Selskapet utarbeider BCR (anbefales sterkt på engelsk). Søknaden må inneholde: utkast til BCR med ev. annekser; utfylt søknadsskjema og BCR-kriterier etter EDPB-anbefaling **1/2022** (behandlingsansvarlige) eller **1/2026** (databehandlere), med henvisninger til BCR-tekst og søknadsskjema; liste over bundne enheter og lokasjoner («List of entities bound»; for Tyskland angis delstat); bevis på at reglene er bindende for alle selskapene.
3. Ev. dokumentasjon på etterlevelse i praksis: personvernpolicyer; instrukser for ansatte (kan være del av «Code of conduct»); internkontrollrutiner; opplæringsplan og -materiell; beskrivelse av klageprosedyren; sikkerhetsrutiner; beskrivelse av PVOs oppgaver og støtte.
4. Dokumentene sendes Datatilsynet for vurdering; tilbakemelding ved behov for endringer.
5. Når kravene i art. 47 er oppfylt: søknaden sendes en annen EØS-tilsynsmyndighet (co-reviewer) for kvalitetssjekk. Flere enn 14 berørte tilsynsmyndigheter (etablering i over 14 EØS-land) → to co-reviewere.
6. Dokumentene deles med alle EØS-tilsynsmyndigheter for skriftlige kommentarer; diskuteres i EDPBs ekspertundergruppe for internasjonale overføringer; Datatilsynet formidler endringer.
7. Ved enighet sender Datatilsynet søknaden til EDPB, som skal gi uttalelse innen **åtte uker** (kan forlenges med seks uker).
8. Etter positiv uttalelse gir Datatilsynet endelig godkjenning.
9. Virksomheten må oversette BCR til alle relevante språk og gjøre den kjent (ansatte, kunder, forretningsforbindelser).
10. Plikt til å oppdatere BCR og underrette Datatilsynet om mindre endringer **én gang i året** (gjerne med sporede endringer); **større materielle endringer meldes umiddelbart**.
11. Endres kravene i 1/2022 og 1/2026, må skjemaet fylles ut på nytt ved årlig oppdatering.

**BCR godkjent før 25. mai 2018:** gjelder til de endres, erstattes eller oppheves (art. 46 nr. 5), men virksomheten må oppdatere dokumentene etter GDPR (bruk 1/2022 og 1/2026) og varsle Datatilsynet om endringene (kan skje med den årlige rapporteringen, art. 47 nr. 2 k).

### 6. Tilleggskrav – Schrems II (s. 7–8)
- Schrems II (C-311/18): man må alltid undersøke om beskyttelsesnivået i praksis undergraves av forhold i tredjelandet, f.eks. overvåkingslover som går lenger enn nødvendig og proporsjonalt; i så fall ytterligere tiltak.
- To typetilfeller: (a) overføring på virksomhetens vegne (sending, lagring i tredjeland, support fra tredjeland); (b) databehandleren overfører i strid med virksomhetens ønsker (behandles i kapittel 7 om EØS-skytjenester).
- **Bygger overføringen på adekvansbeslutning eller et art. 49-unntak, kan man se bort fra tilleggskravene.**
- Bakgrunn: Privacy Shield ble kjent ugyldig; SCC fortsatt gyldig, men ikke alltid tilstrekkelig, fordi SCC ikke binder tredjelandets myndigheter. Er ytterligere tiltak nødvendige men ikke iverksatt, er overføringen **ulovlig og må opphøre**. Tilsynsmyndighetene legger til grunn at det samme gjelder **andre overføringsgrunnlag**.
- Ikke alle overvåkingslover er problematiske: unntak fra personvernet kan være proporsjonale og strengt nødvendige; lovene må angi når, på hvilke vilkår og i hvilket omfang de gjelder, ha garantier mot misbruk, og de registrertes rettigheter og effektive rettsmidler må ivaretas i praksis.
- USA: etterretningslovene er oppdatert etter Schrems II, og USA har fått ny adekvansbeslutning.
- EU-domstolens dommer og EU-charteret er ikke direkte bindende for Norge, men GDPR tolkes likt, så avgjørelsene har stor betydning. EMK er bindende via menneskerettsloven.

**Fem steg i vurderingen (sjekkliste, s. 7):**
1. **Kjenn overføringene** – full oversikt over prosesser, systemer, tjenester, løsninger, partnere, leverandører, databehandlere og underleverandører som overfører ut av EØS. Fjerntilgang (f.eks. teknisk støtte) er overføring. Alle overføringer skal stå i protokollen; plikt til å informere de registrerte. Husk nettsidetillegg, markedsføringstjenester og skytjenester, og videreoverføringer («onward transfers»).
2. **Identifiser overføringsgrunnlag** – før overføringen starter. Ved bruk av unntaksreglene trengs ikke steg 3 og 4.
3. **Vurder om grunnlaget vil være effektivt i lys av alle omstendighetene** – lover og praksis i tredjelandet: påvirker de behandlingen, gir de lavere beskyttelse i praksis? Vurder også databehandlere, underleverandører og infrastruktur. Bare lover/praksis som går lenger enn nødvendig og proporsjonalt undergraver nivået.
4. **Iverksett ytterligere tiltak** – som sikrer tilsvarende nivå i praksis. Finnes ikke slike, eller kan de ikke iverksettes: **ikke overfør**.
5. **Re-evaluer med jevne mellomrom** – lovgivning kan endres, tiltak kan bli ineffektive, importøren kan bryte forpliktelser, unntak kan brukes mer enn forutsatt.

**Steg 3 – vurdering av beskyttelsesnivået (s. 7–8).** Se på alle aktører (behandlingsansvarlige, databehandlere, underleverandører) og infrastruktur. Hvilke lover og praksis som gjelder kan avhenge av:
- formålet (markedsføring, HR, lagring, teknisk støtte, kliniske studier)
- typen aktører (offentlige/private, behandlingsansvarlige/databehandlere)
- sektor (adtech, telekom, finans, journalistikk, helse)
- kategori personopplysninger (f.eks. særlover for mindreårige)
- om data lagres i tredjeland eller det er fjerntilgang til data lagret i EØS
- dataformat (klartekst, pseudonymisert, kryptert)
- mulighet for videreoverføring til nye tredjeland

Eksempel: noen land begrenser myndigheters adgang til informasjon fra medier, advokater eller helsepersonell.

- **Inngrep vs. krenkelse:** lover/praksis kan være et *inngrep* uavhengig av sensitivitet eller faktisk skade, men det er bare en *krenkelse* når de går lenger enn nødvendig og proporsjonalt. **Ytterligere tiltak trengs bare ved krenkelse.**
- Momenter for krenkelsesvurderingen: EMDs praksis etter EMK art. 8 (faktaark om masseovervåking); Schrems II; art. 45 nr. 2; EDPB-anbefaling 02/2020 om europeiske essensielle garantier for overvåkingstiltak.
- Offentlig tilgjengelige opplysninger: myndighetsinnhenting av slike vil lettere være proporsjonal – konkret vurdering. Å publisere opplysninger kun for å overføre dem er brudd på både art. 6 og kap. V.
- **Lov vs. praksis:** Er loven i orden, men praktiseres krenkende (eller lovene er hemmelige/mangler), må tiltak iverksettes. Er loven problematisk, men det er ingen grunn til å tro at den anvendes på de overførte opplysningene i praksis, trengs ikke ytterligere tiltak – men dette må **dokumenteres detaljert**, bl.a. med erfaringer fra lignende aktører i samme bransje/tilsvarende overføringer og annen aktuell informasjon.
- Importørens dokumenterte erfaring med tidligere utleveringsbegjæringer kan vektlegges, men bare hvis tredjelandets lov ikke forbyr importøren å informere om slike. At importøren ikke har mottatt begjæringer er **ikke i seg selv tilstrekkelig**, men kan inngå i en helhetsvurdering.

**Krav til informasjonen vurderingen bygger på:**
- **relevant** – til hjelp i den konkrete situasjonen, ikke generell/abstrakt
- **objektiv** – underbygget av empirisk kunnskap, ikke antakelser
- **pålitelig** – kilden og informasjonen vurderes kritisk hver for seg
- **verifiserbar** – tilsynsmyndigheter/domstoler må kunne etterprøve
- **tilgjengelig** – må kunne deles med tilsynsmyndigheter, domstoler og de registrerte

Se EDPB-anbefaling 01/2020 om ytterligere tiltak (bl.a. informasjonskilder).

**Steg 4 – ytterligere tiltak (s. 8):**
- Tekniske, juridiske eller organisatoriske – ofte kombinert. I utgangspunktet bør **tekniske tiltak** inngå, fordi lokale lover går foran avtaler; juridiske/organisatoriske tiltak alene vil sjelden være nok. Konkret vurdering.
- **Kryptering** (sterk) og nøkkelhåndtering sentralt: motvirker myndighetstilgang under transport og lagring så lenge nøkkelen ikke er eller blir tilgjengelig for myndighetene/aktører under tredjelandets lov. Skyleverandører kan ha særskilte fremgangsmåter for å hente ut kryptert data (se NSM). Forvalter importøren nøkkelen på vegne av behandlingsansvarlig, er kryptering **ikke** effektivt mot utleveringsbegjæringer. Algoritmen må være state-of-the-art og kvalitetssikres rutinemessig.
- **Pseudonymisering**: forutsetter at koblingsnøkkelen ikke er eller blir tilgjengelig for myndighetene; ta hensyn til informasjon myndighetene kan forventes å ha. Særlig praktisk for forskning.
- **Juridiske tiltak**: kontraktsforpliktelse til bestemte tekniske tiltak og nøkkelhåndtering; forbud mot reidentifisering; plikt for importøren til å bistå med å vurdere og følge med på beskyttelsesnivået; informere om pålegg fra overvåkingsmyndigheter hvis mulig; utfordre alle utleveringsbegjæringer; hjelpe registrerte med rettighetene i tredjelandet.
- **Organisatoriske tiltak**: interne rutiner, fremgangsmåter og internkontroll for å håndtere utleveringsbegjæringer, gode rapporteringslinjer, god dokumentasjon av begjæringer, opplæring og streng tilgangsstyring.
- EDPB 01/2020 anneks 2 inneholder flere eksempler (ikke uttømmende).
- Ved valg av tiltak, se på: dataformat; dataenes natur (f.eks. særlige kategorier); lengde og kompleksitet i behandlingsforløpet, antall aktører og forholdet mellom dem; hvilke teknikker/parametere tredjelandets lovgivning anvendes gjennom; mulighet for videreoverføring (f.eks. via underleverandør).
- Tiltak sikrer tilstrekkelig nivå → overføring kan starte. Tiltak påkrevd men ikke iverksatt/effektive → ingen overføring. Tidligere lovlig, men endrede omstendigheter gjør den ulovlig → **overføringene må opphøre, og allerede overførte data tilbakeføres eller slettes**.

**Vurderinger og dokumentasjon (s. 8):** Virksomhetene må selv vurdere (ansvarlighet). Datatilsynet kan **ikke forhåndsgodkjenne** vurderingene. Gjør dem samvittighetsfullt og dokumenter godt – i tilsynssaker vil Datatilsynet være særlig opptatt av dokumentasjonen. Datatilsynet vil tolke loven likt som EDPB.

### 7. Opplysninger behandlet i EØS, inkludert skytjenester i EØS (s. 9–11)
- Behandling i EØS eller adekvat land er i utgangspunktet ikke overføring, men opplysninger kan havne i ikke-adekvate land hvis skyleverandøren er underlagt tredjelands lovgivning.
- EDPB-rapport (Coordinated Enforcement Action, offentlig sektors bruk av skytjenester; relevant også for private): flere fallgruver ved ikke-europeiske skyleverandører; feil kan gi brudd på art. 28. Sitat (Datatilsynets oversettelse): «Når anvendelsen av tredjelands lovgivning gjør det mulig å be om utlevering av data lagret av skytjenesteleverandøren i EØS, bør en grundig analyse gjennomføres før avtalen inngås.» Se også reviderte Guidelines 05/2021 (avsnitt 24 og eksempel 12).
- Plikten til informasjonssikkerhet gjelder uansett. Manglende vurderinger i forkant kan være i strid med ansvarlighetsprinsippet – «i seg selv et alvorlig lovbrudd» – selv om behandlingen senere viser seg uproblematisk.

**Flytskjema (s. 9):** Behandle personopplysninger i EØS → Kan overføringer likevel skje? Nei → OK. Ja → Hvem er behandlingsansvarlig for ev. overføring? «Vi» → følg reglene om overføring til tredjeland. «Tjenesteleverandør i kontekst av databehandleroppdraget» → Tiltak og garantier på plass? Ja → OK / Nei → Ikke OK. «Tjenesteleverandør i kontekst av avtale om utlevering til ny behandlingsansvarlig» → Lovlig utlevert? Ja → OK / Nei → Tiltak og garantier på plass?

**Steg 1 – Kan overføringer likevel skje?** Eksempler: tjenesten spesifiserer at support kan ytes fra ikke-adekvat land (visse tider på døgnet, krisegjenoppretting) – tilgang inkl. fjerntilgang er overføring; tjenesteavtalen tar forbehold om utlevering til myndigheter i ikke-adekvat land; tjenesten er underlagt juridiske forpliktelser i ikke-adekvat land som går foran avtalen. Reglene om overføring gjelder i det øyeblikket **tilgang** finnes.

**Steg 2 – Hvem er behandlingsansvarlig for den mulige overføringen?** Den som bestemmer formål og midler (typisk den som har interesse i overføringen). Support til dere → trolig dere; følg reglene i kapittel 1–6. Overføring for at leverandøren skal oppfylle egne juridiske forpliktelser → trolig leverandøren, men dere har ansvar fordi dere tar leverandøren i bruk → gå til steg 3. Felles behandlingsansvar kan foreligge (Fanpage-dommen, Wirtschaftsakademie Schleswig-Holstein).

**Steg 3 – Forpliktelser når leverandøren potensielt kan overføre:**
- Bare databehandlere med «tilstrekkelige garantier» kan brukes (art. 28 nr. 1), bl.a. at opplysninger ikke overføres ulovlig i leverandørkjeden. Art. 28 nr. 1 er en form for risikovurdering (art, omfang, omstendigheter), men gir **ingen** dekning for å velge leverandører som sier de kan bryte avtalen, instruksene eller GDPR. «Man kan altså ikke risikovurdere seg bort fra eget ansvar.»
- Forbehold som innebærer brudd, eller grunn til å tro at databehandleren kan bryte reglene → tiltak, ellers kan databehandleren ikke benyttes. **Vage og vide forbehold om overføring til ikke-adekvate land for å oppfylle leverandørens juridiske forpliktelser er et typisk holdepunkt** for at tiltak må iverksettes.
- Tiltak: som i kapittel 6; kryptering eller pseudonymisering med god nøkkelhåndtering særlig praktisk. Eksempel «Navn Navnesen»: er data korrekt pseudonymisert og bare kunden har koblingsnøkkelen, kan skytjenesten brukes lovlig selv om den er underlagt problematisk tredjelandslov – forutsatt at sammenstilling ikke avslører identitet.
- Kan opplysninger leses i klartekst i skyen (f.eks. ikke kryptert under behandling), anbefales pseudonymisering (EDPB 1/2020, særlig para. 94–96).
- For effektiv kryptering bør leverandøren **ikke ha tilgang til krypteringsnøkkelen**.
- En databehandler kan lovlig utlevere når det er pålagt etter EU-rett eller nasjonal rett i et EØS-land.

**Steg 4 – Hva er avtalt?** Leverandør kan være behandlingsansvarlig for noen behandlinger og databehandler for andre. Er det avtalt at leverandøren er behandlingsansvarlig for en behandling som kan gi overføring, sitter i utgangspunktet den nye behandlingsansvarlige med ansvaret – men dere må ha rettslig grunnlag (art. 6, ev. art. 9) for utleveringen, utleveringen må være forenlig med formålet, og informasjonsplikten gjelder. Kan dere ikke lovlig utlevere → tiltak for at leverandøren bare behandler etter instruks (steg 3).

**Europeiske eksempler (s. 10–11):**
- Ansvar for å velge databehandler/skyleverandør som oppfyller GDPR; er leverandøren databehandler, må dere sikre at den kun behandler og overfører etter instruks (EDPB-rapporten).
- **Sverige:** Stockholm Kommunstyrelsen ba IMY om forhåndsdrøftelse (2021) om Azure AD og Teams (USA uten adekvans da). Bruken innebar ingen overføring i seg selv, men overføring kunne skje om Microsoft ble pålagt utlevering etter amerikansk lov. Kommunen hevdet lav sannsynlighet og harmløse data. IMY: DPIA mangelfull; kommunen må etter art. 28 ta stilling til tekniske og organisatoriske garantier mot ulovlig overføring (f.eks. utlevering i strid med art. 48); får den ikke tilstrekkelige garantier, kan den ikke velge leverandøren.
- **Frankrike:** Conseil d'État – bruk av leverandør underlagt tredjelandslov er ikke i seg selv overføring, men overføring kan skje ved utleveringsforespørsler. Ikke ulovlig i den konkrete saken (Doctolib/covid-19-vaksinering), bl.a. fordi data var kryptert og nøkkelen håndtert av en tredjepart i Frankrike.
- **Danmark:** Datatilsynet.dk har skyveileder (dansk og engelsk). Skiller mellom «tilsigtet» og «utilsigtet» overføring (KOMBIT-saken): (i) formål knyttet til virksomhetens behov (support e.l.) eller eksplisitt forbehold fra databehandler → tilsiktet; virksomheten ansvarlig for kap. V. (ii) Overføringer i strid med databehandleravtalen → utilsiktet; fritar ikke for ansvar, men tillater mer risikobasert tilnærming. Norsk Datatilsynet: selv uten forbehold i avtalen kan det finnes holdepunkter for ulovlige overføringer (f.eks. avdekket i risikovurdering etter art. 32) som krever tiltak; ulik tolkning kan forekomme, men betydningen i praksis er usikker fordi leverandører underlagt tredjelandslov som regel tar forbehold.

### 8. Unntak – art. 49 (s. 12–14)
- Brukes bare hvis man ikke klarer å identifisere et effektivt overføringsgrunnlag. Ikke hovedregel; tolkes **restriktivt**; gir ikke tilsvarende beskyttelse → forhøyet risiko. EDPB Guidelines 2/2018 om art. 49.
- Unntakene for samtykke og avtaleoppfyllelse kan **ikke** brukes av offentlige organer i utøvelse av offentlig myndighet. Avtale- og rettskravsunntakene kan bare brukes **leilighetsvis**.
- To steg: man må alltid ha behandlingsgrunnlag (art. 6) for behandlingen, og deretter overføringsgrunnlag; art. 49 kun hvis intet effektivt grunnlag finnes.
- Nasjonal lov kan begrense overføring av spesifikke kategorier; foreløpig ingen slik lovgivning i Norge.

**Oversikt – unntak og vilkår:**
| Unntak (art. 49 nr. 1) | Sentrale vilkår | Offentlig myndighetsutøvelse? | Leilighetsvis? |
|---|---|---|---|
| a) Uttrykkelig og informert samtykke | Gyldig samtykke (art. 4 nr. 11, art. 7; frivillig, aktiv handling, kan trekkes); uttrykkelig; informert om **mulige risikoer** ved overføringen (f.eks. ingen tilsynsmyndighet/likeverdige rettigheter, mottakere eller kategorier, alle land opplysningene sendes til, at samtykke er grunnlaget, at det ikke foreligger adekvans – kan være standardisert); **spesifikt** (ikke mulig for ukjente fremtidige overføringer); innhentet **før** overføringen | Nei | – |
| b) Nødvendig for å oppfylle avtale med den registrerte (eller tiltak før avtaleinngåelse etter den registrertes ønske) | Nødvendighet = nær årsakssammenheng; ikke for ytterligere opplysninger. EDPB Guidelines 2/2019 om art. 6 nr. 1 b relevante | Nei | Ja |
| c) Nødvendig for å inngå/oppfylle avtale i den registrertes interesse mellom behandlingsansvarlig og annen fysisk/juridisk person | Nødvendighet og leilighetsvis | Nei | Ja |
| d) Viktige allmenne interesser anerkjent i EØS-rett eller norsk rett | Må kunne utledes av EØS-rett/norsk rett at overføringen tillates for slike interesser (f.eks. gjensidighet i internasjonalt samarbeid; indikasjon: internasjonal avtale som Norge er part i). Eksempler: utveksling mellom konkurranse-, skatte-, toll-, finanstilsyns-, trygde- eller folkehelsemyndigheter (smittesporing, antidoping); humanitær organisasjon etter Genève-konvensjonene. Rettet mot offentlige, men privat kan bruke det | Ja (hovedsakelig offentlige) | Ikke krav, men ikke systematisk/i stor skala; vanlig drift → art. 46 |
| e) Fastsette, gjøre gjeldende eller forsvare rettskrav | Også forvaltningssaker og utenrettslige prosedyrer (reguleringsorganer). Nær sammenheng og nødvendighet; «godvilje» hos utenlandske myndigheter ikke nok; begrens til det nødvendige; anonymiserte/pseudonymiserte data hvis tilstrekkelig; ikke for ren mulighet for fremtidige prosesser; prosessen bør fremgå av formelt regelverk | Ja | Ja |
| f) Vitale interesser når den registrerte fysisk eller juridisk ikke kan samtykke | Medisinsk nødsituasjon, direkte nødvendig; ikke generelle fremtidige vitale interesser (ikke forskning); juridisk ute av stand pga. mental tilstand eller alder (norske regler, f.eks. pasient- og brukerrettighetsloven: 16 år for helsehjelp); kan ikke brukes hvis personen kan samtykke | Ja | – |
| g) Fra offentlig register | Register som etter norsk rett/EØS-rett skal gi informasjon til allmennheten, tilgjengelig for allmennheten eller enhver med berettiget interesse; vilkårene må være oppfylt i det konkrete tilfellet. Ikke hele registeret/hele kategorier; ved register for berettiget interesse kun på anmodning fra disse eller når de selv er mottakere; vurdering fra sak til sak; videre bruk i samsvar med regelverket | Ja | – |
| Annet ledd: tvingende berettigede interesser | Enkeltstående, ikke-gjentakende; nødvendig av hensyn til tvingende berettigede interesser som går foran de registrertes; begrenset antall registrerte; vurder alle omstendigheter og gi nødvendige garantier; dokumenter i protokollen; **varsle Datatilsynet**; informere de registrerte om overføringen og interessene. Ta særlig hensyn til opplysningenes art, formål, varighet og situasjonen i mottakerstaten og endelige mottakerstater | Nei | (enkeltstående) |

**Eksempler i kilden:**
- Avtale (b): reisebyrå som sender klientopplysninger til hoteller og guider i Chile → kan bruke unntaket. Selskap som sentraliserer HR/lønn i India av forretningsmessige grunner → kan ikke (ingen direkte og objektiv forbindelse); bruk SCC eller BCR. (Kilden nummererer disse «Eksempel 1» og «Eksempel 3».)
- Leilighetsvis: selger som reiser og hvis opplysninger sendes til potensielle kunder i tredjeland → leilighetsvis; EU-bank som sender til bank i Brasil for en kundeforespurt transaksjon → leilighetsvis, men ikke hvis del av stabilt samarbeid; multinasjonalt selskap med jevnlige kurs i Singapore via fast partner (navn, stilling, matallergier, tilretteleggingsbehov) → systematisk og gjentakende, ikke leilighetsvis.
- Avtale i den registrertes interesse (c): lønnsleverandør i Moldova valgt av kostnadshensyn → ikke objektivt nødvendig; unntaket ikke passende.
- Rettskrav (e): forsvar i kriminal-/administrativ etterforskning utenfor EØS (korrupsjon, konkurranserett, innsidehandel); reduksjon/bortfall av bøter eller gebyr; fremlegging av dokumenter før sivil rettssak; igangsette prosessuelle steg; søke godkjenning av selskapsfusjon.
- Vitale interesser (f): person kritisk syk i Mongolia → ja; helseforetak som vil bidra til forskningsprosjekt → nei, bruk f.eks. SCC.
- Offentlige registre (g): selskapsregistre, organisasjonsregistre, register over dommer, registre over rettigheter og forpliktelser i eiendom, kjøretøyregistre.

**Art. 48 – krav om utlevering fra domstol eller forvaltningsorgan i tredjeland (s. 14):** Slik utlevering skal i utgangspunktet bare skje hvis dommen/vedtaket kan anerkjennes og håndheves etter internasjonal avtale (f.eks. traktat om gjensidig juridisk bistand). Foreligger slik avtale, bør virksomheten normalt **avslå** kravet og henvise til avtalen og relevante norske myndigheter.

### 9. Eksempelsaker fra veiledningsmøter (s. 15)
Datatilsynet kan ikke forhåndsgodkjenne løsninger, men gir råd.
- **Vestre Viken HF – pseudonymisering som effektivt tiltak:** hjemmedialyse via skytjeneste; leverandør og sky underlagt tredjelands lovgivning; data i EØS, men support fra tredjeland og mulige utleveringsbegjæringer. Datatilsynet: i supporttilfellene trolig Vestre Viken som er behandlingsansvarlig for overføringer → kapittel V (del 1–6) gjelder; i tillegg tiltak mot ulovlig utlevering (del 7). Tiltak: pseudonymisering med eksisterende pasientpseudonym (egnet – koblingsnøkkel under helseforetakets kontroll, ikke tilgjengelig for tredjelands myndigheter); Datatilsynet frarådet å kombinere med initialer (økt identifiserbarhet). Ingen innvendinger mot videre gjennomføring.
- **Sikt – ikke grunn til å tro at problematisk lovgivning får anvendelse:** felles løsning for identitets- og tilgangsstyring fra amerikanske leverandører i amerikanskeid sky; ansatte i USA trengte klartekst-tilgang; USA uten adekvans på tidspunktet. FISA 702 identifisert som problematisk og uproporsjonal. EDPB: ikke behov for tiltak hvis ikke grunn til å tro at loven anvendes i praksis. Datatilsynet: vurderingen er «binær» – enten «grunn til å tro» eller «ikke grunn til å tro»; ikke krav om 100 % sikkerhet, men en viss sannsynlighetsovervekt basert på grundige vurderinger; spørsmålet er om loven får anvendelse, ikke om myndighetene vil bruke den. Sikt spurte flere leverandører om tidligere utleveringsbegjæringer (ingen); vurderte lovtekst og amerikansk dokumentasjon, eksperter; vurderte «possession, custody or control», og om dataene er «contents of communications» til/fra en «target» (system-til-system-kommunikasjon falt utenfor; systemet inneholdt bare om varsel var sendt, e-post håndtert i separat system). Sikt gikk videre med avtalemessige tilleggstiltak. Datatilsynet godkjente ikke vurderingen, men bekreftet handlingsrom og at vurderingene fremsto grundige og metodisk gode.

## Praktiske sjekkpunkter
- Kartlegg alle overføringer, inkl. fjerntilgang/support, underleverandører, onward transfers, nettsidetillegg og markedsføringsverktøy; før dem i protokollen og informer de registrerte.
- Test de tre EDPB-vilkårene for «overføring».
- Sjekk adekvans først (inkl. forbehold for Canada, Japan, Sør-Korea, Færøyene; for USA: er importøren DPF-sertifisert?). Kontroller EU-kommisjonens oversikt for unntak.
- Uten adekvans: velg art. 46-grunnlag – normalt SCC 2021/914 med riktig modul (1–4), eller BCR for konsern. Kontroller at SCC brukes uendret, og at tilleggsklausuler ikke motsier dem.
- Ved SCC modul 2/3: egen DPA ikke nødvendig, da SCC dekker art. 28.
- Gjennomfør og dokumenter en TIA (steg 3) før signering: lover og praksis, alle aktører og infrastruktur, sektor, datakategori, lagring vs. fjerntilgang, dataformat, videreoverføring; kildene må være relevante, objektive, pålitelige, verifiserbare og tilgjengelige.
- Skill inngrep fra krenkelse; tiltak kreves kun ved krenkelse. Dokumenter grundig hvis det konkluderes med at problematisk lov ikke anvendes i praksis.
- Ved behov for ytterligere tiltak: prioriter tekniske tiltak (sterk kryptering der importør/leverandør **ikke** har nøkkelen; pseudonymisering med koblingsnøkkel utenfor tredjelandets rekkevidde), supplert med kontraktsmessige og organisatoriske tiltak; legg dem inn i SCC.
- Finnes ingen effektive tiltak: ikke overfør; ved endrede forhold: stans overføring og tilbakefør/slett data.
- Re-evaluer jevnlig.
- EØS-sky med leverandør underlagt tredjelandslov: gå gjennom de fire stegene; se etter vage forbehold om utlevering/overføring i DPA/tjenestevilkår; krev garantier etter art. 28; vurder egen nøkkelhåndtering.
- Art. 49 bare som siste utvei, restriktivt; kontroller vilkår for hvert unntak, herunder «leilighetsvis» og forbud for offentlig myndighetsutøvelse; for annet ledd: varsle Datatilsynet og informer de registrerte.
- Avslå utleveringskrav fra tredjelands domstoler/myndigheter som ikke bygger på internasjonal avtale (art. 48).

## Viktige sitater
- «Hvis det ikke finnes, er overføringen ulovlig. Det gjelder også hvis overføringsgrunnlaget ikke vil fungere i praksis.» (s. 1)
- «De nyeste standard personvernbestemmelsene fra EU-kommisjonen oppfyller kravene i personvernforordningen artikkel 28.» (s. 4)
- «Dersom man bruker personvernbestemmelsene uendret, trenger man hverken søke om forhåndsgodkjenning eller varsle Datatilsynet.» (s. 4)
- «Dersom det er nødvendig med ytterligere tiltak, men slike tiltak ikke iverksettes, er overføringen ulovlig og må opphøre.» (s. 7)
- «Man trenger bare iverksette ytterligere tiltak der det foreligger en krenkelse.» (s. 7)
- «Dersom derimot en dataimportør i tredjeland forvalter krypteringsnøkkelen på vegne av behandlingsansvarlig, vil ikke kryptering være effektivt mot utleveringsbegjæringer fra lokale myndigheter.» (s. 8)
- «Man kan altså ikke risikovurdere seg bort fra eget ansvar.» (s. 10)
- «Et unntak skal ikke benyttes som hovedregel, og unntakene må tolkes restriktivt.» (s. 12)

## Kryssreferanser
- GDPR: art. 3 nr. 2, 4 nr. 11, 6, 7, 9 nr. 2 a, 28 (nr. 1, 3), 30, 32, 44–49, 58 nr. 2 j; direktiv (EU) 2016/680 art. 36
- Rettspraksis: C-311/18 (Schrems II); Wirtschaftsakademie (Fanpage); EMD om masseovervåking (EMK art. 8)
- EDPB: Guidelines 3/2018, 05/2021, 2/2018, 2/2019, 2/2020, 04/2021, 07/2022; Recommendations 01/2020 og 02/2020; Recommendations 1/2022 og 1/2026 (BCR); WP263rev.01
- [K38](K38-tia-guide.md) – TIA-veiledning
- [K05](K05-dt-databehandleravtale.md) – databehandleravtaler; [K01](K01-dt-behandlingsansvarlig-og-databehandler.md) – roller
- [K04](K04-dt-fore-protokoll.md) – protokoll (overføringer skal fremgå)
- [K10](K10-dt-kryptering.md) – kryptering som tiltak
- [K02](K02-dt-behandlingsgrunnlag.md) – behandlingsgrunnlag/samtykke
- [K12](K12-dt-dpia-veiledning.md) – DPIA (IMY-saken viser mangelfull DPIA ved skyvalg)

## Aktualitet og begrensninger
- Utskrift 22.09.2026; ingen publiseringsdato vises, men teksten nevner EDPB-anbefaling 1/2026 (BCR-P) og USA-adekvans (DPF, juli 2023) – oppdatert nylig.
- Adekvanslisten er et øyeblikksbilde «per nå»; sjekk EU-kommisjonens oversikt. **[Merknad – ikke fra kilden]** Adekvansbeslutningen for EU-U.S. Data Privacy Framework har vært gjenstand for rettslige utfordringer; kontroller status ved bruk.
- Overgangsfristene for gamle SCC (27.12.2022) er utløpt; gamle SCC kan ikke brukes.
- Noen eksempler (Brasil-eksemplet, Sverige/Sikt-sakene) er skrevet da Brasil/USA ikke hadde adekvans.
- Norsk kontekst: EU-domstolens dommer og charteret er ikke direkte bindende for Norge, men styrende for tolkning.

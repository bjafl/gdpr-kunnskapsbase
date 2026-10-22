---
id: K12
tittel: "Veiledning om DPIA (Vurdering av personvernkonsekvenser)"
utgiver: Datatilsynet
dato: "Udatert i utskriften (nettside skrevet ut 2026-09-22)"
spraak: nb
fil: "ressurser/Datatilsynet/Veiledning om DPIA _ Datatilsynet.pdf"
url: "https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/vurdering-av-personvernkonsekvenser/ (utskrift med ?print=true)"
type: veileder
gdpr_artikler: [5, 9, 10, 22, 24, 25, 28, 30, 32, 35, 36, 39]
emner: [dpia, risikovurdering, forhandsdroftelse, hoy-risiko, wp29-kriterier, dpia-liste]
relevans: høy
---

# Veiledning om DPIA – vurdering av personvernkonsekvenser (Datatilsynet)

## Sammendrag
Datatilsynets samlede nettveileder om vurdering av personvernkonsekvenser (Data Protection Impact Assessment, DPIA) etter GDPR art. 35, og om forhåndsdrøftelse med Datatilsynet etter art. 36. Veilederen dekker når en DPIA er påkrevd, Datatilsynets nasjonale liste over behandlinger som alltid krever DPIA, når DPIA ikke kreves, hvem som har ansvaret og hvem som skal involveres, hva en DPIA kan omfatte (flere behandlinger, tekniske produkter), forholdet til eksisterende behandlinger og endringer i risiko, begrepet «høy risiko» (fire vurderingsmomenter og Artikkel 29-gruppens ni kriterier med eksempeltabell), minimumsinnhold (art. 35 nr. 7), offentliggjøring, og en detaljert beskrivelse av forhåndsdrøftelse (når, hva som skal sendes inn, mulige utfall, to eksempler). Til slutt lister den eksisterende rammeverk (SDM, AEPD, CNIL, ISO/IEC 29134 m.fl.). Veilederen bygger på anbefalingene fra Artikkel 29-gruppen (WP248), supplert med Datatilsynets erfaring fra konsesjonsbehandling. Målgruppe: behandlingsansvarlige, personvernombud og rådgivere.

PDF-en er en utskrift av nettsiden (13 sider); utskriften har ingen synlig publiserings- eller endringsdato.

## Når skal agenten bruke denne kilden
- Avgjøre om en planlagt behandling krever DPIA (nasjonal liste + WP29-kriterier + «to av ni»-tommelfingerregel).
- Begrunne og dokumentere at DPIA *ikke* er nødvendig.
- Avklare roller: behandlingsansvarlig, personvernombud (PVO), databehandler, de registrerte, informasjonssikkerhetsansvarlig, IT, ledelse.
- Fastsette minimumsinnhold i en DPIA og struktur på risikovurderingen (konsekvens × sannsynlighet, liste over hva som skal vurderes).
- Avgjøre om forhåndsdrøftelse med Datatilsynet er nødvendig, og hva en anmodning må inneholde.
- Skille sikkerhetsrisikovurdering (art. 32) fra personvernkonsekvensvurdering (art. 35).
- Finne referanserammeverk/metoder for DPIA.

## Hovedinnhold

### 1. Innledning og om DPIA (s. 1)
- Art. 35 definerer når DPIA er påkrevd, hva den skal inneholde og hvem som skal gjennomføre den. Datatilsynet har laget en sjekkliste som oppsummerer veiledningen («Sjekkliste for vurdering av personvernkonsekvenser», se [K21](K21-dt-sjekkliste-dpia-faser.md)).
- **Definisjon:** En DPIA er «en prosess som skal beskrive behandlingen av personopplysninger, og vurdere om den er nødvendig og proporsjonal». Den skal også bidra til å håndtere risikoene for enkeltpersoners rettigheter og friheter ved å vurdere dem og fastlegge risikoreduserende tiltak (s. 1).
- DPIA er et viktig verktøy for **ansvarlighet** (jf. art. 24): den hjelper med etterlevelse og med å dokumentere at tilstrekkelige tiltak er gjort – «en prosess som skal bidra til å skape og påvise etterlevelse» (s. 1).
- **En gjentagende prosess:** Å vurdere personvernkonsekvenser er en prosess som alltid skal gjennomføres for alle behandlinger. En konkret DPIA etter art. 35 gjentar prosessen, men først og fremst for å finne *ekstra* tiltak for å redusere en høy risiko man ikke har klart å redusere tidligere (s. 1).
- **DPIA reparerer ikke ulovlig behandling.** Alle behandlinger må i utgangspunktet oppfylle grunnkravene i forordningens øvrige bestemmelser. Usikker på lovlighet → start i art. 5, 6 og 9, ikke art. 35. Usikker på rettigheter → art. 12–22 (s. 1).
- Det meste av innholdet i en DPIA skal altså være gjort fra før (oversikt over behandlinger som del av internkontrollen). DPIA krever *i tillegg* at det iverksettes nødvendige tiltak for å oppfylle de registrertes rettigheter **utover minimumskravene** når behandlingen utgjør en særskilt risiko (basert på art, omfang, formål og sammenheng). «Nødvendige tiltak» = tiltak som går utover lovens ordlyd, men som etter en forholdsmessighetsvurdering er nødvendige for å sikre balansen mellom personverninteresser og virksomhetens interesser (s. 1).

### 2. Sanksjoner (s. 1)
Manglende overholdelse kan gi sanksjoner. Hvis det ikke foretas DPIA der det er pålagt (art. 35 nr. 1, 3, 4), DPIA utføres på uriktig måte (art. 35 nr. 2 og nr. 7–9), eller forhåndsdrøftelse unnlates når det er krav (art. 36 nr. 3 bokstav e), kan det gi administrative bøter på **opptil 10 millioner euro**, eller for virksomhet **opptil 2 % av samlet global årsomsetning** i forutgående regnskapsår – det høyeste beløpet benyttes (s. 1).

### 3. Om innholdet i veilederen (s. 1)
Bygger på anbefalingene fra Artikkel 29-gruppen (WP248, se [K24](K24-wp248-dpia.md)), med utdypninger basert bl.a. på Datatilsynets erfaring med konsesjonsbehandling (Norge hadde, i motsetning til mange EU-land, konsesjonsplikt).

### 4. Når må man gjennomføre en DPIA? (s. 2)
**Art. 35 nr. 1** (gjengitt): Dersom det er sannsynlig at en type behandling, særlig ved bruk av ny teknologi og idet det tas hensyn til behandlingens art, omfang, formål og sammenheng, vil medføre en høy risiko for fysiske personers rettigheter og friheter, skal den behandlingsansvarlige *før* behandlingen foreta en DPIA.

Datatilsynet har plikt til å utarbeide og offentliggjøre en liste over behandlingsaktiviteter som krever DPIA. Aktivitetene på listen krever **alltid** DPIA (s. 2).

**To-trinns sjekk (s. 2):**
1. Sjekk om behandlingen står på Datatilsynets liste over behandlingsaktiviteter som alltid krever vurdering.
2. Hvis ikke: vurder om behandlingen vil medføre høy risiko for fysiske personers rettigheter og friheter.

Er DPIA gjennomført og risikoen endrer seg underveis, må den behandlingsansvarlige vurdere om behandlingen fremdeles er i tråd med vurderingen (s. 2).

**Art. 35 nr. 3 – eksempler i forordningen** (s. 2): a) systematisk og omfattende vurdering av personlige aspekter basert på automatisert behandling, herunder profilering, som danner grunnlag for avgjørelser med rettsvirkning eller tilsvarende betydelig påvirkning; b) behandling i stor skala av særlige kategorier (art. 9 nr. 1) eller opplysninger om straffedommer og lovovertredelser (art. 10); c) systematisk overvåking i stor skala av et offentlig tilgjengelig område. Listen er ikke uttømmende.

**Ved tvil anbefaler Datatilsynet å gjennomføre DPIA**, fordi det er et nyttig verktøy for å sikre etterlevelse (s. 2).

#### Datatilsynets liste over behandlingsaktiviteter som alltid krever DPIA (s. 2)
(* = «i følge med minst ett annet kriterium» fra WP29-kriteriene; kriteriene i parentes er slik de står i listen.)

| # | Behandlingsaktivitet | Eksempel / kriterier |
|---|---|---|
| 1 | Personopplysninger samlet inn via en tredjepart i følge med minst ett annet kriterium* | Innsamling og sammenstilling av personopplysninger fra tredjeparter for å avgjøre om den registrerte skal få tilbud om, fortsette å motta, eller nektes et produkt, en tjeneste eller et tilbud. (Sårbare registrerte og evaluering/poengsetting) |
| 2 | Behandling av biometriske opplysninger for å identifisere enkeltpersoner i følge med minst ett annet kriterium* | Biometri for identifisering i stor skala. (Særlige kategorier eller svært personlige opplysninger og stor skala) |
| 3 | Behandling av genetiske opplysninger i følge med minst ett annet kriterium* | Genetiske opplysninger i stor skala, inkl. gensekvensering. (Særlige kategorier eller svært personlige opplysninger og stor skala) |
| 4 | Behandling av personopplysninger med innovativ teknologi i følge med minst ett annet kriterium* | Helseopplysninger med innovativ velferdsteknologi som helseimplantater. (Innovativ bruk og særlige kategorier) |
| 5 | Behandling for systematisk monitorering av ansatte | Overvåking av ansattes internettaktivitet, elektronisk kommunikasjon og kameraovervåking. (Sårbare registrerte og systematisk monitorering) |
| 6 | Behandling uten samtykke for vitenskapelige eller historiske formål i følge med minst ett annet kriterium* | Helseopplysninger for forskningsformål uten samtykke. (Evaluering og særlige kategorier eller svært personlige opplysninger) |
| 7 | Behandling av lokasjonsdata i følge med minst ett annet kriterium* | Systematisk sammenstilling av lokasjons- og trafikkdata fra teleoperatører, eller behandling av opplysninger om abonnentens bruk av telenettet/teleoperatørens tjenester. (Svært personlige opplysninger og systematisk monitorering) |
| 8 | Behandling for å evaluere læring, mestring og trivsel i skoler eller barnehager | Inkluderer alle utdanningsnivåer: barne- og ungdomsskole, videregående og høyere utdanning. (Sårbare registrerte og systematisk monitorering) |
| 9 | Systematisk monitorering, inkludert kameraovervåking, på offentlig tilgjengelige områder i stor skala | (Systematisk monitorering og stor skala) |
| 10 | Kameraovervåking i skoler og barnehager i åpningstider | (Systematisk monitorering og sårbare registrerte) |
| 11 | Behandling av særlige kategorier eller svært personlige opplysninger i stor skala for algoritmetrening | – |
| 12 | Systematisk monitorering av effektivitet, ferdigheter, kunnskap, mental helse og utvikling | (Svært personlige opplysninger og systematisk monitorering) |
| 13 | Behandling der formålet er å tilby en tjeneste eller utvikle produkter for kommersiell bruk som involverer å forutsi jobbprestasjoner, økonomi, helse, personlige preferanser eller interesser, pålitelighet, adferd, lokasjon eller bevegelsesmønster | (Særlige kategorier eller svært personlige opplysninger og evaluering/poengsetting) |
| 14 | Innsamling av personopplysninger i stor skala gjennom «tingenes internett» eller velferdsteknologi | (Stor skala og særlige kategorier eller svært personlige opplysninger) |

Listen er godkjent av Det europeiske personvernrådet (EDPB). Engelsk versjon: dpialist280119.pdf (se [K20](K20-dt-dpia-liste.md)) (s. 2).

### 5. Når kreves det ikke DPIA? (s. 2)
- Behandlingen vil sannsynligvis ikke «medføre en høy risiko».
- Behandlingens art, omfang, sammenheng og formål er svært lik en behandling som allerede har en DPIA – resultatet fra den foreliggende vurderingen kan brukes.
- Behandlingen er kontrollert av en tilsynsmyndighet før mai 2018 på særskilte betingelser som ikke har endret seg (i Norge vanligvis = man har hatt konsesjon).
- Behandlingen er i samsvar med art. 6 nr. 1 bokstav c eller e **og** har rettsgrunnlag i EU-rett eller nasjonal lov som regulerer den spesifikke behandlingen, og en DPIA allerede er gjennomført som ledd i utarbeidelsen av rettsgrunnlaget (art. 35 nr. 10) – med mindre medlemsstaten har bestemt at DPIA er nødvendig før behandlingen.

**Prop. 56 LS (2017–2018) kap. 16.5.5** (sitert, s. 2): Departementet mener unntaket i art. 35 nr. 10 er så snevert at det ikke trengs nasjonale unntak fra unntaket; det kommer bare til anvendelse når det supplerende rettsgrunnlaget inneholder en spesifikk regulering av behandlingsaktivitetene, «noe som sjelden er tilfelle». Departementet foreslo ingen utvidet plikt til forhåndsdrøfting etter art. 36 nr. 5, men en forskriftshjemmel (lovforslaget § 14).

### 6. DPIA skal gjennomføres før behandlingen starter (s. 2–3)
- I samsvar med innebygd personvern og personvern som standard (art. 25, fortalepunkt 78). Vurderingen skal være et verktøy i beslutningsprosesser.
- Bør starte **så tidlig som mulig** i utformingen, selv om enkelte elementer ennå er ukjente. Oppdatering gjennom prosjektets livssyklus. Enkelte steg kan måtte gjentas i utviklingsprosessen fordi valg av tekniske/organisatoriske tiltak kan påvirke alvorlighetsgrad eller sannsynlighet for ny risiko. DPIA skal være en **kontinuerlig prosess**, særlig når behandlingen er dynamisk (s. 3).

### 7. Behandlingsansvarlig har ansvaret (s. 3)
- Den behandlingsansvarlige skal sikre at DPIA gjennomføres (art. 35 nr. 2). Den kan utføres av andre (internt/eksternt), men øverste ansvar ligger hos behandlingsansvarlig. Art. 24 nr. 1 gjengis.

**Personer som må kobles på (s. 3):**
1. **Personvernombudet** (om utpekt): behandlingsansvarlig må rådføre seg med PVO. PVOs råd og beslutningene som tas bør dokumenteres i vurderingen. PVO skal også kontrollere gjennomføringen (art. 39 nr. 1 bokstav c).
2. **Databehandler**: bør bistå og fremlegge all nødvendig informasjon (art. 28 nr. 3 bokstav f). Roller og ansvar nedfelles i avtale; avtalen bør også si at databehandleren blant annet skal bistå i DPIA.
3. **De registrerte eller deres representanter**: synspunkter innhentes «dersom det er relevant» (art. 35 nr. 9). Datatilsynet anbefaler dette.
   - i) Kan innhentes på ulike måter (generell studie, spørsmål til medarbeiderrepresentanter, spørreskjema til fremtidige kunder). Behandlingsansvarlig må ha rettslig grunnlag for å behandle personopplysninger som fremkommer. **Et samtykke til behandling regnes ikke som en tilbakemelding fra de registrerte.**
   - ii) Hvis endelige beslutninger avviker fra de registrertes synspunkter, skal begrunnelsen dokumenteres.
   - iii) Beslutning om **ikke** å innhente synspunkter skal også begrunnes og dokumenteres (f.eks. forretningssensitiv informasjon, uforholdsmessig eller umulig).

**God praksis – andre roller (s. 3):**
- Spesifikke avdelinger som foreslår DPIA bør bidra med informasjon og delta i evalueringen.
- Uavhengige eksperter fra ulike yrkesgrupper (jurister, IT-eksperter, sikkerhetseksperter, sosiologer, etikkspesialister osv.) ved behov.
- Informasjonssikkerhetsansvarlig og PVO kan foreslå DPIA, bistå med metodikk, evaluere kvaliteten på risikovurderingen og om restrisikoen er akseptabel, og utvikle kunnskap spesifikk for virksomheten.
- Informasjonssikkerhetsansvarlig og/eller IT-avdelingen bør bistå og kan foreslå DPIA ut fra sikkerhets- eller operative behov.

### 8. Hva kan en DPIA omfatte? (s. 3)
- **Flere behandlinger/prosjekter:** en DPIA kan omfatte flere lignende behandlingsaktiviteter med tilsvarende høye risikoer (art. 35 nr. 1). Fortalepunkt 92: kan utvides til mer enn ett prosjekt, f.eks. felles applikasjon/plattform for flere myndigheter eller på tvers av en industrisektor.
- **Gjenbruk for lignende behandlinger** (art, omfang, sammenheng, formål og risiko). Ikke nødvendig å utføre DPIA for situasjoner som allerede er undersøkt (samme teknologi, samme type opplysninger, samme formål).
  - Eksempler: en gruppe kommuner som hver innfører lignende kameraovervåkingssystem kan utføre én DPIA; et jernbaneselskap kan gjøre én DPIA for kameraovervåking på samtlige togstasjoner.
  - Når ulike behandlingsansvarlige bruker samme vurdering: en referansevurdering bør deles eller gjøres offentlig; tiltakene skal implementeres, og det skal begrunnes hvorfor kun én vurdering er gjort.
- **Felles behandlingsansvar:** pliktene skal defineres spesifikt; DPIA skal vise hvem som er ansvarlig for hvilke tiltak. Hver bør dele nyttig informasjon uten å røpe forretningshemmeligheter, immaterielle rettigheter eller sårbarheter.
- **Tekniske produkter** (maskin-/programvare): nyttig å vurdere i forbindelse med utvikling. Den som bruker produktet må fortsatt utføre egen DPIA for den konkrete behandlingen, men kan støtte seg på leverandørens DPIA. Eksempel: produsent av smarte strømmålere og energileverandører.

### 9. Behandlinger som allerede er i gang (s. 3–4)
- Ikke krav om DPIA for behandlinger som tidligere er kontrollert av Datatilsynet eller PVO og som ikke har endret seg. Fortalepunkt 171: beslutninger/godkjenninger etter direktiv 95/46/EF gjelder til de endres, erstattes eller oppheves.
- Har behandlingen endret seg (omfang, formål, innsamlede opplysninger, behandlingsansvarliges/mottakeres identitet, lagringstid, tekniske og organisatoriske tiltak osv.) siden forutgående kontroll, og vil sannsynligvis gi høy risiko → DPIA.
- **Endringer i risiko:** DPIA kan kreves ved endringer i risiko (ny teknologi, nytt formål). Revisjon av DPIA fremmer kontinuerlige forbedringer. Motsatt kan endringer minske risiko (f.eks. beslutninger ikke lenger automatisert, overvåking ikke lenger systematisk) – da kan DPIA-behovet falle bort.
- **Organisatoriske eller sosiale endringer** (s. 4): f.eks. at effektene av automatiske beslutninger får økt betydning, eller nye kategorier registrerte blir sårbare for forskjellsbehandling, kan kreve ny DPIA.

### 10. Risiko og risikovurdering (s. 5)
- Plikten til DPIA forstås på bakgrunn av den generelle forpliktelsen til hensiktsmessig håndtering av risiko.
- «Risiko» = et scenario som beskriver en hendelse og dens estimerte konsekvenser basert på alvorlighet og sannsynlighet. Risikohåndtering = samordnede aktiviteter for å styre og kontrollere en virksomhet basert på risiko.
- Digdirs definisjon gjengis: risiko er knyttet til mulige avvik fra mål; kombinasjon av (mulige) konsekvenser og (tilhørende) sannsynligheter (se [K17](K17-digdir-gjennomfore-risikovurdering.md)).
- «Rettigheter og friheter» = de registrertes rettigheter etter art. 12–22 og andre grunnleggende friheter (privatliv, kommunikasjonsvern, personvern, ytringsfrihet, religionsfrihet, organisasjonsfrihet, ikke-diskriminering) etter bl.a. EMK, SP og ØSK. Prinsippene i art. 5 bør også være oppfylt.

**Sikkerhetsrisiko (art. 32) vs. personvernkonsekvenser (art. 35)** (s. 5):
- Art. 24, 25, 32 og 35 stiller krav om risikovurderinger; felles er en verdivurdering og en trusselvurdering knyttet til personopplysningene og de registrertes rettigheter og friheter.
- **Art. 32 – personopplysningssikkerhet:** skal *alltid* gjennomføres før alle behandlinger og oppdateres regelmessig og ved endringer; identifisere områder som kan gi utilsiktet eller uautorisert tilgang, endring, sletting, tap eller utlevering.
- **Art. 35 – personvernkonsekvenser:** for behandlinger som sannsynligvis gir høy risiko. Sikkerhetstiltak vil ikke nødvendigvis redusere faren for krenkelse; den behandlingsansvarlige må i stedet finne tiltak ved å endre *hvordan* behandlingen utføres og hvordan rettighetene ivaretas. Datatilsynet anbefaler å ta **den registrertes perspektiv**.

**Den registrertes perspektiv – fire mål** (s. 5):
1. **Medbestemmelse** – reell innflytelse. Eksempler: særskilt spesifisering av samtykke, regelmessig fornying av samtykke, nytt samtykke fra barn når de når samtykkealder, tilrettelagt innsynsløsning med redigering, sletting og tilbaketrekking av samtykke; reell reservasjonsmulighet når grunnlaget er art. 6 f.
2. **Åpenhet** – informasjon og innsyn. Eksempler: regelmessig informasjon, særskilt varsel før overføring fra et register til et annet, innsynsløsning med oversikt over utleveringer, tegninger av dataflyt, dataportabilitet, lav terskel for å informere om sikkerhetsavvik, informasjon om tiltak, programvare og algoritmer.
3. **Forutsigbarhet** – mindre kompleks behandling. Eksempler: spesifisering av formål, klare kriterier for utvalg til forskning, klare begrensninger for kobling mellom registre, færre variabler, kortere lagringstid.
4. **Tillit** – ved å demonstrere at medbestemmelse, åpenhet og forutsigbarhet er reelle mål og bruke ressurser på dette.

**Risiko må vurderes kontinuerlig** (s. 5): DPIA er ikke obligatorisk for hver behandling, men den generelle plikten til risikohåndtering består; behandlingsansvarlige må kontinuerlig vurdere risiko for å identifisere når høy risiko sannsynligvis foreligger.

### 11. Prosessflyt (figur, s. 6)
Sannsynlig høy risiko (art. 35 nr. 1, 3, 4)? NEI → ikke krav om DPIA. JA → Unntak (art. 35 nr. 5, 10)? JA → ikke krav om DPIA. NEI → DPIA (art. 35 nr. 7), med innspill fra: råd fra PVO (art. 35 nr. 2), PVO kontrollerer gjennomføringen (art. 39 nr. 1 c); atferdsnormer (art. 35 nr. 8); synspunkter fra de registrerte (art. 35 nr. 9). Revidering ved behov (art. 35 nr. 11). Deretter: høy restrisiko (art. 36 nr. 1)? NEI → ingen forhåndsdrøftelse; JA → forhåndsdrøftelse.

### 12. Hva skal vurderes? (s. 6)
Risiko = konsekvensen av at rettigheter og friheter ikke ivaretas × sannsynligheten (kvantifisering av usikkerhet). Ikke-uttømmende liste – konsekvens av og sannsynlighet for at:
- personopplysninger behandles uten rettslig grunnlag
- personopplysninger behandles på en ikke rettferdig måte
- det ikke er tilstrekkelig åpenhet rundt behandlingen
- det samles inn mer enn nødvendig for formålet
- opplysningene ikke er korrekte
- opplysninger lagres lenger enn nødvendig
- den registrerte ikke får tilstrekkelig informasjon til et informert valg
- den registrerte ikke får innsyn
- den registrerte ikke får korrigert eller slettet opplysninger
- det ikke er lagt til rette for dataportabilitet
- rettigheter ikke ivaretas ved profilering
- behandlingen kan resultere i diskriminering
- behandlingen begrenser ytringsfrihet og religionsfrihet

Konsekvensen kan være fysisk, materiell og ikke-materiell skade. Eksempler fra fortalepunkt 75: forskjellsbehandling; identitetstyveri eller -bedrageri; økonomisk tap; skade på omdømme; tap av fortrolighet for taushetsbelagte opplysninger; uautorisert oppheving av pseudonymisering; andre økonomiske eller sosiale ulemper.

### 13. Når er det «høy risiko»? (s. 7–9)
- Enhver behandling innebærer en viss risiko; plikten gjelder bare når risikoen er «høy», dvs. konsekvens og sannsynlighet for avvik vurderes som **større enn normalt** (s. 7).
- Fortalepunkt 76: objektiv vurdering ut fra art, omfang, formål og sammenheng.

**Fire vurderingsmomenter** (s. 7):
1. **Behandlingens art** – iboende karakteristikk. Spørsmål: Gjør behandlingen det lett eller vanskelig å utøve rettigheter? Preges den av uforutsigbarhet og lite åpenhet? Er det usikkerhet om prinsippene i art. 5 ivaretas?
   - *Systematisk behandling* (WP29): skjer i henhold til et system; er forhåndsarrangert (planlagt) organisatorisk eller metodisk; skjer som følge av en plan om å samle inn personopplysninger; skjer som del av en strategi. Særskilt inngripende fordi den er kontinuerlig, lite forutsigbar, og det kan være umulig å unngå registrering (f.eks. Oslo S, Oslo lufthavn).
   - *Kategorier*: art. 9, art. 10, elektronisk kommunikasjon, lokasjonsdata, privatøkonomi, «life-logging applications» → momenter for høy risiko.
   - *Skjev maktbalanse*: ikke enkelt for den registrerte å samtykke, protestere eller utøve rettigheter.
   - *Ny teknologi* eller ny bruk av eksisterende teknologi som ikke er vurdert.
2. **Behandlingens omfang** – «stor skala» (fortalepunkt 91: betydelig mengde opplysninger som kan påvirke et stort antall registrerte). WP29-faktorer: antall registrerte (tall eller prosentandel); datavolum (antall variabler, detaljeringsgrad); lagringstid (kort, tidsavgrenset, permanent); geografisk omfang (lokalt, regionalt, nasjonalt, internasjonalt, globalt).
3. **Behandlingens formål** – inngripende formål: kontrollformål (skatt, NAV, toll, politi, forsikring); avgjørelser om enkeltpersoner basert på systematisk og omfattende analyse av personlige aspekter; beslutninger som får betydning for den registrerte.
4. **Sammenhengen (kontekst)** – høy risiko der den registrerte har klar forventning om personvern: forventning om konfidensialitet (helse, velferd, arbeidsforhold); forventning om privatliv (hjemmet, rekreasjon); sammenstilling av datasett innsamlet for ulike formål av ulike behandlingsansvarlige.

Etter å ha beskrevet de fire sidene: vurder om iboende risikoelementer reduseres av iverksatte tiltak (s. 7).

#### Artikkel 29-gruppens ni kriterier (s. 7–8)
1. **Evaluering eller poengsetting** – inkl. profilering og forutsigelse, særlig «aspekter som gjelder arbeidsprestasjoner, økonomisk situasjon, helse, personlige preferanser eller interesser, pålitelighet eller atferd, plassering eller bevegelser» (fortalepunkt 71 og 91).
2. **Automatiske beslutninger med rettslig eller tilsvarende betydelig virkning** (art. 35 nr. 3 a).
3. **Systematisk monitorering** – observere, overvåke eller kontrollere de registrerte, inkl. opplysninger samlet gjennom nettverk eller «systematisk overvåking i stor skala av et offentlig tilgjengelig område» (art. 35 nr. 3 c).
4. **Særlige kategorier eller opplysninger av svært personlig karakter** – art. 9 og art. 10.
5. **Personopplysninger behandles i stor skala** – vurder: a) antall registrerte (antall eller andel av populasjonen); b) mengde og/eller spennvidde av opplysninger; c) varighet eller regelmessighet; d) geografisk omfang.
6. **Matching eller sammenstilling av datasett** – fra to eller flere operasjoner med ulike formål og/eller ulike behandlingsansvarlige, utover den registrertes rimelige forventninger.
7. **Personopplysninger om sårbare registrerte** – skjev maktbalanse; barn, arbeidstakere, mer sårbare grupper (psykisk syke, asylsøkere, eldre, pasienter osv.) og ubalanse i forholdet generelt.
8. **Innovativ bruk eller anvendelse av ny teknologisk eller organisatorisk løsning** – f.eks. fingeravtrykk + ansiktsgjenkjenning for adgangskontroll; «tingenes internett» (art. 35 nr. 1, fortalepunkt 89 og 91).
9. **Når behandlingen «hindrer de registrerte i å utøve en rettighet eller gjøre bruk av en tjeneste eller en avtale»** (art. 22, fortalepunkt 91) – f.eks. bank som kredittvurderer kunder mot en database for å avgjøre lån.

**Tommelfingerregel (s. 8):** I de fleste tilfeller kan man anta at DPIA skal gjøres dersom **to** av kriteriene er oppfylt. Jo flere kriterier, desto mer sannsynlig høy risiko – uavhengig av planlagte tiltak. En behandling som bare oppfyller **ett** kriterium kan likevel i gitte tilfeller kreve DPIA.

**Eksempeltabell (s. 8):**

| Eksempel på behandling | Mulige relevante kriterier | DPIA sannsynlig påkrevd? |
|---|---|---|
| Sykehus – pasienters genetiske data og annen pasientdata (journalsystem) | Særlige kategorier/svært personlig; sårbare registrerte; omfattende behandling | JA |
| Kamerasystem for å overvåke kjøreatferd på motorveier med intelligent videoanalyse og automatisk gjenkjenning av bilskilt | Systematisk monitorering; innovativ bruk av teknologi | JA |
| Virksomhet som systematisk overvåker ansattes aktiviteter (arbeidsplass, internettaktivitet osv.) | Systematisk monitorering; sårbare registrerte | JA |
| Innsamling fra offentlige sosiale medier for å generere profiler | Vurdering/bedømmelse; omfattende behandling; matching/kombinering av datasett; sensitive/svært personlige opplysninger | JA |
| Institusjon som oppretter database for kredittvurdering eller svik på nasjonalt plan | Vurdering/bedømmelse; automatisk beslutning med rettslig/betydelig virkning; hindrer utøvelse av rettighet/tjeneste/avtale; sensitive/svært personlige | JA |
| Lagring for arkivering av pseudonymiserte personfølsomme data om sårbare registrerte i forskningsprosjekter/kliniske forsøk | Sensitive opplysninger; sårbare registrerte; hindrer utøvelse av rettighet | JA |
| Leges, helsepersonells eller advokats behandling av opplysninger om pasienter/klienter | Sensitive/svært personlige; sårbare registrerte | NEI |
| Nettmagasin som bruker e-postliste til generisk daglig oversikt | Omfattende behandling | NEI |
| Nettbutikk for veteranbildeler med begrenset profilering basert på hva besøkende har sett/kjøpt | Vurdering eller bedømmelse | NEI |

Hvis behandlingen svarer til «JA»-situasjonene, men behandlingsansvarlig likevel mener høy risiko ikke er sannsynlig, bør det **begrunnes og dokumenteres** hvorfor DPIA ikke gjennomføres, og PVOs synspunkter noteres (s. 9).

**Protokoll (s. 9):** Protokollen etter art. 30 nr. 1 (formål, kategorier, mottakere, og om mulig generell beskrivelse av sikkerhetstiltak etter art. 32 nr. 1) er grunnlaget for å avgjøre om høy risiko er sannsynlig – også når konklusjonen er at DPIA ikke skal gjennomføres. Se [K04](K04-dt-fore-protokoll.md).

### 14. Hvordan gjennomføre en DPIA? (s. 10)
**Minimumsinnhold (art. 35 nr. 7):**
- a) systematisk beskrivelse av planlagte behandlingsaktiviteter og formålene
- b) vurdering av om behandlingsaktivitetene er nødvendige og står i rimelig forhold til formålene
- c) vurdering av risikoene for de registrertes rettigheter og friheter
- d) planlagte tiltak for å håndtere risikoene og påvise at forordningen overholdes

I tillegg (ansvarlighet): bedømme, evaluere og eventuelt godkjenne – her har **ledelsen eller styret** den viktigste rollen; arbeidet sammenstilles og funn presenteres for ledelsen.

**Figur – fire faser (s. 10):** «Plikter for alle»: (1) Systematisk beskrivelse av behandlingen (art, omfang, formål, sammenheng; kilder og mottakere; informasjonssikkerhet; ansvarsforhold) og (2) Nødvendighet og proporsjonalitet (personvernprinsipper, rettslig grunnlag, rettigheter, friheter). «Tilleggsplikter for DPIA»: (3) Risiko for de registrertes rettigheter og friheter (åpenhet, forutsigbarhet, medbestemmelse, tillit) og (4) Ledelsens validering av DPIA (sammenstilling og presentasjon av funn, hensynet til interessenter, gjennomgang, beslutning og godkjenning). Detaljert sjekkliste: [K21](K21-dt-sjekkliste-dpia-faser.md).

- **Atferdsnormer, sertifiseringer m.m.:** etterlevelse av atferdsnorm (bransjenorm) skal tas i betraktning (art. 35 nr. 8). Sertifiseringer, segl og merker, og bindende virksomhetsregler (BCR), bør også tas i betraktning.
- **Allmenn ramme / skalerbarhet:** kravene utgjør en bred ramme; også mindre virksomheter kan gjennomføre en tilpasset DPIA. I risikostyringsterminologi: 1) **Fastslå sammenheng**; 2) **Vurdere risikoene** (sannsynlighet og alvorlighetsgrad); 3) **Håndtere risikoene** («begrense risikoen», «sikre vern av personopplysningene», «påvise at denne forordning overholdes»).
- **Fleksibilitet:** struktur og form kan fastsettes fritt (jf. fortalepunkt 90), men DPIA må uansett være en reell risikovurdering som muliggjør tiltak.
- **Sektorspesifikke rammeverk** oppmuntres av WP29.

### 15. Offentliggjøring (s. 10)
- Ikke rettslig krav, men behandlingsansvarlig bør som minimum **overveie å offentliggjøre deler** av DPIA. Særlig god praksis når offentligheten er berørt, f.eks. offentlig myndighet.
- Offentlig versjon kan være oppsummering av hovedfunn eller en uttalelse om at DPIA er gjennomført (unngå sikkerhetsdetaljer/forretningshemmeligheter).
- Komplett DPIA skal formidles Datatilsynet ved forhåndsdrøftelse eller på anmodning. Ved forhåndsdrøftelse skal hele vurderingen legges frem (art. 36 nr. 3 e); Datatilsynet vil ikke avsløre forretningshemmeligheter eller sikkerhetssvakheter.

### 16. Forhåndsdrøftelse med Datatilsynet (art. 36) (s. 11–12)
- Nødvendig når DPIA er gjennomført og behandlingen **fortsatt medfører høy risiko**.
- Skriftlig, formalisert prosess; saksbehandling etter forvaltningsloven og offentleglova, i praksis likt tidligere konsesjonsbehandling. Datatilsynet vurderer lovlighet og om prinsippene ivaretas, og gir skriftlig tilbakemelding med råd eller pålegg.
- Datatilsynet vurderer som minimum: om behandlingen er i tråd med forordningen; om risikoen er tilstrekkelig identifisert; om risikoen er tilstrekkelig redusert.

**Rekkefølge (s. 11):**
1. Gjennomføre DPIA (og oppfylle plikter knyttet til internkontroll).
2. Iverksette risikoreduserende tiltak – når høy risiko er redusert, kan behandlingen starte.
3. Be om forhåndsdrøftelse dersom: det er gjennomført DPIA og man ikke klarer å redusere risiko; eller vurderingen er behandlet i ledergruppen mer enn én gang, risikoen fremdeles er høy og viljen til å gjennomføre fremdeles er stor.

- Behandlinger som tidligere krevde konsesjon vil mest sannsynlig kreve DPIA.
- Hovedkontor i et annet land → Datatilsynet vurderer samarbeid med tilsynsmyndigheten der.
- Ønske om veiledning/diskusjon kvalifiserer **ikke** som forhåndsdrøftelse – be om veiledningsmøte.
- Uansett: plikt til å dokumentere, oppbevare og ved behov oppdatere DPIA.

**Hva må sendes inn (s. 11):**
1. Navn, telefon og e-post til kontaktperson og PVO hos behandlingsansvarlig, og til databehandler hvis aktuelt.
2. Systematisk beskrivelse med fokus på hva som gir høy risiko: art, omfang, formål og sammenheng; kilder, mottakere, risikovurderinger, informasjonssikkerhet og ansvarsforhold.
3. Vurdering av nødvendighet og proporsjonalitet: dokumentasjon av tiltak og garantier for personvernprinsippene, rettigheter og friheter (f.eks. informasjonstiltak, innsynsløsninger, granulering av samtykke).
4. Vurdering av risiko for rettigheter og friheter: dokumentasjon fra DPIA etter art. 35; risikovurdering i forhold til medbestemmelse, åpenhet og forutsigbarhet; tiltak – gjennomførte tiltak, vurderte men ikke gjennomførte tiltak, og begrunnelse for hvorfor tiltak ikke er gjennomført.
5. Dokumentasjon fra ledelsens validering: sammenstilling av presentasjon og funn; dokumentasjon av hensynet til interessenter; ledelsens gjennomgang og beslutning.
I tillegg bør andre relevante forhold vurderes vedlagt (f.eks. ledelsens beslutning om å be om forhåndsdrøftelse).

**Sikker sending (s. 11):** Skriftlig via e-post eller brev. E-postserveren støtter TLS; PGP-kryptering kan brukes ved behov for høyere sikkerhet.

**Mulige utfall (s. 11):** Datatilsynet kan bruke alle virkemidler og sanksjonsmuligheter: 1) be om ytterligere informasjon (f.eks. sikring, innebygd personvern); 2) gi skriftlige råd, og bruke myndighet til pålegg, advarsler, irettesettelser, stedlig tilsyn eller forbud mot behandling.

**Eksempler (s. 11–12):**
1. *Langvarige forskningsprosjekter med helseopplysninger i stort omfang uten samtykke:* forventer dokumenterte tiltak som reelt gir de registrerte kjennskap til prosjektet og enkelt innsyn i hvilke opplysninger som er innhentet fra hvor; reservasjonsmulighet reduserer også risiko. Bruker virksomheten ressurser på tiltak som reelt sikrer forutsigbarhet, åpenhet og medbestemmelse → ikke nødvendig med forhåndsdrøftelse. Velger den å ikke gjøre det og har en legitim begrunnelse → forhåndsdrøftelse nødvendig.
2. *Teletilbyder som vil bruke lokasjonsopplysninger til andre formål (videresalg av antall personer og nasjonaliteter ved severdigheter, f.eks. Gaustatoppen i påsken), grunnlag art. 6 f:* forventer tiltak for lagringsbegrensning (hvor lang tid anonymisering tar, og hvor lenge identifiserende opplysninger lagres) og dataminimering (unngå direkte identifiserende opplysninger; grupper under et visst antall registreres ikke); der relevant: enkel kjennskap til salget, innsyn i hva som er brukt/utlevert, og reservasjonsmulighet. Samme konklusjon som eksempel 1.

### 17. Eksisterende rammeverk (s. 13)
Forordningen foreskriver ikke prosedyre; rammeverk må dekke minimumskravene. Eksempler:
- Generelle: Tyskland – Standard Data Protection Model V.1.0 (2016) ([K37](K37-sdm-standard-datavernmodell.md)); Spania – AEPD «Guía para una Evaluación de Impacto en la Protección de Datos Personales (EIPD)» (2014); Frankrike – CNIL PIA (2015) ([K28](K28-cnil-pia-metode.md)–[K30](K30-cnil-pia-kunnskapsbaser.md)).
- Sektorspesifikt: DPIA Template for Smart Grid and Smart Metering Systems (EU-kommisjonen).
- Internasjonal standard: ISO/IEC 29134.
- Annet: «A Process for Data Protection Impact Assessment under the European General Data Protection Regulation» (Friedewald m.fl., 2016) ([K40](K40-dpia-prosess-uld.md)); IAPP-rammeverk (krever medlemskap).

## Praktiske sjekkpunkter
- Kontroller først om behandlingen står på Datatilsynets DPIA-liste (14 punkter); hvis ja, er DPIA obligatorisk.
- Hvis ikke på listen: gå gjennom de ni WP29-kriteriene. To eller flere treff → anta DPIA-plikt. Ett treff → vurder konkret.
- Ved tvil: gjennomfør DPIA (Datatilsynets anbefaling).
- Hvis DPIA ikke gjennomføres til tross for treff på kriterier: dokumenter begrunnelsen og PVOs synspunkter.
- Kontroller at behandlingen er lovlig (art. 5, 6, 9) *før* DPIA – DPIA reparerer ikke ulovlig behandling.
- Start DPIA før behandlingen og tidlig i design; oppdater ved endringer i teknologi, formål, mottakere, lagringstid, kontekst eller sårbarhet.
- Sørg for at PVO er rådspurt og at rådene er dokumentert; at databehandleravtalen forplikter databehandler til å bistå med DPIA (art. 28 nr. 3 f); at de registrertes synspunkter er innhentet, eller at begrunnelsen for å la være er dokumentert.
- Kontroller at DPIA inneholder alle fire elementer i art. 35 nr. 7 (a–d) og en ledelsesvalidering.
- Vurder risiko fra den registrertes perspektiv (medbestemmelse, åpenhet, forutsigbarhet, tillit) – ikke bare sikkerhet.
- Bruk listen over 13 «hva skal vurderes»-punkter og skadeeksemplene i fortalepunkt 75.
- Ved felles behandlingsansvar: angi hvem som er ansvarlig for hvilke tiltak.
- Hvis høy restrisiko etter tiltak: forhåndsdrøftelse med Datatilsynet før oppstart (art. 36 nr. 1), med de fem dokumentasjonspunktene. Send kryptert ved behov.
- Vurder å publisere en sammenfatning av DPIA, særlig for offentlige virksomheter.

## Viktige sitater
- «En vurdering av personvernkonsekvenser er en prosess som skal beskrive behandlingen av personopplysninger, og vurdere om den er nødvendig og proporsjonal.» (s. 1)
- «Å gjennomføre en DPIA reparerer ikke en ulovlig behandling av personopplysninger.» (s. 1)
- «Aktivitetene på denne lista krever alltid en vurdering av personvernkonsekvenser» (s. 2)
- «I de tilfellene der det er usikkert om det er nødvendig å gjennomføre en vurdering av personvernkonsekvenser eller ikke, anbefaler vi at det gjøres» (s. 2)
- «Husk at et samtykke til behandling ikke regnes som en tilbakemelding fra de registrerte.» (s. 3)
- «I de fleste situasjoner kan en behandlingsansvarlig anta at det skal gjøres en vurdering av personvernkonsekvenser dersom to av disse kriteriene er oppfylt.» (s. 8)
- «Sikkerhetstiltak vil ikke nødvendigvis redusere denne faren og en behandlingsansvarlig må i stedet finne risikoreduserende tiltak ved å endre på hvordan behandlingen skal utføres» (s. 5)
- «Dersom dere ønsker veiledning, innspill eller diskusjon rundt om dere tenker riktig eller gjør nødvendige vurderinger, vil det ikke kvalifisere til en forhåndsdrøftelse.» (s. 11)

## Kryssreferanser
- GDPR: art. 5, 6, 9, 10, 12–22, 24, 25, 28 nr. 3 f, 30 nr. 1, 32, 35 (nr. 1, 2, 3, 4, 5, 7, 8, 9, 10, 11), 36 (nr. 1, 3 e, 5), 39 nr. 1 c; fortalepunkt 71, 75, 76, 78, 89, 90, 91, 92, 171
- Popplyl. og Prop. 56 LS (2017–2018) kap. 16.5.5
- [K20](K20-dt-dpia-liste.md) – Datatilsynets DPIA-liste (engelsk PDF)
- [K21](K21-dt-sjekkliste-dpia-faser.md) – sjekkliste for de fire DPIA-fasene
- [K22](K22-dpia-eksempler.md) – eksempler
- [K24](K24-wp248-dpia.md) – WP248, kilden til de ni kriteriene
- [K13](K13-dt-innebygd-personvern.md) – innebygd personvern (art. 25)
- [K04](K04-dt-fore-protokoll.md) – protokoll (art. 30)
- [K17](K17-digdir-gjennomfore-risikovurdering.md) – Digdirs risikovurdering
- [K28](K28-cnil-pia-metode.md), [K29](K29-cnil-pia-maler.md), [K30](K30-cnil-pia-kunnskapsbaser.md) – CNIL PIA; [K37](K37-sdm-standard-datavernmodell.md) – SDM; [K40](K40-dpia-prosess-uld.md) – Friedewald-prosessen

## Aktualitet og begrensninger
- Utskriften (22.09.2026) viser ingen publiserings-/endringsdato; innholdet bygger på WP248 og omtaler overgangen fra konsesjonsregimet (før mai 2018).
- Norsk kontekst (konsesjon, Prop. 56 LS, forvaltningsloven/offentleglova).
- Lenker til eksterne rammeverk (AEPD 2014, CNIL 2015, SDM V1.0 2016) kan være utdaterte. **[Merknad – ikke fra kilden]** Nyere versjoner finnes av flere av disse (f.eks. SDM 3.x og oppdaterte CNIL PIA-veiledere); WP248 er videreført (endorsed) av EDPB.
- Bøtesatsen i veilederen (10 mill. euro / 2 %) gjelder brudd på art. 35/36 (jf. art. 83 nr. 4).

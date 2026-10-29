---
id: K13
tittel: "Innebygd personvern og personvern som standard"
utgiver: Datatilsynet
dato: "Udatert i utskriften (nettside skrevet ut 2026-09-22)"
spraak: nb
fil: "ressurser/Datatilsynet/Innebygd personvern og personvern som standard _ Datatilsynet.pdf"
url: "https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/innebygd-personvern-og-personvern-som-standard/"
type: veileder
gdpr_artikler: [5, 6, 12, 15, 20, 22, 24, 25, 28, 32, 35, 42, 58]
emner: [innebygd-personvern, personvern-som-standard, privacy-by-design, dataminimering, lagringsbegrensning, tilgangsstyring, anskaffelse, dark-patterns]
relevans: høy
---

# Innebygd personvern og personvern som standard (Datatilsynet)

## Sammendrag
Datatilsynets veileder (14 sider i utskrift) om GDPR art. 25 – innebygd personvern (data protection by design) og personvern som standardinnstilling (data protection by default). Den er basert på EDPBs Guidelines 4/2019 om art. 25 og forklarer hvem som er ansvarlig (behandlingsansvarlig, også ved bruk av tredjepartsløsninger og databehandlere), hva kravet innebærer (tekniske og organisatoriske tiltak og garantier, effektivitetskrav, vurderingsmomentene «state of the art», kostnader, art/omfang/formål/sammenheng og risiko), når det gjelder (før og under behandlingen, også for eldre systemer), hva personvern som standard krever (dataminimering i innsamling, omfang, lagringstid og tilgang), og gir for hvert personvernprinsipp en tabell med «nøkkelelementer» og illustrerende eksempler. Avsluttes med sertifisering og håndhevelse. Siden opplyser at en oppdatert veiledning om programvareutvikling med innebygd personvern er under arbeid.

## Når skal agenten bruke denne kilden
- Når en løsning, app, KI-modell eller et system skal anskaffes, utvikles eller konfigureres, og man trenger konkrete art. 25-krav.
- Kravspesifikasjon i anbud og kontrakter (inkl. databehandleravtaler) – krav om innebygd personvern til leverandører/databehandlere.
- DPIA/risikovurdering: tiltakskatalog per prinsipp (lovlighet, rettferdighet, åpenhet, formålsbegrensning, dataminimering, riktighet, lagringsbegrensning, integritet og konfidensialitet, ansvarlighet).
- Vurdere standardinnstillinger (forhåndsavkryssede bokser, obligatoriske skjemafelt, deaktivering av unødvendige funksjoner, synlighet/publisering).
- Gap-analyse av eldre systemer mot art. 25.
- Vurdere «dark patterns» og manipulerende design.

## Hovedinnhold

### 1. Innledning (s. 1)
- Innebygd personvern betyr at det tas hensyn til personvern i **alle utviklingsfaser** av et system eller en løsning, slik at systemene oppfyller personvernprinsippene og ivaretar de registrertes rettigheter.
- Art. 25: personvern skal bygges inn i behandlingsaktiviteter og være standardinnstilling.
- Datatilsynet har egen veiledning for programvareutviklere («Programvareutvikling med innebygd personvern»), men den er «ikke lenger tilstrekkelig for dagens behov» og oppdateres.
- Veiledningen er basert på EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default.
- **Historikk:** «Privacy by design» ble utviklet av personvernmyndighetene i Ontario, Canada på 1990-tallet; de syv prinsippene ble vedtatt på en internasjonal personvernkonferanse i 2010. Innebygd personvern ble først obligatorisk med GDPR. De syv stegene:
  1. Vær i forkant, forebygg fremfor å reparere
  2. Gjør personvern til standardinnstilling
  3. Bygg personvern inn i designet
  4. Skap full funksjonalitet
  5. Ivareta informasjonssikkerheten fra start til slutt
  6. Vis åpenhet
  7. Respekter brukerens personvern

### 2. Hvem er ansvarlig? (s. 2)
- **Behandlingsansvarlige** har det overordnede ansvaret – uansett størrelse – for at alle «midler» (system, mobilapp osv.) har innebygd personvern. «Middel» = den tekniske innretningen: løsningen, programmet, app-en, infrastrukturen, algoritmen osv.
- Forutsetning: grunnleggende forståelse av personvernprinsippene.
- Tips: styringssystemer for utvikling, anskaffelse og oppdatering av løsninger skal inneholde krav om innebygd personvern; sørg for tilstrekkelig personvernkompetanse.

**Tredjepartsløsninger og databehandlere (s. 2):**
- Behandlingsansvarlige må alltid vurdere om midlene faktisk har innebygd personvern, også ved produkter/tjenester utviklet av tredjeparter. Produsenter bør utvikle i tråd med kravene for at behandlingsansvarlige skal kunne bruke dem.
- Behandlingsansvarlige må stille krav om, vurdere og forvisse seg om at databehandlere oppfyller kravene, og evaluere med jevne mellomrom.
- Må ha kompetanse til å vurdere om tredjeparters/databehandleres midler har nødvendige garantier.
- Tips: still krav om innebygd personvern i **anbudskonkurranser og kontrakter**; sørg for tilstrekkelig **bestillerkompetanse**; velg databehandlere og produsenter som kan garantere innebygd personvern.

**Ansvarlighet og dokumentasjon (s. 2):**
- Behandlingsansvarlige skal kunne **demonstrere** at kravet er oppfylt – vise hvordan prinsippene og rettighetene er implementert effektivt, f.eks. hvordan tiltakene fører til godt personvern.
- Enhver behandling vurderes konkret; ved ferdige produkter må man kunne vise hvordan de ivaretar innebygd personvern.
- Tips: ta vare på vurderinger underveis (for revisjon/oppdatering); ta vare på risikoanalyser, DPIA-er, PVOs synspunkter, sikkerhetstester m.m.

### 3. Hva er innebygd personvern? (s. 3)
- Kravet omfatter å implementere **tilstrekkelige tekniske og organisatoriske tiltak og nødvendige garantier** slik at prinsippene og de registrertes rettigheter ivaretas **effektivt** i behandlingen.
- «Tilstrekkelig» = egnede og hensiktsmessige for å implementere personvernet effektivt. Tiltak kan være alt fra avansert kunstig intelligens til opplæring av ansatte.
- Tips: risikobasert tilnærming; bruk standarder, «best practices» og anerkjente atferdsnormer.

**Krav til effektivitet:** tiltak må ha **reell virkning** – prinsippene faktisk implementert, registrerte kan håndheve rettigheter, individets friheter ikke innskrenket. Effektivitet vurderes konkret per behandling. Virksomheten må kunne **påvise** at tiltakene er effektive. Tips: definer egne **nøkkeltallsindikatorer (KPI-er)** – kvantitative eller kvalitative – og evaluer mot dem; demonstrer effektivitet og vurder regelmessig om tiltakene fungerer og er oppdaterte.

**Momenter i vurderingen av tiltak** (ikke kriterier i seg selv, men del av samlet vurdering):
| Moment | Innhold (kilden) | Tips |
|---|---|---|
| «State of the art» | Dagens status i teknisk utvikling – dynamisk. Virksomheten må være oppdatert; tiltak (f.eks. konfidensialitet) kan svekkes over tid. Også organisatoriske tiltak (f.eks. opplæring mot dataangrep) må følge nye angrepsvektorer og trusler. | «Fremtidssikre» tiltak; vurder jevnlig teknisk utvikling; krev at produsenter og databehandlere holder virksomheten orientert og tiltak oppdatert |
| Gjennomføringskostnader | Alle ressurser (tid, penger, kompetanse); totalt kostnadsbilde (implementering, drift, opplæring, vedlikehold). Ikke mer enn nødvendig; enkle, billige tiltak kan være effektive; dyre tiltak garanterer ikke effekt. **Høye kostnader er ingen unnskyldning** for å unnlate effektive tiltak. | Få oversikt over totale kostnader; estimer og budsjetter for opplæring, oppdateringer, drift og vedlikehold |
| Behandlingens art, omfang, formål og sammenheng | Må også vurderes etter art. 24, 32 og 35; kartlegges fra start. **Art** = iboende karakteristikk (systematisk behandling, automatiserte avgjørelser, ny teknologi, skjevt maktforhold). **Omfang** = størrelse og rekkevidde (antall registrerte, datavolum, lagringstid, geografisk omfang). **Formål** = kontrollformål, avgjørelser av betydning for den registrerte. **Sammenheng** = forventninger (privatliv, konfidensialitet, deling). | – |
| Risiko og risikovurdering | Risikoer av varierende sannsynlighet og alvorlighet for rettigheter og friheter må hensyntas under hele behandlingen; virksomheten må ha oversikt over risiko knyttet til prinsippene og rettighetene. | Foreta løpende oppdaterte risikovurderinger. Forutsetter systematisk oversikt over behandlingen og vurdering av nødvendighet og proporsjonalitet |

### 4. Når må personvern bygges inn? (s. 4)
- **Før behandlingen:** idet man fastsetter midlene, ved anskaffelse, vurdering, utforming, valg og innstillinger av behandlingssystemer.
- **Etter oppstart – krav om vedlikehold:** sørge for at behandlingen fortsatt tilfredsstiller kravene; ha oversikt over hvor godt den ivaretar personvernet i praksis. Gjelder også ved bruk av databehandlere – vurder behandlingsaktivitetene med jevne mellomrom.
- **Eldre systemer:** kravet gjelder også systemer utviklet før GDPR (2018) som fortsatt er i bruk; plikt til å oppdatere og iverksette tiltak. Tips: gjør en **GAP-analyse** mot kravene; identifiser tiltak for krav som ikke er ivaretatt; foreta jevnlige vurderinger og oppdateringer.

### 5. Personvern som standard (s. 5)
- Alle behandlingsmidler skal ha standardinnstillinger som er **mest mulig personvernfremmende og minst mulig inngripende**. Som standard skal de registrerte kunne håndheve rettighetene effektivt, og bare nødvendige opplysninger i tråd med behandlingsgrunnlaget skal samles inn og behandles.
- **Eksempel – avkrysningsboks:** samtykkeboksen må **ikke være forhåndsavkrysset**; den registrerte skal avgi samtykke ved aktiv handling.
- Dataminimering gjelder innsamling, antall behandlinger, lagring og gjenbruk til nye formål; skal være standard utgangspunkt.
- Ved ferdig programvare: funksjoner som ikke er **strengt nødvendige skrus av** før programvaren tas i bruk; innstillinger som ivaretar rettigheter skrus på.
- Gjelder også organisatoriske tiltak.
- Tips: test om formålet kan nås med de mest personvernfremmende/minst inngripende tiltakene (utvid etter hvert hvis nødvendig og forankret i rettslig grunnlag); all intern behandling (oppslag, overføring, viderebehandling) må ha rettslig grunnlag og være nødvendig; ved dynamiske kontrakter må behandlingsansvarlig påse at personvern som standard ivaretas; tilgang baseres på tjenstlig behov.

**Sider av dataminimering særlig relevante for personvern som standard:**
- **Innsamling:** kun nødvendige opplysninger; nøye vurdering av mengder, kategorier og detaljnivå; kan formålet nås med færre/mindre inngripende opplysninger, skal man ikke samle inn mer. Tips: minimer; «Select before you collect».
- **Behandlingens omfang:** begrens behandlinger (innsamling, lagring, aksessering, sletting m.m.) til det minimale; viderebehandling må være forenlig med opprinnelig formål. Tips: *Minimér og skjul* (granulert, aggregert eller pseudonymisert?); *Separér* (lagre separat for å unngå urettmessig kobling; lagre ulikt etter beskyttelsesgrad).
- **Lagringstid:** fastsett og begrunn lagringstid; standardinnstillinger eller rutiner for automatisk eller manuell sletting etter fastsatt tid. Tips: slett når ikke lenger nødvendig – også i **backup og hos databehandlere**; anonymiser hvis behov uten personkobling (anonymisering likestilles med sletting).
- **Tilgangsstyring:** tilgang basert på tjenstlig behov og nødvendighetsvurdering, i alle ledd av dataflyten. De registrerte må som standard kunne **påvirke/intervenere** før opplysninger gjøres tilgjengelig for et ubegrenset antall personer (særlig viktig for barn og sårbare grupper; spredning via internett og søkemotorer) – f.eks. samtykke før publisering eller personverninnstillinger der de selv velger grad av tilgjengeliggjøring. Tips: rutiner for hvilke roller som skal ha hvilken tilgang; revider tilgangsstyringen regelmessig; gode rutiner ved offentliggjøring og regelmessig vurdering av reell mulighet for intervenering.

### 6. Eksempler på implementering av prinsippene (s. 6–12)
Innebygd personvern omfatter planlegging, anskaffelse, utvikling, drift, vedlikehold, lagring, sletting osv. Nøkkelelementene og eksemplene er veiledende og ikke uttømmende; i tillegg må rettighetene ivaretas.

#### 6.1 Lovlighet – nøkkelelementer (s. 6)
| Element | Krav |
|---|---|
| Relevans | Rett behandlingsgrunnlag brukes |
| Differensiering | Grunnlaget differensieres per behandlingsaktivitet |
| Spesifisert formål | Grunnlaget tydelig knyttet til det spesifikke formålet |
| Nødvendighet | Behandlingen nødvendig og ubetinget for at formålet skal være lovlig |
| Selvbestemmelse | Høyest mulig grad av kontroll for den registrerte innenfor rammene av grunnlaget |
| Samtykke | Frivillig, spesifikt, informert, utvetydig; særlig hensyn til barn og unge |
| Trekke samtykke | Like enkelt å trekke som å gi – ellers ikke gyldig |
| Interesseavveining | Ved berettiget interesse: vektet avveining med særlig vekt på maktbalanse, spesielt barn under 18 og sårbare grupper; tiltak og garantier som reduserer negativ innvirkning |
| Forutbestemmelse | Lovhjemmelen etablert før behandlingen |
| Opphør | Opphører hjemmelen for rettslig forpliktelse, skal behandlingen opphøre |
| Justering | Ved gyldig endring av grunnlag justeres behandlingen |
| Ansvarstildeling | Ved felles behandlingsansvar: tydelig og gjennomsiktig fordeling overfor den registrerte, tiltak utformet deretter |

**Eksempel 1 – bank og lånesøknader:** Banken vil hente ligningsopplysninger direkte fra Skatteetaten. Innsamlingen direkte fra Skatteetaten er ikke «nødvendig for kontraktsinngåelse» (kunden kan selv oppgi opplysningene), og direkte tilgang gir risiko for misbruk og mindre involvering → annet grunnlag: forhåndssamtykke. Portalen viser hva som er nødvendig og hva som er valgfritt; standard er ingen innsamling fra andre kilder enn den registrerte utover kredittsjekk; direkte innhenting presenteres slik at det ikke hindrer å *ikke* samtykke; samtykket gir midlertidig tilgang til et bestemt sett opplysninger; samtykke dokumenteres og kan enkelt kontrolleres og trekkes.

(Øverst s. 7 står et avsnitt om at den behandlingsansvarlige på forhånd har vurdert kravene til innebygd personvern og inkludert dem i kravspesifikasjonen i anbudet for å anskaffe en plattform – fordi det ellers kan bli for sent eller svært dyrt å implementere senere. Avsnittet ser ut til å være resten av et eksempel hvis begynnelse ikke er med i utskriften.)

#### 6.2 Rettferdighet – nøkkelelementer (s. 7)
Prinsippet krever at opplysninger ikke behandles urettmessig, ugunstig, diskriminerende, usant eller misvisende; tiltak skal også støtte retten til informasjon, selvbestemmelse og begrensning.
| Element | Krav |
|---|---|
| Selvbestemmelse | Høyest mulig grad av bestemmelse over bruk, omfang og vilkår |
| Interaksjon | Den registrerte kan kommunisere og utøve rettigheter |
| Forventning | Samsvar med rimelige forventninger |
| Ikke-diskriminering | Ingen urettferdig diskriminering |
| Ikke-utnyttelse | Ikke utnytte behov eller sårbarheter |
| Forbrukervalg | Ikke «låse» brukere urettferdig; proprietære tjenester kan gi innlåsing som svekker dataportabilitet (art. 20) |
| Maktbalanse | Sentralt mål; ubalanser unngås, ellers anerkjennes og motvirkes |
| Ingen risikooverføring | Risikoen overføres ikke til de registrerte |
| Ingen bedrag | Objektiv og nøytral informasjon; unngå villedende eller manipulerende språk/design |
| Respekter rettigheter | Ikke berøre grunnleggende rettigheter med mindre uttrykkelig begrunnet i loven |
| Etisk | Se bredere innvirkning på rettigheter og verdighet |
| Sannferdig | Informasjon tilgjengelig; oppfør deg som erklært; ikke villed |
| Menneskelig inngripen | Kvalifisert menneskelig inngripen som kan avdekke maskinskapte skjevheter (art. 22) |
| Rettferdige algoritmer | Vurder regelmessig om algoritmer fungerer etter formålet, juster for skjevheter; informer om algoritmebasert analyse/prediksjon (arbeidsytelse, økonomi, helse, preferanser, pålitelighet/atferd, plassering/bevegelse) |

**Eksempel 2 – søkemotor:** alternativer kan ikke presenteres slik at de skyver den registrerte mot mer innsamling, gjør det vanskelig å ikke samtykke eller senere justere innstillinger. Dette er **«dark patterns»** (manipulerende design som utnytter kunnskap om menneskelig atferd) og strider mot innebygd personvern. Standardalternativer bør ikke være inngripende; samtykke/avstå presenteres som **to like synlige valg** som korrekt viser konsekvensene.
**Eksempel 3 – strømmetjeneste med premium:** prioritert kundeservice for premium kan ikke diskriminere vanlige abonnenters utøvelse av rettigheter (art. 12 nr. 5 – svar uten unødig opphold og senest innen én måned). Alle registrerte skal ha lik og udiskriminert tilgang til rettighetene.
**[Merknad – ikke fra kilden]** Fristen «uten ugrunnet opphold og senest én måned» står i art. 12 nr. 3; art. 12 nr. 5 gjelder at kommunikasjon og tiltak skal være gratis (jf. [K43](K43-gdpr-kap03-den-registrertes-rettigheter.md#art-12)).

#### 6.3 Åpenhet – nøkkelelementer (s. 8)
Støtter rettighetene i art. 15–22.
| Element | Krav |
|---|---|
| Klarhet | Klart og tydelig språk, kortfattet og forståelig |
| Semantisk | Klar betydning for publikum |
| Tilgjengelig | Lett tilgjengelig |
| Kontekstuell | Riktig tidspunkt og riktig form |
| Relevant | Relevant og gjeldende for den spesifikke registrerte |
| Universell utforming | Tilgjengelig for alle, inkl. maskinlesbare språk |
| Forståelig | God forståelse av hva de kan forvente, særlig barn og sårbare |
| Flere medier/kanaler | Ulike kanaler og medier, ikke bare tekst |
| Lagdelt | Lagdeling som løser spenningen mellom fullstendighet og forståelse |

**Eksempel 4 – personvernerklæring:** klart og kortfattet; lagvis informasjon (viktigste punkter uthevet, rullegardinmenyer, lenker); flere kanaler inkl. videoklipp; god flyt mellom sider; synlig på alle sider – alltid **ett klikk unna**; universell utforming; kontekstuell informasjon via informasjonsflytdiagram, informasjons-/forklaringsbokser og pop-up-vinduer når opplysninger legges inn (en generell erklæring alene er ikke nok når mange behandlinger skjer).

#### 6.4 Formålsbegrensning – nøkkelelementer (s. 8–9)
Forhåndsdefinerte, eksplisitte og legitime formål; viderebehandling krever forenlighetsvurdering etter art. 6 nr. 4.
| Element | Krav |
|---|---|
| Forhåndsbestemt | Formål bestemmes før utforming |
| Spesifisert | Eksplisitt hvorfor opplysninger behandles |
| Formålsrettet | Formålet bestemmer utforming og grenser |
| Nødvendig | Formålet bestemmer hvilke opplysninger som er nødvendige |
| Kompatibilitet | Nye formål må være kompatible og styrer endringer i design |
| Begrens viderebehandling | Ikke koble datasett eller viderebehandle for inkompatible formål |
| Begrensninger for gjenbruk | Tekniske tiltak (hashing, kryptering – hashing kan ikke reverseres, kryptering kan) og organisatoriske tiltak (policyer, kontraktsforpliktelser) |
| Evaluering | Regelmessig vurdere nødvendighet og utforming opp mot formålsbegrensningen |

**Eksempel 5 – nettbutikk og CRM:** CRM med automatisk kjøpekraftanalyse (offentlig informasjon) for målrettet annonsering ligger utenfor opprinnelig formål (levering og betaling). Behandlingsansvarlig krever at CRM-leverandøren kartlegger hvordan funksjonene bruker personopplysninger, vurderer forenlighet og rettslig grunnlag; ved negativt svar brukes ikke funksjonene (eller man avstår fra tilleggsfunksjonene).

#### 6.5 Dataminimering – nøkkelelementer (s. 9–10)
Fastsett om formålet kan nås uten personopplysninger eller med begrenset bruk (f.eks. aggregerte data); fastsett på forhånd nødvendige funksjoner og parametere; slett/anonymiser når identifikasjon ikke lenger er nødvendig (f.eks. statistikk); pseudonymiser hvis fortsatt identifikasjon er nødvendig.
| Element | Krav |
|---|---|
| Unngå innsamling | Ikke behandle personopplysninger hvis mulig |
| Begrensning | Begrens mengden til det nødvendige |
| Begrensning av tilgang | Minimalt antall personer med tilgang |
| Relevans | Relevante, og relevans kan demonstreres |
| Nødvendighet | Hver kategori nødvendig og bare hvis formålet ikke kan nås på annen måte |
| Aggregering | Bruk aggregerte data når mulig |
| Pseudonymisering | Så snart direkte identifiserbarhet ikke trengs; lagre identifikasjonsnøkler separat |
| Anonymisering og sletting | Når ikke (lenger) nødvendig |
| Dataflyt | Ikke flere kopier enn nødvendig |
| «State of the art» | Oppdatert og passende teknologi for å unngå og minimere data |

**Eksempel 6 – bokhandel på nett:** obligatoriske felt for fødselsdato og telefonnummer er ikke nødvendige; adresse ikke nødvendig for e-bok. Løsning: to skjemaer – fysiske bøker med leveringsadresse, e-bøker uten adresse; felt bør ikke være obligatoriske med mindre nødvendigheten kan demonstreres.

#### 6.6 Riktighet – nøkkelelementer (s. 10)
Riktige og oppdaterte opplysninger; rimelige steg for sletting/retting; uriktige data kan gi feil beslutninger (manuelt, automatisert eller KI).
| Element | Krav |
|---|---|
| Datakilder | Pålitelige kilder |
| Nøyaktighetsgrad | Så nøyaktig som nødvendig for formålet |
| Målbart | Reduser falske positiver/negativer, f.eks. bias i automatiserte beslutninger og KI |
| Verifisering | Verifiser riktighet før og underveis (f.eks. alderskrav) |
| Sletting/retting | Straks slette/rette; særlig legge til rette når den registrerte er/var barn |
| Unngå feilutbredelse | Reduser effekten av akkumulerte feil i behandlingskjeden |
| Tilgang | Informasjon og effektiv tilgang (art. 12–15) for å kontrollere og be om retting |
| Kontinuerlig sjekk | Riktig i alle ledd; kvalitetstester i kritiske trinn |
| Oppdatert | Oppdateres om nødvendig |

**Eksempel 7 – forsikring og KI-profilering:** innebygd personvern ved valg av KI-applikasjon og trening; representativt utvalg for å unngå skjevheter; pseudonymisering før overføring til treningssystemet; kun pålitelige og oppdaterte kilder; test for pålitelighet og ikke-diskriminering under utvikling og før lansering; KI-en beslutter ikke alene; regelmessig gjennomgang og justering.
**Eksempel 8 – helseinstitusjon:** unik identifikator (ikke bare navn) for å unngå forveksling; konsistens på tvers av systemer; hash-teknikk på unik identifikator og uforanderlige kryptografiske tidsstempler for å gjenkjenne, korrelere og spore endringer.

#### 6.7 Lagringsbegrensning – nøkkelelementer (s. 10–11)
Formålet er hovedkriteriet for lagringstid; tiltak skal støtte retten til sletting og protest.
| Element | Krav |
|---|---|
| Sletting og anonymisering | Klare interne rutiner og funksjoner |
| Effektivitet av anonymisering/sletting | Ikke mulig å gjenidentifisere/gjenopprette; bør testes |
| Automatisering | Sletting av visse opplysninger bør automatiseres |
| Lagringskriterier | Bestem hvilke data og hvor lenge |
| Begrunnelse | Kunne begrunne og fremlegge begrunnelse og rettsgrunnlag for lagringsperioden |
| Håndhevelse av oppbevaringsrutiner | Håndhev og kontroller at rutinene praktiseres |
| Sikkerhetskopier/logger | Bestem hvilke opplysninger og lagringstid for backup og logger |
| Dataflyt | Vær bevisst på kopier; begrens «midlertidige» lagringer |

**Eksempel – medlemsadministrasjon:** sletting når medlemskap avsluttes og grunnlag faller bort. Fra manuell rutine (sletting fra alle enheter, sikkerhetskopier, logger, e-poster m.m.) til **automatisk slettesystem** etter forhåndsdefinerte kriterier og intervaller; rutinen gjennomgås og testes jevnlig.

#### 6.8 Integritet og konfidensialitet – nøkkelelementer (s. 11–12)
Beskyttelse mot uautorisert/lovstridig behandling og utilsiktet tap, ødeleggelse eller skade. Fortalepunkt 78: mulighet til å iverksette og forbedre sikkerhetsfunksjoner; kontinuerlig vurdering; regelmessig gjennomgang; retningslinjer for brudd.
| Element | Krav |
|---|---|
| ISMS | Operativt middel for policyer og prosedyrer for informasjonssikkerhet |
| Risikoanalyse | Vurder virkning på rettigheter mot identifiserte risikoer; omfattende, systematisk og realistisk **trusselmodellering** og **angrepsoverflateanalyse** |
| Sikkerhet ved design | Sikkerhetskrav tidligst mulig; kontinuerlige tester |
| Vedlikehold | Regelmessig gjennomgang og testing av programvare, maskinvare, systemer og tjenester |
| Styring av adgangskontroll | Kun autorisert personell med tjenstlig behov; skill tilgangsrettigheter. Begrensning av tilgang (personell) – minimalt antall; begrensning av tilgang (innhold) – kun nødvendige attributter per operasjon og kun registrerte i den ansattes ansvarsområde; tilgangsdifferensiering (lese, skrive, slette, rette) |
| Sikker overføring | Mot uautorisert og utilsiktet tilgang og endring |
| Sikker lagring | Mot uautorisert tilgang og endring; prosedyrer for risiko ved sentralisert vs. desentralisert lagring; noen data trenger ekstra tiltak eller isolasjon |
| Pseudonymisering | Også for sikkerhetskopier/logger (hashing, kryptering) |
| Sikkerhetskopier/logger | Behold så langt nødvendig; revisjonsspor og hendelsesovervåking; beskytt, gjennomgå regelmessig, håndter hendelser raskt |
| Katastrofegjenoppretting/forretningskontinuitet | Gjenopprett tilgjengelighet etter større hendelser |
| Beskyttelse i henhold til risiko | Tiltak etter risiko; spesielt risikable data holdes atskilt |
| Sikkerhetshendelses-responshåndtering | Rutiner, prosedyrer og ressurser for å oppdage, begrense, håndtere, rapportere og lære |
| Hendelseshåndtering | Prosesser for brudd og hendelser, inkl. melding til tilsynsmyndigheten og underretning av de registrerte (brudd på personopplysningssikkerheten, art. 33–34) |

**Eksempel 10 – uttrekk fra pasientdatabase til kvalitetssikring:** tilgang begrenset til én avdeling; pseudonymisering før overføring; nettverkssegmentering og tilgangskontroll; sikkerhetsovervåking og inntrengingsdeteksjon/-forebygging isolert fra drift; automatisert revisjonssystem med varsler; riktig tilgangsnivå; ekstrakter lagres tre måneder i separate databaser med transparent kryptering og kolonnekryptering; dekrypteringsnøkler i dedikerte sikkerhetsmoduler (kan ikke hentes ut). (Kilden hopper fra eksempel 8 til 10 – eksempel 9 er ikke nummerert i utskriften; medlemsadministrasjons-eksempelet er unummerert.)

#### 6.9 Ansvarlighet (s. 12)
Overordnet prinsipp: behandlingsansvarlig skal kunne demonstrere etterlevelse av alle prinsippene, gi føringer for at innebygd personvern håndheves i alle behandlinger og dokumentere dette – f.eks. påvise hvorfor et tiltak er tilstrekkelig for lagringsbegrensning. Krever god forståelse av forpliktelsene og evne til å etterleve dem.

### 7. Sertifiseringsmuligheter (s. 13)
Sertifisering (art. 42) kan brukes som element for å påvise etterlevelse; sertifiserte prosesser hensyntas av tilsynsmyndigheter. Ved sertifisering av innebygd personvern er elementer i designprosessen særlig relevante: valg av behandlingsmidler, tekniske og organisatoriske tiltak og forvaltning av dem, prosess for kontinuerlig vurdering. Mer informasjon kommer fortløpende.

### 8. Håndhevelse (s. 14)
Datatilsynet kan føre tilsyn etter art. 58; korrigerende tiltak etter art. 58 nr. 2 kan være overtredelsesgebyr eller pålegg. **Ved utmåling av overtredelsesgebyr er vurderingen av brudd på innebygd personvern et spesielt viktig moment.**

## Praktiske sjekkpunkter
- Kontroller at styringssystemet for utvikling/anskaffelse/oppdatering har krav om innebygd personvern og at bestillerkompetanse finnes.
- Ta inn art. 25-krav i anbud, kravspesifikasjon og kontrakt/databehandleravtale; krev at leverandøren holder deg oppdatert om «state of the art» og kartlegger funksjoners bruk av personopplysninger.
- Kontroller standardinnstillinger: ingen forhåndsavkryssede samtykkebokser; unødvendige funksjoner deaktivert; minst inngripende alternativ som standard; registrerte kan påvirke offentliggjøring.
- Kontroller at kun nødvendige skjemafelt er obligatoriske.
- Gå gjennom nøkkelelementtabellene per prinsipp som sjekkliste i DPIA og kravspesifikasjon.
- Se etter «dark patterns»: samtykke/avslag skal være to like synlige valg.
- Sørg for fastsatte og begrunnede lagringstider, helst automatisert sletting – også i backup, logger og hos databehandlere; test at sletting/anonymisering er effektiv.
- Tilgangsstyring etter tjenstlig behov, differensiert, revidert regelmessig.
- KI: representative treningsdata, pseudonymisering, bias-testing, menneskelig inngripen, løpende overvåking.
- Eldre systemer: gjennomfør GAP-analyse mot art. 25.
- Definer KPI-er for effektivitet; dokumenter vurderinger, DPIA, PVO-råd og sikkerhetstester.

## Viktige sitater
- «Innebygd personvern er et sentralt krav i personopplysningsloven og betyr at det tas hensyn til personvern i alle utviklingsfaser av et system eller en løsning.» (s. 1)
- «Behandlingsansvarlige må alltid vurdere om behandlingsmidler faktisk har innebygd personvern, også om de tar i bruk produkter og tjenester som er utviklet av tredjeparter.» (s. 2)
- «Imidlertid er høye kostnader ingen unnskyldning for å unnlate implementering av effektive tiltak i behandlingen for å få på plass innebygd personvern.» (s. 3)
- «Som standardinnstilling må avkrysningsboksen ikke være forhåndsavkrysset» (s. 5)
- «Ved bruk av programvare som er ferdig utviklet, må behandlingsansvarlig konfigurere programvaren slik at funksjoner som ikke er strengt nødvendig for behandlingen skrus av før programvaren tas i bruk.» (s. 5)
- «Kravet om innebygd personvern gjelder også for systemer og løsninger som ble utviklet før personvernregelforordningen av 2018 trådte i kraft» (s. 4)
- «Ved ileggelse av overtredelsesgebyr, er vurderingen av brudd på innebygd personvern et spesielt viktig moment» (s. 14)

## Kryssreferanser
- GDPR: art. 5, 6 nr. 4, 12 nr. 3, 12–22, 20, 22, 24, 25, 28, 32, 35, 42, 58 nr. 2; fortalepunkt 78
- EDPB Guidelines 4/2019 on Article 25
- [K09](K09-dt-grunnleggende-prinsipper.md) – personvernprinsippene
- [K12](K12-dt-dpia-veiledning.md) – DPIA (DPIA skal skje i samsvar med art. 25)
- [K05](K05-dt-databehandleravtale.md) – krav til databehandlere
- [K08](K08-dt-retting-og-sletting.md) – sletting/retting; [K10](K10-dt-kryptering.md) – kryptering
- [K06](K06-dt-informasjon-og-apenhet.md) – åpenhet; [K02](K02-dt-behandlingsgrunnlag.md) – samtykke og behandlingsgrunnlag
- [K39](K39-cnil-mobilapper.md) – CNIL om mobilapper (konkretisering for apper)

## Aktualitet og begrensninger
- Utskrift 22.09.2026; ingen publiseringsdato. Bygger på EDPB Guidelines 4/2019 (versjon 2.0, 2020).
- Datatilsynets egen «programvareutvikling med innebygd personvern»-veiledning er under revisjon.
- Utskriften ser ut til å mangle begynnelsen på ett eksempel (anbud for plattform, s. 7) og eksempel 9 er ikke nummerert; tabellene er gjengitt fullstendig.
- Sertifiseringsmekanismer etter art. 42 er ikke konkretisert («kommer fortløpende»).

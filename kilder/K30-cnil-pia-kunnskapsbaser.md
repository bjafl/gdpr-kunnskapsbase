---
id: K30
tittel: "PIA, knowledge bases"
utgiver: CNIL (Commission Nationale de l'Informatique et des Libertés, Frankrike)
dato: "Februar 2018 (February 2018 edition)"
spraak: en
fil: "ressurser/cnil-pia-3-en-knowledgebases.pdf"
type: metode
gdpr_artikler: [5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25, 28, 32, 33, 34, 35, 36, 44, 45, 46, 47, 48, 49]
emner: [dpia, pia, risikovurdering, trusselkatalog, tiltakskatalog, alvorlighet, sannsynlighet, risikokilder, støtteressurser, informasjonssikkerhet, kryptering, tilgangskontroll, logging, sikkerhetskopi, databehandler, rettigheter, samtykke]
relevans: høy
---

# PIA, knowledge bases (CNIL, 2018)

## Sammendrag

Tredje av CNILs tre PIA-guider (GDPR-tilpasset 2018-utgave, 104 sider). Dokumentet er et **oppslagsverk**: kapittel 1 gir kunnskapsbasene for selve risikostudien – typologi av personopplysninger, støtteressurser, risikokilder og utfall av fryktede hendelser; **skalaer og regler for alvorlighet og sannsynlighet (4 nivåer)** med eksempler på fysiske, materielle og moralske konsekvenser; **trusselkataloger** for de tre fryktede hendelsene (uautorisert tilgang, uønsket endring, forsvinning) per støtteressurs og handling; og skalaer for handlingsplanen. Kapittel 2–43 er en **tiltakskatalog** (alfabetisk etter fransk tittel) med formål («Aims»), god praksis og anbefalinger for hvert tiltak – fra anonymisering, arkivering, kryptering og tilgangskontroll til informasjon, samtykke, rettigheter, databehandlere, overføringer og logging. Katalogen dekker både de rettslige grunnprinsippene og sikkerhetstiltakene som inngår i malene ([K29](K29-cnil-pia-maler.md)). Mange anbefalinger er franske (ANSSI, RGS, DP-Act) og noen tekniske terskler er utdaterte (se Aktualitet).

## Når skal agenten bruke denne kilden

- Når agenten skal **estimere alvorlighet eller sannsynlighet** – bruk skalaene i §1.5–1.6 og eksempeltabellen for konsekvenser.
- Når agenten skal **identifisere trusler** systematisk per støtteressurs (maskinvare, programvare, nettverk, personer, papir, papirkanaler) – bruk trusselkatalogene §1.7–1.9.
- Når agenten skal **foreslå tiltak** mot en risiko eller fylle ut feltet «Implementation» i en DPIA – slå opp tiltaket i katalogen (kap. 2–43).
- Når agenten skal sjekke om en **databehandleravtale** dekker art. 28-punktene og CNILs tilleggskrav (kap. 34), eller tredjepartsforhold (kap. 32).
- Når agenten skal vurdere rutiner for **rettigheter, informasjon og samtykke** (kap. 11–13, 22, 31), **avvikshåndtering** (kap. 17), **lagringstid** (kap. 9) eller **logging** (kap. 36, 43).
- Når agenten skal sette **mål for risikobehandling** og bygge handlingsplan (§1.10; se også typologi av mål i [K31](K31-cnil-pia-tilkoblede-objekter.md) vedlegg 6).

## Hovedinnhold

### Del 1 – Kunnskapsbaser for studien (s. 2–10)

#### 1.1 Typologi av personopplysninger (s. 2)

| Type | Kategorier |
|---|---|
| Vanlige personopplysninger (common) | Sivilstatus, identitet, identifikasjonsdata |
| | Privatliv (levevaner, sivilstand m.m. – unntatt sensitive eller farlige data) |
| | Yrkesliv (CV, utdanning og opplæring, utmerkelser m.m.) |
| | Økonomisk og finansiell informasjon (inntekt, finansiell situasjon, skatt m.m.) |
| | Tilkoblingsdata (IP-adresser, hendelseslogger m.m.) |
| | Lokasjonsdata (reiser, GPS-data, GSM-data m.m.) |
| Opplysninger *oppfattet som* sensitive | Personnummer (social security number) |
| | Biometriske data |
| | Bankdata |
| Sensitive opplysninger etter DP-Act (art. 8 og 9; direktivet art. 8) | Filosofisk, politisk, religiøs og fagforeningsmessig overbevisning, seksualliv, helse, rasemessig eller etnisk opprinnelse |
| | Lovbrudd, domfellelser, sikkerhetstiltak |

**[Merknad – ikke fra kilden]** Tabellen bygger på den gamle franske DP-Act. Etter GDPR er tilsvarende kategorier «særlige kategorier av personopplysninger» (art. 9 nr. 1), som også omfatter genetiske opplysninger og biometriske opplysninger med det formål å entydig identifisere en fysisk person – biometri er altså ikke bare «oppfattet som» sensitivt. Lovbrudd og domfellelser reguleres i art. 10 (jf. [K43](K43-gdpr-kap02-prinsipper.md#art-9)).

#### 1.2 Typologi av støtteressurser (supporting assets) (s. 2)

| Gruppe | Type støtteressurs | Eksempler |
|---|---|---|
| Informasjonssystemer | Maskinvare og elektroniske lagringsmedier | Datamaskiner, kommunikasjonsreléer, USB-pinner, harddisker |
| | Programvare | Operativsystemer, e-post, databaser, fagapplikasjoner |
| | Datakanaler (computer channels) | Kabler, Wi-Fi, fiberoptikk |
| Organisasjoner | Personer | Brukere, IT-administratorer, beslutningstakere |
| | Papirdokumenter | Utskrifter, kopier, håndskrevne dokumenter |
| | Papirbaserte overføringskanaler | Post, arbeidsflyt (workflow) |

#### 1.3 Typologi av risikokilder (s. 3)

| Type | Eksempler |
|---|---|
| Interne menneskelige kilder | Ansatte, IT-ansvarlige, praktikanter, ledere |
| Eksterne menneskelige kilder | Mottakere av personopplysninger, autoriserte tredjeparter (f.eks. offentlige myndigheter og rettsvesen med lovhjemmel), tjenesteleverandører, hackere, besøkende, tidligere ansatte, aktivister, konkurrenter, kunder, vedlikeholdspersonell, lovbrytere, fagforeninger, journalister, frivillige organisasjoner, kriminelle organisasjoner, organisasjoner kontrollert av en fremmed stat, terrororganisasjoner, nærliggende industrivirksomhet |
| Ikke-menneskelige kilder | Skadelig kode av ukjent opprinnelse (virus, ormer m.m.), vann (rør, vassdrag m.m.), brennbare, etsende eller eksplosive materialer, naturkatastrofer, epidemier, dyr |

#### 1.4 Typologi av utfall av fryktede hendelser (s. 3)

| Fryktet hendelse | Utfall | Beskrivelse |
|---|---|---|
| Uautorisert tilgang | Ingen (None) | Dataene ses av personer uten tjenstlig behov, men brukes ikke. |
| | Lagring (Storage) | Dataene kopieres og lagres et annet sted uten videre bruk. |
| | Videreformidling (Redistribution) | Dataene spres mer enn nødvendig og utenfor de registrertes kontroll (f.eks. uønsket spredning av et bilde på Internett, tap av kontroll over informasjon publisert i sosiale medier). |
| | Bruk (Use) | Dataene brukes til andre formål enn planlagt og/eller urimelig (kommersielle formål, identitetstyveri, bruk mot de registrerte) eller sammenstilles med annen informasjon (f.eks. bostedsadresse + sanntids geolokasjon). |
| Uønsket endring | Funksjonsfeil (Malfunction) | Dataene endres til gyldige eller ugyldige data som ikke brukes riktig; behandlingen kan gi feil, funksjonssvikt eller ikke lenger levere forventet tjeneste. |
| | Bruk (Use) | Dataene endres til andre gyldige data slik at behandlingen er eller kan bli misbrukt (f.eks. identitetstyveri ved å endre koblingen mellom identitet og biometri). |
| Forsvinning | Funksjonsfeil | Data mangler, noe som gir feil eller en annen tjeneste enn forventet (f.eks. allergier ikke lenger registrert i journal; opplysninger i selvangivelse borte så skatten ikke kan beregnes). |
| | Blokkering (Blockage) | Data mangler slik at behandlingen ikke kan levere tjenesten (f.eks. forsinkede/blokkerte administrative eller kommersielle prosesser, umulig å gi helsehjelp pga. tapt journal, de registrerte kan ikke utøve sine rettigheter). |

#### 1.5 Skala og regler for alvorlighet (severity) (s. 4–5)

Alvorlighet = risikoens størrelse; estimeres primært ut fra omfanget av potensielle konsekvenser for de registrerte, **med hensyn til eksisterende, planlagte eller tilleggstiltak** (som skal nevnes i begrunnelsen). «Important: these are only examples, which can be very different depending on the context» (s. 4).

Konsekvenstyper: **fysiske** (tap av livskvalitet, vansiring eller økonomisk tap knyttet til fysisk integritet), **materielle** (lidt tap eller tapt inntekt for den enkeltes formue), **moralske** (fysisk eller følelsesmessig lidelse, vansiring eller tap av livskvalitet) (fotnoter 3–5).

**Nivå 1 – Ubetydelig (Negligible):** De registrerte påvirkes ikke, eller får noen ulemper de overkommer uten problemer.

| Fysiske | Materielle | Moralske |
|---|---|---|
| Mangelfull omsorg for en avhengig person (mindreårig, person under vergemål) | Tidstap ved å gjenta formaliteter eller vente på at de blir gjennomført | Ren irritasjon over mottatt eller etterspurt informasjon |
| Forbigående hodepine | Mottak av uønsket post (f.eks. spam) | Frykt for å miste kontroll over egne data |
| | Gjenbruk av data publisert på nettsteder til målrettet reklame (informasjon til sosiale nettverk, gjenbruk til papirpost) | Følelse av krenket privatliv uten reell eller objektiv skade (f.eks. kommersiell påtrengenhet) |
| | Målrettet reklame for vanlige forbruksvarer | Tidstap ved å konfigurere egne data |
| | | Manglende respekt for fri bevegelse på nett pga. nektet tilgang til kommersielt nettsted (f.eks. alkohol pga. feil alder) |

**Nivå 2 – Begrenset (Limited):** Betydelige ulemper som de vil kunne overkomme til tross for noen vanskeligheter.

| Fysiske | Materielle | Moralske |
|---|---|---|
| Mindre fysiske plager (f.eks. mindre sykdom pga. tilsidesatte kontraindikasjoner) | Uforutsette betalinger (f.eks. feilaktige bøter), tilleggskostnader (bankgebyrer, advokatutgifter), betalingsmislighold | Nekter å fortsette å bruke informasjonssystemer (varsling, sosiale nettverk) |
| Mangelfull omsorg som gir mindre, men reell skade (f.eks. funksjonsnedsettelse) | Nektet tilgang til administrative eller kommersielle tjenester | Mindre, men objektive psykiske plager (ærekrenkelse, omdømme) |
| Ærekrenkelse som gir fysisk eller psykisk gjengjeldelse | Tapte muligheter for komfort (avlyst fritid, kjøp, ferie, avsluttet nettkonto) | Relasjonsproblemer med private eller profesjonelle bekjente (image, svekket omdømme, tap av anerkjennelse) |
| | Gått glipp av forfremmelse | Følelse av krenket privatliv uten irreversibel skade |
| | Blokkert konto for nettjenester (spill, forvaltning) | Trakassering/skremsel i sosiale medier |
| | Mottak av uønskede målrettede utsendelser som kan skade omdømmet | |
| | Kostnadsøkning (f.eks. høyere forsikringspremie) | |
| | Ikke-oppdaterte data (f.eks. tidligere stilling) | |

(Merk: i tekstuttrekket står eksemplene for nivå 1 og 2 i én sammenhengende celle; fordelingen over følger kildens rekkefølge – de første punktene i hver kolonne hører til nivå 1, de senere til nivå 2. Kontroller mot PDF s. 4 ved tvil.)

**Nivå 3 – Betydelig (Significant):** Betydelige konsekvenser som de bør kunne overkomme, men med reelle og alvorlige vanskeligheter.

| Fysiske | Materielle | Moralske |
|---|---|---|
| Alvorlige fysiske plager som gir langvarig skade (f.eks. forverret helse pga. feil behandling eller tilsidesatte kontraindikasjoner) | Behandling av feil data som gir f.eks. feil på kontoer (bank, kunder, sosiale etater) | Alvorlige psykiske plager (f.eks. depresjon, utvikling av fobi) |
| Skade på fysisk integritet, f.eks. etter overfall, ulykke hjemme eller på jobb | Målrettet nettreklame om et privat forhold personen ville holde hemmelig (f.eks. graviditet, legemiddelbehandling) | Følelse av krenket privatliv med irreversibel skade |
| | Uriktig eller upassende profilering | Følelse av sårbarhet etter innkalling til retten |
| | Underslag av penger som ikke erstattes | Følelse av krenkelse av grunnleggende rettigheter (f.eks. diskriminering, ytringsfrihet) |
| | Ikke-midlertidige økonomiske vansker (f.eks. må ta opp lån) | Utpressing |
| | | Nettmobbing og trakassering |

**Nivå 4 – Maksimal (Maximum):** Betydelige eller til og med irreversible konsekvenser som de kanskje ikke kan overkomme.

| Fysiske | Materielle | Moralske |
|---|---|---|
| Langvarige eller permanente fysiske plager (f.eks. pga. tilsidesatte kontraindikasjoner) | Målrettede, unike og ikke-tilbakevendende tapte muligheter (boliglån, avslag på studier, praksisplass eller jobb, eksamensforbud) | Langvarige eller permanente psykiske plager |
| Død (f.eks. drap, selvmord, dødsulykke) | Forbud mot å ha bankkonto | Strafferettslig sanksjon |
| Permanent svekket fysisk integritet | Skade på eiendom | Bortføring |
| | Tap av bolig | Tap av familiebånd |
| | Tap av arbeid | Manglende evne til å gå til sak |
| | Separasjon eller skilsmisse | Endret forvaltningsstatus og/eller tap av rettslig autonomi (vergemål) |
| | Økonomisk tap som følge av svindel (f.eks. etter phishing-forsøk) | |
| | Blokkert i utlandet | |
| | Tap av kundedata | |
| | Finansiell risiko | |
| | Betydelig gjeld | |
| | Arbeidsuførhet | |
| | Manglende evne til å flytte | |
| | Tap av bevis i rettstvist | |
| | Tap av tilgang til vital infrastruktur (vann, strøm) | |

**Regel (s. 5):** Velg det nivået som best samsvarer med de identifiserte konsekvensene ved å sammenligne dem med de generiske konsekvensene i skalaen. Nivået kan **heves eller senkes** ut fra:
- identifiseringsgrad for personopplysningene;
- risikokildenes art;
- antall sammenkoblinger (særlig med utenlandske nettsteder);
- antall mottakere (som gjør det lettere å sammenstille opprinnelig adskilte opplysninger).

#### 1.6 Skala og regler for sannsynlighet (likelihood) (s. 6)

Sannsynlighet = hvor gjennomførbart det er at risikoen inntreffer; estimeres primært ut fra sårbarhetene i støtteressursene og risikokildenes kapabilitet til å utnytte dem, med hensyn til eksisterende, planlagte eller tilleggstiltak.

| Nivå | Definisjon | Eksempel |
|---|---|---|
| 1. Ubetydelig (Negligible) | «it does not seem possible for the selected risk sources to materialize the threat by exploiting the properties of supporting assets» | Tyveri av papirdokumenter i rom beskyttet med kortleser **og** adgangskode |
| 2. Begrenset (Limited) | «it seems difficult …» | … i rom beskyttet med kortleser |
| 3. Betydelig (Significant) | «it seems possible …» | … på kontorer som ikke kan nås uten innsjekk i resepsjonen |
| 4. Maksimal (Maximum) | «it seems extremely easy …» | … i den offentlige lobbyen |

Velg nivået som best samsvarer med støtteressursenes sårbarheter og risikokildene. Kan **heves eller senkes** ut fra:
- åpent mot Internett eller lukket system;
- datautveksling med utlandet eller ikke;
- sammenkoblinger med andre systemer eller ingen;
- heterogent eller homogent system;
- variabelt eller stabilt system;
- organisasjonens omdømme (image).

(Regel for samlet risikonivå fra metoden, [K28](K28-cnil-pia-metode.md) s. 15: risikoens alvorlighet = den fryktede hendelsens alvorlighet; risikoens sannsynlighet = høyeste sannsynlighet blant tilhørende trusler.)

**Handlinger på støtteressurser** (definert i [K31](K31-cnil-pia-tilkoblede-objekter.md) vedlegg 4): *brukt upassende* (used inappropriately – brukt utenfor tiltenkt kontekst uten å bli endret/skadet), *observert* (observed – spionert på uten skade), *overbelastet* (overloaded – driftsgrenser overskredet), *skadet* (damaged), *endret* (altered – transformert), *mistet* (lost – tapt, stjålet, solgt eller gitt bort), samt *manipulert* (manipulated – for personer).

#### 1.7 Trusler som kan gi uautorisert tilgang (konfidensialitet, «C») (s. 6–7)

| Støtteressurs | Handling | Eksempler på trusler | Eksempler på sårbarheter |
|---|---|---|---|
| Maskinvare | Brukt upassende | Bruk av USB-pinner/disker som ikke passer informasjonens sensitivitet; bruk eller transport av sensitivt utstyr til private formål; harddisken med informasjonen brukes til andre formål (f.eks. frakte andre data til en leverandør, overføre andre data mellom databaser) | Kan brukes til andre formål enn tiltenkt; misforhold mellom maskinvarens kapasitet og behovet (f.eks. flere TB disk for noen få GB data) |
| Maskinvare | Observert | Se på en persons skjerm uten at vedkommende vet det (på toget); ta bilde av en skjerm; geolokasjon av maskinvare; fjerndeteksjon av elektromagnetiske signaler | Gjør tolkbare data observerbare; genererer kompromitterende utstråling |
| Maskinvare | Endret | Sporing med maskinvarebasert keylogger; fjerning av komponenter; tilkobling av enheter (f.eks. USB-pinner) for å starte et OS eller hente data | Komponenter (kort, utvidelseskort) kan legges til, fjernes eller byttes via kontakter (porter, spor); komponenter kan deaktiveres (USB-port) |
| Maskinvare | Mistet | Tyveri av bærbar PC fra hotellrom; tyveri av jobbtelefon (lommetyv); gjenfinning av kassert lagringsmedium/maskinvare; tap av elektronisk lagringsmedium | Små, attraktive mål (markedsverdi) |
| Programvare | Brukt upassende | Innholdsskanning; urettmessig sammenstilling av data; privilegieeskalering, sletting av spor; sending av spam via e-postprogram; misbruk av nettverksfunksjoner | Gjør data tilgjengelige for visning eller manipulering (sletting, endring, flytting); kan brukes til annet enn normal bruk; tillater avansert funksjonalitet |
| Programvare | Observert | Skanning av nettverksadresser og porter; innsamling av konfigurasjonsdata; analyse av kildekode for å finne sårbarheter; testing av hvordan databaser svarer på ondsinnede spørringer | Mulig å observere programvarens funksjon; tilgang til og lesing av kildekode |
| Programvare | Endret | Sporing med programvarebasert keylogger; infeksjon med skadelig kode; installasjon av fjernadministrasjonsverktøy; utskifting av komponenter under oppdatering, vedlikehold eller installasjon | Redigerbar (kan forbedres, konfigureres); utilstrekkelig kompetente utviklere/forvaltere (ufullstendige spesifikasjoner, få interne ressurser); fungerer ikke som forventet |
| Datakanaler | Observert | Avlytting av Ethernet-trafikk; innhenting av data sendt over Wi-Fi | Gjennomtrengelig (kompromitterende utstråling); gjør tolkbare data observerbare |
| Personer | Observert | Utilsiktet avsløring i samtale; avlyttingsutstyr i møter | Personer som ikke kan holde på hemmeligheter; forutsigbare (rutinepregede liv som gjør gjentatt spionasje lett) |
| Personer | Manipulert | Påvirkning (phishing, social engineering, bestikkelse); press (utpressing, psykisk trakassering) | Lett påvirkelige (naive, godtroende, sløve, lav selvfølelse, liten lojalitet); lett manipulerbare (sårbare for press mot seg selv eller familie/venner) |
| Personer | Mistet | Headhunting av ansatte; endrede arbeidsoppgaver; overtakelse av hele eller deler av organisasjonen | Liten lojalitet til organisasjonen; personlige behov som i stor grad ikke er dekket; lett brudd på kontraktsforpliktelser |
| Papirdokumenter | Observert | Lesing, kopiering, fotografering | Gjør tolkbare data synlige |
| Papirdokumenter | Mistet | Tyveri av filer fra kontorer; tyveri av post fra postkasser; gjenfinning av kasserte dokumenter | Bærbare |
| Papirkanaler | Observert | Lesing av signaturbøker i omløp; kopiering av dokumenter under transport | Observerbare |

(Tabellen er rekonstruert fra et tekstuttrekk der kildens tabell var forskjøvet; radene og innholdet stemmer med samme tabell i [K31](K31-cnil-pia-tilkoblede-objekter.md) s. 43–44.)

#### 1.8 Trusler som kan gi uønsket endring (integritet, «I») (s. 8)

| Støtteressurs | Handling | Eksempler på trusler | Eksempler på sårbarheter |
|---|---|---|---|
| Maskinvare | Endret | Tillegg av inkompatibel maskinvare som gir feil; fjerning av komponenter nødvendige for at en applikasjon fungerer | Komponenter kan legges til/fjernes/byttes via kontakter; komponenter kan deaktiveres (USB-port) |
| Programvare | Brukt upassende | Uønskede endringer av data i databaser; sletting av filer nødvendige for at programvaren skal virke; operatørfeil som endrer data | Gjør data tilgjengelige for visning/manipulering; kan brukes til annet enn normal bruk; tillater avansert funksjonalitet |
| Programvare | Endret | Feil ved oppdatering, konfigurasjon eller vedlikehold; infeksjon med skadelig kode; utskifting av komponenter | Redigerbar; utilstrekkelig kompetente utviklere/forvaltere; fungerer ikke som forventet |
| Datakanaler | Brukt upassende | Man-in-the-middle-angrep for å endre eller legge til data i nettverkstrafikk; replay-angrep (gjensending av avlyttede data) | Tillater endring av trafikk (avlytting og gjensending, eventuelt endret); eneste overføringsvei for flyten; tillater endring av delingsregler (protokoll som tillater nye noder) |
| Personer | Overbelastet | Høy arbeidsbelastning, stress eller negative endringer i arbeidsforhold; oppgaver utover evner; dårlig bruk av kompetanse | Utilstrekkelige ressurser for oppgavene; kapasitet ikke tilpasset arbeidsforholdene; utilstrekkelig kompetanse; manglende evne til omstilling |
| Personer | Manipulert | Påvirkning (rykter, desinformasjon) | Lett påvirkelige (naive, godtroende, sløve) |
| Papirdokumenter | Endret | Endring av tall i en fil; erstatning av original med forfalskning | Kan forfalskes (redigerbart innhold) |
| Papirkanaler | Endret | Endring av notat uten forfatterens kunnskap; bytte fra én signaturbok til en annen; sending av flere motstridende dokumenter | Distribuerte dokumenter kan endres; eneste overføringsvei; kanalen kan endres |

#### 1.9 Trusler som kan gi forsvinning (tilgjengelighet, «D») (s. 8–10)

| Støtteressurs | Handling | Eksempler på trusler | Eksempler på sårbarheter |
|---|---|---|---|
| Maskinvare | Brukt upassende | Lagring av private filer; privat bruk | Kan brukes til andre formål enn tiltenkt |
| Maskinvare | Overbelastet | Full lagringsenhet; strømbrudd; overbelastet prosesseringskapasitet; overoppheting; ekstreme temperaturer; tjenestenektangrep (DoS) | For lav lagrings- eller prosesseringskapasitet; krever konstant strøm; følsom for spenningsvariasjoner |
| Maskinvare | Endret | Tillegg av inkompatibel maskinvare som gir feil; fjerning av komponenter nødvendige for systemet | Komponenter kan legges til/fjernes/byttes; kan deaktiveres |
| Maskinvare | Skadet | Flom, brann, hærverk, naturlig slitasje, feil på lagringsenhet | Komponenter av dårlig kvalitet (skjøre, lettantennelige, dårlig aldringsbestandighet); ikke tilpasset bruksforholdene; slettbare (sårbare for magnetfelt eller vibrasjoner) |
| Maskinvare | Mistet | Tyveri av bærbar PC; tap av mobiltelefon; kassering av støtteressurs; for små disker som fører til mange lagringsmedier og tap av noen | Bærbare, attraktive mål (markedsverdi) |
| Programvare | Brukt upassende | Sletting av data; bruk av forfalsket eller kopiert programvare; operatørfeil som sletter data | Gjør data tilgjengelige for visning/manipulering; kan brukes til annet enn normal bruk; tillater avansert funksjonalitet |
| Programvare | Overbelastet | Overskridelse av databasestørrelse; injeksjon av data utenfor normalt verdiområde; DoS-angrep | Tillater all slags data; tillater ubegrenset datamengde; tillater handlinger utført via inndata; lav interoperabilitet |
| Programvare | Endret | Feil ved oppdatering, konfigurasjon eller vedlikehold; skadelig kode; utskifting av komponenter | Redigerbar; utilstrekkelig kompetente utviklere/forvaltere; fungerer ikke som forventet |
| Programvare | Skadet | Sletting av kjørbar fil eller kildekode under kjøring; logisk bombe (i K31: også virus) | Programmer kan slettes; eneste kopi; komplisert i bruk (lite brukervennlig, få forklaringer) |
| Programvare | Mistet | Lisens ikke fornyet for programvare som brukes til å nå dataene; leverandøren slutter med sikkerhetsoppdateringer; leverandørkonkurs; korrupt lagringsmodul med lisensnumre | Eneste kopi (av lisensavtaler eller internt utviklet programvare); attraktiv (sjelden, innovativ, høy kommersiell verdi); overdragbar (full overdragelsesklausul i lisens) |
| Datakanaler | Overbelastet | Misbruk av båndbredde; uautorisert nedlasting; tap av Internett-forbindelse | Ikke-skalerbar overføringskapasitet (utilstrekkelig båndbredde; begrenset antall telefonnumre) |
| Datakanaler | Skadet | Kuttede kabler, dårlig Wi-Fi-mottak, korrosjon på kabler | Kan skades (skjøre, dårlig kabelstruktur, nakne kabler, uforholdsmessig kappe); eneste |
| Datakanaler | Mistet | Tyveri av kobberkabler | Attraktive mål (markedsverdi), transporterbare (lette, kan skjules); lite iøynefallende |
| Personer | Overbelastet | Høy arbeidsbelastning, stress, negative endringer i arbeidsforhold; oppgaver utover evner; dårlig bruk av kompetanse | Utilstrekkelige ressurser; kapasitet ikke tilpasset; utilstrekkelig kompetanse; manglende omstillingsevne |
| Personer | Skadet | Arbeidsulykke; yrkessykdom; annen skade eller sykdom; død; nevrologisk, psykologisk eller psykiatrisk lidelse | Fysiske, psykiske eller mentale begrensninger |
| Personer | Mistet | Død, pensjonering, omplassering; kontraktsslutt eller oppsigelse; overtakelse av hele eller deler av organisasjonen | Liten lojalitet; udekkede personlige behov; lett brudd på kontraktsforpliktelser |
| Papirdokumenter | Brukt upassende | Gradvis utvisking over tid; frivillig sletting av deler av et dokument; gjenbruk av papir til notater, handleliste; bruk av notatbøker til annet | Redigerbare (slettbart innhold, termopapir som ikke tåler temperaturendringer) |
| Papirdokumenter | Skadet | Aldring av arkiverte dokumenter; brann | Dårlig kvalitet (skjøre, lettantennelige, dårlig aldringsbestandighet); ikke tilpasset bruksforholdene |
| Papirdokumenter | Mistet | Tyveri av dokumenter; tap av filer ved flytting; kassering | Bærbare |
| Papirkanaler | Overbelastet | Overbelastet post; overbelastet godkjenningsprosess | Kvantitative eller kvalitative begrensninger |
| Papirkanaler | Skadet | Arbeidsflyt avsluttet etter omorganisering; postlevering stanset av streik | Ustabil, eneste |
| Papirkanaler | Endret | Endret måte å sende post på; omplassering av kontorer; omorganisering av papirkanaler; endret arbeidsspråk | Redigerbar (kan erstattes) |
| Papirkanaler | Mistet | Prosess fjernet etter omorganisering; tap av budfirma; ledig stilling | Behovet er ikke anerkjent |

#### 1.10 Skalaer for handlingsplanen (s. 10)

| Kriterium | Nivå 1 | Nivå 2 | Nivå 3 |
|---|---|---|---|
| Vanskelighetsgrad (Difficulty) | Lav | Moderat | Høy |
| Økonomisk kostnad (Financial cost) | Ingen (Nil) | Moderat | Høy |
| Termin (Term) | Kvartal | År | 3 år |
| Fremdrift (Progress) | Ikke startet | Pågår | Fullført |

(Merk: [K31](K31-cnil-pia-tilkoblede-objekter.md) vedlegg 5 bruker en annen termin-skala – År / Kvartal / Måned – og «Significant» i stedet for «High» for kostnad.)

---

### Del 2 – Tiltakskatalog (kap. 2–43)

Hvert kapittel har «Aims» (formål), «Good practices» (god praksis, ev. «to be followed if the measure is used to address risks») med «Recommendations», og ofte «Notes» og «Tools/To find out more». Nedenfor er katalogen gjengitt kompakt med alle anbefalinger. Kolonnen «Mal» viser hvor tiltaket hører hjemme i malene i [K29](K29-cnil-pia-maler.md): **P** = grunnprinsipper (2.1 proporsjonalitet), **R** = rettigheter (2.2), **D** = data-spesifikke sikkerhetstiltak (3.1 A), **G** = generelle sikkerhetstiltak (3.1 B), **O** = organisatoriske tiltak (3.1 C).

#### Oversikt

| Kap. | Tiltak | Mal | Side |
|---|---|---|---|
| 2 | Anonymisering | D | 11 |
| 3 | Arkivering | D | 12 |
| 4 | Kryptering (generelt, symmetrisk, asymmetrisk, utstyr, database, partisjon/container, filer, e-post, kanal) | D | 14 |
| 5 | Partisjonering av data | D | 18 |
| 6 | Fysisk adgangskontroll | G | 19 |
| 7 | Integritetsovervåking (hash, MAC, e-signatur) | D | 21 |
| 8 | Logisk tilgangskontroll (privilegier, autentisering, sertifikater, legitimasjon) | D | 24 |
| 9 | Lagringstid: begrenset | P | 29 |
| 10 | Holde risikokilder på trygg avstand | G | 31 |
| 11 | Retten til begrensning og retten til å protestere | R | 32 |
| 12 | Retten til retting og sletting | R | 35 |
| 13 | Innsynsrett og dataportabilitet | R | 37 |
| 14 | Formål: spesifisert, uttrykkelig og legitimt | P | 39 |
| 15 | Behandlingsgrunnlag, forbud mot misbruk | P | 40 |
| 16 | Forhåndsformaliteter | – | 42 |
| 17 | Håndtering av hendelser og brudd | O | 43 |
| 18 | Personalforvaltning | O | 45 |
| 19 | Forvaltning av arbeidsstasjoner (generelt, mobile enheter, smarttelefoner) | G | 46 |
| 20 | Prosjektstyring (generelt, programvareanskaffelse) | O | 51 |
| 21 | Risikostyring | O | 53 |
| 22 | Informasjon til de registrerte | R | 56 |
| 23 | Bekjempelse av skadevare | G | 60 |
| 24 | Vedlikehold | G | 61 |
| 25 | (tomt kapittel i kilden) | – | 63 |
| 26 | Dataminimering | P | 63 |
| 27 | Organisering | O | 67 |
| 28 | Policy (regelstyring) | O | 68 |
| 29 | Beskyttelse mot ikke-menneskelige risikokilder | G | 69 |
| 30 | Datakvalitet | P | 71 |
| 31 | Samtykke | R | 72 |
| 32 | Forhold til tredjeparter | O | 76 |
| 33 | Sikkerhetskopiering | G | 78 |
| 34 | Databehandlere: identifisert og regulert i avtale | R | 80 |
| 35 | Tilsyn (supervision) | O | 82 |
| 36 | Overvåking/logging av sikkerhetshendelser (surveillance) | G | 83 |
| 37 | Driftssikkerhet | G | 86 |
| 38 | Sikkerhet i datakanaler (nettverk) | G | 88 |
| 39 | Sikkerhet for papirdokumenter | D | 95 |
| 40 | Maskinvaresikkerhet | G | 98 |
| 41 | Nettstedsikkerhet | G | 102 |
| 42 | Overføringer ut av EU | R | 103 |
| 43 | Sporbarhet (logging) | D | 104 |

#### 2 Anonymisering (s. 11)
**Formål:** fjerne identifiserende kjennetegn.
- Bestem hva som må anonymiseres ut fra kontekst, lagringsform (databasefelt, tekstutdrag m.m.) og identifiserte risikoer.
- Anonymiser permanent de data som krever det, tilpasset dataformen.
- Hvis permanent anonymisering ikke er mulig: velg verktøy (delvis sletting, kryptering, hashing, nøkkelbasert hashing, indeks m.m.) som best møter funksjonsbehovene.

#### 3 Arkivering (s. 12–13)
**Formål:** prosedyrer for å bevare og forvalte elektroniske arkiver slik at deres (rettslige) verdi sikres gjennom hele perioden (overføring, lagring, migrering, tilgjengelighet, eliminering, arkivpolicy, konfidensialitet).
- Bekreft at arkivprosessene er definert – skill overføring, lagring, forvaltning av beskrivende data, konsultasjon/kommunikasjon og administrasjon (forhold til opprinnelseskontor, teknologisk/juridisk overvåking, oppgradering og migrering av medier og formater).
- Bekreft at arkivrollene er identifisert – opprinnelseskontor, avleverende enheter, arkivmyndighet (bevaring), kontrollorgan (vitenskapelig/teknisk kontroll av offentlige arkiver).
- Bekreft at tiltakene sikrer identifikasjon og autentisering av arkivets opprinnelse, integritet, forståelighet, lesbarhet, tilgjengelighet, bevaringstid og sporbarhet av operasjoner (overføring, konsultasjon, migrering, sletting). Anbefaling: egne tilgangsmetoder for arkiverte data; krypter arkivene og planlegg sikker re-kryptering med nye nøkler før nøklenes levetid utløper; planlegg utskifting av foreldede medier; prosedyre som sikrer at hele arkivet destrueres.
- Bestem metoder for konfidensialitet basert på risiko – krypter systematisk arkiverte sensitive data (DP-Act art. 8 og 9).
- Bekreft at arkivmyndigheten har en arkivpolicy (AP) – rettslige, funksjonelle, operasjonelle og tekniske begrensninger.
- Bekreft at det finnes en erklæring om arkivpraksis (DAP) – prosedyrer for å oppnå AP-målene.
- Verktøy: ANSSI-arkivguide, NF Z42-013, Archives de France.

#### 4 Kryptering (s. 14–17)

**4.1 Generelt** – Formål: gjøre data uforståelige for alle uten tilgangsrett (symmetrisk/asymmetrisk, offentlige algoritmer kjent som sterke, sertifikater).
- Bestem hva som skal krypteres (hel disk, partisjon, container, enkeltfiler, databasedata, kommunikasjonskanal) ut fra lagringsform, risiko og ytelseskrav.
- Velg type (symmetrisk/asymmetrisk) ut fra kontekst og risiko.
- Bruk løsninger basert på offentlige algoritmer kjent som sterke; anbefaling: sertifiserte/kvalifiserte verktøy (ANSSI førstenivå-sertifisering).
- Sikre tilgjengelighet, integritet og konfidensialitet for informasjon nødvendig for å gjenopprette tapte hemmeligheter (administratorpassord, gjenopprettings-CD).
- Verktøy: RGS, funksjonen «Confidentiality».

**4.2 Symmetrisk** – én nøkkel per formål; anerkjent mekanisme – anbefaling: RGS-kompatibel, f.eks. AES, blokkstørrelse minst 128 bit, ikke-deterministisk modus (f.eks. CBC med tilfeldig IV), nøkkellengde tilpasset levetid (f.eks. minst 128 bit for konfidensialitet til 2020), ikke svake nøkler; dokumenter nøkkelhåndtering (prosedyre).

**4.3 Asymmetrisk** – én nøkkel per formål; anerkjent mekanisme med sikkerhetsbevis (RGS, f.eks. RSAES-OAEP; nøkkelstyrke tilsvarende minst 128 bit til 2020); generer nøkler etter RGS (registrert sertifikatleverandør); verifiser sertifikater (formålsangivelse, gyldighet, ikke tilbakekalt, korrekt sertifikatkjede); beskytt nøkkelgenerering og -bruk etter nivå i hierarkiet (rotnøkler: delte hemmeligheter, bankboks); dokumenter i en «certification policy» (ansvar, identifikasjon/autentisering, livssykluskrav, sikkerhetstiltak, sertifikat- og CRL-profiler, revisjoner).

**4.4 Utstyr** – Formål: redusere risiko ved gjenfinning av utstyr (arbeidsstasjon, server, flyttbare medier). Krypter på maskinvarenivå (SED-disker) eller OS-nivå (partisjon/container) – f.eks. dm-crypt, FileVault, VeraCrypt. Ikke lagre nøkler på utstyret som krypteres med mindre sikker lagring brukes (TPM).

**4.5 Database** – Formål: beskytte mot tyveri av server, uautorisert fysisk tilgang og direkte tilgang fra administratorer. Krypter lagringsområdet (maskinvare-, OS- eller databasenivå) og/eller selve dataene (applikasjonskryptering) for konfidensialitet også overfor administratorer; ved adskilte IT-team kan databasekryptering gi tilgang kun for databaseadministratorer, ikke systemadministratorer.

**4.6 Partisjoner/containere** – krypter på OS-nivå (partisjon, katalog, fil) eller med spesialprogramvare (container) – f.eks. VeraCrypt, Zed!.

**4.7 Enkeltfiler** – krypter lagrede filer og e-postvedlegg – f.eks. ZoneCentral, Security BOX, AxCrypt, GPG; ellers minst komprimeringsverktøy med passordkryptering (7-Zip med AES) eller maskinvareløsning.

**4.8 E-post** – krypter e-post (f.eks. GPG) mot avlytting.

**4.9 Kommunikasjonskanal** – krypter kanalen mellom autentisert server og klient: tjenestesertifikat etter RGS og TLS (tidligere SSL; vurder passord på privat nøkkel og strenge tilgangsrettigheter), eller SSH-tunnel (VPN) eller IPsec-VPN.

#### 5 Partisjonering av data (s. 18)
**Formål:** redusere mulighet for sammenstilling og for omfattende brudd (identifiser datasett per virksomhetsområde og skill dem logisk).
- Identifiser de data hver forretningsprosess trenger – gi kun tilgang til nødvendige data (f.eks. statistikkavdelingen får ikke navn).
- Skill data logisk per prosess – tilgangsrettigheter per prosess (lønn, ferie, karriere); eget IT-miljø for de mest sensitive data.
- Kontroller jevnlig at partisjoneringen virker og at nye mottakere/sammenkoblinger ikke er lagt til.

#### 6 Fysisk adgangskontroll (s. 19–20)
**Formål:** begrense uautorisert fysisk tilgang (liste over autoriserte, autentisering av ansatte og besøkende, adgangslogg, alarm).
- Del bygget i soner etter risiko: publikumssone (resepsjon, venterom, møterom), tjenestesone (kontorer der data behandles, kontrollert adgang), sikkerhetssone (servere, nettverksadministrasjon, aktive nettverkskomponenter, strøm- og teleutstyr).
- Hold oppdatert liste over hvem (besøkende, ansatte, praktikanter, leverandører) som har adgang til hver sone; gjennomgå rettigheter til sikkerhetssoner jevnlig.
- Autentisering av ansatte proporsjonal med risiko: lav risiko – resepsjonist; høyere – adgangsport/proximity-kort med bilde og/eller ansattnummer; kortet skal være synlig.
- Autentisering av besøkende proporsjonal med risiko: høy risiko – mottakspolicy etter forhåndsavtalt tidsplan, ID-kontroll, kort gyldig kun under besøket.
- Definer handlinger ved feilet autentisering – nekt adgang, varsle sikkerhetsansvarlig.
- Før adgangslogg etter å ha informert de registrerte – registrer identitet, dato og tid inn/ut; logg som ikke går mer enn **tre måneder** tilbake.
- Besøkende utenfor publikumssoner skal eskorteres hele tiden.
- Beskytt de mest sensitive sonene – låst dør, kodelås eller videotelefon; bytt koder jevnlig; tydelig skilting; sikre åpninger (gitter på vinduer i bakkeplan, forsterkede dører).
- Installer innbruddsalarm – deteksjon av åpninger/inntrengning med sentral varsling (vakt og eksterne tjenester), særlig i sikkerhetssoner; CCTV for de mest sensitive sonene.
- Verktøy: system for å forsinke inntrengere og for inngripen før de forlater sonen.

#### 7 Integritetsovervåking (s. 21–23)

**7.1 Generelt** – Formål: varsles ved uønsket endring eller forsvinning (hash, MAC, e-signatur, hindre SQL-injeksjon).
- Identifiser data som må integritetsovervåkes ut fra risiko.
- Velg metode ut fra kontekst og robusthet: **hash** mot feil; **MAC** mot feil og endring fra personer uten nøkkel; **elektronisk signatur** mot feil og endring fra andre enn signataren.
- Bestem når funksjonen anvendes og kontroll skjer – f.eks. fingeravtrykk ved registrering, nytt ved hver visning, visuell advarsel ved avvik (gjenopprett fra sikkerhetskopi).
- Ved innlegging i database: tiltak mot skripting/SQL-injeksjon – hindre spesialtegn og SQL-setninger, filtrer eller krypter før lagring, begrens inndatavolum.

**7.2 Hashfunksjon** – RGS-kompatibel, f.eks. **SHA-256**; send fingeravtrykket via annen kanal eller signert (e-post), eller lagre det sikkert (sikkerhetskopi, arkiv, lagring).

**7.3 MAC** – RGS-kompatibel, f.eks. «retail» CBC-MAC med AES og to separate nøkler.

**7.4 Elektronisk signatur** – én nøkkel per formål; sertifiserte/kvalifiserte verktøy; RGS-mekanismer som RSA-SSA-PSS eller ECDSA med kurvene P-256, P-384, P-521, B-283, B-409 eller B-571; nøkler fra registrert sertifikatleverandør (RGS v2); verifiser sertifikater; beskytt nøkkelgenerering; dokumenter i certification policy. Merknad: smartkort som signaturenhet bør brukes med kortleser med innebygd PIN-tastatur.

#### 8 Logisk tilgangskontroll (s. 24–28)
**Formål:** begrense uautorisert elektronisk tilgang (brukerprofiler, autentisering, passordpolicy).

**8.1 Forvaltning av tilgangsrettigheter**
- Forvalt profiler med oppgave- og ansvarsdeling (helst sentralt), etter **tjenstlig behov (need-to-know) og minste privilegium**; tildel profil ved ansettelse og ved stillingsendring.
- Unik identifikator for alle med legitim tilgang (ansatte, kontraktsparter, tredjeparter).
- Generiske/delte identifikatorer kun med toppledelsens godkjenning og sporing (oppmøteliste, aktivitetsregister).
- Begrens tilgang til administrasjonsverktøy og -grensesnitt; begrens bruk av høyprivilegerte kontoer; «administrator»-kontoer kun for IT-avdelingen og administrasjonsoppgaver – administratorer bruker begrenset konto til e-post og nettlesing.
- Hver konto, særlig privilegerte, har eget passord; administratorkontoer individuelle.
- Logg bruk av privilegier (se kap. 43).
- **Årlig gjennomgang** av rettigheter: slett ubrukte kontoer, juster rettigheter.
- Trekk tilbake rettigheter når tilgang ikke lenger er autorisert eller kontrakten opphører; juster ved jobbskifte; midlertidige kontoer (praktikanter, leverandører) med utløpsdato.

**8.2 Autentisering**
- Velg metode etter kontekst, risiko og robusthet: lav risiko – passord; høyere – engangspassord-token (bytt standard aktiveringspassord), del av passord via SMS, kort med PIN, elektronisk sertifikat eller annen sterk autentisering.
- Passord skal aldri stå ukryptert i programmer, filer, skript, spor/logger eller på skjermen.
- Handlinger ved feilet autentisering: **sperr kontoen etter fem mislykkede forsøk**, øk ventetiden mellom forsøk; logg lokal tilgang.
- Begrens autentisering med brukernavn/passord til arbeidsstasjonen (opplåsing); autentiser arbeidsstasjonen mot servere med kryptografiske mekanismer.
- Merknader: sterk autentisering = minst to faktorer (noe man vet, har, er). I dårlig sikrede miljøer (delte arbeidsstasjoner): ekstra autentisering til applikasjonen. Biometri krevde CNIL-forhåndsgodkjenning etter DP-Act; CNIL anbefaler «sporløs» biometri (håndkontur, venemønster) eller fingeravtrykk lagret på personlig enhet.
- Verktøy: RGS «Authentication»; NAC-løsninger ved mange brukere.

**8.3 Autentisering med elektroniske sertifikater** – som 7.4: én nøkkel per formål, sertifiserte verktøy, RSA-SSA-PSS/ECDSA, nøkler fra godkjent leverandør (RGS v1.0), sertifikatverifisering, nøkkelbeskyttelse, certification policy.

**8.4 Forvaltning av legitimasjon (credentials)**
- Passordpolicy, automatisk håndhevet der mulig, og kommunisert til brukerne. Anbefaling: **minst 8 tegn**; byttes ved minste mistanke om kompromittering og eventuelt periodisk (hver 6. eller 12. måned); minst 3 av 4 tegntyper (store, små, tall, spesialtegn); de **5 siste** passordene kan ikke gjenbrukes; ikke samme passord for ulike tilganger; ikke knyttet til personopplysninger (navn, fødselsdato).
- Egen passordpolicy for administratorer – i tråd med CNIL-delib. 2017-012 (19.1.2017); aldri samme passord flere steder; programvare skal ikke huske passord; maks antall forsøk før varsel og sperring.
- Bytt standardpassord straks etter installasjon.
- Unikt tilfeldig initialpassord per konto, overført sikkert (to kanaler eller skrapefelt), byttes ved første innlogging og ved nytt passord.
- Lagre autentiseringsinformasjon (passord, private nøkler) kun tilgjengelig for autoriserte – minst mulig tilgangsrettigheter, krypter passordfiler; deponer administrasjonslegitimasjon i safe/låst skap.
- Ved mange hemmeligheter: sentral autentiseringsløsning med OTP eller sikker passordhvelv – robust hovedpassord, lagring som ikke kan gjenopprettes uten hemmeligheten, maskert visning, motstand mot dekryptering/brute force/replay, automatisk lukking/sperring.
- Når en administrator slutter: deaktiver individuelle kontoer og bytt alle administrasjonspassord vedkommende kjente (funksjonelle, generiske, tjenestekontoer).
- Merknader: huskeregler for komplekse passord (første bokstav i hvert ord i en setning osv.); slett all biometrisk autentiseringsdata i adgangssystemer [ved opphør].
- Verktøy: CERTA-notat om passord.

#### 9 Lagringstid: begrenset (s. 29–30)
**Formål:** DP-Act art. 6 og 36, GDPR art. 5 nr. 1 e; redusere alvorlighet ved å ikke lagre data lenger enn nødvendig.
- Definer tidsbegrenset lagringstid per datakategori tilpasset formål og/eller lovkrav; skill vanlige data, arkiverte data (tilgang kun for berørte), funksjonelle spor og logger.
- Behandlingen skal kunne oppdage utløpt lagringstid – automatikk basert på opprettelses- eller sist brukt-dato; hver opplysning bør ha en dato for når den skal slettes.
- Sletting når lagringstiden utløper, med metode tilpasset risikoen – **logisk sletting (statusflagg der data fortsatt kan leses i databasen) er ikke tilstrekkelig**. God praksis: mellomlagringstid der data først er tilgjengelig for alle, deretter kun for en begrenset krets (f.eks. 6 måneder for alle, så kun tvisteavdelingen).
- Ved utløp (etter eventuell mellomarkivering): slett umiddelbart – automatisk arkivering/sletting også av logger og spor; ved manuell sletting skal verktøyet ha massesletting. Der konteksten tillater det kan brukeren forlenge lagringstiden; standard er sletting ved planlagt utløp.
- Merknader: formålet rettferdiggjør normalt ikke lagring i påvente av politi- eller rettssak utover lovens frister, men enkelte sektorer har lagringsplikt (telekom, flypassasjerdata). Arkivering og sletting begrenser konsekvensene ved tyveri eller utilsiktet spredning.

#### 10 Holde risikokilder på trygg avstand (s. 31)
**Formål:** hindre at menneskelige og ikke-menneskelige risikokilder skader dataene (farlige produkter, farlige områder, overføring ut av EU).
- Lagre farlige produkter (brennbare, etsende, eksplosive, aerosoler, våte artikler) i egnede rom på trygg avstand fra databehandlingsområder.
- Unngå farlige geografiske områder (flomsoner, nær flyplasser, kjemisk industri, jordskjelv- og vulkansoner).
- Ikke lagre data i utlandet uten garantier: adekvat land (nevner Canada, Sveits, Argentina, Guernsey, Jersey, Isle of Man), EU-standardkontrakter, BCR, Privacy Shield for USA, eller unntak i DP-Act art. 69. Behandlingsansvarlig forblir ansvarlig for sikkerheten.

#### 11 Retten til begrensning og retten til å protestere (s. 32–34)
**11.1 Generelt** – Formål: DP-Act art. 38, GDPR art. 18 og 21; sikre at personer kan protestere mot bruk av sine data; la den registrerte «fryse» behandlingen mens legitimiteten kontrolleres; kontroller om unntak gjelder (rettslig plikt, tvingende berettigede grunner, rettskrav, allmenn interesse).
- Bestem praktiske midler: så raskt som mulig, **innen to måneder uten unntak**, i samme form som behandlingen (post og/eller e-post), ikke avskrekkende og uten kostnad.
- Sikre at retten alltid kan utøves og at dataene faktisk muliggjør det – analyser når midlene ikke virker og ha reserveløsninger.
- Den registrerte skal kunne gjøre sitt valg før endelig validering av sine svar (DP-Act art. 96).
- ID-kontroll ved oppmøte (også av fullmektig); per post: signert, kopi av legitimasjon (ikke lagres med mindre bevis må beholdes), svaradresse; per e-post (kryptert kanal over Internett): digitalisert legitimasjon (ikke lagret, eller i sort-hvitt, lav oppløsning, kryptert).
- Sikre at legitime grunner oppgis og vurderes (unntatt markedsføring og helseforskning, der retten til å protestere er skjønnsmessig/ubetinget).
- Varsle alle mottakere om protester (DP-Decree art. 97).
- Merknad: retten til begrensning lar den registrerte fryse behandlingen som beskyttelsestiltak.

**11.2 Telefon** – protest ved tastetrykk. **11.3 Elektronisk skjema** – lett tilgjengelig skjema med opt-out-bokser eller avmelding (slett konto). **11.4 E-post** – tydelig identifisert avsender; innhold som samsvarer med emnet; protest ved svar eller lenke, uten krav om å identifisere seg.

**11.5 Tilkoblet objekt eller mobilapp** – «Privacy»-innstillinger (mulighet til å endre standard; tilgjengelig ved første aktivering og senere via egen meny); mulighet til å protestere mot innsamling av spesielle data (varsle med ikon/lys når appen kjører i bakgrunnen, mikrofonen «lytter», lokasjon samles inn, og la brukeren protestere); ta hensyn til mindreårige (foreldrekontroll; ekskluder barn under 13 fra automatisert profilering); stopp innsamling når samtykke trekkes.

**11.6 Forskning med identifiserbare biologiske prøver (DNA)** – ved videre behandling som avviker fra den opprinnelige: rett til å protestere uten krav om begrunnelse.

#### 12 Retten til retting og sletting (s. 35–36)
**12.1 Generelt** – Formål: DP-Act art. 40, GDPR art. 16, 17 og 19; rette, supplere, oppdatere, sperre eller slette; kontroller unntak (DP-Act art. 41: nasjonal sikkerhet, forsvar, offentlig sikkerhet; GDPR art. 17: ytrings- og informasjonsfrihet, rettslig plikt, allmenn interesse, folkehelse, forskning/statistikk, rettskrav).
- Praktiske midler: innen to måneder, samme form som behandlingen, ikke avskrekkende, kostnadsfritt.
- Sikre at retten alltid kan utøves – reserveløsninger; klare instruksjoner og enkle steg for å slette data ved salg eller kassering av enhet; sletting ved tyveri av enhet.
- ID-verifisering (som kap. 11; også fullmektiger og arvinger etter avdød).
- Verifiser at rettelser er korrekte; sikre at slettede data faktisk slettes; bekreft overfor den som ba om det; informer tredjeparter som har mottatt dataene.
- Ved sletteanmodning: informer om data som likevel lagres (tekniske krav, rettslige plikter).
- Retten til å bli glemt for mindreårige: en internettbruker under 18 kan, ved publisering eller opprettelse av konto, uten begrunnelse kreve sletting snarest mulig (unntak: informasjonsfrihet, allmenn interesse, rettslig plikt).
- Merknad: **én måned** til å slette eller svare; deretter kan saken bringes inn for CNIL.
- **12.2 Målrettet nettreklame** – gi tilgang til interesseområdene i profilen og mulighet til å endre dem; autentisering via kontoinnlogging eller informasjonskapsel.

#### 13 Innsynsrett og dataportabilitet (s. 37–38)
**13.1 Generelt** – Formål: GDPR art. 15 og 20; kjenne sine data; hente ut data man har gitt i et lett gjenbrukbart format; unntak (statistikk/forskning uten personvernrisiko, nasjonal sikkerhet; ingen portabilitet for behandling i allmennhetens interesse/offentlig myndighet eller av hensyn til andres rettigheter).
- Praktiske midler: så raskt som mulig, innen to måneder (**én måned etter GDPR**), samme form, ikke avskrekkende, ikke kostnad utover kopieringskostnad. Anbefaling: informer om status (mottatt, forventet svardato); ved arkiver kan svarfristen forlenges hvis den registrerte informeres og en rimelig frist gis.
- Reserveløsninger; ID-kontroll som kap. 11.
- Sikre at all informasjon kan gis samtidig som tredjeparters personopplysninger beskyttes.
- Verktøy: DP-Act art. 92–95 og 98; CNIL-guide for arbeidsgivere.

**13.2 Medisinske journaler** – gi informasjon innen 8 dager etter forespørsel, og innen 2 måneder hvis informasjonen er over 5 år gammel; foreldre (mindreårige) og verger kan utøve innsynsrett (DP-Act art. 58).

#### 14 Formål: spesifisert, uttrykkelig og legitimt (s. 39)
**Formål:** DP-Act art. 6, GDPR art. 5 nr. 1 b; hindre uforenlig bruk og misbruk.
- Beskriv formålene i detalj og begrunn legitimiteten.
- Forklar formål med deling med tredjeparter og formål om tjenesteforbedring.
- Forklar særlige vilkår for behandlingen, særlig sammenstilling av data.

#### 15 Behandlingsgrunnlag, forbud mot misbruk (s. 40–41)
**Formål:** GDPR art. 6.
- Bestem og begrunn behandlingsgrunnlaget (samtykke; avtale; rettslig plikt; vitale interesser; allmenn interesse/offentlig myndighet; berettiget interesse – unntatt der den registrertes interesser går foran, særlig barn).
- Merknader: ved rettslig plikt/allmenn interesse – angi rettsgrunnlaget i unionsretten eller nasjonal rett. Det kan være flere grunnlag, f.eks. **avtale** for produktets primærformål og **samtykke** for sekundærformål (tjenesteforbedring, markedsføring) innhentet ved aktivering.
- Viderebehandling uten samtykke eller lovhjemmel – forenlighetsvurdering (GDPR art. 6 nr. 4): kobling mellom formålene; konteksten for innsamlingen (forholdet til behandlingsansvarlig); opplysningenes art (særlige kategorier, straffedommer); mulige konsekvenser for de registrerte; nødvendige garantier (kryptering, pseudonymisering).

#### 16 Forhåndsformaliteter (s. 42)
- Meld behandlingen til CNIL før iverksetting (fransk ordning før GDPR).
- Kontroller at behandlingen samsvarer med meldt formål.
- Gjennomfør en PIA og få den validert.
- **Konsulter CNIL hvis residual risiko er høy (GDPR art. 36).**
- Gjennomfør andre sektorielle og kontraktuelle formaliteter.
- Verktøy: CNILs PIA-metode og -guider; WP29-retningslinjer om DPIA.

#### 17 Håndtering av hendelser og brudd (s. 43–44)
**Formål:** operativ organisasjon som kan oppdage og håndtere hendelser som påvirker de registrerte (ansvar, responsplan, kvalifisering av brudd).
- Definer roller, ansvar og prosedyrer for tilbakemelding og respons – formaliser ansvar for personvernombud/DPO, samhandling med CNIL og de registrerte; kriseteam ved skadelig hendelse.
- Katalog over personer ansvarlige for bruddhåndtering.
- Responsplan for hver høy risiko, oppdatert og testet periodisk – **test minst hvert annet år**.
- Kategoriser brudd etter konsekvens for de registrerte:

| Kategori | Definisjon | Håndtering |
|---|---|---|
| Hendelse (event) | Brudd uten konsekvenser | Registrer og varsle DPO |
| Incident | Brudd med isolerte konsekvenser | Løs det; varsle berørte registrerte der relevant (ikke nødvendig hvis ikke høy risiko, eller hvis tekniske tiltak – f.eks. kryptering – gjør dataene uforståelige for uautoriserte) |
| Skadelig hendelse (damaging event) | Brudd med betydelige, umiddelbare konsekvenser for én eller flere | I tillegg: start dybdeanalyse |
| Krise | Brudd med betydelige, mer langsiktige konsekvenser for én eller flere | I tillegg: iverksett etablert krisehåndteringsplan |

- Før oppdatert dokumentasjon over brudd (GDPR art. 33 nr. 5) – kontekst, kategori og antall berørte registrerte og poster, virkninger, tiltak.
- Analyser muligheten for å forbedre sikkerhetstiltak etter brudd.
- Merknader: «Telecoms Package» (2009, fransk lov 2011) innførte meldeplikt for teleoperatører; GDPR utvider til alle behandlingsansvarlige. Underretning av de registrerte (ved høy risiko) skal minst beskrive bruddets art, kontaktpunkt og anbefalte tiltak for å redusere negative virkninger; melding til tilsynsmyndigheten skal også beskrive konsekvensene og tiltak, og er nødvendig så snart bruddet medfører risiko for rettigheter og friheter. Andre meldeplikter gjelder i tillegg. Viktig å kunne sikre og fremlegge bevis.
  - **[Merknad – ikke fra kilden]** Etter GDPR skal underretningen av de registrerte (art. 34 nr. 2) også beskrive de sannsynlige konsekvensene av bruddet (art. 33 nr. 3 bokstav b–d gjelder for begge). Melding til tilsynsmyndigheten kan bare unnlates dersom bruddet sannsynligvis ikke vil medføre en risiko, og skal skje uten ugrunnet opphold og om mulig senest 72 timer etter at den behandlingsansvarlige fikk kjennskap til bruddet (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33)).
- Verktøy: CLUSIF-prosedyre for ofre, CERTA-notat om inntrenging, direktiv 2009/136/EF, GDPR art. 33 og 34.

#### 18 Personalforvaltning (s. 45)
**Formål:** redusere risiko for at egenskaper ved personer utnyttes (kompetanse, ressurser, bevisstgjøring).
- Sikre at personer med tilgang er kvalifiserte – ellers opplæring.
- Sikre tilfredsstillende arbeidsforhold – tilstrekkelige ressurser for oppgavene.
- Bevisstgjør om risiko ved egne sårbarheter: ondsinnede kan utnytte personer som snakker for mye, er forutsigbare, lett påvirkelige eller lett manipulerbare.
- Ved endringer (nye tjenester, verktøy, arbeidsmetoder): tiltak for å støtte omstillingen.

#### 19 Forvaltning av arbeidsstasjoner (s. 46–50)
**19.1 Generelt** – Formål: redusere risiko for at egenskaper ved programvare utnyttes.
- IT-avdelingen leverer sikre, fungerende arbeidsstasjoner; tyverisikringskabler for bærbare der lokalene ikke er fysisk sikret.
- Hent ut data (unntatt private) før arbeidsstasjoner omdisponeres; slett data før omdisponering eller ved deling; slett midlertidige data ved hver pålogging på delte maskiner.
- Ved kompromittering: undersøk alle spor av inntrenging for å avgjøre om annen informasjon er kompromittert.
- Hold systemer og applikasjoner oppdatert, eller isoler maskinen og overvåk logger nøye der det ikke er mulig – bruk vedlikeholdte versjoner, ukentlig automatisk sjekk, test oppdateringer før utrulling, sørg for tilbakerulling, sjekk lisenser.
- Dokumenter konfigurasjoner (herdingsprosedyrer, lenker for sikkerhetsoppdateringer).
- Reduser misbruksmuligheter: minste privilegium; IP-adresser kun der nødvendig; deaktiver unødvendige tjenester og kontoer (gjest, leverandørkontoer); blokker fjerndiagnose-/konfigurasjonsporter; deaktiver autorun; boot kun fra lokal disk.
- Beskytt tilgangspunkter: BIOS-passord, bytt standardpassord, passordbeskyttet skjermsparer (**5 min ved vedlikehold, maks 15 min ved vanlig bruk**), vis siste innlogging.
- Aktiver innebygd beskyttelse (innloggingspassord, brannmur, automatiske oppdateringer, skadevarebeskyttelse, applikasjonstilgangskontroll).
- Forby lokal deling av kataloger; lagre brukerdata på sikkerhetskopiert nettverksområde; ved lokal lagring: synkronisering/backup-midler.
- Sikre nettleserkonfigurasjon (beskytt lagrede skjema/passord/sertifikater; hovedpassord; forby passordlagring ved høy risiko); sikker nettleser på servere med nettilgang; minst mulig plugins, oppdatert; forby applikasjoner fra usikre kilder.
- Søk etter sårbarheter (overvåking, skanneverktøy som Nmap og Nikto, HIPS); integritetskontroll (Tripwire, Spybot, Rootkit Revealer).
- Logg: tilstrekkelig loggstørrelse (eldste hendelser skal ikke overskrives automatisk); logg applikasjons-, sikkerhets- og systemhendelser (innlogging med ID, tid, utfall, utlogging; endringer i sikkerhet/privilegier/kontoer; stopp/start av sensitive prosesser; tilgang/endring av systemdata; mislykket ressurstilgang; sensitive operasjoner; sikkerhetsrettinger; administrasjon og fjernstyring; antiviruslogger); eksporter via domene eller syslog; analyser innloggingstider, protokoll, brukertype, IP, gjentatte feil, uplanlagte avbrudd.
- Verktøy: signer kjørbar kode for internt utviklede, verdifulle applikasjoner; signaturkontroll under kjøring.

**19.2 Mobile enheter** – krypter lagrede data (hel disk fysisk/logisk, enkeltfiler, containere); minimer data og forby lagring ved utenlandsreiser ved behov; sikre tilgjengelighet (kopier til annen maskin/server snarest); slett fra enheten når data er lagt inn i organisasjonens system; personvernfilter utenfor organisasjonen. Merknader: fingeravtrykkslesere krevde CNIL-godkjenning; diskkryptering skal ikke kunne slås av, og nøkkelkopi skal bevares. Verktøy: ANSSI-guide for reisende.

**19.3 Mobiltelefoner/smarttelefoner** – konfigurer før utlevering (autolås etter **1–5 minutter**, kryptert minnekort, fjernlåsing/-sletting, begrenset installasjon av apper); informer brukerne (memo: ikke senke sikkerhetsnivået, ikke åpne e-post fra ukjente, ikke lagre sensitive filer, tøm cache/cookies, meld hendelser straks, kun programvare fra pålitelige kilder); sikre serveren (egen DMZ/VLAN, antivirus/antispam, sikkerhetsoppdateringer, sertifikatautentisering av enheter); sikre telefoner ved livsløpsslutt (slett alle data og innstillinger, demonteringsprosedyre). Strengere tiltak ved høy risiko: blokker vedlegg; trafikkanalyse; verifiser kryptering; ingen lokal lagring/nettilgang til sensitive data; ikke send sensitive filer per e-post; ende-til-ende-kryptert SMS; hviteliste av apper; jevnlig reinstallasjon av testet image.

#### 20 Prosjektstyring (s. 51–52)
**20.1 Generelt** – Formål: integrere personvern i alle nye behandlinger.
- Bruk CNILs risikostyringstilnærming fra tjenesten/applikasjonen designes.
- Foretrekk «trusted names» innen informasjonssikkerhet og personvern (prosedyrer, produkter, styringssystemer, organisasjoner, personer) – førstenivå-sertifisering, kvalifisering, ISO 27001-sertifisering, personsertifiseringer (CISSP, CISM, ISO 27001 Lead Auditor).
- Foretrekk anerkjente retningslinjer (internasjonale standarder, CNIL, ANSSI).
- Gjennomfør CNIL-formaliteter før oppstart.

**20.2 Programvareanskaffelse (kjøp, utvikling)**
- Tilstrekkelige ressurser for utviklere/forvaltere (klare spesifikasjoner, dokumentasjon, kompetanse).
- Foretrekk interoperable og brukervennlige applikasjoner.
- Utvikling i miljø adskilt fra produksjon (andre maskiner og rom).
- Beskytt tilgjengelighet, integritet og ev. konfidensialitet for kildekode.
- Inndata- og lagringsformater som minimerer data (f.eks. fødselsdato-felt som ikke tillater måned og dag – nedtrekksmeny).
- Dataformater som støtter lagringstid.
- Innebygd tilgangskontroll per brukerkategori.
- Unngå fritekstfelt; hvis nødvendig, vannmerketekst om innsynsrett, relevans og forbud mot subjektive vurderinger og sensitive opplysninger.
- **Forby bruk av reelle data før produksjon; anonymiser produksjonsdata ved akseptansetest**; slett sikkert alle enheter brukt til sensitive data.
- Sikre at programvaren virker som spesifisert ved akseptansetest.

#### 21 Risikostyring (s. 53–55)
**Formål:** styre risikoen behandlingene utgjør for de registrertes rettigheter og friheter.
- List behandlinger (automatiserte eller ikke), data og støtteressurser: maskinvare (HR-server, bærbar, CD-ROM), programvare (OS, fagsystem), kommunikasjonskanaler (fiber, Wi-Fi, Internett), papir (utskrift, kopi).
- Vurder hvordan grunnprinsippene (informasjon, samtykke, innsyn m.m.) respekteres.
- Vurder risiko for hver behandling:
  - konsekvenser for de tre risikoene: uautorisert tilgang (f.eks. identitetstyveri etter at alle lønnsslipper lekker), uønsket endring (f.eks. uriktig anklage etter endring av tilgangslogger), forsvinning (f.eks. legemiddelinteraksjon ikke oppdaget fordi pasientjournalen ikke er tilgjengelig);
  - risikokilder: interne/eksterne menneskelige, tilfeldige eller tilsiktede (IT-administrator, bruker, hacker, konkurrent); interne/eksterne ikke-menneskelige (vann, farlige materialer, ikke-målrettet virus);
  - trusler via støtteressurser som kan bli brukt upassende (misbruk av rettigheter, betjeningsfeil), endret (keylogger, utilsiktet skadevare), mistet (tyveri av PC, tap av USB), observert (skjerm på toget, foto av skjerm, geolokasjon), skadet (hærverk, slitasje), overbelastet (full lagring, DoS);
  - eksisterende/planlagte tiltak (tilgangskontroll, sikkerhetskopi, sporbarhet, lokalsikkerhet, kryptering, anonymisering);
  - estimer alvorlighet og sannsynlighet (skala: «negligible, moderate, significant, maximum» – merk avvik fra «limited» i §1.5).
- Dokumentasjonstabell:

| Risks | Impacts on data subjects | Main risk sources | Main threats | Existing or planned measures | Severity | Likelihood |
|---|---|---|---|---|---|---|
| Illegitimate access to personal data | | | | | | |
| Unwanted change of data | | | | | | |
| Disappearance of data | | | | | | |

- Implementer og kontroller planlagte tiltak.
- **Periodisk sikkerhetsrevisjon – årlig der mulig**, med handlingsplan fulgt opp på høyeste nivå.
- Oppdater risikokartet periodisk og ved større endringer – ved hver ny behandling og **minst årlig** av en dedikert komité.
- Verktøy: GDPR art. 35 nr. 7 (sitert); CNILs PIA-guider; informasjonssikkerhetsrisiko kan studeres samtidig med personvernrisiko; budsjett for tiltak; RGS; EBIOS.

#### 22 Informasjon til de registrerte (s. 56–59)
**22.1 Generelt** – Formål: DP-Act art. 32, GDPR art. 12–14; hindre innsamling uten kunnskap; kontroller unntak.
- Bestem og begrunn informasjonsmidlene (eller hvorfor umulig): presentasjon av og tilgang til vilkår for bruk/personvern; lesbare, forståelige vilkår; enhetsspesifikke klausuler; detaljerte formål (inkl. sammenstilling); detaljert liste over data; tilgang til enhetsidentifikatorer og om de deles med tredjeparter; rettigheter (trekke samtykke, sletting); sikker lagringsmetode (særlig ved utkontraktering); kontaktinformasjon; varsling om endringer; ved overføring til tredjeparter: formål, data og tredjepartenes identitet.
- Informasjonen skal være fullstendig, klar og tilpasset målgruppen – forståelig for personer uten IT-kunnskap.
- Gis senest ved innsamling; data skal ikke kunne samles inn uten informasjon (reserveløsninger).
- Mulighet til å bevise at informasjon er gitt (oppslag alle må ha sett, signatur/parafering).
- Merknader: individuelt (muntlig, pop-up) eller kollektivt (oppslag) hvis alle har lett tilgang. Innhold: behandlingsansvarliges identitet, formål, obligatorisk/frivillig, konsekvenser av ikke å svare, mottakere, rettigheter, ansvarlig for rettigheter, planlagte overføringer. Ved overføring til tilknyttede tredjeparter (datterselskaper, konsern, partnere): liste over mottakere i egen seksjon med datakategorier, formål og lenke til deres personvernerklæring, og intern prosess for å oppdatere listen.
- **22.2 Ansatte** – innhent forhåndsuttalelse fra ansattes representanter der arbeidsretten krever det; bruk egnet metode (oppslag, internmemo, e-post, skjema, arbeidsavtale, reglement, IT-reglement).
- **22.3 Nettsted** – direkte eller lett tilgjengelig informasjon på forsiden eller relevant seksjon.
- **22.4 Tilkoblet objekt/mobilapp** – melding ved første aktivering og deretter via egen meny; **QR-kode på enheten hvis den ikke har skjerm**; informer om tilgang til enhetsidentifikatorer og deling; om appen kan kjøre i bakgrunnen; om beskyttelse av tilgang til enheten.
- **22.5 Telefon** – automatisk melding før samtalen om rettigheter, formål med opptak (opplæring, kvalitet) og mulighet til å protestere; autentisering av innringer.
- **22.6 Skjema** – informasjonsteksten i samme skrifttype som resten.
- **22.7 Målrettet reklame** – synlig og lesbar informasjon om former for målrettet reklame, prosedyrer, kategorier av informasjon, hva som ikke samles inn og hvordan man samtykker; informasjon og samtykke **før** lagring av eller tilgang til informasjon i terminalutstyret.
- **22.8 Oppdatering av eksisterende behandling** – egen informasjon om nye formål eller mottakere.

#### 23 Bekjempelse av skadevare (s. 60)
**Formål:** beskytte tilgang til offentlige og ukontrollerte nett, arbeidsstasjoner og servere mot skadelig kode.
- Antivirus på servere og arbeidsstasjoner – sanntidsanalyse etter IT-avdelingens regler; brukeren kan ikke deaktivere eller endre; full automatisk skanning **minst ukentlig** med minimal forstyrrelse.
- Automatisk og regelmessig oppdatering av signaturer og motorer; nødoppdateringer.
- Filtrering av inn- og utgående trafikk (brannmur, proxy).
- Send antivirus-hendelser til sentral server for statistikk og etterhåndtering.
- Anti-spyware installert, konfigurert og oppdatert.

#### 24 Vedlikehold (s. 61–63)
**24.1 Generelt** – Formål: begrense trusler ved vedlikehold av maskin- og programvare.
- Avtale med leverandør som regulerer vedlikehold (se kap. 32); loggbok over alle vedlikeholdsoperasjoner.
- Styr fjernvedlikehold: krypterte kanaler, robuste nøkler/passord, logging.
- Krypter eller slett data på maskinvare som sendes til ekstern reparasjon; ellers fjern lagringsmedier eller gjør vedlikeholdet internt.

**24.2 Arbeidsstasjoner** – fjerntilgang kun med brukerens samtykke og synlig indikasjon på skjermen; ved fysisk inngrep på maskin med sensitive data – slett dataene under vedlikeholdet; konfigurer telefoner (som 19.3, styrt av et flåtestyringssystem / MDM); informer brukerne (meld tap, tyveri, unormal funksjon); slett alt før kassering/resirkulering.

**24.3 Lagringsmedier** – slett sikkert eller destruer kasserte medier (sertifisert sletteprogramvare, degausser eller spesialisert leverandør); fjerntilgang kun med brukerens samtykke.

**24.4 Multifunksjonsskrivere og kopimaskiner** – ved ekstern reparasjon: krypter/slett data før forsendelse; taushetserklæring eller reparasjon på stedet med IT til stede; forby forsendelse av utstyr med sensitive data. Ved fjernvedlikehold: taushetserklæring, individuelle robuste passord som byttes, oppringingstilgang kun ved behov og avslått som standard, logg, hindre «bouncing» videre til LAN/Internett. Ved kassering: sikkert rom, sikker sletting, fysisk destruksjon hvis sletting ikke er mulig, taushetserklæring fra destruksjonsfirma, **destruksjonsrapport oppbevart i 10 år**.

#### 26 Dataminimering (s. 63–66)
**26.1 Minimering av innsamling** – Formål: DP-Act art. 6, GDPR art. 5 nr. 1 c; redusere alvorlighet ved å begrense til det strengt nødvendige.
- Begrunn innsamlingen av hver opplysning.
- Skill klart mellom anonyme og pseudonyme data.
- Unngå fritekstfelt («kommentarer»); bruk nedtrekkslister; hvis uunngåelig – bevisstgjør brukerne (ingen krenkende ord, ingen ikke-meldte sensitive data).
- Bekreft at data er adekvate, relevante og ikke overdrevne – definer formålet, identifiser nødvendige data, vis hvorfor hver kategori er nødvendig, utelukk data som ikke hindrer formålet; revider formålet om nødvendig.
- Ikke samle inn særlige kategorier (GDPR art. 9) eller straffedommer (art. 10) unntatt i særlige tilfeller.
- Hindre innsamling av tilleggsdata – kun definerte felt; kontroller jevnlig at ingen ekstra data samles.
- Merknader: barns data – innsamling om barn, foreldre eller familie skal være særlig begrenset og begrunnet.

**26.2 Minimering av selve dataene** – redusere sensitiviteten:
- Filtrer og fjern unødvendige data (f.eks. **EXIF-metadata** i bilder).
- Reduser sensitivitet ved konvertering: slett IP-adresse når by/bydel er utledet; uskarp/blur personer i videoovervåking; smartmåler som aggregerer forbruk over en periode i stedet for sanntid.
- Reduser identifiserbarhet: 1) anonyme data (bruk uten å avsløre identitet), 2) pseudonyme data (bruk uten å avsløre identitet, men fortsatt identifiserbar og ansvarlig), 3) ikke-sammenkoblbarhet (flere bruk kan ikke kobles), 4) ikke-observerbarhet (andre kan ikke se at tjenesten brukes). Valget gjøres ut fra truslene; pseudonymisering kan være bedre enn anonymisering ved behov for sporbarhet; kombinasjoner er mulig.
- Reduser opphopning av data: uavhengige delsystemer med separat tilgangskontroll.
- Begrens tilgang: need-to-know, egne policyer for sensitive data, kryptering ved overføring og lagring, beskytt midlertidige filer/cookies.
- Begrens oversending av elektroniske dokumenter til dem som trenger dem.
- Slett sikkert data som ikke lenger trengs eller som den registrerte ber om slettet – også fra sikkerhetskopier der relevant (sikker sletting; degausser for magnetiske medier).

#### 27 Organisering (s. 67)
**Formål:** organisasjon som kan styre og kontrollere personvernet.
- Behandlingsansvarlig utpeker en person (DPO) som bistår med etterlevelse, med ressurser – stillingsbeskrivelse, menneskelige og økonomiske ressurser, direkte rapportering, organisatorisk og beslutningsmessig frihet, ingen interessekonflikt, informer ansattes representanter, konsultasjon med DPO før nye behandlinger.
  - **[Merknad – ikke fra kilden]** Plikten til å utpeke personvernombud gjelder bare i tilfellene i art. 37 nr. 1: offentlige myndigheter og organer, kjerneaktiviteter med regelmessig og systematisk overvåking i stor skala, eller behandling i stor skala av særlige kategorier eller opplysninger om straffedommer (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-37)).
- Definer roller, ansvar og samhandling: DPO-oppgaver (behandlingsoversikt, uavhengig etterlevelseskontroll, rapportering), skill administrator med tilgang til data fra administrator med tilgang til bruksspor, beskriv samspill mellom prosjekteiere, sikkerhetsleder og DPO, definer oppgaver i risikostyring, beskriv bruddhåndtering.
- Oppfølgingskomité (behandlingsansvarlig, DPO, interessenter) som møtes **minst årlig** for å sette mål og gjennomgå alle behandlinger.

#### 28 Policy (regelstyring) (s. 68)
**Formål:** dokumentbase med personvernmål og -regler.
- Samle personvernpolicy i form tilpasset innhold (risikoer, prinsipper, mål, regler) og målgruppe (brukere, IT, ledelse) – kravspesifikasjoner, ledelsesbrev, retningslinjer for IT-bruk, prosedyre for personvern i prosjekter.
- Distribuer til dem som skal håndheve den.
- Formell prosedyre for unntak: vurder risikovirkning, godkjenning av behandlingsansvarlig, oppdater policy.
- Flerårig handlingsplan med oppfølging; kontroller etterlevelse **minst årlig**; revider policy jevnlig.

#### 29 Beskyttelse mot ikke-menneskelige risikokilder (s. 69–70)
**Formål:** redusere/unngå risiko fra klima, brann, vann, ulykker, dyr.
- Brann: rydd lokalene, nok og riktige slokkeapparater (pulver, væske, gass), røyk- og varmedetektorer med sentral alarm, inertgass eller luftavtrekk i IT-rom.
- Temperaturovervåking: klimaanlegg med alarm ved terskeloverskridelse, sentral varsling.
- Strøm: aggregat eller UPS som håndterer kontrollert nedstengning og kontinuerlig drift, med alarm.
- Vannskade: IT- og teleutstyr **minst 15 cm over gulvet** i IT-rom i bakkeplan; avstand til vannrør, klimaanlegg, radiatorer.
- Dimensjoner essensielle tjenester (strøm, vann, kjøling) etter systemene.
- Responstid ved feil i vedlikeholdsavtaler for sikkerhetsutstyr; kontroller utstyret **minst årlig**.
- Høye tilgjengelighetskrav: minst to uavhengige telekomtilknytninger med rask omkobling; ved svært høye krav – reservested.
- Verktøy: CNPP, APSAD, NFPA.

#### 30 Datakvalitet (s. 71)
**Formål:** DP-Act art. 6, GDPR art. 5 nr. 1 d; unngå beregning på uriktige eller utdaterte data.
- Regelmessig kontroll av riktigheten av brukerens data.
- Be brukeren jevnlig kontrollere og oppdatere sine data.
- Sporbarhet av endringer.
- Merknad: kvalitetskravet gjelder også koblingen mellom identifiserende data og data om personen.

#### 31 Samtykke (s. 72–75)
**31.1 Generelt** – Formål: DP-Act art. 7, GDPR art. 7 og 8; fritt, spesifikt og informert valg; vurder om annet grunnlag gjelder.
- Bestem og begrunn midler (eller hvorfor umulig): uttrykkelig samtykke ved registrering; segmentert per datakategori/behandlingstype; uttrykkelig samtykke før deling med andre brukere; forståelig og lett tilgjengelig, klart språk tilpasset målgruppen (særlig barn); foreldresamtykke for barn under 13; nytt samtykke for ny bruker; bekreftelse etter lang tids inaktivitet; tydelig indikasjon (ikon, lys) når spesielle data (f.eks. lokasjon) behandles; samtykkeinnstillinger bevares ved kontraktsbytte.
- Samtykke før behandlingen starter (reserveløsninger).
- Fritt: et ikke for restriktivt alternativ må finnes, og ingen over-/underordningsforhold (f.eks. arbeidsgiver/arbeidstaker).
- Informert og transparent om formålene; spesifikt formål.
- Ved utkontraktering: hver parts forpliktelser i skriftlig avtale.
- Merknader: CNIL mener en arbeidstaker ikke kan samtykke fritt til behandling arbeidsgiveren setter opp. Praktiske samtykkehandlinger: taste PIN, holde telefonen mot smart plakat (Bluetooth), NFC. For informasjonssamfunnstjenester til barn ligger bevisbyrden for foreldresamtykke på behandlingsansvarlig (eller databehandler), med rimelig innsats etter tilgjengelig teknologi.
  - **[Merknad – ikke fra kilden]** GDPR art. 8 nr. 2 legger plikten til å treffe rimelige tiltak for å kontrollere foreldresamtykket på den behandlingsansvarlige, ikke på databehandleren (jf. [K43](K43-gdpr-kap02-prinsipper.md#art-8)).

**31.2 Sensitive data (DP-Act art. 8)** – informert, uttrykkelig samtykke før behandling, med mindre annet grunnlag eller loven forbyr.
**31.3 Nettsted** – avkrysningsbokser som ikke er forhåndsavkrysset (opt-in).
**31.4 Informasjonskapsler (cookies)** – samtykke for cookies som ikke er strengt nødvendige for tjenesten brukeren uttrykkelig ba om (banner, overlagt samtykkesone eller bokser), etter informasjon og før lagring; enkelt men presist språk («lage brukerprofiler for å sende målrettet reklame», ikke bare «reklame»). Merknad: nettleserinnstillinger gir bare gyldig samtykke hvis brukeren kan velge cookies per formål – en nettleser som godtar alt som standard gir ikke spesifikt samtykke.
**31.5 Tilkoblet objekt/mobilapp** – samtykke ved første aktivering; nytt samtykke for ny bruker; bekreftelse etter lang inaktivitet; bevar innstillinger ved bytte av enhet/reinstallasjon; segmentert samtykke (særlig deling med andre brukere eller tredjepartsselskaper); ikon/lys ved behandling av spesielle data; tilgang til samtykkeinnstillinger når som helst.
**31.6 Geolokasjon via smarttelefon** – mulighet til å nekte systematisk geolokasjon; velge hvilke apper som kan bruke den; velge hvem som får se lokasjonen og med hvilken presisjon.
**31.7 Målrettet reklame** – enkle, kostnadsfrie metoder for å godta/avslå atferdsbasert reklame og velge interesser; plattform for helt/delvis avslag; forklar sletting av cookies og historikk; cookie som husker at brukeren har reservert seg.
**31.8 Forskning med biologiske prøver** – uttrykkelig, informert samtykke for videre behandling som avviker fra den opprinnelige.

#### 32 Forhold til tredjeparter (s. 76–77)
**32.1 Generelt** – Formål: redusere risikoen ved tredjeparters legitime tilgang.
- Identifiser alle tredjeparter med (mulig) legitim tilgang – visse ansattkategorier, innleide (leverandører), IT-vedlikehold, forretningspartnere, autoriserte tredjeparter.
- Bestem deres rolle (IT-administrator, databehandler, mottaker, autorisert tredjepart) ut fra handlingene de utfører – en skyleverandør er normalt databehandler, men kan i noen tilfeller være behandlingsansvarlig.
- Fordel ansvar ut fra risikoen.
- Velg form for rettigheter/plikter ut fra juridisk struktur og geografi – kontrakt, avtale, bestilling eller BCR.
- Formaliser reglene gjennom hele relasjonens livssyklus etter kategori og handlinger.

**32.2 Innleide på organisasjonens lokaler** – samme tiltak som for ansatte (opplæring, IT-reglement vedlagt reglementet); arbeidsstasjon fra organisasjonen eller kontroll av at arbeidsgiverens utstyr er forenlig med sikkerhetsmålene; taushetsklausul med egen arbeidsgiver som gjelder kundene; tidsbegrensede tilganger som utløper automatisk ved oppdragets planlagte slutt.

**32.3 Tredjepartsmottakere** – kontrakt som angir: hvilke data; formålene den registrerte har samtykket til at dataene overføres for; vilkår for utøvelse av rettigheter; tekniske sikkerhetstiltak ved overføringen. Krev at tredjeparten publiserer personvernerklæring med sikkerhetsmål. Krypter alltid dataflyt over Internett. Informer tredjeparten systematisk når den registrerte krever retting.

**32.4 Autoriserte tredjeparter (myndigheter)** – svar kun på offisielt sendte henvendelser (post eller faks) via samme kanal, **ikke på e-post**; kontroller rettsgrunnlaget for hver henvendelse; autentiser den som spør; utlever kun det som er etterspurt.

#### 33 Sikkerhetskopiering (s. 78–79)
**Formål:** sikre tilgjengelighet og/eller integritet med bevart konfidensialitet.
- Regelmessig backup av papir og elektroniske data etter krav til tilgjengelighet og integritet – f.eks. **daglig inkrementell, ukentlig full**; papir kopieres ved utarbeidelse; automatisk verifisering med rapport.
- Krypter overføringskanalen ved automatisert nettverksbackup.
- Samme sikkerhetsnivå som i drift – krypterte data/kopier eller tilstrekkelig tilgangsbeskyttelse; fysiske medier lagret **på et annet sted** enn dataene (brann- og vanntett skap); sikret transport (autorisert person, sikker beholder).
- Test regelmessig – **utvalg månedlig, full gjenoppretting årlig**.
- Test integriteten ved behov (SHA-256 eller e-signatur).
- Dokumenter IT-avdelingens forpliktelse til å gjenopprette kryptert informasjon ved tap av hemmeligheter, og kontroller prosedyrene.
- Sikre at organisasjon, personell, systemer og lokaler er tilgjengelige innen virksomhetens tidskrav.
- Bekreft geografisk plassering av backup (land).
- Merknader: backup ut av EU krever adekvat land, standardkontrakter, BCR, Privacy Shield (USA) eller unntak. Behandlingsansvarlig forblir ansvarlig. En backupplan (mål) og backupprosedyre (operative midler) skal sikre integritet og varighet uten å true konfidensialiteten.

#### 34 Databehandlere: identifisert og regulert i avtale (s. 80–81)
**34.1 Generelt** – Formål: GDPR art. 28. Avtale med hver databehandler som dekker alle punktene i art. 28: omfang og varighet; formål; dokumenterte instrukser; forhåndsgodkjenning ved bruk av annen databehandler; tilgang til dokumentasjon som viser etterlevelse; **umiddelbar varsling av brudd**; osv.
  - **[Merknad – ikke fra kilden]** Varslingsplikten følger ikke av art. 28 selv, men av art. 33 nr. 2: databehandleren skal «uten ugrunnet opphold» underrette den behandlingsansvarlige om brudd på personopplysningssikkerheten; etter art. 28 nr. 3 bokstav f skal databehandleren bistå med oppfyllelsen av art. 32–36 (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33)).

**34.2 Databehandlere (vertskap, vedlikehold, administrator, spesialtjenester) – unntatt skyleverandører**
- Avtale inngått *intuitu personae* (knyttet til den konkrete leverandøren).
- Krev databehandlerens sikkerhetspolicy (PSSI) og dokumentasjon av sikkerhetssertifiseringer, vedlagt avtalen; kontroller at tiltakene samsvarer med CNILs anbefalinger.
- Fastsett i avtalen: hvilke data databehandleren får tilgang til eller mottar; operasjonene den skal utføre; lagringstid; mottakere behandlingsansvarlig krever overføring til; operasjoner ved oppdragets slutt (permanent sletting, eller tilbakelevering for reversibilitet og deretter sletting hos databehandler); sikkerhetsmålene satt av behandlingsansvarlig.
- Fordel ansvaret for prosessene for de registrertes rettigheter.
- Forby eller regulere uttrykkelig bruk av underdatabehandlere («tier-2 processors»).
- Fastslå at etterlevelse av personvernforpliktelsene er et bindende vilkår i avtalen.

**34.3 Skyleverandører (i tillegg)**
- Krev minst logisk separasjon mellom organisasjonens data og andre kunders.
- Definer tydelig hvor data kan lagres **og fra hvilke land de kan aksesseres** – leverandører oppgir ofte lagringssted, men sjelden hvor administratorene får tilgang fra; dette må avklares i avtalen.
- Se CNILs anbefaling om skytjenester.

#### 35 Tilsyn (supervision) (s. 82)
**Formål:** helhetlig og oppdatert oversikt over personvern og etterlevelse.
- Regelmessig kontroll av behandlinger (etterlevelse, tiltakenes effektivitet) – de mest sensitive og de med brudd/klager, ellers stikkprøver slik at alle kontrolleres jevnlig; eksterne revisjoner av de mest sensitive.
- Personvernmål og indikatorer – kart over behandlinger og risikoer, forhåndsmelding til CNIL.
- Fordel ansvar ut fra risiko – **RACI-matrise** (Responsible, Accountable, Consulted, Informed).
- Regelmessig vurdering – årlig risikokart for alle behandlinger, årlig vurdering av etterlevelse av personvernpolicy, fremdriftsrapport for tiltak, presentert for behandlingsansvarlig.
- Verktøy: CNIL godkjenner revisjonsprosedyrer; ANSSI TDBSSI-guide.

#### 36 Overvåking (surveillance) av sikkerhetshendelser (s. 83–85)
**36.1 Generelt** – Formål: tidlig oppdagelse av hendelser og informasjon til analyse/bevis.
- Loggarkitektur: tidsstempling i UTC; pålitelig tidskilde (NTP); sentralisering på relativt isolert innsamlingsmaskin med egen konsultasjonsstasjon; eksport av logger; nok lagringskapasitet; arkivering og backup av logger; beskyttelse mot sabotasje og uautorisert tilgang.
- Velg hendelser som logges ut fra kontekst, støtteressurser (arbeidsstasjoner, brannmur, nettverksutstyr, servere), risiko og rettslige rammer – logg handlinger på arbeidsstasjoner kun ved forhøyet risiko; franske regler for lagring av trafikkdata ved offentlig internettilgang (ett år) og LCEN ved innholdsproduksjon.
- Følg personvernregelverket når logger inneholder personopplysninger – informer brukerne, bruk kun til oppgitt formål.
- Periodisk analyse; ev. automatisk deteksjon av svake signaler.
- **Oppbevar hendelseslogger i seks måneder** med mindre lov krever annet.
- Verktøy: CERTA-notat om logger; RGS tidsstempling.

**36.2 Klientarbeidsstasjon** – som 19.1 (loggstørrelse, hendelsestyper, eksport, analyse).
**36.3 Brannmur** – filtreringspolicy som forbyr direkte kommunikasjon mellom interne arbeidsstasjoner og utsiden (kun via brannmur) og tillater kun eksplisitt autoriserte flyter; logg alle godkjente forbindelser og alle avviste forsøk (tidsstempel til nærmeste millisekund, kilde- og mål-IP, transportprotokoll, TCP-flagg og tilstander); eksporter logger via sikker kanal til dedikert server.
**36.4 Nettverksutstyr** – logg aktivitet på hver port på svitsjer/rutere; eksporter via syslog eller netflow; overvåk volum over tid og etterlevelse av ACL-er.
**36.5 Server** – logg mest mulig om klientforespørsler på webservere (vellykkede forbindelser, metoder, spørringer, volum, fordeling per land) for å finne konfigurasjonsfeil og SQL-injeksjon; logg brukeraktivitet på proxy; alle DNS-spørringer; autentiseringsdata og varighet på fjerntilgangsservere; mottak og håndtering av meldinger på e-postservere.

#### 37 Driftssikkerhet (s. 86–87)
**Formål:** begrense sannsynlighet og alvorlighet for risiko mot støtteressurser i drift.
- Dokumenter driftsprosedyrer, hold dem oppdatert og tilgjengelige.
- Oppdatert inventar over programvare og maskinvare (programvare, fysiske og virtuelle servere, infrastruktur, tredjepartstjenester, nettverk og telekom – med OS, IP/MAC, applikasjoner, versjoner, patcher, firmware).
- Overvåk sårbarheter (inkl. firmware) og rett snarest – automatiske oppdateringer der mulig, ellers så snart rettinger foreligger, ellers mekanismer som hindrer utnyttelse.
- Formaliser oppdateringsprosedyrer.
- Produksjonsservere kun til tiltenkt bruk – kun nødvendig programvare og porter.
- Fysisk redundans (RAID) eller duplisering mellom servere/sider.
- Tilstrekkelig lagrings- og prosesseringskapasitet, også ved toppbelastning.
- Fysiske driftsforhold (temperatur, fuktighet, strøm) med reserve (UPS, aggregat).
- Begrens tilgang til sensitiv og verdifull maskinvare; begrens mulighet for endring (forseglinger, hengelås, låste diskarrayer).
- Gjenopprettingsplan (PRA) eller kontinuitetsplan (PCA) ut fra tilgjengelighetsmål – formalisert, distribuert og testet jevnlig.
- Prosedyre for sikkerhetshendelser (oppdage, registrere, beskrive, løse) – se kap. 17.

#### 38 Sikkerhet i datakanaler (nettverk) (s. 88–94)
**38.1 Generelt** – Formål: redusere risiko fra nettverkenes egenskaper.
- Oppdatert detaljert nettverkskart; inventar over alle Internett-tilganger med tiltak håndhevet ved hvert punkt.
- Sikre tilgjengelighet (kapasitet, alternative løsninger ved feil).
- Segmenter nettverket i logiske subnett etter tjenester (VLAN eller fysisk adskilte nett).
- Forby direkte kommunikasjon mellom interne arbeidsstasjoner og eksterne nett – internt nett uten innkommende Internett-forbindelser og en DMZ.
- Kun eksplisitt tillatte forbindelser via brannmur (f.eks. kun innkommende til port 443 for HTTPS-webserver).
- Overvåk nettverksaktivitet etter å ha informert de registrerte – IDS/IPS i sanntid.
- Plan for respons på større inntrenging (nettverkskart, liste over autorisert personell, kontaktinfo til bistandsorganer).
- Automatisk identifikasjon av maskinvare (MAC-adresser) for å blokkere ukjente enheter.
- Sikre administrasjonstrafikk; begrens tilgang til fjerndiagnose-/konfigurasjonsporter; begrens SNMP (UDP 161/162).
- Forby tilkobling av ukontrollert maskinvare – kun utstyr godkjent av IT-avdelingen.
- Send hemmeligheter (dekrypteringsnøkkel, passord) separat via en annen kanal enn dataene (kryptert fil per e-post, passord per telefon/SMS).
- Verktøy: NIDS, HIDS, hybrid IDS; NIPS, WIPS, NBA, HIPS; CERTA-notater; RGS autentisering.

**38.2 Aktivt nettverksutstyr** – SSH eller direkte tilkobling til brannmurer, rutere, svitsjer; Telnet forbudt unntatt direkte tilkobling.
**38.3 Fjernadministrasjonsverktøy** – kun IT-personell innen egne oppgaver; unik identifikasjon; minst robust passord og helst sertifikat; logg aktivitet; sikker autentiseringsflyt (ingen klartekstpassord, ingen replaybare sekvenser); forhåndsgodkjenning fra brukeren (klikk på pop-up); forby endring av sikkerhetsinnstillinger og visning av passord; blokker uthenting av hemmeligheter; krypter all trafikk; brukeren informeres om pågående fjernadministrasjon (ikon).
**38.4 Mobile eller fjerntliggende enheter** – sterk autentisering (to faktorer; bytt standard aktiveringspassord for OTP); krypter kommunikasjon (dedikerte linjer, VPN med sterke algoritmer, 128-bit SSL for webtjenester); brannmur aktivert når enheten forlater lokalene (egen fjerntilgangsinfrastruktur, forby samtidig tilkobling til internt nett og trådløst nett, brukeren kan ikke slå av brannmuren).
**38.5 Trådløse grensesnitt (Wi-Fi, Bluetooth, IR, 4G)** – forby usikret kommunikasjon; forby samtidig trådløs og Ethernet; deaktiver ubrukte grensesnitt; kontroller trådløse nett (kun LAN-utvidelse for ansatte og helt isolert offentlig gjestenett; autentiser; krypter).
**38.6 Wi-Fi** – WPA/WPA2 med AES-CCMP eller «Enterprise»-modus (RADIUS, EAP-TLS eller PEAP); forby ad hoc-nett; brannmur ved inn-/utgang; MAC-filtrering i visse tilfeller.
**38.7 Bluetooth** – gjensidig autentisering; kun fildeling med IT-kontrollert utstyr; krypter trafikken.
**38.8 Infrarød** – autentisering før forbindelse og overføring.
**38.9 Mobilnett (2G/3G/4G)** – SIM-kort beskyttet med PIN ved hver bruk.
**38.10 Nettlesing** – HTTPS for serverautentisering og konfidensialitet; nøkler etter RGS; sertifikatleverandør etter RGS v1.0.
**38.11 Filoverføring** – SFTP (eventuelt SCP); krypter filer før sending ved høy risiko.
**38.12 Faks** – i fysisk sikret rom; personlig kode for utskrift; vis mottakers identitet; send originaler etterpå; forhåndslagrede numre.
**38.13 ADSL/fiber** – inventar over lokale internettilganger; fysisk isolert fra internt nett; kun for spesifikke legitime behov; aktivert kun ved bruk; slå av Wi-Fi på ruteren.
**38.14 E-post** – krypter vedlegg med personopplysninger; bevisstgjør om e-post fra ukjente og risikable vedlegg (.pif, .com, .bat, .exe, .vbs, .lnk) eller blokker dem; ikke videresend «hoaxes»; policy for e-postautentisering og **DMARC**.
**38.15 Direktemeldinger** – bevisstgjøring (forsiktighet, ikke reelle personopplysninger i profiler, vedlegg, lenker); forby installasjon/bruk med mindre nødvendig, og da kun fra leverandørens nettsted.

#### 39 Sikkerhet for papirdokumenter (s. 95–97)
**Formål:** begrense uautorisert tilgang til papirdokumenter.
**39.1 Merking** – synlig merking på hver side med sensitive personopplysninger («This document includes sensitive personal data» / «… personal data that is protected by law»); «[Personal data]» i emnefeltet på e-post som skrives ut; merking i fagapplikasjoner; påminnelse i korrespondanse om at vedlegg kun skal til opprinnelig mottaker og destrueres ved lagringstidens slutt. Merknad: merking kan tiltrekke ondsinnede, men fordelene veier normalt tyngre.
**39.2 Dokumentenes sårbarheter** – papir og utskriftsmetode tilpasset lagringsforholdene; hent utskrifter straks eller bruk sikker utskrift; begrens distribusjon; lagre i sikkert skap (brannsikkert arkivskap med lås, safe); makuler med kvern av egnet nivå – DIN 32757, **minst nivå 3**. For de mest sensitive: kopi på annet sikkert sted, forseglinger.
**39.3 Papirkanaler** – send kun nødvendige dokumenter; spor sirkulasjonen (liste over sendte/mottatte, identitet og signatur for avsender, kurer, mottaker, dato/tid); velg kanal etter risiko og frekvens (post, egne sjåfører, budfirma); styrk tillit til budfirma (informasjon om risiko, klausuler om tilgjengelighet/integritet/konfidensialitet, ID-kontroll av sjåfører); beskytt dokumentene (rekommandert i dobbel konvolutt merket «Confidential», beholdere som tåler ulykker/brann). Ved høy risiko: kopier av alt som distribueres, prosedyrer for stjålne/endrede/manglende dokumenter, forseglinger.

#### 40 Maskinvaresikkerhet (s. 98–101)
**40.1 Generelt** – Formål: redusere risiko fra maskinvarens egenskaper.
- Oppdatert inventar (arbeidsstasjoner og brukere, servere, nettverk/telekom, skrivere, fakser – med OS, IP/MAC, applikasjoner, versjoner, patcher).
- Skill organisasjonens ressurser i delte lokaler (dedikerte nettverksressurser under IT-avdelingens ansvar; låst rack i delte tekniske rom).
- Blokker tilgang til data på kassert utstyr (inspiser, sikkert rom, sikker sletting, fysisk destruksjon, taushetserklæring fra destruksjonsfirma, **destruksjonsrapport i 10 år**).
- RAID eller tilsvarende; kapasitet og forhold (plassering, fuktighet, temperatur) tilpasset bruken; strømforsyning beskyttet mot spenningsvariasjoner og med reserve eller kontrollert nedstengning.
- Beskytt sensitiv og verdifull maskinvare; begrens endringsmuligheter (forseglinger, hengelås, låste diskarrayer).

**40.2 Arbeidsstasjoner** – som 19.1 (sikre og fungerende maskiner, tyverisikring, uthenting og sletting før omdisponering, slette midlertidige data, undersøkelse ved kompromittering).
**40.3 Mobile enheter** – kryptering (jf. kap. 4); minimer data og forby ved utenlandsreiser ved behov; sikre tilgjengelighet; slett når data er overført; personvernfilter; **automatisk låsing etter noen minutters inaktivitet**. Merknader: fingeravtrykkslesere krever CNIL-godkjenning med mindre de dekkes av «Single authorization 52»; brukere skal ikke kunne slå av diskkryptering; behold nøkkelkopi.
**40.4 Flyttbare lagringsmedier** – kun medier fra IT-avdelingen; forby trådløse USB-pinner (Bluetooth); forby USB-pinner på usikret utstyr; kun til jobbformål; deaktiver autorun (gruppepolicy); krypter data; lever defekte/unødvendige medier til IT; destruer sikkert (degausser for magnetiske medier; makulering DIN 32757 nivå 3 for CD/DVD; for SSD/flash: krypter, formater, krypter på nytt med annen nøkkel).
**40.5 Multifunksjonsskrivere og kopimaskiner** – bytt fabrikkpassord; deaktiver unødvendige nettverksgrensesnitt og tjenester; krypter harddisker der mulig; begrens skanning-til-e-post til interne adresser (eventuelt én adresse); vedlikehold og kassering som 24.4 (destruksjonsrapport i 10 år).

#### 41 Nettstedsikkerhet (s. 102)
**Formål:** redusere risiko fra nettstedets egenskaper.
- Teletjenester skal følge RGS – sertifikat signert av godkjent rot-CA; RGS-samsvarssertifikat tilgjengelig på nettstedet.
- **Trafikk krypteres med TLS**; webserveren skal kun akseptere TLS (ekskluder SSL, tving kryptering).
- Cookies: samtykke før installasjon; for egne cookies: **gyldighet maks 13 måneder**, **HttpOnly**-flagg, **SameSite**-flagg for cookies som ikke trenger tredjepartstilgang.
- Definer en **Content-Security-Policy** som kun inkluderer aktører du tillater å plassere innhold.
- Gjennomfør sikkerhetsrevisjoner.
- Verktøy: ANSSIs guide for sikring av nettsteder.

#### 42 Overføringer ut av EU (s. 103)
**Formål:** DP-Act art. 68–69, GDPR art. 44–50.
- Angi geografisk lagringssted for de ulike behandlingsdataene.
- Begrunn valg av ekstern hosting avhengig av land og angi de rettslige garantiene som sikrer adekvat beskyttelse ved overføring.

#### 43 Sporbarhet (logging) (s. 104)
**Formål:** registrere og tilskrive brukernes konsultasjon og handlinger slik at det kan gis bevis ved undersøkelser.
- Applikasjonslogging av endringer og tilganger med tidspunkt – UTC, NTP, sentralisering på isolert maskin, eksport, kapasitet, arkivering og backup av logger, beskyttelse mot sabotasje og uautorisert tilgang, **streng konfidensialitet for logger**.
- Brukerautentisering som gjør det mulig å tilskrive hendelser – forby generiske/delte identifikatorer, følg CNILs passordanbefalinger, foretrekk sterk tofaktorautentisering.
- Følg personvernregelverket for logger knyttet til identifiserte brukere – informer brukerne, ikke bruk loggene til andre formål.
- Periodisk analyse; ev. automatisk deteksjon av unormal aktivitet.
- **Oppbevar hendelseslogger i seks måneder** med mindre lov krever annet.
- Verktøy: sikre loggenes bevisverdi (tidsstempling, digital signatur, fingeravtrykk) i tråd med RGS.

---

### Hurtigoppslag: tiltak per fryktet hendelse (avledet fra katalogen)

| Fryktet hendelse | Typiske tiltak i katalogen |
|---|---|
| Uautorisert tilgang | Minimering (26), lagringstid (9), anonymisering (2), kryptering (4), partisjonering (5), logisk tilgangskontroll (8), fysisk adgangskontroll (6), sporbarhet (43), nettverkssikkerhet (38), arbeidsstasjoner/mobile (19, 40), vedlikehold (24), tredjeparter/databehandlere (32, 34), personal (18), papir (39) |
| Uønsket endring | Integritetsovervåking (7), logisk tilgangskontroll (8), sporbarhet (43), sikkerhetskopi (33), skadevare (23), driftssikkerhet (37), nettverkssikkerhet/kryptering av kanaler (38, 4.9), datakvalitet (30), personal (18) |
| Forsvinning | Sikkerhetskopi (33), driftssikkerhet inkl. PRA/PCA og RAID (37, 40), beskyttelse mot ikke-menneskelige kilder (29), unngå risikokilder (10), skadevare (23), vedlikehold (24), hendelseshåndtering (17), papirsikkerhet (39) |

(Denne tabellen er en sammenstilling laget for oppslag – **[Merknad – ikke fra kilden]** som tabell, men hver henvisning peker til kildens kapitler.)

## Praktiske sjekkpunkter

- Kontroller at alvorlighet er vurdert med utgangspunkt i konsekvenser for **de registrerte** (fysiske, materielle, moralske), sammenlignet med eksemplene i §1.5, og justert for identifiserbarhet, risikokilder, sammenkoblinger og antall mottakere.
- Kontroller at sannsynlighet er vurdert ut fra sårbarheter og kildenes kapabilitet, og justert for Internett-eksponering, utlandsutveksling, sammenkoblinger, heterogenitet, variabilitet og omdømme.
- Kontroller at trusselidentifikasjonen har gått gjennom alle seks typer støtteressurser og relevante handlinger (brukt upassende, observert, endret, mistet, overbelastet, skadet, manipulert) for alle tre fryktede hendelser.
- Kontroller at logisk sletting ikke brukes som «sletting» ved utløpt lagringstid (kap. 9).
- Kontroller at kontoer sperres etter et begrenset antall feilforsøk (CNIL: 5), at rettigheter gjennomgås årlig og at midlertidige kontoer har utløpsdato (kap. 8).
- Kontroller at hendelseslogger oppbevares i ca. seks måneder med mindre annet er lovpålagt, og at logger er beskyttet og konfidensielle (kap. 36, 43).
- Kontroller at sikkerhetskopier lagres et annet sted, krypteres/beskyttes som produksjonsdata, og testes (utvalg månedlig, full årlig) (kap. 33).
- Kontroller at databehandleravtaler dekker art. 28 og i tillegg: sikkerhetspolicy/sertifiseringer vedlagt, eksakte operasjoner, lagringstid, tilbakelevering/sletting ved opphør, sikkerhetsmål, ansvar for rettigheter, regulering av underdatabehandlere – og for sky: logisk separasjon samt lagrings- **og tilgangsland** (kap. 34).
- Kontroller at avvikshåndtering kategoriserer brudd (hendelse, incident, skadelig hendelse, krise), at responsplaner testes minst hvert annet år og at bruddlogg føres (kap. 17).
- Kontroller at testing ikke skjer på reelle produksjonsdata uten anonymisering (kap. 20).
- Kontroller at tilkoblede enheter uten skjerm har informasjon via QR-kode/app, og at brukeren varsles (ikon/lys) når mikrofon, lokasjon eller bakgrunnskjøring er aktiv (kap. 11.5, 22.4, 31.5).
- Kontroller at henvendelser fra myndigheter besvares kun via offisiell kanal etter kontroll av rettsgrunnlag, og kun med etterspurte data (kap. 32.4).
- Ved risiko som ikke kan reduseres tilstrekkelig: forhåndsdrøft med tilsynsmyndigheten (kap. 16, GDPR art. 36).

## Viktige sitater

- «Important: these are only examples, which can be very different depending on the context» (s. 4)
- «The value of the level that best matches the potential impacts identified is then selected, by comparing the impacts identified in the context considered with the generic impacts in the scale.» (s. 5)
- «Maximum: it seems extremely easy for the selected risk sources to materialize the threat by exploiting the properties of supporting assets» (s. 6)
- «Deletion of a piece of data reaching the end of its storage duration cannot be in a logical fashion» (s. 29)
- «Consult the CNIL if the residual risks are high, pursuant to Article 36 of the General Data Protection Regulation (GDPR).» (s. 42)
- «The CNIL considers that an employee cannot consent freely to processing set up by his/her employer given their hierarchical relationship.» (s. 73)
- «cloud computing service providers often stipulate the data storage location, but seldom indicate the geographic regions from which their administrators access their platform; this point must be clarified in the contract.» (s. 81)
- «Retain the event logs for six months unless legal and regulatory restrictions require specific storage durations.» (s. 104)

## Kryssreferanser

- GDPR: art. 5 (prinsipper; kap. 9, 14, 26, 30), art. 6 (kap. 15), art. 7–8 (kap. 31), art. 9–10 (kap. 26), art. 12–14 (kap. 22), art. 15–21 (kap. 11–13), art. 25 (kap. 20), art. 28 (kap. 34), art. 32 (sikkerhetstiltakene), art. 33–34 (kap. 17), art. 35–36 (kap. 16, 21), art. 44–50 (kap. 10, 33, 42).
- [K28](K28-cnil-pia-metode.md) – metoden som bruker skalaene og katalogene.
- [K29](K29-cnil-pia-maler.md) – malene der tiltakene dokumenteres.
- [K31](K31-cnil-pia-tilkoblede-objekter.md) – anvendt eksempel; gjengir skalaer og trusselkataloger; har i tillegg typologi av mål for risikobehandling og eksempel på risikokilder med motiver.
- [K33](K33-cnil-sikkerhetsguide.md), [K34](K34-cnil-cybersikkerhet-2024.md) – CNILs sikkerhetsguide (nyere og mer oppdaterte tiltak).
- [K10](K10-dt-kryptering.md) – Datatilsynet om kryptering.
- [K05](K05-dt-databehandleravtale.md), [K01](K01-dt-behandlingsansvarlig-og-databehandler.md) – databehandleravtaler og roller (kap. 32, 34).
- [K14](K14-dt-overforing-utenfor-eos.md), [K38](K38-tia-guide.md) – overføringer (kap. 10, 33, 42).
- [K15](K15-dt-digitale-angrep.md) – digitale angrep og avvik (kap. 17).
- [K32](K32-nsm-grunnprinsipper.md) – NSMs grunnprinsipper (norsk sikkerhetsbaseline).
- [K39](K39-cnil-mobilapper.md) – CNILs anbefalinger for mobilapper (kap. 11.5, 22.4, 31.5).
- [K25](K25-wp259-samtykke.md), [K26](K26-wp260-apenhet.md) – samtykke og åpenhet.
- [K37](K37-sdm-standard-datavernmodell.md) – SDM-tiltakskatalog (alternativ).

## Aktualitet og begrensninger

- 2018-utgaven er tilpasset GDPR, men mange anbefalinger viser fortsatt til den gamle franske DP-Act (meldeplikt til CNIL, forhåndsgodkjenning av biometri, «Single authorization 52», «Article 31»-liste per faks) og franske organer/standarder (ANSSI, RGS, CERTA, LCEN, DIN 32757). Disse må oversettes til norske forhold.
- **[Merknad – ikke fra kilden]** Flere tekniske anbefalinger er utdaterte: «128 bits for confidentiality guaranteed until 2020»; «128-bit SSL»; WPA/WPA2 (WPA3 er nå standard); passordregel om periodisk bytte (moderne anbefalinger, inkl. CNILs passordanbefaling delib. 2022-100 som erstattet delib. 2017-012, legger mer vekt på lengde/entropi og MFA og mindre på periodisk bytte). Nevnte programvare (Spybot, Rootkit Revealer, Zed!, Security BOX) kan være utgått. CERTA heter nå CERT-FR.
- **[Merknad – ikke fra kilden]** Privacy Shield (nevnt i kap. 10 og 33) ble kjent ugyldig av EU-domstolen i Schrems II (C-311/18, 16.7.2020). Overføringer til USA kan nå skje under EU–US Data Privacy Framework (adekvansbeslutning, dvs. beslutning om tilstrekkelig beskyttelsesnivå etter art. 45, juli 2023) for sertifiserte mottakere, ellers standardkontrakter (standard personvernbestemmelser, art. 46 nr. 2 bokstav c; 2021/914) med overføringsvurdering. Listen over adekvate land i kap. 10 er ufullstendig/utdatert.
- **[Merknad – ikke fra kilden]** Fristen «innen to måneder» for rettigheter (kap. 11–12) stammer fra fransk rett; under GDPR art. 12 nr. 3 er fristen «uten ugrunnet opphold» og senest **én måned** (kan forlenges med ytterligere to måneder ved behov) – kap. 13 nevner dette selv. Kap. 13 sier «ikke kostnad utover kopieringskostnad»; etter art. 15 nr. 3 skal den første kopien gis kostnadsfritt, og gebyr basert på administrasjonskostnadene kan bare kreves for flere kopier (jf. [K43](K43-gdpr-kap03-den-registrertes-rettigheter.md#art-12)).
- **[Merknad – ikke fra kilden]** Aldersgrensen 13 år for foreldresamtykke er brukt i katalogen; i Norge er grensen 13 år (personopplysningsloven § 5), i Frankrike 15 år.
- **[Merknad – ikke fra kilden]** Kategoriseringen av avvik i kap. 17 er CNILs interne inndeling; GDPR bruker begrepet «brudd på personopplysningssikkerheten» (art. 4 nr. 12), og tersklene er «risiko» (melding til tilsynsmyndigheten uten ugrunnet opphold og om mulig innen 72 timer, art. 33) og «høy risiko» (underretning av de registrerte, art. 34).
- **[Merknad – ikke fra kilden]** CNIL har senere publisert oppdaterte sikkerhetsveiledninger (bl.a. «Guide de la sécurité des données personnelles», 2023/2024-utgaver – se [K33](K33-cnil-sikkerhetsguide.md)/[K34](K34-cnil-cybersikkerhet-2024.md)), som bør foretrekkes for konkrete tekniske krav. CNILs PIA-verktøy (programvare) inneholder en tiltakskatalog basert på denne kunnskapsbasen.
- Deler av tabellene i §1.5 og §1.7 er rekonstruert fra et tekstuttrekk med forskjøvne kolonner; innholdet er kontrollert mot de tilsvarende tabellene i [K31](K31-cnil-pia-tilkoblede-objekter.md).

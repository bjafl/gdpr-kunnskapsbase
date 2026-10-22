---
id: K28
tittel: "Privacy Impact Assessment (PIA) – Methodology (how to carry out a PIA)"
utgiver: CNIL (Commission Nationale de l'Informatique et des Libertés, Frankrike)
dato: "Juni 2015 (June 2015 Edition)"
spraak: en
fil: "ressurser/CNIL-PIA-1-Methodology.pdf"
type: metode
gdpr_artikler: [5, 6, 32, 35, 36]
emner: [dpia, pia, risikovurdering, metode, ebios, alvorlighet, sannsynlighet, risikokart, raci]
relevans: høy
---

# PIA – Methodology (CNIL, 2015)

## Sammendrag

Første av CNILs tre PIA-guider: metodeguiden som beskriver *hvordan* en vurdering av personvernkonsekvenser (PIA/DPIA – CNIL bruker begrepene om hverandre, s. 3) gjennomføres. Metoden er en tilpasning av den franske risikostyringsmetoden EBIOS (ANSSI) til personvern (s. 4). En PIA hviler på to pilarer: (1) grunnleggende prinsipper og rettigheter som er «non-negotiable» uansett risikonivå, og (2) styring av risiko for de registrertes personvern, som bestemmer passende tekniske og organisatoriske tiltak (s. 4). Metoden har fire steg: **1. Kontekst – 2. Tiltak (controls) – 3. Risikoer – 4. Beslutning**, og er en iterativ, kontinuerlig forbedringsprosess (s. 7). En risiko består av en *fryktet hendelse* (feared event: uautorisert tilgang, uønsket endring, forsvinning) og alle *trusler* som kan gjøre den mulig; risikonivå estimeres ut fra *alvorlighet* (severity) og *sannsynlighet* (likelihood) (s. 6, 15). Dokumentet er 19 sider, skrevet under direktiv 95/46 og den franske personvernloven (DP-Act), og må brukes sammen med «PIA-2-Tools» (maler og kunnskapsbaser) og «PIA-3-GoodPractices» (tiltakskatalog) (s. 3). Målgruppe: behandlingsansvarlige (accountability), produktleverandører (innebygd personvern), prosjekteiere, leverandører/«prime contractors», personvernombud (DPO) og informasjonssikkerhetsleder (CISO) (s. 4).

## Når skal agenten bruke denne kilden

- Når brukeren trenger en **prosessmodell** for DPIA: hvilke steg, i hvilken rekkefølge, hvem gjør hva (RACI-tabellen s. 9).
- Når agenten skal forklare **risikobegrepet** i personvernsammenheng (risikokilde → støtteressurs → trussel → fryktet hendelse → konsekvens) og hvordan alvorlighet og sannsynlighet bestemmes.
- Når agenten skal velge **rekkefølge på tiltak** (styring → data → konsekvenser → risikokilder → støtteressurser, s. 13).
- Når det skal lages en **DPIA-rapport** og man trenger minimumsinnholdet (s. 10).
- For konkrete skalaer, trusselkataloger og tiltakskatalog: bruk [K30](K30-cnil-pia-kunnskapsbaser.md); for utfyllbare tabeller: [K29](K29-cnil-pia-maler.md); for et utfylt eksempel: [K31](K31-cnil-pia-tilkoblede-objekter.md).

## Hovedinnhold

### Forord og skrivekonvensjoner (s. 3)

- Skal brukes sammen med [PIA-2-Tools] (maler og kunnskapsbaser) og [PIA-3-GoodPractices] (katalog over tiltak for å oppfylle rettslige krav og behandle risiko).
- «Privacy» brukes som samlebegrep for alle grunnleggende rettigheter og friheter (EU-charteret art. 7 og 8, direktiv 95/46 art. 1, DP-Act art. 1).
- «PIA» brukes om både Privacy Impact Assessment og Data Protection Impact Assessment (DPIA).

### Innledning (s. 4–10)

**To pilarer (s. 4):**
1. Grunnleggende prinsipper og rettigheter – fastsatt i lov, «non-negotiable», kan ikke varieres etter risikoens art, alvorlighet eller sannsynlighet.
2. Risikostyring for de registrertes personvern – bestemmer passende tekniske og organisatoriske tiltak.

**Virkeområde (s. 4):** Metoden er bruk av EBIOS i konteksten «Personal Data protection». Brukes av behandlingsansvarlige som vil vise etterlevelse (accountability) og produktleverandører som vil vise innebygd personvern (privacy by design). Fotnote: «behandling av personopplysninger» og «produkt» brukes om hverandre.

**Hvorfor PIA (s. 5):**
- Kan gjennomføres for enhver kompleks eller innovativ behandling/produkt med høye innsatser; det kan også være en rettslig plikt.
- Personopplysninger har verdi for organisasjonen, men behandlingen skaper «de facto» et betydelig ansvar pga. risikoen for de registrerte. Sikkerhetsbrudd kan gi fysisk skade, materiell og moralsk skade.
- Opplysninger har verdi for andre: markedsverdi (spam, målrettet reklame) eller skadeverdi ved urettmessige handlinger (diskriminering, nektet tilgang til ytelser) eller ondsinnede handlinger (bankbedrageri, identitetstyveri, utpressing, innbrudd, ærekrenkelse, trusler, vold).
- Trusselbildet endres: kultur for å eksponere privatliv, økte kapabiliteter hos risikokilder (organisert kriminalitet, verktøy lett tilgjengelig på nett, statlig spionasje).
- Risikostyring gjør det mulig å bestemme *nødvendige og tilstrekkelige* tiltak, prioritere risiko, behandle den forholdsmessig, optimalisere kostnader og ta beslutninger på et så objektivt grunnlag som mulig.

**Hva er en personvernrisiko (s. 6)** – et hypotetisk scenario som beskriver:

| Element | Eksempel fra kilden |
|---|---|
| hvordan **risikokilder** (risk sources) | en ansatt bestukket av en konkurrent |
| kan utnytte sårbarheter i **støtteressurser** (personal data supporting assets) | filbehandlingssystemet som tillater manipulering av data |
| i en kontekst av **trusler** (threats) | misbruk ved å sende e-post |
| og la **fryktede hendelser** (feared events) inntreffe | uautorisert tilgang til personopplysninger |
| på **personopplysninger** | kundefil |
| og dermed gi **konsekvenser** (impacts) for de registrertes personvern | uønskede henvendelser, følelse av krenket privatliv |

Risikonivået estimeres ut fra (s. 6):
- **Alvorlighet (severity)** = risikoens størrelse; avhenger hovedsakelig av hvor skadelige de potensielle konsekvensene er (sett i lys av konteksten: opplysningenes art, de registrerte, formål).
- **Sannsynlighet (likelihood)** = muligheten for at risikoen inntreffer; avhenger hovedsakelig av sårbarhetsnivået i støtteressursene og risikokildenes kapabilitet til å utnytte dem.

**Hvordan gjennomføres en PIA (s. 7)** – etterlevelse bygger på:
- respekt for de rettslige prinsippene (spesifisert, uttrykkelig og legitimt formål; adekvate, relevante og ikke overdrevne opplysninger; klar og fullstendig informasjon; begrenset lagringstid; rett til innsigelse, innsyn, retting og sletting osv.);
- styring av risiko knyttet til sikkerheten for personopplysninger (DP-Act art. 34 / direktivet art. 17: ta «all useful precautions» for å hindre endring, skade eller uautorisert tilgang).

Fire steg (figur 4, s. 7):
1. Definer og beskriv konteksten for behandlingen og dens innsatser (stakes).
2. Identifiser eksisterende eller planlagte tiltak (for å oppfylle rettslige krav og behandle risiko forholdsmessig).
3. Vurder personvernrisikoene for å sikre at de er korrekt behandlet.
4. Beslutt om måten prinsippene etterleves og risikoene behandles på kan valideres – eller gå tilbake til tidligere steg.

Prosessen er kontinuerlig forbedring, kan kreve flere iterasjoner, og krever **oppfølging av endringer over tid (f.eks. årlig) og oppdatering ved hver vesentlig endring** (s. 7).

**Detaljert prosess (figur 5, s. 8):**

| Steg | Innhold |
|---|---|
| 1.1 Presentasjon | Presentasjon, formål, innsatser |
| 1.2 Beskrivelse | Personopplysninger, prosesser, støtteressurser m.m. |
| 2.1 Rettslige tiltak | Formål, informasjon, de registrertes rettigheter m.m. |
| 2.2 Risikobehandlingstiltak | Tiltak på personopplysninger, konsekvenser, kilder, støtteressurser |
| 3.1 Kilder | Hvem? Hvorfor? |
| 3.2 Fryktede hendelser | Hva? → alvorlighet |
| 3.3 Trusler | Hvordan? → sannsynlighet |
| 3.4 Risikoer | Alvorlighet × sannsynlighet |
| 4.1 Evaluering | Akseptabelt? |
| 4.2 Mål (hvis nei) | Sett mål, gjenta stegene |
| 4.3 Handlingsplan / 4.4 Validering (hvis ja) | PIA ferdig |

Endringer i konteksten utløser ny runde. Metoden bør brukes **så snart en ny behandling designes**; å gjøre det etter at systemet og tiltakene er implementert kan sette valgene i tvil (s. 8).

**Hvem deltar (RACI, s. 9)** – PIA gjennomføres normalt av behandlingsansvarlig eller produktleverandør; kan også gjøres av en databehandler på vegne av behandlingsansvarlig (fotnote 7).

| Steg | Behandlingsansvarlig | Prosjekteier (business) | Leverandør (prime contractor) | DPO | CISO |
|---|---|---|---|---|---|
| 1.1 Generell beskrivelse | Accountable | Consulted | Informed | Responsible | Informed |
| 1.2 Detaljert beskrivelse | Accountable | Consulted | Informed | Responsible | Informed |
| 2.1 Rettslige tiltak | Accountable | Consulted | Consulted | Responsible | Informed |
| 2.2 Risikobehandlingstiltak | Accountable | Consulted | Consulted | – | Responsible |
| 3.1 Risikokilder | Accountable | Consulted | Informed | Informed | Responsible |
| 3.2 Fryktede hendelser | Accountable | Consulted | Informed | Informed | Consulted |
| 3.3 Trusler | Accountable | Informed | Consulted | Responsible | Responsible |
| 3.4 Risikoer | Accountable | Informed | Informed | Informed | Consulted |
| 4.1 Evaluering | Accountable | Informed | Informed | Responsible | Consulted |
| 4.2 Mål | Accountable | Consulted | Consulted | Responsible | Informed |
| 4.3 Handlingsplan | Accountable | Responsible | Consulted | Responsible | Informed |
| 4.4 Formell validering | Responsible | Informed | Informed | Informed/Consulted | Informed |

(Tabellen er gjengitt fra tekstuttrekket; enkelte celler i kildens tabell kan være forskjøvet ved ekstraksjon – særlig rad 2.2, 3.3 og 4.4. Kontroller mot PDF ved behov.) Definisjoner: Accountable = person med fullmakt til å godkjenne; Consulted = konsultert for informasjon; Informed = informert om resultatet; Responsible = utfører handlingen. Ansvarsfordelingen kan tilpasses organisasjonens prosesser (f.eks. prosjektstyring), og eksterne kan måtte involveres (s. 9).

**PIA-rapporten (s. 10)** – minimum:

| Del | Innhold |
|---|---|
| Innledning | Presentasjon av behandlingen |
| Hoveddel | Beskrivelse av omfang (scope); liste over rettslige tiltak; liste over risikobehandlingstiltak; risikokart |
| Konklusjon | Begrunnelse for validering av PIA |
| Vedlegg | Detaljert beskrivelse av omfang; detaljert presentasjon av tiltak; detaljert beskrivelse av risikoer; handlingsplan |

Rapporten skal **gjøres tilgjengelig** for tilsynsmyndigheten (trenger ikke sendes rutinemessig, men skal kunne fremlegges på forespørsel). Det kan være nyttig å publisere hele eller deler av den (regulatoriske krav, accountability, omdømme) (s. 10).

### Steg 1 – Kontekst: PIA-ens omfang (s. 11)

Mål: få et klart bilde av behandlingen(e).

**1.1 Generell beskrivelse:** beskriv behandlingen, formål og innsatser (fotnote 19: svar på «Hva er de forventede fordelene – for organisasjonen, de registrerte, samfunnet?»). Identifiser behandlingsansvarlig og databehandlere.

**1.2 Detaljert beskrivelse:** definer og beskriv omfanget i detalj:
- personopplysningene, mottakerne og lagringstidene;
- prosessene og støtteressursene for hele livssyklusen (fra innsamling til sletting).

Tips:
- Flere behandlinger kan studeres i samme PIA.
- Skill mellom opplysninger som gjelder selve behandlingen og opplysninger som er nødvendige for å gjennomføre tiltak (f.eks. identitetsstyring, tilgangskontroll, logging, samtykke) (fotnote 20).
- Steget revideres hver gang konteksten endres.

### Steg 2 – Tiltak: etterlevelseskomponentene (s. 12–13)

Mål: bygge systemet som sikrer etterlevelse av personvernprinsippene. Tiltak kan lages fra bunnen eller hentes fra god praksis/internasjonale standarder; tidligere hendelser og implementeringsproblemer brukes til forbedring; det er nyttig å fastsette hva som skal skje hvis et tiltak viser seg ineffektivt. Steget revideres til etterlevelse og risikobehandling er tilstrekkelig.

**2.1 Rettslige tiltak (obligatoriske)** – forklar hvordan hvert krav skal oppfylles:
1. formål: spesifisert, uttrykkelig og legitimt;
2. minimering: begrense mengden til det strengt nødvendige;
3. kvalitet: bevare opplysningenes kvalitet (gjelder også koblingen mellom identifiserende opplysninger og opplysningene om personen);
4. lagringstid: nødvendig for formålet, med mindre annen lov krever lengre tid;
5. informasjon: den registrertes rett til informasjon;
6. samtykke: samtykke eller annet behandlingsgrunnlag;
7. innsigelsesrett;
8. innsynsrett;
9. rett til retting og sletting;
10. overføringer ut av EU;
11. forhåndskontroll: formaliteter før behandling (fransk ordning – se Aktualitet).

**2.2 Risikobehandlingstiltak** (eksisterende eller planlagte):
1. organisatoriske: organisering, policy, risikostyring, prosjektstyring, hendelseshåndtering, tilsyn m.m.;
2. logiske sikkerhetstiltak: anonymisering, kryptering, sikkerhetskopier, partisjonering, logisk tilgangskontroll m.m.;
3. fysiske sikkerhetstiltak: fysisk tilgangskontroll, maskinvaresikkerhet, beskyttelse mot ikke-menneskelige risikokilder m.m.

**Anbefalt rekkefølge for valg av tiltak (s. 13):**
1. **Styring av personvern** (governance): tverrgående tiltak – organisering, policy, risikostyring, prosjektstyring.
2. **Personopplysningene**: forebygge brudd – minimere, anonymisere.
3. Hvis utilstrekkelig: **potensielle konsekvenser** – hindre at konsekvenser inntreffer, oppdage og begrense dem (sikkerhetskopier, integritetskontroll, avvikshåndtering).
4. Hvis utilstrekkelig: **risikokildene** – hindre dem i å handle, oppdage/begrense, eller vende seg mot dem (fysisk og logisk tilgangskontroll, kryptering, logging, styring av tredjeparter, beskyttelse mot skadevare).
5. Til sist: **støtteressursene** – hindre utnyttelse av sårbarheter, oppdage og begrense trusler (drift, overvåking, beskytte kanaler, redusere sårbarheter i programvare, maskinvare, papir).

### Steg 3 – Risikoer: potensielle personvernbrudd (s. 14–15)

Mål: god forståelse av risikoenes årsaker og konsekvenser.

**3.1 Risikokilder:** identifiser relevante kilder i den konkrete konteksten (svar på «Hvem eller hva kan være kilde til risiko?») og beskriv deres kapabiliteter. (Typologi: se [K30](K30-cnil-pia-kunnskapsbaser.md) §1.3.)

**3.2 Fryktede hendelser** – tre standardhendelser:
- **uautorisert tilgang** (illegitimate access) – brudd på konfidensialitet;
- **uønsket endring** (unwanted change) – brudd på integritet;
- **forsvinning** (disappearance) – brudd på tilgjengelighet.

For hver: (a) bestem potensielle konsekvenser for de registrerte («Hva frykter vi kan skje med de registrerte?»); (b) estimer alvorlighet, særlig ut fra konsekvensenes skadelighet og eventuelle tiltak som endrer dem; (c) begrunn estimatet formelt.

Eksempler på fryktede hendelser (s. 14):
- Opplysninger om ansattes vaner samles ulovlig uten deres kunnskap og brukes av overordnede for å finne bevis for oppsigelse (f.eks. kameraovervåking).
- Kontaktdata hentes og brukes uten kunnskap til kommersielle formål (spam, målrettet reklame).
- Identiteter forfalskes for å utføre ulovlige handlinger i de registrertes navn, som så blir straffeforfulgt.
- Etter uønsket endring av helseopplysninger får pasienter feil behandling, med forverring, uførhet eller død.
- Søknader om sosiale ytelser forsvinner, slik at mottakerne fratas ytelser og må gjenta formaliteter.

Tips (s. 15): skill mellom eksisterende/planlagte og **tilleggstiltak**, og mellom **initial og residual (gjenværende) alvorlighet**. Konsekvensanalysen kan også brukes til å fastsette sikkerhetsbehov (konfidensialitet, integritet, tilgjengelighet) for kravspesifikasjoner.

**3.3 Trusler:** identifiser trusler mot støtteressursene som kan føre til hver fryktet hendelse («Hvordan kan det skje?»). For hver trussel: velg risikokilder som kan forårsake den; estimer sannsynlighet (sårbarhetsnivå i støtteressursene, kildenes kapabilitet, tiltak som endrer dem); begrunn estimatet.

Eksempler på trusler (s. 15):
- En angriper injiserer uventede spørringer i et skjema på et nettsted.
- En konkurrent på besøk inkognito stjeler en bærbar harddisk.
- En ansatt sletter tabeller i en database ved en feil.
- Vannskade ødelegger servere og telekommunikasjon.

Tips: trusler kan identifiseres empirisk (idémyldring) eller systematisk – for hver støtteressurs vurderes om den kan bli **observert, brukt på annen måte enn planlagt, endret, skadet/ødelagt, mistet eller stjålet**. Det er mulig (men ikke anbefalt) å utelate trusler mot hendelser med ubetydelig eller begrenset alvorlighet, eller kun studere de mest sannsynlige truslene.

**3.4 Risikoer – regel for risikonivå (s. 15):**
- **Risikoens alvorlighet = alvorligheten til den fryktede hendelsen.**
- **Risikoens sannsynlighet = den høyeste sannsynligheten blant truslene knyttet til den fryktede hendelsen.**
- En risiko = én fryktet hendelse + alle trusler som kan gjøre den mulig (fotnote 37).
- Presenter et **kart (risk map)** over alle risikoene etter nivå.

### Skalaer for alvorlighet og sannsynlighet og risikokartet

Metodeguiden fra 2015 viser til skalaene, men selve skalaene står i verktøy-/kunnskapsbasedokumentet. I 2018-utgaven av CNILs kunnskapsbaser ([K30](K30-cnil-pia-kunnskapsbaser.md) s. 4–6) er de slik (gjengitt her for oppslag – innholdet er fra K30, ikke fra dette dokumentet):

**Alvorlighet (severity) – estimeres for fryktede hendelser:**

| Nivå | Generisk beskrivelse av konsekvenser |
|---|---|
| 1. Ubetydelig (Negligible) | De registrerte påvirkes ikke, eller får noen ulemper de overkommer uten problemer. |
| 2. Begrenset (Limited) | Betydelige ulemper som de kan overkomme til tross for noen vanskeligheter. |
| 3. Betydelig (Significant) | Betydelige konsekvenser som de bør kunne overkomme, men med reelle og alvorlige vanskeligheter. |
| 4. Maksimal (Maximum) | Betydelige eller til og med irreversible konsekvenser som de kanskje ikke kan overkomme. |

Justeringsfaktorer (opp/ned): identifiserbarhet, risikokildenes art, antall sammenkoblinger (særlig med utlandet), antall mottakere.

**Sannsynlighet (likelihood) – estimeres for trusler:**

| Nivå | Definisjon | Eksempel (tyveri av papirdokumenter) |
|---|---|---|
| 1. Ubetydelig | Det synes ikke mulig for de valgte risikokildene å realisere trusselen ved å utnytte støtteressursenes egenskaper | lagret i rom med kortleser **og** adgangskode |
| 2. Begrenset | Det synes vanskelig | rom beskyttet med kortleser |
| 3. Betydelig | Det synes mulig | kontorer som krever innsjekk i resepsjonen |
| 4. Maksimal | Det synes ekstremt lett | i den offentlige lobbyen |

Justeringsfaktorer: åpent mot Internett vs. lukket; datautveksling med utlandet; sammenkoblinger; heterogent vs. homogent system; variabelt vs. stabilt system; organisasjonens omdømme.

**Risikokartet:** en 4×4-matrise med alvorlighet (1–4) på y-aksen og sannsynlighet (1–4) på x-aksen der hver av de tre risikoene (uautorisert tilgang, uønsket endring, forsvinning) plasseres – gjerne både initialt og residualt (se mal i [K29](K29-cnil-pia-maler.md) s. 23 og eksempel i [K31](K31-cnil-pia-tilkoblede-objekter.md) s. 35).

### Steg 4 – Beslutning: validering av PIA (s. 16)

Mål: beslutte om måten PIA er håndtert på og de **residuale risikoene** (risiko som gjenstår etter tiltak) kan aksepteres.

- **4.1 Evaluering:** gå gjennom resultatene; kontroller at det ikke er nyttig eller mulig å forbedre hvordan hvert rettslige tiltak er implementert og hvordan hver risiko er behandlet; bestem om de er akseptable, med begrunnelse, særlig sett opp mot innsatsene identifisert tidligere.
- **4.2 Tilfelle 1 – ikke akseptabel:** fastsett mål for de rettslige kravene og risikoene som ikke ble ansett akseptabelt behandlet; gjenta stegene.
- **4.3 Tilfelle 2 – akseptabel: handlingsplan** for planlagte tiltak ved behov. Tiltakene i handlingsplanen skal formaliseres, implementeres, følges opp regelmessig og forbedres kontinuerlig.
- **4.4 Tilfelle 2 – formell validering** av PIA. Beslutningen foregriper ikke en eventuell samsvarsvurdering fra tilsynsmyndigheten (fotnote 39).

### Vedlegg – definisjoner (s. 17–18)

| Begrep | Definisjon (kortfattet gjengivelse) |
|---|---|
| Personopplysning | Enhver opplysning om en identifisert eller identifiserbar fysisk person; alle midler behandlingsansvarlig eller andre kan bruke skal tas i betraktning (DP-Act). |
| Fryktet hendelse (feared event) | Brudd på personopplysningssikkerheten som kan påvirke de registrertes personvern. |
| Risikostyring | Iterativ prosess: vurdere (identifisere, estimere alvorlighet/sannsynlighet, evaluere), behandle (forholdsmessige tiltak), akseptere residual risiko, kommunisere, overvåke endringer. |
| Alvorlighet | Estimat av størrelsen på potensielle konsekvenser; avhenger av konsekvensenes skadelighet. |
| Trussel | Typisk handling, med eller uten hensikt, fra risikokilder som kan forårsake en fryktet hendelse. |
| Tiltak (control) | Handling for å behandle risiko: unngå, redusere, overføre eller beholde. |
| Risiko | Scenario som beskriver en fryktet hendelse og alle trusler som gjør den mulig; estimeres i alvorlighet og sannsynlighet. |
| Risikokilde | Person eller ikke-menneskelig kilde som kan forårsake risiko, ved uhell eller med vilje. |
| Støtteressurs (supporting asset) | Ressurs personopplysninger er avhengige av: maskinvare, programvare, nettverk, personer, papir eller papirbaserte overføringskanaler. |
| Sannsynlighet | Estimat av muligheten for at risikoen inntreffer; avhenger av utnyttbare sårbarheter og kildenes kapabilitet. |
| Sårbarhet | Egenskap ved en støtteressurs som kan utnyttes av risikokilder og la trusler inntreffe. |

Referanser (s. 19): EU-charteret, direktiv 95/46, Ordonnance 2011-1012 (bruddvarsling telekom), DP-Act (lov 78-17), ISO 31000:2009, PIA-guidene, CNILs «Security of Personal Data»-guide, EBIOS (ANSSI 2010).

## Praktiske sjekkpunkter

- Kontroller at DPIA-en dekker begge pilarene: (1) etterlevelse av ufravikelige prinsipper/rettigheter og (2) risikovurdering – risikovurderingen kan aldri «kompensere» for brudd på grunnprinsippene.
- Kontroller at DPIA-en startes i designfasen, ikke etter implementering (s. 8).
- Kontroller at konteksten beskriver hele livssyklusen (innsamling → sletting), mottakere og lagringstider, og identifiserer behandlingsansvarlig og databehandlere.
- Kontroller at opplysninger som genereres av tiltakene selv (logger, identitetsstyring, samtykkeregistrering) er med i omfanget.
- Kontroller at alle tre fryktede hendelser (konfidensialitet, integritet, tilgjengelighet) er vurdert, med konsekvenser *for de registrerte* (ikke for organisasjonen).
- Kontroller at alvorlighet er satt per fryktet hendelse og sannsynlighet per trussel, og at risikoens sannsynlighet = høyeste trusselsannsynlighet.
- Kontroller at hvert estimat har en skriftlig begrunnelse som viser til de faktorene som er brukt.
- Kontroller at initial og residual risiko er skilt, og at tilleggstiltak er skilt fra eksisterende/planlagte.
- Velg tiltak i rekkefølgen styring → data → konsekvenser → kilder → støtteressurser.
- Kontroller at rapporten har minimumsinnholdet (s. 10), inkludert risikokart og handlingsplan.
- Kontroller at roller er fordelt (RACI) og at behandlingsansvarlig formelt validerer.
- Planlegg revisjon minst årlig og ved vesentlige endringer.

## Viktige sitater

- «fundamental principles and rights, which are "non-negotiable", established by law and which must be respected and cannot be subject to any variation, regardless of the nature, severity and likelihood of risks» (s. 4)
- «A risk is a hypothetical scenario that describes: how risk sources ... could exploit the vulnerabilities in personal data supporting assets ... in a context of threats ... and allow feared events to occur ... thus generating impacts on the privacy of data subjects» (s. 6)
- «This is a continuous improvement process. Therefore, it sometimes requires several iterations to achieve an acceptable privacy protection system.» (s. 7)
- «Implementing this approach at the outset makes it possible to determine the necessary and sufficient controls and thus to optimize costs.» (s. 8)
- «its severity equals to that of the feared event concerned by the risk; its likelihood equals the highest likelihood value of the threats associated with the feared event.» (s. 15)
- «It need not be routinely sent, but must be kept available to authorities which may request it.» (s. 10, fotnote 16)
- «The decision in no manner prejudges the conformity assessment that may be made, if necessary, by the data protection authority» (s. 16, fotnote 39)

## Kryssreferanser

- GDPR: art. 35 (DPIA, særlig nr. 7 minimumsinnhold, nr. 2 DPO-råd, nr. 9 de registrertes syn), art. 36 (forhåndsdrøfting ved høy residual risiko), art. 32 (sikkerhet), art. 5 (prinsippene), art. 24 og 25 (ansvar, innebygd personvern); fortalepunkt 75–77, 84, 89–92.
- [K29](K29-cnil-pia-maler.md) – maltabellene som operasjonaliserer stegene.
- [K30](K30-cnil-pia-kunnskapsbaser.md) – skalaer, risikokilder, trusselkataloger og tiltakskatalog.
- [K31](K31-cnil-pia-tilkoblede-objekter.md) – utfylt eksempel (tilkoblet leke).
- [K24](K24-wp248-dpia.md) – WP248: når DPIA kreves og minimumskriterier (CNIL-metoden er nevnt som eksempel på metode i WP248-vedlegget).
- [K23](K23-cnil-risikoark.md) – CNILs risikoark (forenklet risikovurdering).
- [K12](K12-dt-dpia-veiledning.md), [K20](K20-dt-dpia-liste.md), [K21](K21-dt-sjekkliste-dpia-faser.md) – Datatilsynets DPIA-veiledning, liste og fasesjekkliste.
- [K17](K17-digdir-gjennomfore-risikovurdering.md), [K18](K18-digdir-retningslinje-risiko.md), [K19](K19-digdir-risikovurderingsverktoy.md) – Digdirs risikometodikk (organisasjonsrisiko, kan kombineres).
- [K37](K37-sdm-standard-datavernmodell.md) – SDM, alternativ tysk metodikk for tiltak.
- [K33](K33-cnil-sikkerhetsguide.md) – CNILs sikkerhetsguide (tiltak).

## Aktualitet og begrensninger

- Denne utgaven er fra **juni 2015** og bygger på **direktiv 95/46** og den daværende franske personvernloven (DP-Act). Henvisninger til DP-Act art. 6, 7, 32, 34, 38–40, 68–69 og direktivets artikler er ikke direkte anvendelige under GDPR.
- Strukturen «2. Controls» med 11 rettslige krav inkluderer «prior checking» (forhåndskontroll/meldeplikt), en fransk ordning som i stor grad falt bort med GDPR.
- Selve skalaene for alvorlighet og sannsynlighet står ikke i dette dokumentet; de er hentet fra K30 ovenfor.
- **[Merknad – ikke fra kilden]** CNIL publiserte en GDPR-tilpasset **2018-utgave (februar 2018)** av alle tre PIA-guidene (Methodology, Templates, Knowledge Bases). I 2018-metoden heter stegene 1. Kontekst, 2. Grunnleggende prinsipper (proporsjonalitet/nødvendighet og de registrertes rettigheter), 3. Risikoer (datasikkerhet), 4. Validering – jf. strukturen i [K29](K29-cnil-pia-maler.md) og [K31](K31-cnil-pia-tilkoblede-objekter.md). Den kjernemessige risikologikken (fryktede hendelser, trusler, 4-nivå skalaer) er videreført. Brukeren bør helst benytte 2018-utgaven av metodeguiden hvis den er tilgjengelig.
- **[Merknad – ikke fra kilden]** CNIL har også utgitt et gratis, åpen kildekode **PIA-verktøy** (programvare, første versjon ca. 2017–2018, senere oppdatert) som implementerer 2018-metodikken og er oversatt til flere språk. Verktøyet kan være nyttig som praktisk ramme.
- **[Merknad – ikke fra kilden]** I norsk kontekst er forhåndsdrøfting med Datatilsynet (GDPR art. 36) relevant der residual risiko er høy; Datatilsynet anerkjenner ikke én bestemt metode, men CNIL-metoden er en anerkjent og mye brukt tilnærming.

---
id: K15
tittel: "Håndtering av personvernet ved digitale angrep"
utgiver: Datatilsynet
dato: "Udatert i utskriften (nettside skrevet ut 2026-09-22)"
spraak: nb
fil: "ressurser/Datatilsynet/Håndtering av personvernet ved digitale angrep _ Datatilsynet.pdf"
url: "https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/avvik/digitale-angrep/"
type: veileder
gdpr_artikler: [32, 33, 34]
emner: [avvik, brudd-pa-personopplysningssikkerheten, varsling, ddos, phishing, credential-stuffing, direktorsvindel, losepengevirus, ransomware, hendelseshandtering]
relevans: høy
---

# Håndtering av personvernet ved digitale angrep (Datatilsynet)

## Sammendrag
Kort veileder (7 sider i utskrift) fra Datatilsynet om hvordan personvernet skal håndteres når en virksomhet utsettes for digitale angrep. Den beskriver fem vanlige hendelsestyper – tjenestenektangrep (DDoS), phishing, e-postangrep (credential stuffing), direktørsvindel (CEO-fraud) og utpressingsangrep (løsepengevirus/ransomware) – og angir for hver typiske personvernkonsekvenser og om det normalt skal meldes til Datatilsynet. Hovedbudskap: prioriter å håndtere hendelsen; meld til Datatilsynet innen 72 timer selv om informasjonen er midlertidig og ufullstendig, og følg opp med utfyllende melding. DDoS og direktørsvindel har mindre potensial for alvorlige brudd; vellykkede phishing-, e-post- og utpressingsangrep har høy risiko for alvorlige brudd. Veilederen avsluttes med en handlingsliste (krisehåndtering, eksterne aktører, varsling av politi/NSM/Datatilsynet) og fire oppsummerte steg ved mistanke om brudd.

## Når skal agenten bruke denne kilden
- Ved en pågående eller nylig sikkerhetshendelse: avgjøre om det er et brudd på personopplysningssikkerheten og om det skal meldes til Datatilsynet (art. 33) og de registrerte underrettes (art. 34).
- Ved utarbeiding av hendelseshåndterings-/avviksrutiner og beredskapsplaner.
- Ved risikovurdering der trusselscenarioene phishing, ransomware, credential stuffing, DDoS eller CEO-fraud skal beskrives.
- Ved gjennomgang av databehandleravtaler: plikter rundt hendelseshåndtering og bistand ved avvik. **[Merknad – ikke fra kilden]** Kilden omtaler ikke databehandleres varslingsplikt (art. 33 nr. 2) eksplisitt.

## Hovedinnhold

### 1. Innledning (s. 1)
- Alle virksomheter kan utsettes for digitale angrep; motivasjon, metode og alvorlighetsgrad varierer.
- Virksomheter kan være **spesielt sårbare** i perioder knyttet til **høytider, ferieavvikling** og tidspunkt med mer bruk av **vikarer og potensielt uerfarent personell** – vær bevisst bemanning og rutiner også da.
- Sårbarheten og konsekvensene avhenger i stor grad av hvor god struktur virksomheten har på styringen av informasjonssikkerhet og personopplysningssikkerhet (internkontroll).
- Det er viktig å **identifisere typen hendelse**, fordi det har betydning for vurderingen av mulige brudd på personvernet.
- **Ved uklare konsekvenser:** hovedprioritet er egen håndtering av hendelsen. Melding til Datatilsynet i tidlig fase kan inneholde **midlertidig og ufullstendig informasjon**, men det er «viktig og lovpålagt» å sørge for at den første meldingen gis **innen 72-timers fristen**, og at den følges opp med utfyllende informasjon når virksomheten har bedre oversikt.
- **Overordnet (uthevet i kilden):** tjenestenektangrep og direktørsvindel har i mindre grad potensial for alvorlige brudd; vellykkede phishing-, e-post- og utpressingsangrep har høy risiko for alvorlige brudd på personopplysningssikkerheten.
- Hjemler: art. 33 (når og hvilke brudd som skal meldes til Datatilsynet) og art. 34 (når og hvordan de berørte skal informeres).

### 2. Oversikt – hendelsestyper og meldeplikt

| Hendelsestype | Typisk personvernrisiko (kilden) | Meldes til Datatilsynet? |
|---|---|---|
| Tjenestenektangrep (DDoS) | Ofte minimal; kan være alvorlig ved bortfall av kritiske tjenester | Bare hvis det kan medføre risiko for rettigheter og friheter |
| Phishing | Høy; data på avveie eller utilgjengelige | «De fleste vellykkede» – ja |
| E-postangrep (credential stuffing) | Høy; data på avveie eller utilgjengelige | Ja, med mindre det «sannsynligvis ikke vil medføre en risiko» |
| Direktørsvindel (CEO-fraud) | I de fleste tilfeller lav | Vurderes konkret i hvert enkelt tilfelle |
| Utpressingsangrep (ransomware) | Fra lav til katastrofal | Ja hvis uklart om/hvilke opplysninger er på avveie (i påvente av avklaring), og ved påvirket tilgjengelighet/integritet |

### 3. Tjenestenektangrep (DDoS) (s. 2)
- Formål: gjøre en tjeneste utilgjengelig. Teknisk enkle, krever nesten ingen kompetanse, kan kjøpes som tjeneste billig. (Henvisning til Nettvett.no og NSM om forebygging.)
- **Personvern:** i svært mange tilfeller minimale konsekvenser; ofte rettet mot nettsider for signaleffekt; gjerne kortvarige.
- **Konsekvenser:**
  - Ofte ingen personvernkonsekvenser; brudd som «sannsynligvis ikke vil medføre en risiko for fysiske personers rettigheter og friheter» skal **ikke** meldes.
  - Kan likevel ramme personvernet: bortfall av bank- og betalingstjenester (folk får ikke betalt i butikk/restaurant).
  - Ansatte kan selv gjøre endringer i systemet (brannmurer, cacheløsninger o.l.) for å håndtere situasjonen, noe som i ettertid kan føre til **uønsket publisering av personinformasjon**.
  - Bortfall av telenett, kraftnett, helsetjenester eller nødtjenester kan gi alvorlige konsekvenser for personvernet.
- **Regel (uthevet):** Tjenestenektangrep som kan medføre en risiko for fysiske personers rettigheter og friheter, skal meldes til Datatilsynet.

### 4. Phishing (s. 3)
- Starter typisk med e-post eller SMS; lurer mottakeren til å oppgi brukernavn/passord, åpne vedlegg med skadelig kode eller gjennomføre betaling. Brukes for å få tilgang til systemer (e-post, lønn, HR, produksjon, filområder). En av de mest effektive angrepsmåtene; utnytter menneskelige sårbarheter.
- Motivasjon: svært mange vellykkede phishingangrep etterfølges av **utpressingsangrep**; også bedriftsspionasje, statlig spionasje eller økonomisk svindel.
- Virksomheter kan rammes **selv med tofaktor-/flerfaktorautentisering** (sterk autentisering); ulike typer har ulik robusthet, men flere faktorer gjør det uansett vanskeligere.
- Handle raskt for å redusere konsekvensene.
- **Regel (uthevet):** De fleste vellykkede phishingangrep medfører brudd på personopplysningssikkerheten og **må meldes** til Datatilsynet.
- **Personvern og phishing:** kan føre til at opplysninger kommer på avveie eller blir utilgjengelige. En trusselaktør som logger inn med en ansatts konto har minst tilegnet seg ulovlig tilgang til brukernavn og passord – det er derfor ofte «kun et spørsmål om hvor mange personopplysninger bruddet gjelder». Må vite hvilke systemer som behandler personopplysninger og **gjennomgå loggene**.
- **Hvis innbrudd oppdages: bruddet må først og fremst stoppes** (uthevet).
- Konsekvensene kan være betydelige (f.eks. filområder med sykemeldinger og dokumenter om nåværende/tidligere ansatte, kunder m.fl.). Få raskt oversikt over berørte opplysninger for å vurdere om de berørte skal varsles.
- **Innbrudd i e-postkonto:** trusselaktøren kan ha fått tilgang til opplysninger om mange personer. Alle personer det finnes informasjon om i e-poster og kontaktregisteret, samt kontoeieren, må sannsynligvis regnes som berørt. Har kontoen blitt brukt til å sende e-post videre, er også mottakerne berørt. **Ofte minst noen hundre berørte per e-postkonto.** Enkelte kontoer er mer sensitive: HR-ansatte, verneombud, tillitsvalgte, ledere, ansatte i helseforetak.
- **Økonomisk svindel:** kontakt banken så fort som mulig (se også direktørsvindel). Hvis svindelen «sannsynligvis ikke vil medføre en risiko for fysiske personers rettigheter og friheter», trenger den ikke meldes.

### 5. E-postangrep / credential stuffing (s. 4)
- Utnytter at folk gjenbruker brukernavn og passord på tvers av nettkontoer; stjålne påloggingsdetaljer fra urelaterte datainnbrudd brukes; automatiserte og i stor skala.
- Datatilsynet ser klare sammenhenger mellom store datalekkasjer av databaser med brukernavn/passord og angrep mot norske virksomheter (henvisning til digi.no: «26 milliarder poster lekket»; TV 2 utsatt for dataangrep – 18 000 kunder måtte bytte passord).
- Datatilsyn fra mange land har laget felles veiledning om forebygging, oppdagelse og risikoreduksjon (Datatilsynets nyhet 2022).
- **Personvern:** som ved phishing – en trusselaktør som logger inn med gyldig brukernavn/passord har minst tilegnet seg ulovlig tilgang til brukerens profilinformasjon og bekreftelse på at kombinasjonen er i aktiv bruk. Kartlegg systemer og gjennomgå logger; stopp bruddet; få oversikt over berørte opplysninger for å vurdere varsling av de berørte. Meldes ikke hvis det «sannsynligvis ikke vil medføre en risiko».

### 6. Direktørsvindel (CEO-fraud) (s. 5)
- Personer som utgir seg for å være ledelsen forsøker å sette i gang økonomiske transaksjoner. Kanaler: e-post (eksterne og tilsynelatende interne), SMS, fysiske brev, telefon, samt strukturerte kanaler som faktura- og betalingssystemer.
- Store økonomiske konsekvenser; også konsekvenser for personene som ble lurt og gjennomførte transaksjonene i god tro.
- **Personvern:** i de aller fleste tilfeller lav risiko for den enkeltes rettigheter og friheter. Men den eksterne aktøren kan ha kartlagt både personen de utgir seg for og personene de vil lure. **Om det gir grunnlag for å melde avvik, må vurderes i hvert enkelt tilfelle.**
- Kartleggingen – særlig det å utgi seg for å være intern via interne e-postsystemer – kan være støttet av phishing og e-postangrep.

### 7. Utpressingsangrep / løsepengevirus (ransomware) (s. 6)
- Eksterne aktører får adgang til IT-plattformen og **krypterer, sletter og/eller kopierer ut** data; formålet er å presse virksomheten til å betale for å få tilbake tilgang. Trusler om å **publisere stjålet sensitiv informasjon** for å øke betalingssannsynligheten.
- **Alvorlighetsgrad:** fra «irriterende» (data ikke kopiert ut, rask gjenoppretting på egenhånd) til «katastrofal» (sensitive opplysninger på avveie eller virksomhetskritiske data permanent tapt).
- **Kostnader:** fra noen titalls millioner kroner (typisk mellomstor offentlig/privat virksomhet) til flere hundre millioner kroner (større, globale virksomheter).
- **Politiet advarer mot å betale løsepenger:** betalere kan få flere løsepengekrav og andre hendelser; ingen garanti for at systemene åpnes; betaling insentiverer angriperen.
- **Spredningsveier:** ansatt åpner dokument med skadelig kode i e-post; lurt til å gi fra seg brukernavn/passord via phishing/e-postangrep; tilgang via **lekkede brukernavn og passord**; utnyttelse av kjente og ukjente sårbarheter (**zero-day**) eller «bakdører» i programvare.
- **Personvern:**
  - **Lav konsekvens** hvis virksomheten har god kontroll på hvilke personopplysninger som er lagret hvor, opplysningene er godt beskyttet med **tilgangsstyring og kryptering**, og **tilstrekkelig logging** kan dokumentere at personopplysninger ikke er kopiert ut.
  - Er det **uklart om og hvilke** personopplysninger som er på avveie, skal angrepet **meldes til Datatilsynet i påvente av ytterligere avklaring**. Vurder raskt om de registrerte bør varsles.
  - Vurder også om hendelsen i tillegg til brudd på konfidensialitet påvirker **tilgjengelighet** til viktige systemer eller **integritet** (mulig manipulasjon av personopplysninger) – da skal hendelsen også meldes.
- Henvisning til NSMs omfattende veiledning om digital utpressing.

### 8. Hva gjør dere? (s. 7)
**Ved pågående sikkerhetshendelse – prioriter håndtering og få oversikt:**
- Ta i bruk **planen for krisehåndtering** hvis dere har en, og **opprett krisestab**.
- Vurder å involvere **tredjeparter** hvis dere ikke har kompetanse selv – se NSMs liste over godkjente aktører (kvalitetsordning for leverandører som håndterer IKT-hendelser) og Næringslivets Sikkerhetsråds nødplakat for digitale angrep.
- Det finnes tilbydere av **CERT-tjenester** (Computer Emergency Response Team); oversikt på DFØs markedsplassen.anskaffelser.no (SOC- og CERT-tjenester).

**Varsle relevante myndigheter:**
- Datatilsynet anbefaler, på lik linje med Politiet, at **datakriminalitet anmeldes**.
- Vurder om dere skal **varsle NSM** (Nasjonalt cybersikkerhetssenter).
- Ved mistanke om brudd på personopplysningssikkerheten skal det sendes **melding til Datatilsynet innen 72 timer**.

**[Merknad – ikke fra kilden]** Etter art. 33 nr. 1 skal bruddet meldes «uten ugrunnet opphold og når det er mulig, senest 72 timer etter å ha fått kjennskap til det»; fristen løper altså fra kjennskap til et brudd, ikke fra mistanke, og 72 timer er en ytre grense. Meldeplikten gjelder ikke når bruddet «sannsynligvis ikke vil medføre en risiko for fysiske personers rettigheter og friheter» – også for hendelser som påvirker tilgjengelighet eller integritet. Underretning av de registrerte (art. 34) kreves bare ved sannsynlig **høy** risiko (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33)).

**Oppsummert ved mistanke om brudd – fire steg:**
1. Iverksett tiltak for å **stoppe selve bruddet**.
2. Involver og søk råd hos **personvernombudet** tidlig; PVO kan også bidra i dialogen med Datatilsynet.
3. **Kartlegg** hvilke personopplysninger som kan være berørt, **vurder risikoen** for de berørte og **varsle** dem eventuelt.
4. **Meld fra til Datatilsynet** dersom det er aktuelt.

Utfyllende veiledning om brudd på personopplysningssikkerheten (avvik) finnes på Datatilsynets nettsider.

## Praktiske sjekkpunkter
- Kontroller at det finnes en krisehåndteringsplan, definert krisestab og avtale/oversikt over eksterne hendelseshåndterere (NSM-godkjente aktører, CERT/SOC).
- Kontroller at beredskap og rutiner holder også i ferier/høytider og med vikarer.
- Ha oversikt over hvilke systemer som behandler hvilke personopplysninger, og sørg for logging som kan dokumentere hva som er (eller ikke er) eksfiltrert.
- Ved hendelse: stopp bruddet først; involver PVO tidlig; identifiser hendelsestypen.
- Meld til Datatilsynet innen 72 timer ved mistanke om brudd – med foreløpig informasjon om nødvendig – og send oppfølgende melding.
- Ved kompromittert e-postkonto: regn kontoeier, alle personer i e-poster/kontakter og mottakere av e-post sendt fra kontoen som berørt; vær særlig oppmerksom på HR, verneombud, tillitsvalgte, ledere og helseforetak.
- Ved ransomware: meld hvis uklart om data er kopiert ut; vurder også tilgjengelighet og integritet; ikke betal løsepenger (politiets råd); vurder varsling av de registrerte raskt.
- Ved DDoS: meld bare ved risiko (f.eks. bortfall av betalings-, tele-, kraft-, helse- eller nødtjenester); kontroller at nødendringer (brannmur/cache) ikke har eksponert personopplysninger.
- Ved direktørsvindel: vurder konkret om kartlegging av ansatte innebærer brudd; kontakt bank straks ved økonomisk svindel.
- Anmeld datakriminalitet til politiet; vurder varsling til NSM.
- Bruk flerfaktorautentisering, men legg ikke til grunn at den gir full beskyttelse mot phishing.

## Viktige sitater
- «Ved hendelser hvor mulige konsekvenser for personvernet er uklare, skal hovedprioriteringen være egen håndtering av hendelsen.» (s. 1)
- «Det er imidlertid viktig og lovpålagt å sørge for at denne første meldingen gis innen 72-timers fristen» (s. 1)
- «Vellykkede phishing-, epost- og utpressingsangrep, har derimot en høy risiko for alvorlige brudd på personopplysningssikkerheten.» (s. 1)
- «Tjenestenektangrep som kan medføre en risiko for fysiske personers rettigheter og friheter, skal meldes til Datatilsynet.» (s. 2)
- «De fleste vellykkede phishingangrep medfører brudd på personopplysningssikkerheten, og må meldes til Datatilsynet.» (s. 3)
- «Hvis virksomheten oppdager et innbrudd i egne systemer, må bruddet først og fremst stoppes.» (s. 3)
- «Ofte kan det være snakk om minst noen hundre berørte personer per e-postkonto.» (s. 3)
- «Hvis det derimot er uklart om og eventuelt hvilke personopplysninger som er på avveie, skal utpressingsangrep meldes til Datatilsynet i påvente av ytterligere avklaring.» (s. 6)

## Kryssreferanser
- GDPR: art. 32 (sikkerhet), art. 33 (melding til tilsynsmyndigheten innen 72 timer), art. 34 (underretning av den registrerte)
- [K10](K10-dt-kryptering.md) – kryptering som tiltak som reduserer konsekvenser (jf. art. 34 nr. 3 a)
- [K16](K16-dfo-veileder-informasjonssikkerhet.md) – informasjonssikkerhet/internkontroll
- [K32](K32-nsm-grunnprinsipper.md) – NSMs grunnprinsipper for IKT-sikkerhet (forebygging, deteksjon, håndtering)
- [K34](K34-cnil-cybersikkerhet-2024.md), [K33](K33-cnil-sikkerhetsguide.md) – CNILs sikkerhetsveiledning
- [K13](K13-dt-innebygd-personvern.md) – hendelseshåndtering som nøkkelelement for integritet og konfidensialitet
- [K05](K05-dt-databehandleravtale.md) – databehandlers bistand ved avvik

## Aktualitet og begrensninger
- Utskrift 22.09.2026; ingen publiseringsdato i utskriften. Referanser til nyhetssaker fra 2022 og senere.
- Kilden er kort og praktisk orientert; den gjengir ikke innholdet i art. 33 nr. 3 (hva meldingen skal inneholde) eller art. 34 nr. 3 (unntak fra varsling) – disse finnes i Datatilsynets egne avvikssider, som ikke er del av denne kilden. **[Merknad – ikke fra kilden]** Etter art. 33 nr. 1 løper 72-timersfristen fra den behandlingsansvarlige ble kjent med bruddet, og forsinket melding må begrunnes; databehandler skal underrette den behandlingsansvarlige uten ugrunnet opphold (art. 33 nr. 2); alle brudd skal dokumenteres internt (art. 33 nr. 5).
- Norsk kontekst (Politiet, NSM, NSR, DFØ).

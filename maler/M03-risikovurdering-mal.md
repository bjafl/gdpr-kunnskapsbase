---
id: M03
tittel: "Mal – risikovurdering av informasjonssikkerhet og personvern (art. 32)"
gdpr_artikler: [24, 25, 32, 35, 36]
kilder: [K17, K18, K19, K28, K29, K30, K31, K33, K37, K40, K32, K12, K21, K23]
---

# Mal – risikovurdering av informasjonssikkerhet og personvern (art. 32)

*Bruk: Malen dekker sikkerhetsrisikovurderingen som art. 32 krever for alle behandlinger [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md), og kan brukes som risikodel i en DPIA (se [M04](M04-dpia-mal.md)). Den bygger på Digdirs metode ([K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18](../kilder/K18-digdir-retningslinje-risiko.md), [K19](../kilder/K19-digdir-risikovurderingsverktoy.md)) og CNILs PIA-metode ([K28](../kilder/K28-cnil-pia-metode.md), [K30](../kilder/K30-cnil-pia-kunnskapsbaser.md)), med SDM-beskyttelsesmålene ([K37](../kilder/K37-sdm-standard-datavernmodell.md)) for tiltakene. Arbeidsflyt: [A03](../arbeidsflyter/A03-risikovurdering-informasjonssikkerhet.md). Metodebakgrunn: [T09](../temaer/T09-risikovurdering-metoder-og-skalaer.md). Tiltakskatalog: [M09](M09-sikkerhetstiltak-sjekkliste.md).*

*Kursiv tekst er veiledning og fjernes i ferdig dokument. Felt i [hakeparentes] fylles ut.*

---

## 0. Dokumentinformasjon

| Felt | Verdi |
|---|---|
| Tittel | [Risikovurdering – navn på behandling/system] |
| Versjon / dato | [1.0 / ÅÅÅÅ-MM-DD] |
| Risikoeier / systemeier | [navn, rolle] *– den som har mandat og kan akseptere risiko på sitt nivå [K18 kap. 3](../kilder/K18-digdir-retningslinje-risiko.md)* |
| Prosessleder | [navn] *– leder arbeidsgruppen [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md)* |
| Deltakere og roller | [fag/forretning, IT/drift, informasjonssikkerhet (CISO), personvernombud (PVO), leverandør ved behov] *– CNIL: CISO ansvarlig for risikokilder og tiltak, PVO for rettslige tiltak og evaluering [K28 s. 9](../kilder/K28-cnil-pia-metode.md)* |
| Metode og skala | [Anbefalt: Digdir 5-nivå med personvernkategori, se kap. 4 / Alternativ: CNIL 4×4, se vedlegg A] |
| Styrende dokumenter | [Policy for informasjonssikkerhet vX, retningslinje for risiko vX, ...] *– navn og versjon [K17 trinn 1](../kilder/K17-digdir-gjennomfore-risikovurdering.md)* |
| Relatert dokumentasjon | [protokoll (art. 30), DPIA, databehandleravtaler, tidligere risikovurderinger] |
| Neste planlagte revisjon | [dato] *– minst årlig og ved vesentlige endringer [K30 kap. 21](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K28 s. 7](../kilder/K28-cnil-pia-metode.md)* |

---

## 1. Kontekst, formål og omfang

### 1.1 Formål med risikovurderingen

[Tekst]

*Avklar om dette er (a) generell art. 32-vurdering av en behandling, (b) risikodelen av en DPIA, (c) vurdering før anskaffelse/endring/tjenesteutsetting, eller (d) vurdering av spesifikke spørsmål. Spesielle spørsmål kan kreve egen innretning [K17 trinn 1](../kilder/K17-digdir-gjennomfore-risikovurdering.md).*

### 1.2 Beskrivelse av behandlingen

| Felt | Verdi |
|---|---|
| Behandling(er) og formål | [ ] |
| Behandlingsgrunnlag | [ ] *– må være avklart før risikovurderingen; lovlighet kan ikke «risikovurderes bort» [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md), [K28 s. 4](../kilder/K28-cnil-pia-metode.md). Se [T02](../temaer/T02-behandlingsgrunnlag-og-samtykke.md)* |
| Behandlingsansvarlig | [ ] |
| Databehandlere og underdatabehandlere | [navn, tjeneste, lokasjon/land] |
| Kategorier registrerte og omtrentlig antall | [ansatte, kunder, barn, pasienter …; antall] |
| Livsløp | [innsamling → lagring → bruk → utlevering → arkivering → sletting] *– hele livsløpet skal med [K28 s. 11](../kilder/K28-cnil-pia-metode.md)* |

### 1.3 Avgrensning

| Med i vurderingen | Ikke med (begrunnelse) |
|---|---|
| [systemer, prosesser, lokasjoner] | [ ] |

*Noter obs-områder og områder gitt lav prioritet [K17 trinn 2](../kilder/K17-digdir-gjennomfore-risikovurdering.md). En DPIA kan ikke begrenses til én komponent [K40 § 4.1](../kilder/K40-dpia-prosess-uld.md).*

### 1.4 Beskyttelsesbehov for behandlingen (SDM)

| Kriterium | Ja/Nei | Kommentar |
|---|---|---|
| Særlige kategorier (art. 9) eller straffedommer (art. 10) | | *gir som hovedregel «høyt» nivå [K37 9.3](../kilder/K37-sdm-standard-datavernmodell.md)* |
| Fødselsnummer, biometri, genetikk eller andre svært koblingsbare/uforanderlige data | | [K37 9.3](../kilder/K37-sdm-standard-datavernmodell.md), [K10](../kilder/K10-dt-kryptering.md) |
| De registrerte er avhengige av virksomhetens beslutninger/tjenester | | [K37 9.3](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md) |
| Sårbare registrerte (barn, pasienter, ansatte i underordningsforhold) | | |
| Store datamengder / mange roller med ulike rettigheter (kumulativ effekt) | | [K37 9.5](../kilder/K37-sdm-standard-datavernmodell.md) |
| Overføring utenfor EØS | | [K37 9.6](../kilder/K37-sdm-standard-datavernmodell.md); se [T11](../temaer/T11-overforing-tredjeland-og-tia.md) |
| **Konklusjon beskyttelsesnivå** | **[Normal / Høy / Svært høy]** | *aldri lavere enn normal [K37 9.3](../kilder/K37-sdm-standard-datavernmodell.md)* |

### 1.5 DPIA-screening

[Er DPIA gjennomført eller påkrevd? Ja/Nei/Vurderes – henvis til vurdering]

*Vurder mot WP248-kriteriene og Datatilsynets liste; se [T10](../temaer/T10-dpia-art35-36.md) og [A02](../arbeidsflyter/A02-gjennomfore-dpia.md). Risikovurderingen her erstatter ikke DPIA når den er påkrevd [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md).*

---

## 2. Verdier: informasjonstyper og støtteressurser

### 2.1 Informasjonstyper

| ID | Informasjonstype | Personopplysningskategorier | Særlige kategorier? | Konfidensialitet | Integritet | Tilgjengelighet | Lagringssted | Lagringstid |
|---|---|---|---|---|---|---|---|---|
| I1 | [f.eks. kundeprofil] | [navn, kontakt, kjøpshistorikk] | [Nei] | [Lav/Moderat/Høy/Svært høy] | [ ] | [ ] | [system, land] | [ ] |
| I2 | [logger generert av systemet] | [bruker-ID, IP, tidspunkt] | | | | | | |

*Ta med opplysninger som genereres av tiltakene selv (logger, tilgangskontroll, samtykkeregistrering) [K28 s. 11](../kilder/K28-cnil-pia-metode.md). Bruk CNILs typologi: vanlige, oppfattet sensitive (personnummer, biometri, bankdata), sensitive [K30 §1.1](../kilder/K30-cnil-pia-kunnskapsbaser.md). Behovet for K-I-T vurderes ut fra konsekvensen for de registrerte ved brudd [K28 s. 15 tips](../kilder/K28-cnil-pia-metode.md).*

### 2.2 Støtteressurser

| Type | Konkret ressurs | Ansvarlig/leverandør | Merknad |
|---|---|---|---|
| Maskinvare og lagringsmedier | [servere, klienter, mobiler, USB] | | |
| Programvare | [fagsystem, database, OS, SaaS] | | |
| Datakanaler | [internett, VPN, Wi-Fi, API] | | |
| Personer | [brukere, administratorer, leverandørpersonell] | | |
| Papirdokumenter | [utskrifter, skjemaer] | | |
| Papirbaserte kanaler | [post, interne arbeidsflyter] | | |
| Lokaler | [kontor, serverrom, datasenter] | | |

*Typologi fra [K30 §1.2](../kilder/K30-cnil-pia-kunnskapsbaser.md) og [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md).*

### 2.3 Dataflyt

[Diagram eller tabell: kilde → system → mottaker, med kanal og kryptering]

*Dataflytdiagram er grunnlag for arkitektur, tilgangsstyring og logging [K32 1.1.6](../kilder/K32-nsm-grunnprinsipper.md), [K33 ark 1](../kilder/K33-cnil-sikkerhetsguide.md).*

---

## 3. Risikokilder og trusselaktører

| ID | Risikokilde | Type | Motiv/årsak | Kapasitet | Relevant? |
|---|---|---|---|---|---|
| RK1 | [ekstern angriper / kriminelle] | Ekstern, menneskelig, tilsiktet | [økonomisk vinning] | [Moderat] | [Ja] |
| RK2 | [ansatt med legitim tilgang] | Intern, menneskelig, tilsiktet/utilsiktet | [nysgjerrighet, feil] | | |
| RK3 | [databehandler/leverandørpersonell] | Ekstern, menneskelig | | | |
| RK4 | [virksomheten selv – formålsglidning] | Intern | [ny bruk av data] | | *SDM/ULD: organisasjonen selv er en risikokilde [K37 9.6](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md)* |
| RK5 | [offentlige myndigheter i tredjeland] | Ekstern | | | |
| RK6 | [brann, vann, strømbrudd, ikke-målrettet skadevare] | Ikke-menneskelig | | | |

*Typologi: [K30 §1.3](../kilder/K30-cnil-pia-kunnskapsbaser.md). Vurder intensjon og kapasitet [K18 vedlegg H](../kilder/K18-digdir-retningslinje-risiko.md).*

---

## 4. Skalaer, risikomatrise og akseptkriterier

### 4.1 Valg av skala – anbefaling og begrunnelse

**Anbefalt: Digdirs fem-nivåskala (Svært høy – Høy – Moderat – Lav – Ubetydelig) med 5×5-matrise og akseptkriterier fra [K18](../kilder/K18-digdir-retningslinje-risiko.md), der konsekvenskategorien «Personvern» vurderes for den registrerte med CNILs alvorlighetsbeskrivelser fra [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md).**

*Begrunnelse **[Merknad – ikke fra kildene: vurdering basert på kildene]**:*
- *Den er norsk, brukes i offentlig sektor og gjengis av Datatilsynet i DPIA-veiledningen [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md), [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md).*
- *Den har ferdige akseptkriterier knyttet til ledernivå [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md) – CNIL-metoden har ikke det.*
- *Den håndterer konsekvenser både for den registrerte og for virksomheten gjennom konsekvenskategorier, slik at én tabell dekker begge perspektiver [K18 kap. 6.1](../kilder/K18-digdir-retningslinje-risiko.md).*
- *Digdirs personvernrad er grov [K18 Aktualitet](../kilder/K18-digdir-retningslinje-risiko.md); den forsterkes derfor med CNILs konkrete eksempler, som er skrevet fra de registrertes perspektiv [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md).*
- *«Ubetydelig» gir mulighet til å synliggjøre beskrivelser som ikke representerer reell risiko [K18 kap. 6.2](../kilder/K18-digdir-retningslinje-risiko.md).*

*Alternativ: CNILs 4×4 (alvorlighet × sannsynlighet) med mål-typologi – se **vedlegg A**. Velg alternativet når vurderingen inngår i en DPIA etter CNIL-malen ([K29](../kilder/K29-cnil-pia-maler.md)) eller virksomheten ikke har egne akseptkriterier og ønsker et rent personvernperspektiv.*

*Skalaene skal fastsettes før arbeidet starter og ikke justeres underveis [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md). Har virksomheten egne vedtatte skalaer, brukes de [K18 kap. 3.2](../kilder/K18-digdir-retningslinje-risiko.md).*

### 4.2 Konsekvensskala – for den registrerte (kategori «Personvern»)

| Nivå | Digdir-beskrivelse [K18 vedlegg D](../kilder/K18-digdir-retningslinje-risiko.md) | Operasjonalisering med CNIL-eksempler [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
|---|---|---|
| **Svært høy** | Vesentlig hindrer fungering i samfunnet (eller mer) | Betydelige eller irreversible konsekvenser personen kanskje ikke kan overkomme: død, permanent fysisk/psykisk skade, tap av bolig eller arbeid, betydelig gjeld, svindeltap, strafferettslig sanksjon, tap av rettslig autonomi |
| **Høy** | Påvirker fungering i samfunnet | Betydelige konsekvenser med reelle og alvorlige vanskeligheter: langvarig helseskade, feil på bank-/trygdekonti, uriktig profilering, økonomiske vansker, diskriminering, utpressing, nettmobbing, irreversibel krenkelse av privatliv |
| **Moderat** | De fleste ville følt seg krenket | Betydelige ulemper som kan overkommes med noen vanskeligheter: uforutsette gebyrer, nektet tilgang til tjenester, mindre helseplager, objektive men mindre psykiske plager, omdømmeskade, trakassering i sosiale medier |
| **Lav** | Noen kan føle seg krenket | Ulemper som overkommes uten problemer: tidstap, spam, irritasjon, følelse av krenket privatliv uten objektiv skade |
| **Ubetydelig** | Ikke merkbart | Ingen merkbar påvirkning |

***[Merknad – ikke fra kildene]*** *Koblingen mellom Digdir-nivåene og CNIL-nivåene (CNIL 4 → Svært høy, 3 → Høy, 2 → Moderat, 1 → Lav) er malens egen og må godkjennes av risikoeier. Juster nivået opp eller ned for identifiseringsgrad, risikokildenes art, antall sammenkoblinger og antall mottakere [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md).*

### 4.3 Konsekvensskala – for virksomheten

| Nivå | Tjenestenivå / Regelverk [K18 vedlegg D](../kilder/K18-digdir-retningslinje-risiko.md) | Vår økonomi (tilpass beløp) [K18 vedlegg D](../kilder/K18-digdir-retningslinje-risiko.md) | Omdømme / annet [fylles inn] |
|---|---|---|---|
| **Svært høy** | Vesentlig hindrer fungering i samfunnet (eller mer) | > [80 000] | [ ] |
| **Høy** | Påvirker fungering i samfunnet | ≤ [80 000] | [ ] |
| **Moderat** | Et godt merkbart økonomisk eller rettighetsmessig tap | ≤ [20 000] | [ ] |
| **Lav** | Et lite merkbart økonomisk eller rettighetsmessig tap | ≤ [5 000] | [ ] |
| **Ubetydelig** | Ikke merkbart | ≤ [1 000] | [ ] |

*Beløpene er Digdirs eksempler; tilpass slik at økningen langs konsekvensaksen tilsvarer sannsynlighetsaksen (faktor ca. 4) [K18 vedlegg D–E](../kilder/K18-digdir-retningslinje-risiko.md). Legg til HMS ved behov.*

### 4.4 Sannsynlighetsskala

| Nivå | Hyppighet [K18 vedlegg E](../kilder/K18-digdir-retningslinje-risiko.md) | Kvalitativ støtte – sårbarhet og trusselaktør [K18 vedlegg H](../kilder/K18-digdir-retningslinje-risiko.md) | Gjennomførbarhet for risikokilden [K30 §1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
|---|---|---|---|
| **Svært høy** | Over 50 ganger/år (over 1/uke) | Relevante tiltak ikke etablert; aktør med svært sterk motivasjon og høy kapasitet; uhell kan skje tilnærmet uhindret | Synes ekstremt lett |
| **Høy** | Inntil 50/år (inntil 1/uke) | Tiltak lite systematiske, sentrale tiltak mangler; sterk motivasjon; uhell skjer ofte | Synes mulig *[se merknad]* |
| **Moderat** | Inntil 12/år (inntil 1/mnd.) | Tiltak systematiske og risikobaserte, men kan omgås av egne ansatte; en viss motivasjon | Synes vanskelig *[se merknad]* |
| **Lav** | Inntil 3/år (inntil 1 hver 4. mnd.) | Tiltak verifisert at de virker; kan bare omgås med gode ressurser og full kjennskap | Synes ikke mulig |
| **Ubetydelig** | Tilnærmet 0 | Relevante aktører har ingen interesse eller kapasitet | – |

*Bruk hyppighet der det finnes historikk; ellers kvalitativ støtte. De tre faktorene (hyppighet, trusselaktør, sårbarhet) ses i sammenheng, ikke isolert [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md). Sannsynligheten skal gjelde hele forløpet frem til den valgte konsekvensen, og kan aldri være høyere enn sannsynligheten for selve bruddet [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 vedlegg G](../kilder/K18-digdir-retningslinje-risiko.md). **[Merknad – ikke fra kildene]** Plasseringen av CNIL-beskrivelsene i kolonnen til høyre er malens egen tilnærming og bare veiledende.*

### 4.5 Risikomatrise (5×5) [K18 vedlegg C](../kilder/K18-digdir-retningslinje-risiko.md)

| Sannsynlighet ↓ / Konsekvens → | Ubetydelig | Lav | Moderat | Høy | Svært høy |
|---|---|---|---|---|---|
| **Svært høy** | Ubetydelig | Moderat | Høy | Høy | Svært høy |
| **Høy** | Ubetydelig | Moderat | Moderat | Høy | Høy |
| **Moderat** | Ubetydelig | Lav | Moderat | Moderat | Høy |
| **Lav** | Ubetydelig | Lav | Lav | Moderat | Moderat |
| **Ubetydelig** | Ubetydelig | Ubetydelig | Ubetydelig | Ubetydelig | Ubetydelig |

*Risiko er kombinasjonen, ikke produktet, av sannsynlighet og konsekvens [K19](../kilder/K19-digdir-risikovurderingsverktoy.md). Ved konsekvenser langt utenfor matrisens ytterpunkt: håndter som om risikoen var på et høyere nivå [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md).*

### 4.6 Akseptkriterier

| Risikonivå | Kriterier [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md) | Hvem kan akseptere | GDPR-tillegg for personvernrisiko ***[Merknad – ikke fra kildene: syntese]*** |
|---|---|---|---|
| **Lav** | Kan aksepteres uten videre tiltaksvurdering når hele utfallsrommet er lavt | Ledere på alle nivå | – |
| **Moderat** | Vesentlig betydning; systematisk tiltaksarbeid; alternativer uhensiktsmessige eller vesentlig dyrere; nytte/kost; nytten ansees større | Ledere på alle nivå | PVO orienteres |
| **Høy** | Nødvendig; systematisk og grundig tiltaksarbeid; alternativer svært uhensiktsmessige; nytte/kost; nytten er større | Minimum avdelingssjef [tilpass] | Høy restrisiko for de registrerte: PVO-råd; vurder DPIA og forhåndsdrøfting (art. 36) [K23](../kilder/K23-cnil-risikoark.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md) |
| **Svært høy** | Strengt nødvendig; systematisk og svært grundig arbeid; alternativer totalt uhensiktsmessige; nytte/kost; nytten er større | Kun direktør / assisterende direktør [tilpass] | Kan ikke aksepteres internt alene for personvernrisiko; forhåndsdrøfting eller avstå fra behandlingen [K23](../kilder/K23-cnil-risikoark.md), [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md), [K37 kap. 10](../kilder/K37-sdm-standard-datavernmodell.md) |

*Kan en risiko ikke aksepteres og ikke unngås, skal oppgaven ikke gjennomføres eller fortsette [K18 kap. 3.1](../kilder/K18-digdir-retningslinje-risiko.md). Grunnprinsipper og rettigheter er ikke gjenstand for risikoaksept [K28 s. 4](../kilder/K28-cnil-pia-metode.md).*

---

## 5. Uønskede hendelser – identifisering

| Risiko-ID | Risikobeskrivelse: (1) innledende hendelse – (2) brudd – (3) konsekvenser | Fryktet hendelse (K / I / T / personvernmål) | Berørte informasjonstyper | Støtteressurs(er) | Risikokilde(r) | Prioritet (A–D) |
|---|---|---|---|---|---|---|
| R1 | (1) [Phishing mot ansatt med admin-tilgang] (2) [uautorisert tilgang til kundedatabase] (3) [kundedata lekkes og brukes til svindel mot kundene; tilsynssak; omdømmetap] | K | I1 | [fagsystem, e-post, personer] | RK1 | A |
| R2 | (1) [Løsepengevirus via sårbar VPN] (2) [data kryptert og utilgjengelig, ev. eksfiltrert] (3) [tjenester stanset; registrerte får ikke ytelser; ev. lekkasje] | T (+K) | | | | |
| R3 | (1) [Ansatt slår opp på kjente personer] (2) [uautorisert innsyn] (3) [krenkelse av privatliv] | K | | | RK2 | |
| R4 | (1) [Data gjenbrukes til nytt formål] (2) [formålsglidning] (3) [registrerte mister kontroll/forutsigbarhet] | Ikke-kobling / åpenhet | | | RK4 | |
| R5 | (1) [Feil i integrasjon] (2) [uønsket endring av data] (3) [feil vedtak/utbetaling] | I | | | | |
| R6 | (1) [Sletterutine mangler] (2) [data lagres lenger enn nødvendig] (3) [større skadeomfang ved senere brudd] | Dataminimering | | | | |
| R7 | (1) [Registrert ber om innsyn/sletting] (2) [systemet kan ikke finne/slette alle data om personen] (3) [rettigheter ikke oppfylt] | Intervenerbarhet | | | | |

*Veiledning:*
- *Bruk idédugnad i runder: objektet generelt, hver del, obs-områder, oppgaver/tjenester, informasjonstyper, trusselaktører, farer, sårbarheter [K17 trinn 3](../kilder/K17-digdir-gjennomfore-risikovurdering.md). Supplér med trusselkatalogene: for hver støtteressurs – kan den bli observert, brukt upassende, endret, skadet, mistet/stjålet, overbelastet? [K28 s. 15](../kilder/K28-cnil-pia-metode.md), [K30 §1.7–1.9](../kilder/K30-cnil-pia-kunnskapsbaser.md).*
- *Dekk minst de tre fryktede hendelsene uautorisert tilgang, uønsket endring og forsvinning [K28 s. 14](../kilder/K28-cnil-pia-metode.md), [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md). Dekk også personvernmålene dataminimering, ikke-kobling, åpenhet og intervenerbarhet [K37 kap. 5](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md).*
- *Skriv hvilken del (1/2/3) stikkordene hører til [K17 trinn 3](../kilder/K17-digdir-gjennomfore-risikovurdering.md). Berører konsekvensene flere kategorier vesentlig, kan de deles i separate risikoer [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md).*
- *Grovsorter: A høy, B moderat, C lav, D ikke viktig [K17 trinn 3](../kilder/K17-digdir-gjennomfore-risikovurdering.md). Analyser i prioritert rekkefølge.*
- *Uanalyserte risikoer føres i en restliste [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md).*

---

## 6. Eksisterende tiltak

| Tiltak-ID | Eksisterende tiltak | Virker mot risiko-ID | Referanse (M09 / NSM / CNIL) | Effekt dokumentert? (Ja/Nei/Delvis) | Kommentar |
|---|---|---|---|---|---|
| E1 | [MFA for alle administratorer] | R1, R2 | [M09 B3; NSM 2.6.7; CNIL ark 4] | [Ja – konfigurasjonsrapport] | |
| E2 | [Daglig backup, offline-kopi ukentlig] | R2 | [M09 E1; NSM 2.9; CNIL ark 17] | [Delvis – ikke testet siste 12 mnd.] | |

*Gå gjennom [M09](M09-sikkerhetstiltak-sjekkliste.md) først for å få oversikt. Tiltak skal være vurdert (fullstendige og realistiske) før risikoanalysen, fordi de påvirker både alvorlighet og sannsynlighet [K31 3.2](../kilder/K31-cnil-pia-tilkoblede-objekter.md). Å ha et tiltak er ikke nok – beskriv hvordan det virker i dette systemet [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md).*

---

## 7. Risikoanalyse (før nye tiltak)

| Risiko-ID | Konsekvens for den registrerte (nivå) | Begrunnelse | Konsekvens for virksomheten (nivå + kategori) | Begrunnelse | Tilhørende sannsynlighet | Begrunnelse | **Risikonivå** (styrende kategori) | Vurdering: Kan aksepteres / Ikke akseptabel |
|---|---|---|---|---|---|---|---|---|
| R1 | [Høy] | [kontaktdata + kjøpshistorikk for 40 000 kunder; svindelrisiko; CNIL nivå 3] | [Moderat – omdømme/regelverk] | [ ] | [Moderat] | [phishing forekommer jevnlig; MFA reduserer, men admin-konto uten phishing-resistent MFA] | **[Moderat – Personvern]** | [Ikke akseptabel – krever systematisk tiltaksarbeid] |
| R2 | | | | | | | | |

*Veiledning:*
- *Estimer konsekvensen for den registrerte **og** for virksomheten. Risikonivået bestemmes av den kombinasjonen (kategori, konsekvens, tilhørende sannsynlighet) som gir **høyest** risikonivå [K18 kap. 7.2, vedlegg G](../kilder/K18-digdir-retningslinje-risiko.md).*
- *Start med mest forventet konsekvens, men vurder alltid mest fryktet utfall [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md).*
- *Begrunn hvert estimat skriftlig med faktorene som er brukt [K28 s. 14–15](../kilder/K28-cnil-pia-metode.md), [K19 kolonne J og M](../kilder/K19-digdir-risikovurderingsverktoy.md).*
- *Vurderingen i siste kolonne gjøres mot akseptkriteriene i 4.6 [K17 trinn 5](../kilder/K17-digdir-gjennomfore-risikovurdering.md).*

### 7.1 Risikomatrise før tiltak

| Sannsynlighet ↓ / Konsekvens → | Ubetydelig | Lav | Moderat | Høy | Svært høy |
|---|---|---|---|---|---|
| **Svært høy** | | | | | |
| **Høy** | | | | | |
| **Moderat** | | | | [R1] | |
| **Lav** | | | | | |
| **Ubetydelig** | | | | | |

*Plasser risiko-ID-ene. Merk gjerne personvernrisiko med (P) og virksomhetsrisiko med (V).*

---

## 8. Nye tiltak (risikohåndtering og tiltaksplan)

| Tiltak-ID | Tiltak | Mot risiko-ID | Virkning (reduserer konsekvens / sannsynlighet) | Type (forebyggende / oppdagende / korrigerende) | SDM-mål | Referanse (NSM / CNIL ark / CNIL PIA) | Ansvarlig | Frist | Kostnad (ingen/moderat/høy) | Vanskelighetsgrad (lav/moderat/høy) | Status (ikke startet / pågår / fullført) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| N1 | [Phishing-resistent MFA for administratorer] | R1 | [Sannsynlighet] | [Forebyggende] | [Konfidensialitet] | [NSM 2.6.7; CNIL ark 4] | [ ] | [ ] | [ ] | [ ] | [ ] |
| N2 | [Gjenopprettingstest av backup kvartalsvis; offline-kopi] | R2 | [Konsekvens] | [Korrigerende] | [Tilgjengelighet] | [NSM 2.9.3–2.9.4; CNIL ark 17] | | | | | |
| N3 | [Applikasjonslogging av oppslag med varsling ved avvik] | R3 | [Sannsynlighet (avskrekkende) og oppdagelse] | [Oppdagende] | [Åpenhet] | [NSM 3.2; CNIL ark 16] | | | | | |

*Veiledning:*
- *Vurder først om risikoen kan **unngås** (alternativ arbeidsmåte, mindre data) [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md). Tiltak velges i rekkefølgen styring → data → konsekvenser → risikokilder → støtteressurser [K28 s. 13](../kilder/K28-cnil-pia-metode.md).*
- *Risikobehandlingsalternativer: unngå, redusere, overføre, beholde [K28 vedlegg – definisjon av «tiltak»](../kilder/K28-cnil-pia-metode.md).*
- *Velg tiltak etter nytte/kost; for liv og helse etter ALARP [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md). Vurder kostnader og uheldige sideeffekter, også på andre risikoer [K19](../kilder/K19-digdir-risikovurderingsverktoy.md), [K31](../kilder/K31-cnil-pia-tilkoblede-objekter.md).*
- *Høy alvorlighet + høy sannsynlighet: tiltak både før, under og etter hendelsen [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md).*
- *Skalaer for kostnad, vanskelighetsgrad, termin og fremdrift: [K30 §1.10](../kilder/K30-cnil-pia-kunnskapsbaser.md). Handlingsplanen skal ha ansvar, frist, ressurser og målekriterier [K40 § 4.3](../kilder/K40-dpia-prosess-uld.md).*
- *Nye systemer tas som hovedregel ikke i bruk før valgte tiltak er implementert; for eksisterende systemer vurderes midlertidige tiltak eller stans straks [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md).*

---

## 9. Restrisiko (etter nye tiltak)

| Risiko-ID | Konsekvens etter tiltak (registrert / virksomhet) | Sannsynlighet etter tiltak | **Restrisiko** | Begrunnelse | Akseptabel? | Akseptert av (rolle) |
|---|---|---|---|---|---|---|
| R1 | [Høy / Moderat] | [Lav] | **[Moderat]** | [ ] | [Ja] | [ ] |

### 9.1 Risikomatrise etter tiltak

| Sannsynlighet ↓ / Konsekvens → | Ubetydelig | Lav | Moderat | Høy | Svært høy |
|---|---|---|---|---|---|
| **Svært høy** | | | | | |
| **Høy** | | | | | |
| **Moderat** | | | | | |
| **Lav** | | | | [R1] | |
| **Ubetydelig** | | | | | |

*Restrisiko er risikoen som gjenstår etter tiltak [K19](../kilder/K19-digdir-risikovurderingsverktoy.md), [K28 s. 16](../kilder/K28-cnil-pia-metode.md). Høy alvorlighet for de registrerte kan bare aksepteres når sannsynligheten er ubetydelig og alvorligheten ikke kan reduseres [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md).*

---

## 10. Personvernspesifikke konklusjoner

| Spørsmål | Svar | Henvisning |
|---|---|---|
| Er det restrisiko «Høy» eller «Svært høy» i kategorien Personvern? | [Ja/Nei – ID-er] | |
| Tilsier resultatet at DPIA er påkrevd (hvis ikke allerede gjort)? | [ ] | [T10](../temaer/T10-dpia-art35-36.md) |
| Er det høy restrisiko som ikke kan reduseres → forhåndsdrøfting med Datatilsynet (art. 36)? | [ ] | [K23](../kilder/K23-cnil-risikoark.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md), [K30 kap. 16](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Dekker tiltakene alle sju SDM-mål? | [ ] | [K37](../kilder/K37-sdm-standard-datavernmodell.md) |
| Må databehandleravtale/sikkerhetsvedlegg oppdateres? | [ ] | [M01](M01-databehandleravtale-sjekkliste.md), [T07](../temaer/T07-databehandleravtale-art28.md) |
| Må protokoll (art. 30) oppdateres med generell beskrivelse av sikkerhetstiltak? | [ ] | [K12 s. 9](../kilder/K12-dt-dpia-veiledning.md) |
| Råd fra personvernombudet | [tekst / dato] | |

---

## 11. Kvalitet og kunnskapsstyrke

| Felt | Verdi |
|---|---|
| Tidsbruk og gjennomføring | [antall møter, deltakere, tilpasninger av metoden] |
| Hva var bra / hva kunne vært grundigere | [ ] |
| Kunnskapsstyrke samlet | [Svak / Middels / Sterk] *[K17 trinn 6](../kilder/K17-digdir-gjennomfore-risikovurdering.md)* |
| Risikoer med avvikende kunnskapsstyrke | [ID – begrunnelse] |
| Restliste (identifisert, ikke analysert) | [ ] |

*Kunnskapsstyrke = deltakernes kompetanse (kjennskap til objektet, fagkompetanse, analysekompetanse) og grundigheten i analysene; nivået bør samsvare med usikkerheten i sannsynlighetsestimatene [K17 trinn 6](../kilder/K17-digdir-gjennomfore-risikovurdering.md).*

---

## 12. Konklusjon, aksept og signatur

**Oppsummering:** [Kort om generelt risikonivå, spesielt høye risikoer, viktigste tiltak og frister – jf. risikonotatets resultatdel [K17 trinn 5](../kilder/K17-digdir-gjennomfore-risikovurdering.md)]

**Beslutning:**
- [ ] Restrisiko akseptert som beskrevet i kap. 9; tiltak N1–Nx gjennomføres innen fristene.
- [ ] Akseptert under forutsetning av [ ].
- [ ] Ikke akseptert – behandlingen [startes ikke / stanses / endres slik: ].
- [ ] Forhåndsdrøfting med Datatilsynet skal anmodes (ledelsens beslutning) [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md).

| Rolle | Navn | Risikonivå vedkommende kan akseptere | Dato | Signatur |
|---|---|---|---|---|
| Risikoeier / systemeier | | [Lav/Moderat] | | |
| Avdelingssjef | | [Høy] | | |
| Direktør / ass. direktør | | [Svært høy] | | |
| Personvernombud (rådgivende) | | – | | |
| CISO / informasjonssikkerhetsleder (rådgivende) | | – | | |

*Aksept skal skje på et ledernivå som står i forhold til risikoens størrelse [K18 kap. 5](../kilder/K18-digdir-retningslinje-risiko.md). Valideringstekst kan følge CNIL-strukturen: dato – hvem validerer – behandling – formål – begrunnelse – forbehold – signatur [K29](../kilder/K29-cnil-pia-maler.md).*

---

## Vedlegg A – Alternativ skala: CNIL 4×4 (alvorlighet × sannsynlighet)

**Alvorlighet for de registrerte** [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md):

| Nivå | Beskrivelse |
|---|---|
| 1 Ubetydelig | Påvirkes ikke, eller ulemper de overkommer uten problemer |
| 2 Begrenset | Betydelige ulemper de kan overkomme til tross for noen vanskeligheter |
| 3 Betydelig | Betydelige konsekvenser de bør kunne overkomme, men med reelle og alvorlige vanskeligheter |
| 4 Maksimal | Betydelige eller irreversible konsekvenser de kanskje ikke kan overkomme |

*Juster for identifiseringsgrad, risikokildenes art, sammenkoblinger (særlig med utlandet) og antall mottakere.*

**Sannsynlighet** [K30 §1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md):

| Nivå | Beskrivelse (for de valgte risikokildene, ved å utnytte støtteressursenes egenskaper) |
|---|---|
| 1 Ubetydelig | Synes ikke mulig |
| 2 Begrenset | Synes vanskelig |
| 3 Betydelig | Synes mulig |
| 4 Maksimal | Synes ekstremt lett |

*Juster for internett-eksponering, utveksling med utlandet, sammenkoblinger, heterogenitet, variabilitet og omdømme.*

**Regler:** alvorlighet per fryktet hendelse; sannsynlighet per trussel; risikoens sannsynlighet = høyeste trusselsannsynlighet [K28 s. 15](../kilder/K28-cnil-pia-metode.md).

**Risikokart** (alvorlighet ↑, sannsynlighet →) [K28 s. 15](../kilder/K28-cnil-pia-metode.md), [K29](../kilder/K29-cnil-pia-maler.md):

| Alvorlighet ↓ / Sannsynlighet → | 1 Ubetydelig | 2 Begrenset | 3 Betydelig | 4 Maksimal |
|---|---|---|---|---|
| **4 Maksimal** | | | | |
| **3 Betydelig** | | | | |
| **2 Begrenset** | | | | |
| **1 Ubetydelig** | | | | |

**Akseptregler (mål-typologi)** [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md):

| Profil | Mål |
|---|---|
| Alvorlighet 3–4 og sannsynlighet 3–4 | Må absolutt unngås eller reduseres (forebygging, beskyttelse og gjenoppretting) |
| Alvorlighet 3–4, sannsynlighet 1–2 | Unngå/redusere med vekt på forebygging; aksepteres bare hvis alvorligheten ikke kan reduseres og sannsynligheten er ubetydelig |
| Alvorlighet 1–2, sannsynlighet 3–4 | Reduser sannsynligheten, vekt på gjenoppretting; aksepteres bare hvis sannsynligheten ikke kan reduseres og alvorligheten er ubetydelig |
| Alvorlighet 1–2 og sannsynlighet 1–2 | Bør kunne aksepteres |

**Tabellformat (CNIL ark 20)** [K33 ark 20 s. 48](../kilder/K33-cnil-sikkerhetsguide.md):

| Fryktet hendelse | Virkninger for personene | Hovedrisikokilder | Hovedtrusler | Eksisterende/planlagte tiltak | Alvorlighet | Sannsynlighet |
|---|---|---|---|---|---|---|
| Uautorisert tilgang | | | | | | |
| Uønsket endring | | | | | | |
| Tap/forsvinning av data | | | | | | |

---

## Vedlegg B – Utfylt eksempelrad (illustrasjon)

| Felt | Eksempel ***[Merknad – ikke fra kildene: konstruert eksempel]*** |
|---|---|
| Risikobeskrivelse | (1) Angriper finner forutsigbar URL til dokumentarkiv i kundeportal (2) uautorisert tilgang til andre kunders dokumenter (3) lønnsslipper og fødselsnummer på avveie; identitetstyveri; melding til Datatilsynet |
| Fryktet hendelse | Uautorisert tilgang (konfidensialitet) |
| Konsekvens registrert | Høy – fødselsnummer og inntekt muliggjør identitetsmisbruk (CNIL nivå 3) |
| Konsekvens virksomhet | Høy – Regelverk (avvik, tilsynssak) |
| Sannsynlighet | Høy – feilen er en av CNILs hyppigste tilsynsfunn [K34 s. 2](../kilder/K34-cnil-cybersikkerhet-2024.md); portalen er åpen mot internett og ikke sårbarhetstestet [K30 §1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Risikonivå | Høy (matrise: Høy × Høy) |
| Tiltak | Tilgangskontroll på objektnivå, sårbarhetstest før produksjon, ikke personopplysninger i URL [K33 ark 10](../kilder/K33-cnil-sikkerhetsguide.md), [K34 s. 2](../kilder/K34-cnil-cybersikkerhet-2024.md); kryptering av dokumenter; logging av oppslag [K33 ark 16](../kilder/K33-cnil-sikkerhetsguide.md) |
| Restrisiko | Høy konsekvens × Lav sannsynlighet = Moderat |

---
id: T09
tittel: "Risikovurdering – metoder, skalaer og akseptkriterier"
gdpr_artikler: [24, 25, 32, 35, 36]
kilder: [K17, K18, K19, K16, K28, K29, K30, K31, K23, K33, K37, K40, K12, K21, K24, K32]
---

# Risikovurdering – metoder, skalaer og akseptkriterier

Notatet sammenligner risikometodene i kunnskapsbasen – **Digdir** ([K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18](../kilder/K18-digdir-retningslinje-risiko.md), [K19](../kilder/K19-digdir-risikovurderingsverktoy.md)), **CNIL PIA** ([K28](../kilder/K28-cnil-pia-metode.md), [K29](../kilder/K29-cnil-pia-maler.md), [K30](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K31](../kilder/K31-cnil-pia-tilkoblede-objekter.md)) med **CNILs forenklede risikoark** ([K23](../kilder/K23-cnil-risikoark.md), [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md)), **SDM/ULD** ([K37](../kilder/K37-sdm-standard-datavernmodell.md), [K40](../kilder/K40-dpia-prosess-uld.md)) og **DFØs styringsramme** ([K16](../kilder/K16-dfo-veileder-informasjonssikkerhet.md)) – og gjengir alle skalaene side om side. Det forklarer forskjellen mellom *informasjonssikkerhetsrisiko for virksomheten* og *personvernrisiko for den registrerte*, behandler risikoakseptkriterier, og gir en anbefaling om hvilken metode som passer når.

Utfyllbar mal: [M03](../maler/M03-risikovurdering-mal.md). Arbeidsflyt: [A03](../arbeidsflyter/A03-risikovurdering-informasjonssikkerhet.md). Tiltakskatalog: [T08](T08-informasjonssikkerhet-art32.md) og [M09](../maler/M09-sikkerhetstiltak-sjekkliste.md).

## Kjerneregler (kort svar)

1. **GDPR krever risikovurdering i flere sammenhenger:** art. 24, 25, 32 og 35. Felles er en verdivurdering og en trusselvurdering knyttet til personopplysningene og de registrertes rettigheter og friheter [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md).
2. **Sikkerhetsrisikovurdering (art. 32) skal alltid gjøres** før behandlingen og oppdateres regelmessig og ved endringer; **DPIA (art. 35)** kreves når behandlingen sannsynligvis gir høy risiko [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md). Se [T10](T10-dpia-art35-36.md).
3. **Perspektivet er den registrertes.** Konsekvensene skal vurderes for de registrerte, ikke bare for virksomheten [K33 ark 20 s. 49](../kilder/K33-cnil-sikkerhetsguide.md), [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md), [K37 9.1](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 3.1](../kilder/K40-dpia-prosess-uld.md). En virksomhetsmetode (Digdir/ISO) kan brukes, men personvernkategorien må vurderes ut fra de registrertes rettigheter og friheter [K17 Aktualitet](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 Aktualitet](../kilder/K18-digdir-retningslinje-risiko.md).
4. **Risiko = konsekvens/alvorlighet + tilhørende sannsynlighet**, uttrykt som en *kombinasjon* (oppslag i matrise), ikke et produkt [K19](../kilder/K19-digdir-risikovurderingsverktoy.md), [K18 vedlegg A](../kilder/K18-digdir-retningslinje-risiko.md), [K28 s. 6](../kilder/K28-cnil-pia-metode.md).
5. **Skalaene og akseptkriteriene skal fastsettes før vurderingen starter**, ikke justeres underveis [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md), [K17 trinn 1](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 kap. 6](../kilder/K18-digdir-retningslinje-risiko.md).
6. **Velg det verste relevante utfallet**, ikke bare det mest forventede: Digdir krever den kombinasjonen som gir høyest risikonivå [K18 kap. 7.2](../kilder/K18-digdir-retningslinje-risiko.md); CNIL setter risikoens sannsynlighet lik den høyeste blant truslene [K28 s. 15](../kilder/K28-cnil-pia-metode.md).
7. **Restrisiko skal vurderes etter tiltak og aksepteres på riktig nivå** [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md), [K28 s. 16](../kilder/K28-cnil-pia-metode.md). **Høy restrisiko for de registrerte som ikke kan reduseres, utløser forhåndsdrøfting med Datatilsynet (art. 36)** – uavhengig av intern akseptmyndighet [K23 steg 3](../kilder/K23-cnil-risikoark.md), [K30 kap. 16](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md).
8. **Kan en risiko ikke aksepteres og ikke unngås, skal behandlingen ikke gjennomføres** [K18 kap. 3.1](../kilder/K18-digdir-retningslinje-risiko.md), [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md), [K37 kap. 10](../kilder/K37-sdm-standard-datavernmodell.md).
9. **Dokumenter begrunnelsen** for hvert estimat og kunnskapsstyrken bak [K28 s. 14–15](../kilder/K28-cnil-pia-metode.md), [K17 trinn 6](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
10. **Revider** jevnlig (CNIL: minst årlig) og ved vesentlige endringer [K28 s. 7](../kilder/K28-cnil-pia-metode.md), [K30 kap. 21](../kilder/K30-cnil-pia-kunnskapsbaser.md), [K24](../kilder/K24-wp248-dpia.md).

## Rettslig grunnlag

- **Art. 24 nr. 1** – tiltak ut fra «risikoene av varierende sannsynlighet og alvorlighet for fysiske personers rettigheter og friheter» **[Merknad – ikke fra kildene: ordlyd]**.
- **Art. 25 nr. 1** – innebygd personvern ut fra samme risikobegrep [K13](../kilder/K13-dt-innebygd-personvern.md).
- **Art. 32 nr. 1–2** – egnet sikkerhetsnivå ut fra risiko, særlig risiko for tilintetgjøring, tap, endring, ikke-autorisert utlevering eller tilgang. Se [T08](T08-informasjonssikkerhet-art32.md).
- **Art. 35 nr. 1, 3, 7 bokstav c–d, nr. 11** – DPIA ved sannsynlig høy risiko; vurdering av risiko og tiltak; gjennomgang ved endret risiko [K24](../kilder/K24-wp248-dpia.md), [K40 § 3](../kilder/K40-dpia-prosess-uld.md).
- **Art. 36 nr. 1** – forhåndsdrøfting når DPIA viser høy risiko dersom ikke tiltak treffes [K12 s. 6](../kilder/K12-dt-dpia-veiledning.md), [K23](../kilder/K23-cnil-risikoark.md).
- **Fortalepunkt 75–77, 83, 84, 89–94** [K17 Kryssreferanser](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 Kryssreferanser](../kilder/K18-digdir-retningslinje-risiko.md). **[Merknad – ikke fra kildene]** Fortalepunkt 75 beskriver risiko for fysisk, materiell eller immateriell skade (bl.a. diskriminering, identitetstyveri eller -bedrageri, økonomisk tap, omdømmeskade, tap av konfidensialitet for opplysninger underlagt taushetsplikt, uautorisert reversering av pseudonymisering, tap av kontroll); fortalepunkt 76 sier at sannsynlighet og alvorlighet skal fastsettes ut fra behandlingens art, omfang, sammenheng og formål, og vurderes objektivt.
- **Offentlig sektor:** eForvaltningsforskriften § 15 – internkontroll på informasjonssikkerhetsområdet basert på anerkjente standarder, tilpasset risiko [K16 s. 11](../kilder/K16-dfo-veileder-informasjonssikkerhet.md). Digdirs eksempel-retningslinje anbefaler at risikostyring for informasjonssikkerhet og personvern integreres i én felles retningslinje [K18 innledende råd](../kilder/K18-digdir-retningslinje-risiko.md).

## Utdyping

### 1. To risikobegreper: virksomhetens informasjonssikkerhetsrisiko og den registrertes personvernrisiko

| | Informasjonssikkerhetsrisiko (virksomheten) | Personvernrisiko (den registrerte) |
|---|---|---|
| **Hva beskyttes** | Virksomhetens mål, oppgaver og tjenester; IKT-systemer og informasjon («Risiko er mulige avvik fra våre mål») [K18 vedlegg A](../kilder/K18-digdir-retningslinje-risiko.md), [K32 s. 3](../kilder/K32-nsm-grunnprinsipper.md) | Den registrertes rettigheter og friheter (art. 12–22, privatliv, ikke-diskriminering, ytringsfrihet m.m.) [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md) |
| **Typiske konsekvenser** | Tjenestenivå, økonomi, omdømme, regelbrudd, HMS [K18 kap. 6.1](../kilder/K18-digdir-retningslinje-risiko.md) | Fysisk, materiell og moralsk skade for personen [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md); tap av medbestemmelse, åpenhet, forutsigbarhet [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md) |
| **Hvem er risikokilde** | Primært eksterne trusselaktører, uhell, teknisk svikt [K32 s. 5](../kilder/K32-nsm-grunnprinsipper.md) | Også virksomheten selv, legitime interne brukere, databehandlere, myndigheter [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md), [K37 9.6](../kilder/K37-sdm-standard-datavernmodell.md) |
| **Hendelsestyper** | Brudd på konfidensialitet, integritet, tilgjengelighet | De samme tre «fryktede hendelsene» [K28 s. 14](../kilder/K28-cnil-pia-metode.md) – **pluss** risiko fra lovlig, men inngripende behandling (manglende åpenhet, formålsglidning, kobling) [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md), [K37 5.4.2](../kilder/K37-sdm-standard-datavernmodell.md) |
| **Akseptlogikk** | Restrisiko kan aksepteres av ledelsen etter kriterier og nytte/kost [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md) | Grunnprinsippene er «ikke-forhandlingsbare» [K28 s. 4](../kilder/K28-cnil-pia-metode.md); høy restrisiko → forhåndsdrøfting (art. 36); ULD: ingen akseptabel restrisiko i ordinær forstand [K40 § 3.1](../kilder/K40-dpia-prosess-uld.md) |
| **Typisk metode** | Digdir [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md)/[K18](../kilder/K18-digdir-retningslinje-risiko.md), ISO/IEC 27005, NSM 1.1.3 [K32](../kilder/K32-nsm-grunnprinsipper.md) | CNIL PIA [K28](../kilder/K28-cnil-pia-metode.md), SDM [K37](../kilder/K37-sdm-standard-datavernmodell.md), ULD [K40](../kilder/K40-dpia-prosess-uld.md) |

**Konsekvenser for praksis:**
- **Sikkerhetstiltak reduserer ikke nødvendigvis personvernrisiko.** Den behandlingsansvarlige må i DPIA også endre *hvordan* behandlingen utføres og hvordan rettighetene ivaretas [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md).
- **Samme hendelse, ulik alvorlighet.** En lekkasje av en kundeliste kan være «lav» for virksomhetens økonomi, men «betydelig» for de registrerte hvis listen avslører helseforhold. Digdirs metode håndterer dette ved at konsekvenser i ulike kategorier kan behandles som separate risikoer, og ved at den kategorien som gir høyest risikonivå bestemmer [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 vedlegg G](../kilder/K18-digdir-retningslinje-risiko.md).
- **Konflikter må synliggjøres.** Sikkerhetslogging av ansatte eller overvåking av brukere kan redusere virksomhetsrisiko og samtidig øke personvernrisiko; SDM krever at slike tilfeller dokumenteres og begrunnes særskilt, og at personvernnivået går foran ved avvik [K37 9.4](../kilder/K37-sdm-standard-datavernmodell.md).
- DFØ viser at konsekvenser både for virksomheten (mål, økonomi) og for innbyggere/samfunn (rettigheter, livssituasjon, liv og helse) skal inngå i forståelsen av informasjonssikkerhetsrisiko i offentlig sektor [K16 s. 4–5](../kilder/K16-dfo-veileder-informasjonssikkerhet.md).
- **[Merknad – ikke fra kildene]** ISO/IEC 27005 og ISO 31000 definerer risiko som «effekten av usikkerhet på mål»; i et GDPR-løp bør «mål» uttrykkelig omfatte vern av de registrertes rettigheter og friheter. Digdirs konsekvenskategori «Personvern» er en slik operasjonalisering [K18 kap. 6.1](../kilder/K18-digdir-retningslinje-risiko.md).

### 2. Metodene i kortform

#### 2.1 Digdir – «Gjennomføre risikovurdering» med eksempel-retningslinje og Excel-verktøy (K17, K18, K19)

- **Formål:** Operativ risiko i informasjonssikkerhet og internkontroll, særlig offentlig sektor; arbeidsgruppebasert, ledet av prosessleder [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
- **Seks trinn:** (1) felles referanseramme, (2) obs-områder, (3) identifisere risikoer (idédugnad, hendelsesbank, støttemetoder; tredelt risikobeskrivelse; grovsortering A–D), (4) analysere (forstå, estimere konsekvens, tilhørende sannsynlighet, risikonivå), (5) evaluere mot akseptkriterier («Kan aksepteres»/«Ikke akseptabel»), (6) kvalitet og kunnskapsstyrke. Utvides med «Foreslå håndtering av risikoer» [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
- **Risikobeskrivelse:** (1) innledende hendelse – (2) informasjonssikkerhetsbrudd/målavvik – (3) konsekvenser [K17 trinn 3](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 kap. 7.1](../kilder/K18-digdir-retningslinje-risiko.md).
- **Konsekvenskategorier:** Tjenestenivå, Personvern, HMS, Regelverk, Vår økonomi [K18 kap. 6.1](../kilder/K18-digdir-retningslinje-risiko.md).
- **Skalaer:** fem nivåer (Svært høy–Ubetydelig) i retningslinjen [K18 kap. 6.2](../kilder/K18-digdir-retningslinje-risiko.md); **fire nivåer** (Lav–Svært høy) i Excel-verktøyet [K19](../kilder/K19-digdir-risikovurderingsverktoy.md).
- **Akseptkriterier med beslutningsnivå** [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md); tiltak etter ALARP (liv og helse) og nytte/kost [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md).
- **Dokumentasjon:** risikonotat + risikotabell + risikomatrise + restliste [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
- **Styrker:** norsk, integrerer personvern i virksomhetens internkontroll, tydelige akseptkriterier og ledernivåer, kunnskapsstyrke, støtteverktøy. **Svakheter:** virksomhetsperspektiv; personvernskalaen er grov («noen/de fleste ville følt seg krenket»); frekvensbasert sannsynlighetsskala passer dårlig for sjeldne, målrettede hendelser; ingen kobling til art. 36 [K18 Aktualitet](../kilder/K18-digdir-retningslinje-risiko.md), [K17 Aktualitet](../kilder/K17-digdir-gjennomfore-risikovurdering.md).

#### 2.2 CNIL PIA-metoden (K28 metode, K29 maler, K30 kunnskapsbaser, K31 eksempel)

- **Formål:** DPIA; tilpasning av EBIOS til personvern [K28 s. 4](../kilder/K28-cnil-pia-metode.md).
- **To pilarer:** ufravikelige grunnprinsipper og rettigheter + risikostyring for de registrertes personvern [K28 s. 4](../kilder/K28-cnil-pia-metode.md).
- **Fire steg:** 1 Kontekst – 2 Tiltak (rettslige og risikobehandlende) – 3 Risikoer – 4 Beslutning [K28 s. 7–8](../kilder/K28-cnil-pia-metode.md). (2018-utgaven: 1 Kontekst, 2 Grunnprinsipper, 3 Risikoer, 4 Validering [K28 Aktualitet](../kilder/K28-cnil-pia-metode.md), [K29](../kilder/K29-cnil-pia-maler.md).)
- **Risikomodell:** risikokilde → sårbarheter i støtteressurser → trussel → fryktet hendelse (uautorisert tilgang / uønsket endring / forsvinning) → konsekvenser for de registrerte [K28 s. 6](../kilder/K28-cnil-pia-metode.md). Alvorlighet settes per fryktet hendelse, sannsynlighet per trussel; risikoens sannsynlighet = høyeste trusselsannsynlighet [K28 s. 15](../kilder/K28-cnil-pia-metode.md).
- **Skalaer:** fire nivåer for alvorlighet og sannsynlighet med eksempler og justeringsfaktorer [K30 §1.5–1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md). Trusselkataloger per støtteressurs [K30 §1.7–1.9](../kilder/K30-cnil-pia-kunnskapsbaser.md). Tiltakskatalog kap. 2–43 [K30](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- **Akseptlogikk:** evaluering → mål → handlingsplan → formell validering; typologi av mål etter risikoprofil [K28 s. 16](../kilder/K28-cnil-pia-metode.md), [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md).
- **Styrker:** den registrertes perspektiv, svært konkrete skalaer og kataloger, ferdige maler og utfylt eksempel, kobling til art. 36. **Svakheter:** fransk kontekst (2015/2018), ingen eksplisitt risikomatrise med nivåer eller ledernivåer for aksept; tung for små behandlinger [K28 Aktualitet](../kilder/K28-cnil-pia-metode.md), [K30 Aktualitet](../kilder/K30-cnil-pia-kunnskapsbaser.md).

#### 2.3 CNILs forenklede risikoanalyse (K23 infografikk og K33 ark 20)

- **K23** (2017): screening mot ni kriterier → vurdering av hver fryktet hendelse (alvorlighet = virkninger + data; sannsynlighet = risikokilder + støtteressurser) → tiltak → høy restrisiko? → forhåndsdrøfting [K23](../kilder/K23-cnil-risikoark.md). Ingen skalaer.
- **K33 ark 20** (2024): «risikoanalyse, selv minimal» i tre trinn: (1) identifiser behandlinger, data og støttemedier; (2) for hver behandling – virkninger for tre fryktede hendelser, risikokilder, trusler (brukt upassende, endret, tapt, observert, skadet, overbelastet), eksisterende/planlagte tiltak, alvorlighet og sannsynlighet (eksempelskala «ubetydelig, moderat, stor, maksimal»); (3) iverksett og kontroller tiltak. Tabellmal med sju kolonner [K33 ark 20 s. 47–49](../kilder/K33-cnil-sikkerhetsguide.md).
- **Egnet for:** behandlinger som ikke krever DPIA, men der art. 32 krever en dokumentert vurdering.

#### 2.4 SDM og ULDs DPIA-prosess (K37, K40)

- **Formål:** omsette rettslige krav til tiltak via **sju beskyttelsesmål** (dataminimering, tilgjengelighet, integritet, konfidensialitet, ikke-kobling, åpenhet, intervenerbarhet) [K37 kap. 5](../kilder/K37-sdm-standard-datavernmodell.md).
- **Beskyttelsesnivå** (normal / høy / svært høy) fastsettes ut fra **inngrepsintensitet for den registrerte** – aldri lavere enn normal [K37 9.3](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md). Systemer og prosesser arver nivået fra dataene [K37 kap. 8](../kilder/K37-sdm-standard-datavernmodell.md).
- **Risikoevaluering** som **mål–faktisk-sammenligning** mot referansetiltak; avvik vektes etter hvor mye de truer måloppnåelsen; alternative tiltak må være funksjonelt likeverdige [K37 10.3](../kilder/K37-sdm-standard-datavernmodell.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md).
- **Tilleggsrisikoanalyse** av fire aspekter: organisasjonens motivasjon og muligheter for uautorisert formålsendring, tredjelandsoverføring, og omfanget av informasjonssikkerhetstiltak [K37 9.6](../kilder/K37-sdm-standard-datavernmodell.md).
- **ULDs tre faser:** A Forberedelse (scoping-rapport) – B Evaluering – C Rapport og tiltak (handlingsplan med tiltak, ansvar, frist, målekriterier; publisering; uavhengig revisjon) [K40 § 4](../kilder/K40-dpia-prosess-uld.md).
- **Styrker:** dekker personvernmålene (ikke bare K-I-T), sterk kobling til GDPR-artikler, egnet for tiltaksvalg og revisjon. **Svakheter:** ingen sannsynlighetsskala eller matrise i v1.0; referansekatalogen ikke med i v1.0; tysk kontekst; standpunktet om «ingen akseptabel restrisiko» avviker fra WP29/CNIL [K37 Aktualitet](../kilder/K37-sdm-standard-datavernmodell.md), [K40 Aktualitet](../kilder/K40-dpia-prosess-uld.md).

#### 2.5 DFØ – styringsramme (K16)

DFØ-veilederen er **ingen risikometode**, men plasserer risikovurdering i virksomhetsstyringen: Digdirs internkontrollmodell med syv områder (ledelsens styring og oppfølging, risikovurdering, risikohåndtering, overvåking og hendelseshåndtering, måling/evaluering/revisjon, kompetanse og kulturutvikling, kommunikasjon), skillet mellom styringsaktiviteter og sikkerhetstiltak, og at «risikostyring» og «internkontroll» i praksis er det samme med risikobasert tilnærming [K16 s. 5, 9](../kilder/K16-dfo-veileder-informasjonssikkerhet.md). Bruk den til å forankre risikovurderingen hos ledelsen og i styringsdialogen (offentlig sektor).

#### 2.6 NSM som ramme for risikoprosessen (K32)

NSM 1.1.3 lister elementene i en IKT-risikoprosess (verdivurdering, trusselvurdering, eksisterende tiltak, identifisering, vurdering, rapportering, håndtering, etablere/justere tiltak, verifisere) og 1.1.4 krever toleransegrenser fastsatt av ledelsen, gjerne basert på konsekvens ved tap av konfidensialitet, integritet og tilgjengelighet [K32 1.1.3–1.1.4](../kilder/K32-nsm-grunnprinsipper.md). NSM nevner ISO/IEC 27005, NIST SP 800-30 og OCTAVE Allegro som eksempler på metoder [K32 s. 11–12](../kilder/K32-nsm-grunnprinsipper.md).

### 3. Skalaene side om side

#### 3.1 Konsekvens / alvorlighet

| Rang | Digdir retningslinje (K18 vedlegg D) – Personvern | Digdir – Vår økonomi | Digdir Excel (K19) | CNIL PIA (K30 §1.5) – alvorlighet for de registrerte | CNIL ark 20 (K33) | SDM/ULD beskyttelsesnivå (K37 9.3, K40) |
|---|---|---|---|---|---|---|
| 0 | **Ubetydelig** – ikke merkbart | Tap ≤ 1 000 | – | – | – | – (aldri lavere enn normal) |
| 1 | **Lav** – noen kan føle seg krenket | ≤ 5 000 | **Lav (1)** | **1 Ubetydelig** – påvirkes ikke, eller ulemper de overkommer uten problemer | Ubetydelig | **Normal** – ingen scenarier med potensial for høy inngrepsintensitet |
| 2 | **Moderat** – de fleste ville følt seg krenket | ≤ 20 000 | **Moderat (2)** | **2 Begrenset** – betydelige ulemper de kan overkomme til tross for noen vanskeligheter | Moderat | |
| 3 | **Høy** – påvirker fungering i samfunnet | ≤ 80 000 | **Høy (3)** | **3 Betydelig** – betydelige konsekvenser de bør kunne overkomme, men med reelle og alvorlige vanskeligheter | Stor | **Høy** – f.eks. art. 9-data, avhengighet, alvorlige konsekvenser, mangel på effektive garantier |
| 4 | **Svært høy** – vesentlig hindrer fungering i samfunnet (eller mer) | > 80 000 | **Svært høy (4)** | **4 Maksimal** – betydelige eller irreversible konsekvenser de kanskje ikke kan overkomme | Maksimal | **Svært høy** – eksistensiell/vital avhengighet + tilleggsrisiko som den registrerte ikke kan oppdage/rette |

**Viktig:** Raden «Rang» og plasseringen på samme linje er en **indikativ sammenstilling** for oversettelse mellom metodene **[Merknad – ikke fra kildene]**. Kildene definerer ikke en slik ekvivalens. SDM-nivåene er ikke en konsekvensskala for én hendelse, men et beskyttelsesbehov for hele behandlingen. Digdirs beløpsgrenser er illustrative [K18 Aktualitet](../kilder/K18-digdir-retningslinje-risiko.md).

**CNIL-eksempler på konsekvenser** (utdrag fra [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md)):
- *1 Ubetydelig:* tidstap ved å gjenta formaliteter, spam, irritasjon, følelse av krenket privatliv uten reell skade.
- *2 Begrenset:* uforutsette betalinger/gebyrer, nektet tilgang til tjenester, mindre fysiske plager, mindre men objektive psykiske plager, trakassering i sosiale medier.
- *3 Betydelig:* alvorlige fysiske plager med langvarig skade, feil på konti, uriktig profilering, underslag som ikke erstattes, alvorlige psykiske plager, diskriminering, utpressing, nettmobbing.
- *4 Maksimal:* død, permanent skade, tap av bolig eller arbeid, betydelig gjeld, strafferettslig sanksjon, tap av rettslig autonomi.

**Justeringsfaktorer for alvorlighet** (CNIL): identifiseringsgrad, risikokildenes art, antall sammenkoblinger (særlig med utlandet), antall mottakere [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md). **Faktorer som løfter SDM-nivå:** særlige kategorier, uforanderlige data (biometri, genetikk), svært koblingsbare identifikatorer, risiko for diskriminering/stigmatisering, avhengighet, kumulative effekter (store datamengder, mange roller) [K37 9.3, 9.5](../kilder/K37-sdm-standard-datavernmodell.md).

**Digdirs øvrige konsekvenskategorier** [K18 vedlegg D](../kilder/K18-digdir-retningslinje-risiko.md): Tjenestenivå og Regelverk (ikke merkbart → et lite merkbart økonomisk eller rettighetsmessig tap → godt merkbart tap → påvirker fungering i samfunnet → vesentlig hindrer fungering i samfunnet); HMS (behandlingsbehov og sykemeldingslengde).

#### 3.2 Sannsynlighet

| Rang | Digdir retningslinje (K18 vedlegg E) – hyppighet | Digdir vedlegg H – sårbarhet (tiltaksetablering) | Digdir Excel (K19) | CNIL PIA (K30 §1.6) – gjennomførbarhet for risikokilden | CNIL ark 20 (K33) |
|---|---|---|---|---|---|
| 0 | **Ubetydelig** – tilnærmet 0 | Relevante aktører har ingen interesse/kapasitet | – | – | – |
| 1 | **Lav** – inntil 3/år (inntil 1 hver 4. mnd.) | Tiltak systematiske, risikobaserte og verifisert at de virker | **Lav (1)** | **1 Ubetydelig** – synes ikke mulig (eks.: rom med kortleser **og** kode) | Ubetydelig |
| 2 | **Moderat** – inntil 12/år (inntil 1/mnd.) | Tiltak systematiske og risikobaserte | **Moderat (2)** | **2 Begrenset** – synes vanskelig (rom med kortleser) | Moderat |
| 3 | **Høy** – inntil 50/år (inntil 1/uke) | Tiltak i liten grad systematiske; sentrale tiltak mangler | **Høy (3)** | **3 Betydelig** – synes mulig (kontor med innsjekk i resepsjon) | Stor |
| 4 | **Svært høy** – over 50/år (over 1/uke) | Relevante tiltak ikke etablert | **Svært høy (4)** | **4 Maksimal** – synes ekstremt lett (offentlig lobby) | Maksimal |

(Rangering og radplassering er indikativ **[Merknad – ikke fra kildene]**.)

**Merk forskjellen i karakter:** Digdir uttrykker sannsynlighet som **hyppighet per år** (faktor ca. 4 mellom nivåene, samme som økonomiskalaen) [K18 vedlegg E](../kilder/K18-digdir-retningslinje-risiko.md), supplert med kvalitativ støtte om trusselaktørens intensjon og kapasitet og sårbarhet [K18 vedlegg H](../kilder/K18-digdir-retningslinje-risiko.md). CNIL uttrykker sannsynlighet som **hvor lett risikokilden kan realisere trusselen** gitt støtteressursenes sårbarheter og eksisterende tiltak [K30 §1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md). For sjeldne, tilsiktede personvernbrudd er CNIL-skalaen ofte lettere å bruke; Digdir-skalaen passer best for hyppige driftshendelser **[Merknad – ikke fra kildene: vurdering]**.

**Justeringsfaktorer for sannsynlighet** (CNIL): åpent mot internett vs. lukket, datautveksling med utlandet, sammenkoblinger, heterogent/homogent, variabelt/stabilt system, organisasjonens omdømme [K30 §1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md). **Digdirs tre faktorer** (ses i sammenheng, ikke isolert): historisk hyppighet, trusselaktørens intensjon og kapasitet, sårbarhetsnivå/tiltaksstyrke [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 vedlegg H](../kilder/K18-digdir-retningslinje-risiko.md).

**Digdir vedlegg H – trusselaktør** (utdrag): *Svært høy* – svært sterk motivasjon direkte mot oss, kompetanse til å overvinne svært avanserte tiltak; *Høy* – sterk motivasjon mot vår type virksomhet; *Moderat* – en viss motivasjon, kan overvinne enkle tiltak; *Lav* – svært liten interesse, lav kompetanse [K18 vedlegg H](../kilder/K18-digdir-retningslinje-risiko.md).

**SDM** har ingen sannsynlighetsskala; i stedet vurderes sannsynligheten for at organisasjonen *ikke* etterlever reglene til tross for tiltakene, ut fra motivasjon og operative muligheter for formålsendring, tredjelandsforhold og informasjonssikkerhetstiltak [K37 9.6](../kilder/K37-sdm-standard-datavernmodell.md).

#### 3.3 Risikomatriser

**Digdir retningslinje – 5×5** [K18 vedlegg C](../kilder/K18-digdir-retningslinje-risiko.md) (rader = sannsynlighet, kolonner = konsekvens):

| Sannsynlighet ↓ / Konsekvens → | Ubetydelig | Lav | Moderat | Høy | Svært høy |
|---|---|---|---|---|---|
| **Svært høy** | Ubetydelig | Moderat | Høy | Høy | Svært høy |
| **Høy** | Ubetydelig | Moderat | Moderat | Høy | Høy |
| **Moderat** | Ubetydelig | Lav | Moderat | Moderat | Høy |
| **Lav** | Ubetydelig | Lav | Lav | Moderat | Moderat |
| **Ubetydelig** | Ubetydelig | Ubetydelig | Ubetydelig | Ubetydelig | Ubetydelig |

**Digdir Excel-verktøy – 4×4** [K19](../kilder/K19-digdir-risikovurderingsverktoy.md) (standardverdier; kan endres):

| Sannsynlighet ↓ / Konsekvens → | Lav | Moderat | Høy | Svært høy |
|---|---|---|---|---|
| **Svært høy** | Moderat | Høy | Høy | Svært høy |
| **Høy** | Moderat | Moderat | Høy | Høy |
| **Moderat** | Lav | Moderat | Moderat | Høy |
| **Lav** | Lav | Lav | Moderat | Moderat |

Fargekoder: Lav grønn, Moderat gul, Høy oransje, Svært høy rød [K19](../kilder/K19-digdir-risikovurderingsverktoy.md). 4×4-matrisen er identisk med 5×5-matrisen uten «Ubetydelig»-raden og -kolonnen.

**CNIL – risikokart 4×4** [K28 s. 15](../kilder/K28-cnil-pia-metode.md), [K29](../kilder/K29-cnil-pia-maler.md), [K31](../kilder/K31-cnil-pia-tilkoblede-objekter.md): alvorlighet (1–4) på y-aksen, sannsynlighet (1–4) på x-aksen; hver fryktet hendelse plasseres, gjerne både initialt og residualt. CNIL gir **ingen fast nivåinndeling av cellene**, men en **typologi av mål** etter risikoprofil [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md):

| Risikoprofil | Mål |
|---|---|
| Høy alvorlighet og høy sannsynlighet (3–4/3–4) | Må absolutt unngås eller reduseres med tiltak på både alvorlighet og sannsynlighet; uavhengige tiltak for forebygging, beskyttelse og gjenoppretting |
| Høy alvorlighet, lav sannsynlighet (3–4/1–2) | Må unngås eller reduseres; vekt på forebygging. Kan bare aksepteres hvis alvorligheten ikke kan reduseres **og** sannsynligheten er ubetydelig |
| Lav alvorlighet, høy sannsynlighet (1–2/3–4) | Må reduseres med tiltak på sannsynlighet; vekt på gjenoppretting. Kan bare aksepteres hvis sannsynligheten ikke kan reduseres **og** alvorligheten er ubetydelig |
| Lav alvorlighet og lav sannsynlighet (1–2/1–2) | Bør kunne aksepteres |

**Merk asymmetrien:** I Digdir-matrisen gir Svært høy sannsynlighet × Lav konsekvens og Lav sannsynlighet × Svært høy konsekvens begge «Moderat». CNIL-typologien behandler høy alvorlighet strengere: den kan bare aksepteres når sannsynligheten er *ubetydelig*. For personvernrisiko bør høy alvorlighet derfor vektes tyngre enn matrisen alene tilsier – Digdir åpner selv for dette: risikoer med konsekvenser «langt utenfor matrisens normale ytterpunkt» skal håndteres som om de var på et høyere nivå [K18 kap. 4](../kilder/K18-digdir-retningslinje-risiko.md).

#### 3.4 Kunnskapsstyrke og handlingsplanskalaer

| Skala | Nivåer | Kilde |
|---|---|---|
| Kunnskapsstyrke (metodesiden) | svak – middels – sterk | [K17 trinn 6](../kilder/K17-digdir-gjennomfore-risikovurdering.md) |
| Kunnskapsstyrke (retningslinjen) | lav – moderat – høy | [K18 kap. 7.3 tillegg C](../kilder/K18-digdir-retningslinje-risiko.md) |
| Handlingsplan: vanskelighetsgrad | lav – moderat – høy | [K30 §1.10](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Handlingsplan: kostnad | ingen – moderat – høy | [K30 §1.10](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Handlingsplan: termin | kvartal – år – 3 år (K31: år – kvartal – måned) | [K30 §1.10](../kilder/K30-cnil-pia-kunnskapsbaser.md) |
| Handlingsplan: fremdrift | ikke startet – pågår – fullført | [K30 §1.10](../kilder/K30-cnil-pia-kunnskapsbaser.md) |

### 4. Regler for å sette nivåer

**Digdir** [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18 kap. 7.2, vedlegg G](../kilder/K18-digdir-retningslinje-risiko.md):
1. Anslå *innledende sannsynlighet* (at hendelsen skjer og gir målavvik).
2. Finn berørte konsekvenskategorier og *mest forventet* konsekvensnivå per kategori; høyeste gir foreløpig hovedkategori.
3. Anslå *tilhørende sannsynlighet* for dette konsekvensnivået – den kan **aldri være høyere** enn den innledende.
4. Vurder andre kategorier og andre kombinasjoner (særlig *mest fryktet* utfall); velg kombinasjonen med **høyest risikonivå**.
5. Ubetydelig konsekvens eller sannsynlighet gir alltid ubetydelig risiko [K18 kap. 6.2](../kilder/K18-digdir-retningslinje-risiko.md).
6. Digdir anbefaler å starte med konsekvensen og deretter vurdere sannsynligheten for at hendelsen inntreffer med den konsekvensen [K19](../kilder/K19-digdir-risikovurderingsverktoy.md).

**CNIL** [K28 s. 14–15](../kilder/K28-cnil-pia-metode.md), [K30 §1.5–1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md):
1. For hver fryktet hendelse: hva frykter vi kan skje med de registrerte? Estimer **alvorlighet** (med eksisterende/planlagte tiltak), juster med faktorene, begrunn.
2. For hver trussel mot støtteressursene: hvilke risikokilder? Estimer **sannsynlighet** (sårbarhet × kildens kapabilitet, med tiltak), juster, begrunn.
3. Risikoens alvorlighet = den fryktede hendelsens; risikoens sannsynlighet = **høyeste** av truslene.
4. Skill **initial** og **residual** risiko, og eksisterende/planlagte fra **tilleggstiltak** [K28 s. 15](../kilder/K28-cnil-pia-metode.md).
5. Systematisk trusselidentifikasjon: for hver støtteressurs – kan den bli observert, brukt på annen måte, endret, skadet, mistet/stjålet, overbelastet? [K28 s. 15](../kilder/K28-cnil-pia-metode.md), [K30 §1.7–1.9](../kilder/K30-cnil-pia-kunnskapsbaser.md).

**SDM** [K37 9.3–9.5, 10.2](../kilder/K37-sdm-standard-datavernmodell.md): fastsett beskyttelsesnivå for dataene (arves av systemer og prosesser), vurder kumulative effekter, presiser kvantitativt (akseptabel nedetid, aktualitet, sporbarhet, frister for rettigheter), og sammenlign tiltak mot referansetiltak.

### 5. Risikoakseptkriterier

#### 5.1 Digdir – kriterier og beslutningsnivå [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md)

| Risikonivå | Vilkår for aksept | Hvem kan akseptere |
|---|---|---|
| **Lav** | Kan aksepteres uten videre tiltaksvurdering – når *hele utfallsrommet* er lavt i alle berørte kategorier | Ledere på alle nivå |
| **Moderat** | Vesentlig betydning for målene; systematisk tiltaksarbeid; alternativer uhensiktsmessige/høyere risiko/vesentlig dyrere; ALARP og nytte/kost; nytten ansees større enn risikoen | Ledere på alle nivå |
| **Høy** | Nødvendig for målene; systematisk og grundig arbeid; alternativer svært uhensiktsmessige/svært kostbare; ALARP og nytte/kost; nytten er større | Minimum avdelingssjef |
| **Svært høy** | Strengt nødvendig; systematisk og svært grundig arbeid; alternativer totalt uhensiktsmessige eller utenfor økonomisk handlingsrom; ALARP og nytte/kost; nytten er større | Kun direktør eller assisterende direktør |

Prinsipper: aksept bare når risikoen er lav eller etter risikohåndtering; ledernivå i forhold til risikoens størrelse; nye systemer tas som hovedregel ikke i bruk før valgte tiltak er implementert; for eksisterende systemer vurderes straks midlertidige tiltak eller stans [K18 kap. 4–5](../kilder/K18-digdir-retningslinje-risiko.md).

#### 5.2 CNIL

- Validering av DPIA når rettslige tiltak og risikobehandling er akseptable sett opp mot innsatsene (stakes); ellers settes mål og stegene gjentas; tre utfall: validert, betinget av forbedring, avvist [K28 s. 16](../kilder/K28-cnil-pia-metode.md), [K31](../kilder/K31-cnil-pia-tilkoblede-objekter.md).
- Lav restrisiko → behandlingen kan gjennomføres; høy restrisiko + flere tiltak mulig → nye tiltak; høy restrisiko + ingen ytterligere tiltak → **plikt til å konsultere tilsynsmyndigheten**; planlagte tiltak skal være implementert før behandlingen starter [K23 steg 3](../kilder/K23-cnil-risikoark.md).
- Typologi av mål (se 3.3) [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md). «Noen risikoer kan ikke tas», særlig ved sensitive data eller svært betydelige skader – da kan behandlingen (delvis) måtte unngås [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md).

#### 5.3 ULD/SDM

- «Unlike in risk management, there is no acceptable residual risk» – enhver behandling er et inngrep som må begrunnes; ingen *de minimis*-aksept fordi få personer berøres [K40 § 3.1, § 4.3](../kilder/K40-dpia-prosess-uld.md).
- Kan risiko ikke reduseres tilstrekkelig, kan konklusjonen være å **avstå fra behandlingen** [K37 kap. 10](../kilder/K37-sdm-standard-datavernmodell.md).
- **[Merknad – ikke fra kildene / jf. K40 Aktualitet]** Dette er ULDs/SDMs perspektiv; WP248/EDPB, Datatilsynet og CNIL bruker en risikobasert tilnærming der restrisiko vurderes og høy restrisiko utløser forhåndsdrøfting. Etter kildehierarkiet [_KONVENSJONER](../_KONVENSJONER.md) går EDPB/WP29 og Datatilsynet foran ULD.

#### 5.4 Samlet anbefaling for akseptkriterier i GDPR-sammenheng

**[Merknad – ikke fra kildene: syntese]**
1. **Grunnprinsipper og rettigheter er ikke gjenstand for risikoaksept.** Mangler behandlingsgrunnlag, formål eller nødvendighet, hjelper ingen sikkerhetstiltak [K28 s. 4](../kilder/K28-cnil-pia-metode.md), [K40 § 4.2](../kilder/K40-dpia-prosess-uld.md).
2. **Bruk virksomhetens akseptkriterier (Digdir B) for virksomhetsrisiko og for intern beslutningsmyndighet.**
3. **Legg på et GDPR-gulv for personvernrisiko:** (a) restrisiko *Høy/Svært høy* i kategorien Personvern (eller CNIL alvorlighet 3–4 med sannsynlighet over «ubetydelig») kan ikke aksepteres internt alene når DPIA er påkrevd – det krever forhåndsdrøfting med Datatilsynet (art. 36) [K23](../kilder/K23-cnil-risikoark.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md), [K30 kap. 16](../kilder/K30-cnil-pia-kunnskapsbaser.md); (b) høy alvorlighet aksepteres bare når sannsynligheten er ubetydelig [K31 vedlegg 6](../kilder/K31-cnil-pia-tilkoblede-objekter.md).
4. **Beslutningen om forhåndsdrøfting tas av ledelsen** etter dokumentasjon av at risikoen ikke kan reduseres [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md).
5. **Personvernombudet skal gi råd** om DPIA og restrisiko (art. 35 nr. 2) [K24](../kilder/K24-wp248-dpia.md), [K12](../kilder/K12-dt-dpia-veiledning.md).

### 6. Hvilken metode passer når?

| Situasjon | Anbefalt metode | Begrunnelse |
|---|---|---|
| Art. 32-vurdering for en ordinær behandling uten DPIA-plikt, liten/mellomstor virksomhet | CNIL ark 20 (tre trinn, tre fryktede hendelser) + tiltak fra M09 | Enkel, personvernperspektiv, dokumenterbar [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md) |
| Art. 32-vurdering i offentlig virksomhet som allerede bruker Digdirs internkontroll | Digdir K17/K18 med konsekvenskategori Personvern vurdert med CNIL-alvorlighetsbeskrivelser | Integreres i eksisterende risikostyring og akseptkriterier [K18 innledende råd](../kilder/K18-digdir-retningslinje-risiko.md), [K16](../kilder/K16-dfo-veileder-informasjonssikkerhet.md) |
| Risikovurdering av et IKT-system/en skytjeneste med mange behandlinger | Digdir (systemnivå, flere konsekvenskategorier) + egen personvernanalyse per behandling | Digdir håndterer flere kategorier; CNIL/SDM sikrer de registrertes perspektiv |
| DPIA (art. 35) | CNIL PIA (K28–K31) eller Datatilsynets fasesjekkliste [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md); supplér med SDM-målene for tiltakskapitlet | Den registrertes perspektiv, kobling til art. 36, ferdige maler [K28](../kilder/K28-cnil-pia-metode.md), [K29](../kilder/K29-cnil-pia-maler.md) |
| Tiltaksvalg og begrunnelse (art. 25/32) og revisjon av tiltak | SDM mål–faktisk-sammenligning | Sikrer at alle sju mål dekkes; egnet for revisjon [K37 10.3](../kilder/K37-sdm-standard-datavernmodell.md) |
| Vurdering av en databehandlers sikkerhet i DPA-gjennomgang | M09 (NSM 2.1.10 + CNIL ark 14/22) + risikovurdering av restavvik med valgt skala | Leverandørens egen risikovurdering dekker ikke den behandlingsansvarliges risiko |
| Behandling med høyt beskyttelsesbehov (særlige kategorier, sårbare grupper, avhengighet) | CNIL PIA + SDM-nivå «høy/svært høy» for skalering av tiltak | Sikrer strengere tiltak og vurdering av kumulative effekter [K37 9.3–9.7](../kilder/K37-sdm-standard-datavernmodell.md) |
| Statlig styringsdialog / ledelsesrapportering | Digdir-risikonotat + DFØ-rammen | Tilpasset etatsstyring [K16](../kilder/K16-dfo-veileder-informasjonssikkerhet.md) |

**Kombinasjon er mulig og anbefalt.** CNIL sier at informasjonssikkerhetsrisiko (f.eks. EBIOS RM) kan vurderes samtidig med personvernrisiko – tilnærmingene er kompatible [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md), [K30 kap. 21](../kilder/K30-cnil-pia-kunnskapsbaser.md). Datatilsynet gjengir Digdirs risikodefinisjon i DPIA-veiledningen [K12 s. 5](../kilder/K12-dt-dpia-veiledning.md). Praktisk: én risikotabell der hver risiko har både *konsekvens for den registrerte* og *konsekvens for virksomheten*, og der den høyeste styrer risikonivået – se [M03](../maler/M03-risikovurdering-mal.md).

### 7. Dokumentasjon

| Element | Digdir | CNIL | SDM/ULD |
|---|---|---|---|
| Hoveddokument | Risikonotat (formål, omfang, deltakere, styrende dokumenter, metode, obs-områder, utfordringer, resultat, kunnskapsstyrke) [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md) | PIA-rapport: presentasjon, omfang, rettslige tiltak, risikobehandlingstiltak, risikokart, konklusjon/validering [K28 s. 10](../kilder/K28-cnil-pia-metode.md) | Scoping-rapport + evalueringsrapport, gjerne publisert [K40 § 4](../kilder/K40-dpia-prosess-uld.md) |
| Risikooversikt | Risikotabell sortérbar på risikonivå; restliste [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K19](../kilder/K19-digdir-risikovurderingsverktoy.md) | Tabell per fryktet hendelse (virkninger, kilder, trusler, tiltak, alvorlighet, sannsynlighet) [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md), [K30 kap. 21](../kilder/K30-cnil-pia-kunnskapsbaser.md) | Mål–faktisk-sammenligning per beskyttelsesmål [K37 10.3](../kilder/K37-sdm-standard-datavernmodell.md) |
| Tiltaksplan | «Foreslå håndtering»; risiko etter tiltak [K19](../kilder/K19-digdir-risikovurderingsverktoy.md) | Handlingsplan med vanskelighet, kostnad, termin, fremdrift [K30 §1.10](../kilder/K30-cnil-pia-kunnskapsbaser.md) | Handlingsplan med tiltak, ansvar, frist, ressurser, målekriterier [K40 § 4.3](../kilder/K40-dpia-prosess-uld.md) |
| Beslutning | Aksept per risiko på riktig ledernivå [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md) | Formell validering av behandlingsansvarlig [K28 s. 16](../kilder/K28-cnil-pia-metode.md), [K29](../kilder/K29-cnil-pia-maler.md) | Uavhengig revisjon anbefales [K40 § 4.3](../kilder/K40-dpia-prosess-uld.md) |

### 8. Motstrid og uklarheter mellom kildene

- **Antall nivåer:** Digdirs retningslinje har fem nivåer inkl. «Ubetydelig» [K18](../kilder/K18-digdir-retningslinje-risiko.md), Excel-verktøyet fire [K19](../kilder/K19-digdir-risikovurderingsverktoy.md). Avklar hvilken skala som gjelder før start [K19 Praktiske sjekkpunkter](../kilder/K19-digdir-risikovurderingsverktoy.md).
- **Digdirs brukerveiledning motsier seg selv** om cellen Svært høy sannsynlighet × Høy konsekvens (først «Svært høy», så «Høy»); standardmatrisen i malen gir «Høy» [K19 Aktualitet](../kilder/K19-digdir-risikovurderingsverktoy.md).
- **CNILs nivånavn varierer:** «Negligible, Limited, Significant, Maximum» [K30 §1.5–1.6](../kilder/K30-cnil-pia-kunnskapsbaser.md); «negligible, moderate, significant, maximum» [K30 kap. 21](../kilder/K30-cnil-pia-kunnskapsbaser.md); «negligible, moderate, large, maximum» [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md). Innholdet er det samme fire-nivåsystemet – bruk navnene fra [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md) konsekvent.
- **Kunnskapsstyrke:** «svak/middels/sterk» [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md) vs. «lav/moderat/høy» [K18](../kilder/K18-digdir-retningslinje-risiko.md).
- **Restrisiko:** aksepterbar etter kriterier [K18](../kilder/K18-digdir-retningslinje-risiko.md) / etter tiltak og ev. forhåndsdrøfting [K23](../kilder/K23-cnil-risikoark.md), [K28](../kilder/K28-cnil-pia-metode.md) / «ingen akseptabel restrisiko» [K40](../kilder/K40-dpia-prosess-uld.md).
- **Skjæringspunkt for DPIA:** CNILs infografikk sier at to av ni kriterier gir sannsynlig DPIA-plikt; WP248 og Datatilsynet presiserer at ett kriterium kan være nok, og at den norske listen gjelder i tillegg [K23 Aktualitet](../kilder/K23-cnil-risikoark.md). Se [T10](T10-dpia-art35-36.md).
- **SDM-versjon:** v1.0 i kildene er erstattet av nyere versjoner med referansetiltakskatalog og mer GDPR-basert risikomodell [K37 Aktualitet](../kilder/K37-sdm-standard-datavernmodell.md).

## Vanlige feil og fallgruver

- Kun virksomhetens konsekvenser vurderes; personvernkategorien mangler eller er tom [K33 ark 20 s. 49](../kilder/K33-cnil-sikkerhetsguide.md).
- Skalaene justeres underveis for å få «akseptable» resultater [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md).
- Risiko beregnes som produkt (S × K) i stedet for oppslag i normert matrise [K19](../kilder/K19-digdir-risikovurderingsverktoy.md).
- Bare mest forventet utfall vurderes – lavfrekvente, alvorlige utfall for de registrerte overses [K18 kap. 7.2, vedlegg G](../kilder/K18-digdir-retningslinje-risiko.md).
- Tilhørende sannsynlighet settes høyere enn sannsynligheten for selve bruddet [K17 trinn 4](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
- Alvorlighet vurderes uten hensyn til datatype, identifiserbarhet, antall mottakere og sammenkoblinger [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md).
- Deler av behandlingen glemmes (innsamling, partnere/databehandlere, livsløpsslutt, papir, logger generert av tiltakene selv) [K33 ark 20](../kilder/K33-cnil-sikkerhetsguide.md), [K28 s. 11](../kilder/K28-cnil-pia-metode.md).
- Restrisiko aksepteres fordi «få personer berøres» [K40 § 4.3](../kilder/K40-dpia-prosess-uld.md).
- Høy restrisiko aksepteres internt uten vurdering av art. 36 [K23](../kilder/K23-cnil-risikoark.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md).
- Estimater uten skriftlig begrunnelse og uten angitt kunnskapsstyrke [K28 s. 14–15](../kilder/K28-cnil-pia-metode.md), [K17 trinn 6](../kilder/K17-digdir-gjennomfore-risikovurdering.md).
- Ingen revisjon etter endringer [K24](../kilder/K24-wp248-dpia.md), [K28 s. 7](../kilder/K28-cnil-pia-metode.md).

## Sjekkliste

- [ ] Er formålet med risikovurderingen avklart: art. 32-vurdering, DPIA-risikodel, eller systemrisiko? [K17 trinn 1](../kilder/K17-digdir-gjennomfore-risikovurdering.md)
- [ ] Er metode, skalaer og akseptkriterier valgt og godkjent **før** start, og dokumentert i risikonotatet? [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K18](../kilder/K18-digdir-retningslinje-risiko.md)
- [ ] Har skalaen en personvernkategori med beskrivelser fra de registrertes perspektiv (f.eks. CNIL-eksemplene)? [K30 §1.5](../kilder/K30-cnil-pia-kunnskapsbaser.md)
- [ ] Dekker vurderingen alle tre fryktede hendelser og alle støtteressurser, inkl. papir, personer og leverandører? [K28](../kilder/K28-cnil-pia-metode.md), [K30 §1.2](../kilder/K30-cnil-pia-kunnskapsbaser.md)
- [ ] Er hver risiko beskrevet tredelt (hendelse – brudd – konsekvens) eller som kilde → trussel → fryktet hendelse → virkning? [K17](../kilder/K17-digdir-gjennomfore-risikovurdering.md), [K28 s. 6](../kilder/K28-cnil-pia-metode.md)
- [ ] Er det verste relevante utfallet vurdert, og er sannsynligheten satt for hele forløpet? [K18 vedlegg G](../kilder/K18-digdir-retningslinje-risiko.md)
- [ ] Er hvert estimat begrunnet, og er kunnskapsstyrken angitt? [K28](../kilder/K28-cnil-pia-metode.md), [K17 trinn 6](../kilder/K17-digdir-gjennomfore-risikovurdering.md)
- [ ] Er restrisiko vurdert etter tiltak og akseptert av rett ledernivå? [K18 vedlegg B](../kilder/K18-digdir-retningslinje-risiko.md)
- [ ] Er høy restrisiko for de registrerte vurdert opp mot art. 36? [K23](../kilder/K23-cnil-risikoark.md), [K21](../kilder/K21-dt-sjekkliste-dpia-faser.md)
- [ ] Er risikovurderingen satt opp for revisjon (dato, utløsende endringer)? [K28 s. 7](../kilder/K28-cnil-pia-metode.md)

## Se også

- [T08 – Informasjonssikkerhet (art. 32)](T08-informasjonssikkerhet-art32.md) · [T10 – DPIA (art. 35–36)](T10-dpia-art35-36.md) · [T13 – Innebygd personvern](T13-innebygd-personvern-art25.md) · [T03 – Grunnprinsipper](T03-grunnprinsipper-art5.md)
- Maler: [M03 – Risikovurdering](../maler/M03-risikovurdering-mal.md) · [M09 – Sikkerhetstiltak](../maler/M09-sikkerhetstiltak-sjekkliste.md) · [M04 – DPIA-mal](../maler/M04-dpia-mal.md)
- Arbeidsflyter: [A03 – Risikovurdering informasjonssikkerhet](../arbeidsflyter/A03-risikovurdering-informasjonssikkerhet.md) · [A02 – Gjennomføre DPIA](../arbeidsflyter/A02-gjennomfore-dpia.md)

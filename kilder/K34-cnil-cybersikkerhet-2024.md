---
id: K34
tittel: "Cybersecurity – GDPR: the best prevention against cyber risks (2024 edition)"
utgiver: CNIL (Commission nationale de l'informatique et des libertés, Frankrike)
dato: "2024 (2024-utgaven; tall for 2023)"
spraak: en
fil: "ressurser/cnil_cybersecurity_2024_en.pdf"
type: artikkel
gdpr_artikler: [32, 33, 34, 35, 36, 83]
emner: [informasjonssikkerhet, avvik, brudd-paa-personopplysningssikkerheten, losepengevirus, tilsyn, statistikk, vanlige-feil]
relevans: middels
---

# Cybersecurity 2024 – «GDPR: the best prevention against cyber risks» (CNIL, 2024)

## Sammendrag

En kort informasjonsbrosjyre (2 sider) fra CNIL som presenterer GDPR som et cybersikkerhetsinstrument. Den oppsummerer sikkerhetspliktene i GDPR, definerer brudd på personopplysningssikkerheten (data breach) med eksempler, gir statistikk over meldte brudd til CNIL i 2023 og for perioden mai 2018–mai 2023, beskriver CNILs fire roller innen cybersikkerhet, lister de **hyppigste overtredelsene** CNIL finner i tilsyn, og forklarer løsepengevirus (ransomware). Kilden er mest nyttig som begrunnelse/motivasjon (statistikk, sanksjonsrisiko) og for listen over typiske sikkerhetsfeil som tilsynet ser etter.

## Når skal agenten bruke denne kilden

- Når man trenger en kort oversikt over GDPRs sikkerhetsplikter (art. 32–36) for ledelse/ikke-spesialister.
- Når man skal begrunne prioritering av sikkerhetstiltak med tilsynsstatistikk og sanksjonsrisiko (en tredjedel av CNILs sanksjoner i 2023 gjaldt sikkerhet).
- Som sjekkliste over **typiske feil tilsynsmyndigheten finner** (URL-manipulering, passordpolicy, klartekstpassord, HTTP, manglende skjermlås, manglende sårbarhetstesting).
- Ved vurdering av om en hendelse (f.eks. løsepengevirus, tap av tilgjengelighet/integritet) er et brudd på personopplysningssikkerheten.

## Hovedinnhold

### GDPR som cybersikkerhetsinstrument (s. 1)

- Sikkerhet har vært et grunnprinsipp i fransk personvernlov siden 1978 («enshrined in the law for more than 45 years»); GDPR har forsterket kravene og supplert med nye plikter og verktøy: melding av brudd, DPIA, atferdsnormer og sertifisering.
- «The GDPR is the first text to impose specific cybersecurity obligations on all organisations», underlagt tilsynsmyndighetens undersøkelses- og håndhevingsmyndighet.
- Ved manglende etterlevelse: overtredelsesgebyr (administrative fine) på inntil **20 millioner euro eller 4 % av omsetningen**.

**Sikkerhetsplikter etter GDPR (s. 1):**

| Plikt | Når |
|---|---|
| Iverksette tekniske og organisatoriske tiltak for å sikre data | Alltid |
| Føre register (intern oversikt) over brudd på personopplysningssikkerheten | Alltid |
| Gjennomføre personvernkonsekvensvurdering (PIA/DPIA) | For visse sensitive behandlinger |
| Melde brudd til tilsynsmyndigheten (CNIL) | Hvis det er risiko for personer |
| Informere de registrerte om bruddet | Hvis det er høy risiko for personer |

**Nøkkeltall (s. 1):** 4 668 meldinger om brudd i 2023; 1 006 av dem (22 %) skyldtes løsepengevirus; 1/3 av CNILs sanksjoner i 2023 gjaldt brudd på sikkerhetsplikten.

**Hva er en PIA (s. 1):** Et verktøy for å bygge en GDPR-konform og personvernvennlig behandling; gjelder når behandlingen sannsynligvis medfører høy risiko for de registrertes rettigheter og friheter. Ved høy restrisiko må behandlingsansvarlig konsultere tilsynsmyndigheten før behandlingen starter (forhåndsdrøfting, art. 36); lykkes man ikke i å redusere risikoen tilstrekkelig, kan tilsynsmyndigheten avgi en uttalelse om at den planlagte behandlingen bryter GDPR.

### Melding av brudd på personopplysningssikkerheten (s. 1)

**Definisjon:** «a breach of security resulting in the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of or access to personal data transmitted, stored or otherwise processed» (art. 4 nr. 12). Det vil si enhver sikkerhetshendelse – ondsinnet eller ikke, tilsiktet eller ikke – som kompromitterer integritet, konfidensialitet eller tilgjengelighet.

**Eksempler:**
- utilsiktet sletting av medisinske data hos en helseinstitusjon uten sikkerhetskopi;
- tap av en ukryptert USB-pinne med kopi av en bedrifts kundedatabase;
- ondsinnet tilkobling til en skoles database og endring av elevresultater.

**GDPR krever at behandlingsansvarlig:**
- dokumenterer brudd internt;
- melder til tilsynsmyndigheten innen **72 timer** når bruddet medfører risiko for personers rettigheter og friheter;
- informerer de registrerte når risikoen er høy.

**Statistikk 2023:**
- I snitt 13 meldinger per dag.
- **87 %** gjaldt tap av konfidensialitet (tredjepart fikk kjennskap til eller kopierte data). Behandlingsansvarlige er lite bevisste på at tap av integritet eller tilgjengelighet også er brudd; CNIL ser likevel klar økning i meldinger om integritets- og tilgjengelighetstap, særlig pga. løsepengevirus.
- Meldeplikten gjelder brudd av både utilsiktet og ulovlig opprinnelse; flertallet skyldes ondsinnede eksterne handlinger (hacking, tyveri av fysiske medier, falsk teknisk støtte).
- **Hacking: 60 %** av alle meldinger (ca. 2 700); 22 % gjaldt løsepengevirus.
- Mest berørte sektorer (rangert): offentlig forvaltning (18 %), faglig/vitenskapelig/teknisk virksomhet (14 %), finans og forsikring, helse- og sosialtjenester, varehandel, informasjon og kommunikasjon, industri, andre tjenester, administrative tjenester, utdanning, transport. *(Prosentfordelingen for sektorene etter de to første er ikke entydig lesbar i tekstuttrekket.)*

**Nyttige ressurser:** cnil.fr/fr/cybersecurite; CERT-FR (cert.ssi.gouv.fr – «to be checked daily»); ANSSI (cyber.gouv.fr); cybermalveillance.gouv.fr.

### CNILs rolle i cybersikkerhet (s. 2)

CNIL arbeider innen fire områder:

1. **Bevisstgjøring av allmennheten** – faktaark (datatap/-tyveri, phishing, kapring av sosiale kontoer, webkamera-utpressing, identitetsbeskyttelse og -tyveri, passordråd, privat surfing, plakat «cyberreflekser»); partnerskap med sivilsamfunn og bedrifter.
2. **Veiledning til profesjonelle** – passordanbefaling (oppdatert 2022), anbefaling om hendelseslogging, generell sikkerhetsguide med sjekkliste (se [K33](K33-cnil-sikkerhetsguide.md)), ressurser om nettsteds- og IT-sikring, jevnlige publikasjoner om vanlige brudd (løsepengevirus, direktørsvindel/CEO-svindel, angrep på e-post, feilkonfigurerte skytjenester, «credential stuffing», tap av enheter); sektorveiledere (SMB, foreninger, kommuner); «sandkasse»-programmet (digital helse 2021, EdTech 2022). Egen støtte til SMB-er (GDPR-guide med Bpifrance, sjekkliste, mal for forenklet protokoll, guide om lagringstid).
3. **Tilsyn og sanksjoner** – informasjonssikkerhet dekkes systematisk i CNILs ca. **300 formelle tilsyn per år**; grunnleggende prinsipper kontrolleres (passord, database- og nettverkssikkerhet m.m.) samt at det finnes **avviksregister** (bruddregister).
4. **Deltakelse i cyberøkosystemet** – partnerskap med ANSSI (bl.a. guiden «Ransomware attacks, all concerned»), over 20 presentasjoner i 2023, medlem av Cybermalveillance.gouv.fr, Campus Cyber, Club EBIOS og CESIN.

### Hyppigste overtredelser i CNILs tilsyn (s. 2)

1. Data fritt tilgjengelig ved å **endre en URL** (manglende autentisering, forutsigbar URL) – f.eks. endre et tall i adressefeltet gir tilgang til andres dokumenter.
2. **Passordpolicy** som ikke er i samsvar med CNILs passordanbefaling.
3. **Overføring av passord i klartekst**, f.eks. ved opprettelse av nettkonto.
4. **Overføring av data over ukrypterte kanaler (HTTP)**, f.eks. nettskjema med personopplysninger.
5. **Manglende automatisk låsing** av arbeidsstasjonsøkter, slik at tredjepart får tilgang.
6. **Utilstrekkelig testing** for sårbarheter før et nytt system tas i bruk (nytt verktøy, nettsted, skjema uten testfase).

**To hovedtrender i brudd:** forsettlig hacking og tyveri fra ondsinnede tredjeparter; utilsiktede feil fra personer som handler på vegne av behandlingsansvarlig. I andre tilfeller er årsaken ukjent for den som melder.

**Frist:** Halvparten av meldingene sendes innen 72-timersfristen. «An out-of-delay notification constitutes a breach of the GDPR which can be sanctionned by the CNIL.»

**[Merknad – ikke fra kilden]** Etter art. 33 nr. 1 skal bruddet meldes «uten ugrunnet opphold og når det er mulig, senest 72 timer» etter at den behandlingsansvarlige fikk kjennskap til det, med mindre bruddet sannsynligvis ikke vil medføre en risiko; meldes det ikke innen 72 timer, skal årsakene til forsinkelsen oppgis. Fristen er altså ikke absolutt, men forsinkelsen må begrunnes (jf. [K43](K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33)).

### Brudd: status fem år etter GDPR (mai 2018–mai 2023) (s. 2)

- 17 483 meldinger om brudd; antallet har økt over årene (når meldinger med samme opphav grupperes).
- Privat sektor står for ca. to tredjedeler, hvorav **39 % fra SMB-er**; offentlig sektor 22 %.
- Årsaker: **55 % eksterne ondsinnede handlinger**, 20 % menneskelig feil, 25 % annet.

### Løsepengevirus (ransomware) (s. 2)

- Ondsinnede programmer som krypterer offerets data og krever løsepenger for dekrypteringsnøkkelen; spres ofte via e-postvedlegg eller lenker.
- I bedriftsnett sprer programmet seg til alle tilgjengelige ressurser.
- Svært lønnsomt: opportunistiske angrep med løsepenger på noen hundre euro, men større virksomheter rammes i økende grad med krav opp mot flere millioner euro.
- Noen utnytter kjente sikkerhetshull for å spre seg. Ved å gjøre servere, programvare og data utilgjengelige rammes kritiske tjenester, noe som svært ofte fører til endring og/eller tap av tilgjengelighet til personopplysninger – som **kan utgjøre et brudd på personopplysningssikkerheten**.

## Praktiske sjekkpunkter

- Kontroller at det føres intern oversikt (avviksregister) over alle brudd – CNIL kontrollerer dette i tilsyn.
- Kontroller at hendelsesprosessen også fanger opp tap av **tilgjengelighet og integritet** (f.eks. løsepengevirus, utilsiktet sletting uten backup), ikke bare konfidensialitetsbrudd.
- Kontroller at meldeprosessen sikrer melding innen 72 timer – for sen melding er i seg selv et brudd som kan sanksjoneres.
- Kontroller mot de seks vanligste tilsynsfunnene:
  - dokumenter og ressurser er beskyttet med autentisering og ikke tilgjengelige via forutsigbare URL-er (tilgangskontroll på objektnivå);
  - passordpolicy følger tilsynets anbefaling (se [K33](K33-cnil-sikkerhetsguide.md) ark 4);
  - passord sendes aldri i klartekst (f.eks. i velkomst-e-post);
  - alle skjemaer og sider med personopplysninger bruker HTTPS/TLS;
  - automatisk skjermlås er aktivert;
  - nye systemer sårbarhetstestes før produksjonssetting.
- Kontroller at sikkerhetskopier finnes (eksempelet med medisinske data uten backup) og at bærbare medier er kryptert (eksempelet med USB-pinne).

## Viktige sitater

- «The GDPR is the first text to impose specific cybersecurity obligations on all organisations» (s. 1)
- «4 668 notifications of data breaches in 2023» (s. 1)
- «1/3 of the sanctions issued by the CNIL en 2023 relate to non-compliance with the security obligation.» (s. 1)
- «87% of the data breach notifications received by the CNIL in 2023 relate to a loss of confidentiality» (s. 1)
- «statistics show that data controllers are barely aware that such incident constitutes a data breach» – om tap av integritet/tilgjengelighet (s. 1)
- «Information security is systematically covered in the 300 formal inspection procedures conducted by the CNIL each year.» (s. 2)
- «an out-of-delay notification constitutes a breach of the GDPR which can be sanctionned by the CNIL.» (s. 2)

## Kryssreferanser

- GDPR: art. 4 nr. 12 (definisjon av brudd), art. 32 (sikkerhet), art. 33 (melding innen 72 timer; nr. 5 intern dokumentasjon), art. 34 (informasjon til registrerte ved høy risiko), art. 35 (DPIA), art. 36 (forhåndsdrøfting), art. 83 (overtredelsesgebyr – merk at 20 mill./4 % er nivået i art. 83 nr. 5; brudd på art. 32 faller etter art. 83 nr. 4 under 10 mill./2 % **[Merknad – ikke fra kilden]**).
- Andre kilder:
  - [K33](K33-cnil-sikkerhetsguide.md) – CNILs fullstendige sikkerhetsguide med sjekkliste (konkrete tiltak bak listen over vanlige feil).
  - [K15](K15-dt-digitale-angrep.md) – Datatilsynet om personvern ved digitale angrep.
  - [K32](K32-nsm-grunnprinsipper.md) – NSMs tiltak mot løsepengevirus (2.9 gjenoppretting, 4.1–4.4 hendelseshåndtering).
  - [K24](K24-wp248-dpia.md), [K12](K12-dt-dpia-veiledning.md) – DPIA.

## Aktualitet og begrensninger

- Statistikken gjelder 2023 og Frankrike (CNIL); brosjyren er en kort informasjonspublikasjon, ikke en veileder med normative krav.
- **[Merknad – ikke fra kilden]** Brosjyren angir nivået for overtredelsesgebyr «20 millioner euro eller 4 % av omsetningen» generelt; for brudd på sikkerhetsplikten (art. 32) og meldeplikten (art. 33–34) er maksimum etter art. 83 nr. 4 10 millioner euro eller 2 % av global årsomsetning. Høyeste nivå gjelder bl.a. brudd på de grunnleggende prinsippene i art. 5, som også omfatter integritet og konfidensialitet (art. 5 nr. 1 bokstav f).
- **[Merknad – ikke fra kilden]** I Norge er Datatilsynet tilsynsmyndighet for melding av brudd; norske tall finnes i Datatilsynets årsrapporter.
- Tekstuttrekket inneholder noen fransk/engelsk-blandinger og en sektorfigur som ikke kan leses entydig.

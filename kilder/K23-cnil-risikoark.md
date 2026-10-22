---
id: K23
tittel: "PIA – An overview of the requirements and methodology"
utgiver: CNIL (Commission nationale de l'informatique et des libertés, Frankrike)
dato: "2017 (filnavn 171019; PDF opprettet 27.03.2017)"
spraak: en
fil: "ressurser/171019_fiche_risque_en_cmjk.pdf"
type: metode
gdpr_artikler: [35, 36]
emner: [dpia, pia, risikovurdering, alvorlighet, sannsynlighet, restrisiko, forhåndsdrøftelse, infografikk]
relevans: middels
---

# PIA – oversikt over krav og metode (CNIL, 2017)

## Sammendrag
Énsides infografikk (A4 liggende) fra CNIL som oppsummerer DPIA-/PIA-prosessen i fire steg (0–3) med et gjennomgående eksempel: en innovativ geolokaliseringstjeneste der serverne hackes, og kriminelle bruker dataene til å se når brukerne ikke er hjemme og begår innbrudd. Den viser (0) hvorfor en ny behandling kan gi personvernrisiko, (1) screening mot ni kriterier – to eller flere gir sannsynligvis høy risiko og krav om DPIA, (2) evaluering av hver risiko (ulovlig tilgang, uønsket endring, tap av data) der **alvorlighet** bestemmes av potensielle virkninger og dataene, og **sannsynlighet** av risikokilder og støtteressurser, og (3) håndtering: tiltak, vurdering av høy restrisiko, og plikt til å konsultere tilsynsmyndigheten dersom høy restrisiko ikke kan reduseres. Ingen skalaer er angitt – disse finnes i CNILs fulle PIA-metode (K28–K30).

**Merk:** PDF-en har ikke tekstlag; innholdet er lest visuelt (gjengitt i 250 dpi). All tekst var lesbar.

## Når skal agenten bruke denne kilden
- For en rask, pedagogisk forklaring av DPIA-logikken (screening → risikovurdering → tiltak → restrisiko → forhåndsdrøfting) til ikke-eksperter eller ledelse.
- Som huskeliste for hva som driver alvorlighet (virkning + data) og sannsynlighet (risikokilder + støtteressurser) i CNIL-metoden.
- For detaljer og skalaer: bruk K28 (metode), K29 (maler), K30 (kunnskapsbaser).

## Hovedinnhold

### Tittel
«PIA – An overview of the requirements and methodology»

### Steg 0: Launching a new processing (Å starte en ny behandling)
Tekst: Hver dag skapes mange tjenester i den digitale verden. De bygger ofte på behandling av personopplysninger for å dekke behov hos organisasjoner eller brukere. «The supporting assets used to store the data have different levels of vulnerabilities toward feared events such as illegitimate access, unwanted change, or disappearance of personal data.» Slike risikoer vil sannsynligvis ha betydelige konsekvenser for brukernes personvern.

Eksempelforløp (seks bokser):
1. «Let's imagine an innovative service relying on its users' geolocation» – en innovativ tjeneste basert på brukernes geolokasjon.
2. «The service is released on the market and widely adopted by users» – lanseres og tas i bruk av mange.
3. «The collected data are sent on remote servers» – data sendes til eksterne servere.
4. «The servers are hacked by a criminal organisation and data are accessed» – serverne hackes av en kriminell organisasjon.
5. «With the data, it is possible to deduce the users' residential adress and know when the homes are vacant. Several houses are then burglarised» – bostedsadresse og fravær kan utledes; flere hus utsettes for innbrudd.
6. «Question is, how to avoid this situation?»

### Steg 1: Considering the processing (Vurdere behandlingen – screening)
Tekst: Slike risikoer er uønsket både for «the data processor» og de registrerte. Før en behandling gjennomføres, er det viktig å analysere den for å forstå dens iboende risikoer. Flere faktorer påvirker risikoen, f.eks. hva slags data som behandles. «Generally speaking, if a processing meets two of the criteria listed, then it is likely to present high risks and would require to carry out a privacy impact assessment.»

Flyt: «It is first essential to identify the processing's features» → kriterieliste → «The processing meets several criteria and is likely to present high risk to the rights and freedoms of data subjets» → «A developed risk assessment is then necessary».

**De ni kriteriene** (i eksempelet er «Large scale» og «Matched datasets» uthevet som oppfylt):
| # | Kriterium (original) | Norsk |
|---|---|---|
| 1 | Evaluation / Scoring | Evaluering/poengsetting |
| 2 | Automated decision-making | Automatiserte avgjørelser |
| 3 | Systematic monitoring | Systematisk overvåking |
| 4 | Sensitive data | Sensitive/særlige opplysninger |
| 5 | **Large scale** | Stor skala (oppfylt i eksempelet) |
| 6 | **Matched datasets** | Sammenstilte datasett (oppfylt i eksempelet) |
| 7 | Vulnerable data subjects | Sårbare registrerte |
| 8 | New technology | Ny teknologi |
| 9 | Prevent data subject from exercising a right | Hindrer den registrerte i å utøve en rettighet |

### Steg 2: Evaluating the privacy risks (Vurdere personvernrisikoene)
Tekst: Vurderingen fastsetter først konteksten behandlingen utføres i, inkludert formål og tekniske egenskaper. I tillegg til å vurdere de grunnleggende prinsippene – nødvendighet og proporsjonalitet – «each risk has to be analysed to evaluate its severity and likehood according to its potential impacts on the rights and freedoms of data subjects, the data processed, the risks sources and the supporting assets».

Flyt: «It starts with the study of the processing's context» → «Follows the evaluation of each risk (illegitimate access, unwanted modification, data loss) on the rights and freedoms of data subjects».

**Risikomodell:**
| Dimensjon | Bestemmes av | Eksempel i kilden |
|---|---|---|
| **Alvorlighet (Severity)** | Potensielle virkninger (Potential impacts) | innbrudd (burglary) |
| | Data | geolokasjon (geolocation) |
| **Sannsynlighet (Likehood)** | Risikokilder (Risk sources) | nettkriminelle (cyber criminals) |
| | Støtteressurser (Supporting assets) | servere (servers) |

De tre fryktede hendelsene: ulovlig tilgang (illegitimate access), uønsket endring (unwanted modification), tap av data (data loss) – jf. konfidensialitet, integritet, tilgjengelighet.

### Steg 3: Adressing the risks (Håndtere risikoene)
Tekst: Når risikoene er identifisert, skal det avgjøres om de er akseptable gitt eksisterende og planlagte tekniske og organisatoriske tiltak. «If it doesn't seem possible in regard of the foreseen measures, the data protection authority has to be consulted.» «In any case, it is mandatory to implement the planned controls before carrying out the processing.»

Beslutningsflyt:
1. «To adress those risks, appropriate technical and organisational measures must be implemented»
2. «Are there any high residual risks?»
   - **Lav restrisiko:** «There are low residual risks – The processing can be carried out»
   - **Høy restrisiko, men flere tiltak mulig:** «There are high residual risks but additional measures can be implemented» → tilbake til tiltak (stiplet pil)
   - **Høy restrisiko, ingen ytterligere tiltak:** «There are high residual risks and no additional measures can adress them – It is mandatory to consult the data protection authority»

## Praktiske sjekkpunkter
- Screen ny behandling mot de ni kriteriene; to eller flere → sannsynligvis DPIA (sjekk også Datatilsynets liste, K20).
- Beskriv konteksten (formål, tekniske egenskaper) før risikoanalysen.
- Vurder nødvendighet og proporsjonalitet (grunnleggende prinsipper) i tillegg til risiko.
- Analyser hver av de tre fryktede hendelsene: ulovlig tilgang, uønsket endring, tap av data.
- Vurder **alvorlighet** ut fra virkning for de registrerte og hvilke data det gjelder; vurder **sannsynlighet** ut fra risikokilder og sårbarheter i støtteressursene (servere, nettverk, personer osv.).
- Iverksett tekniske og organisatoriske tiltak og vurder restrisiko.
- Høy restrisiko som ikke kan reduseres → forhåndsdrøfting med tilsynsmyndigheten (art. 36).
- Planlagte tiltak skal være implementert før behandlingen starter.

## Viktige sitater
- «Generally speaking, if a processing meets two of the criteria listed, then it is likely to present high risks and would require to carry out a privacy impact assessment.» (steg 1)
- «each risk has to be analysed to evaluate its severity and likehood according to its potential impacts on the rights and freedoms of data subjects, the data processed, the risks sources and the supporting assets.» (steg 2)
- «If it doesn't seem possible in regard of the foreseen measures, the data protection authority has to be consulted.» (steg 3)
- «In any case, it is mandatory to implement the planned controls before carrying out the processing.» (steg 3)
- «There are high residual risks and no additional measures can adress them. It is mandatory to consult the data protection authority» (steg 3)

## Kryssreferanser
- GDPR: art. 35 nr. 1, 3 og 7; art. 36 nr. 1; art. 32 (sikkerhet); fortalepunkt 76, 84, 90, 94
- Andre kilder: [K28](K28-cnil-pia-metode.md) – full CNIL-metode med skalaer for alvorlighet og sannsynlighet; [K29](K29-cnil-pia-maler.md) – maler; [K30](K30-cnil-pia-kunnskapsbaser.md) – kunnskapsbaser (trusler, tiltak); [K24](K24-wp248-dpia.md) – WP248, kilden til de ni kriteriene; [K20](K20-dt-dpia-liste.md); [K21](K21-dt-sjekkliste-dpia-faser.md)

## Aktualitet og begrensninger
- Fra 2017 (før GDPR trådte i kraft), men konsistent med GDPR og WP248. Fransk tilsynsmyndighet; generelt anvendelig.
- Kun overordnet infografikk – ingen skalaer, matriser eller akseptkriterier.
- Kilden bruker «data processor» der det i GDPR-terminologi trolig menes behandlingsansvarlig/virksomheten. **[Merknad – ikke fra kilden]**
- Stavefeil i originalen («likehood», «adress», «subjets») er beholdt i sitater.
- **[Merknad – ikke fra kilden]** Kilden sier at to kriterier gir sannsynlig høy risiko; WP248 og Datatilsynet presiserer at også ett kriterium i noen tilfeller kan være nok, og at nasjonale lister (K20) gjelder i tillegg.

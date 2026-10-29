---
id: K09
tittel: "Veiledning om de grunnleggende personvernprinsippene"
utgiver: Datatilsynet
dato: "Udatert nettside (utskrift 2026-09-22)"
spraak: nb
fil: "ressurser/Datatilsynet/Veiledning om de grunnleggende personvernprinsippene _ Datatilsynet.pdf"
url: "https://www.datatilsynet.no/rettigheter-og-plikter/personvernprinsippene/grunnleggende-personvernprinsipper/"
type: veileder
gdpr_artikler: [5, 6, 9, 23, 24, 25, 32, 89]
emner: [prinsipper, lovlighet, rettferdighet, gjennomsiktighet, formaalsbegrensning, dataminimering, riktighet, lagringsbegrensning, integritet, konfidensialitet, ansvarlighet, tiltak]
relevans: høy
---

# Veiledning om de grunnleggende personvernprinsippene (Datatilsynet, udatert)

## Sammendrag
Nettveileder fra Datatilsynet (7 utskriftssider) som forklarer personvernprinsippene i GDPR art. 5 (med støtte i art. 6 og 9): lovlighet, rettferdighet og gjennomsiktighet; formålsbegrensning; dataminimering; riktighet; lagringsbegrensning; integritet og konfidensialitet; og ansvarlighet. For hvert prinsipp gis en kort forklaring og **eksempler på tiltak** – nyttig som tiltakskatalog i DPIA og innebygd personvern. Veilederen kobles til Datatilsynets veiledning om programvareutvikling med innebygd personvern og sjekklisten for kravsetting. Målgruppe: alle som behandler personopplysninger, særlig utviklere og prosjekter.

## Når skal agenten bruke denne kilden
- Når en DPIA eller risikovurdering skal vurdere etterlevelse av prinsippene i art. 5, og foreslå tiltak per prinsipp.
- Ved innebygd personvern (art. 25) / kravspesifikasjon for systemer.
- Ved vurdering av viderebehandling (forenlighet med opprinnelig formål).
- Som kort forklaring av prinsippene til brukere.

## Hovedinnhold

### Innledning (s. 1)
Reglene bygger på grunnleggende prinsipper som alle som behandler personopplysninger må opptre i samsvar med. Veilederen er en utredning av prinsippene i art. 5, og baserer seg også på art. 6 og 9.

### 1. Lovlig, rettferdig og gjennomsiktig (s. 1)
**Lovlig:** Det må finnes et rettslig grunnlag. Art. 6 regulerer når behandling er lovlig – minst ett vilkår må være oppfylt. Ved sensitive opplysninger må i tillegg minst ett av vilkårene i art. 9 være oppfylt (se [K02](K02-dt-behandlingsgrunnlag.md)).
*Tiltak for lovlighet:*
- Tiltak som sørger for at behandlingen ikke går ut over det rettslige grunnlaget. Ved samtykke bør det f.eks. etableres tiltak for å kontrollere hva det er gitt samtykke til, og settes tekniske sperrer for all behandling som går ut over dette.
- Skille mellom opplysninger som er nødvendige for å levere tjenesten og opplysninger det kan være valgfritt å oppgi for tilgang til utvidede tjenester.

**Rettferdig:** Behandlingen skal skje i respekt for de registrertes interesser og rimelige forventninger, være gjennomsiktig og forståelig, og ikke foregå på fordekte eller manipulerende måter.
*Tiltak for rettferdighet:*
- Tiltak som ivaretar rettigheter og friheter etter personvernregelverket og andre grunnleggende rettigheter – f.eks. ytringsfrihet, tankefrihet, bevegelsesfrihet, likhet for loven, retten til frihet, samvittighet og religionsfrihet.
- Tiltak som gjør resultater fra automatiserte avgjørelser forutsigbare og forståelige – f.eks. åpenhet om profilering og hvilke opplysninger som er avgjørende for at enkeltpersoner blir delt inn i ulike kategorier.

**Gjennomsiktig:** Behandlingen skal være oversiktlig og forutsigbar; den registrerte skal være informert. Gjennomsiktighet skaper tillit og setter den registrerte i stand til å bruke rettighetene og ivareta sine interesser.
*Tiltak for gjennomsiktighet:*
- Funksjonalitet for interaksjon mellom behandlingsansvarlig og registrert, slik at det er enkelt å tilegne seg informasjon om behandlingen.
- Funksjonalitet for å gi informasjon om hvilke opplysninger som behandles, hva de brukes til, og mulighet til å gjøre seg kjent med rettighetene og hvordan de utøves.
- Personvernerklæring på nettsidene med generell informasjon om virksomhetens personvernpolicy (se [K06](K06-dt-informasjon-og-apenhet.md)).

### 2. Formålsbegrensning (s. 2)
**Spesifikke, uttrykkelige, angitte og legitime formål:** Ethvert formål skal identifiseres og beskrives presist, slik at alle berørte har samme entydige forståelse. Legitimt formål betyr at det i tillegg til rettslig grunnlag skal være i samsvar med øvrige etiske og rettslige samfunnsnormer.
*Tiltak:*
- Tiltak som gjør at det eksplisitt tas stilling til hvilken prosessering som er innenfor de angitte formålene og hva som ikke er det; tekniske sperrer mot prosessering utenfor formålet, f.eks. utlevering.
- Tiltak som sikrer at det som standard kun behandles opplysninger til det som er forutsatt fra starten.
- Tiltak som sikrer at det som standard kun behandles opplysninger som er nødvendige for hvert spesifikke formål.

**Ikke gjenbruk til uforenlige formål:** Gjenbruk til nye formål er mulig dersom nytt formål er forenlig med opprinnelig formål **og** det finnes rettslig grunnlag for den nye behandlingen. Er behandlingen ikke forenlig, kan opplysningene bare behandles dersom de registrerte har **samtykket** til viderebehandlingen, eller den er **hjemlet i lovgivning** med formål å ivareta hensynene i art. 23 nr. 1.
Sentrale momenter i forenlighetsvurderingen:
- om det er forbindelse mellom opprinnelig og nytt formål
- i hvilken sammenheng opplysningene er samlet inn
- opplysningenes art, f.eks. om det behandles sensitive opplysninger
- mulige konsekvenser av den tiltenkte viderebehandlingen
- om opplysningene beskyttes ved f.eks. kryptering eller pseudonymisering
*Tiltak:*
- Tiltak for å identifisere gjenbruk som ikke er forutsatt fra innsamlingstidspunktet.
- Tiltak for å vurdere om gjenbruksformålet er uforenlig med opprinnelig formål.
- Tiltak for å stoppe behandling med formål som er uforenlige med opprinnelig formål.

**Merk:** Gjenbruk til arkivformål i allmennhetens interesse, vitenskapelige eller historiske forskningsformål eller statistiske formål er ikke uforenlig dersom behandlingen er underlagt nødvendige garantier.
*Tiltak (garantier):*
- Tekniske og organisatoriske tiltak for å sikre at det ikke behandles mer enn nødvendig (dataminimering).
- Tekniske tiltak for pseudonymisering når formålet kan oppfylles slik.
- Tekniske tiltak for anonymisering når formålet kan oppfylles slik.

### 3. Dataminimering (s. 3)
- Begrense mengden opplysninger som hentes inn og behandles til det som er nødvendig for formålet.
- Er identitetsopplysninger eller personopplysninger ikke nødvendige, taler prinsippet for ikke å samle dem inn eller behandle dem. Prinsippet kan også være relevant for **hvor mange personer** som registreres i et datasett.
*Tiltak for å:*
- ta stilling til om formålet med rimelighet kan oppfylles på annen måte enn ved å behandle personopplysninger – i så fall skal det ikke behandles personopplysninger.
- sikre at det kun samles inn og brukes relevante og nødvendige opplysninger. *Eksempel:* En kart-app som viser veien fra A til B trenger å vite hvor brukeren er når appen er i bruk, men ikke hvem som bruker appen eller tilgang til kontakter eller bilder på telefonen.
- sikre at det ikke behandles opplysninger om flere personer enn nødvendig – relevant for forskning (nødvendig antall deltakere, utvalg/kontrollutvalg for representasjon).

### 4. Riktighet (s. 4)
- Opplysninger skal være korrekte og oppdateres hvis nødvendig. Behandlingsansvarlig må sørge for å **straks** slette eller rette opplysninger som er uriktige med hensyn til formålene.
*Tiltak:*
- Tiltak for at opplysningene er korrekte og oppdaterte – f.eks. regelmessig varsle brukere om å kontrollere sine opplysninger (mange banker gjør dette ved innlogging i nettbank).
- Tiltak for at uriktige opplysninger straks slettes eller korrigeres.
- Brukes back-up for gjenoppretting, må også disse gjennomgås for nødvendig korrigering.

### 5. Lagringsbegrensning (s. 5)
- Opplysninger skal lagres slik at de **slettes eller anonymiseres** når de ikke lenger er nødvendige for formålet de ble innhentet for.
*Tiltak:*
- Tiltak for å sikre at lagringstiden ikke er lengre enn nødvendig. Behandlingsansvarlig bør innføre **tidsfrister for sletting** eller **periodisk gjennomgang**.

### 6. Integritet og konfidensialitet (s. 6)
- Opplysninger skal behandles slik at integritet og konfidensialitet beskyttes.
*Tiltak:*
- tiltak mot uautorisert utlevering og tilgang
- tiltak mot utilsiktet og ulovlig ødeleggelse, tap og endringer
- som standard sørge for at opplysningene er tilgjengelige for autoriserte personer når det er nødvendig
- som standard sikre at opplysningene ikke gjøres tilgjengelige for et ubegrenset antall mennesker uten den berørte personens medvirkning
- tiltak for å spore endringer i systemet og for å kunne håndtere sikkerhetsbrudd
- tiltak for at systemene er robuste mot f.eks. sårbarheter, angrep og uhell
- Se også sjekklisten for «Krav» i veiledningen om programvareutvikling med innebygd personvern, og sjekklisten for kravsetting (pdf).

### 7. Ansvarlighet (s. 7)
- Understreker behandlingsansvarliges ansvar for å opptre i samsvar med reglene.
- «Det er ikke nok å bare ha ansvaret – man må vise at man tar ansvaret.»
- Behandlingsansvarlig må opptre **proaktivt** og etablere alle nødvendige organisatoriske og tekniske tiltak for å sikre etterlevelse til enhver tid, og kunne **vise** at den faktisk opptrer i samsvar med reglene.

### Tiltakskatalog (oppsummert)

| Prinsipp | Eksempeltiltak fra kilden |
|---|---|
| Lovlighet | Tekniske sperrer mot behandling utover samtykke; skille obligatoriske og valgfrie opplysninger |
| Rettferdighet | Ivareta grunnleggende rettigheter; forutsigbare/forståelige automatiserte avgjørelser, åpenhet om profilering |
| Gjennomsiktighet | Interaksjonsfunksjonalitet; informasjon om opplysninger, bruk og rettigheter; personvernerklæring |
| Formålsbegrensning | Eksplisitt avgrensning av prosessering; sperrer mot f.eks. utlevering; standardbegrensning til forutsatt bruk; identifisere/vurdere/stoppe uforenlig gjenbruk |
| Garantier ved arkiv/forskning/statistikk | Dataminimering, pseudonymisering, anonymisering |
| Dataminimering | Vurdere alternativ uten personopplysninger; kun relevante og nødvendige data; begrense antall personer |
| Riktighet | Brukervarsel om kontroll; straks rette/slette; korrigere back-up |
| Lagringsbegrensning | Slettefrister; periodisk gjennomgang |
| Integritet og konfidensialitet | Tilgangskontroll; vern mot tap/endring; tilgjengelighet for autoriserte; ikke ubegrenset tilgjengeliggjøring; sporbarhet/hendelseshåndtering; robusthet |
| Ansvarlighet | Proaktive tiltak; kunne dokumentere etterlevelse |

### Lenker siden viser til
- /rettigheter-og-plikter/virksomhetenes-plikter/programvareutvikling-med-innebygd-personvern/ (veiledning om programvareutvikling med innebygd personvern)
- /globalassets/…/innebygd-personvern/02-sjekkliste_krav_250817.pdf (sjekkliste for kravsetting)

## Praktiske sjekkpunkter
- Kontroller at hver behandling er vurdert mot alle sju prinsippene, og at det er valgt minst ett tiltak per relevant prinsipp.
- Kontroller at det finnes tekniske sperrer som hindrer behandling utover grunnlag og formål (f.eks. utlevering).
- Kontroller at obligatoriske og frivillige felt er skilt.
- Kontroller at viderebehandling er forenlighetsvurdert etter de fem momentene, eller har samtykke/lovhjemmel (art. 23 nr. 1).
- Kontroller at løsninger ikke samler inn mer enn nødvendig (jf. kart-app-eksemplet) og ikke flere personer enn nødvendig.
- Kontroller at det finnes mekanismer for å oppdatere/rette data, også i back-up.
- Kontroller slettefrister eller periodisk gjennomgang.
- Kontroller sporbarhet (logging), hendelseshåndtering og robusthet.
- Kontroller at etterlevelse er dokumentert (ansvarlighet).

## Viktige sitater
- «Alle som behandler personopplysninger må opptre i samsvar med disse prinsippene.» (s. 1)
- «… den skal ikke foregå på fordekte eller manipulerende måter.» (s. 1)
- «At formålet skal være legitimt innebærer at det i tillegg til å ha et rettslig grunnlag også skal være i samsvar med øvrige etiske og rettslige samfunnsnormer.» (s. 2)
- «Dataminimalitetsprinsippet kan også være relevant i vurderingen av hvor stort antall personer som skal registreres i et datasett.» (s. 3)
- «Dersom back-up brukes for gjenoppretting av data må også disse gjennomgås med hensyn til nødvendig korrigering.» (s. 4)
- «Det er ikke nok å bare ha ansvaret – man må vise at man tar ansvaret.» (s. 7)

## Kryssreferanser
- GDPR: art. 5 nr. 1 a–f og nr. 2, art. 6 (særlig nr. 4), art. 9, art. 23 nr. 1, art. 24, art. 25, art. 32, art. 89
- Andre kilder: [K02](K02-dt-behandlingsgrunnlag.md) – lovlighet; [K03](K03-dt-fastsette-formal.md) – formål; [K06](K06-dt-informasjon-og-apenhet.md) – gjennomsiktighet; [K08](K08-dt-retting-og-sletting.md) – riktighet og sletting; [K10](K10-dt-kryptering.md) – konfidensialitet; [K13](K13-dt-innebygd-personvern.md) – innebygd personvern; [K12](K12-dt-dpia-veiledning.md) – DPIA (vurdering av prinsippene).

## Aktualitet og begrensninger
- Udatert i utskriften (skrevet ut 22.09.2026); lenket sjekkliste har filnavn som tyder på versjon fra 2017.
- Tiltakslistene er eksempler, ikke uttømmende.
- **[Merknad – ikke fra kilden]** Kilden sier at gjenbruk krever at nytt formål er forenlig **og** at det finnes rettslig grunnlag for den nye behandlingen. Fortalepunkt 50 sier at når behandlingen er forenlig med de opprinnelige formålene, «kreves det ikke et annet rettslig grunnlag enn det som ligger til grunn for innsamlingen av personopplysninger» (jf. [K43](K43-gdpr-fortale.md#fp-50) og [art. 6 nr. 4](K43-gdpr-kap02-prinsipper.md#art-6)). Spørsmålet er omdiskutert; lovteksten bør leses ved vurdering av viderebehandling.

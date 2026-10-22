---
id: K19
tittel: "Risikovurdering støtteverktøy (Excel-mal) med brukerveiledning"
utgiver: Digitaliseringsdirektoratet (Digdir)
dato: "Udatert; malen merket «Oppdatert i versjon 2.0 av Internkontroll i praksis – informasjonssikkerhet»"
spraak: nb
fil: "ressurser/Digdir/[MAL] Risikovurdering støtteverktøy_bokmål.xlsm + ressurser/Digdir/[STØTTE] Brukerveiledning_risikovurderingsverktøy_bokmål.pdf"
type: verktøy
gdpr_artikler: [32, 35]
emner: [risikovurdering, risikomatrise, risikotabell, verktøy, restrisiko, tiltak]
relevans: middels
---

# Risikovurdering støtteverktøy med brukerveiledning (Digdir, udatert)

## Sammendrag
Makroaktivert Excel-arbeidsbok (.xlsm) fra Digdir som støtte- og dokumentasjonsverktøy for Digdirs risikovurderingsmetode (K17). Verktøyet har tre faner: **Start** (konfigurerbar 4×4-risikomatrise og nivåbetegnelser), **Risikovurdering** (risikotabell for inntil 100 risikobeskrivelser med konsekvens, tilhørende sannsynlighet, risikonivå, vurdering av risikohåndtering og risiko etter tiltak) og **Matrise** (automatisk plott av risiko før tiltak og gjenværende risiko). Nivåene velges fra nedtrekkslister, og risikonivået slås opp i matrisen (kombinasjon, ikke produkt, av sannsynlighet og konsekvens). Brukerveiledningen (2–3 sider) forklarer arbeidsflyten. Digdir gir ikke brukerstøtte eller hjelp til tilpasninger. NB: verktøyet bruker fire nivåer (Lav–Svært høy), mens eksempel-retningslinjen (K18) bruker fem (inkl. Ubetydelig).

## Når skal agenten bruke denne kilden
- Når brukeren vil dokumentere en risikovurdering (informasjonssikkerhet, art. 32 eller DPIA-risikodel) i en enkel tabell + matrise.
- Når agenten skal lage eller fylle en risikotabell med samme kolonner som Digdirs verktøy, eller forklare hvordan verktøyet brukes.
- Når man skal vise risiko før og etter tiltak (gjenværende risiko/restrisiko).

## Hovedinnhold

### Brukerveiledningen – om verktøyet
- Kan brukes som støtte-/dokumentasjonsverktøy til metoden i Digdirs veiledningsmateriell; metode og organisering beskrives der. Virksomheten må selv vurdere bruk med andre metoder.
- Enkelt Excel-verktøy for virksomheter av ulik størrelse og kompleksitet; fritt å tilpasse, men «Digitaliseringsdirektoratet ikke har anledning til å bistå med tilpasninger eller brukerstøtte».
- Må ses i sammenheng med veiledningsmateriellet og eksempler på styrende dokumenter. Forutsetninger/føringer verktøyet bygger på:
  - Fire nivåer på risikoenes alvorlighetsgrad
  - Fire nivåer på sannsynlighet
  - Fire nivåer på konsekvens
  - Virksomheten skal kunne angi nivå/beskrivelse av sannsynlighet og konsekvens
  - Virksomheten skal kunne angi beskrivelsen av risikonivå
  - Risiko før og etter planlagte tiltak vises i risikomatrise
  - «Risiko uttrykkes som kombinasjonen av sannsynlighet og konsekvens, ikke produktet av sannsynlighet multiplisert med konsekvens.»

### Fane 1: Start (startbildet)
Tekst øverst: «Oppdatert i versjon 2.0 av Internkontroll i praksis – informasjonssikkerhet. Utarbeidet av Digitaliseringsdirektoratet.»

**Standard risikomatrise (4×4)** – y-akse sannsynlighet, x-akse konsekvens:

| Sannsynlighet ↓ / Konsekvens → | Lav (1) | Moderat (2) | Høy (3) | Svært høy (4) |
|---|---|---|---|---|
| **Svært høy (4)** | Moderat | Høy | Høy | Svært høy |
| **Høy (3)** | Moderat | Moderat | Høy | Høy |
| **Moderat (2)** | Lav | Moderat | Moderat | Høy |
| **Lav (1)** | Lav | Lav | Moderat | Moderat |

**Fargekoder** (betinget formatering etter risikonivå): Lav = grønn, Moderat = gul, Høy = oransje, Svært høy = rød.

**Nivåtabeller under matrisen** (redigerbare betegnelser med tallverdi):

| Nivå | SANNSYNLIGHET | KONSEKVENS | RISIKO |
|---|---|---|---|
| 1 | Lav | Lav | Lav |
| 2 | Moderat | Moderat | Moderat |
| 3 | Høy | Høy | Høy |
| 4 | Svært høy | Svært høy | Svært høy |

**Tilpasning:**
- Hver celle i matrisen kan endres ved å velge risikonivå fra en nedtrekksliste (verdiene er de fire risikobetegnelsene; feilmelding «Sett inn en verdi fra listen»). Fargen følger verdien.
- Betegnelsene på de fire nivåene for risiko, konsekvens og sannsynlighet kan endres ved å skrive i tabellene under matrisen; endringen slår gjennom i matrisen og i risikovurderingsarket.
- Når nivåer og matrise er som ønsket, klikk knappen **«Til Risikovurdering»**. (Fanene Risikovurdering og Matrise er skjult og nås via makroknapper.)

### Fane 2: Risikovurdering (risikotabell)
Plass til **100 risikobeskrivelser** (R1–R100). Kolonner (synlige brukerkolonner I–R; A–H er hjelpekolonner):

| Kol. | Overskrift | Innhold / utfylling |
|---|---|---|
| A | ID | Automatisk «R» + nummer (R1…R100) |
| B | NR | Løpenummer |
| C–H | Sanns_verdi, Kons_verdi, Risiko_verdi, Sanns_etter_verdi, Kons_etter_verdi, Gj_Risiko_verdi | Skjulte tallverdier (1–4, 0 hvis tom) brukt til sortering og plotting |
| I | Risikobeskrivelse – Stikkord om: (1) innledende hendelse(r) (2) informasjonssikkerhetsbruddet (3) de uønskede konsekvensene som kan oppstå | Fritekst |
| J | Begrunnelse for konsekvensvurdering | Fritekst |
| K | Konsekvens | Nedtrekk: Lav / Moderat / Høy / Svært høy (fra Start) |
| L | Tilhørende sannsynlighet | Nedtrekk: Lav / Moderat / Høy / Svært høy |
| M | Begrunnelse for vurdering av tilhørende sannsynlighet | Fritekst |
| N | Risikonivå | Beregnes automatisk ved oppslag i Start-matrisen; farget |
| O | Vurdering av risikohåndtering | Fritekst; brukes i første omgang til «Kan aksepteres» eller «Ikke akseptabel» |
| P | Konsekvens etter tiltak | Nedtrekk (som K) |
| Q | Sannsynlighet etter tiltak | Nedtrekk (som L) |
| R | Gjenværende risiko | Beregnes automatisk fra matrisen; farget |

Eksempelrad i malen: R1 «Risiko 1» – Konsekvens Høy, Tilhørende sannsynlighet Svært høy → Risikonivå Høy; etter tiltak Konsekvens Moderat, Sannsynlighet Moderat → Gjenværende risiko Moderat.

**Arbeidsflyt i fanen (brukerveiledningen):**
1. Utgangspunkt er uønskede hendelser som virksomheten på forhånd har diskutert seg frem til.
2. Digdir anbefaler å ta utgangspunkt i hva **konsekvensen** kan bli dersom en gitt hendelse inntreffer, og deretter vurdere **sannsynligheten** for at hendelsen inntreffer med den beskrevne konsekvensen. Virksomheten vurderer selv om det skal vurderes sannsynlighet for ulike grader av konsekvens for samme hendelse, eller bare det mest forventede utfallet.
3. Velg konsekvens- og sannsynlighetsnivå fra nedtrekksmenyene (innholdet styres av nivåene på Start).
4. Risikonivået uttrykkes automatisk med farge ut fra matrisen. Endres en celle i Start-matrisen, endres også resultatet (eksempel: cellen sannsynlighet = Svært høy, konsekvens = Høy har standardverdi «Høy»/oransje; endres den til «Svært høy», vises risikoen som «Svært høy»/rød).
5. **Evaluer** hver risiko: kolonnen «Vurdering av risikohåndtering» brukes til «Kan aksepteres» eller «Ikke akseptabel».
6. **Foreslå håndtering:** gjør en ny vurdering av konsekvens og sannsynlighet etter at ett eller flere tenkte sikkerhetstiltak er implementert → **gjenværende risiko** viser tiltakets risikoreduserende effekt. «Vær oppmerksom på at også kostnader og uheldige sideeffekter må vurderes før man beslutter endelig håndtering av risikoen.»
7. **Sortering:** risikoene kan sorteres etter ID-nummer og etter risikonivå – både før og etter planlagte tiltak (knapper).
8. Knappen **«Til Risikomatrise»** leder til siste skjermbilde.

### Fane 3: Matrise
To 4×4-matriser (y: sannsynlighet Svært høy–Lav; x: konsekvens Lav–Svært høy):
- **Risiko før tiltak** – risiko-ID-ene (f.eks. R1) plottes i cellen ut fra Konsekvens/Tilhørende sannsynlighet.
- **Gjenværende risiko** – plottes ut fra verdiene etter tiltak.
Fargene følger oppsettet på Start. (I malen står R1 i cellen Svært høy/Høy før tiltak og Moderat/Moderat etter.)

## Praktiske sjekkpunkter
- Kontroller at Start-matrisen og nivåbetegnelsene er justert til virksomhetens egne førende beskrivelser (f.eks. K18) før registrering starter.
- Vær obs på at verktøyet har 4 nivåer uten «Ubetydelig», mens K18 har 5 – avklar hvilken skala som gjelder og tilpass matrisen.
- Fyll ut begrunnelse for både konsekvens og sannsynlighet for hver risiko (kolonne J og M) – det dokumenterer vurderingen.
- Skriv risikobeskrivelsen tredelt: (1) innledende hendelse, (2) brudd, (3) konsekvenser.
- Noter «Kan aksepteres»/«Ikke akseptabel» i kolonne O; for «Ikke akseptabel» registreres tiltak og ny konsekvens/sannsynlighet (P, Q) → gjenværende risiko (R).
- Vurder kostnader og uheldige sideeffekter før tiltak besluttes.
- Bruk matrisefanen til å vise risiko før/etter i risikonotatet (jf. K17).
- **[Merknad – ikke fra kilden]** Verktøyet har ingen egen kolonne for tiltaksbeskrivelse, ansvarlig, frist eller konsekvenskategori; legg til kolonner eller før dette i risikonotatet/tiltaksplanen. Filen inneholder makroer (VBA) – vurder virksomhetens makropolicy.

## Viktige sitater
- «Risiko uttrykkes som kombinasjonen av sannsynlighet og konsekvens, ikke produktet av sannsynlighet multiplisert med konsekvens.» (Brukerveiledning)
- «Digitaliseringsdirektoratet anbefaler at man i analysen tar utgangspunkt i hva konsekvensen kan bli dersom en gitt hendelse inntreffer, og at det deretter gjøres en vurdering av sannsynligheten for at hendelsen inntreffer med den beskrevne konsekvensen.» (Brukerveiledning)
- «Risikoen man da står igjen med er den gjenværende risikoen.» (Brukerveiledning)
- «Det er i verktøyet avsatt plass til at det skal være mulig å inkludere 100 risikobeskrivelser.» (Brukerveiledning)

## Kryssreferanser
- GDPR: art. 32 nr. 1–2 (risikobasert sikkerhet), art. 35 nr. 7 bokstav c–d (risikovurdering og tiltak i DPIA), art. 36 (forhåndsdrøfting ved høy restrisiko)
- Andre kilder: [K17](K17-digdir-gjennomfore-risikovurdering.md) – metoden verktøyet støtter; [K18](K18-digdir-retningslinje-risiko.md) – skalaer og akseptkriterier; [K29](K29-cnil-pia-maler.md) – CNILs PIA-maler som alternativt dokumentasjonsformat

## Aktualitet og begrensninger
- Malen er udatert (versjon 2.0 av Internkontroll i praksis), men lenket fra Digdir-nettsiden sist endret 2025.
- Brukerveiledningen inneholder en tilsynelatende motsigelse: først sies at Konsekvens «Høy» + Sannsynlighet «Svært høy» gir «Svært høy»/rød (figur 4), deretter at samme celle som standard har «Høy»/oransje. Standardmatrisen i malen gir «Høy». Figurene i brukerveiledningen er ikke tilgjengelige i tekstuttrekket.
- Rettet mot informasjonssikkerhet; ingen egne felt for personvernspesifikke vurderinger (de registrertes rettigheter, behandlingsgrunnlag osv.). **[Merknad – ikke fra kilden]**
- Kolonnestruktur, nedtrekkslister og farger er lest fra .xlsm-filens XML (datavalidering og betinget formatering); makrokoden (knappene) er ikke analysert.

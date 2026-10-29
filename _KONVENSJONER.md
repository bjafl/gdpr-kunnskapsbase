# Konvensjoner for kunnskapsbasen

Denne filen beskriver hvordan kunnskapsbasen er bygget opp og hvordan nye notater skal skrives. Les den før du legger til eller endrer filer.

## Mappestruktur

| Mappe | Innhold |
|---|---|
| `kilder/` | Ett notat per kildedokument i `ressurser/`. Tro mot kilden, detaljert, med sidehenvisninger. ID `K01`–`K44`. Unntak: K42–K44 er ordrett lovtekst (se under). |
| `temaer/` | Tematiske synteser på tvers av kilder (f.eks. behandlingsgrunnlag, DPIA, overføring). Viser til `K`-notater. |
| `maler/` | Utfyllbare maler og sjekklister (DPIA, databehandleravtale, TIA, risikovurdering, protokoll). |
| `arbeidsflyter/` | Steg-for-steg prosedyrer for agenten (hvordan gjennomføre/kvalitetssikre en DPIA, DPA-gjennomgang osv.). |

## Språk

- Norsk bokmål. Faguttrykk på engelsk i parentes første gang de brukes: «vurdering av personvernkonsekvenser (DPIA)».
- Korte sitater beholdes på originalspråket, i anførselstegn, med sidetall: «...» (s. 12).
- **Begreper:** [BEGREPSBANK.md](BEGREPSBANK.md) er fasit for begrepsbruk. Den gir lovens norske begrep, det offisielle engelske motsvaret og hjemmelen, og den viser hvilke praksisbegreper som svarer til hvilke lovbegreper. Bruk lovens begrep når et rettslig begrep omtales.
- Termer: behandlingsansvarlig (controller), databehandler (processor), underdatabehandler (sub-processor), den registrerte (data subject), behandlingsgrunnlag (legal basis), personvernforordningen/GDPR, personopplysningsloven (popplyl.), Datatilsynet, EDPB (Personvernrådet), WP29 (Artikkel 29-gruppen).

## Format for kildenotater (`kilder/Kxx-kortnavn.md`)

```markdown
---
id: K12
tittel: "Veiledning om DPIA"
utgiver: Datatilsynet
dato: "2018 (sist endret 2024-03-13)"   # så presist som kilden oppgir
spraak: nb | nn | en | fr
fil: "ressurser/Datatilsynet/Veiledning om DPIA _ Datatilsynet.pdf"
type: veileder | retningslinje | metode | mal | sjekkliste | standard | liste | artikkel | verktøy | lov
gdpr_artikler: [35, 36]
emner: [dpia, risikovurdering]
relevans: høy | middels | lav
---

# <Tittel> (<utgiver>, <år>)

## Sammendrag
5–10 linjer: hva dokumentet er, hovedbudskap, hvem det er for.

## Når skal agenten bruke denne kilden
Konkrete situasjoner/spørsmål der denne kilden er riktig oppslag.

## Hovedinnhold
Strukturert etter dokumentets egen oppbygning (bruk underoverskrifter).
BEVAR konkrete detaljer: kriterielister, terskler, definisjoner, eksempler,
tabeller, skalaer, krav, unntak, frister. Dette er viktigere enn prosa.
Bruk tabeller der kilden har tabeller. Oppgi sidetall (s. X) for viktige punkter.

## Praktiske sjekkpunkter
Punktliste med handlingsrettede regler utledet fra kilden ("Kontroller at ...").

## Viktige sitater
3–10 korte, ordrette sitater med sidetall.

## Kryssreferanser
- GDPR: art. X nr. Y, fortalepunkt (recital) Z
- Andre kilder: [K24](K24-wp248-dpia.md) – hvorfor relevant

## Aktualitet og begrensninger
Er kilden utdatert/erstattet? Bygger den på direktiv 95/46? Gjelder den bare Frankrike/Tyskland/Norge?
Egne tilføyelser som ikke står i kilden markeres: **[Merknad – ikke fra kilden]**.
```

## Lovtekst (`type: lov`, K42–K44)

K42, K43 og K44 er ikke notater, men **ordrett lovtekst** fra Lovdata. De følger ikke notatformatet over.

- Alt mellom `<!-- KILDETEKST START … -->` og `<!-- KILDETEKST SLUTT -->` er ordrett kildetekst. **Teksten der skal ikke redigeres for hånd.** Bare formateringen er endret: overskrifter, lister, fotnoter og lenker gjort om til ren tekst.
- Over markøren står frontmatter, navigasjon og oppslagshjelp, som er redaksjonelt.
- Ankre: `#p12a` (popplyl. § 12 a), `#p3-15` (ekomloven § 3-15 i K44), `#art-28` (GDPR art. 28) og `#fp-26` (fortalepunkt 26).
- GDPR er delt i én fil per kapittel. Hver fil har `gdpr_artikler` i frontmatter, slik at [INDEKS-artikler.md](INDEKS-artikler.md) lenker hver artikkel til riktig fil.
- Henvis slik: «GDPR art. 28 nr. 3 bokstav a [K43]», «popplyl. § 16 [K42]», «ekomloven § 3-15 [K44]».

## Format for temanotater (`temaer/Txx-*.md`)

```markdown
---
id: T07
tittel: "Databehandleravtale (art. 28)"
gdpr_artikler: [28, 29, 32]
kilder: [K05, K01, K39]
---

# <Tittel>

## Kjerneregler (kort svar)
De 5–10 viktigste reglene, hver med kildehenvisning [K05].

## Rettslig grunnlag
GDPR-artikler, fortalepunkter, personopplysningsloven, ev. andre lover.

## Utdyping
Underoverskrifter per deltema. Syntese på tvers av kilder, med henvisninger [K05 s. 3], [K24 s. 9].
Peker på forskjeller/uenighet mellom kilder og på hvilken kilde som er nyest/mest autoritativ.

## Vanlige feil og fallgruver

## Sjekkliste

## Se også
Lenker til maler/, arbeidsflyter/ og andre temaer.
```

Kildehierarki ved motstrid: GDPR/lov > EDPB/WP29-retningslinjer > Datatilsynet (norsk praksis) > andre tilsyn (CNIL, ULD) > metodeverk (Digdir, NSM, SDM).

## Format for maler og arbeidsflyter

- `maler/Mxx-*.md`: utfyllbar mal med tabeller/felt og veiledning per felt i kursiv, med kildehenvisning. Skal kunne kopieres direkte inn i et arbeidsdokument.
- `arbeidsflyter/Axx-*.md`: «Når brukes» · «Input agenten trenger fra brukeren» (spørsmål å stille) · «Steg» (nummerert, hvert steg peker til tema/mal/kilde) · «Output» · «Kvalitetskontroll» · «Når skal det eskaleres til jurist/personvernombud».

## Kvalitetskrav

- Ikke dikt opp innhold. Det som ikke står i kilden, skal enten utelates eller merkes **[Merknad – ikke fra kilden]**.
- Lange kilder gir lange notater: et 100-siders dokument bør gi et notat på flere tusen ord. Detalj > kortfattethet, men uten utfylling.
- Lenker mellom notater er relative markdown-lenker (`[K12](../kilder/K12-dt-dpia-veiledning.md)`).

## Kilderegister (ID → fil)

| ID | Notatfil | Kildefil (i `ressurser/`) |
|---|---|---|
| K01 | K01-dt-behandlingsansvarlig-og-databehandler.md | Datatilsynet/Behandlingsansvarlig og databehandler _ Datatilsynet.pdf |
| K02 | K02-dt-behandlingsgrunnlag.md | Datatilsynet/Behandlingsgrunnlag _ Datatilsynet.pdf |
| K03 | K03-dt-fastsette-formal.md | Datatilsynet/Fastsette formål _ Datatilsynet.pdf |
| K04 | K04-dt-fore-protokoll.md | Datatilsynet/Føre protokoll _ Datatilsynet.pdf |
| K05 | K05-dt-databehandleravtale.md | Datatilsynet/Hvordan lage en databehandleravtale_ _ Datatilsynet.pdf |
| K06 | K06-dt-informasjon-og-apenhet.md | Datatilsynet/Informasjon og åpenhet _ Datatilsynet.pdf |
| K07 | K07-dt-legge-til-rette-for-rettigheter.md | Datatilsynet/Legge til rette for rettigheter _ Datatilsynet.pdf |
| K08 | K08-dt-retting-og-sletting.md | Datatilsynet/Retting og sletting _ Datatilsynet.pdf |
| K09 | K09-dt-grunnleggende-prinsipper.md | Datatilsynet/Veiledning om de grunnleggende personvernprinsippene _ Datatilsynet.pdf |
| K10 | K10-dt-kryptering.md | Datatilsynet/Kryptering _ Datatilsynet.pdf |
| K11 | K11-art30-protokollmaler.md | artikkel-30_protokoll-behandlingsansvarlig.xlsx + artikkel-30_protokoll-databehandler.xlsx |
| K12 | K12-dt-dpia-veiledning.md | Datatilsynet/Veiledning om DPIA _ Datatilsynet.pdf |
| K13 | K13-dt-innebygd-personvern.md | Datatilsynet/Innebygd personvern og personvern som standard _ Datatilsynet.pdf |
| K14 | K14-dt-overforing-utenfor-eos.md | Datatilsynet/Overføring av personopplysninger ut av EØS _ Datatilsynet.pdf |
| K15 | K15-dt-digitale-angrep.md | Datatilsynet/Håndtering av personvernet ved digitale angrep _ Datatilsynet.pdf |
| K16 | K16-dfo-veileder-informasjonssikkerhet.md | Datatilsynet/DFØ_veileder-informasjonssikkerhet.pdf |
| K17 | K17-digdir-gjennomfore-risikovurdering.md | Digdir/Gjennomføre risikovurdering _ Digdir.pdf |
| K18 | K18-digdir-retningslinje-risiko.md | Digdir/[EKSEMPEL] Retningslinje Forstå, vurdere og håndtere risiko_bokmål.docx |
| K19 | K19-digdir-risikovurderingsverktoy.md | Digdir/[MAL] Risikovurdering støtteverktøy_bokmål.xlsm + [STØTTE] Brukerveiledning_risikovurderingsverktøy_bokmål.pdf |
| K20 | K20-dt-dpia-liste.md | dpialist280119.pdf |
| K21 | K21-dt-sjekkliste-dpia-faser.md | sjekkliste-for-dpiafaser.pdf |
| K22 | K22-dpia-eksempler.md | eksempler.jpg |
| K23 | K23-cnil-risikoark.md | 171019_fiche_risque_en_cmjk.pdf |
| K24 | K24-wp248-dpia.md | 20171013_wp248_rev01_enpdf_4.pdf |
| K25 | K25-wp259-samtykke.md | 20180416_article_29_wp_guidelines_on_consent_publish_...pdf |
| K26 | K26-wp260-apenhet.md | wp260_enpdf_transparency.pdf |
| K27 | K27-wp244-ledende-tilsynsmyndighet.md | wp244_rev01_en-lead-supervisory-authority.pdf |
| K28 | K28-cnil-pia-metode.md | CNIL-PIA-1-Methodology.pdf |
| K29 | K29-cnil-pia-maler.md | cnil-pia-2-en-templates.pdf |
| K30 | K30-cnil-pia-kunnskapsbaser.md | cnil-pia-3-en-knowledgebases.pdf |
| K31 | K31-cnil-pia-tilkoblede-objekter.md | cnil-pia-piaf-connectedobjects-en.pdf |
| K32 | K32-nsm-grunnprinsipper.md | NSMs Grunnprinsipper for IKT-sikkerhet v2.1.pdf |
| K33 | K33-cnil-sikkerhetsguide.md | cnil_guide_securite_personnelle_ven_0.pdf |
| K34 | K34-cnil-cybersikkerhet-2024.md | cnil_cybersecurity_2024_en.pdf |
| K35 | K35-cnil-referentiel-audit.md | referentiel_audit_en.pdf |
| K36 | K36-cnil-referentiel-digital-safe.md | referentiel_cfn_en.pdf |
| K37 | K37-sdm-standard-datavernmodell.md | SDM-Methodology_V1.0.pdf |
| K38 | K38-tia-guide.md | guide_tia.pdf |
| K39 | K39-cnil-mobilapper.md | recommendation-mobiles-app.pdf |
| K40 | K40-dpia-prosess-uld.md | apf2016.pdf |
| K41 | K41-dcat-ap-no.md | Digdir/dcat-ap-no_beskrivelse-av-datasett.pdf |
| K42 | K42-personopplysningsloven.md | https://lovdata.no/dokument/NL/lov/2018-06-15-38/* (norsk del) |
| K43 | K43-gdpr.md (oversikt), K43-gdpr-fortale.md, K43-gdpr-kap01…kap11-*.md | https://lovdata.no/dokument/NL/lov/2018-06-15-38/* (forordningen) |
| K44 | K44-ekomloven-3-15.md | https://lovdata.no/dokument/NL/lov/2024-12-13-76/* (kun § 3-15) |

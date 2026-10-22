---
id: A04
tittel: "Arbeidsflyt: Vurdere overføring til tredjeland og gjennomføre TIA"
gdpr_artikler: [6, 9, 13, 14, 28, 30, 44, 45, 46, 47, 48, 49]
kilder: [K14, K38, K05, K10, K21, K29, K33]
---

# Arbeidsflyt: Vurdere overføring til tredjeland og gjennomføre TIA

## Når brukes

- En leverandør, skytjeneste, underleverandør, konsernselskap eller samarbeidspartner behandler, lagrer, aksesserer (support/fjerntilgang) eller mottar personopplysninger utenfor EØS – eller kan komme til å gjøre det.
- Ved gjennomgang av databehandleravtaler/tjenestevilkår med underleverandører eller forbehold om overføring/utlevering ([A01](A01-gjennomga-databehandleravtale.md)).
- Når en DPIA ([A02](A02-gjennomfore-dpia.md)) eller protokoll avdekker overføringer.
- Ved revurdering av eksisterende overføringer (lovendringer, endret adekvansstatus, ny underleverandør).
- Når brukeren spør om en leverandør «er lovlig å bruke» mht. tredjeland.

Fagstoff: [T11](../temaer/T11-overforing-tredjeland-og-tia.md). Mal: [M06](../maler/M06-tia-mal.md).

## Input agenten trenger fra brukeren

1. Hvilken behandling/tjeneste gjelder det, og hva er formålet?
2. Hvem er eksportør og importør (navn, land, konsern)? Hvem er behandlingsansvarlig og hvem er databehandler?
3. Hvor lagres data? Hvor ytes drift og support fra (inkl. «follow-the-sun», krisegjenoppretting)? Hvilke underleverandører, i hvilke land?
4. Hvilke data og registrerte (særlige kategorier, art. 10, fødselsnummer, barn, sårbare)? Volum?
5. Format: klartekst, kryptert (hvem har nøklene?), pseudonymisert (hvem har koblingsnøkkelen)?
6. Hvilket overføringsgrunnlag påberopes i dag (DPF, SCC-modul, BCR, art. 49)?
7. Dokumenter: databehandleravtale, SCC med vedlegg, underleverandørliste, leverandørens TIA/«transfer impact»-dokumentasjon, åpenhetsrapporter, sikkerhetsdokumentasjon, DPF-sertifiseringsoppføring.
8. Finnes DPIA for behandlingen?

## Steg

1. **Kartlegg dataflyten.** List alle overføringer i kjeden, inkl. fjerntilgang/support, underleverandører, videreoverføringer, nettsidetillegg og analyse-/markedsføringsverktøy [K14 s. 7; K38 s. 10]. Kontroller at de står i protokollen [K14 s. 7].

2. **Er det en overføring?** Test EDPBs tre kumulative vilkår (eksportør underlagt GDPR; utlevering/tilgjengeliggjøring til annen rettslig enhet; importør i tredjeland/internasjonal organisasjon) [K14 s. 1; K38 s. 5–6]. Egen ansatt på reise = nei; konsernselskap/leverandør med fjerntilgang = ja [K38 s. 6]. Bruk M06 del A1.

3. **Leverandør underlagt tredjelands lov med data i EØS?** Kjør Datatilsynets fire steg (kan overføring likevel skje → hvem er ansvarlig → garantier etter art. 28 nr. 1 → hva er avtalt). Se etter vage forbehold om utlevering/overføring for å oppfylle leverandørens rettslige forpliktelser – typisk holdepunkt for at tiltak trengs [K14 s. 9–10]. M06 del A6.

4. **Grunnlag for selve behandlingen.** Bekreft art. 6 (ev. 9/10), minimering, informasjon (art. 13–14) og vurder om anonymiserte data kan brukes i stedet [K38 s. 11]. Mangler → [A06](A06-vurdere-behandlingsgrunnlag.md).

5. **Adekvans?** Sjekk mottakerlandet mot gjeldende liste og forbehold [K14 s. 2]:
   - USA: er importøren DPF-sertifisert, og dekker sertifiseringen aktuelle data? **[Merknad – ikke fra kildene]** Verifiser aktuell status for DPF.
   - **Brasil:** K14 lister Brasil som adekvat, men et eksempel i samme kilde behandler Brasil som ikke-adekvat. Verifiser status på vurderingsdatoen før konklusjon; formuler betinget inntil verifisert.
   - Canada/Japan/Sør-Korea/Færøyene: kontroller at importøren faller inn under beslutningens omfang [K38 s. 6–7].
   Adekvans → dokumenter verifiseringen (kilde, dato) og gå til steg 11. Ingen TIA nødvendig [K38 s. 6].

6. **Art. 46-grunnlag.** Velg/verifiser grunnlag: normalt SCC 2021/914 med riktig modul (1 BA→BA, 2 BA→DB, 3 DB→DB, 4 DB→BA) eller BCR [K14 s. 3–4]. Kontroller at SCC er uendret, vedleggene fylt ut, og at tilleggsklausuler ikke motsier SCC. Ved modul 2/3 dekkes art. 28 [K14 s. 4].

7. **Art. 49 bare som siste utvei.** Hvis verken adekvans eller art. 46 er mulig: vurder unntakene restriktivt (samtykke informert om risiko; avtale og rettskrav bare leilighetsvis; ikke samtykke/avtale for offentlig myndighetsutøvelse; annet ledd krever varsel til Datatilsynet og informasjon til de registrerte) [K14 s. 12–14]. Dokumenter vilkårene; ingen TIA.

8. **TIA – steg 1–3 (M06 del B–D).** Avklar hvem som gjør TIA-en (eksportøren; ved leverandør som eksportør: krev hele TIA-en med bevis og verifiser/komplettér) [K38 s. 8–9]. Beskriv overføringen (type tilgang, format, frekvens, kategorier, sårbarhet). Vurder lov og praksis: personvernlov og uavhengig tilsyn, rettigheter, rettsmidler, overvåkingslover/-praksis, de fem European Essential Guarantees, rettsstat, mottatte begjæringer [K38 s. 17–21]. Bruk kilder som er relevante, objektive, pålitelige, verifiserbare og tilgjengelige [K14 s. 8]. Skill inngrep fra krenkelse [K14 s. 7]. Konkluder (1) effektivt / (2) ikke effektivt / (3) ikke grunn til å tro at loven anvendes – (3) krever grundig dokumentasjon [K38 s. 21–22; K14 s. 15].

9. **TIA – steg 4 (M06 del E): supplerende tiltak.** Kartlegg eksisterende tiltak; legg til nye. Prioriter tekniske tiltak som oppfyller EDPB-vilkårene: kryptering der **eksportøren** (ikke importøren) forvalter nøklene; pseudonymisering der koblingsnøkkelen er utenfor tredjelandets rekkevidde [K38 s. 23–24; K14 s. 8]. Supplér med kontraktuelle og organisatoriske tiltak (åpenhet, varsling, bestride begjæringer, revisjon, oppsigelse) [K38 s. 24–25]. Der importøren må ha klartekst og det ikke finnes effektive tekniske tiltak: vurder om løsningen kan endres (EØS-support, just-in-time-tilgang, kundestyrte nøkler) – ellers konklusjon (3) med solid dokumentasjon eller ingen overføring.

10. **Beslutning og implementering (M06 del F).** Er verktøy + tiltak effektivt → lag handlingsplan, ta tiltakene inn i SCC/DPA, innhent uttalelse fra PVO og CISO og godkjenning [K38 s. 26–27]. Ikke effektivt → ikke overfør / stans; krev sletting med bevis eller retur [K38 s. 26; K14 s. 8].

11. **Dokumenter og informer.** Oppdater protokoll, personvernerklæring (mottakere/land/grunnlag), DPIA (M04 pkt. 1.7) og leverandøroversikt [K14 s. 7; K21 s. 3–4].

12. **Revurdering (M06 del G).** Sett intervall (f.eks. hvert 2. år) og utløsende hendelser: lovendringer, endret adekvansstatus (DPF, Brasil), ny underleverandør, mottatt begjæring, importør varsler hindring [K38 s. 28; K14 s. 7].

## Output

- Kartlegging av overføringer (liste over ledd i kjeden med land, rolle, grunnlag).
- Konklusjon per overføring: ikke overføring / adekvans (verifisert dato) / art. 46 + TIA / art. 49 (vilkår dokumentert) / ikke tillatt.
- Utfylt TIA ([M06](../maler/M06-tia-mal.md)) der art. 46 brukes.
- Liste over krav til leverandør (dokumentasjon, kontraktsendringer, tekniske tiltak) – kan legges inn i DPA-gjennomgangen ([M01](../maler/M01-databehandleravtale-sjekkliste.md)).
- Handlingsplan og revurderingsdato.
- Markering av alle opplysninger som må verifiseres (adekvansstatus, DPF-sertifisering, lovanalyse).

## Kvalitetskontroll

- [ ] Fjerntilgang/support og underleverandører er med [K14 s. 7].
- [ ] Adekvansstatus er verifisert mot gjeldende kilde med dato – ikke bare hentet fra kunnskapsbasen [K14 s. 2].
- [ ] Brasil og DPF er eksplisitt håndtert der relevant.
- [ ] Riktig SCC-modul; SCC uendret; tilleggstiltak inntatt [K14 s. 4].
- [ ] TIA bygger på konkrete, etterprøvbare kilder – ikke bare leverandørens konklusjon [K38 s. 9].
- [ ] Tekniske tiltak oppfyller alle EDPB-kontrollpunktene (nøkkelkontroll hos eksportør) [K38 s. 23–24].
- [ ] Konklusjon (3) er bare brukt med grundig dokumentasjon [K14 s. 8].
- [ ] Art. 49 er ikke brukt for systematiske/gjentakende overføringer [K14 s. 12].
- [ ] PVO og CISO har uttalt seg; revurderingsdato er satt [K38 s. 27–28].

## Når skal det eskaleres til jurist/personvernombud

- Alle konklusjoner av type (2) eller (3) i steg 3 → jurist og PVO.
- Overføring av særlige kategorier, art. 10-data, fødselsnummer, barns data eller store volum til ikke-adekvat land → jurist og PVO.
- Leverandøren nekter å levere TIA-dokumentasjon, nekter SCC, eller har vide forbehold om utlevering → jurist (kan bety at leverandøren ikke kan brukes [K14 s. 10]).
- Ønske om å endre SCC eller bruke ad hoc-klausuler/BCR → jurist (godkjenning kreves) [K14 s. 3–5].
- Bruk av art. 49 annet ledd (krever varsel til Datatilsynet) → jurist og PVO.
- Utleveringskrav fra utenlandsk domstol/myndighet (art. 48) → jurist umiddelbart [K14 s. 14].
- Endret adekvansstatus (f.eks. DPF) som berører mange leverandører → jurist, PVO og ledelse.
- Offentlig sektor eller helse med sektorspesifikke krav (taushetsplikt, arkiv, sikkerhetsloven) → jurist.

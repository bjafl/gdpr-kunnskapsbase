---
id: A06
tittel: "Arbeidsflyt – vurdere behandlingsgrunnlag"
gdpr_artikler: [5, 6, 7, 8, 9, 10, 13, 14, 21]
kilder: [K01, K02, K03, K06, K08, K09, K11, K14, K25, K26, K39]
---

# A06 – Vurdere behandlingsgrunnlag

## Når brukes

- En ny behandling planlegges, eller en eksisterende skal dokumenteres (protokoll, personvernerklæring, DPIA).
- Brukeren spør «kan vi …?» om innsamling, bruk, deling eller gjenbruk av personopplysninger.
- Opplysninger skal brukes til et nytt formål (forenlighetsvurdering).
- Samtykke vurderes, eller eksisterende samtykkeløsning skal kvalitetssikres.
- Opplysninger skal utleveres til en annen behandlingsansvarlig.
- Særlige kategorier, straffedommer, barn eller fødselsnummer er involvert.

**Fagbakgrunn:** [T02](../temaer/T02-behandlingsgrunnlag-og-samtykke.md), [T03](../temaer/T03-grunnprinsipper-art5.md). **Mal:** [M08 Interesseavveining](../maler/M08-interesseavveining-mal.md).

## Input agenten trenger fra brukeren

1. Hvem er virksomheten (privat, offentlig myndighet, arbeidsgiver i saken)? Er den behandlingsansvarlig? (Ellers: [T01](../temaer/T01-roller-behandlingsansvarlig-databehandler.md).)
2. Hva er **formålet** – konkret? Er det flere formål?
3. Hvilke **registrerte** (kunder, ansatte, søkere, barn, pasienter …) og hvilke **opplysninger**? Særlige kategorier, straffedommer, fødselsnummer?
4. Hvor kommer opplysningene fra (den registrerte, tredjepart, offentlig kilde, observasjon/sensor)?
5. Finnes en avtale med den registrerte, og hva har vedkommende bedt om?
6. Finnes en lov eller forskrift som **pålegger** eller gir virksomheten en **oppgave** som krever behandlingen? Hvilken bestemmelse?
7. Er opplysningene allerede samlet inn for et annet formål? Med hvilket grunnlag og hvilken informasjon ble gitt?
8. Skal opplysningene deles? Med hvem og i hvilken rolle?
9. Brukes informasjonskapsler, SDK-er eller annen lesing/skriving på brukerens enhet?
10. Er det automatiserte avgjørelser eller profilering?

## Steg

1. **Avklar formål og rolle.**
   - Formålet skal være skriftlig, spesifikt, uttrykkelig og legitimt; avvis vage formål («administrasjon», «forbedre tjenesten») [K03; K09 s. 2].
   - Del opp i separate formål/behandlingsaktiviteter – grunnlag vurderes per formål og per opplysning [K02 s. 1, 10].
   - Bekreft at brukeren er behandlingsansvarlig [K01].

2. **Nytt formål for eksisterende data? → forenlighetsvurdering** ([art. 6 nr. 4](../kilder/K43-gdpr-kap02-prinsipper.md#art-6)).
   - Vurder: kobling mellom formålene; sammenheng og forholdet til den registrerte; opplysningenes art; konsekvenser; garantier (kryptering/pseudonymisering); rimelige forventninger [K03; K09 s. 2] → [T03](../temaer/T03-grunnprinsipper-art5.md) avsnitt 3.
   - Uforenlig → bare med samtykke eller lovhjemmel (art. 23 nr. 1) [K09 s. 2]. Arkiv/forskning/statistikk med art. 89-garantier er ikke uforenlig [K03].
   - Forenlig → identifiser grunnlag for det nye formålet [K09 s. 2] og planlegg informasjon før oppstart [K26 avsn. 45–48].
   - Var opprinnelig grunnlag samtykke: nytt formål krever nytt samtykke, med mindre et annet grunnlag passer bedre [K25 s. 12].

3. **Gå gjennom grunnlagene i [art. 6 nr. 1](../kilder/K43-gdpr-kap02-prinsipper.md#art-6) i denne rekkefølgen** og stopp ved det som passer best (ett per formål) [K02 s. 1]:
   - **c) Rettslig plikt:** Finnes en klar lovplikt uten valgfrihet? Angi hjemmel [K02 s. 6].
   - **e) Offentlig oppgave/myndighet:** Har virksomheten en lovbestemt oppgave? Angi hjemmel [K02 s. 8].
   - **b) Avtale:** Er behandlingen objektivt nødvendig for å levere det den registrerte har bedt om, eller for tiltak den registrerte har bedt om før avtale? Ikke «liten skrift», ikke virksomhetens egne ønsker (kredittsjekk), ikke avtalebrudd [K02 s. 5; K25 s. 8].
   - **f) Berettiget interesse:** Ikke for offentlige myndigheters oppgaveutførelse [K02 s. 9]. Fyll ut [M08](../maler/M08-interesseavveining-mal.md) (tre vilkår). Inngripende sporing/profilering for reklame passer sjelden [K39 s. 28–29].
   - **a) Samtykke:** Bare når den registrerte har et reelt valg. Normalt ikke for arbeidsgiver eller offentlig myndighet [K25 s. 6–7]. Gå til steg 5.
   - **d) Vitale interesser:** Bare liv og død / fare for helse, ikke masseinnhenting [K02 s. 7].
   - **[Merknad – ikke fra kildene]** Rekkefølgen er en praktisk arbeidsrekkefølge, ikke et rettslig hierarki; grunnlagene er likestilte i art. 6.

4. **Tilleggsvilkår.**
   - **Særlige kategorier:** Finn unntak i [art. 9 nr. 2](../kilder/K43-gdpr-kap02-prinsipper.md#art-9) (uttrykkelig samtykke, arbeidsrett, vitale interesser, ideelle organisasjoner, åpenbart offentliggjort, rettskrav, viktige allmenne interesser, helse, folkehelse, forskning) eller popplyl. [§ 6](../kilder/K42-personopplysningsloven.md#p6), [§ 7](../kilder/K42-personopplysningsloven.md#p7), [§ 9](../kilder/K42-personopplysningsloven.md#p9); kontroller at lovhjemmel oppfyller forordningens krav. Avtale er ikke unntak [K02 s. 2; K25 s. 19].
   - **Straffedommer:** offentlig kontroll, [popplyl. § 11](../kilder/K42-personopplysningsloven.md#p11) eller annen lov med garantier ([art. 10](../kilder/K43-gdpr-kap02-prinsipper.md#art-10)) [K02 s. 2].
   - **Barn:** informasjonssamfunnstjeneste + samtykke → foreldresamtykke under 13 år i Norge ([art. 8](../kilder/K43-gdpr-kap02-prinsipper.md#art-8), [popplyl. § 5](../kilder/K42-personopplysningsloven.md#p5)), forholdsmessig verifisering; sjekk andre lands grenser [K02 s. 4; K25 s. 23–27].
   - **Automatiserte avgjørelser ([art. 22](../kilder/K43-gdpr-kap03-den-registrertes-rettigheter.md#art-22)):** avtale, lov eller uttrykkelig samtykke + garantier [K08; K25 s. 18].
   - **Lesing/skriving på terminalutstyr:** samtykke etter ePrivacy ([ekomloven § 3-15](../kilder/K44-ekomloven-3-15.md)) med mindre unntak, i tillegg til GDPR-grunnlag for etterfølgende behandling [K39 s. 11, 30] → [T15](../temaer/T15-apper-sdk-og-sporingsteknologi.md).
   - **Fødselsnummer:** kontroller [popplyl. § 12](../kilder/K42-personopplysningsloven.md#p12) (saklig behov for sikker identifisering, og metoden er nødvendig for å oppnå det).
   - **Overføring ut av EØS:** eget overføringsgrunnlag i tillegg [K14 s. 12] → [T11](../temaer/T11-overforing-tredjeland-og-tia.md).

5. **Ved samtykke – kvalitetssikre løsningen** [K02 s. 3–4; K25] (lovtekst: [art. 4 nr. 11](../kilder/K43-gdpr-kap01-alminnelige-bestemmelser.md#art-4), [art. 7](../kilder/K43-gdpr-kap02-prinsipper.md#art-7)):
   - Frivillig: ingen maktubalanse, ikke betingelse for tjenesten, granulært per formål, ingen ulempe ved nei/tilbaketrekking.
   - Spesifikt og informert: behandlingsansvarlig(e), formål, datatyper, tilbaketrekkingsrett, ev. art. 22 og tredjelandsrisiko; atskilt fra vilkår; klart språk.
   - Aktiv handling før behandlingen starter; ingen forhåndsavkryssing/scrolling.
   - Uttrykkelig der art. 9/22/49 krever det.
   - Dokumentasjon (tidspunkt, versjon av tekst/flyt, hva som ble vist).
   - Tilbaketrekking like enkel, i samme grensesnitt; rutine for stans og sletting; ingen stille bytte av grunnlag [K25 s. 22–23].

6. **Ved utlevering til annen behandlingsansvarlig:** avgivers grunnlag for utleveringen, forenlighet med formålet, mottakers eget grunnlag, informasjon til de registrerte [K01 s. 9; K14 s. 9–10].

7. **Kontroller prinsippene** – nødvendighet og dataminimering, lagringstid, riktighet, sikkerhet [K09] → [T03](../temaer/T03-grunnprinsipper-art5.md).

8. **Dokumenter og implementer.**
   - Protokoll: kolonne I (art. 6), J (supplerende hjemmel/interesse), K (art. 9/10) [K11] → [M02](../maler/M02-protokoll-art30.md).
   - Personvernerklæring: grunnlag per formål, berettiget interesse, protestrett, tilbaketrekkingsrett [K06 s. 2; K26 vedlegg] → [T04](../temaer/T04-apenhet-og-informasjonsplikt.md).
   - Vurder DPIA-plikt [M05](../maler/M05-dpia-terskelvurdering.md).

## Output

Et notat per behandling med:
1. Formål (konkret) og behandlingsaktiviteter.
2. Valgt behandlingsgrunnlag per formål, med hjemmel og kort begrunnelse – og hvorfor andre grunnlag er forkastet.
3. Tilleggsgrunnlag (art. 9/10, art. 8, art. 22, ePrivacy, overføring) der relevant.
4. Ev. forenlighetsvurdering (art. 6 nr. 4) og ev. utfylt M08.
5. Krav til samtykkeløsningen (hvis samtykke).
6. Konsekvenser: hvilke rettigheter gjelder (protest, portabilitet, tilbaketrekking) [K25 s. 30] – se [T05](../temaer/T05-de-registrertes-rettigheter.md).
7. Tiltak/forutsetninger og hva som må oppdateres (protokoll, erklæring, DPIA).
8. Åpne spørsmål og forbehold.

## Kvalitetskontroll

- [ ] Ett grunnlag per formål, valgt før innsamling [K02 s. 1].
- [ ] Lovhjemmel er konkret angitt der c/e brukes, og innebærer plikt (c) eller oppgave (e) [K02 s. 6, 8].
- [ ] «Nødvendig» er vurdert strengt (avtale og berettiget interesse) [K02 s. 5, 9].
- [ ] Samtykke er ikke valgt der det er maktubalanse [K25 s. 6–7].
- [ ] Art. 9-unntak er vurdert ved sensitive data [K02 s. 2].
- [ ] Interesseavveining er dokumentert med alle tre vilkår [K02 s. 9].
- [ ] Ingen plan om å «falle tilbake» på annet grunnlag hvis samtykket faller [K02 s. 3].
- [ ] Egne vurderinger og ikke-kildebaserte påstander er merket.

## Når skal det eskaleres til jurist/personvernombud

- Særlige kategorier eller straffedommer uten klart unntak; behov for å vurdere om en lovhjemmel er tilstrekkelig [K02 s. 2].
- Forskning, arkiv og statistikk ([popplyl. § 9](../kilder/K42-personopplysningsloven.md#p9) annet ledd krever rådføring med personvernombud med mindre det er gjort DPIA; jf. også [§ 10](../kilder/K42-personopplysningsloven.md#p10)) [K02 s. 2].
- Offentlig sektor som vurderer samtykke eller berettiget interesse.
- Arbeidsforhold (kontroll/overvåking av ansatte – også annen lovgivning, f.eks. arbeidsmiljøloven).
- Barn som målgruppe, profilering, automatiserte avgjørelser.
- Uforenlig viderebehandling eller ønske om å endre grunnlag for eksisterende data.
- Interesseavveining som er tett, eller inngripende sporing/profilering.
- Usikkerhet om ePrivacy-reglene (ekomloven) – se merknader i [K39].

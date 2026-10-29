---
id: A05
tittel: "Arbeidsflyt: Håndtere avvik (brudd på personopplysningssikkerheten)"
gdpr_artikler: [4, 28, 32, 33, 34]
kilder: [K15, K34, K33, K30, K32, K05, K10, K06, K39]
---

# Arbeidsflyt: Håndtere avvik (brudd på personopplysningssikkerheten)

## Når brukes

- Brukeren melder en pågående eller nylig sikkerhetshendelse (phishing, kompromittert konto, løsepengevirus, feilsendt e-post, tapt PC/minnepinne, feil tilgangsstyring, utilsiktet sletting, hendelse hos leverandør).
- En databehandler har varslet om et brudd.
- Brukeren spør om en hendelse skal meldes til Datatilsynet eller varsles til de registrerte.
- Brukeren skal etablere/forbedre en avviksrutine eller vurdere avviksklausuler i en databehandleravtale (bruk steg 0 og [T12](../temaer/T12-avvik-og-brudd-art33-34.md)).

Mal: [M07](../maler/M07-avviksvurdering-og-melding.md). **Tidskritisk: melding uten ugrunnet opphold og om mulig senest 72 timer etter at virksomheten ble kjent med bruddet ([art. 33 nr. 1](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33)).**

## Input agenten trenger fra brukeren

Spør kort og i prioritert rekkefølge – ikke forsink håndteringen:

1. **Er hendelsen stoppet/under kontroll?** Hvis ikke: det er første prioritet [K15 s. 3, 7].
2. Når skjedde den, når ble den oppdaget, og når ble dere kjent med at personopplysninger er berørt?
3. Hva har skjedd (type hendelse, berørte systemer/kontoer/leverandører)?
4. Hvilke opplysninger og hvilke personer er (eller kan være) berørt? Omtrent hvor mange? Særlige kategorier, fødselsnummer, passord, økonomi, barn?
5. Er data kopiert ut, endret eller utilgjengelige? Finnes logger som kan vise det?
6. Var dataene kryptert (og er nøkkelen intakt)? Finnes backup?
7. Er dere behandlingsansvarlig eller databehandler for disse dataene?
8. Er personvernombudet varslet? Er krisestab/IT-sikkerhet/ekstern hendelseshåndterer involvert?

## Steg

0. **(Forberedelse – når det ikke er en akutt hendelse.)** Kontroller at virksomheten har: planverk med roller, klassifisering og beredskap også i ferier/høytider [K15 s. 1; K32 4.1]; kriterier for når en hendelse er et brudd på personopplysningssikkerheten og en 72-timers prosedyre [K33 ark 19]; avviksregister [K30 kap. 17]; oversikt over hvilke systemer som behandler hvilke data og logging som kan dokumentere eksfiltrering [K15 s. 6]; avtaler med eksterne hendelseshåndterere [K15 s. 7]; konkrete avviksklausuler i databehandleravtalene [K05]; øvelser minst hvert annet år [K30 kap. 17].

1. **Stopp og inneslutt.** Iverksett tiltak for å stoppe bruddet (stenge/låse kontoer, tilbakestille passord, isolere systemer, fjerne offentlig tilgang, be feilmottaker slette). Aktiver krisestab og ekstern hjelp ved behov. Sikre logger og bevis, og før tidslinje [K15 s. 3, 7; K32 4.3]. Ved løsepengevirus: følg politiets råd om ikke å betale [K15 s. 6].

2. **Registrer hendelsen og start klokka.** Opprett post i avviksregisteret (M07 del A1–A2). Fastsett tidspunktet virksomheten ble kjent med bruddet og regn ut fristen (72 timer) [K15 s. 1]. Varsle PVO [K15 s. 7].

3. **Er dere databehandler?** Varsle den behandlingsansvarlige **straks** ([art. 33 nr. 2](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33): «uten ugrunnet opphold»), med all tilgjengelig informasjon (art. 33 nr. 3-feltene), og oppdater fortløpende. Den behandlingsansvarlige vurderer og melder [K05; K39 s. 36]. Fortsett med bistand (steg 4–5 for egen del), og følg avtalens frister.

4. **Klassifiser.** Er personopplysninger berørt? Hvilken bruddtype – konfidensialitet, integritet, tilgjengelighet (ofte flere) [K34 s. 1]? Ingen personopplysninger → loggfør som sikkerhetshendelse og avslutt personvernsporet. Fyll ut M07 A3–A4. Husk at kompromittert e-post typisk berører kontoeier, alle i e-poster/kontakter og mottakere – ofte hundrevis [K15 s. 3].

5. **Vurder risikoen for de registrerte (M07 del B1).** Vurder opplysningenes art, volum, identifiserbarhet, konsekvenser (identitetstyveri, svindel, økonomisk tap, diskriminering, omdømme, taushetsbelagte opplysninger), varighet, sårbare grupper og risikoreduserende forhold (kryptering, logging, gjenoppretting) [K33 ark 19; K12 s. 6; K15 s. 6]. Bruk Datatilsynets hendelsestabell som utgangspunkt: vellykket phishing/e-postangrep → normalt melde; løsepengevirus med uklart om data er på avveie → meld i påvente; DDoS → bare ved risiko; CEO-svindel → konkret [K15]. Konkluder: ingen risiko / risiko / høy risiko (M07 B2). Tersklene står i [art. 33 nr. 1](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33) (meldeplikt med mindre bruddet «sannsynligvis ikke vil medføre en risiko») og [art. 34 nr. 1](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-34) (underretning ved sannsynlig «høy risiko»).

6. **Meld til Datatilsynet uten ugrunnet opphold, om mulig innen 72 timer (ved risiko).** Fyll ut M07 del C ([art. 33 nr. 3](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33)-innholdet: art, kategorier og antall, kontaktpunkt, konsekvenser, tiltak). **Send foreløpig melding selv om informasjonen er ufullstendig**, og send utfyllende melding senere (art. 33 nr. 4) [K15 s. 1; K33 ark 19]. Meldes det etter 72 timer, oppgi årsaken (art. 33 nr. 1). **[Merknad – ikke fra kildene]** Bruk Datatilsynets gjeldende elektroniske meldeskjema; ved grenseoverskridende behandling, avklar ledende tilsynsmyndighet.

7. **Varsle (underrette) de registrerte uten ugrunnet opphold (ved høy risiko, [art. 34](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-34)).** Vurder unntakene i art. 34 nr. 3 (kryptering som gjør data uforståelige; etterfølgende tiltak; uforholdsmessig innsats → offentlig kunngjøring) [K10; K30 kap. 17]. Bruk tekstmalen i M07 del D: klart språk, hva som har skjedd, hvilke data, mulige konsekvenser, hva virksomheten har gjort, konkrete råd og kontaktpunkt; send i en kanal der folk faktisk ser det, adskilt fra markedsføring [K06; K30 kap. 17].

8. **Andre varsler.** Vurder politianmeldelse og varsel til NSM/NCSC [K15 s. 7]; sektormyndigheter og andre lovpålagte meldeplikter [K33 ark 19]; bank ved svindel [K15 s. 3, 5]; felles behandlingsansvarlige; styre/forsikring (M07 B4).

9. **Følg opp og oppdater.** Oppdater Datatilsynet og de registrerte ved ny vesentlig informasjon. Gjenopprett systemer («build back better») [K32 4.3.4]. Kartlegg rotårsak [K32 4.3.6].

10. **Lukk og lær.** Fullfør M07 del E: rotårsak, lærdommer, forbedringstiltak med ansvarlig og frist, behov for oppdatert risikovurdering (art. 32, [A03](A03-risikovurdering-informasjonssikkerhet.md)) eller DPIA ([A02](A02-gjennomfore-dpia.md)), og endringer i databehandleravtaler ([A01](A01-gjennomga-databehandleravtale.md)) [K32 4.4; K30 kap. 17]. Dokumenter begrunnelsen dersom det ikke ble meldt eller varslet. Orienter ledelsen.

## Output

- Avviksregisterpost (M07 del A) – for alle hendelser.
- Dokumentert vurdering av meldeplikt og varslingsplikt med begrunnelse (M07 del B).
- Ferdig utkast til melding til Datatilsynet (M07 del C) – foreløpig og utfyllende.
- Utkast til varsel til de registrerte (M07 del D) ved høy risiko.
- Oversikt over andre varsler (politi, NSM, sektormyndighet, behandlingsansvarlig).
- Oppfølgingsplan og lærdommer (M07 del E).

## Kvalitetskontroll

- [ ] Første melding sendt innen 72 timer, eller forsinkelsen er begrunnet [K15 s. 1; K34 s. 2].
- [ ] Vurderingen er gjort ut fra risiko for de registrerte, ikke virksomheten [K33 ark 19].
- [ ] Integritets- og tilgjengelighetsbrudd er vurdert, ikke bare konfidensialitet [K34 s. 1].
- [ ] Antall berørte er realistisk anslått (e-postkontoer!) [K15 s. 3].
- [ ] Meldingen dekker art, kategorier og antall, kontaktpunkt, konsekvenser og tiltak.
- [ ] Varselet til de registrerte er forståelig og gir konkrete råd [K06; K30 kap. 17].
- [ ] Hendelsen står i avviksregisteret uansett utfall [K34 s. 1].
- [ ] Unntak fra varsling er dokumentert (f.eks. kryptering med intakt nøkkel) [K10].
- [ ] Alle opplysninger agenten ikke har fått bekreftet er merket som foreløpige.

## Når skal det eskaleres til jurist/personvernombud

- **PVO skal involveres tidlig i alle brudd** som kan berøre personopplysninger [K15 s. 7].
- Høy risiko / tvil om varsling av de registrerte → PVO og jurist.
- Særlige kategorier, fødselsnummer, barn, mange berørte, eller data publisert/forsøkt solgt → PVO, jurist, ledelse/krisestab.
- Løsepengevirus, utpressing eller mistanke om statlig aktør → krisestab, ledelse, politi/NSM, jurist.
- Brudd hos databehandler der informasjonen er mangelfull eller forsinket → jurist (avtaleforhold) og PVO.
- Grenseoverskridende behandling (registrerte i flere EØS-land) → jurist (ledende tilsynsmyndighet).
- Risiko for erstatningskrav, mediedekning eller tilsynssak → jurist og ledelse.
- Fristen på 72 timer er i ferd med å bli oversittet → PVO umiddelbart; send foreløpig melding.

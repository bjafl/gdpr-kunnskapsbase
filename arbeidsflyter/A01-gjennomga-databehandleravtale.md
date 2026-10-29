---
id: A01
tittel: "Arbeidsflyt – gjennomgå databehandleravtale / leverandøravtale"
gdpr_artikler: [24, 26, 28, 32, 33, 34, 44, 45, 46]
kilder: [K01, K05, K06, K10, K11, K14, K26, K30, K33, K39]
---

# A01 – Gjennomgå databehandleravtale (DPA) / leverandøravtale

## Når brukes

- Brukeren skal inngå, fornye eller revidere avtale med en leverandør som behandler personopplysninger (SaaS, sky, drift, support, lønn, markedsføring, analyse, apputvikler, SDK).
- Brukeren har fått leverandørens standard-DPA («take it or leave it») og vil vite om den holder.
- Brukeren vil lage egen DPA eller bruke dansk standard-DPA / EU-kommisjonens standardavtale [K05 s. 4].
- Ved revisjon av eksisterende leverandørportefølje eller etter endringer hos leverandøren (nye underdatabehandlere, ny region, nye funksjoner).

**Hovedverktøy:** [M01 Sjekkliste](../maler/M01-databehandleravtale-sjekkliste.md). **Fagbakgrunn:** [T07](../temaer/T07-databehandleravtale-art28.md), [T01](../temaer/T01-roller-behandlingsansvarlig-databehandler.md).

## Input agenten trenger fra brukeren

Still disse spørsmålene (de som ikke kan besvares, noteres som «Uklart» i rapporten):

1. **Dokumenter:** DPA, hovedavtale/tjenestevilkår, sikkerhetsvedlegg/-dokumentasjon, liste over underdatabehandlere, SCC/overføringsdokumentasjon, sertifikater/revisjonsrapporter. Hvilken versjon og dato?
2. **Tjenesten:** Hva skal leverandøren gjøre? Hvilket system? Hvilke funksjoner er aktivert (inkl. analyse, KI, telemetri)?
3. **Data:** Hvilke kategorier registrerte og opplysninger? Særlige kategorier, straffedommer, barn, fødselsnummer? Omtrentlig volum?
4. **Formål** hos brukeren og behandlingsgrunnlag (finnes i protokollen?).
5. **Hvem er brukeren** – behandlingsansvarlig, eller selv databehandler som skal bruke underdatabehandler?
6. **Lokasjon:** Hvor lagres data, og fra hvilke land kan leverandøren/underleverandører få tilgang (support, drift)? Er leverandøren eller morselskapet underlagt tredjelands lov?
7. **Risiko:** Finnes DPIA, risikovurdering eller TIA? Er tjenesten forretningskritisk?
8. **Forhandlingsrom:** Kan avtalen endres, eller er den standard?
9. **Frister og beslutningstaker:** Når skal avtalen signeres, og hvem godkjenner?

## Steg

1. **Rolleavklaring** – avgjør om det faktisk er et databehandleroppdrag, og for hvilke behandlinger.
   - Bruk vurderingsmomentene: hvem bestemmer formål og vesentlige midler, hva går oppdraget ut på, har leverandøren egne forpliktelser, bruker den data til egne formål [K01 s. 4–6] → [T01](../temaer/T01-roller-behandlingsansvarlig-databehandler.md).
   - Bryt relasjonen ned per behandling: databehandling for kunden / felles behandlingsansvar / leverandørens egne formål (særlig ved SDK, analyse, reklame, telemetri, KI) [K39 s. 17–22].
   - Definisjoner: [art. 4 nr. 7 og 8](../kilder/K43-gdpr-kap01-alminnelige-bestemmelser.md#art-4); databehandler som selv fastsetter formål og midler, anses som behandlingsansvarlig ([art. 28 nr. 10](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-28)).
   - Utfall: (a) databehandler → fortsett; (b) selvstendig behandlingsansvarlig → DPA er feil verktøy; vurder grunnlag for utlevering [K01 s. 9] og gå til [A06](A06-vurdere-behandlingsgrunnlag.md); (c) felles ansvar → [art. 26](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-26)-ordning i tillegg; (d) blandet → DPA for databehandlingsdelen + regulering/forbud for resten.
   - Dokumenter vurderingen (M01 rad 1.1).

2. **Garantivurdering ([art. 28 nr. 1](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-28))** – før avtaleteksten.
   - Kompetanse, pålitelighet, ressurser; sertifisering og scope; sikkerhetsdokumentasjon; underleverandørkjeden [K05 s. 3; K33 ark 14].
   - Notér om leverandøren tar forbehold som innebærer mulig brudd på GDPR – da kan den ikke brukes uten tiltak [K14 s. 9–10].

3. **Art. 28-krav – avtaleteksten punkt for punkt** (M01 del 2–4). Ordlyd: [art. 28 nr. 3](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-28).
   - Behandlingsbeskrivelse: gjenstand (tema), art, formål, varighet, registrerte, opplysningstyper – konkret og i samsvar med protokollen [K05 s. 4; K11].
   - Behandlingsansvarliges rettigheter: instrukser, bestemmelsesrett, oppsigelsesrett [K05 s. 4].
   - Bokstav a–h + varsel om ulovlig instruks [K05 s. 5–6]. Marker hvert punkt OK / Mangler / Uklart.
   - Se særlig etter: bruk til egne formål, ensidig endringsrett, vage lov-/myndighetsforbehold, «reasonable efforts» uten frister, revisjon begrenset til sertifikater, sletting uten frist [T07 «Vanlige feil»](../temaer/T07-databehandleravtale-art28.md).

4. **Sikkerhet ([art. 32](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-32))** – sikkerhetsvedlegget og dokumentasjonen.
   - Sammenlign med risikonivået og [M09](../maler/M09-sikkerhetstiltak-sjekkliste.md): kryptering i ro og transitt, nøkkelhåndtering, tilgangsstyring og autentisering, logging, backup, fjernvedlikehold, sårbarhetshåndtering, kontinuitet [K05 s. 5; K33 ark 14–16, 22; K10].
   - For apper/SDK: TLS, nøkkellager, MASVS L1, oppdateringsplikt [K39 s. 55–56].
   - Ved behov for full risikovurdering: [A03](A03-risikovurdering-informasjonssikkerhet.md), [T08](../temaer/T08-informasjonssikkerhet-art32.md).

5. **Underdatabehandlere** (lovens «annen databehandler», [art. 28 nr. 2 og 4](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-28); M01 rader 4.d1–4.d6).
   - Hvilken modell (særlig/generell/forbud)? Fullstendig liste med tjeneste, **lagrings- og tilgangsland** og overføringsgrunnlag? Varslingsfrist og reell mulighet til å motsette seg endringer (art. 28 nr. 2)? Samme forpliktelser videreført? Fullt ansvar? Hele kjeden? [K05 s. 5; K01 s. 9; K30 kap. 34.3; K39 s. 53]
   - Kontroller samsvar med mottakerinformasjonen i personvernerklæringen [K26].

6. **Overføring til tredjeland** (M01 del 5; [art. 44–49](../kilder/K43-gdpr-kap05-overforing-av-personopplysninger-til-tredjestater.md#art-44)).
   - Kartlegg alle overføringer, også fjerntilgang/support, underdatabehandlere og videreoverføringer [K14 s. 7].
   - Identifiser grunnlag per mottaker (adekvans, SCC-modul, BCR, art. 49) [K14].
   - Ved SCC/BCR eller EØS-leverandør underlagt tredjelands lov: gjennomfør eller kontroller TIA og supplerende tiltak – følg **[A04 Overføring og TIA](A04-overforing-og-tia.md)** og **[T11](../temaer/T11-overforing-tredjeland-og-tia.md)**, med [M06 TIA-mal](../maler/M06-tia-mal.md).
   - Vage og vide forbehold om utlevering til tredjelands myndigheter er et typisk holdepunkt for at tiltak kreves [K14 s. 9–10].

7. **Kobling til andre plikter.**
   - Protokoll: databehandleren, overføringer og sikkerhet registrert [K11] → [M02](../maler/M02-protokoll-art30.md).
   - DPIA: kreves eller må oppdateres? [M05](../maler/M05-dpia-terskelvurdering.md), [A02](A02-gjennomfore-dpia.md).
   - Personvernerklæring: mottaker og ev. tredjeland oppført [K06 s. 2].
   - Avvikshåndtering: leverandørens varslingsfrist (lovkrav: «uten ugrunnet opphold», [art. 33 nr. 2](../kilder/K43-gdpr-kap04-behandlingsansvarlig-og-databehandler.md#art-33)) passer inn i egen 72-timersrutine → [A05](A05-avvikshandtering.md).

8. **Klassifiser funn.**
   - **Kritisk** (må rettes før signering): feil rolle; ingen instruks; bruk til egne formål uten regulering; uregulert/ulovlig overføring; ingen sletting; revisjon utelukket; ingen brudd-varsling; manglende garantier.
   - **Vesentlig** (bør forhandles): uklare frister, svak underdatabehandlerordning, generiske beskrivelser, mangelfullt sikkerhetsvedlegg.
   - **Mindre**: anbefalte punkter (tilsynsprosedyre, slettemetode, kontaktpunkt).
   - Juster etter risiko – ved høy risiko blir A-punkter vesentlige [K05 s. 1].

9. **Formuler anbefalte endringer.**
   - Bruk Datatilsynets eksempelformuleringer der de finnes [K05 s. 4–6] og forslagene i M01; marker egne forslag som utkast til juridisk kvalitetssikring.
   - Ved standardavtaler uten forhandlingsrom: foreslå konfigurasjonstiltak (region, kundestyrte nøkler, avslå telemetri/egne formål), tilleggsavtale eller alternativ leverandør [K01 s. 3].

10. **Skriv rapport** (se Output) og legg ved utfylt M01.

## Output

Rapport med følgende struktur:

1. **Sammendrag** (3–6 linjer): leverandør, tjeneste, rolle, risikonivå, samlet anbefaling (signere / signere med endringer / ikke signere / eskalere).
2. **Rolleavklaring** med begrunnelse.
3. **Funnliste** – tabell: nr., M01-referanse, funn, alvorlighetsgrad (kritisk/vesentlig/mindre), hjemmel og kilde, anbefalt endring/formulering.
4. **Overføringsvurdering** – status og henvisning til TIA.
5. **Sikkerhet** – hovedfunn.
6. **Åpne spørsmål** til leverandøren (Uklart-punktene).
7. **Oppfølging etter signering:** revisjonsplan/-frekvens, protokoll- og DPA-register, personvernerklæring, DPIA [K05 s. 6; K39 s. 36–37].
8. **Vedlegg:** utfylt M01.

## Kvalitetskontroll

- [ ] Rollen er vurdert per behandling, ikke bare per leverandør [K39 s. 17].
- [ ] Alle bokstaver a–h + siste ledd er vurdert eksplisitt [K05 s. 5–6].
- [ ] Overføring er vurdert også for fjerntilgang og underdatabehandlere [K14 s. 7].
- [ ] Hver funn har hjemmel og kildehenvisning; egne vurderinger er merket.
- [ ] Skillet lovkrav / anbefaling er tydelig [K05].
- [ ] Datatilsynets eksempelformuleringer er gjengitt ordrett der de brukes.
- [ ] Ingen påstander om leverandørens praksis som ikke står i dokumentene – det som ikke er dokumentert er «Uklart».
- [ ] Rapporten sier hva som må til før signering, og hva som kan følges opp senere.

## Når skal det eskaleres til jurist/personvernombud

- Rollen er uklar eller blandet (felles ansvar, leverandørens egne formål, SDK-er med egne formål).
- Særlige kategorier, straffedommer, barn eller store volumer – eller DPIA viser høy risiko.
- Overføring til tredjeland uten adekvans, eller EØS-leverandør underlagt tredjelands lov med vide utleveringsforbehold [K14 s. 9–10].
- Leverandøren nekter å endre kritiske punkter (instruks, egne formål, sletting, revisjon, varsling).
- Ansvarsbegrensninger, erstatning og regress mellom partene (art. 82) – utenfor agentens mandat.
- Offentlig sektor (anskaffelsesregler, arkiv, sikkerhetsloven) eller sektorlovgivning (helse, finans).
- Når en avtale skal signeres på tross av kritiske funn (risikoaksept må tas av ledelsen).

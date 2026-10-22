---
id: M06
tittel: "Mal: Overføringskonsekvensvurdering (Transfer Impact Assessment, TIA)"
gdpr_artikler: [4, 5, 6, 9, 10, 13, 14, 23, 28, 44, 45, 46, 47, 49, 87]
kilder: [K38, K14, K05, K10, K24]
---

# Mal: Overføringskonsekvensvurdering (Transfer Impact Assessment, TIA)

> **Bruk av malen.** Malen følger CNILs TIA-guide (januar 2025), som bygger på EDPB Recommendations 01/2020 og har forutsetningskontroller pluss seks steg [K38], supplert med Datatilsynets veiledning om overføring ut av EØS og Schrems II-vurderingen [K14 s. 7–10]. TIA gjøres av **eksportøren** (behandlingsansvarlig eller databehandler) **med importørens bistand**, **før** overføring som bygger på et **art. 46-verktøy** (SCC, BCR m.fl.) [K38 s. 3]. Kursiv er veiledning. Fagstoff: [T11](../temaer/T11-overforing-tredjeland-og-tia.md). Prosess: [A04](../arbeidsflyter/A04-overforing-og-tia.md). Datatilsynet kan ikke forhåndsgodkjenne vurderingen – dokumentasjonen er avgjørende i tilsyn [K14 s. 8].

---

## 0. Dokumentkontroll

| Felt | Utfylling |
|---|---|
| TIA-ID / navn | |
| Behandling(er) som omfattes (ref. protokoll) | |
| Utarbeidet av / dato | |
| Bistand fra importør (navn, kontakt, dato for mottatt informasjon) | |
| Versjon | |
| Tilknyttet DPIA (M04) / DPA / SCC-avtale | |

---

## DEL A – Forutsetninger før TIA

### A1. Foreligger det en overføring?

| Spørsmål | Ja/Nei | Begrunnelse |
|---|---|---|
| Er dataene personopplysninger (art. 4 nr. 1)? | ☐ | |
| Er eksportøren underlagt GDPR for behandlingen? | ☐ | |
| Sender eller gjør eksportøren opplysningene tilgjengelige for en **annen, rettslig atskilt** behandlingsansvarlig/databehandler (importør)? | ☐ | *Egen ansatt på reise = ikke overføring; konsernselskap = kan være overføring [K38 s. 6; K14 s. 1].* |
| Er importøren i et land utenfor EØS eller en internasjonal organisasjon (uansett om importøren selv er underlagt GDPR etter art. 3)? | ☐ | |
| Gjelder det fjerntilgang/support fra tredjeland til data i EØS? | ☐ | *Er overføring [K38 s. 6; K14 s. 7].* |
| Leverandør underlagt tredjelands lov uten avtalt tilgang fra utlandet? | ☐ | *Vurder Datatilsynets firestegsmodell (A6 nedenfor) [K14 s. 9–10].* |

**Konklusjon A1:** ☐ Overføring – fortsett ☐ Ikke overføring – dokumenter og avslutt (andre krav, f.eks. art. 32, gjelder fortsatt)

### A2. Kreves TIA?

| Spørsmål | Svar | Konsekvens |
|---|---|---|
| Har mottakerlandet en **gjeldende** adekvansbeslutning, og faller importøren/sektoren innenfor beslutningens omfang? | ☐ Ja ☐ Nei | *Ja → ingen TIA eller tilleggstiltak nødvendig [K38 s. 6; K14 s. 2]. Dokumenter verifiseringen.* |
| Dato og kilde for verifisering av adekvansstatus | | *Sjekk EU-kommisjonens oversikt og datatilsynet.no. Forbehold: Canada (PIPEDA), Japan (APPI, unntak bl.a. media/akademia), Sør-Korea, Færøyene; **USA bare DPF-sertifiserte** (verifiser på dataprivacyframework.gov og at sertifiseringen dekker aktuelle data, f.eks. HR) [K14 s. 2; K38 s. 7].* |
| Brasil: er adekvans bekreftet på vurderingsdatoen? | ☐ Ja ☐ Nei ☐ Ikke relevant | *K14 lister Brasil som adekvat (s. 2), men et eksempel i samme kilde (s. 3) behandler Brasil som ikke-adekvat. Verifiser alltid gjeldende status før du konkluderer [K14 merknad].* |
| DPF: er aktuell status for EU-U.S. Data Privacy Framework kontrollert? | ☐ Ja ☐ Ikke relevant | ***[Merknad – ikke fra kildene]** DPF har vært rettslig utfordret; verifiser status. Vurder SCC som reserve.* |
| Bygger overføringen på et art. 49-unntak? | ☐ Ja ☐ Nei | *Ja → ingen TIA, men vilkårene i art. 49 må være oppfylt og dokumentert; restriktiv tolkning [K38 s. 7; K14 s. 12–14].* |

**Konklusjon A2:** ☐ TIA kreves (art. 46-verktøy) ☐ TIA kreves ikke – begrunnelse dokumentert: …

*Det anbefales å dokumentere beslutningen om ikke å gjennomføre TIA [K38 s. 16].*

### A3. Roller og ansvar for TIA

| Felt | Utfylling |
|---|---|
| Tilfelle | ☐ 1: Behandlingsansvarlig (EØS) → databehandler (tredjeland) ☐ 2: Databehandler (EØS) → underdatabehandler (tredjeland) ☐ 3: Behandlingsansvarlig (EØS) → behandlingsansvarlig (tredjeland) ☐ Annet |
| Hvem gjennomfører TIA (eksportør) | |
| Hvem bistår (importør) og hva er levert (lovanalyse, åpenhetsrapporter, oversettelser) | *Databehandler plikter å gi informasjon som viser etterlevelse, inkl. TIA (art. 28 nr. 3 h) [K38 s. 8–9].* |
| Ved tilfelle 2: har behandlingsansvarlig mottatt **hele** TIA-en med konkrete bevis (ikke bare sammendrag)? Er den verifisert/komplettert? | *Et sammendrag uten bevis oppfyller ikke databehandlerens plikt; behandlingsansvarlig tar endelig beslutning og skal verifisere grundigere jo høyere risiko [K38 s. 9].* |

### A4. Omfang og videreoverføringer

| Ledd i kjeden | Eksportør | Importør | Land | Rolle | Grunnlag | Dekket av denne TIA? |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 (videreoverføring) | | | | | | |
| 3 | | | | | | |

*Hele dataflyten, inkl. videreoverføringer, skal med [K38 s. 10]. Ved SCC: videreoverføring bare til part som er bundet av/tiltrer SCC, eller etter modul 1 kl. 8.7–8.8 / modul 2–3 kl. 8.8 [K38 s. 10].*

### A5. Samsvar med GDPR-prinsippene

| Spørsmål | Svar |
|---|---|
| Behandlingsgrunnlag (art. 6, ev. 9/10) for overføringen | |
| Er bare strengt nødvendige data med (minimering)? | |
| Kan anonymiserte data overføres i stedet? | *Da gjelder ikke GDPR, forutsatt effektiv anonymisering [K38 s. 11].* |
| Er de registrerte informert (art. 13–14) og står overføringen i protokollen (art. 30)? | *[K38 s. 11; K14 s. 7]* |

### A6. (Ved leverandør underlagt tredjelands lov med data i EØS) Datatilsynets fire steg

| Steg [K14 s. 9–10] | Vurdering |
|---|---|
| 1. Kan overføringer likevel skje (support fra tredjeland, forbehold om utlevering, tredjelands rettslige forpliktelser)? | |
| 2. Hvem er behandlingsansvarlig for den mulige overføringen (vi / leverandøren)? | |
| 3. Hvilke garantier og tiltak sikrer at leverandøren ikke overfører ulovlig (art. 28 nr. 1)? Finnes vage forbehold i avtalen? | *Vage og vide forbehold er et typisk holdepunkt for at tiltak må iverksettes [K14 s. 10].* |
| 4. Hva er avtalt (er leverandøren behandlingsansvarlig for noe)? Har vi grunnlag for utlevering? | |

---

## DEL B – Steg 1: Kjenn overføringen

### B1. Eksportør

| Felt | Utfylling |
|---|---|
| Navn | |
| Kontaktpunkt (avdeling/person ansvarlig for overføringen) | |
| Eksportland | |
| Rolle | ☐ Behandlingsansvarlig ☐ Felles behandlingsansvarlig ☐ Databehandler – i så fall behandlingsansvarlig: … |
| Annen nyttig informasjon | |

### B2. Importør

| Felt | Utfylling |
|---|---|
| Navn | |
| Kontaktpunkt | |
| Importland | |
| Rolle | ☐ Behandlingsansvarlig ☐ Felles behandlingsansvarlig ☐ Databehandler – behandlingsansvarlig: … |
| Arten av importørens virksomhet (avgjør hvilke lover som gjelder) | *Er importøren særlig beskyttet i mottakerlandet, f.eks. helsetjenester eller advokat? [K38 s. 12]* |
| Annen nyttig informasjon (morselskap, underleverandører, sertifiseringer) | |

### B3. Overføringen

| Felt | Utfylling |
|---|---|
| Importørens behandlingsaktiviteter | *F.eks. IT-støtte, hosting, SaaS, markedsføring [K38 s. 13].* |
| Type overføring | ☐ Fjerntilgang uten mulighet for nedlasting/lagring ☐ Fjerntilgang med mulighet for nedlasting/lagring ☐ Overføring og hosting/lagring i tredjeland ☐ Annet: … |
| Overføringsmetode | *SFTP, API, e-post, ekstern tilkobling, fysisk medium* |
| Dataformat | ☐ Klartekst ☐ Kryptert (hvem har nøkkel?) ☐ Pseudonymisert (hvem har koblingsnøkkel?) ☐ Annet |
| Frekvens | ☐ Enkeltoverføring ☐ Sporadisk (hyppighet) ☐ Regelmessig/kontinuerlig (hyppighet) |
| Mulig videreoverføring fra importør | ☐ Ja (spesifiser) ☐ Nei |
| Kategorier personopplysninger | ☐ Identifikasjon ☐ Kontakt ☐ Familieliv ☐ Arbeidsliv ☐ Tjenestebruk ☐ Annet: … |
| Særlige kategorier | ☐ Etnisitet ☐ Politisk oppfatning ☐ Religion/livssyn ☐ Fagforening ☐ Genetiske/biometriske (identifisering) ☐ Helse ☐ Seksuelle forhold/legning ☐ Ingen |
| Andre svært personlige opplysninger | ☐ Straffedommer/lovovertredelser (art. 10) ☐ Nasjonalt ID-nummer/fødselsnummer (art. 87) ☐ Lokasjonsdata ☐ Finansielle data (svindelrisiko) ☐ Annet ☐ Ingen |
| Kategorier registrerte | |
| Sårbare registrerte (barn, pasienter, avhengige personer) | ☐ Ja (spesifiser) ☐ Nei |
| Hel eller delvis overføring (andel av datasettet) | ☐ Hel ☐ Delvis (%) |
| Datavolum / antall registrerte | |
| Startdato / sluttdato eller varighet | |

*Tabellene er fra [K38 s. 12–15]. Protokollen og kontrakten kan brukes som kilde.*

---

## DEL C – Steg 2: Overføringsverktøy

| Felt | Utfylling |
|---|---|
| Art. 46-verktøy | ☐ SCC 2021/914 – modul: ☐1 ☐2 ☐3 ☐4 ☐ BCR-C ☐ BCR-P ☐ Atferdsnorm (*ingen godkjente per i dag*) ☐ Sertifisering (*ingen godkjente per i dag*) ☐ Ad hoc-klausuler (*krever godkjenning*) [K14 s. 3; K38 s. 16] |
| Dokumentasjon (signert avtale, BCR med enhetsliste, sertifikat) | |
| Er SCC brukt uendret? Tilleggsklausuler som ikke motsier SCC? | *Uendret → ingen godkjenning/varsel [K14 s. 4]. Endring som begrenser rettigheter/plikter krever godkjenning [K38 s. 27 fn. 56].* |
| Ved modul 2/3: dekker SCC også art. 28? | *Ja – egen DPA ikke nødvendig [K14 s. 4]; kontroller likevel at instrukser og vedlegg er fylt ut.* |

**Konklusjon steg 2:** ☐ Art. 46-verktøy → TIA kreves, gå til steg 3.

---

## DEL D – Steg 3: Lov og praksis i mottakerlandet

*Formål: avgjøre om lov eller praksis kan undergrave garantiene i verktøyet. Ta hensyn til egenskapene fra steg 1 [K38 s. 17]. Kildene skal være relevante, objektive, pålitelige, verifiserbare og tilgjengelige [K14 s. 8; K38 s. 17]. Bruk EDPB Rec. 01/2020 vedlegg 3, landanalyser, importørens bidrag og bransjenettverk [K38 s. 17].*

### D1 (3A). Personvernlovgivning

| Spørsmål | Svar | Kilde |
|---|---|---|
| Hvilket personvernrammeverk gjelder for importøren? | | |
| Virkeområde | ☐ Generelt ☐ Sektorielt (spesifiser) | |
| Tilsluttet internasjonale personvernkonvensjoner (f.eks. konvensjon 108+)? | ☐ Ja ☐ Nei | |
| Finnes kompetent personvernmyndighet? | ☐ Ja (navn) ☐ Nei | |
| Er den uavhengig? | ☐ Ja ☐ Nei – begrunn | *Vurder etter GDPR art. 52–54, konvensjon 108+ art. 15 m.fl. [K38 s. 18].* |

### D2 (3B). De registrertes rettigheter

| Rettighet | Finnes? (☐ Ja – referanse / ☐ Nei) |
|---|---|
| Innsyn | |
| Retting | |
| Sletting | |
| Protestere mot behandling i særlige situasjoner | |
| Protestere mot automatiserte avgjørelser | |
| Andre | |
| Er lovbestemte begrensninger nødvendige og forholdsmessige i et demokratisk samfunn? | |

### D3 (3C). Rettsmidler og sanksjoner

| Spørsmål | Svar (Ja/Nei – begrunn) |
|---|---|
| Finnes effektive rettsmidler? | |
| Finnes effektive og avskrekkende sanksjoner? | |
| Kan registrerte i EØS utøve rettighetene og rettsmidlene? | |

### D4 (3D). Lover og praksis som gir myndigheter tilgang

| Spørsmål | Svar | Referanser og beskrivelse (virkeområde, myndighet, pliktens art) |
|---|---|---|
| Finnes **overvåkingslover** som gjelder importøren og kan pålegge utlevering eller gi myndigheter tilgang til de overførte dataene? | ☐ Ja ☐ Nei | *Generelle lover, strafferett, nasjonal sikkerhet, skatt, regulering, politi, etterretning [K38 s. 19].* |
| Finnes **overvåkingspraksis** som gir slik tilgang (også uten eller i strid med lov)? | ☐ Ja ☐ Nei | |

*Momenter for hvilke lover som gjelder: formål, aktørtype, sektor, datakategori, lagring vs. fjerntilgang, dataformat, videreoverføring [K14 s. 7–8].*

### D5 (3E). European Essential Guarantees (EDPB Rec. 02/2020)

| Garanti | Ja/Nei – begrunnelse |
|---|---|
| Tilgang styrt av klare, presise og tilgjengelige regler | |
| Tilgang nødvendig og forholdsmessig for et formål i art. 23 nr. 1 (nasjonal sikkerhet, forsvar, offentlig sikkerhet, straffeforfølgning, viktige allmenne interesser m.m.) | |
| Uavhengig tilsynsmekanisme | |
| Myndigheten er underlagt åpenhet og regelmessig kontroll | |
| Den registrerte har generelle (uavhengig av statsborgerskap) og effektive rettsmidler for et uavhengig og upartisk organ | |

*[K38 s. 20]. Datatilsynet: bare lover/praksis som går lenger enn nødvendig og proporsjonalt er en **krenkelse**; tiltak trengs bare ved krenkelse [K14 s. 7].*

### D6 (3F). Rettsstat

| Spørsmål | Svar |
|---|---|
| Finnes rettsstatsproblemer som påvirker de registrertes mulighet til å søke oppreisning mot ulovlig tilgang? | ☐ Ja (beskriv) ☐ Nei |

### D7 (3G). Mottatte begjæringer og «grunn til å tro»

| Spørsmål | Svar |
|---|---|
| Kan importøren dokumentere at den ikke har mottatt begjæringer om / vært utsatt for direkte myndighetstilgang til EØS-data (siste år)? Hvordan (åpenhetsrapport)? | ☐ Ja ☐ Nei – type, antall, håndtering |
| Er importøren forbudt å informere om begjæringer? | ☐ Ja ☐ Nei – *i så fall kan historikk ikke vektlegges [K14 s. 8]* |
| Kan det dokumenteres at det **ikke er grunn til å tro** at problematisk lov vil anvendes på disse dataene/denne importøren (sektor, historikk, erfaringer fra lignende aktører, lovens nøkkelbegreper)? | ☐ Ja (beskriv grundig) ☐ Nei |

*Fravær av begjæringer er ikke alene nok, men kan inngå i en helhetsvurdering [K14 s. 8]. Datatilsynet (Sikt-saken): vurderingen er binær; ikke krav om 100 % sikkerhet, men en viss sannsynlighetsovervekt; spørsmålet er om loven får anvendelse, ikke om myndighetene vil bruke den [K14 s. 15].*

### D8. Konklusjon steg 3

| Nr. | Konklusjon | Kryss | Videre |
|---|---|---|---|
| (1) | Verktøyet er effektivt; overføring kan skje uten supplerende tiltak | ☐ | Steg 6 |
| (2) | Verktøyet er ikke effektivt; supplerende tiltak må iverksettes | ☐ | Steg 4 |
| (3) | Verktøyet er ikke effektivt, men det er ikke grunn til å tro at problematisk lov anvendes i praksis – overføring uten supplerende tiltak (påvist og dokumentert) | ☐ | Steg 6 |

**Begrunnelse:** …

*[K38 s. 21–22]*

---

## DEL E – Steg 4: Supplerende tiltak

*Tiltak identifiseres per overføring og land; jo høyere risiko, jo flere og grundigere tiltak. Kontraktuelle og organisatoriske tiltak alene er som regel ikke nok – tekniske tiltak må inngå [K38 s. 22; K14 s. 8]. Involver CISO.*

### E1 (4A). Eksisterende tiltak

**Tekniske tiltak**

| Tiltak | Implementert? | Beskrivelse (hvem gjennomfører) | Samsvar med EDPB-vilkår | Risikoer som reduseres |
|---|---|---|---|---|
| Pseudonymisering | ☐ | | *Kontroller alle: (1) data kan ikke knyttes til person uten tilleggsinformasjon; (2) tilleggsinformasjonen holdes **utelukkende av eksportøren**, separat, i EØS/likeverdig jurisdiksjon; (3) eksportøren har eneste kontroll over algoritme/register; (4) analyse viser at data ikke kan reidentifiseres selv med informasjon myndighetene kan ha [K38 s. 23].* | |
| Kryptering | ☐ | | *Kontroller alle: (1) state-of-the-art transportkryptering mot aktive/passive angrep; (2) pålitelig PKI; (3) tiltak mot angrep på sende-/mottakssystemer, testing for bakdører; (4) ende-til-ende på applikasjonslaget ved behov; (5) robust algoritme og nøkkellengde; (6) styrke tilpasset hvor lenge konfidensialiteten må vare; (7) korrekt implementert i vedlikeholdt programvare; (8) **nøkler forvaltes av eksportøren** eller betrodd enhet i EØS/likeverdig jurisdiksjon [K38 s. 23–24]. Har importøren nøkkelen, er kryptering ikke effektivt mot utleveringsbegjæringer [K14 s. 8].* | |
| Annet | ☐ | | | |

**Organisatoriske tiltak**

| Tiltak | ☐ | Beskrivelse |
|---|---|---|
| Dokumentasjon av innsynsbegjæringer (mottatt, svar, begrunnelse, aktører) | ☐ | |
| Dataminimering og need-to-know-tilgang, revisjoner, disiplinærtiltak | ☐ | |
| Involvering av PVO ved alle begjæringer | ☐ | |
| Sikkerhets- og personvernstandarder/sertifisering | ☐ | |
| Interne retningslinjer for behandling av begjæringer | ☐ | |
| Ansvarsfordeling, egne team, opplæring | ☐ | |
| Annet | ☐ | |

**Kontraktuelle tiltak**

| Tiltak | ☐ | Avtalereferanse |
|---|---|---|
| Supplerende tekniske/organisatoriske tiltak gjort bindende | ☐ | |
| Åpenhetsplikt: liste lover, praksis, tiltak, begjæringer; opplyse om rettslige hindringer | ☐ | |
| Forbud mot bakdører | ☐ | |
| Revisjonsrett | ☐ | |
| Varsling av eksportør (og registrerte) ved myndighetstilgang | ☐ | |
| Plikt til å vurdere lovlighet og bestride begjæringer; søke midlertidig forføyning | ☐ | |
| Minimumsutlevering ved pålegg | ☐ | |
| Plikt til å informere om manglende evne til å overholde avtalen | ☐ | |
| Klartekst bare med eksportørens samtykke | ☐ | |
| Sanksjoner/erstatning til registrerte ved brudd | ☐ | |
| Oppsigelse ved brudd; retur/sletting med bevis | ☐ | |
| Annet | ☐ | |

*[K38 s. 24–25; K14 s. 8]*

**Konklusjon 4A:** ☐ Verktøy + eksisterende tiltak er effektivt → steg 6 ☐ Ikke effektivt → E2

### E2 (4B). Nye supplerende tiltak

| Type | Tiltak | Hvem gjennomfører | Samsvar med EDPB | Risikoer som reduseres |
|---|---|---|---|---|
| Teknisk | | | | |
| Organisatorisk | | | | |
| Kontraktuelt | | | | |

**Konklusjon 4B:** ☐ Effektivt → steg 5 ☐ Ikke effektivt → **overføringen gjennomføres ikke / avsluttes**; importøren sletter alle data og beviser det, eller returnerer alle data og sletter kopier [K38 s. 26; K14 s. 8].

---

## DEL F – Steg 5: Implementering (handlingsplan)

| Handling | Beskrivelse | Kostnad (dagsverk, valgfritt) | Ansvarlig (jurist, teknisk, fag) | Frist | Status |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

*Prosessuelle steg: endres SCC slik at rettigheter/plikter begrenses, eller tiltakene motsier SCC, kreves godkjenning fra tilsynsmyndigheten [K38 s. 27 fn. 56]. Tiltak må tas inn i SCC/avtalen [K14 s. 4].*

### Uttalelser og godkjenning

| Rolle | Uttalelse | Dato | Signatur |
|---|---|---|---|
| Personvernombud / personvernansvarlig | | | |
| Informasjonssikkerhetsansvarlig (CISO) | | | |
| Ansvarlig for overføringen (godkjenning etter interne regler) | | | |

*Legg ved juridiske/tekniske notater fra rådgivere [K38 s. 22, 27].*

---

## DEL G – Steg 6: Revurdering

| Felt | Utfylling |
|---|---|
| Intervall mellom gjennomganger | *F.eks. hvert 2. år; fastsatt etter land og risiko [K38 s. 28].* |
| Dato for neste gjennomgang | |
| Hendelser som utløser tidligere gjennomgang | ☐ Endret lov/praksis i mottakerlandet ☐ Endret/opphevet adekvansbeslutning (f.eks. DPF, Brasil) ☐ Importør varsler at den ikke kan overholde avtalen ☐ Ny underleverandør/videreoverføring ☐ Endret dataformat/kategorier ☐ Mottatt myndighetsbegjæring ☐ Annet |
| Ansvarlig for overvåking av lovendringer | |

*Tidligere lovlig overføring som blir ulovlig ved endrede forhold må stanses, og data tilbakeføres eller slettes [K14 s. 8].*

---

## Vedlegg – Kontrolliste før signering/oppstart

- [ ] Overføring bekreftet (A1) og TIA-behov avklart (A2), med verifisert adekvansstatus og dato.
- [ ] Hele kjeden inkl. videreoverføringer kartlagt (A4).
- [ ] Behandlingsgrunnlag, minimering, informasjon og protokoll i orden (A5).
- [ ] Steg 1–3 utfylt med kilder som oppfyller kildekravene.
- [ ] Konklusjon (3) – hvis brukt – er grundig dokumentert.
- [ ] Tekniske tiltak oppfyller alle EDPB-kontrollpunkter; nøkler/koblingsnøkkel hos eksportør.
- [ ] Tiltak tatt inn i SCC/DPA uten å motsi SCC.
- [ ] PVO og CISO har uttalt seg; godkjenning signert.
- [ ] Revurderingsdato satt.

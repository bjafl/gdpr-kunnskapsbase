---
id: M01
tittel: "Sjekkliste for gjennomgang av databehandleravtale (DPA)"
gdpr_artikler: [28, 29, 32, 33, 34, 35, 36, 44, 46]
kilder: [K01, K03, K04, K05, K07, K10, K11, K13, K14, K24, K30, K33, K39]
---

# M01 – Sjekkliste for gjennomgang av databehandleravtale (DPA)

*Bruk: Kopier malen inn i et arbeidsdokument og fyll ut én tabellrad per krav. Status: **OK** / **Mangler** / **Uklart** / **I.R.** (ikke relevant – begrunn). Kolonnen «Lov/anbefaling» viser om kravet følger av GDPR (L) eller er anbefalt (A) av Datatilsynet eller andre kilder. Fremgangsmåten er beskrevet i [A01](../arbeidsflyter/A01-gjennomga-databehandleravtale.md); bakgrunn i [T07](../temaer/T07-databehandleravtale-art28.md) og [T01](../temaer/T01-roller-behandlingsansvarlig-databehandler.md).*

*Prinsipp: «Jo mer omfangsrik, inngripende eller risikofylt behandlingen er, jo mer konkret må avtalen være» [K05 s. 1]. Ved høy risiko bør A-punkter behandles som krav.*

*Formuleringsforslagene merket «[K05]» er Datatilsynets eksempelformuleringer [K05 s. 4–6]. Øvrige forslag er **[Merknad – ikke fra kildene]** og må tilpasses og kvalitetssikres juridisk.*

---

## Del 0 – Metadata

| Felt | Utfylling |
|---|---|
| Behandlingsansvarlig (kunde) | |
| Leverandør (databehandler) | *Juridisk navn, org.nr., land* |
| Tjeneste / system | |
| Dokumenter gjennomgått | *DPA (versjon/dato), hovedavtale, vilkår, sikkerhetsvedlegg, underdatabehandlerliste, SCC/TIA, sertifikater* |
| Avtaletype | *Egen / leverandørens standard / dansk standard-DPA / EU-kommisjonens standardavtale (2021/915) / SCC modul 2–3* [K05 s. 4; K14 s. 4] |
| Risikonivå for behandlingen | *Lav / middels / høy – begrunn (særlige kategorier, volum, barn, ny teknologi, tredjeland)* |
| DPIA gjennomført? | *Ja / nei / ikke påkrevd – ref.* → [T10](../temaer/T10-dpia-art35-36.md) |
| Gjennomgått av / dato | |

---

## Del 1 – Forutsetninger (før avtaleteksten)

| # | Krav | Hjemmel | L/A | Hva man ser etter | Typiske avvik / røde flagg | Forslag | Status | Kommentar |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Rollen er avklart: leverandøren behandler på vegne av kunden | Art. 4 nr. 8, 28 | L | Hvem bestemmer formål og vesentlige midler (hvilke data, lagringstid, tilgang)? Bruker leverandøren data til egne formål? [K01 s. 4–6] | Leverandøren er reelt selvstendig eller felles behandlingsansvarlig for deler (telemetri, produktforbedring, reklame, KI-trening) [K39 s. 20, 22] | Bryt ned per behandling; egne formål reguleres separat eller forbys; ev. art. 26-ordning | | |
| 1.2 | Tilstrekkelige garantier vurdert | Art. 28 nr. 1 | L | Kompetanse, dybdekunnskap, pålitelighet, ressurser; sertifisering/atferdsnorm; sikkerhetsdokumentasjon [K05 s. 3; K33 ark 14] | Ingen dokumentasjon; ISO-sertifikat med annet scope enn tjenesten [K33 ark 14] | Be om sertifikat + scope, sikkerhetspolicy, revisjonsrapport | | |
| 1.3 | Skriftlig, bindende avtale (kan være elektronisk) | Art. 28 nr. 3, 9 | L | Signert/akseptert; rangordning mot hovedavtale | DPA «kan endres ensidig av leverandøren» | Endringer krever skriftlig enighet eller varsel med oppsigelsesrett | | |
| 1.4 | Standardavtale: vedleggene utfylt | – | L/A | Instruks, behandlingsbeskrivelse, sikkerhet, underdatabehandlere [K05 s. 4] | Tomme eller generiske vedlegg | Fyll ut konkret | | |

---

## Del 2 – Beskrivelse av behandlingen (art. 28 nr. 3 første ledd)

| # | Krav | Hjemmel | L/A | Hva man ser etter | Typiske avvik / røde flagg | Forslag | Status | Kommentar |
|---|---|---|---|---|---|---|---|---|
| 2.1 | Tema (hva oppdraget går ut på) | Art. 28 nr. 3 | L | Konkret tjenestebeskrivelse [K05 s. 4] | «Levering av tjenestene» uten mer | [K05]: «Behandlingen … består i å stille system X til rådighet, samt å utføre nødvendig vedlikehold av systemet.» | | |
| 2.2 | Behandlingens art og formål | Art. 28 nr. 3 | L | Klart angitte formål; ett avsnitt per formål [K05 s. 4] | «Alle formål nødvendige for å levere og forbedre tjenesten» | Konkrete formål som speiler protokollen [K03] | | |
| 2.3 | Varighet | Art. 28 nr. 3 | L | Periode eller «til oppsigelse» [K05 s. 4] | Mangler | «Behandlingen varer inntil avtalen sies opp av en av partene.» [K05] | | |
| 2.4 | Kategorier registrerte | Art. 28 nr. 3 | L | Ansatte, kunder, pasienter, barn … [K05 s. 4] | «Alle personer kunden laster opp» | List kategoriene | | |
| 2.5 | Typer personopplysninger, inkl. særlige kategorier | Art. 28 nr. 3 | L | Konkrete opplysninger [K05 s. 4] | Særlige kategorier ikke nevnt, men forekommer | List; marker art. 9/10-data | | |
| 2.6 | Lagringstid og operasjoner | – | A | Hvilke data leverandøren får, hvilke operasjoner, lagringstid [K30 kap. 34.2] | Leverandøren bestemmer lagringstid selv | Lagringstid fastsatt av kunden | | |

---

## Del 3 – Den behandlingsansvarliges plikter og rettigheter

| # | Krav | Hjemmel | L/A | Hva man ser etter | Typiske avvik / røde flagg | Forslag | Status | Kommentar |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Kunden er ansvarlig for etterlevelse og bestemmer formål og midler | Art. 24, 4 nr. 7 | L (DT) | Uttrykkelig [K05 s. 4] | Leverandøren «bestemmer hvordan tjenesten behandler data» | «Den behandlingsansvarlige har rett og plikt til å bestemme formålet med behandlingen og hvilke hjelpemidler som skal brukes.» | | |
| 3.2 | Dokumenterte instrukser i avtalen eller vedlegg | Art. 28 nr. 3 a | L | Instruksvedlegg [K05 s. 4] | «I samsvar med leverandørens personvernerklæring» | Eget instruksvedlegg | | |
| 3.3 | Oppsigelsesrett hvis leverandøren ikke lenger oppfyller art. 28 nr. 1 | Art. 28 nr. 1 | L (DT-tolkning) | [K05 s. 4] | Ingen oppsigelsesrett / bindingstid uten unntak | Rett til oppsigelse med umiddelbar virkning ved vesentlig brudd på personvernforpliktelser | | |
| 3.4 | Vederlag for bistand/revisjon | – | A | Rimelige, forhåndsavtalte kostnader [K05 s. 4] | Uforholdsmessige gebyrer som hindrer revisjon/bistand | Bistand som følge av leverandørens brudd er kostnadsfri | | |

---

## Del 4 – Databehandlerens forpliktelser (art. 28 nr. 3 a–h)

| # | Krav | Hjemmel | L/A | Hva man ser etter | Typiske avvik / røde flagg | Forslag | Status | Kommentar |
|---|---|---|---|---|---|---|---|---|
| 4.a1 | Bare behandle etter dokumenterte instrukser | Art. 28 nr. 3 a, art. 29 | L | Uttrykkelig [K05 s. 5] | «Med mindre annet følger av leverandørens forretningsbehov» | «Databehandleren skal kun behandle personopplysninger etter dokumenterte instrukser fra den behandlingsansvarlige.» | | |
| 4.a2 | Instruksen omfatter overføring til tredjeland | Art. 28 nr. 3 a | L | Hvilke land, grunnlag, underdatabehandlere [K14 s. 9–10] | Taushet om overføring; «data kan behandles hvor som helst leverandøren eller underleverandører opererer» | Overføring bare til listede land/mottakere med angitt grunnlag | | |
| 4.a3 | Unntak for lovpålagt behandling – med forhåndsvarsel | Art. 28 nr. 3 a | L | Unntaket gjelder EU-/EØS-rett eller nasjonal rett [K05 s. 5; K14 s. 9–10] | Vagt forbehold om utlevering etter «gjeldende lov» (inkl. tredjelands lov) – **rødt flagg** [K14 s. 9–10] | Begrens til EØS-rett; plikt til å varsle, utfordre begjæringer og gi minst mulig [K14 s. 8] | | |
| 4.a4 | Omgående varsel om instruks i strid med personvernregler | Art. 28 nr. 3 siste ledd | L | [K05 s. 5] | Mangler | «Databehandleren skal omgående underrette den behandlingsansvarlige dersom den mener at en instruks er i strid med personvernregelverket.» | | |
| 4.a5 | Ingen bruk til egne formål | Art. 28 nr. 10, 29 | L/A | Forbud mot egne formål (analyse, produktutvikling, KI-trening, markedsføring) [K01 s. 3, 6; K39 s. 19–20] | «Aggregerte/anonymiserte data kan brukes til å forbedre tjenesten»; uklar anonymisering | Forbud; ev. særskilt avtale etter forenlighetsvurdering [K39 s. 53] | | |
| 4.b1 | Fortrolighet/taushetsplikt for autoriserte | Art. 28 nr. 3 b | L | [K05 s. 5] | Bare egne ansatte omfattes, ikke innleide | Gjelder alle med tilgang, også innleide og underleverandører | | |
| 4.b2 | Påvisbar på anmodning; gjelder etter opphør | Art. 28 nr. 3 b, h | L | [K05 s. 5] | Ingen etterfølgende virkning | «Plikten til konfidensialitet gjelder også etter at oppdraget er fullført.» | | |
| 4.b3 | Kun nødvendige autorisasjoner; tilgang fratas | Art. 32 | A | [K05 s. 5] | Bred administratortilgang | Tjenstlig behov, minste privilegium, periodisk gjennomgang | | |
| 4.c1 | Alle tiltak etter art. 32 | Art. 28 nr. 3 c | L | [K05 s. 5] | Bare «bransjestandard sikkerhet» | Henvis til art. 32 + sikkerhetsvedlegg | | |
| 4.c2 | Sikkerhetsvedlegg med minimumskrav | Art. 32 | A | Kryptering (lagring/overføring), pseudonymisering, logging, tilgangskontroll, autentisering, backup, fysisk sikring [K05 s. 5; K33 ark 14; K10] | Ingen konkrete tiltak; leverandøren kan redusere sikkerhetsnivå ensidig | Konkret vedlegg; endringer ikke til lavere nivå → [M09](M09-sikkerhetstiltak-sjekkliste.md) | | |
| 4.c3 | Nøkkelhåndtering | Art. 32 | A | Hvem har krypteringsnøkler? [K33 ark 22; K14 s. 8] | Leverandøren styrer nøkler alene ved høy risiko/tredjelandseksponering | Kundekontrollerte nøkler der risiko tilsier | | |
| 4.c4 | Logging og tilgang til logger | Art. 32 | A | Loggingsplikt, 6–12 mnd. rullerende [K33 ark 16] | Ingen logger tilgjengelig for kunden | Plikt til logging og utlevering av relevante logger ved hendelser | | |
| 4.c5 | Fjernvedlikehold kontrollert | Art. 32 | A | Tilgang ved behov, avgrenset, logget [K33 ark 15] | Permanent fjerntilgang | Tidsbegrenset, godkjent tilgang | | |
| 4.c6 | Ingen tilgang for egne formål «av sikkerhets- eller lovhensyn» uten kundens tillatelse | Art. 28, 29 | A | [K33 ark 22] | Vid tilgangsrett for leverandøren | Tilgang kun etter instruks | | |
| 4.d1 | Forhåndsgodkjenning – valgt modell angitt | Art. 28 nr. 2, 3 d | L | Særlig / generell / forbud [K05 s. 5] | Uklart hvilken modell | Velg en av [K05]-formuleringene (se under) | | |
| 4.d2 | Liste over godkjente underdatabehandlere | Art. 28 nr. 2 | L | Navn, tjeneste, **lagrings- og tilgangsland**, overføringsgrunnlag [K05 s. 5; K30 kap. 34.3] | Bare lenke til nettside som endres uten varsel; land mangler | Vedlegg med fullstendig liste | | |
| 4.d3 | Varsling av endringer + innsigelsesrett (ved generell godkjenning) | Art. 28 nr. 2 | L | Frist i uker for varsel og innsigelse [K05 s. 5] | Varsel kun ved oppdatert nettside; ingen reell konsekvens av innsigelse | E-postvarsel min. X uker før; ved innsigelse rett til å si opp uten kostnad | | |
| 4.d4 | Samme forpliktelser videreført skriftlig | Art. 28 nr. 4 | L | [K05 s. 5; K01 s. 9] | «Vesentlig tilsvarende» / «ikke mindre beskyttende i det vesentlige» uten instruks/revisjon | Samme forpliktelser, aldri dårligere beskyttelse [K01 s. 9] | | |
| 4.d5 | Fullt ansvar for underdatabehandlere | Art. 28 nr. 4 | L/A | [K05 s. 5; K01 s. 9] | Ansvar fraskrevet | «Databehandleren har fullt ansvar overfor den behandlingsansvarlige for underdatabehandlerens oppfyllelse.» | | |
| 4.d6 | Hele kjeden («russiske dukker») | Art. 28 nr. 4 | A | Underleverandørers underleverandører [K33 ark 14; K39 s. 53] | Ukjent kjede | Krav om innsyn i hele kjeden | | |
| 4.e1 | Bistand med rettighetsforespørsler | Art. 28 nr. 3 e | L | [K05 s. 5] | «Kunden må selv bruke selvbetjeningsverktøyene» uten bistand ellers | Bistand så langt mulig, med egnede tiltak | | |
| 4.e2 | Konkret bistand og frister | – | A | F.eks. videresende slettekrav innen 5 dager; samle data ved innsyn [K05 s. 5; K07] | Ingen frist; fristen gjør én-månedsfristen umulig | [K05]: «Ved innsynskrav må databehandler bistå ved å samle opplysningene som er lagret om den registrerte …» | | |
| 4.f1 | Bistand med art. 32–36 | Art. 28 nr. 3 f | L | Sikkerhet, avvik, varsling registrerte, DPIA, forhåndsdrøfting [K05 s. 5–6] | Bare sikkerhet nevnt | Uttrykkelig bistand med alle relevante artikler | | |
| 4.f2 | Varsling ved brudd – frist og innhold | Art. 33 nr. 2–3 | L | «Straks» / uten ugrunnet opphold; innhold etter art. 33 nr. 3 [K05 s. 5–6; K39 s. 36] | «Commercially reasonable time»; varsel bare ved «bekreftet» brudd; ingen innholdskrav | Konkret frist i timer etter kjennskap (også ved mistanke), løpende oppdatering, innhold art. 33 nr. 3 a–d **[Merknad]** | | |
| 4.f3 | Bistand ved DPIA/forhåndsdrøfting – hva forventes | Art. 35–36 | A | [K05 s. 6; K24 s. 14–15] | Mangler | Plikt til å gi nødvendig informasjon og vurdere tiltak | | |
| 4.g1 | Sletting eller tilbakelevering – valgt alternativ angitt | Art. 28 nr. 3 g | L | [K05 s. 6] | «Leverandøren sletter i henhold til egne rutiner» | [K05]: «Databehandleren er forpliktet til å tilbakelevere alle personopplysninger … og deretter slette egne kopier.» eller «… forpliktet til å slette alle personopplysninger …» | | |
| 4.g2 | Påvise sletting | Art. 28 nr. 3 g, h | L | Dokumentasjon/inspeksjon [K05 s. 6] | Ingen bekreftelse | Skriftlig slettebekreftelse innen X dager | | |
| 4.g3 | Hvordan og når – inkl. backup og underdatabehandlere | – | A | [K05 s. 6; K13 s. 5] | Backup beholdes ubegrenset | Frist for sletting i produksjon og backup; sikker sletting [K33 ark 15] | | |
| 4.g4 | Format for tilbakelevering (reversibilitet) | – | A | [K30 kap. 34.2] | Kun proprietært format | Strukturert, maskinlesbart format | | |
| 4.h1 | Gjøre tilgjengelig all nødvendig informasjon | Art. 28 nr. 3 h | L | [K05 s. 6] | «Etter leverandørens skjønn» | Plikt til å gi informasjon på anmodning | | |
| 4.h2 | Revisjon og inspeksjon (også ved tredjepart med fullmakt) | Art. 28 nr. 3 h | L | [K05 s. 6; K33 ark 14] | Kun sertifikater/rapporter; revisjon utelukket; urimelige vilkår | Tredjepartsrapporter som første trinn, men rett til revisjon/inspeksjon når nødvendig **[Merknad]** | | |
| 4.h3 | Tilsynsprosedyre og frekvens | – | A | Vedlegg med prosedyre [K05 s. 6] | Ingen | [K05]: «Den behandlingsansvarlige … gjennomfører (tidsangivelse) et fysisk tilsyn hos databehandler … Utover det planlagte tilsynet kan den behandlingsansvarlige gjennomføre tilsyn etter behov.» | | |

**Formuleringsalternativer for underdatabehandlere [K05 s. 5] (velg én):**
- «Databehandleren skal bare bruke annen databehandler etter forutgående særlig skriftlig godkjennelse. Den behandlingsansvarlige skal motta anmodningen om bruk av ny databehandler senest innen (antall uker) før endringen eventuelt trer i kraft.»
- «Databehandleren har den behandlingsansvarliges generelle godkjennelse til å bruke andre databehandlere. Databehandleren må likevel underrette den behandlingsansvarlige ved eventuelle planer om å skifte ut eller bruke nye databehandlere. Den behandlingsansvarlige må motta en slik underretning minimum (antall uker) før endringen trer i kraft. Den behandlingsansvarlige skal ha mulighet til å motsette seg endringene, og skal meddele databehandleren om dette senest (antall uker) etter underretningen er mottatt.»
- «Databehandleren kan ikke bruke andre databehandlere.»

---

## Del 5 – Overføring ut av EØS

*Detaljert vurdering: [T11](../temaer/T11-overforing-tredjeland-og-tia.md), [A04](../arbeidsflyter/A04-overforing-og-tia.md), [M06](M06-tia-mal.md).*

| # | Krav | Hjemmel | L/A | Hva man ser etter | Typiske avvik / røde flagg | Forslag | Status | Kommentar |
|---|---|---|---|---|---|---|---|---|
| 5.1 | Alle overføringer kartlagt – også fjerntilgang/support, underdatabehandlere, onward transfers | Art. 44 | L | [K14 s. 7] | «Follow-the-sun»-support ikke nevnt | Liste over land for lagring og tilgang | | |
| 5.2 | Overføringsgrunnlag angitt per mottaker | Art. 45–49 | L | Adekvans / SCC (modul) / BCR / art. 49 [K14] | Grunnlag mangler; art. 49 brukt for løpende overføring | Angi grunnlag; SCC vedlagt | | |
| 5.3 | TIA og supplerende tiltak der SCC/BCR brukes | Art. 46 (Schrems II) | L | [K14 s. 7–8] | Ingen vurdering | Gjennomfør TIA [M06](M06-tia-mal.md) | | |
| 5.4 | EØS-leverandør underlagt tredjelands lov | Art. 28 nr. 1, 48 | L | Forbehold om utlevering til myndigheter [K14 s. 9–10] | Vage og vide forbehold – typisk holdepunkt for tiltak | Kryptering med kundens nøkler, pseudonymisering, kontraktsforpliktelser; ellers ikke bruk [K14 s. 9–10] | | |

---

## Del 6 – Tilleggskrav (særlig ved høy risiko, sky og apper)

| # | Krav | Kilde | L/A | Status | Kommentar |
|---|---|---|---|---|---|
| 6.1 | Logisk separasjon fra andre kunder (sky) | [K30 kap. 34.3] | A | | |
| 6.2 | Forhåndsvarsling/godkjenning av endringer med personvernbetydning | [K39 s. 37, 63] | A | | |
| 6.3 | Databehandlerens protokoll (art. 30 nr. 2) – utdrag på anmodning | [K04; K11] | L/A | | |
| 6.4 | Kontaktpunkt for personvern hos begge | [K39 s. 33] | A | | |
| 6.5 | SDK: dokumentasjon av lese-/skriveoperasjoner, samtykkeblokkering, rettighets-API, fjerndeaktivering | [K39 s. 53–54, 64–67] | A | | |
| 6.6 | Utvikler: akseptansetest, sikkerhetskrav (TLS, MASVS L1), oppdateringsplikt ved sårbarhet | [K39 s. 33, 36, 55] | A | | |
| 6.7 | Innebygd personvern og varsling om «state of the art» | [K13 s. 2, 4] | A | | |
| 6.8 | Etterlevelse som vesentlig/bindende vilkår | [K30 kap. 34.2] | A | | |
| 6.9 | Ansvarsbegrensning uthuler ikke personvernpliktene | **[Merknad]** | A | | |

---

## Del 7 – Oppsummering

| Felt | Utfylling |
|---|---|
| Antall OK / Mangler / Uklart | |
| Kritiske funn (må rettes før signering) | *Typisk: rolle feil, ingen instruks, egne formål, uregulerte overføringer, ingen sletting/revisjon* |
| Vesentlige funn (bør forhandles) | |
| Mindre funn | |
| Anbefaling | *Signere / signere med endringer / ikke signere / eskalere* |
| Oppfølging etter signering | *Revisjonsplan, protokolloppdatering, DPA-register* [K11; K39 s. 36] |

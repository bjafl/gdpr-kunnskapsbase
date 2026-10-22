# Kjente motstrider, hull og utdaterte punkter

Listen er samlet under oppbyggingen av basen. Sjekk den før du gir et bastant svar på punktene under. Løsningen følger kildehierarkiet i [_KONVENSJONER.md](_KONVENSJONER.md): GDPR går foran EDPB/WP29, deretter Datatilsynet, andre tilsyn og til sist metodeverk.

## Utdaterte eller erstattede kilder

| Kilde | Status | Konsekvens |
|---|---|---|
| [K25](kilder/K25-wp259-samtykke.md) WP259 (samtykke) | Erstattet av EDPB Guidelines 05/2020, som i hovedsak er likt, men presiserer cookie walls og scrolling | Bruk K25, men nevn 05/2020 |
| [K27](kilder/K27-wp244-ledende-tilsynsmyndighet.md) WP244 (ledende tilsyn) | Erstattet av EDPB Guidelines 8/2022, som snur standpunktet om felles hovedvirksomhet for felles behandlingsansvarlige | Legg 8/2022 til grunn ([T14](temaer/T14-tilsynsmyndighet-og-one-stop-shop.md)) |
| [K28](kilder/K28-cnil-pia-metode.md) CNIL PIA-metode | Utgaven er fra 2015 og bygger på direktiv 95/46. Skalaene er hentet fra K30 | Bruk metodelogikken, men GDPR-krav fra [T10](temaer/T10-dpia-art35-36.md) |
| [K35](kilder/K35-cnil-referentiel-audit.md), [K36](kilder/K36-cnil-referentiel-digital-safe.md) | Bygger på direktiv 95/46. CNILs merkeordning er avviklet | Bare som inspirasjon til sjekklister |
| [K37](kilder/K37-sdm-standard-datavernmodell.md) SDM v1.0 | Nyere versjoner (v2/v3) har en katalog over referansetiltak | Mangler sannsynlighetsskala og tiltakskatalog |
| [K10](kilder/K10-dt-kryptering.md) Kryptering (2017) | Tekniske detaljer er utdatert, for eksempel «TLS 1.3 i draft» | Bruk K33 (2024) for tekniske krav |
| [K14](kilder/K14-dt-overforing-utenfor-eos.md) Overføring | Listen over adekvate land og DPF-status endrer seg | **Verifiser alltid** status på vurderingsdatoen |

## Motstrid mellom kilder

| Tema | Motstrid | Håndtering |
|---|---|---|
| Brasil og adekvans | K14 lister Brasil som adekvat (s. 2), men eksemplet på s. 3 behandler Brasil som ikke-adekvat | Verifiser hos Europakommisjonen og Datatilsynet ([T11](temaer/T11-overforing-tredjeland-og-tia.md)) |
| Restrisiko | ULD ([K40](kilder/K40-dpia-prosess-uld.md)) godtar ingen restrisiko. WP248, CNIL og Datatilsynet lar høy restrisiko utløse forhåndsdrøfting (art. 36). Digdir lar ledelsen akseptere restrisiko innenfor kriterier | WP248 legges til grunn ([T10](temaer/T10-dpia-art35-36.md)) |
| Risikoskalaer | Digdirs retningslinje ([K18](kilder/K18-digdir-retningslinje-risiko.md)) har 5 nivåer, Digdirs verktøy ([K19](kilder/K19-digdir-risikovurderingsverktoy.md)) 4 og CNIL 4×4. Brukerveiledningen til K19 motsier sin egen matrise i én celle. Nivånavnene varierer mellom K30 og K33 | [T09](temaer/T09-risikovurdering-metoder-og-skalaer.md) viser skalaene side om side. [M03](maler/M03-risikovurdering-mal.md) anbefaler Digdirs 5-nivåskala |
| Matriselogikk | Digdirs matrise gir «Moderat» både for svært høy konsekvens med lav sannsynlighet og omvendt. CNIL godtar høy alvorlighet bare når sannsynligheten er ubetydelig | M03 har et eget GDPR-gulv i akseptkriteriene |
| Kunnskapsstyrke | K17 bruker svak/middels/sterk, K18 lav/moderat/høy | Samme begrep |
| Beskyttelsesmål | SDM ([K37](kilder/K37-sdm-standard-datavernmodell.md)) har 7 mål, ULD ([K40](kilder/K40-dpia-prosess-uld.md)) har 6 (uten dataminimering) | Bruk 7 |
| DPIA-kriterier | [K20](kilder/K20-dt-dpia-liste.md) dekker bare 8 av WP248s 9 kriterier | Bruk alle 9 fra [K24](kilder/K24-wp248-dpia.md) |
| Forhåndsdrøfting | [K21](kilder/K21-dt-sjekkliste-dpia-faser.md) knytter det til at saken er «behandlet i ledergruppen mer enn én gang». Art. 36 krever bare høy restrisiko som ikke er redusert | Art. 36 gjelder. K21 er en praktisk operasjonalisering |
| Passord | [K30](kilder/K30-cnil-pia-kunnskapsbaser.md) anbefaler periodisk bytte og sperring etter 5 forsøk. [K33](kilder/K33-cnil-sikkerhetsguide.md) (nyere) sier nei til periodisk bytte og knytter sperregrensen til passordstyrken | K33 gjelder |
| Lagringstid for logger | K33: 6–12 måneder. K30: 6 måneder | K33 gjelder |
| Kryptografi | K10: RSA 3072. K33: RSA på minst 2048. K30 nevner WPA/WPA2, K32/K33 krever WPA2/WPA3 | Nyeste kilde gjelder. Sjekk gjerne NSM og ANSSI |
| Bøteramme | [K34](kilder/K34-cnil-cybersikkerhet-2024.md) oppgir 20 mill./4 %, men brudd på art. 32–34 har taket 10 mill./2 % (art. 83 nr. 4) | Art. 83 gjelder |
| Varslingsfrist fra databehandler | K05: «straks». K33: «så snart som mulig». K30: «umiddelbar». K39: «innen 72-timersvinduet». GDPR art. 33 nr. 2: «uten ugrunnet opphold» | Avtal en konkret frist i DPA-en, for eksempel 24–48 timer ([M01](maler/M01-databehandleravtale-sjekkliste.md)) |
| Ansvar for underdatabehandler | K05 kaller fullt ansvar en anbefaling. K01 sier at det følger av art. 28 nr. 4 | Art. 28 nr. 4 gjelder ([T07](temaer/T07-databehandleravtale-art28.md)) |
| Oppsigelsesrett i DPA | K05 krever det, men det står ikke uttrykkelig i art. 28 | Datatilsynets anbefaling |
| Instruks om overføring | K05 nevner ikke at instruksen etter art. 28 nr. 3 a også må dekke overføring til tredjeland | Fylt inn fra K14 i T07/M01 |
| Aldersgrense for barns samtykke | K25 bruker 16 år (GDPR-utgangspunktet), K02 bruker 13 år (Norge) | 13 år i Norge |
| Cookies/ePrivacy i Norge | Merknadene i K25 og K39 beskriver kravet i ekomloven § 3-15 litt ulikt | **Verifiser** gjeldende ordlyd og Nkom-praksis |
| Protokoll for databehandler | Datatilsynets mal ([K11](kilder/K11-art30-protokollmaler.md)) sier at «alle kolonner» er obligatoriske, men art. 30 nr. 2 krever færre. Eksempelet bruker samtykke i rekruttering, noe som er problematisk etter K25 | Art. 30 nr. 2 gjelder |
| Forenlig viderebehandling | [K09](kilder/K09-dt-grunnleggende-prinsipper.md) krever eget behandlingsgrunnlag også ved forenlig viderebehandling, noe som er strengere enn fortalepunkt 50 kan tilsi | Omstridt. Vær forsiktig ([T03](temaer/T03-grunnprinsipper-art5.md)) |

## Hull i kildegrunnlaget

Basen dekker ikke disse temaene med primærkilder. Det som står om dem, er merket **[Merknad – ikke fra kildene]** og bør verifiseres:

- Innholdet i melding om brudd (art. 33 nr. 3) og varsel med unntak (art. 34 nr. 2–3). Verken WP250/EDPB 9/2022 eller Datatilsynets egne avvikssider finnes i kildene.
- Fristene og innsendingskravene ved forhåndsdrøfting (art. 36 nr. 2–3).
- SCC klausul 14–15 i ordlyd, og Datatilsynets meldekanal.
- Personvernombud (art. 37–39), der det bare finnes spredt omtale.
- EDPB-retningslinjer av nyere dato, for eksempel 07/2020 (roller), 01/2022 (innsyn), 1/2024 (berettiget interesse), 2/2023 (teknisk sporing) og 9/2022 (brudd).
- Ordrett lovtekst. GDPR og personopplysningsloven finnes ikke i fulltekst. Slå opp på lovdata.no ved behov for ordlyd.
- Sektorlovgivning, som helseregisterloven, arbeidsmiljøloven kap. 9 og offentleglova.
- Fysisk sikring og personellsikkerhet er svakt dekket hos NSM. Bruk K33 og K30.

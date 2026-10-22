---
id: M07
tittel: "Mal: Avviksskjema – intern logg, vurdering av meldeplikt/varslingsplikt og melding til Datatilsynet"
gdpr_artikler: [4, 28, 32, 33, 34]
kilder: [K15, K34, K33, K30, K32, K05, K10, K06, K12, K28, K39, K27]
---

# Mal: Avviksskjema – intern logg, vurdering av meldeplikt/varslingsplikt og melding til Datatilsynet

> **Bruk av malen.** Del A fylles ut for **alle** sikkerhetshendelser som kan berøre personopplysninger, og utgjør posten i avviksregisteret (art. 33 nr. 5) [K30 kap. 17; K34 s. 1]. Del B er vurderingen av meldeplikt (art. 33) og varslingsplikt (art. 34). Del C samler opplysningene som trengs i meldingen til Datatilsynet. Del D er varselet til de registrerte. Del E er oppfølging. **Fristen er 72 timer fra man ble kjent med bruddet – ikke vent på full oversikt; meld trinnvis** [K15 s. 1; K33 ark 19]. Kursiv er veiledning. Fagstoff: [T12](../temaer/T12-avvik-og-brudd-art33-34.md). Prosess: [A05](../arbeidsflyter/A05-avvikshandtering.md).

---

## DEL A – Hendelsesregistrering (intern logg)

### A1. Identifikasjon og tidslinje

| Felt | Utfylling |
|---|---|
| Avviks-ID | |
| Registrert av / rolle | |
| Hvordan ble hendelsen oppdaget (logg/varsel, ansatt, databehandler, registrert, tredjepart, media) | |
| Tidspunkt hendelsen startet (anslått) | |
| Tidspunkt hendelsen ble oppdaget | |
| Tidspunkt virksomheten ble **kjent med** at personopplysninger er berørt (start på 72-timersfristen) | ***[Merknad – ikke fra kildene]** Normalt når man har rimelig grad av sikkerhet for at en sikkerhetshendelse har kompromittert personopplysninger; begrunn tidspunktet.* |
| 72-timersfrist utløper | |
| Tidspunkt hendelsen ble stoppet/inneholdt | |
| Er hendelsen pågående? | ☐ Ja ☐ Nei |
| Varsel fra databehandler mottatt (tidspunkt, fra hvem) | *Databehandler skal varsle straks [K05].* |
| PVO varslet (tidspunkt) | *Involver PVO tidlig [K15 s. 7].* |

### A2. Beskrivelse av hendelsen

| Felt | Utfylling |
|---|---|
| Hva har skjedd (fakta) | |
| Hendelsestype | ☐ Phishing ☐ Kompromittert konto / credential stuffing ☐ Løsepengevirus ☐ DDoS ☐ Direktørsvindel ☐ Skadevare/innbrudd ☐ Feilsendt e-post/brev ☐ Feil tilgangsstyring / data tilgjengelig via URL ☐ Tap/tyveri av enhet eller dokument ☐ Utilsiktet sletting/ødeleggelse ☐ Feilkonfigurert skytjeneste ☐ Feil hos databehandler ☐ Annet: … *[K15; K34 s. 1–2]* |
| Årsak (kjent/foreløpig/ukjent) | ☐ Ondsinnet ekstern ☐ Ondsinnet intern ☐ Menneskelig feil ☐ Teknisk feil ☐ Ukjent |
| Berørte systemer/tjenester/lokasjoner | |
| Berørte databehandlere/underleverandører | |
| Er data kopiert ut (eksfiltrert)? Kan logging dokumentere det? | ☐ Ja ☐ Nei, dokumentert ved logg ☐ Uklart *Uklart ved løsepengevirus → meld i påvente av avklaring [K15 s. 6].* |

### A3. Bruddtype (kryss alle som gjelder)

| Type | Kryss | Beskrivelse |
|---|---|---|
| Konfidensialitet – uautorisert utlevering/tilgang | ☐ | |
| Integritet – uautorisert/utilsiktet endring | ☐ | |
| Tilgjengelighet – tap/ødeleggelse/utilgjengelighet (også midlertidig) | ☐ | *Tilgjengelighets- og integritetsbrudd er også brudd [K34 s. 1].* |
| Ingen personopplysninger berørt (ren sikkerhetshendelse) | ☐ | *Begrunn; ikke et brudd etter art. 4 nr. 12, men loggfør.* |

### A4. Berørte opplysninger og personer

| Felt | Utfylling |
|---|---|
| Kategorier personopplysninger | ☐ Identifikasjon/kontakt ☐ Fødselsnummer ☐ Påloggingsdata/passord ☐ Økonomi/betalingsdata ☐ Lokasjon ☐ Kommunikasjon/e-post-innhold ☐ HR/personaldata ☐ Annet: … |
| Særlige kategorier (art. 9) / straffedommer (art. 10) | ☐ Helse ☐ Etnisitet ☐ Religion ☐ Politisk oppfatning ☐ Fagforening ☐ Genetiske/biometriske ☐ Seksuelle forhold ☐ Straffedommer ☐ Ingen |
| Kategorier registrerte | ☐ Ansatte ☐ Kunder/brukere ☐ Barn ☐ Pasienter ☐ Elever/studenter ☐ Innbyggere ☐ Andre: … |
| Omtrentlig antall registrerte | *Ved e-postkompromittering: kontoeier + alle personer i e-poster og kontakter + mottakere av e-post sendt fra kontoen – ofte flere hundre [K15 s. 3].* |
| Omtrentlig antall registreringer (poster) | |
| Er opplysningene kryptert/pseudonymisert? Er nøkkelen kompromittert? | *[K10; K30 kap. 17]* |
| Geografisk omfang (registrerte i andre EØS-land?) | |

### A5. Strakstiltak

| Tiltak | Tidspunkt | Ansvarlig |
|---|---|---|
| Stoppe bruddet (isolere, stenge konto, tilbakekalle tilgang, sperre URL) | | |
| Sikre bevis og logger (tidslinje) | | *[K32 4.3.3]* |
| Tilbakekalle/gjenopprette (passordbytte, gjenoppretting fra backup, be mottaker slette feilsendt materiale) | | |
| Krisestab/eksterne hendelseshåndterere aktivert | | *[K15 s. 7]* |
| Kontakt med bank (ved svindel) | | *[K15 s. 3, 5]* |

---

## DEL B – Vurdering av meldeplikt og varslingsplikt

### B1. Risikovurdering for de registrerte

*Vurder alvorlighet og sannsynlighet for konsekvenser for de registrertes rettigheter og friheter – ikke for virksomheten [K33 ark 19]. Bruk CNILs firenivåskala for alvorlighet [K30; K28].*

| Moment | Vurdering |
|---|---|
| Opplysningenes art og sensitivitet | |
| Volum og antall berørte | |
| Hvor lett personene kan identifiseres | |
| Mulige konsekvenser (identitetstyveri, svindel, økonomisk tap, diskriminering, omdømme, tap av taushetsbelagte opplysninger, fysisk skade, psykisk belastning, tap av tilgang til tjenester) | *Fortalepunkt 75 [K12 s. 6].* |
| Varighet/reversibilitet av konsekvensene | |
| Særlige kjennetegn ved de registrerte (barn, sårbare) | |
| Mottakerens art (ukjent/ondsinnet vs. kjent og pålitelig som har bekreftet sletting) | ***[Merknad – ikke fra kildene]** moment fra WP250/EDPB.* |
| Risikoreduserende forhold (kryptering, rask gjenoppretting, logging som viser at intet ble kopiert) | *[K15 s. 6; K10]* |
| Samlet alvorlighet | ☐ 1 Ubetydelig ☐ 2 Begrenset ☐ 3 Betydelig ☐ 4 Maksimal |
| Samlet sannsynlighet for at konsekvensene inntreffer | ☐ 1 Ubetydelig ☐ 2 Begrenset ☐ 3 Betydelig ☐ 4 Maksimal |

### B2. Konklusjon

| Konklusjon | Kryss | Begrunnelse |
|---|---|---|
| **Ingen risiko sannsynlig** – loggføres, meldes ikke | ☐ | |
| **Risiko** – meldes til Datatilsynet innen 72 timer | ☐ | |
| **Høy risiko** – meldes til Datatilsynet **og** varsles til de registrerte uten ugrunnet opphold | ☐ | |
| Uavklart – meldes foreløpig (trinnvis) | ☐ | *[K15 s. 1, 6]* |

**Datatilsynets veiledende utgangspunkt per hendelsestype** [K15]: vellykket phishing og e-postangrep → normalt meld; løsepengevirus med uklart om data er på avveie eller med påvirket tilgjengelighet/integritet → meld; DDoS → bare ved risiko (f.eks. bortfall av betaling, tele, kraft, helse, nødtjenester); direktørsvindel → vurder konkret.

### B3. Unntak fra varsling av de registrerte (art. 34 nr. 3)

| Unntak | Gjelder? | Dokumentasjon |
|---|---|---|
| a) Tekniske/organisatoriske tiltak gjør opplysningene uforståelige for uvedkommende (f.eks. kryptering, nøkkel ikke kompromittert) | ☐ | *[K10; K30 kap. 17]* |
| b) Etterfølgende tiltak sikrer at den høye risikoen sannsynligvis ikke lenger vil oppstå | ☐ | ***[Merknad – ikke fra kildene]*** |
| c) Uforholdsmessig innsats – erstattes av offentlig kunngjøring eller tilsvarende effektiv informasjon | ☐ | ***[Merknad – ikke fra kildene]*** |

### B4. Andre meldinger

| Mottaker | Vurdert | Sendt (tidspunkt) |
|---|---|---|
| Politiet (anmeldelse av datakriminalitet) | ☐ | *Datatilsynet anbefaler anmeldelse [K15 s. 7].* |
| NSM / Nasjonalt cybersikkerhetssenter | ☐ | *[K15 s. 7]* |
| Sektormyndighet / annen lovpålagt meldeplikt | ☐ | *Andre meldeplikter gjelder i tillegg [K33 ark 19]. **[Merknad – ikke fra kildene]** Verifiser sektorregelverk (ekom, NIS, finans, helse).* |
| Behandlingsansvarlig (hvis vi er databehandler) | ☐ | *Straks, med informasjon som i del C [K05].* |
| Felles behandlingsansvarlig | ☐ | *[K39 s. 66–67]* |
| Forsikringsselskap, styre, revisor | ☐ | |

---

## DEL C – Opplysninger til melding til Datatilsynet

*Feltene dekker minimumsinnholdet i art. 33 nr. 3 (**[Merknad – ikke fra kildene]**: ordlyden er ikke gjengitt i kildegrunnlaget; kontroller mot forordningen og Datatilsynets gjeldende meldeskjema). Opplysninger som ikke er kjent ennå, kan ettersendes trinnvis [K15 s. 1; K33 ark 19].*

| # | Felt | Utfylling |
|---|---|---|
| C1 | Type melding | ☐ Foreløpig ☐ Utfyllende/oppfølging (ref. tidligere melding) ☐ Endelig |
| C2 | Behandlingsansvarlig: navn, org.nr., adresse | |
| C3 | Kontaktpunkt: personvernombud eller annen kontaktperson – navn, telefon, e-post (art. 33 nr. 3 b) | |
| C4 | Databehandler(e) involvert | |
| C5 | Tidspunkt for bruddet, oppdagelse og kjennskap | |
| C6 | Hvis meldingen sendes etter 72 timer: årsak til forsinkelsen | ***[Merknad – ikke fra kildene]** art. 33 nr. 1.* |
| C7 | Bruddets art: hva har skjedd, bruddtype (konfidensialitet/integritet/tilgjengelighet), årsak (art. 33 nr. 3 a) | |
| C8 | Kategorier og omtrentlig antall registrerte (art. 33 nr. 3 a) | |
| C9 | Kategorier og omtrentlig antall registreringer (art. 33 nr. 3 a) | |
| C10 | Særlige kategorier / art. 10 / fødselsnummer / barn berørt? | |
| C11 | Sannsynlige konsekvenser for de registrerte (art. 33 nr. 3 c) | *Melding skal beskrive konsekvensene [K30 kap. 17].* |
| C12 | Tiltak truffet eller foreslått for å håndtere bruddet, inkl. tiltak for å redusere skadevirkninger (art. 33 nr. 3 d) | |
| C13 | Er de registrerte varslet? Når, hvordan, med hvilket innhold? Hvis nei: begrunnelse/unntak | |
| C14 | Grenseoverskridende: registrerte i andre EØS-land? Andre tilsynsmyndigheter varslet? | *[K27](../kilder/K27-wp244-ledende-tilsynsmyndighet.md)* |
| C15 | Andre myndigheter varslet (politi, NSM, sektormyndighet) | |
| C16 | Eventuelle tiltak for å forhindre gjentakelse | |

**Innsendt** (kanal, tidspunkt, kvittering/saksnr.): …
*[Merknad – ikke fra kildene] Datatilsynet tar imot meldinger via elektronisk meldeskjema på datatilsynet.no; verifiser gjeldende kanal.*

---

## DEL D – Varsel til de registrerte (ved høy risiko)

*Klart og enkelt språk, kortfattet og lett tilgjengelig; levert slik at mottakeren faktisk får det med seg, adskilt fra annen informasjon (f.eks. markedsføring) [K06]. Minimum: bruddets art, kontaktpunkt og anbefalte tiltak [K30 kap. 17], samt (**[Merknad – ikke fra kildene]** art. 34 nr. 2) sannsynlige konsekvenser og iverksatte tiltak.*

| Felt | Utfylling |
|---|---|
| Kanal (e-post, SMS, brev, innlogget tjeneste, offentlig kunngjøring) | |
| Målgruppe og antall | |
| Tidspunkt sendt | |

**Tekstmal:**

> **Emne: Viktig informasjon om dine personopplysninger**
>
> Den [dato] ble [virksomhet] kjent med at [kort, konkret beskrivelse av hva som har skjedd].
>
> **Hvilke opplysninger om deg som er berørt:** [kategorier].
>
> **Hva dette kan bety for deg:** [sannsynlige konsekvenser, f.eks. risiko for svindelforsøk, phishing, misbruk av identitet].
>
> **Hva vi har gjort:** [stoppet bruddet, sikret systemene, varslet Datatilsynet og politiet, øvrige tiltak].
>
> **Hva vi anbefaler at du gjør:** [konkrete råd, f.eks. bytt passord der du har brukt samme passord, vær oppmerksom på e-post/SMS som ber om opplysninger, kontakt banken, følg med på kontoutskrifter].
>
> **Spørsmål:** Kontakt [kontaktpunkt/personvernombud, telefon, e-post]. Du kan også klage til Datatilsynet.
>
> Vi beklager det inntrufne.

---

## DEL E – Oppfølging og lukking

| Felt | Utfylling |
|---|---|
| Rotårsak (endelig) | *[K32 4.3.6]* |
| Lærdommer («lessons learned») | *[K32 4.4.1]* |
| Forbedringstiltak (sikkerhet, rutiner, opplæring, avtaler) – ansvarlig og frist | |
| Behov for oppdatert risikovurdering (art. 32) eller DPIA? | ☐ Ja ☐ Nei |
| Behov for endring i databehandleravtale/leverandørstyring? | ☐ Ja ☐ Nei |
| Begrunnelse dersom bruddet **ikke** ble meldt eller registrerte **ikke** varslet | *Skal dokumenteres for å kunne vise etterlevelse.* |
| Avvik lukket (dato, av hvem) | |
| Ledelsen orientert (dato) | |

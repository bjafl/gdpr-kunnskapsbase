---
id: K10
tittel: "Kryptering"
utgiver: Datatilsynet
dato: "2012-01-24 (sist endret 2017-03-07)"
spraak: nb
fil: "ressurser/Datatilsynet/Kryptering _ Datatilsynet.pdf"
url: "https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/informasjonssikkerhet-internkontroll/kryptering/"
type: veileder
gdpr_artikler: [5, 32, 34]
emner: [kryptering, informasjonssikkerhet, konfidensialitet, tls, nokkelforvaltning, e-post, fodselsnummer, passord]
relevans: middels
---

# Kryptering (Datatilsynet, 2012)

## Sammendrag
Nettside fra Datatilsynet (2 utskriftssider) om kryptering som tiltak for konfidensialitet. Den forklarer symmetrisk og asymmetrisk kryptering, viser til NSM som riktig myndighet for kryptokrav, og angir tre elementer for god nok sikring: kryptografiske mekanismer (AES 128/256, SHA-2 ≥ 256, RSA 3072), tillit til kryptomodul (Common Criteria / FIPS 140-2) og nøkkelforvaltning (hardware for data at rest, PKI). Virksomheten avgjør selv gjennom risikovurdering om sikringen er god nok. Datatilsynet mener kryptering er nødvendig ved overføring av særlige kategorier, fødselsnummer, opplysninger om mange og opplysninger klassifisert som beskyttelsesverdige. Siden gir råd om HTTPS/TLS, kryptering av enkeltfiler, harddiskkryptering, og en spørsmål-og-svar-del om e-post, passord og fødselsnummer. Publisert 24.01.2012, sist endret 07.03.2017 – de tekniske anbefalingene er delvis utdatert.

## Når skal agenten bruke denne kilden
- Når det skal vurderes om kryptering er nødvendig (f.eks. i DPIA, risikovurdering eller sikkerhetsvedlegg til databehandleravtale).
- Ved spørsmål om sending av fødselsnummer, sensitive opplysninger eller lønnsslipper på e-post.
- Ved spørsmål om passordlagring eller valg av passord for krypterte filer.
- Som utgangspunkt for minimumskrav til algoritmer/nøkler – men kontroller alltid oppdaterte NSM-krav.

## Hovedinnhold

### Grunnbegreper
- Kryptering er en matematisk metode som sørger for konfidensialitet ved at informasjon ikke kan leses av uvedkommende. Informasjonen «låses ned» med en nøkkel og kan ikke leses før den låses opp med riktig nøkkel; nøkkelen for å låse opp trenger ikke være den samme som for å låse ned.
- **Symmetrisk kryptering:** samme nøkkel låser ned og opp; nøkkelen må utveksles sikkert mellom avsender og mottaker.
- **Asymmetrisk kryptering** (offentlig nøkkelkryptering, public key): nøkkelpar – én privat og én offentlig, matematisk relatert. Den offentlige kan distribueres fritt; den private kjennes bare av eieren. Den ene kan ikke utledes av den andre. Validiteten (gyldighet og ekthet) til den offentlige nøkkelen må kontrolleres og administreres.
- Kravet til nøkkellengde er forskjellig for metodene.

### Hvilke krav stiller Datatilsynet?
- Datatilsynet er **ikke** riktig myndighet for kryptering og kan ikke veilede i hvordan man krypterer. Viser til **Nasjonal sikkerhetsmyndighet (NSM)** og deres krav til kryptografi, samt anbefalinger i Sikkerhetsbloggen.

### Hva gir god nok sikring av konfidensialitet? – tre elementer
Det viktigste er å bruke utbredte og anerkjente algoritmer og metoder, med tilstrekkelig nøkkellengde.
1. **Funksjoner – kryptografiske mekanismer:** Som symmetrisk konfidensialitetsbeskyttelse anbefales **AES med 128 eller 256 bits nøkkel**. Som avtrykksalgoritme (hash) anbefales **SHA-2 med minst 256 bits styrke**. For **RSA** anbefales **3072 bits nøkkel**.
2. **Tillit til kryptomodul:** Moduler som genererer, beskytter og bruker private nøkler eller sesjonsnøkler skal evalueres mot **Common Criteria, FIPS 140-2** eller tilsvarende.
3. **Nøkkelforvaltning:** Nøkler kan lages i software (for eget bruk) for datakommunikasjon (data in transit). Nøkler må lages og brukes i **hardware for langtidslagring (data at rest)**. Levetid avhenger av beskyttelsen. Langtidsnøkler skal være **asymmetriske og digitale sertifikater**, og **PKI** skal benyttes for nøkkelforvaltning. Nøkler skal slettes forsvarlig etter bruk.

Mangler eller er ett av elementene svakt, er sikringen ikke god nok.

### Hvem avgjør om sikringen er god nok?
- Virksomheten (behandlingsansvarlig) må selv foreta en **risikovurdering** av innholdet som skal beskyttes. *Eksempel:* En lønnsslipp kan inneholde sensitive opplysninger og krever derfor konfidensialitet.
- Hva som brukes som passord for kryptering og hvordan passord håndteres, må risikovurderes. Passord for dekryptering av lønnsslipp bør f.eks. **ikke** være fødselsnummer eller andre kjennetegn for mottaker.
- Datatilsynet kan gi pålegg om sikring og fastlegge kriterier for akseptabel risiko.

### Hva skal man kryptere?
Datatilsynet mener kryptering er **nødvendig** når informasjonen som overføres er:
1. særlige kategorier av personopplysninger (sensitive)
2. fødselsnummer
3. personopplysninger om mange
4. personopplysninger som behandlingsansvarlig har klassifisert som beskyttelsesverdige

### Når og hvordan skal man kryptere?
**Datakommunikasjon (data in transit)** – overføring mellom to eller flere lokasjoner, f.eks.:
1. mellom virksomhetens egne lokasjoner
2. mellom virksomheten og leverandør (databehandler eller sikkerhetspart)
3. mellom leverandører og underleverandører
4. mellom leverandørers datasentre

**E-post og nettsider:** Mest vanlig med HTTPS. Bruk høyeste versjon av TLS; unngå SSL 3.0 (og lavere) med kjente svakheter. TLS 1.0 er en forbedring av SSL 3.0; TLS 1.2 har også sine problemer avhengig av algoritme og klient; «TLS 1.3 er i draft og kommer snart» (utdatert).

**Kryptering av enkeltfiler:** Kan man ikke kryptere e-posten eller være sikker på at overføringen er kryptert, kan innebygde mekanismer i programvare brukes – f.eks. 7zip, PDF eller nyere MS Office, som støtter AES 256. Nøkkelen må sikres og sendes **separat**; f.eks. SMS eller muntlig over telefon – men dette må risikovurderes og anbefales bare i enkelttilfeller når kommunikasjonen ikke kan krypteres. Utfordringer: manglende kontroll på endepunkter og avlytting.

**Harddiskkryptering:** Sikrer konfidensialitet når maskinen er avslått – data er sikret hvis maskinen mistes/stjeles. Standard i moderne operativsystemer, f.eks. FileVault (macOS), BitLocker (Windows), maskinvarebasert harddiskkrypto fra Intel.

### Spørsmål og svar (s. 2)
- **Hva bør jeg ikke sende på e-post?** E-post er i utgangspunktet ukryptert og går via mange knutepunkter; kan overvåkes/analyseres. Innholdet kan beskyttes med kryptering.
- **Sending og lagring av sensitiv e-post?** Overføring av sensitive opplysninger skal normalt krypteres. Sensitiv e-post må lagres kryptert inntil den hentes inn i den delen av informasjonssystemet som er egnet for behandling av sensitive opplysninger.
- **Passord?** Passord skal beskyttes hos den ansvarlige virksomheten; beskyttelsesgraden må være bedre eller lik beskyttelsesnivået for opplysningene passordet beskytter. Viser til OWASP «Password Storage Cheat Sheet».
- **Fødselsnummer per e-post eller post?** Skal ikke være tilgjengelig for andre enn mottakeren. Per post: lukket konvolutt, ikke synlig i konvoluttvindu eller på utsiden. Datatilsynet anbefaler kryptering ved sending på usikret e-post, men virksomheten må gjøre egne vurderinger for tilfredsstillende sikkerhet.
- **Kan konfidensielle opplysninger sendes ukryptert hvis kunden samtykker?** Virksomheten har plikt til å sikre opplysningene tilstrekkelig, og **samtykke fra kunden gjør ikke at kravene til informasjonssikkerhet kan senkes**. Opplysninger som krever konfidensialitet skal normalt krypteres ved overføring.

### Lenker siden viser til
- Nasjonal sikkerhetsmyndighet (NSM) og Sikkerhetsbloggen
- OWASP «Password Storage Cheat Sheet»
- /rettigheter-og-plikter/virksomhetenes-plikter/informasjonssikkerhet-internkontroll/ (informasjonssikkerhet), undersider om fødselsnummer, «Se flere spørsmål og svar om informasjonssikkerhet»

## Praktiske sjekkpunkter
- Kontroller at overføring av særlige kategorier, fødselsnummer, opplysninger om mange og beskyttelsesverdige opplysninger krypteres.
- Kontroller at kryptering omfatter alle overføringsveier: interne lokasjoner, til/fra leverandør, mellom leverandør og underleverandør, mellom datasentre.
- Kontroller at algoritmer og nøkkellengder er anerkjente og oppdaterte (kilden: AES-128/256, SHA-2 ≥ 256, RSA 3072) – verifiser mot gjeldende NSM-krav.
- Kontroller at kryptomoduler er evaluert (Common Criteria/FIPS 140-2 eller tilsvarende), og at nøkler for data at rest håndteres i hardware med PKI.
- Kontroller TLS-konfigurasjon (ikke SSL 3.0 eller eldre).
- Kontroller at bærbare enheter har full diskkryptering.
- Kontroller at passord for krypterte filer ikke er fødselsnummer e.l., og sendes separat.
- Kontroller at passordlagring gir minst samme beskyttelse som dataene passordet beskytter.
- Avvis at samtykke fra kunden brukes som begrunnelse for å sende ukryptert.
- Ta krav til kryptering inn i sikkerhetsvedlegget i databehandleravtalen ([K05](K05-dt-databehandleravtale.md)).

## Viktige sitater
- «Datatilsynet er ikke riktig myndighet for kryptering og kan ikke veilede i hvordan man krypterer.»
- «Som symmetrisk konfidensialitetsbeskyttelse anbefales AES med 128 eller 256 bits nøkkel.»
- «Dersom et av disse elementene mangler eller er svakt, er ikke sikringen god nok.»
- «Virksomheten (behandlingsansvarlig) må selv foreta en risikovurdering av innholdet den trenger å beskytte.»
- «Passord for dekryptering av lønnsslipp bør for eksempel ikke være fødselsnummer eller andre kjennetegn for mottaker.»
- «… og et samtykke fra kunden gjør ikke at kravene til informasjonssikkerhet kan senkes.»

## Kryssreferanser
- GDPR: art. 5 nr. 1 f (integritet og konfidensialitet), art. 32 nr. 1 a (pseudonymisering og kryptering), art. 34 nr. 3 a (kryptering kan fjerne plikten til å underrette de registrerte om brudd på personopplysningssikkerheten)
- Andre kilder: [K32](K32-nsm-grunnprinsipper.md) – NSMs grunnprinsipper for IKT-sikkerhet; [K16](K16-dfo-veileder-informasjonssikkerhet.md) – informasjonssikkerhet; [K33](K33-cnil-sikkerhetsguide.md) og [K34](K34-cnil-cybersikkerhet-2024.md) – CNILs sikkerhetsråd; [K05](K05-dt-databehandleravtale.md) – sikkerhetsvedlegg.

## Aktualitet og begrensninger
- Publisert 24.01.2012, sist endret 07.03.2017 – eldre enn GDPR; viser ikke til art. 32.
- Tekniske detaljer er delvis utdatert: «TLS 1.3 er i draft» (TLS 1.3 ble standardisert i 2018); FIPS 140-2 er avløst av FIPS 140-3.
- **[Merknad – ikke fra kilden]** Bruk oppdaterte NSM-anbefalinger (f.eks. NSMs kryptografiske anbefalinger) for algoritmevalg; TLS 1.2 med sterke chiffersuiter eller TLS 1.3 er i dag vanlig minimumskrav.

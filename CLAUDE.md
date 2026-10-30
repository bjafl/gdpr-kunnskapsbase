# GDPR-kunnskapsbase: instruks for agenten

Dette repoet er en kunnskapsbase på norsk bokmål om personvernregelverket: GDPR, personopplysningsloven, veiledere og maler. Den skal brukes til å svare på spørsmål og til å lage DPIA, gjennomgå databehandleravtaler, gjøre risikovurderinger og TIA, føre protokoll og håndtere avvik.

**Start alltid med [README.md](README.md).** Den har rutetabellen (spørsmål → fil) og reglene for svar. Formatet for hver filtype står i [_KONVENSJONER.md](_KONVENSJONER.md).

## Kildene i kortform

| Hva | Hvor | Bruk |
|---|---|---|
| **Lovtekst (fasit)** | [kilder/K43-gdpr.md](kilder/K43-gdpr.md) (GDPR, oversikt: artikkel → fil) og [kilder/K42-personopplysningsloven.md](kilder/K42-personopplysningsloven.md). Cookies: [kilder/K44-ekomloven-3-15.md](kilder/K44-ekomloven-3-15.md) |
| Lovtekst, engelsk | [kilder/K45-gdpr-en.md](kilder/K45-gdpr-en.md): offisiell engelsk GDPR, samme ankre som K43 | Engelskspråklige kilder (EDPB, CNIL), engelske sitater. Norsk tekst er fasit for norske svar | Ordlyd, vilkår, frister, definisjoner |
| Temaer `T01–T15` | `temaer/` | Syntese og kjerneregler. Start her ved spørsmål |
| Arbeidsflyter `A01–A06` | `arbeidsflyter/` | Steg for steg når noe skal *gjøres* |
| Maler `M01–M09` | `maler/` | Utfyllbare dokumenter |
| Kildenotater `K01–K41` | `kilder/` | Referat av veiledere: Datatilsynet, EDPB/WP29, CNIL, Digdir, NSM m.fl. |
| **Begrepsbank** | [BEGREPSBANK.md](BEGREPSBANK.md) | Lovbegrep norsk ↔ engelsk, hjemmel, praksisbegrep → lovbegrep |
| Artikkelindeks | [INDEKS-artikler.md](INDEKS-artikler.md) | GDPR-artikkel → alle notater som omtaler den |
| Hull og motstrid | [KJENTE-MOTSTRIDER.md](KJENTE-MOTSTRIDER.md) | Utdaterte kilder, uenighet mellom kildene |

## Slå opp i lovteksten

```bash
grep -n -A40 '^### Artikkel 28\.' kilder/K43-gdpr-kap*.md      # GDPR-artikkel
grep -n -A2  'id="fp-47"' kilder/K43-gdpr-fortale.md            # fortalepunkt (recital)
grep -n -A20 '^### § 16\.' kilder/K42-personopplysningsloven.md  # popplyl. § (§ 12 a skrives '§ 12 a\.')
grep -n -A40 '^### Article 28 ' kilder/K45-gdpr-en-ch*.md       # GDPR-artikkel, engelsk
grep -n -A2  'id="fp-47"' kilder/K45-gdpr-en-recitals.md       # recital, engelsk
```

Ankre for lenker: `K43-gdpr-kapNN-*.md#art-28`, `K43-gdpr-fortale.md#fp-47`, `K42-personopplysningsloven.md#p16`.

## Regler

- **Lovteksten (K42–K45) går foran alt annet.** For norske svar er norsk tekst (K43) fasit, engelsk (K45) brukes til engelske kilder og sitater. Avviker et notat fra den, gjelder lovteksten, og du sier fra om avviket. Kildehierarkiet står i README.
- **Ikke rediger K42–K45 for hånd.** Teksten mellom `KILDETEKST START` og `KILDETEKST SLUTT` er ordrett fra Lovdata eller EUR-Lex. Oppdatering skjer med skript (se «Vedlikehold» i README).
- Henvis til kilde i hvert svar, for eksempel «GDPR art. 33 nr. 1 [K43]», «[T12]» eller «[K15 s. 3]».
- Bruk lovens begreper (fasit: [BEGREPSBANK.md](BEGREPSBANK.md)): brudd på personopplysningssikkerheten, overtredelsesgebyr, beslutning om tilstrekkelig beskyttelsesnivå, rett til å protestere, forhåndsdrøftinger. Praksisbegreper som «avvik» og «adekvansbeslutning» kan brukes i tillegg.
- Tekst merket **[Merknad – ikke fra kilden]** er tilført av den som skrev notatet. Behandle den som mindre sikker.
- Gjelder svaret ferske forhold (adekvansbeslutninger, nye EDPB-retningslinjer, lovendringer etter 01.01.2022), si fra og anbefal å sjekke.
- Når du endrer `gdpr_artikler` i en frontmatter, generer indeksen på nytt med `python _verktoy/build_index.py .`. Sjekk lenkene med `python _verktoy/linkcheck.py .`.

import re, sys, pathlib, collections
root = pathlib.Path(sys.argv[1])
ART = {1:"Formål",2:"Saklig virkeområde",3:"Geografisk virkeområde",4:"Definisjoner",5:"Prinsipper",6:"Behandlingens lovlighet",7:"Vilkår for samtykke",8:"Barns samtykke",9:"Særlige kategorier",10:"Straffedommer og lovovertredelser",11:"Behandling som ikke krever identifikasjon",12:"Åpenhet, kommunikasjon og frister",13:"Informasjon – innsamlet fra den registrerte",14:"Informasjon – ikke innsamlet fra den registrerte",15:"Innsyn",16:"Retting",17:"Sletting",18:"Begrensning",19:"Underretning ved retting/sletting/begrensning",20:"Dataportabilitet",21:"Rett til å protestere",22:"Automatiserte avgjørelser og profilering",23:"Begrensninger (nasjonal rett)",24:"Behandlingsansvarliges ansvar",25:"Innebygd personvern og personvern som standardinnstilling",26:"Felles behandlingsansvarlige",27:"Representanter utenfor EU",28:"Databehandler",29:"Behandling under myndighet",30:"Protokoll",31:"Samarbeid med tilsynsmyndigheten",32:"Sikkerhet ved behandlingen",33:"Melding av brudd til tilsynsmyndigheten",34:"Underretning av den registrerte ved brudd",35:"Vurdering av personvernkonsekvenser (DPIA)",36:"Forhåndsdrøftinger",37:"Utpeking av personvernombud",38:"Personvernombudets stilling",39:"Personvernombudets oppgaver",40:"Atferdsnormer",41:"Tilsyn med atferdsnormer",42:"Sertifisering",43:"Sertifiseringsorganer",44:"Generelt prinsipp for overføringer",45:"Overføring på grunnlag av beslutning om tilstrekkelig beskyttelsesnivå (adekvans)",46:"Overføring med nødvendige garantier",47:"Bindende virksomhetsregler (BCR)",48:"Overføring/utlevering ikke tillatt etter unionsretten",49:"Unntak i særlige situasjoner",56:"Ledende tilsynsmyndighet",58:"Tilsynsmyndighetens myndighet",60:"Samarbeid ledende/berørte tilsynsmyndigheter",61:"Gjensidig bistand",62:"Tilsynsmyndighetenes felles aktiviteter",65:"Tvisteløsning i EDPB",82:"Erstatningsansvar",83:"Overtredelsesgebyr",85:"Ytrings- og informasjonsfrihet",87:"Nasjonalt identifikasjonsnummer",89:"Arkiv, forskning og statistikk"}
# Reserve for emnenavn: artikkeloverskriftene i lovteksten (K43)
for kf in sorted((root/"kilder").glob("K43-gdpr-kap*.md")):
    for n, tittel in re.findall(r"^### Artikkel (\d+)\. (.+)$", kf.read_text(encoding="utf8"), re.M):
        ART.setdefault(int(n), tittel.strip())
idx = collections.defaultdict(list)
for sub in ["temaer","maler","arbeidsflyter","kilder"]:
    for f in sorted((root/sub).glob("*.md")):
        t = f.read_text(encoding="utf8")
        m = re.search(r"^gdpr_artikler:\s*\[([^\]]*)\]", t, re.M)
        if not m: continue
        tit = re.search(r'^tittel:\s*"?(.*?)"?\s*$', t, re.M)
        fid = f.name.split("-")[0]
        for a in re.findall(r"\d+", m.group(1)):
            idx[int(a)].append((sub, fid, f.name, tit.group(1) if tit else f.stem))
out = ["# Indeks: GDPR-artikkel → notater", "", "Generert automatisk fra `gdpr_artikler` i frontmatter. Temanotater (T), maler (M) og arbeidsflyter (A) står først – start der; kildenotater (K) gir detaljene.", "", "| Art. | Emne | Tema/mal/arbeidsflyt | Kilder |", "|---|---|---|---|"]
for a in sorted(idx):
    syn = ", ".join(f"[{fid}]({sub}/{n})" for sub,fid,n,_ in idx[a] if sub!="kilder")
    src = ", ".join(f"[{fid}]({sub}/{n})" for sub,fid,n,_ in idx[a] if sub=="kilder")
    out.append(f"| {a} | {ART.get(a,'')} | {syn} | {src} |")
(root/"INDEKS-artikler.md").write_text("\n".join(out)+"\n", encoding="utf8")
print(len(idx), "artikler indeksert")

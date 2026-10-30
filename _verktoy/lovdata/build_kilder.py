#!/usr/bin/env python3
"""Del personopplysningsloven (Lovdata, fulltekst) i kildefiler for kunnskapsbasen.

    python3 -I build_kilder.py <lovdata-html> <kilder-mappe> [hentet-dato]

Lager:
    K42-personopplysningsloven.md        norsk lov, kap. 1–9
    K43-gdpr.md                          oversikt: artikkel -> fil
    K43-gdpr-fortale.md                  innledning og fortalepunkt 1–173
    K43-gdpr-kapNN-<slug>.md             ett per GDPR-kapittel I–XI

Alt mellom KILDE_START og KILDE_SLUTT er ordrett lovtekst; alt utenfor er
redaksjonelt. verify() sjekker at kildeteksten tegn for tegn (uten whitespace og
markdown-markup) er lik teksten i Lovdata-HTML-en.
"""
import re
import sys
import types
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup, Tag

sys.path.insert(0, str(Path(__file__).parent))
import lovdata2md as L  # noqa: E402

URL = "https://lovdata.no/dokument/NL/lov/2018-06-15-38/*"
KILDE_START = "<!-- KILDETEKST START: ordrett fra Lovdata, kun formatering endret -->"
KILDE_SLUTT = "<!-- KILDETEKST SLUTT -->"
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]


# --- Kroker: ankre og overskriftsnivå -------------------------------------

def anchor(el):
    i = el.get("id") or ""
    if m := re.fullmatch(r"PARAGRAF_(\w+)", i):
        return f'<a id="p{m[1]}"></a>'
    if m := re.fullmatch(r"gdpr/ARTIKKEL_(\d+)", i):
        return f'<a id="art-{m[1]}"></a>'
    # Fortalepunkt: listepunkt direkte under forordningens innledning
    if "listeItem" in L.classes(el) and el.parent.get("id") == "KAPITTEL_gdpr":
        n = el.find("td").get_text(strip=True).rstrip(".")
        return f'<a id="fp-{n}"></a>'
    return None


def gdpr_heading(level, title):
    for prefix, lvl in (("KAPITTEL", 1), ("Avsnitt", 2), ("Artikkel", 3), ("EUROPAPARLAMENTS", 1)):
        if title.startswith(prefix):
            return lvl
    return level


# --- Rendering ------------------------------------------------------------

def render(nodes):
    lines, footnotes = [], []
    L.convert(types.SimpleNamespace(children=nodes), lines, footnotes)
    md = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    if footnotes:
        md += "\n\n---\n\n" + "\n".join(f"[^{n}]: {t}" for n, t in footnotes)
    return md


def slug(text, words=5):
    t = text.lower().translate(str.maketrans({"æ": "ae", "ø": "o", "å": "a", "é": "e"}))
    return "-".join(re.findall(r"[a-z0-9]+", t)[:words])


def yaml_list(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"


def frontmatter(**kv):
    out = ["---"]
    for k, v in kv.items():
        out.append(f"{k}: {v}")
    return "\n".join(out + ["---", ""])


def page(fm, intro, source_md):
    return f"{fm}\n{intro.strip()}\n\n{KILDE_START}\n\n{source_md}\n\n{KILDE_SLUTT}\n"


# --- Hovedprogram ---------------------------------------------------------

def main(html_path, outdir, hentet):
    outdir = Path(outdir)
    soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "html.parser")
    body = soup.find(id="documentBody")
    gdpr = body.find(id="KAPITTEL_gdpr")
    L.HOOKS["anchor"] = anchor

    meta = "\n".join(L.meta_block(soup))
    dato_felles = f'"LOV-2018-06-15-38, sist endret ved LOV-2021-06-18-124 fra 01.01.2022 (hentet fra Lovdata {hentet})"'
    files = {}

    # K42: norsk lov (alt i documentBody utenom forordningen)
    popplyl_nodes = [c for c in body.children if isinstance(c, Tag) and c is not gdpr]
    popplyl_md = render(popplyl_nodes)
    arts = sorted({int(a) for a in re.findall(r"forordningen artikkel (\d+)", popplyl_md)})
    files["K42-personopplysningsloven.md"] = page(
        frontmatter(
            id="K42",
            tittel='"Personopplysningsloven (lovtekst, kap. 1–9)"',
            utgiver="Justis- og beredskapsdepartementet (lovtekst fra Lovdata)",
            dato=dato_felles,
            spraak="nb",
            fil=f'"{URL}"',
            type="lov",
            gdpr_artikler=yaml_list(arts),
            emner="[personopplysningsloven, norsk rett, lovtekst, nasjonale tilpasninger]",
            relevans="høy",
        ),
        f"""
# Lov om behandling av personopplysninger (personopplysningsloven) – kap. 1–9

**Ordrett lovtekst.** Dette er de norske bestemmelsene i personopplysningsloven (§ 1–34). Personvernforordningen (GDPR), som gjelder som norsk lov etter § 1, ligger i [K43](K43-gdpr.md).

**Oppslag:** Hver paragraf har anker `p<nr>`, for eksempel [§ 12 a](#p12a). Med Grep: `grep -n '^### § 12 a\\.' kilder/K42-personopplysningsloven.md`. Henvisninger til GDPR i teksten slås opp i [K43](K43-gdpr.md).

**Om formateringen:** Teksten er konvertert fra Lovdata-HTML. Lenker er gjort om til ren tekst, bokstavlister er Markdown-lister, og fotnoter uten henvisning i teksten («Endret ved lov …») står som sitatblokk der Lovdata plasserer dem. Ordlyden er ikke endret.

## Lovdata-metadata

{meta}
""",
        popplyl_md,
    )

    # GDPR: innledning/fortale + ett kapittel per fil
    L.HOOKS["heading"] = gdpr_heading
    kids = [c for c in gdpr.children if isinstance(c, Tag)]
    chapters = [c for c in kids if re.fullmatch(r"KAPITTEL_gdpr-\d+", c.get("id") or "")]
    first = kids.index(chapters[0])
    fortale_md = render(kids[:first])
    n_fp = len(re.findall(r'<a id="fp-\d+"></a>', fortale_md))

    chapter_info = []  # (nr, tittel, filnavn, [(art, tittel)])
    for i, ch in enumerate(chapters, 1):
        title = ch.find("h3").get_text(" ", strip=True)
        articles = []
        for a in ch.find_all("div", id=re.compile(r"^gdpr/ARTIKKEL_\d+$")):
            h = re.sub(r"\s+", " ", a.find(["h4", "h5"]).get_text(" ", strip=True))
            articles.append((int(a["id"].split("_")[1]), h))
        name = re.sub(r"^KAPITTEL [IVX]+ ", "", title)
        chapter_info.append((i, name, f"K43-gdpr-kap{i:02d}-{slug(name)}.md", articles))

    def nav(idx):
        names = ["K43-gdpr-fortale.md"] + [c[2] for c in chapter_info]
        labels = ["Fortale"] + [f"Kap. {ROMAN[c[0] - 1]}" for c in chapter_info]
        prev = f"[← {labels[idx - 1]}]({names[idx - 1]})" if idx > 0 else ""
        nxt = f"[{labels[idx + 1]} →]({names[idx + 1]})" if idx + 1 < len(names) else ""
        # Engelsk tekst (K45, se _verktoy/eurlex/build_gdpr_en.py) med samme ankre, hvis den finnes
        en = (["K45-gdpr-en-recitals.md"] if (outdir / "K45-gdpr-en-recitals.md").exists() else [None]) + [
            next(iter(sorted(outdir.glob(f"K45-gdpr-en-ch{c[0]:02d}-*.md"))), None) for c in chapter_info
        ]
        eng = f"English: [K45 {'recitals' if idx == 0 else 'ch. ' + ROMAN[idx - 1]}]({Path(en[idx]).name})" if en[idx] else ""
        return " · ".join(x for x in (prev, "[Oversikt K43](K43-gdpr.md)", nxt, eng) if x)

    gdpr_intro_common = (
        "**Ordrett lovtekst:** norsk tekst av forordning (EU) 2016/679 slik den er inntatt i "
        "personopplysningsloven § 1 på Lovdata. Lenker er gjort om til ren tekst, og ordlyden er ikke endret."
    )

    files["K43-gdpr-fortale.md"] = page(
        frontmatter(
            id="K43",
            tittel='"GDPR – innledning og fortale (fortalepunkt 1–173)"',
            utgiver="Europaparlamentet og Rådet (norsk tekst fra Lovdata)",
            dato=dato_felles,
            spraak="nb",
            fil=f'"{URL}"',
            type="lov",
            gdpr_artikler="[]",
            emner="[gdpr, fortale, recitals, lovtekst]",
            relevans="høy",
        ),
        f"""
# GDPR – innledning og fortale

{nav(0)}

{gdpr_intro_common}

**Oppslag:** Hvert fortalepunkt (recital) har anker `fp-<nr>`, for eksempel [fortalepunkt 26](#fp-26). Med Grep: `grep -n 'id="fp-26"' -A1 kilder/K43-gdpr-fortale.md`. Fortalepunktene står som listepunkter med nummeret først (`- 26\\. …`).
""",
        fortale_md,
    )

    for idx, (i, name, fname, articles) in enumerate(chapter_info, 1):
        ch_md = render([chapters[i - 1]])
        nums = [a for a, _ in articles]
        rng = f"art. {nums[0]}–{nums[-1]}" if len(nums) > 1 else f"art. {nums[0]}"
        files[fname] = page(
            frontmatter(
                id="K43",
                tittel=f'"GDPR kapittel {ROMAN[i - 1]} – {name} ({rng})"',
                utgiver="Europaparlamentet og Rådet (norsk tekst fra Lovdata)",
                dato=dato_felles,
                spraak="nb",
                fil=f'"{URL}"',
                type="lov",
                gdpr_artikler=yaml_list(nums),
                emner="[gdpr, lovtekst]",
                relevans="høy",
            ),
            f"""
# GDPR kapittel {ROMAN[i - 1]} – {name} ({rng})

{nav(idx)}

{gdpr_intro_common}

**Oppslag:** Hver artikkel har anker `art-<nr>`, for eksempel [artikkel {nums[0]}](#art-{nums[0]}), og overskriften `### Artikkel <nr>.`. Med Grep: `grep -n '^### Artikkel {nums[0]}\\.' kilder/K43-gdpr-kap*.md`. Ledd står som `1\\.`, `2\\.` og bokstaver som `- a.`.
""",
            ch_md,
        )

    # Oversikt
    rows = "\n".join(
        f"| {ROMAN[i - 1]} | {name} | {a[0][0]}–{a[-1][0]} | [{fname}]({fname}) |"
        for i, name, fname, a in chapter_info
    )
    art_rows = "\n".join(
        f"| {n} | [{t}]({fname}#art-{n}) | {ROMAN[i - 1]} |"
        for i, _, fname, a in chapter_info
        for n, t in a
    )
    files["K43-gdpr.md"] = f"""{frontmatter(
        id="K43",
        tittel='"Personvernforordningen (GDPR) – norsk lovtekst, oversikt"',
        utgiver="Europaparlamentet og Rådet (norsk tekst fra Lovdata)",
        dato=dato_felles,
        spraak="nb",
        fil=f'"{URL}"',
        type="lov",
        gdpr_artikler="[]",
        emner="[gdpr, lovtekst, oversikt]",
        relevans="høy",
    )}
# Personvernforordningen (GDPR) – norsk lovtekst (oversikt)

Forordning (EU) 2016/679 i norsk språkdrakt, slik den gjelder som norsk lov etter [personopplysningsloven § 1](K42-personopplysningsloven.md#p1). Teksten er hentet fra Lovdata {hentet} og delt i én fil for fortalen og én fil per kapittel. Filene inneholder **ordrett lovtekst**; denne oversikten er redaksjonell.

## Når skal agenten bruke denne kilden

- Når svaret krever den eksakte ordlyden i en GDPR-artikkel eller et fortalepunkt (sitat, vilkår, frister, unntak).
- Når to kilder er uenige: lovteksten står øverst i kildehierarkiet (se [_KONVENSJONER.md](../_KONVENSJONER.md)).
- For norske særregler (aldersgrense, unntak fra informasjonsplikt og innsyn, kameraovervåking, nasjonalt ID-nummer, arbeidsliv og forskning): se [K42](K42-personopplysningsloven.md).

## Slik slår du opp

- **Artikkel N:** finn filen i tabellen under, eller kjør `grep -n '^### Artikkel 28\\.' kilder/K43-gdpr-kap*.md`. Ankeret er `#art-28`.
- **Fortalepunkt N:** [K43-gdpr-fortale.md](K43-gdpr-fortale.md), anker `#fp-N` (`grep -n 'id="fp-26"' -A1 kilder/K43-gdpr-fortale.md`).
- **Definisjoner:** artikkel 4 i [kapittel I]({chapter_info[0][2]}#art-4).
- **Personopplysningsloven § N:** [K42](K42-personopplysningsloven.md), anker `#pN` (f.eks. `#p12a`).
- **Engelsk tekst:** [K45](K45-gdpr-en.md) har samme ankre (`#art-28`, `#fp-47`). Lenke til engelsk kapittel står i navigasjonslinjen i hver fil.

## Filer per kapittel

| Kap. | Tittel | Artikler | Fil |
|---|---|---|---|
| – | Innledning og fortale (fortalepunkt 1–{n_fp}) | – | [K43-gdpr-fortale.md](K43-gdpr-fortale.md) |
{rows}

## Alle artikler

| Art. | Overskrift (lenke) | Kap. |
|---|---|---|
{art_rows}
"""

    for name, text in files.items():
        (outdir / name).write_text(text, encoding="utf-8")
        print(f"{name:65} {len(text):>8,} tegn")
    verify(soup, outdir, files)


# --- Verifisering ---------------------------------------------------------

def _norm(s):
    return re.sub(r"[\s​\xa0]+", "", s)


def verify(soup, outdir, files):
    body = soup.find(id="documentBody")
    for sel in ("a.share-paragraf", "sup.fotnoteref", "td.fotnoteNummer"):
        for el in body.select(sel):
            el.decompose()
    fn_html = [_norm(t.get_text()) for t in body.select("table.fotnote td.fotnote")]
    for t in body.select("table.fotnote"):
        t.decompose()
    src = _norm(body.get_text())
    assert "*" not in src, "kildeteksten inneholder *, markup-strippingen er ikke trygg"

    order = ["K42-personopplysningsloven.md", "K43-gdpr-fortale.md"] + sorted(
        n for n in files if n.startswith("K43-gdpr-kap")
    )
    md_body, fn_md = [], []
    for name in order:
        text = (outdir / name).read_text(encoding="utf-8")
        part = text.split(KILDE_START, 1)[1].split(KILDE_SLUTT, 1)[0]
        for line in part.splitlines():
            if m := re.match(r"^\[\^\d+\]: (.*)", line):
                fn_md.append(_norm(m[1].replace("*", "")))
                continue
            if line.strip() == "---":
                continue
            if m := re.match(r"^> \*(.*)\*$", line):  # fotnote uten referanse
                fn_md.append(_norm(m[1]))
                continue
            line = re.sub(r'<a id="[^"]+"></a>', "", line)
            line = re.sub(r"\[\^\d+\]", "", line)
            line = re.sub(r"^\s*(#+ |- )", "", line)
            line = line.replace("\\.", ".").replace("*", "")
            md_body.append(line)
    got = _norm("".join(md_body))

    ok = got == src
    print(f"\nKildetekst (uten fotnoter): {len(src):,} tegn i HTML, {len(got):,} i MD -> {'IDENTISK' if ok else 'AVVIK'}")
    if not ok:
        i = next(i for i, (a, b) in enumerate(zip(src, got)) if a != b)
        print("  HTML:", src[max(0, i - 60):i + 60])
        print("  MD:  ", got[max(0, i - 60):i + 60])
    fok = sorted(fn_html) == sorted(fn_md)
    print(f"Fotnoter: {len(fn_html)} i HTML, {len(fn_md)} i MD -> {'IDENTISKE' if fok else 'AVVIK'}")
    sys.exit(0 if ok and fok else 1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else date.today().isoformat())

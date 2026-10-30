#!/usr/bin/env python3
"""Lag kilder/K45-gdpr-en*.md: offisiell engelsk tekst av GDPR fra EUR-Lex.

    python3 -I _verktoy/eurlex/build_gdpr_en.py <konsolidert> <oj> <rettelse> kilder [hentet-dato]

Kildene (lagres som .html eller Safari-.webarchive):
  <konsolidert>  EUR-Lex konsolidert tekst 02016R0679-20160504 (artikler med rettelsen ►C1)
                 https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02016R0679-20160504
  <oj>           EU-tidende OJ L 119, 4.5.2016 (fortalen; den konsoliderte teksten har ikke fortale)
                 https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
  <rettelse>     Rettelse OJ L 127, 23.5.2018 (endrer fortalepunkt 71 og artikler)
                 https://publications.europa.eu/resource/celex/32016R0679R(02)

Artiklene hentes fra den konsoliderte teksten fordi den har rettelsen innarbeidet, slik
den norske teksten på Lovdata har. Fortalen hentes fra OJ L 119. Rettelsen av fortalepunkt 71
legges inn som merket blokk rett etter punktet. Skriptet stopper hvis teksten i Markdown
ikke er tegnlik med HTML-en.
"""
import plistlib
import re
import sys
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

START = "<!-- KILDETEKST START: ordrett fra EUR-Lex, kun formatering endret -->"
SLUTT = "<!-- KILDETEKST SLUTT -->"
RETTELSE = "> **[Rettelse, OJ L 127, 23.5.2018]**"
URL_KONS = "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02016R0679-20160504"
URL_OJ = "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679"
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]


def load(path):
    raw = Path(path).read_bytes()
    if raw.startswith(b"bplist"):
        raw = plistlib.loads(raw)["WebMainResource"]["WebResourceData"]
    return BeautifulSoup(raw.decode("utf-8"), "html.parser")


def classes(el):
    return el.get("class") or [] if isinstance(el, Tag) else []


def ws(s):
    return re.sub(r"\s+", " ", s).strip()


# --- Inline -------------------------------------------------------------------

def inline(el):
    """Tekst fra et inline-element. Fotnotehenvisninger blir [^N]."""
    out = []
    for c in el.descendants:
        if isinstance(c, NavigableString):
            if c.find_parent(class_=["anchorarrow", "superscript", "oj-note-tag"]):
                continue
            out.append(str(c))
        elif c.name == "span" and set(classes(c)) & {"superscript", "oj-note-tag"} and c.find_parent("a"):
            # (konsolidert: <a><span class=superscript>1</span></a>; OJ: (<span class=oj-note-tag>4</span>))
            out.append(f"[^{c.get_text(strip=True)}]")
    return re.sub(r"\(\s*(\[\^\d+\])\s*\)", r"\1", ws("".join(out)))


def has_blocks(el):
    return any(isinstance(c, Tag) and c.name in ("p", "div", "table") for c in el.children)


# --- Konsolidert tekst: artikler ---------------------------------------------

def blocks(el, depth=0):
    """Blokkelementer i en artikkel -> Markdown-linjer."""
    lines = []
    for c in el.children:
        if isinstance(c, NavigableString):
            if c.strip():
                lines.append(ws(c))
            continue
        cls = classes(c)
        if "modref" in cls:
            if "C1" in c.get_text():
                lines.append("*▼C1*")
        elif "grid-container" in cls:
            label = inline(c.find(class_="grid-list-column-1"))
            body = blocks(c.find(class_="grid-list-column-2"), depth + 1)
            first = (label + " " + body[0]).strip() if body else label
            lines.append("  " * depth + "- " + first)
            lines += ["  " * (depth + 1) + b.lstrip() if not b.lstrip().startswith("- ") else "  " + b for b in body[1:]]
        elif c.name == "div" and c.find("span", class_="no-parag", recursive=False):
            num = c.find("span", class_="no-parag", recursive=False).get_text(strip=True)
            rest = [x for x in c.children if x is not c.find("span", class_="no-parag", recursive=False)]
            body = []
            for x in rest:
                if isinstance(x, Tag):
                    body += blocks(x, depth) if has_blocks(x) else [inline(x)]
                elif x.strip():
                    body.append(ws(x))
            body = [b for b in body if b]
            lines.append(num.rstrip(".") + "\\. " + body[0])
            lines += body[1:]
        elif c.name in ("p", "div") and not has_blocks(c):
            t = inline(c)
            if t:
                lines.append(t)
        elif c.name in ("div",):
            lines += blocks(c, depth)
    return lines


def article(el):
    n = el["id"].split("_")[1]
    title = inline(el.find(class_="stitle-article-norm"))
    lines = ["", f'<a id="art-{n}"></a>', "", f"### Article {n} – {title}", ""]
    for c in el.children:
        if not isinstance(c, Tag) or "title-article-norm" in classes(c) or "eli-title" in classes(c):
            continue
        for b in blocks(BeautifulSoup(f"<div>{c}</div>", "html.parser").div):
            lines.append(b)
            if not b.startswith("  ") and not b.startswith("- "):
                lines.append("")
            elif b.startswith("- ") or b.startswith("  "):
                pass
        lines.append("")
    out = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    # Tom linje etter hver liste
    out = re.sub(r"(\n(?:  )*- [^\n]*)\n(?!(?:  )*- |\n)", r"\1\n\n", out)
    return n, title, out


def chapters(cons):
    res = []
    for rn in ROMAN:
        cpt = cons.find(id=f"cpt_{rn}")
        heads = cpt.find_all("p", class_=["title-division-1", "title-division-2"], recursive=False)
        ctitle = inline(heads[1])
        md, arts = [f"# {inline(heads[0])} – {ctitle}", ""], []
        for el in cpt.find_all(["div"], id=re.compile(r"^(cpt_[IVX]+\.sct_\d+|art_\d+)$")):
            if el["id"].startswith("cpt"):
                h = el.find_all("p", class_=["title-division-1", "title-division-2"], recursive=False)
                md += ["", f"## {inline(h[0])} – {inline(h[1])}", ""]
            else:
                n, t, text = article(el)
                arts.append((n, t))
                md.append(text)
        res.append((rn, ctitle, arts, re.sub(r"\n{3,}", "\n\n", "\n".join(md)).strip()))
    return res


def footnotes_cons(cons):
    out = {}
    for p in cons.select("p.footnote"):
        n = p.find(class_="superscript").get_text(strip=True)
        a = p.find("a")
        a.decompose()
        out[n] = ws(p.get_text()).lstrip("() ").strip()
    return out


# --- OJ: fortale ----------------------------------------------------------------

def recitals(oj):
    lines = []
    for el in oj.find_all(id=re.compile(r"^rct_\d+$")):
        n = el["id"].split("_")[1]
        tds = el.find("tr").find_all("td", recursive=False)
        paras = [inline(p) for p in tds[1].find_all("p")] or [inline(tds[1])]
        lines += [f'<a id="fp-{n}"></a>', f"{inline(tds[0])} {paras[0]}", ""]
        for p in paras[1:]:
            lines += [p, ""]
    return lines


def footnotes_oj(oj):
    out = {}
    for p in oj.find_all("p", class_="oj-note"):
        a = p.find("a")
        n = a.get_text(strip=True).strip("()")
        a.decompose()
        out[n] = ws(p.get_text())
    return out


def corrigendum_71(corr):
    t = ws(corr.get_text(" "))
    m = re.search(r"recital 71, fifth and sixth sentences: for: ‘(.*?)’, read: ‘(.*?)’\.", t)
    return m.group(2)


# --- Skriving ------------------------------------------------------------------

def slug(s):
    s = s.lower().replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def fm(tittel, arts, dato, hentet, url):
    return [
        "---", "id: K45", f'tittel: "{tittel}"',
        "utgiver: European Parliament and Council (offisiell engelsk tekst fra EUR-Lex)",
        f'dato: "{dato} (hentet fra EUR-Lex {hentet})"', "spraak: en", f'fil: "{url}"', "type: lov",
        f"gdpr_artikler: []", "emner: [gdpr, lovtekst, engelsk]", "relevans: høy", "---", "",
    ]


def used_notes(text, notes):
    refs = re.findall(r"\[\^(\d+)\]", text)
    return [f"[^{n}]: {notes[n]}" for n in dict.fromkeys(refs)]


def main(kons_p, oj_p, corr_p, outdir, hentet):
    cons, oj, corr = load(kons_p), load(oj_p), load(corr_p)
    out = Path(outdir)
    chs = chapters(cons)
    fn_c, fn_o = footnotes_cons(cons), footnotes_oj(oj)
    files = {}
    names = [f"K45-gdpr-en-ch{i + 1:02d}-{slug(t)}.md" for i, (_, t, _, _) in enumerate(chs)]
    nb = sorted(p.name for p in out.glob("K43-gdpr-kap*.md"))
    dato_k = "Regulation (EU) 2016/679, OJ L 119, 4.5.2016, as corrected by OJ L 127, 23.5.2018 (EUR-Lex konsolidert tekst 02016R0679-20160504)"

    for i, (rn, ct, arts, md) in enumerate(chs):
        a, b = arts[0][0], arts[-1][0]
        prev = f"[← Ch. {ROMAN[i - 1]}]({names[i - 1]}) · " if i else ""
        nxt = f" · [Ch. {ROMAN[i + 1]} →]({names[i + 1]})" if i < len(chs) - 1 else ""
        notes = used_notes(md, fn_c)
        text = fm(f"GDPR (EN) chapter {rn} – {ct} (art. {a}–{b})", arts, dato_k, hentet, URL_KONS) + [
            f"# GDPR (EN) chapter {rn} – {ct} (art. {a}–{b})", "",
            f"{prev}[Oversikt K45](K45-gdpr-en.md){nxt} · Norsk: [K43 kap. {rn}]({nb[i]})", "",
            "**Ordrett offisiell engelsk tekst** av forordning (EU) 2016/679 fra EUR-Lex, konsolidert tekst med rettelsen i OJ L 127, 23.5.2018. "
            "Rettede steder er merket `►C1 … ◄` (inne i et ledd) eller `*▼C1*` (foran et rettet punkt), slik EUR-Lex merker dem. "
            "Den konsoliderte teksten er et dokumentasjonsverktøy. Den rettslig bindende teksten er den som er kunngjort i EU-tidende.",
            "",
            f"**Oppslag:** Samme ankre som i den norske teksten: `art-<nr>`, for eksempel [Article {a}](#art-{a}). "
            f"Med Grep: `grep -n '^### Article {a} ' kilder/K45-gdpr-en-ch*.md`. Ledd står som `1\\.` og bokstaver som `- (a)`.",
            "", START, "", md, "",
        ] + ([*notes, ""] if notes else []) + [SLUTT, ""]
        files[names[i]] = "\n".join(text)

    rec = recitals(oj)
    r71 = corrigendum_71(corr)
    i71 = rec.index('<a id="fp-72"></a>')
    rec[i71:i71] = [f"{RETTELSE} Fifth and sixth sentences shall read: ‘{r71}’", ""]
    rtext = "\n".join(rec)
    notes = used_notes(rtext, fn_o)
    files["K45-gdpr-en-recitals.md"] = "\n".join(fm(
        "GDPR (EN) recitals 1–173", [], "Regulation (EU) 2016/679, OJ L 119, 4.5.2016, recitals; recital 71 corrected by OJ L 127, 23.5.2018",
        hentet, URL_OJ) + [
        "# GDPR (EN) recitals 1–173", "",
        "[Oversikt K45](K45-gdpr-en.md) · Norsk: [K43 fortale](K43-gdpr-fortale.md)", "",
        "**Ordrett offisiell engelsk tekst** av fortalen, fra EU-tidende OJ L 119, 4.5.2016. Den konsoliderte teksten på EUR-Lex har ikke fortale. "
        f"Rettelsen i OJ L 127, 23.5.2018, endrer bare fortalepunkt 71. Den rettede ordlyden står som merket blokk (`{RETTELSE}`) rett etter punktet.",
        "",
        "**Oppslag:** Samme ankre som i den norske fortalen: `fp-<nr>`. Med Grep: `grep -n -A2 'id=\"fp-47\"' kilder/K45-gdpr-en-recitals.md`.",
        "", START, "", *rec, *notes, "", SLUTT, "",
    ])

    # Oversikt
    rows = []
    for i, (rn, ct, arts, _) in enumerate(chs):
        for n, t in arts:
            rows.append(f"| {n} | [{t}]({names[i]}#art-{n}) | [K43]({nb[i]}#art-{n}) |")
    chrows = [f"| {rn} | [{ct}]({names[i]}) | {arts[0][0]}–{arts[-1][0]} | [K43]({nb[i]}) |" for i, (rn, ct, arts, _) in enumerate(chs)]
    files["K45-gdpr-en.md"] = "\n".join(fm("GDPR (EN) – oversikt", [], dato_k, hentet, URL_KONS) + [
        "# GDPR på engelsk (K45) – oversikt", "",
        "Offisiell engelsk tekst av forordning (EU) 2016/679, ordrett fra EUR-Lex, delt i én fil per kapittel pluss fortalen. "
        "Filene har **samme ankre som den norske teksten i K43** (`#art-28`, `#fp-47`), så du kan bytte språk ved å bytte filnavn.",
        "",
        "**Kilder og versjon**", "",
        f"- Artikler: konsolidert tekst 02016R0679-20160504 (<{URL_KONS}>), som har rettelsen i OJ L 127, 23.5.2018, innarbeidet. Det samsvarer med den norske teksten på Lovdata, som også følger den rettede ordlyden (for eksempel art. 37 nr. 1 bokstav c «eller»).",
        f"- Fortale: EU-tidende OJ L 119, 4.5.2016 (<{URL_OJ}>). Rettelsen av fortalepunkt 71 er lagt inn som merket blokk.",
        "- Den konsoliderte teksten har «no legal effect». Ved tvil gjelder teksten i EU-tidende med rettelsen.",
        "- Engelsk tekst brukes til å forstå engelskspråklige kilder (EDPB, CNIL) og til begrepsbanken. **Norsk lovtekst (K43) er fasit for norske svar.**",
        "",
        "## Kapitler", "", "| Kap. | Title | Artikler | Norsk |", "|---|---|---|---|", *chrows,
        f"| – | [Recitals](K45-gdpr-en-recitals.md) | fortalepunkt 1–173 | [K43](K43-gdpr-fortale.md) |",
        "", "## Artikler", "", "| Art. | Title | Norsk |", "|---|---|---|", *rows, "",
    ])

    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8")
        print(f"{name:70} {len(text):>8,} tegn")
    verify(cons, oj, r71, fn_c, fn_o, out, names)


# --- Verifisering ---------------------------------------------------------------

def _norm(s):
    return re.sub(r"[\s\xa0​]+", "", s)


def _md_text(path):
    part = path.read_text(encoding="utf-8").split(START, 1)[1].split(SLUTT, 1)[0]
    body, notes = [], []
    for line in part.splitlines():
        if line.startswith(RETTELSE):
            continue
        if m := re.match(r"^\[\^(\d+)\]: (.*)", line):
            notes.append(_norm(m[2]))
            continue
        line = re.sub(r'<a id="[^"]+"></a>', "", line)
        line = re.sub(r"\[\^\d+\]", "", line)
        if line.startswith("#"):
            line = line.lstrip("# ").replace(" – ", "", 1)
        line = re.sub(r"^\s*- ", "", line).replace("\\.", ".").replace("*▼C1*", "")
        body.append(line)
    return _norm("".join(body)), notes


def verify(cons, oj, r71, fn_c, fn_o, out, names):
    # Konsolidert: alle kapitler, uten ▼B/▼C1-markører, pilikoner og fotnotehenvisninger
    src = []
    for rn in ROMAN:
        cpt = BeautifulSoup(str(cons.find(id=f"cpt_{rn}")), "html.parser")
        for el in cpt.select("p.modref, a.anchorarrow"):
            el.decompose()
        for el in cpt.select("span.superscript"):
            el.find_parent("a").decompose()
        src.append(cpt.get_text())
    want = _norm("".join(src)).replace("()", "")
    got = "".join(_md_text(out / n)[0] for n in names)
    ok1 = want == got
    report("Artikler (konsolidert)", want, got)

    rs = BeautifulSoup("".join(str(e) for e in oj.find_all(id=re.compile(r"^rct_\d+$"))), "html.parser")
    for el in rs.select("span.oj-note-tag"):
        el.parent.decompose()
    want2 = _norm(rs.get_text())
    got2, notes2 = _md_text(out / "K45-gdpr-en-recitals.md")
    ok2 = want2 == got2
    report("Fortale (OJ L 119)", want2, got2)
    ok3 = f"‘{r71}’" in (out / "K45-gdpr-en-recitals.md").read_text(encoding="utf-8")
    print(f"Rettelse fp 71: {'OK' if ok3 else 'AVVIK'}")
    sys.exit(0 if ok1 and ok2 and ok3 else 1)


def report(label, want, got):
    ok = want == got
    print(f"{label}: {len(want):,} tegn i HTML, {len(got):,} i MD -> {'IDENTISK' if ok else 'AVVIK'}")
    if not ok:
        i = next((i for i, (a, b) in enumerate(zip(want, got)) if a != b), min(len(want), len(got)))
        print("  HTML:", want[max(0, i - 80):i + 80])
        print("  MD:  ", got[max(0, i - 80):i + 80])


if __name__ == "__main__":
    main(*sys.argv[1:5], sys.argv[5] if len(sys.argv) > 5 else date.today().isoformat())

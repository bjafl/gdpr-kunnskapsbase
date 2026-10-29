#!/usr/bin/env python3
"""Bygg BEGREPSBANK.md og verifiser hvert begrep mot lovteksten.

    python3 -I _verktoy/begrepsbank/build_begrepsbank.py [gdpr-en.xhtml]

Norsk tekst: kilder/K43-*.md (GDPR) og kilder/K42-*.md (personopplysningsloven).
Engelsk tekst: offisiell utgave av forordning (EU) 2016/679 fra EUs publikasjonskontor
(Cellar, CELEX 32016R0679). Hentes automatisk hvis fil ikke oppgis.

Hvert norsk begrep må stå i angitt artikkel/fortalepunkt/paragraf i K43/K42, og
hvert engelske begrep i SAMME enhet i den engelske teksten. Ellers stopper skriptet.
Definisjonene i art. 4 hentes punkt for punkt fra begge tekstene.
"""
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent))
from begreper import KATEGORIER, PRAKSIS  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
KILDER = ROOT / "kilder"
CELLAR = "https://publications.europa.eu/resource/celex/32016R0679"
ELI = "http://data.europa.eu/eli/reg/2016/679/oj"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("\\.", ".").replace("*", "")
    return re.sub(r"\s+", " ", s).strip().lower()


# --- Norsk tekst (K43/K42) -------------------------------------------------

def _units(text, prefix):
    """Del en kildefil i enheter ved ankrene <a id="{prefix}N"></a>."""
    body = text.split("KILDETEKST START", 1)[1].split("KILDETEKST SLUTT", 1)[0]
    parts = re.split(r'<a id="([a-z-]+?)([0-9]+[a-z]?)"></a>', body)
    out = {}
    for i in range(1, len(parts), 3):
        if parts[i] == prefix:
            out[parts[i + 1]] = parts[i + 2]
    return out


NB_ART, ART_FILE = {}, {}
for f in sorted(KILDER.glob("K43-gdpr-kap*.md")):
    for n, t in _units(f.read_text(encoding="utf-8"), "art-").items():
        NB_ART[n], ART_FILE[n] = t, f.name
NB_FP = _units((KILDER / "K43-gdpr-fortale.md").read_text(encoding="utf-8"), "fp-")
NB_PAR = _units((KILDER / "K42-personopplysningsloven.md").read_text(encoding="utf-8"), "p")


# --- Engelsk tekst (EU-tidende) -------------------------------------------

def load_en(path):
    if path:
        return Path(path).read_text(encoding="utf-8")
    req = urllib.request.Request(CELLAR, headers={"Accept": "application/xhtml+xml", "Accept-Language": "eng"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


# --- Hjemmel ---------------------------------------------------------------

def parse_ref(ref):
    """'5(1)(b)' -> ('art','5','art. 5 nr. 1 bokstav b'); 'fp26'; '§12a'."""
    if ref.startswith("fp"):
        return "fp", ref[2:], f"fortalepunkt {ref[2:]}"
    if ref.startswith("§"):
        return "par", ref[1:], f"popplyl. § {ref[1:]}"
    m = re.fullmatch(r"(\d+)(?:\((\d+)\))?(?:\(([a-z])\))?", ref)
    art, nr, b = m.groups()
    label = f"art. {art}" + (f" nr. {nr}" if nr else "") + (f" bokstav {b}" if b else "")
    return "art", art, label


def link(kind, key, label):
    if kind == "art":
        return f"[{label}](kilder/{ART_FILE[key]}#art-{key})"
    if kind == "fp":
        return f"[{label}](kilder/K43-gdpr-fortale.md#fp-{key})"
    return f"[{label}](kilder/K42-personopplysningsloven.md#p{key})"


def check(term, text, where, errors, soft):
    alts = term.split("|")
    t = norm(text)
    hit = [a for a in alts if norm(a) in t]
    if not hit:
        errors.append(f"{where}: fant ikke «{alts[0]}» (alternativer: {alts})")
    elif norm(alts[0]) not in t:
        soft.append(f"{where}: «{alts[0]}» står i bøyd form, verifisert med «{hit[0]}»")
    return alts[0]


def main(en_path=None):
    soup = BeautifulSoup(load_en(en_path), "html.parser")
    en_art = lambda n: soup.find(id=f"art_{n}").get_text(" ")  # noqa: E731
    en_fp = lambda n: soup.find(id=f"rct_{n}").get_text(" ")  # noqa: E731
    errors, soft = [], []

    # 1. Art. 4-definisjoner, punkt for punkt
    # Punkt "- N\. «begrep» definisjon", ev. fulgt av innrykkede underpunkter (a, b, c)
    nb_def = [
        (n, term, (first + " " + " ".join(s.strip()[2:] for s in subs.splitlines() if s.strip())).strip())
        for n, term, first, subs in re.findall(
            r"^- (\d+)\\\. «([^»]+)»:? ?(.*)\n((?:\s+- .*\n)*)", NB_ART["4"], re.M)
    ]
    en4 = re.sub(r"\s+", " ", en_art(4))
    en_def = dict(re.findall(r"\((\d+)\) ['‘]([^’']+)['’]", en4))
    if len(nb_def) != 26 or len(en_def) != 26:
        errors.append(f"art. 4: forventet 26 definisjoner, fant {len(nb_def)} norske og {len(en_def)} engelske")
    defs = []
    for n, term, definisjon in nb_def:
        if n not in en_def:
            errors.append(f"art. 4 nr. {n}: fant ikke engelsk definisjon")
            continue
        defs.append((n, term, en_def[n], definisjon.strip()))

    # 2. Kategorier
    cats = []
    for navn, poster in KATEGORIER:
        rows = []
        for nb, ref, en, merknad in poster:
            kind, key, label = parse_ref(ref)
            where = f"{nb.split('|')[0]} ({label})"
            nb_text = {"art": NB_ART, "fp": NB_FP, "par": NB_PAR}[kind].get(key)
            if nb_text is None:
                errors.append(f"{where}: enheten finnes ikke i K42/K43")
                continue
            nb_vis = check(nb, nb_text, where + " [nb]", errors, soft)
            en_vis = "–"
            if en is not None:
                en_text = en_art(key) if kind == "art" else en_fp(key) if kind == "fp" else ""
                en_vis = check(en, en_text, where + " [en]", errors, soft)
            rows.append((nb_vis, en_vis, link(kind, key, label), merknad))
        cats.append((navn, rows))

    # 3. Praksisbegreper
    praksis = []
    for prak, lov, ref, en in PRAKSIS:
        kind, key, label = parse_ref(ref)
        where = f"praksis «{prak}» ({label})"
        lov_vis = check(lov, NB_ART[key], where + " [nb]", errors, soft)
        en_vis = check(en, en_art(key), where + " [en]", errors, soft)
        praksis.append((prak, lov_vis, en_vis, link(kind, key, label)))

    for s in soft:
        print("merk:", s)
    if errors:
        print("\nFEIL – begrepsbanken er ikke skrevet:")
        for e in errors:
            print("  ", e)
        sys.exit(1)

    write(defs, cats, praksis)
    n_cat = sum(len(r) for _, r in cats)
    print(f"OK: {len(defs)} definisjoner, {n_cat} begreper, {len(praksis)} praksisbegreper – alle verifisert")


def write(defs, cats, praksis):
    out = [
        "# Begrepsbank: GDPR og personopplysningsloven (norsk–engelsk)",
        "",
        "Autoritativ ordliste over personvernbegreper. Hvert begrep er knyttet til hjemmelen i lovteksten. "
        "**Både det norske og det engelske begrepet er maskinelt kontrollert mot lovteksten**: "
        "det norske står i den angitte artikkelen, det angitte fortalepunktet eller den angitte paragrafen i [K43](kilder/K43-gdpr.md) eller [K42](kilder/K42-personopplysningsloven.md), "
        "og det engelske står i samme artikkel eller fortalepunkt i den offisielle engelske utgaven av forordningen.",
        "",
        "**Kilder**",
        "",
        "- Norsk: GDPR slik den er inntatt i personopplysningsloven § 1, og personopplysningsloven, begge fra Lovdata (se K42/K43).",
        f"- Engelsk: Regulation (EU) 2016/679, OJ L 119, 4.5.2016, s. 1–88 (ELI: <{ELI}>), hentet fra EUs publikasjonskontor (Cellar, CELEX 32016R0679) {date.today().isoformat()}. "
        "Rettelsen i OJ L 127, 23.5.2018, er ikke innarbeidet i denne utgaven.",
        "- Personopplysningsloven har ingen offisiell engelsk tekst. Norske lovbegreper står derfor uten engelsk motsvar.",
        "",
        "**Bruk**",
        "",
        "- I norsk tekst skal lovens begrep brukes når et rettslig begrep omtales. Praksisbegreper (seksjon 3) kan brukes i tillegg, men ikke i stedet.",
        "- I engelskspråklige kilder (EDPB/WP29, CNIL) slår du opp det engelske begrepet i seksjon 4 for å finne det norske lovbegrepet.",
        "- Kolonnen «Merknad» er redaksjonell og ikke lovtekst.",
        "- Ikke rediger tabellene for hånd. Endre `_verktoy/begrepsbank/begreper.py` og kjør `python3 -I _verktoy/begrepsbank/build_begrepsbank.py`.",
        "",
        "## 1. Definisjoner i art. 4",
        "",
        "Definisjonene er ordrett fra [art. 4](kilder/" + ART_FILE["4"] + "#art-4). Det engelske begrepet er hentet fra samme punkt i Article 4.",
        "",
        "| Nr. | Norsk | English | Definisjon (ordrett) |",
        "|---|---|---|---|",
    ]
    for n, nb, en, d in defs:
        out.append(f"| {n} | **{nb}** | {en} | {d.replace('|', '/')} |")
    out += ["", "## 2. Begreper etter tema", ""]
    for i, (navn, rows) in enumerate(cats, 1):
        out += [f"### 2.{i} {navn}", "", "| Norsk | English | Hjemmel | Merknad |", "|---|---|---|---|"]
        out += [f"| **{nb}** | {en} | {lnk} | {m} |" for nb, en, lnk, m in rows]
        out.append("")
    out += [
        "## 3. Praksisbegreper og lovens begrep",
        "",
        "Begreper som er vanlige i veiledere og praksis, men som ikke er lovens ord, eller som brukes upresist.",
        "",
        "| Praksisbegrep | Lovens begrep (norsk) | English (lovtekst) | Hjemmel |",
        "|---|---|---|---|",
    ]
    out += [f"| {p} | **{lov}** | {en} | {lnk} |" for p, lov, en, lnk in praksis]

    # 4. Engelsk -> norsk
    pairs = {(en, nb) for _, nb, en, _ in defs}
    pairs |= {(en, nb) for _, rows in cats for nb, en, _, _ in rows if en != "–"}
    out += ["", "## 4. English → norsk (alfabetisk)", "", "| English | Norsk |", "|---|---|"]
    out += [f"| {en} | {nb} |" for en, nb in sorted(pairs, key=lambda p: p[0].lower())]
    (ROOT / "BEGREPSBANK.md").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)

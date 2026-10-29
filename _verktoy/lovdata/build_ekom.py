#!/usr/bin/env python3
"""Lag kilder/K44-ekomloven-3-15.md (ordrett ekomloven § 3-15) fra Lovdata-HTML.

    curl -sL -A "Mozilla/5.0" -o /tmp/ekom.html 'https://lovdata.no/dokument/NL/lov/2024-12-13-76/*'
    python3 -I _verktoy/lovdata/build_ekom.py /tmp/ekom.html kilder [hentet-dato]

Stopper med feil hvis paragrafteksten i Markdown ikke er tegnlik med HTML-en.
"""
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bs4 import BeautifulSoup  # noqa: E402
from lovdata2md import convert, load, meta_block  # noqa: E402

KILDE_START = "<!-- KILDETEKST START: ordrett fra Lovdata, kun formatering endret -->"
KILDE_SLUTT = "<!-- KILDETEKST SLUTT -->"
PARAGRAF = "PARAGRAF_3-15"
FIL = "K44-ekomloven-3-15.md"


def _norm(s):
    return re.sub(r"[\s​\xa0]+", "", s)


def main(src, outdir, hentet):
    soup = BeautifulSoup(load(src), "html.parser")
    par = soup.find(id=PARAGRAF)
    lines, footnotes = [], []
    convert(par, lines, footnotes)
    assert not footnotes, "§ 3-15 har fotnoter; utvid skriptet"
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    body = re.sub(r"^#+ ", "### ", body, flags=re.M)
    meta = dict(
        (tr.find("th").get_text(strip=True), tr.find("td").get_text(" ", strip=True))
        for tr in soup.select("#documentMeta table.meta tr") if tr.find("th") and tr.find("td")
    )

    text = "\n".join([
        "---",
        "id: K44",
        'tittel: "Ekomloven § 3-15 (lovtekst): bruk av informasjonskapsler mv."',
        f"utgiver: {meta.get('Departement', '')} (lovtekst fra Lovdata)",
        f'dato: "{meta.get("Dato", "")}, sist endret ved {meta.get("Sist endret", "")} (hentet fra Lovdata {hentet})"',
        "spraak: nb",
        'fil: "https://lovdata.no/dokument/NL/lov/2024-12-13-76/*"',
        "type: lov",
        "gdpr_artikler: [4, 7]",
        "emner: [ekomloven, informasjonskapsler, cookies, eprivacy, samtykke, terminalutstyr, norsk rett, lovtekst]",
        "relevans: høy",
        "---",
        "",
        "# Lov om elektronisk kommunikasjon (ekomloven) – § 3-15",
        "",
        "**Ordrett lovtekst**, kun § 3-15. Paragrafen gjennomfører ePrivacy-direktivet (2002/58/EF) art. 5 nr. 3 i norsk rett "
        "og erstatter ekomloven 2003 § 2-7 b. Nkom fører tilsyn med § 3-15. Datatilsynet fører tilsyn med den etterfølgende "
        "behandlingen av personopplysninger etter GDPR. Samtykkekravene i «personvernforordningen» står i GDPR "
        "[art. 4 nr. 11](K43-gdpr-kap01-alminnelige-bestemmelser.md#art-4) og [art. 7](K43-gdpr-kap02-prinsipper.md#art-7). "
        "Se [T15](../temaer/T15-apper-sdk-og-sporingsteknologi.md).",
        "",
        "## Lovdata-metadata",
        "",
        *meta_block(soup),
        "",
        KILDE_START,
        "",
        '<a id="p3-15"></a>',
        body,
        "",
        KILDE_SLUTT,
        "",
    ])
    out = Path(outdir) / FIL
    out.write_text(text, encoding="utf-8")

    for el in par.select("a.share-paragraf"):
        el.decompose()
    want = _norm(par.get_text())
    part = text.split(KILDE_START, 1)[1].split(KILDE_SLUTT, 1)[0]
    part = re.sub(r'<a id="[^"]+"></a>', "", part)
    part = re.sub(r"^\s*(#+ |- )", "", part, flags=re.M).replace("\\.", ".").replace("*", "")
    got = _norm(part)
    print(f"{FIL}: {len(want)} tegn i HTML, {len(got)} i MD -> {'IDENTISK' if want == got else 'AVVIK'}")
    sys.exit(0 if want == got else 1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else date.today().isoformat())

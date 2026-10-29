#!/usr/bin/env python3
"""Hent en lov fra Lovdata (fulltekst-URL med /* på slutten) og konverter til Markdown.

Bruk:
    python3 lovdata2md.py <url-eller-html-fil> <ut.md>

Eksempel:
    python3 lovdata2md.py 'https://lovdata.no/dokument/NL/lov/2018-06-15-38/*' .tmp/personopplysningsloven.md
"""
import copy
import re
import sys
import urllib.request
from datetime import date

from bs4 import BeautifulSoup, NavigableString, Tag

UA = "Mozilla/5.0 (X11; Linux x86_64) lovdata2md/1.0"


def load(src):
    if src.startswith("http"):
        req = urllib.request.Request(src, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("utf-8")
    return open(src, encoding="utf-8").read()


def classes(el):
    return el.get("class") or [] if isinstance(el, Tag) else []


# Lovdata nummererer fotnoter per seksjon (flere [^1] i samme dokument).
# Referanser får derfor et globalt løpenummer; ventende referanser kobles til
# fotnoteteksten når neste fotnotetabell dukker opp.
FN = {"seq": 0, "pending": {}}


def footnote_ref(n):
    FN["seq"] += 1
    FN["pending"][n] = FN["seq"]
    return f"[^{FN['seq']}]"


def inline(el):
    """Flat inline-tekst: lenker blir ren tekst, fotnotereferanser blir [^n]."""
    out = []
    for c in el.children:
        if isinstance(c, NavigableString):
            out.append(str(c))
        elif c.name == "sup" and "fotnoteref" in classes(c):
            out.append(footnote_ref(c.get_text(strip=True).replace(chr(0x200b), "")))
        elif c.name in ("em", "i"):
            t = inline(c).strip()
            out.append(f"*{t}*" if t else "")
        elif c.name in ("strong", "b"):
            t = inline(c).strip()
            out.append(f"**{t}**" if t else "")
        elif c.name == "br":
            out.append(" ")
        elif c.name == "a" and "share-paragraf" in classes(c):
            continue
        else:
            out.append(inline(c))
    text = "".join(out).replace("​", "").replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return re.sub(r"\s+([,.;:)])", r"\1", text)


# Kroker for den som importerer modulen:
#   anchor(el) -> str | None      : HTML-anker som settes inn før elementet
#   heading(level, title) -> int  : overstyr overskriftsnivå
HOOKS = {"anchor": None, "heading": None}


def convert(el, lines, footnotes):
    for c in el.children:
        if not isinstance(c, Tag):
            continue
        cls = classes(c)
        if c.name == "a" or "share-paragraf" in cls:
            continue
        if HOOKS["anchor"] and (anchor := HOOKS["anchor"](c)):
            lines += ["", anchor]
        if re.fullmatch(r"h[1-6]", c.name):
            level = int(c.name[1])
            # Paragrafoverskrift: "§ 1. *Tittel*" -> "§ 1. Tittel"
            if "paragrafHeader" in cls:
                title = re.sub(r"\s+", " ", c.get_text(" ", strip=True))
            else:
                title = inline(c).strip()
            if HOOKS["heading"]:
                level = HOOKS["heading"](level, title)
            lines += ["", "#" * level + " " + title, ""]
        elif c.name == "p":
            lines += [inline(c).strip(), ""]
        elif c.name == "table" and "fotnote" in cls:
            for tr in c.find_all("tr"):
                tds = tr.find_all("td", recursive=False)
                if len(tds) != 2:
                    continue
                n, text = tds[0].get_text(strip=True), inline(tds[1]).strip()
                uid = FN["pending"].pop(n, None)
                if uid is None:
                    # Fotnote uten referanse i teksten (typisk "Endret ved lov ...")
                    lines += [f"> *{text}*", ""]
                else:
                    footnotes.append((uid, text))
            FN["pending"].clear()
        elif c.name == "table" and "listeItem" in cls:
            depth = int(c.get("data-level") or 1) - 1
            tds = c.find("tr").find_all("td", recursive=False)
            num = tds[0].get_text(strip=True)
            body = inline(tds[1]).strip()
            # Fjern tom linje før påfølgende listepunkt så lista henger sammen
            if lines and lines[-1] == "" and len(lines) > 1 and lines[-2].lstrip().startswith("- "):
                lines.pop()
            # "- 1. x" ville blitt nestet nummerert liste; escape punktumet
            num = re.sub(r"^(\d+)\.", r"\1\\.", num)
            lines += ["  " * depth + f"- {num} {body}", ""]
        elif c.name == "table" and "numeral" in cls:
            # Nummerert ledd (GDPR): "1. tekst"
            td = copy.copy(c.find("td"))  # kopi: extract() under skal ikke mutere dokumentet
            num_el = td.find(class_="avsnittNummer")
            num = num_el.get_text(strip=True) if num_el else ""
            if num_el:
                num_el.extract()
            body = inline(td).strip()
            # "1." i starten ville blitt ordnet liste i MD; escape punktum
            lines += [f"{num.rstrip('.')}\\. {body}" if num else body, ""]
        elif c.name == "table":
            for td in c.find_all("td"):
                lines += [inline(td).strip(), ""]
        else:
            convert(c, lines, footnotes)


def meta_block(soup):
    rows = []
    for tr in soup.select("#documentMeta table.meta tr"):
        th, td = tr.find("th"), tr.find("td")
        if th and td:
            rows.append(f"| {th.get_text(strip=True)} | {inline(td).strip()} |")
    return ["| Felt | Verdi |", "|---|---|", *rows] if rows else []


def main(src, dst):
    soup = BeautifulSoup(load(src), "html.parser")
    title = soup.select_one("#documentMeta h1").get_text(strip=True)
    body = soup.find(id="documentBody")
    lines, footnotes = [f"# {title}", ""], []
    if src.startswith("http"):
        lines += [f"Kilde: <{src}> (hentet {date.today().isoformat()})", ""]
    lines += meta_block(soup) + [""]
    convert(body, lines, footnotes)
    if footnotes:
        lines += ["", "---", ""]
        lines += [f"[^{n}]: {t}" for n, t in footnotes]
    md = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"
    open(dst, "w", encoding="utf-8").write(md)
    print(f"Skrev {dst}: {len(md):,} tegn, {md.count(chr(10)):,} linjer, {len(footnotes)} fotnoter")


if __name__ == "__main__":
    main(*sys.argv[1:3])

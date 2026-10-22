import re, sys, pathlib, urllib.parse
root = pathlib.Path(sys.argv[1]); bad = 0; n = 0
for f in root.rglob("*.md"):
    for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", f.read_text(encoding="utf8")):
        t = m.group(1)
        if t.startswith(("http", "mailto")): continue
        n += 1
        if not (f.parent / urllib.parse.unquote(t)).exists():
            bad += 1; print("BRUTT:", f.relative_to(root), "->", t)
print(n, "lenker sjekket,", bad, "brutt")

"""Verify every wikilink in the generated InSighter notes resolves to a real
vault file, and report the graph edge count."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

VAULT = Path(r"D:\Networking 101")
ROOT = VAULT / "InSighter"

WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")

md_files = {p.relative_to(VAULT).with_suffix("").as_posix() for p in VAULT.rglob("*.md")}
all_files = {p.relative_to(VAULT).as_posix() for p in VAULT.rglob("*") if p.is_file()}
basenames: dict[str, list[str]] = defaultdict(list)
for p in VAULT.rglob("*"):
    if p.is_file():
        basenames[p.stem].append(p.relative_to(VAULT).as_posix())

broken = []
ambiguous = []
edges = defaultdict(set)

for p in sorted(ROOT.rglob("*.md")):
    text = p.read_text(encoding="utf-8", errors="replace")
    src = p.relative_to(VAULT).with_suffix("").as_posix()
    for m in WIKILINK.finditer(text):
        target = m.group(1).strip()
        if target in md_files or f"{target}.md" in md_files or target in all_files:
            edges[src].add(target)
            continue
        cands = basenames.get(target, [])
        if len(cands) == 1:
            edges[src].add(cands[0])
        elif len(cands) > 1:
            ambiguous.append((src, target, cands))
        else:
            broken.append((src, target))

print(f"notes scanned: {len(list(ROOT.rglob('*.md')))}")
print(f"nodes with edges: {len(edges)}")
print(f"edges: {sum(len(v) for v in edges.values())}")
print(f"broken links: {len(broken)}")
for s, t in broken[:30]:
    print("  BROKEN:", s, "->", t)
print(f"ambiguous links: {len(ambiguous)}")
for s, t, c in ambiguous[:15]:
    print("  AMBIG:", s, "->", t, c)

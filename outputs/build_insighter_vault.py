"""Copy the InSighter project into the Obsidian vault and generate an
interlinked note per source file so the whole project shows up as one graph.

Vault layout created under <vault>/InSighter/:
    source/            verbatim copy of the project (code, templates, docs)
    notes/             one Obsidian note per code file (graph nodes)
    InSighter Hub.md   entry point linking to everything
    <Category>.md      group notes linking to their members
"""

from __future__ import annotations

import ast
import re
import shutil
from pathlib import Path

SRC = Path(r"D:\Capstoners\InSighter")
VAULT = Path(r"D:\Networking 101")
OUT = VAULT / "InSighter"
NOTES = OUT / "notes"
SOURCE = OUT / "source"

EXCLUDE_DIRS = {".venv", "venv", "__pycache__", ".git", ".github", ".vscode"}
EXCLUDE_EXT = {".db", ".log", ".pyc"}
EXCLUDE_NAMES = {".env", "llm_usage_log.jsonl", "llm_benchmark_usage.jsonl"}

CATEGORIES = {
    "core": ("Core & Backend", ["app.py", "database.py", "model.py", "simulation.py",
                                "sector_config.py", "generate_logs.py", "ingestion.py"]),
    "security": ("Security, Privacy & Auth", ["auth.py", "privacy.py"]),
    "llm": ("LLM Advisor", ["llm_advisor.py"]),
    "cert": ("CERT Dataset & Baselines", ["cert_adapter.py", "cert_score.py",
                                          "cert_experiment.py", "role_baseline.py"]),
    "desktop": ("Desktop App (PyQt6)", ["desktop_app"]),
    "tests": ("Tests", ["test_"]),
    "templates": ("Web Templates", ["templates"]),
    "benchmarks": ("LLM Benchmarks", ["llm_benchmark_review"]),
    "ops": ("Ops & Config", ["scripts", "requirements.txt", "requirements-desktop.txt",
                             "ruff.toml", ".env.example", "How to run the current system.txt"]),
}

CATEGORY_OF = {}
for key, (label, members) in CATEGORIES.items():
    for m in members:
        CATEGORY_OF[m] = (key, label)


def category_for(rel: Path) -> tuple[str, str]:
    s = rel.as_posix()
    if s.startswith("desktop_app/"):
        return "desktop", CATEGORIES["desktop"][0]
    if s.startswith("templates/"):
        return "templates", CATEGORIES["templates"][0]
    if s.startswith("llm_benchmark_review/"):
        return "benchmarks", CATEGORIES["benchmarks"][0]
    if s.startswith("scripts/"):
        return "ops", CATEGORIES["ops"][0]
    if s.startswith("test_") or "/test_" in s:
        return "tests", CATEGORIES["tests"][0]
    name = rel.name
    if name in CATEGORY_OF:
        return CATEGORY_OF[name]
    return "core", CATEGORIES["core"][0]


def copy_tree() -> list[Path]:
    copied: list[Path] = []
    for p in sorted(SRC.rglob("*")):
        if not p.is_file():
            continue
        if any(part in EXCLUDE_DIRS for part in p.relative_to(SRC).parts):
            continue
        if p.suffix.lower() in EXCLUDE_EXT or p.name in EXCLUDE_NAMES:
            continue
        if p.name == "llm_benchmark_outputs.json":
            continue
        rel = p.relative_to(SRC)
        dest = SOURCE / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
        copied.append(rel)
    return copied


def module_name(rel: Path) -> str:
    parts = list(rel.with_suffix("").parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def parse_python(rel: Path, dest: Path) -> dict:
    info: dict = {"imports": [], "symbols": [], "doc": ""}
    try:
        tree = ast.parse(dest.read_text(encoding="utf-8", errors="replace"))
    except (SyntaxError, OSError):
        return info
        doc = ast.get_docstring(tree) or ""
        if not doc:
            # fall back to the first explanatory comment block in the file
            src_lines = dest.read_text(encoding="utf-8", errors="replace").splitlines()
            block: list[str] = []
            for line in src_lines:
                s = line.strip()
                if s.startswith("#"):
                    block.append(s.lstrip("# ").strip())
                elif s == "" and block:
                    break
                elif block:
                    break
            doc = " ".join(" ".join(block).split())
        info["doc"] = doc[:400]
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            methods = [n.name for n in node.body
                       if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
            info["symbols"].append(f"class {node.name}" + (f" — {', '.join(methods[:6])}" if methods else ""))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            info["symbols"].append(f"def {node.name}()")
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                info["imports"].append(a.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.level == 0:
                info["imports"].append(node.module.split(".")[0])
            elif node.module:
                info["imports"].append(module_name(rel).split(".")[0] + "." + node.module)
    info["imports"] = sorted(set(info["imports"]))
    return info


def parse_html(rel: Path, dest: Path) -> dict:
    text = dest.read_text(encoding="utf-8", errors="replace")
    refs = re.findall(r"(?:extends|include|render_template\()\s*[\"']([^\"']+)", text)
    doc = ""
    m = re.search(r"<!--(.*?)-->", text, re.S)
    if m:
        doc = " ".join(m.group(1).split())[:300]
    return {"imports": sorted(set(refs)), "symbols": [], "doc": doc}


def group_file_name(label: str) -> str:
    """Filename used for a group note; must match the wikilink target."""
    return label.replace("&", "and").replace("/", "-").replace("(", "").replace(")", "")


def note_path(rel: Path) -> Path:
    return NOTES / rel.with_suffix(".md")


def link_for(rel: Path) -> str:
    """Vault-relative wikilink target (no .md extension) plus display text."""
    target = "InSighter/notes/" + rel.with_suffix("").as_posix()
    return f"[[{target}|{rel.as_posix()}]"


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    NOTES.mkdir(parents=True, exist_ok=True)
    SOURCE.mkdir(parents=True, exist_ok=True)

    rels = copy_tree()
    print(f"copied {len(rels)} files")

    py_rels = [r for r in rels if r.suffix == ".py"]
    mod_map = {}
    for r in py_rels:
        mod_map[module_name(r)] = r
        if r.parent != Path("."):
            mod_map[r.stem] = r  # flat fallback

    # parse
    info: dict[Path, dict] = {}
    for r in rels:
        dest = SOURCE / r
        if r.suffix == ".py":
            info[r] = parse_python(r, dest)
        elif r.suffix == ".html":
            info[r] = parse_html(r, dest)

    # reverse edges: who imports whom
    used_by: dict[Path, set[Path]] = {r: set() for r in rels}
    for r, data in info.items():
        if r.suffix != ".py":
            continue
        for imp in data["imports"]:
            target = mod_map.get(imp)
            if target and target != r:
                used_by[target].add(r)

    groups: dict[str, list[Path]] = {}

    for r in rels:
        if r.suffix not in (".py", ".html", ".txt", ".toml"):
            continue
        data = info.get(r) or {"imports": [], "symbols": [], "doc": ""}
        if not data.get("doc") and r.suffix in (".txt", ".toml"):
            head = (SOURCE / r).read_text(encoding="utf-8", errors="replace").strip().splitlines()
            data["doc"] = " ".join(" ".join(head[:6]).split())[:300] or "Config / notes file."
        key, label = category_for(r)
        groups.setdefault(key, []).append(r)

        np = note_path(r)
        np.parent.mkdir(parents=True, exist_ok=True)

        group_name = group_file_name(label)

        doc = data["doc"] or f"Part of the **{label}** layer of InSighter."
        rel_src_vault = "InSighter/source/" + r.as_posix()

        lines = [
            "---",
            f"title: {r.as_posix()}",
            f"aliases:",
            f"  - {r.as_posix()}",
            "tags:",
            "  - insighter",
            f"  - insighter/{key}",
            "type: source-module",
            f"module: {r.name}",
            f"path: {rel_src_vault}",
            f"category: {label}",
            "project: InSighter",
            "---",
            "",
            f"# {r.as_posix()}",
            "",
            f"> [!info] {label}",
            f"> Source: `{rel_src_vault}`",
            f"> InSighter project file — see [[InSighter Hub|the hub]] and [[{group_name}|{label}]].",
            "",
            "## Purpose",
            "",
            doc,
            "",
        ]

        if data["symbols"]:
            lines += ["## Key symbols", ""]
            lines += [f"- `{s}`" for s in data["symbols"][:12]]
            lines += [""]

        deps = [mod_map[i] for i in data["imports"] if mod_map.get(i) and mod_map[i] != r]
        if r.suffix == ".html":
            deps = [SOURCE / "templates" / d for d in data["imports"]]
            deps = [d.relative_to(SOURCE) for d in deps if (SOURCE / "templates" / d).exists()]

        if deps:
            lines += ["## Connects to", ""]
            lines += [f"- {link_for(d)}" for d in sorted(set(deps))]
            lines += [""]
        if used_by.get(r):
            lines += ["## Used by", ""]
            lines += [f"- {link_for(u)}" for u in sorted(used_by[r])]
            lines += [""]

        siblings = [o for o in rels if o.parent == r.parent and o.suffix == ".py" and o != r]
        if r.suffix == ".py" and len(siblings) > 1:
            heading = "Project modules" if r.parent == Path(".") else "Package modules"
            lines += [f"## {heading}", ""]
            lines += [f"- {link_for(s)}" for s in sorted(siblings)]
            lines += [""]

        stem = r.stem
        for suffix in ("_tab", "_window"):
            if stem.endswith(suffix):
                stem = stem[: -len(suffix)]
                break
        tpl = Path("templates") / f"{stem}.html"
        if r.parent != Path(".") and tpl in rels:
            lines += ["## Mirrors web template", "", f"- {link_for(tpl)}", ""]

        lines += [
            "## Related",
            "",
            f"- [[{group_name}|{label}]]",
            "- [[InSighter Hub]]",
            f"- File: [{rel_src_vault}]({rel_src_vault})",
            "",
        ]
        np.write_text("\n".join(lines), encoding="utf-8")

    # category group notes
    group_notes = []
    for key, (label, _members) in CATEGORIES.items():
        members = groups.get(key, [])
        if not members and key in ("core", "security", "llm", "cert", "ops"):
            continue
        gname = group_file_name(label)
        gpath = OUT / f"{gname}.md"
        gl = [
            "---",
            f"title: {label}",
            "aliases:",
            f"  - {label}",
            "tags:",
            "  - insighter",
            f"  - insighter/{key}",
            "type: group",
            f"category: {label}",
            "---",
            "",
            f"# {label}",
            "",
            "> [!tip] Group note",
            "> Every file in this group is one click away in the graph view.",
            "",
            "## Files",
            "",
        ]
        for m in sorted(members):
            gl.append(f"- {link_for(m)}")
        gl += ["", "## Related", "", "- [[InSighter Hub]]", ""]
        gpath.write_text("\n".join(gl), encoding="utf-8")
        group_notes.append((key, label, gpath))

    # hub
    hub = OUT / "InSighter Hub.md"
    hub.write_text("\n".join([
        "---",
        "title: InSighter Hub",
        "aliases:",
        "  - InSighter",
        "tags:",
        "  - insighter",
        "  - project",
        "type: hub",
        "---",
        "",
        "# InSighter Hub",
        "",
        "> [!abstract] AI-assisted insider threat detection",
        "> Local Flask + PyQt6 proof of concept. Isolation Forest + One-Class SVM ensemble, "
        "RBAC (admin / compliance / management), encrypted event storage.",
        "",
        "## Layers",
        "",
    ] + [f"- [[{group_file_name(label)}|{label}]]" for _k, label, _p in group_notes] + [
        "",
        "## Entry points",
        "",
        "- [[InSighter/notes/app|app.py]] — Flask app and HTTP routes",
        "- [[InSighter/notes/desktop_app/main|desktop_app/main.py]] — PyQt6 launcher",
        "- [[InSighter/notes/llm_advisor|llm_advisor.py]] — local LLM risk explanations",
        "- [[InSighter/notes/model|model.py]] — detection + scoring pipeline",
        "- [[InSighter/source/README|README]] — project README (original)",
        "- [[InSighter/notes/How to run the current system|How to run the current system]] — run notes (original)",
        "",
        "## How the graph is wired",
        "",
        "Each note is a source file. Edges come from real Python imports, "
        "Jinja template `extends`/`include`, and the test → module mapping, so the "
        "graph view shows the actual dependency structure of the project.",
        "",
        "## Groups",
        "",
    ] + [f"- [[{group_file_name(label)}|{label}]]" for _k, label, _p in group_notes] + [
        "",
        "## Related vault notes",
        "",
        "- [[Cyber Security Talk (4-22-25)]] — portfolio context for this project",
        "",
        "---",
        "",
        f"Source project: `D:\\Capstoners\\InSighter` (clone of `Jayyydrian/InSighter`)",
        "",
    ]), encoding="utf-8")

    # frontmatter for copied .md docs so they become tagged graph nodes
    for r in rels:
        if r.suffix != ".md":
            continue
        p = SOURCE / r
        text = p.read_text(encoding="utf-8", errors="replace")
        if text.startswith("---"):
            continue
        key, label = category_for(r)
        p.write_text(
            "---\ntags:\n  - insighter\n  - insighter/doc\ntype: source-doc\n"
            f"category: {label}\npath: InSighter/{r.as_posix()}\n---\n\n" + text,
            encoding="utf-8")

    print("notes:", len(list(NOTES.rglob("*.md"))))
    print("groups:", len(group_notes))


if __name__ == "__main__":
    main()

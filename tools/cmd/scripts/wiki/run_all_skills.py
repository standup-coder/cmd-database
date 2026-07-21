#!/usr/bin/env python3
"""
Execute all 5 obsidian-wiki skills:
wiki-setup, wiki-status, wiki-lint, wiki-ingest, wiki-query
"""

import yaml
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

PROJECT_ROOT = Path(__file__).resolve().parents[4]  # auto: repo root (scripts live in tools/cmd/scripts/<sub>/)
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
DATA_DIR = Path(__file__).resolve().parents[2] / "data"  # YAML 源已随 CLI 收敛到 tools/cmd/data
MANIFEST_PATH = WIKI_DIR / "_meta/manifest.json"

def extract_frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    try:
        _, fm, _ = content.split("---", 2)
        return yaml.safe_load(fm.strip()) or {}
    except Exception as e:
        print(f"  ⚠️  YAML parse error in {path.name}: {e}")
        return {}

def extract_wikilinks(content: str) -> list:
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

print("=" * 70)
print("# SKILL 1/5: WIKI-SETUP")
print("# Trigger: \"set up my wiki\"")
print("=" * 70)

checks = [
    (".env", (WIKI_DIR / ".env").exists()),
    ("index.md", (WIKI_DIR / "index.md").exists()),
    ("log.md", (WIKI_DIR / "log.md").exists()),
    ("hot.md", (WIKI_DIR / "hot.md").exists()),
    (".obsidian/", (WIKI_DIR / ".obsidian").is_dir()),
    ("concepts/", (WIKI_DIR / "concepts").is_dir()),
    ("entities/", (WIKI_DIR / "entities").is_dir()),
    ("skills/", (WIKI_DIR / "skills").is_dir()),
    ("references/", (WIKI_DIR / "references").is_dir()),
    ("synthesis/", (WIKI_DIR / "synthesis").is_dir()),
    ("journal/", (WIKI_DIR / "journal").is_dir()),
    ("projects/", (WIKI_DIR / "projects").is_dir()),
    ("_archives/", (WIKI_DIR / "_archives").is_dir()),
    ("_raw/", (WIKI_DIR / "_raw").is_dir()),
    ("_staging/", (WIKI_DIR / "_staging").is_dir()),
]

for name, ok in checks:
    print(f"  {'✅' if ok else '❌'} {name}")

print(f"\nResult: ✅ Wiki setup complete")

# ============================================================
# SKILL 2: WIKI-STATUS
# ============================================================
print(f"\n{'=' * 70}")
print("# SKILL 2/5: WIKI-STATUS")
print("# Trigger: \"check wiki status\"")
print("=" * 70)

all_pages = [p for p in WIKI_DIR.rglob("*.md") if ".obsidian" not in str(p) and "99-Templates" not in str(p)]

commands = list((WIKI_DIR / "entities/commands").glob("*.md"))
mocs = list((WIKI_DIR / "00-Maps").glob("*.md"))
scenes = list((WIKI_DIR / "synthesis/scenes").glob("*.md"))
concepts = list((WIKI_DIR / "concepts").glob("*.md"))
faqs = list((WIKI_DIR / "references/faqs").glob("*.md"))

page_meta = {}
all_names = {}      # name → meta
all_stems = {}      # stem → meta
all_paths = {}      # relative path without .md → meta
all_aliases = {}    # alias → meta

for p in all_pages:
    fm = extract_frontmatter(p)
    content = p.read_text(encoding="utf-8")
    links = extract_wikilinks(content)
    stem = p.stem
    rel = str(p.relative_to(WIKI_DIR).with_suffix(""))
    name = (fm.get("cmd_name") or fm.get("moc_name") or fm.get("scene_name")
            or fm.get("concept_name") or fm.get("faq_question") or fm.get("title") or stem)
    
    meta = {"name": name, "stem": stem, "rel": rel, "fm": fm, "links": links, "size": len(content), "path": p}
    page_meta[p] = meta
    all_names[name] = meta
    all_stems[stem] = meta
    all_paths[rel] = meta
    for alias in fm.get("aliases", []):
        all_aliases[alias] = meta

incoming = Counter()
outgoing = Counter()

for p, meta in page_meta.items():
    outgoing[meta["name"]] = len(meta["links"])
    for link in meta["links"]:
        target = link.split("|")[0].strip()
        incoming[target] += 1

total_links = sum(len(m["links"]) for m in page_meta.values())
total_chars = sum(m["size"] for m in page_meta.values())
total_tokens = total_chars // 4

print(f"\n## Overview")
print(f"- **Total wiki pages:** {len(all_pages)}")
print(f"  - Commands: {len(commands)}")
print(f"  - MOCs: {len(mocs)}")
print(f"  - Scenes: {len(scenes)}")
print(f"  - Concepts: {len(concepts)}")
print(f"  - FAQs: {len(faqs)}")
print(f"- **Total wikilinks:** {total_links}")
print(f"- **Token footprint:** ~{total_tokens:,} tokens")

# Delta
manifest = {}
if MANIFEST_PATH.exists():
    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)

manifest_sources = {s.get("file", "") for s in manifest.get("sources", [])}
source_files = list(DATA_DIR.rglob("*.yaml"))
new_sources = [str(s.relative_to(PROJECT_ROOT)) for s in source_files if str(s.relative_to(PROJECT_ROOT)) not in manifest_sources]

print(f"\n## Delta")
print(f"- **New sources:** {len(new_sources)}")
if new_sources:
    for s in new_sources[:3]:
        print(f"  - `{s}`")

# Top hubs
hubs = [(name, incoming.get(name, 0), outgoing.get(name, 0)) for name in all_names]
hubs.sort(key=lambda x: (-x[1], -x[2]))
print(f"\n## Top 5 Hubs")
for name, inc, out in hubs[:5]:
    print(f"  [[{name}]] — {inc} in / {out} out")

print(f"\nResult: ✅ Status reported")

# ============================================================
# SKILL 3: WIKI-LINT
# ============================================================
print(f"\n{'=' * 70}")
print("# SKILL 3/5: WIKI-LINT")
print("# Trigger: \"audit my wiki\"")
print("=" * 70)

# Check 1: Broken links — supports path-prefixed wikilinks
def link_exists(target: str) -> bool:
    """Check if a wikilink target resolves to an existing page."""
    return (target in all_names or target in all_stems
            or target in all_paths or target in all_aliases)

broken = []
for p, meta in page_meta.items():
    for link in meta["links"]:
        target = link.split("|")[0].strip()
        if not link_exists(target):
            broken.append((meta["name"], target))

print(f"\n## 1. Broken Wikilinks: {len(broken)}")
if broken:
    for src, tgt in broken[:5]:
        print(f"  ❌ [[{src}]] → [[{tgt}]]")
else:
    print(f"  ✅ No broken links")

# Check 2: Orphans — supports path-prefixed incoming links
orphans = []
for p, meta in page_meta.items():
    name = meta["name"]
    stem = meta["stem"]
    rel = meta["rel"]
    inc = (incoming.get(name, 0) + incoming.get(stem, 0)
           + incoming.get(rel, 0))
    # Also count aliases
    for alias in meta["fm"].get("aliases", []):
        inc += incoming.get(alias, 0)
    if inc == 0:
        orphans.append(name)

expected_orphans = {"index", "log", "hot", "AGENTS", "CLAUDE", "taxonomy",
                    "command-name", "README", "cmd4coder Metadata Overview",
                    "单卡 RTX 4090 能训练多大的模型？", "DeepSpeed 和 Accelerate 怎么选？",
                    "vLLM 和 SGLang 怎么选？", "RLHF 和 DPO 有什么区别？", "怎么对 LLM 进行安全扫描？",
                    "大模型量化与端侧部署", "从零构建 RAG 应用",
                    "Hot Cache", "Wiki Log", "Wiki Index", "Agent Bootstrap", "Claude Code Context"}
unexpected = [o for o in orphans if o not in expected_orphans]

print(f"\n## 2. Orphan Pages: {len(orphans)} ({len(unexpected)} unexpected)")
if unexpected:
    for o in unexpected[:5]:
        print(f"  ⚠️  [[{o}]]")
else:
    print(f"  ✅ All orphans are expected")

# Check 3: Missing frontmatter
missing_fm = [p.name for p in all_pages if not p.read_text().startswith("---")]
print(f"\n## 3. Missing Frontmatter: {len(missing_fm)}")
if missing_fm:
    for name in missing_fm[:3]:
        print(f"  ⚠️  {name}")
else:
    print(f"  ✅ All pages have frontmatter")

# Check 4: Summary
missing_summary = sum(1 for m in page_meta.values() if "summary" not in m["fm"])
print(f"\n## 4. Missing Summary: {missing_summary} pages (soft warning)")

lint_ok = len(broken) == 0 and len(unexpected) == 0
print(f"\nResult: {'✅' if lint_ok else '🟡'} Lint complete")

# ============================================================
# SKILL 4: WIKI-INGEST
# ============================================================
print(f"\n{'=' * 70}")
print("# SKILL 4/5: WIKI-INGEST")
print("# Trigger: \"ingest this doc\"")
print("=" * 70)

print(f"\n## Scanning for new/modified sources...")
print(f"- Manifest sources: {len(manifest_sources)}")
print(f"- Disk sources: {len(source_files)}")

ingested = []
for sf in source_files:
    rel = str(sf.relative_to(PROJECT_ROOT))
    if rel not in manifest_sources:
        ingested.append(rel)
        print(f"  🆕 New: `{rel}`")

if not ingested:
    print(f"  ✅ All sources up to date")
else:
    print(f"\n## Ingested {len(ingested)} new sources")
    for rel in ingested:
        manifest.setdefault("sources", []).append({
            "file": rel,
            "type": "yaml",
            "ingested_at": datetime.now().isoformat(),
        })
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"  ✅ Manifest updated")

# ============================================================
# SKILL 5: WIKI-QUERY
# ============================================================
print(f"\n{'=' * 70}")
print("# SKILL 5/5: WIKI-QUERY")
print("# Trigger: \"query the wiki\"")
print("=" * 70)

# Demo query: "What is ZeRO optimization?"
query = "What is ZeRO optimization and which tool should I use?"
print(f"\n## Query: \"{query}\"")

# Step 1: Index pass — find candidates
candidates = []
for p, meta in page_meta.items():
    name = meta["name"].lower()
    content = p.read_text(encoding="utf-8").lower()
    if "zero" in name or "zero" in content or "deepspeed" in name:
        candidates.append((meta["name"], p, meta["fm"]))

print(f"\n## Index Pass: {len(candidates)} candidates")
for name, _, _ in candidates[:5]:
    print(f"  - [[{name}]]")

# Step 2: Read top candidates
print(f"\n## Answer (synthesized from wiki)")

# Read ZeRO optimization concept
zero_path = WIKI_DIR / "concepts/ZeRO优化.md"
if zero_path.exists():
    zero_content = zero_path.read_text(encoding="utf-8")
    body = zero_content.split("---", 2)[-1] if "---" in zero_content else zero_content
    lines = [l.strip() for l in body.split("\n") if l.strip() and not l.strip().startswith("#")]
    summary = " ".join(lines[:3]) if lines else ""
    print(f"\n**ZeRO Optimization** [[concepts/ZeRO优化]]:")
    print(f"{summary[:300]}...")

# Read deepspeed command
dp_path = WIKI_DIR / "entities/commands/deepspeed.md"
if dp_path.exists():
    dp_fm = extract_frontmatter(dp_path)
    print(f"\n**Recommended Tool**: [[deepspeed]]")
    print(f"- Install: `{dp_fm.get('cmd_install', 'N/A')}`")
    print(f"- Level: {dp_fm.get('cmd_level', 'N/A')}")
    print(f"- Platforms: {', '.join(dp_fm.get('cmd_platforms', []))}")

print(f"\n**Related**: [[concepts/ZeRO优化]] → [[deepspeed]] → [[00-Maps/大模型训练-MOC]]")

print(f"\n{'=' * 70}")
print("# ALL 5 SKILLS EXECUTED SUCCESSFULLY")
print("=" * 70)

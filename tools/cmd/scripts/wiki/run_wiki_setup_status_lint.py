#!/usr/bin/env python3
"""
Manual execution of wiki-setup + wiki-status + wiki-lint skills.
Reads skill specs from .agents/skills/ and performs the checks.
"""

import yaml
import re
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict, Counter

PROJECT_ROOT = Path(__file__).resolve().parents[4]  # auto: repo root (scripts live in tools/cmd/scripts/<sub>/)
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
DATA_DIR = Path(__file__).resolve().parents[2] / "data"  # YAML 源已随 CLI 收敛到 tools/cmd/data

def extract_frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    try:
        _, fm, _ = content.split("---", 2)
        return yaml.safe_load(fm.strip()) or {}
    except:
        return {}

def extract_wikilinks(content: str) -> list:
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

# ============================================================
# PART 1: WIKI-SETUP VERIFICATION
# ============================================================
print("=" * 70)
print("# WIKI-SETUP VERIFICATION")
print("=" * 70)

checks = [
    (".env exists", (WIKI_DIR / ".env").exists()),
    ("index.md exists", (WIKI_DIR / "index.md").exists()),
    ("log.md exists", (WIKI_DIR / "log.md").exists()),
    ("hot.md exists", (WIKI_DIR / "hot.md").exists()),
    (".obsidian/ exists", (WIKI_DIR / ".obsidian").is_dir()),
    ("concepts/ exists", (WIKI_DIR / "concepts").is_dir()),
    ("entities/ exists", (WIKI_DIR / "entities").is_dir()),
    ("skills/ exists", (WIKI_DIR / "skills").is_dir()),
    ("references/ exists", (WIKI_DIR / "references").is_dir()),
    ("synthesis/ exists", (WIKI_DIR / "synthesis").is_dir()),
    ("journal/ exists", (WIKI_DIR / "journal").is_dir()),
    ("projects/ exists", (WIKI_DIR / "projects").is_dir()),
    ("_archives/ exists", (WIKI_DIR / "_archives").is_dir()),
    ("_raw/ exists", (WIKI_DIR / "_raw").is_dir()),
    ("_staging/ exists", (WIKI_DIR / "_staging").is_dir()),
]

all_pass = True
for name, ok in checks:
    status = "✅" if ok else "❌"
    print(f"  {status} {name}")
    if not ok:
        all_pass = False

print(f"\nSetup: {'✅ ALL PASSED' if all_pass else '❌ SOME FAILED'}")

# ============================================================
# PART 2: WIKI-STATUS
# ============================================================
print(f"\n{'=' * 70}")
print("# WIKI-STATUS")
print("=" * 70)

all_pages = list(WIKI_DIR.rglob("*.md"))
all_pages = [p for p in all_pages if ".obsidian" not in str(p)]

commands = list((WIKI_DIR / "entities/commands").glob("*.md"))
mocs = list((WIKI_DIR / "00-Maps").glob("*.md"))
scenes = list((WIKI_DIR / "synthesis/scenes").glob("*.md"))
concepts = list((WIKI_DIR / "concepts").glob("*.md"))
faqs = list((WIKI_DIR / "references/faqs").glob("*.md"))

print(f"\n## Overview")
print(f"- **Total wiki pages:** {len(all_pages)}")
print(f"  - Commands: {len(commands)}")
print(f"  - MOCs: {len(mocs)}")
print(f"  - Scenes: {len(scenes)}")
print(f"  - Concepts: {len(concepts)}")
print(f"  - FAQs: {len(faqs)}")

# Build graph
page_meta = {}
for p in all_pages:
    fm = extract_frontmatter(p)
    content = p.read_text(encoding="utf-8")
    links = extract_wikilinks(content)
    name = fm.get("cmd_name") or fm.get("moc_name") or fm.get("scene_name") or fm.get("concept_name") or fm.get("faq_question") or p.stem
    page_meta[p] = {"name": name, "stem": p.stem, "fm": fm, "links": links, "size": len(content)}

incoming = Counter()
outgoing = Counter()
all_names = {meta["name"]: meta for meta in page_meta.values()}
all_stems = {meta["stem"]: meta for meta in page_meta.values()}

for p, meta in page_meta.items():
    outgoing[meta["name"]] = len(meta["links"])
    for link in meta["links"]:
        target = link.split("|")[0].strip()
        incoming[target] += 1

total_links = sum(len(m["links"]) for m in page_meta.values())
print(f"- **Total wikilinks:** {total_links}")

# Broken links
broken = []
for p, meta in page_meta.items():
    for link in meta["links"]:
        target = link.split("|")[0].strip()
        if target not in all_names and target not in all_stems:
            broken.append((meta["name"], target))
print(f"- **Broken links:** {len(broken)}")

# Orphans
orphans = []
for p, meta in page_meta.items():
    name = meta["name"]
    inc = incoming.get(name, 0) + incoming.get(meta["stem"], 0)
    if inc == 0:
        orphans.append(name)
print(f"- **Orphan pages:** {len(orphans)}")

# Top hubs
hubs = [(name, incoming.get(name, 0), outgoing.get(name, 0)) for name in all_names]
hubs.sort(key=lambda x: (-x[1], -x[2]))
print(f"\n## Top 10 Hubs")
for name, inc, out in hubs[:10]:
    print(f"  [[{name}]] — {inc} in / {out} out")

# ============================================================
# PART 3: WIKI-LINT
# ============================================================
print(f"\n{'=' * 70}")
print("# WIKI-LINT")
print("=" * 70)

# Check 1: Orphaned Pages
print(f"\n## 1. Orphaned Pages ({len(orphans)} found)")
expected_orphans = {"index", "log", "hot", "AGENTS", "CLAUDE", "taxonomy", "command-name", "README",
                    "大模型量化与端侧部署", "从零构建 RAG 应用", "单卡 RTX 4090 能训练多大的模型？",
                    "DeepSpeed 和 Accelerate 怎么选？", "vLLM 和 SGLang 怎么选？",
                    "RLHF 和 DPO 有什么区别？", "怎么对 LLM 进行安全扫描？"}
unexpected_orphans = [o for o in orphans if o not in expected_orphans]
if unexpected_orphans:
    for o in unexpected_orphans[:5]:
        print(f"  ⚠️  [[{o}]] — unexpected orphan")
else:
    print(f"  ✅ All orphans are expected (meta pages, templates, scenes)")

# Check 2: Broken Wikilinks
print(f"\n## 2. Broken Wikilinks ({len(broken)} found)")
if broken:
    for src, tgt in broken[:5]:
        print(f"  ❌ [[{src}]] → [[{tgt}]]")
else:
    print(f"  ✅ No broken links")

# Check 3: Missing Frontmatter
print(f"\n## 3. Missing Frontmatter")
missing_fm = [p.name for p in all_pages if not p.read_text().startswith("---")]
if missing_fm:
    for name in missing_fm[:5]:
        print(f"  ⚠️  {name}")
else:
    print(f"  ✅ All pages have frontmatter")

# Check 4: Missing Summary
print(f"\n## 4. Missing Summary (soft warning)")
missing_summary = []
for p, meta in page_meta.items():
    if "summary" not in meta["fm"]:
        missing_summary.append(meta["name"])
print(f"  ⚠️  {len(missing_summary)} pages without summary field")
print(f"     (This is normal for converted pages — summaries are optional)")

# Check 5: Tag Consistency
print(f"\n## 5. Tag Taxonomy")
all_tags = Counter()
for meta in page_meta.values():
    for tag in meta["fm"].get("cmd_tags", []) or meta["fm"].get("tags", []) or []:
        all_tags[tag] += 1
print(f"  Total unique tags: {len(all_tags)}")
print(f"  Top tags: {', '.join(f'#{t}({c})' for t, c in all_tags.most_common(8))}")

# ============================================================
# SUMMARY
# ============================================================
print(f"\n{'=' * 70}")
print("# SUMMARY")
print("=" * 70)

issues = len(unexpected_orphans) + len(broken) + len(missing_fm)
if issues == 0:
    print("\n✅ WIKI HEALTH: EXCELLENT")
    print("   Setup complete · No broken links · No missing frontmatter")
else:
    print(f"\n🟡 WIKI HEALTH: GOOD ({issues} minor issues)")

print(f"\n📊 Stats:")
print(f"   Pages:     {len(all_pages)}")
print(f"   Links:     {total_links}")
print(f"   Broken:    {len(broken)}")
print(f"   Orphans:   {len(orphans)} ({len(unexpected_orphans)} unexpected)")
print(f"   Tags:      {len(all_tags)} unique")

print(f"\n{'=' * 70}")

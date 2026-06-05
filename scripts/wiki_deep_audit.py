#!/usr/bin/env python3
"""
Deep audit of the LLM-Wiki vault.
Comprehensive checks beyond basic lint.
"""

import yaml
import re
from pathlib import Path
from collections import defaultdict, Counter

PROJECT_ROOT = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder")
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
DATA_DIR = PROJECT_ROOT / "data"

def extract_frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    try:
        _, fm, _ = content.split("---", 2)
        return yaml.safe_load(fm.strip()) or {}
    except Exception as e:
        print(f"  ⚠️  YAML error in {path.name}: {e}")
        return {}

def extract_wikilinks(content: str) -> list:
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)

print("=" * 70)
print("# DEEP AUDIT: LLM-WIKI VAULT")
print("=" * 70)

# ============================================================
# 1. Build comprehensive page registry
# ============================================================
all_pages = [p for p in WIKI_DIR.rglob("*.md")
             if ".obsidian" not in str(p) and "99-Templates" not in str(p)]

registry = {}       # name/stem/rel/alias → meta
path_registry = {}  # relative path → meta

for p in all_pages:
    fm = extract_frontmatter(p)
    content = p.read_text(encoding="utf-8")
    links = extract_wikilinks(content)
    stem = p.stem
    rel = str(p.relative_to(WIKI_DIR).with_suffix(""))
    name = (fm.get("cmd_name") or fm.get("moc_name") or fm.get("scene_name")
            or fm.get("concept_name") or fm.get("faq_question") or fm.get("title") or stem)

    meta = {
        "path": p, "name": name, "stem": stem, "rel": rel,
        "fm": fm, "links": links, "content": content,
        "size": len(content), "has_body": len(content.split("---", 2)[-1].strip()) > 50
    }
    path_registry[rel] = meta
    registry[name] = meta
    registry[stem] = meta
    registry[rel] = meta
    for alias in fm.get("aliases", []):
        registry[alias] = meta

# ============================================================
# 2. Resolve all wikilinks
# ============================================================
print("\n" + "=" * 70)
print("# CHECK 1: WIKILINK RESOLUTION")
print("=" * 70)

broken = []
resolved = 0
for p, meta in path_registry.items():
    for link in meta["links"]:
        target = link.split("|")[0].strip()
        if target not in registry:
            broken.append((meta["name"], target, str(meta["path"].relative_to(WIKI_DIR))))
        else:
            resolved += 1

print(f"Total wikilinks: {resolved + len(broken)}")
print(f"Resolved: {resolved}")
print(f"Broken: {len(broken)}")
if broken:
    for src, tgt, path in broken[:10]:
        print(f"  ❌ [{src}] → [[{tgt}]] (in {path})")
else:
    print("  ✅ All wikilinks resolve correctly")

# ============================================================
# 3. Orphan analysis (comprehensive)
# ============================================================
print("\n" + "=" * 70)
print("# CHECK 2: ORPHAN ANALYSIS")
print("=" * 70)

incoming = Counter()
for p, meta in path_registry.items():
    for link in meta["links"]:
        target = link.split("|")[0].strip()
        incoming[target] += 1

orphans = []
for p, meta in path_registry.items():
    name = meta["name"]
    stem = meta["stem"]
    rel = meta["rel"]
    inc = incoming.get(name, 0) + incoming.get(stem, 0) + incoming.get(rel, 0)
    for alias in meta["fm"].get("aliases", []):
        inc += incoming.get(alias, 0)
    if inc == 0:
        orphans.append(name)

expected = {"index", "log", "hot", "AGENTS", "CLAUDE", "taxonomy", "README",
            "cmd4coder Metadata Overview", "Agent Bootstrap", "Claude Code Context",
            "Wiki Index", "Wiki Log", "Hot Cache", "command-name",
            "单卡 RTX 4090 能训练多大的模型？", "DeepSpeed 和 Accelerate 怎么选？",
            "vLLM 和 SGLang 怎么选？", "RLHF 和 DPO 有什么区别？", "怎么对 LLM 进行安全扫描？",
            "大模型量化与端侧部署", "从零构建 RAG 应用"}

unexpected = [o for o in orphans if o not in expected]
print(f"Total orphans: {len(orphans)}")
print(f"Unexpected: {len(unexpected)}")
if unexpected:
    for o in unexpected[:10]:
        print(f"  ⚠️  [[{o}]]")
else:
    print("  ✅ All orphans are expected")

# ============================================================
# 4. Command frontmatter completeness
# ============================================================
print("\n" + "=" * 70)
print("# CHECK 3: COMMAND FRONTMATTER COMPLETENESS")
print("=" * 70)

cmds = list((WIKI_DIR / "entities/commands").glob("*.md"))
required_fields = ["cmd_name", "cmd_category", "cmd_install", "cmd_level", "cmd_platforms"]
optional_fields = ["cmd_related", "cmd_tags", "cmd_risk_level", "summary"]

missing_required = defaultdict(list)
missing_optional = defaultdict(list)

for p in cmds:
    fm = extract_frontmatter(p)
    for field in required_fields:
        if field not in fm:
            missing_required[field].append(p.stem)
    for field in optional_fields:
        if field not in fm:
            missing_optional[field].append(p.stem)

for field, items in missing_required.items():
    print(f"  ❌ Missing '{field}': {len(items)} commands")
    if len(items) <= 3:
        for i in items:
            print(f"     - {i}")

for field, items in missing_optional.items():
    if len(items) > 0:
        print(f"  ℹ️  Missing optional '{field}': {len(items)} commands")

if not missing_required:
    print("  ✅ All required fields present")

# ============================================================
# 5. cmd_related link validation
# ============================================================
print("\n" + "=" * 70)
print("# CHECK 4: CMD_RELATED LINK VALIDATION")
print("=" * 70)

broken_related = []
for p in cmds:
    fm = extract_frontmatter(p)
    related = fm.get("cmd_related", [])
    for r in related:
        if r not in registry:
            broken_related.append((p.stem, r))

print(f"Broken cmd_related references: {len(broken_related)}")
if broken_related:
    for src, tgt in broken_related[:10]:
        print(f"  ❌ [{src}] cmd_related: '{tgt}' not found")
else:
    print("  ✅ All cmd_related references valid")

# ============================================================
# 6. Category <-> MOC consistency
# ============================================================
print("\n" + "=" * 70)
print("# CHECK 5: CATEGORY ↔ MOC CONSISTENCY")
print("=" * 70)

# Build MOC name set
mocs = list((WIKI_DIR / "00-Maps").glob("*.md"))
moc_names = set()
moc_stems = set()
for p in mocs:
    moc_stems.add(p.stem)
    fm = extract_frontmatter(p)
    if fm and "moc_name" in fm:
        moc_names.add(fm["moc_name"])

# Check if cmd_category values have corresponding MOCs
categories = Counter()
for p in cmds:
    fm = extract_frontmatter(p)
    cat = fm.get("cmd_category", "")
    if cat:
        categories[cat] += 1

missing_mocs = []
for cat, count in categories.most_common():
    # cmd_category like "容器编排/Docker命令" → MOC likely "Docker命令-MOC"
    moc_guess = cat.split("/")[-1] + "-MOC"
    if moc_guess not in moc_stems and cat not in moc_names:
        missing_mocs.append((cat, moc_guess, count))

print(f"Categories without matching MOC: {len(missing_mocs)}")
if missing_mocs:
    for cat, guess, count in missing_mocs[:10]:
        print(f"  ⚠️  '{cat}' ({count} cmds) → expected MOC '{guess}'")
else:
    print("  ✅ All categories have matching MOCs")

# ============================================================
# 7. Content quality: empty sections
# ============================================================
print("\n" + "=" * 70)
print("# CHECK 6: CONTENT QUALITY (EMPTY SECTIONS)")
print("=" * 70)

empty_sections = []
for p in cmds:
    content = p.read_text(encoding="utf-8")
    # Find headers followed by another header (empty section)
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("## ") and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if next_line.startswith("## ") or next_line.startswith("---"):
                empty_sections.append((p.stem, line.strip()))

print(f"Empty sections: {len(empty_sections)}")
if empty_sections:
    for cmd, sec in empty_sections[:10]:
        print(f"  ⚠️  [{cmd}] {sec}")
else:
    print("  ✅ No empty sections detected")

# ============================================================
# 8. Duplicate content detection (hash-based)
# ============================================================
print("\n" + "=" * 70)
print("# CHECK 7: DUPLICATE CONTENT")
print("=" * 70)

import hashlib
body_hashes = defaultdict(list)
for p, meta in path_registry.items():
    body = meta["content"].split("---", 2)[-1].strip()
    h = hashlib.md5(body.encode()).hexdigest()
    body_hashes[h].append(meta["name"])

duplicates = {h: names for h, names in body_hashes.items() if len(names) > 1}
print(f"Duplicate bodies: {len(duplicates)}")
if duplicates:
    for h, names in list(duplicates.items())[:3]:
        print(f"  ⚠️  Same content: {', '.join(names[:5])}")
else:
    print("  ✅ No duplicate content")

# ============================================================
# 9. YAML source <-> Wiki sync check
# ============================================================
print("\n" + "=" * 70)
print("# CHECK 8: YAML SOURCE ↔ WIKI SYNC")
print("=" * 70)

# Load all YAML data files
yaml_cmds = {}
for yf in DATA_DIR.rglob("*.yaml"):
    try:
        data = yaml.safe_load(yf.read_text())
        if data and "commands" in data:
            for cmd in data["commands"]:
                if "name" in cmd:
                    yaml_cmds[cmd["name"]] = cmd
    except:
        pass

# Check for commands in YAML but not in wiki
wiki_cmd_names = set()
for p in cmds:
    fm = extract_frontmatter(p)
    if fm and "cmd_name" in fm:
        wiki_cmd_names.add(fm["cmd_name"])

missing_in_wiki = [n for n in yaml_cmds if n not in wiki_cmd_names]
missing_in_yaml = [n for n in wiki_cmd_names if n not in yaml_cmds]

print(f"Commands in YAML: {len(yaml_cmds)}")
print(f"Commands in Wiki: {len(wiki_cmd_names)}")
print(f"Missing in wiki: {len(missing_in_wiki)}")
print(f"Missing in YAML (orphan wiki pages): {len(missing_in_yaml)}")

if missing_in_wiki[:5]:
    for n in missing_in_wiki[:5]:
        print(f"  ❌ YAML '{n}' not in wiki")
if missing_in_yaml[:5]:
    for n in missing_in_yaml[:5]:
        print(f"  ℹ️  Wiki '{n}' not in YAML")

# ============================================================
# 10. Summary
# ============================================================
print("\n" + "=" * 70)
print("# AUDIT SUMMARY")
print("=" * 70)

issues = []
if broken: issues.append(f"broken links: {len(broken)}")
if unexpected: issues.append(f"unexpected orphans: {len(unexpected)}")
if missing_required: issues.append(f"missing required fields: {sum(len(v) for v in missing_required.values())}")
if broken_related: issues.append(f"broken related refs: {len(broken_related)}")
if missing_mocs: issues.append(f"categories without MOC: {len(missing_mocs)}")
if empty_sections: issues.append(f"empty sections: {len(empty_sections)}")
if duplicates: issues.append(f"duplicate content: {len(duplicates)}")
if missing_in_wiki: issues.append(f"commands missing in wiki: {len(missing_in_wiki)}")

if issues:
    print("Issues found:")
    for issue in issues:
        print(f"  • {issue}")
    print(f"\nHealth Score: {max(0, 100 - len(issues) * 5)}/100")
else:
    print("✅ No issues found. Health Score: 100/100")

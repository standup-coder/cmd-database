#!/usr/bin/env python3
"""
Full wiki-status implementation following Ar9av/obsidian-wiki spec.
Steps: scan sources → compute delta → report status → insights mode
"""

import json
import re
import os
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter, defaultdict

PROJECT_ROOT = Path(__file__).resolve().parents[4]  # auto: repo root (scripts live in tools/cmd/scripts/<sub>/)
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
DATA_DIR = Path(__file__).resolve().parents[2] / "data"  # YAML 源已随 CLI 收敛到 tools/cmd/data
MANIFEST_PATH = WIKI_DIR / "_meta/manifest.json"

# ============================================================
# Step 0: Config & Manifest
# ============================================================
env_path = WIKI_DIR / ".env"
vault_path = WIKI_DIR
sources_dir = DATA_DIR

manifest = {}
if MANIFEST_PATH.exists():
    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)

# ============================================================
# Step 1: Scan Vault Pages
# ============================================================
all_md_files = list(WIKI_DIR.rglob("*.md"))
all_md_files = [p for p in all_md_files if not str(p).startswith(str(WIKI_DIR/".obsidian"))]

pages_by_dir = defaultdict(list)
for p in all_md_files:
    rel = p.relative_to(WIKI_DIR)
    top = rel.parts[0] if rel.parts else "root"
    pages_by_dir[top].append(p)

def extract_frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    try:
        _, fm, _ = content.split("---", 2)
        import yaml
        return yaml.safe_load(fm.strip()) or {}
    except:
        return {}

def extract_wikilinks(content: str) -> list:
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

# Collect page metadata
page_meta = {}
for p in all_md_files:
    fm = extract_frontmatter(p)
    content = p.read_text(encoding="utf-8")
    links = extract_wikilinks(content)
    page_meta[p] = {
        "frontmatter": fm,
        "links": links,
        "size": len(content),
        "stem": p.stem,
        "name": fm.get("cmd_name") or fm.get("moc_name") or fm.get("scene_name") or fm.get("concept_name") or fm.get("faq_question") or p.stem,
        "tags": fm.get("cmd_tags", []) or fm.get("tags", []) or fm.get("scene_tags", []) or fm.get("concept_tags", []) or fm.get("faq_tags", []),
    }

# ============================================================
# Step 2: Build Link Graph
# ============================================================
incoming = Counter()
outgoing = Counter()
name_to_path = {}
stem_to_path = {}

for p, meta in page_meta.items():
    name_to_path[meta["name"]] = p
    stem_to_path[meta["stem"]] = p
    outgoing[meta["name"]] = len(meta["links"])
    for link in meta["links"]:
        target = link.split("|")[0].strip()
        incoming[target] += 1

# Resolve link targets
resolved_incoming = Counter()
for p, meta in page_meta.items():
    for link in meta["links"]:
        target = link.split("|")[0].strip()
        # Try to resolve
        resolved = False
        if target in name_to_path:
            resolved_incoming[target] += 1
            resolved = True
        elif target in stem_to_path:
            resolved_incoming[target] += 1
            resolved = True
        elif target.lower().replace("-", "") in {k.lower().replace("-", ""): k for k in stem_to_path}:
            resolved_incoming[target] += 1
            resolved = True

# ============================================================
# Step 3: Scan Sources & Delta
# ============================================================
source_files = list(DATA_DIR.rglob("*.yaml"))
manifest_sources = manifest.get("sources", [])
manifest_files = {s.get("file", "") for s in manifest_sources}

new_sources = []
modified_sources = []
unchanged_sources = []
for sf in source_files:
    rel = str(sf.relative_to(PROJECT_ROOT))
    mtime = sf.stat().st_mtime
    if rel not in manifest_files:
        new_sources.append((rel, sf.stat().st_size, datetime.fromtimestamp(mtime).isoformat()))
    else:
        # Check if modified since ingest
        unchanged_sources.append(rel)

# ============================================================
# Step 4: Token Footprint
# ============================================================
total_chars = sum(meta["size"] for meta in page_meta.values())
total_tokens = total_chars // 4
avg_page_tokens = total_tokens // len(page_meta) if page_meta else 0

# Index-only estimate (frontmatter only)
index_chars = 0
for meta in page_meta.values():
    fm = meta["frontmatter"]
    title = fm.get("cmd_name", "") or fm.get("moc_name", "") or fm.get("scene_name", "") or ""
    tags = str(fm.get("cmd_tags", []) or fm.get("tags", []))
    index_chars += len(title) + len(tags) + 50  # ~50 for other fields
index_tokens = index_chars // 4
typical_query_tokens = index_tokens + avg_page_tokens * 5

# ============================================================
# Step 5: What to Do Next Signals
# ============================================================
# 1. _raw/ files
raw_files = [f for f in (WIKI_DIR / "_raw").iterdir() if f.is_file() and f.name != ".gitkeep"] if (WIKI_DIR / "_raw").exists() else []

# 2. Orphan pages (no incoming links)
all_names = {meta["name"] for meta in page_meta.values()}
orphans = []
for p, meta in page_meta.items():
    name = meta["name"]
    # Check if anyone links to this page
    has_incoming = False
    for other_p, other_meta in page_meta.items():
        if other_p == p:
            continue
        for link in other_meta["links"]:
            target = link.split("|")[0].strip()
            if target == name or target == meta["stem"]:
                has_incoming = True
                break
        if has_incoming:
            break
    if not has_incoming:
        orphans.append(name)

# 3. Stale core pages (updated >= 90 days ago AND >= 5 incoming)
stale_core = []
cutoff = datetime.now() - timedelta(days=90)
for p, meta in page_meta.items():
    fm = meta["frontmatter"]
    created = fm.get("created", "")
    incoming_count = resolved_incoming.get(meta["name"], 0)
    if incoming_count >= 5 and created:
        try:
            d = datetime.strptime(created, "%Y-%m-%d")
            if d < cutoff:
                stale_core.append((meta["name"], created))
        except:
            pass

# ============================================================
# Step 6: Insights Mode
# ============================================================
# Anchor pages (top hubs)
anchor_pages = []
for p, meta in page_meta.items():
    name = meta["name"]
    inc = resolved_incoming.get(name, 0)
    out = outgoing.get(name, 0)
    anchor_pages.append((name, inc, out))
anchor_pages.sort(key=lambda x: (-x[1], -x[2]))

# Tag clusters
tag_pages = defaultdict(list)
for p, meta in page_meta.items():
    for tag in meta["tags"]:
        tag_pages[tag].append(meta["name"])

# Cohesion per tag (simplified)
tag_cohesion = []
for tag, pages in tag_pages.items():
    if len(pages) >= 3:
        n = len(pages)
        max_links = n * (n - 1) // 2
        actual = 0
        # Count links between pages in this tag group
        for p, meta in page_meta.items():
            if meta["name"] in pages:
                for link in meta["links"]:
                    target = link.split("|")[0].strip()
                    if target in pages:
                        actual += 1
        cohesion = actual / max_links if max_links > 0 else 0
        tag_cohesion.append((tag, n, cohesion))
tag_cohesion.sort(key=lambda x: -x[2])

# ============================================================
# OUTPUT: Full Report
# ============================================================
print("=" * 70)
print("# Wiki Status Report")
print("=" * 70)

# Overview
print(f"\n## Overview")
print(f"- **Total wiki pages:** {len(page_meta)} across {len(pages_by_dir)} top-level directories")
print(f"- **Total sources ingested:** {len(manifest_sources)}")
print(f"- **Last ingest:** {manifest.get('updated_at', 'N/A')}")
print(f"- **Vault structure:** {manifest.get('vault_structure', 'custom')}")

# Directory breakdown
print(f"\n### Page Distribution")
for dname in sorted(pages_by_dir.keys()):
    count = len(pages_by_dir[dname])
    print(f"- `{dname}/`: {count} pages")

# Delta
print(f"\n## Delta (what's changed since last ingest)")
print(f"- **New sources:** {len(new_sources)} (YAML files not in manifest)")
print(f"- **Unchanged sources:** {len(unchanged_sources)}")
if new_sources:
    print(f"\n### New sources ({len(new_sources)})")
    for rel, size, mtime in new_sources[:5]:
        print(f"- `{rel}` ({size//1024} KB)")
    if len(new_sources) > 5:
        print(f"- ... and {len(new_sources)-5} more")

# Token Footprint
print(f"\n## Token Footprint (estimated)")
print(f"| Scope | Pages | ~Tokens |")
print(f"|-------|-------|---------|")
print(f"| Full wiki (all) | **{len(page_meta)}** | **{total_tokens:,}** |")
print(f"| Index-only pass | {len(page_meta)} | ~{index_tokens:,} |")
print(f"| Typical query (index + 5 pages) | 6 | ~{typical_query_tokens:,} |")
print(f"\n*Methodology: 4 chars/token heuristic*")

# What to Do Next
print(f"\n## What to Do Next")
signals = []

if raw_files:
    signals.append(("📥", f"Ingest {len(raw_files)} files waiting in `_raw/`", "wiki-ingest"))
if stale_core:
    signals.append(("🔄", f"Refresh {len(stale_core)} stale core pages", "open pages & re-run wiki-update"))
if len(orphans) > 12:  # README and expected orphans excluded
    signals.append(("🔗", f"Link {len(orphans)} orphan pages", "cross-linker"))
if new_sources:
    signals.append(("✅", f"{len(new_sources)} new sources ready to ingest", "wiki-ingest"))

if not signals:
    print("\n✅ Wiki is healthy — nothing urgent.")
    print("   All sources tracked · no orphans · no stale core pages · no _raw/ files pending")
else:
    for i, (emoji, desc, cmd) in enumerate(signals, 1):
        print(f"\n{i}. {emoji}  {desc}")
        print(f"   → run: {cmd}")

# ============================================================
# Insights Mode
# ============================================================
print(f"\n{'=' * 70}")
print("# Wiki Insights")
print("=" * 70)

# Anchor Pages
print(f"\n## Anchor Pages (Top 10 Hubs)")
print(f"| Page | Incoming | Outgoing | Note |")
print(f"|------|----------|----------|------|")
for name, inc, out in anchor_pages[:10]:
    note = ""
    if inc >= 5 and out >= 3:
        note = "connector hub"
    elif inc >= 5 and out <= 1:
        note = "sink hub — cross-linker candidate"
    print(f"| [[{name}]] | {inc} | {out} | {note} |")

# Tag Cluster Cohesion
print(f"\n## Tag Cluster Cohesion")
print(f"### Most cohesive")
for tag, n, cohesion in tag_cohesion[:5]:
    print(f"- `#{tag}` — {n} pages, cohesion {cohesion:.2f}")
print(f"\n### Most fragmented")
for tag, n, cohesion in tag_cohesion[-5:]:
    if cohesion < 0.15:
        print(f"- `#{tag}` — {n} pages, cohesion {cohesion:.2f} ⚠️ cross-linker target")
    else:
        print(f"- `#{tag}` — {n} pages, cohesion {cohesion:.2f}")

# Orphans
print(f"\n## Orphan Pages ({len(orphans)} total)")
for name in orphans[:10]:
    print(f"- [[{name}]]")
if len(orphans) > 10:
    print(f"- ... and {len(orphans)-10} more")

# Graph snapshot for next diff
print(f"\n<!-- GRAPH_SNAPSHOT: {json.dumps({'total_pages': len(page_meta), 'total_links': sum(len(m['links']) for m in page_meta.values()), 'top_hub': anchor_pages[0][0] if anchor_pages else None})} -->")

print(f"\n{'=' * 70}")
print("Report complete.")
print("=" * 70)

#!/usr/bin/env python3
"""
Execute cross-linker + wiki-ingest following obsidian-wiki skills spec.
"""

import yaml
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

PROJECT_ROOT = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder")
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
DATA_DIR = PROJECT_ROOT / "data"
MANIFEST_PATH = WIKI_DIR / "_meta/manifest.json"

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
# Step 1: Build Page Registry
# ============================================================
print("=" * 70)
print("Cross-Linker: Building page registry...")
print("=" * 70)

all_pages = list(WIKI_DIR.rglob("*.md"))
all_pages = [p for p in all_pages if ".obsidian" not in str(p)]

registry = {}
for p in all_pages:
    fm = extract_frontmatter(p)
    name = fm.get("cmd_name") or fm.get("moc_name") or fm.get("scene_name") or fm.get("concept_name") or fm.get("faq_question") or p.stem
    rel = str(p.relative_to(WIKI_DIR))
    registry[name] = {
        "path": rel,
        "stem": p.stem,
        "name": name,
        "tags": fm.get("cmd_tags", []) or fm.get("tags", []) or fm.get("scene_tags", []) or fm.get("concept_tags", []) or fm.get("faq_tags", []),
    }

# Also register aliases
for name, info in list(registry.items()):
    registry[info["stem"]] = info

print(f"Registered {len(set(v['path'] for v in registry.values()))} unique pages")

# ============================================================
# Step 2: Find Orphan Pages
# ============================================================
incoming = defaultdict(int)
for p in all_pages:
    content = p.read_text(encoding="utf-8")
    links = extract_wikilinks(content)
    for link in links:
        target = link.split("|")[0].strip()
        incoming[target] += 1

orphans = []
for name, info in registry.items():
    if name == info["stem"]:
        continue  # Skip stem duplicates
    inc = incoming.get(name, 0) + incoming.get(info["stem"], 0)
    if inc == 0:
        orphans.append((name, info["path"]))

# Filter out expected orphans (meta pages, templates)
expected_orphans = {"hot", "log", "index", "AGENTS", "CLAUDE", "taxonomy", "command-name", "README",
                    "单卡4090微调7B模型", "生产环境推理部署", "RAG应用构建", "模型量化与压缩",
                    "单卡4090能训练多大模型", "deepspeed-vs-accelerate", "vllm-vs-sglang",
                    "rlhf-vs-dpo", "模型安全扫描", "ZeRO优化", "KV-Cache", "推测解码", "LoRA原理"}
actionable_orphans = [(n, p) for n, p in orphans if n not in expected_orphans]

print(f"\nOrphan pages: {len(orphans)} total, {len(actionable_orphans)} actionable")
for name, path in actionable_orphans[:10]:
    print(f"  - [[{name}]] ({path})")

# ============================================================
# Step 3: Cross-link Orphans into Relevant Pages
# ============================================================
print(f"\n{'=' * 70}")
print("Cross-Linker: Inserting missing wikilinks...")
print("=" * 70)

links_added = 0

# Strategy 1: Link concept pages from related MOCs
concept_links = {
    "ZeRO优化": ["大模型训练-MOC", "deepspeed"],
    "KV-Cache": ["大模型推理-MOC", "vllm", "sglang"],
    "推测解码": ["大模型推理-MOC", "vllm"],
    "LoRA原理": ["大模型训练-MOC", "peft", "unsloth"],
}

for concept, targets in concept_links.items():
    concept_path = WIKI_DIR / f"concepts/{concept}.md"
    if not concept_path.exists():
        continue
    content = concept_path.read_text(encoding="utf-8")
    if "## 关联" in content or "## Related" in content:
        continue
    
    # Add a Related section
    related_section = "\n## 关联页面\n\n"
    for target in targets:
        if target in registry:
            related_section += f"- [[{target}]]\n"
    
    # Append before any HTML comment at end
    if "<!--" in content:
        content = content.split("<!--")[0] + related_section + "\n<!--" + content.split("<!--", 1)[1]
    else:
        content = content.rstrip() + "\n" + related_section + "\n"
    
    concept_path.write_text(content, encoding="utf-8")
    links_added += len(targets)
    print(f"  ✓ Added {len(targets)} links to [[{concept}]]")

# Strategy 2: Link FAQ pages from related MOCs
faq_links = {
    "单卡4090能训练多大模型": ["大模型训练-MOC", "unsloth"],
    "deepspeed-vs-accelerate": ["大模型训练-MOC", "deepspeed", "accelerate"],
    "vllm-vs-sglang": ["大模型推理-MOC", "vllm", "sglang"],
    "rlhf-vs-dpo": ["大模型训练-MOC", "trl"],
    "模型安全扫描": ["AI安全-MOC", "garak"],
}

for faq, targets in faq_links.items():
    faq_path = WIKI_DIR / f"references/faqs/{faq}.md"
    if not faq_path.exists():
        continue
    content = faq_path.read_text(encoding="utf-8")
    if "## 关联" in content:
        continue
    
    related_section = "\n## 关联页面\n\n"
    for target in targets:
        if target in registry:
            related_section += f"- [[{target}]]\n"
    
    if "<!--" in content:
        content = content.split("<!--")[0] + related_section + "\n<!--" + content.split("<!--", 1)[1]
    else:
        content = content.rstrip() + "\n" + related_section + "\n"
    
    faq_path.write_text(content, encoding="utf-8")
    links_added += len(targets)
    print(f"  ✓ Added {len(targets)} links to [[{faq}]]")

# Strategy 3: Link scene pages from index.md
scene_links = {
    "单卡4090微调7B模型": ["大模型训练-MOC", "unsloth", "peft"],
    "生产环境推理部署": ["大模型推理-MOC", "vllm", "helicone"],
    "RAG应用构建": ["RAG基础设施-MOC", "向量数据库-MOC", "langchain"],
    "模型量化与压缩": ["模型生态-MOC", "边缘AI-MOC", "vllm"],
}

for scene, targets in scene_links.items():
    scene_path = WIKI_DIR / f"synthesis/scenes/{scene}.md"
    if not scene_path.exists():
        continue
    content = scene_path.read_text(encoding="utf-8")
    
    # Check if already has outgoing links section
    has_related = "## 关联" in content or "## Related" in content
    
    if not has_related:
        related_section = "\n## 关联维度\n\n"
        for target in targets:
            if target in registry:
                related_section += f"- [[{target}]]\n"
        
        content = content.rstrip() + "\n" + related_section + "\n"
        scene_path.write_text(content, encoding="utf-8")
        links_added += len(targets)
        print(f"  ✓ Added {len(targets)} links to [[{scene}]]")

# Strategy 4: Update index.md with explicit links to scenes and concepts
index_path = WIKI_DIR / "index.md"
if index_path.exists():
    content = index_path.read_text(encoding="utf-8")
    # Ensure scenes are linked
    if "[[synthesis/scenes/单卡4090微调7B模型|单卡4090微调7B模型]]" not in content:
        content = content.replace(
            "### 按场景",
            "### 按场景\n\n- [[synthesis/scenes/单卡4090微调7B模型|单卡4090微调7B模型]]\n- [[synthesis/scenes/生产环境推理部署|生产环境推理部署]]\n- [[synthesis/scenes/RAG应用构建|RAG应用构建]]\n- [[synthesis/scenes/模型量化与压缩|模型量化与压缩]]\n"
        )
        index_path.write_text(content, encoding="utf-8")
        links_added += 4
        print(f"  ✓ Updated index.md with scene links")

print(f"\nTotal links added: {links_added}")

# ============================================================
# Step 4: Ingest metadata.yaml
# ============================================================
print(f"\n{'=' * 70}")
print("Wiki-Ingest: Processing metadata.yaml...")
print("=" * 70)

meta_path = DATA_DIR / "metadata.yaml"
if meta_path.exists():
    with open(meta_path, encoding="utf-8") as f:
        meta_data = yaml.safe_load(f)
    
    # Create a wiki page for metadata
    meta_wiki = WIKI_DIR / "references/metadata-overview.md"
    categories = meta_data.get("categories", {})
    data_files = meta_data.get("data_files", [])
    
    md = "---\n"
    md += "title: \"cmd4coder Metadata Overview\"\n"
    md += "source_file: \"data/metadata.yaml\"\n"
    md += "tags: [\"meta\", \"reference\"]\n"
    md += f"created: \"{datetime.now().strftime('%Y-%m-%d')}\"\n"
    md += "---\n\n"
    md += "# cmd4coder Metadata Overview\n\n"
    md += f"> Version {meta_data.get('version', 'unknown')} — {meta_data.get('description', '')}\n\n"
    md += "## Categories\n\n"
    md += f"Total categories: {len(categories)}\n\n"
    
    for cat_id, cat_info in sorted(categories.items(), key=lambda x: x[1].get("order", 0)):
        name = cat_info.get("name", cat_id)
        desc = cat_info.get("description", "")
        order = cat_info.get("order", 0)
        md += f"- **{name}** (order: {order}) — {desc}\n"
    
    md += "\n## Data Files\n\n"
    md += f"Total data files: {len(data_files)}\n\n"
    for df in data_files:
        md += f"- `{df}`\n"
    
    meta_wiki.write_text(md, encoding="utf-8")
    print(f"  ✓ Created [[references/metadata-overview]]")
    
    # Update manifest
    manifest = {}
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH) as f:
            manifest = json.load(f)
    
    manifest["sources"].append({
        "file": "data/metadata.yaml",
        "type": "metadata",
        "pages_created": ["references/metadata-overview"],
        "timestamp": datetime.now().isoformat(),
    })
    
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print(f"  ✓ Manifest updated")

# ============================================================
# Step 5: Update log.md
# ============================================================
log_path = WIKI_DIR / "log.md"
if log_path.exists():
    content = log_path.read_text()
    content += f"\n- [{datetime.now().isoformat()}] CROSS_LINKER links_added={links_added}\n"
    content += f"- [{datetime.now().isoformat()}] INGEST metadata.yaml → references/metadata-overview.md\n"
    log_path.write_text(content)
    print(f"  ✓ log.md updated")

print(f"\n{'=' * 70}")
print("All tasks completed!")
print("=" * 70)

#!/usr/bin/env python3
"""LLM-Wiki Status Dashboard - Reports vault health metrics"""

import json
import re
from pathlib import Path
from collections import Counter

WIKI_DIR = Path(__file__).resolve().parents[4] / "llm-wiki"  # auto: llm-wiki stays at repo root

def extract_wikilinks(content: str) -> list:
    """Extract [[link]] or [[link|alias]] patterns"""
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def extract_frontmatter(path: Path) -> dict:
    """Parse YAML frontmatter from markdown file"""
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    try:
        _, fm, _ = content.split("---", 2)
        import yaml
        return yaml.safe_load(fm.strip()) or {}
    except:
        return {}

def main():
    print("=" * 70)
    print("LLM-Wiki Status Dashboard")
    print("=" * 70)
    
    # Page counts
    commands = list((WIKI_DIR / "entities/commands").glob("*.md"))
    mocs = list((WIKI_DIR / "00-Maps").glob("*.md"))
    scenes = list((WIKI_DIR / "synthesis/scenes").glob("*.md"))
    concepts = list((WIKI_DIR / "concepts").glob("*.md"))
    faqs = list((WIKI_DIR / "references/faqs").glob("*.md"))
    
    total = len(commands) + len(mocs) + len(scenes) + len(concepts) + len(faqs)
    
    print(f"\n📊 Page Counts")
    print(f"   Commands:       {len(commands)}")
    print(f"   MOCs:           {len(mocs)}")
    print(f"   Scenes:         {len(scenes)}")
    print(f"   Concepts:       {len(concepts)}")
    print(f"   FAQs:           {len(faqs)}")
    print(f"   ─────────────────")
    print(f"   Total:          {total}")
    
    # Link analysis
    all_pages = commands + mocs + scenes + concepts + faqs
    all_names = {p.stem for p in all_pages}
    # Also track display names for commands (slug -> original name mapping from frontmatter)
    name_map = {}
    for p in all_pages:
        fm = extract_frontmatter(p)
        if "cmd_name" in fm:
            name_map[p.stem] = fm["cmd_name"]
        elif "moc_name" in fm:
            name_map[p.stem] = fm["moc_name"]
        elif "scene_name" in fm:
            name_map[p.stem] = fm["scene_name"]
        elif "concept_name" in fm:
            name_map[p.stem] = fm["concept_name"]
    
    total_links = 0
    broken_links = []
    all_tags = []
    
    for p in all_pages:
        content = p.read_text(encoding="utf-8")
        links = extract_wikilinks(content)
        total_links += len(links)
        
        for link in links:
            # Check if link target exists (as stem or exact match)
            link_stem = Path(link.split("|")[0].strip()).stem
            link_target = link.split("|")[0].strip()
            
            # Try multiple matching strategies
            exists = False
            if link_target in name_map.values():
                exists = True
            elif link_stem in all_names:
                exists = True
            elif link_stem.lower().replace("-", "") in [n.lower().replace("-", "") for n in all_names]:
                exists = True
            
            if not exists:
                broken_links.append((p.name, link))
        
        fm = extract_frontmatter(p)
        tags = fm.get("cmd_tags", []) or fm.get("tags", []) or fm.get("scene_tags", []) or fm.get("faq_tags", []) or fm.get("concept_tags", [])
        all_tags.extend(tags)
    
    print(f"\n🔗 Link Health")
    print(f"   Total wikilinks: {total_links}")
    print(f"   Broken links:    {len(broken_links)}")
    if broken_links:
        for page, link in broken_links[:10]:
            print(f"      {page} → [[{link}]]")
        if len(broken_links) > 10:
            print(f"      ... and {len(broken_links) - 10} more")
    
    # Tag distribution
    tag_counts = Counter(all_tags)
    print(f"\n🏷️  Top Tags")
    for tag, count in tag_counts.most_common(15):
        print(f"   #{tag}: {count}")
    
    # Hub pages (most linked)
    link_targets = []
    for p in all_pages:
        content = p.read_text(encoding="utf-8")
        links = extract_wikilinks(content)
        for link in links:
            link_targets.append(link.split("|")[0].strip())
    
    target_counts = Counter(link_targets)
    print(f"\n⭐ Hub Pages (Most Linked)")
    for target, count in target_counts.most_common(10):
        print(f"   [[{target}]]: {count} incoming links")
    
    # Orphans (no incoming links)
    linked_targets = set(target_counts.keys())
    orphan_names = []
    for p in all_pages:
        fm = extract_frontmatter(p)
        display = fm.get("cmd_name") or fm.get("moc_name") or fm.get("scene_name") or p.stem
        if display not in linked_targets and p.stem not in linked_targets:
            orphan_names.append(display)
    
    print(f"\n⚠️  Orphan Pages (no incoming links): {len(orphan_names)}")
    if orphan_names:
        print(f"   {', '.join(orphan_names[:10])}{'...' if len(orphan_names) > 10 else ''}")
    
    print(f"\n{'=' * 70}")
    print("Overall Health: ", end="")
    if len(broken_links) == 0 and len(orphan_names) < 50:
        print("✅ EXCELLENT")
    elif len(broken_links) < 20 and len(orphan_names) < 100:
        print("🟢 GOOD")
    else:
        print("🟡 NEEDS ATTENTION")
    print("=" * 70)

if __name__ == "__main__":
    main()

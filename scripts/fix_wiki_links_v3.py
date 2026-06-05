#!/usr/bin/env python3
"""Fix broken wikilinks using category-to-MOC mapping extracted from YAML source"""

import re
import yaml
from pathlib import Path

WIKI_DIR = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder/llm-wiki")
CMD_DIR = WIKI_DIR / "01-Commands"
DATA_DIR = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder/data")

def build_cat_map():
    """Build mapping from English category to MOC filename"""
    cat_map = {}
    for f in DATA_DIR.rglob("*.yaml"):
        try:
            with open(f, encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
            if not data or "commands" not in data:
                continue
            file_cat = data.get("category", "")
            dim = file_cat.split("/")[-1] if "/" in file_cat else file_cat
            moc_file = f"{dim}-MOC"
            for cmd in data.get("commands", []):
                cmd_cat = cmd.get("category", "")
                if cmd_cat and cmd_cat != file_cat:
                    cat_map[cmd_cat] = moc_file
        except Exception:
            pass
    return cat_map

def main():
    cat_map = build_cat_map()
    print(f"Built category map with {len(cat_map)} entries")
    
    fixed = 0
    broken = 0
    
    for cmd_file in CMD_DIR.glob("*.md"):
        content = cmd_file.read_text(encoding="utf-8")
        original = content
        
        # Extract cmd_category from frontmatter
        cat_match = re.search(r'"cmd_category"\s*:\s*"([^"]+)"', content)
        if not cat_match:
            continue
        
        cmd_category = cat_match.group(1)
        
        # Find the 所属维度 link
        link_match = re.search(r'## 所属维度\n\n\[\[([^\]|]+)-MOC\|([^\]]+)\]\]', content)
        if not link_match:
            continue
        
        old_dim = link_match.group(1)
        old_display = link_match.group(2)
        old_link = f"[[{old_dim}-MOC|{old_display}]]"
        
        # Lookup correct MOC
        correct_moc = cat_map.get(cmd_category)
        
        if correct_moc and correct_moc != f"{old_dim}-MOC":
            new_link = f"[[{correct_moc}|{cmd_category}]]"
            content = content.replace(old_link, new_link)
            fixed += 1
        else:
            broken += 1
        
        if content != original:
            cmd_file.write_text(content, encoding="utf-8")
    
    print(f"Fixed {fixed} command pages")
    print(f"Remaining broken: {broken}")

if __name__ == "__main__":
    main()

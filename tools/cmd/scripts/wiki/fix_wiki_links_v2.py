#!/usr/bin/env python3
"""Fix broken wikilinks by mapping cmd_category to actual MOC filenames"""

import re
import json
from pathlib import Path

WIKI_DIR = Path(__file__).resolve().parents[4] / "llm-wiki"  # auto: llm-wiki stays at repo root
CMD_DIR = WIKI_DIR / "01-Commands"
MOC_DIR = WIKI_DIR / "00-Maps"

def main():
    # Build mapping: moc_name -> moc_filename
    moc_name_to_file = {}
    for p in MOC_DIR.glob("*.md"):
        content = p.read_text(encoding="utf-8")
        # Try to extract moc_name from frontmatter
        match = re.search(r'"moc_name"\s*:\s*"([^"]+)"', content)
        if match:
            moc_name = match.group(1)
            moc_name_to_file[moc_name] = p.stem
    
    print(f"Loaded {len(moc_name_to_file)} MOC mappings")
    
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
        # Pattern: [[anything-MOC|anything]]
        link_match = re.search(r'## 所属维度\n\n\[\[([^\]|]+)-MOC\|([^\]]+)\]\]', content)
        if not link_match:
            continue
        
        old_dim = link_match.group(1)
        old_display = link_match.group(2)
        old_link = f"[[{old_dim}-MOC|{old_display}]]"
        
        # Find correct MOC
        correct_moc = None
        
        # Strategy 1: exact category match
        if cmd_category in moc_name_to_file:
            correct_moc = moc_name_to_file[cmd_category]
        
        # Strategy 2: check if cmd_category is a prefix/suffix of moc_name
        if correct_moc is None:
            for moc_name, moc_file in moc_name_to_file.items():
                if cmd_category in moc_name or moc_name in cmd_category:
                    correct_moc = moc_file
                    break
        
        # Strategy 3: match last part after "/"
        if correct_moc is None:
            cmd_last = cmd_category.split("/")[-1] if "/" in cmd_category else cmd_category
            for moc_name, moc_file in moc_name_to_file.items():
                moc_last = moc_name.split("/")[-1] if "/" in moc_name else moc_name
                if cmd_last == moc_last:
                    correct_moc = moc_file
                    break
        
        # Strategy 4: fuzzy match
        if correct_moc is None:
            cmd_last = cmd_category.split("/")[-1] if "/" in cmd_category else cmd_category
            for moc_name, moc_file in moc_name_to_file.items():
                moc_last = moc_name.split("/")[-1] if "/" in moc_name else moc_name
                if cmd_last.lower() in moc_last.lower() or moc_last.lower() in cmd_last.lower():
                    correct_moc = moc_file
                    break
        
        if correct_moc and correct_moc != f"{old_dim}-MOC":
            new_link = f"[[{correct_moc}|{cmd_category}]]"
            content = content.replace(old_link, new_link)
            fixed += 1
        else:
            broken += 1
            if correct_moc is None:
                pass
                # print(f"Cannot fix: {cmd_file.name} (category: {cmd_category})")
        
        if content != original:
            cmd_file.write_text(content, encoding="utf-8")
    
    print(f"Fixed {fixed} command pages")
    print(f"Remaining broken: {broken}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Fix broken wikilinks in LLM-Wiki by mapping dimensions to actual MOC filenames"""

import re
from pathlib import Path

WIKI_DIR = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder/llm-wiki")
CMD_DIR = WIKI_DIR / "01-Commands"
MOC_DIR = WIKI_DIR / "00-Maps"

def main():
    # Build MOC filename map: dimension -> filename (without .md)
    moc_files = {p.stem: p for p in MOC_DIR.glob("*.md")}
    
    # Also extract moc_name from frontmatter for mapping
    moc_name_to_file = {}
    for p in MOC_DIR.glob("*.md"):
        content = p.read_text(encoding="utf-8")
        # Extract moc_name from frontmatter
        match = re.search(r'"moc_name"\s*:\s*"([^"]+)"', content)
        if match:
            moc_name = match.group(1)
            moc_name_to_file[moc_name] = p.stem
    
    fixed = 0
    broken = 0
    
    for cmd_file in CMD_DIR.glob("*.md"):
        content = cmd_file.read_text(encoding="utf-8")
        original = content
        
        # Find the 所属维度 section and fix the link
        # Pattern: [[dimension-MOC|category]]
        pattern = r'## 所属维度\n\n\[\[([^\]|]+)-MOC\|([^\]]+)\]\]'
        match = re.search(pattern, content)
        if match:
            dim = match.group(1)
            cat = match.group(2)
            
            # Try to find correct MOC filename
            correct_moc = None
            
            # Strategy 1: exact stem match
            if f"{dim}-MOC" in moc_files:
                correct_moc = f"{dim}-MOC"
            
            # Strategy 2: check if category matches moc_name
            if correct_moc is None and cat in moc_name_to_file:
                correct_moc = moc_name_to_file[cat]
            
            # Strategy 3: partial match
            if correct_moc is None:
                for moc_stem in moc_files:
                    if dim.lower() in moc_stem.lower() or moc_stem.lower() in dim.lower():
                        correct_moc = moc_stem
                        break
            
            if correct_moc and correct_moc != f"{dim}-MOC":
                old_link = f"[[{dim}-MOC|{cat}]]"
                new_link = f"[[{correct_moc}|{cat}]]"
                content = content.replace(old_link, new_link)
                fixed += 1
            elif correct_moc is None:
                broken += 1
                # print(f"Cannot fix: {cmd_file.name} -> {dim}-MOC")
        
        if content != original:
            cmd_file.write_text(content, encoding="utf-8")
    
    print(f"Fixed {fixed} command pages")
    print(f"Remaining broken: {broken}")

if __name__ == "__main__":
    main()

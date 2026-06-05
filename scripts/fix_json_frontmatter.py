#!/usr/bin/env python3
"""Fix JSON-formatted frontmatter in wiki files → proper YAML."""

import json
import yaml
from pathlib import Path

WIKI_DIR = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder/llm-wiki")

def fix_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return False
    
    fm_text = parts[1].strip()
    if not fm_text.startswith("{"):
        return False  # Not JSON frontmatter
    
    try:
        data = json.loads(fm_text)
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON parse error in {path.name}: {e}")
        return False
    
    # Convert to YAML
    yaml_fm = yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False)
    new_content = f"---\n{yaml_fm}---\n{parts[2]}"
    path.write_text(new_content, encoding="utf-8")
    print(f"  ✅ Fixed {path.relative_to(WIKI_DIR)}")
    return True

# Find all files with JSON frontmatter
files = list(WIKI_DIR.rglob("*.md"))
fixed = 0
for p in files:
    if ".obsidian" in str(p):
        continue
    if fix_file(p):
        fixed += 1

print(f"\nFixed {fixed} files with JSON frontmatter.")

#!/usr/bin/env python3
"""
Generate summary field for all command pages from their one-line description.
Extracts the first non-header line (typically the > quote description).
"""

import yaml
import re
from pathlib import Path

WIKI_DIR = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder/llm-wiki")

def extract_summary(content: str) -> str:
    """Extract one-line summary from command page body."""
    # Split frontmatter and body
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
        else:
            return ""
    else:
        body = content

    # Find first meaningful line after title
    lines = body.split("\n")
    in_frontmatter = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("---"):
            continue
        # Extract from quote block
        if stripped.startswith("> "):
            return stripped[2:].strip()
        # Or just take the first non-empty line (limited length)
        if len(stripped) > 5 and len(stripped) < 200:
            return stripped
    return ""

def add_summary_to_page(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False

    fm_text = parts[1].strip()
    try:
        fm = yaml.safe_load(fm_text)
    except:
        return False

    if not fm or "summary" in fm:
        return False  # Already has summary

    summary = extract_summary(content)
    if not summary:
        return False

    # Truncate to reasonable length
    if len(summary) > 120:
        summary = summary[:117] + "..."

    # Insert summary into frontmatter
    # Find a good insertion point (after cmd_level or before cmd_tags)
    fm_lines = fm_text.split("\n")
    insert_idx = len(fm_lines)
    for i, line in enumerate(fm_lines):
        if line.strip().startswith("cmd_level:") or line.strip().startswith("cmd_tags:"):
            insert_idx = i
            break

    fm_lines.insert(insert_idx, f'summary: "{summary}"')
    new_fm = "\n".join(fm_lines)
    new_content = f"---\n{new_fm}\n---{parts[2]}"
    path.write_text(new_content, encoding="utf-8")
    return True

# Process all command pages
cmds = list((WIKI_DIR / "entities/commands").glob("*.md"))
fixed = 0
skipped = 0
for p in cmds:
    if add_summary_to_page(p):
        fixed += 1
    else:
        skipped += 1

print(f"Added summary: {fixed} pages")
print(f"Skipped (already has or no extractable summary): {skipped} pages")

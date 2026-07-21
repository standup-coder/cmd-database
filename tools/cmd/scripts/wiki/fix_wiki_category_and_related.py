#!/usr/bin/env python3
"""
Fix two issues in wiki command pages:
1. cmd_category: sync with YAML file-level category (English → Chinese)
2. cmd_related: remove references to commands not in wiki
"""

import yaml
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]  # auto: repo root (scripts live in tools/cmd/scripts/<sub>/)
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
DATA_DIR = Path(__file__).resolve().parents[2] / "data"  # YAML 源已随 CLI 收敛到 tools/cmd/data

def extract_frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}, content
    try:
        _, fm, rest = content.split("---", 2)
        return yaml.safe_load(fm.strip()) or {}, rest
    except:
        return {}, content

def build_file_category_map():
    """Map YAML relative path → file-level category"""
    mapping = {}
    for f in DATA_DIR.rglob("*.yaml"):
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
            if data and "commands" in data:
                rel = str(f.relative_to(PROJECT_ROOT))
                mapping[rel] = data.get("category", "")
        except:
            pass
    return mapping

def build_wiki_cmd_set():
    """Build set of all cmd_names in wiki"""
    names = set()
    stems = set()
    for p in (WIKI_DIR / "entities/commands").glob("*.md"):
        stems.add(p.stem)
        fm, _ = extract_frontmatter(p)
        if fm and "cmd_name" in fm:
            names.add(fm["cmd_name"])
    return names, stems

def moc_filename(category: str) -> str:
    """Convert category path to MOC filename"""
    # category like "容器编排/K8s网络插件" → "K8s网络插件-MOC"
    name = category.split("/")[-1]
    return f"{name}-MOC"

def main():
    file_cats = build_file_category_map()
    wiki_names, wiki_stems = build_wiki_cmd_set()

    cmds = list((WIKI_DIR / "entities/commands").glob("*.md"))
    fixed_cat = 0
    fixed_related = 0

    for p in cmds:
        fm, rest = extract_frontmatter(p)
        if not fm:
            continue

        content = p.read_text(encoding="utf-8")
        original = content
        source_file = fm.get("source_file", "")
        cmd_name = fm.get("cmd_name", "")

        # === Fix 1: cmd_category ===
        file_cat = file_cats.get(source_file, "")
        if file_cat and fm.get("cmd_category") != file_cat:
            # Replace cmd_category in frontmatter
            old_cat = fm["cmd_category"]
            content = content.replace(
                f'cmd_category: "{old_cat}"',
                f'cmd_category: "{file_cat}"'
            )
            content = content.replace(
                f"cmd_category: '{old_cat}'",
                f'cmd_category: "{file_cat}"'
            )
            # Also handle unquoted
            content = content.replace(
                f"cmd_category: {old_cat}",
                f'cmd_category: "{file_cat}"'
            )
            fixed_cat += 1

            # Fix 所属维度 wikilink
            old_moc = old_cat.split("/")[-1] + "-MOC"
            new_moc = moc_filename(file_cat)
            # Replace both the link target and display text
            old_link = f"[[{old_moc}|{old_cat}]]"
            new_link = f"[[{new_moc}|{file_cat}]]"
            content = content.replace(old_link, new_link)

        # === Fix 2: cmd_related ===
        related = fm.get("cmd_related", [])
        valid_related = []
        for r in related:
            # Check if related command exists in wiki (by name or slugified stem)
            slug = r.replace(" ", "-")
            if r in wiki_names or slug in wiki_stems:
                valid_related.append(r)

        if len(valid_related) != len(related):
            # Rebuild cmd_related in frontmatter
            old_block = yaml.dump({"cmd_related": related}, allow_unicode=True, default_flow_style=False).strip()
            new_block = yaml.dump({"cmd_related": valid_related}, allow_unicode=True, default_flow_style=False).strip()
            content = content.replace(old_block, new_block)
            fixed_related += 1

            # Also fix the wikilinks in 关联命令 section
            removed = set(related) - set(valid_related)
            for r in removed:
                slug = r.replace(" ", "-")
                # Remove the list item line
                lines = content.split("\n")
                new_lines = []
                for line in lines:
                    if f"[[{r}]]" in line or f"[[{slug}]]" in line:
                        continue
                    new_lines.append(line)
                content = "\n".join(new_lines)

        if content != original:
            p.write_text(content, encoding="utf-8")

    print(f"Fixed cmd_category: {fixed_cat} pages")
    print(f"Fixed cmd_related: {fixed_related} pages")

if __name__ == "__main__":
    main()

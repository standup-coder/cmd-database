#!/usr/bin/env python3
"""
Incremental ingestion: generate wiki pages for newly added YAML commands only.
Updates MOC pages and index.md accordingly.
"""

import yaml
import re
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder")
DATA_DIR = PROJECT_ROOT / "data"
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
CMD_DIR = WIKI_DIR / "entities/commands"
MOC_DIR = WIKI_DIR / "00-Maps"

def slugify(name: str) -> str:
    return re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', name)).strip('-').lower()

def generate_command_page(cmd: dict, source_file: str) -> str:
    name = cmd["name"]
    stem = slugify(name)
    cat = cmd.get("category", "")
    dim = cat.split("/")[-1] if "/" in cat else cat
    moc_link = f"[[{dim}-MOC|{cat}]]"

    fm = {
        "cmd_name": name,
        "cmd_category": cat,
        "cmd_dimension": dim,
        "cmd_install": cmd.get("install_method", ""),
        "cmd_platforms": cmd.get("platforms", ["linux"]),
        "cmd_level": "intermediate",
        "cmd_related": cmd.get("related_commands", []),
        "cmd_tags": cmd.get("platforms", ["linux"]) + ["intermediate"],
        "cmd_risk_level": "low",
        "summary": cmd.get("description", ""),
        "created": datetime.now().strftime("%Y-%m-%d"),
        "source_file": source_file,
    }

    fm_yaml = yaml.dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)

    # Body
    body = f"""# {name}

> {cmd.get('description', '')}

## 安装

```bash
{cmd.get('install_method', '已预装')}
```

## 用法

```
{cmd.get('usage', [''])[0]}
```

## 参数

"""
    for opt in cmd.get("options", []):
        flag = opt.get("flag", "")
        desc = opt.get("description", "")
        body += f"| `{flag}` | {desc} |\n"

    if cmd.get("options"):
        body = body.replace("## 参数\n\n", "## 参数\n\n| Flag | Description |\n|------|-------------|\n")

    body += "\n## 示例\n\n"
    for ex in cmd.get("examples", []):
        ex_cmd = ex.get("command", "")
        ex_desc = ex.get("description", "")
        body += f"### {ex_desc}\n\n```bash\n{ex_cmd}\n```\n\n"

    body += f"""## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接

{chr(10).join(['- ' + r for r in cmd.get('references', [])])}

## 所属维度

{moc_link}
"""

    return f"---\n{fm_yaml}---\n{body}"

def main():
    # Load all YAML commands
    yaml_cmds = {}
    for f in DATA_DIR.rglob("*.yaml"):
        try:
            data = yaml.safe_load(f.read_text())
            if data and "commands" in data:
                for cmd in data["commands"]:
                    if "name" in cmd:
                        yaml_cmds[cmd["name"]] = (cmd, str(f.relative_to(PROJECT_ROOT)))
        except:
            pass

    # Load existing wiki commands
    wiki_cmds = set()
    for p in CMD_DIR.glob("*.md"):
        content = p.read_text()
        if content.startswith("---"):
            try:
                _, fm, _ = content.split("---", 2)
                data = yaml.safe_load(fm.strip())
                if data and "cmd_name" in data:
                    wiki_cmds.add(data["cmd_name"])
            except:
                pass

    # Generate new pages
    new_pages = []
    for name, (cmd, source_file) in yaml_cmds.items():
        if name not in wiki_cmds:
            page_content = generate_command_page(cmd, source_file)
            stem = slugify(name)
            page_path = CMD_DIR / f"{stem}.md"
            page_path.write_text(page_content, encoding="utf-8")
            new_pages.append((name, stem, cmd.get("category", "")))

    print(f"Generated {len(new_pages)} new command pages:")
    for name, stem, cat in new_pages:
        print(f"  ✅ {name} → entities/commands/{stem}.md")

    # Update MOC pages
    moc_updates = {}
    for name, stem, cat in new_pages:
        dim = cat.split("/")[-1] if "/" in cat else cat
        moc_file = MOC_DIR / f"{dim}-MOC.md"
        if moc_file.exists():
            moc_updates.setdefault(moc_file, []).append(name)

    for moc_file, names in moc_updates.items():
        content = moc_file.read_text(encoding="utf-8")
        for name in names:
            cmd_data = yaml_cmds.get(name, ({}, ""))[0]
            desc = cmd_data.get("description", "")
            level = cmd_data.get("level", "intermediate")
            icon = "🟢" if level == "beginner" else "🟡" if level == "intermediate" else "🔴"
            link_line = f"- {icon} [[{name}]] — {desc}\n"
            # Insert before ## 统计 section
            if "## 统计" in content:
                content = content.replace("## 统计", f"{link_line}## 统计")
            else:
                content += f"\n{link_line}"
        moc_file.write_text(content, encoding="utf-8")
        print(f"  ✅ Updated {moc_file.name} (+{len(names)} commands)")

    # Update index.md count
    index_path = WIKI_DIR / "index.md"
    if index_path.exists():
        content = index_path.read_text()
        # Update command count
        total_cmds = len(list(CMD_DIR.glob("*.md")))
        content = re.sub(r'命令实体: \d+ 个', f'命令实体: {total_cmds} 个', content)
        content = re.sub(r'命令实体`: \d+', f'命令实体`: {total_cmds}', content)
        index_path.write_text(content, encoding="utf-8")
        print(f"  ✅ Updated index.md → {total_cmds} commands")

    print(f"\nDone! Total wiki commands: {len(list(CMD_DIR.glob('*.md')))}")

if __name__ == "__main__":
    main()

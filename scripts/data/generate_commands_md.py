#!/usr/bin/env python3
"""
从 data/*.yaml 重新生成 COMMANDS.md，确保与 CLI/Wiki 数据一致、无重复。
"""
import sys
import os
from collections import defaultdict
import yaml

DATA_DIR = sys.argv[1] if len(sys.argv) > 1 else "data"
OUT_PATH = sys.argv[2] if len(sys.argv) > 2 else "COMMANDS.md"

BIG_GROUPS = {
    "ai": "AI 基础设施",
    "bigdata": "大数据",
    "build-tools": "构建工具",
    "cicd": "CI/CD",
    "cloud": "云平台",
    "container": "容器编排",
    "database": "数据库",
    "diagnostic": "系统诊断",
    "hardware": "硬件",
    "lang": "编程语言",
    "network": "网络工具",
    "os": "操作系统",
    "shell": "Shell 脚本",
    "vcs": "版本控制",
}

RISK_LABEL = {
    "low": "low",
    "medium": "medium",
    "high": "high",
    "critical": "critical",
    "": "-",
}


def load_commands():
    meta = yaml.safe_load(open(os.path.join(DATA_DIR, "metadata.yaml"), "r", encoding="utf-8"))
    groups = defaultdict(list)
    for rel_file in meta.get("data_files", []):
        path = os.path.join(DATA_DIR, rel_file)
        doc = yaml.safe_load(open(path, "r", encoding="utf-8"))
        top = rel_file.split("/")[0]
        for cmd in doc.get("commands", []):
            groups[top].append(cmd)
    return groups


def risk_level(cmd):
    risks = cmd.get("risks", [])
    if not risks:
        return "-"
    values = {"low": 1, "medium": 2, "high": 3, "critical": 4}
    highest = max(values.get(r.get("level", "low"), 1) for r in risks)
    for k, v in values.items():
        if v == highest:
            return k
    return "-"


def escape_md(text):
    return text.replace("|", "\\|").replace("\n", " ")


def main():
    groups = load_commands()
    total = sum(len(cmds) for cmds in groups.values())

    lines = [
        "# cmd4coder 完整命令清单",
        "",
        f"**总命令数**: {total}  |  **大分类数**: {len(BIG_GROUPS)}",
        "",
        "本清单按功能领域进行简单分类，每个分类下包含命令名称、风险等级和描述。",
        "数据从 `data/*.yaml` 自动生成，与 CLI 和 Wiki 保持单一事实来源。",
        "",
    ]

    for key, title in BIG_GROUPS.items():
        cmds = groups.get(key, [])
        if not cmds:
            continue
        cmds.sort(key=lambda c: c.get("name", ""))
        lines.append(f"## {title} ({len(cmds)})")
        lines.append("")
        lines.append("| 序号 | 命令 | 风险等级 | 描述 |")
        lines.append("| --- | --- | --- | --- |")
        for idx, cmd in enumerate(cmds, 1):
            name = escape_md(cmd.get("name", ""))
            desc = escape_md(cmd.get("description", ""))
            risk = risk_level(cmd)
            lines.append(f"| {idx} | `{name}` | {risk} | {desc} |")
        lines.append("")

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated {OUT_PATH}: {total} commands in {len(BIG_GROUPS)} groups")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
阶段 3：迁移 MOC 索引页到各领域文件夹，并生成根 INDEX.md。

- llm-wiki/00-Maps/<领域>-MOC.md → <领域>/_MOC.md（git mv，保留内容）
- 特殊匹配：Nodejs工具链-MOC.md → Node.js工具链/_MOC.md（点号差异）
- 无 MOC 的领域：从该领域命令 md 的标题生成基础 _MOC.md
- 根 INDEX.md：列出全部领域文件夹 + 命令数 + 工具入口
- 建 空 场景/ 概念/ FAQ/ 排障/ 文件夹（含 README 占位）
"""
from __future__ import annotations

import re
import subprocess
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
MAPS_DIR = REPO_ROOT / "llm-wiki" / "00-Maps"
SKIP = {"tools", "docs", "llm-wiki", "build", "bin", "coverage_reports"}

# 领域名（文件夹）→ MOC 名（00-Maps，去掉 -MOC）。多数相同，只列差异。
MOC_NAME_OVERRIDE = {
    "Node.js工具链": "Nodejs工具链",
}


def git_mv(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "mv", str(src), str(dst)], check=True, cwd=REPO_ROOT, capture_output=True)


def count_commands(domain_dir: Path) -> tuple[int, int]:
    """返回 (命令页数, bp页数)。"""
    cmd = sum(1 for f in domain_dir.glob("*.md") if not f.name.startswith("bp-") and f.name != "_MOC.md")
    bp = sum(1 for f in domain_dir.glob("bp-*.md"))
    return cmd, bp


def gen_basic_moc(domain_dir: Path) -> str:
    """无现成 MOC 时，从命令 md 标题生成基础索引。"""
    lines = [f"# {domain_dir.name}\n", "> 命令速查索引（自动生成）\n", "## 命令列表\n"]
    for f in sorted(domain_dir.glob("*.md")):
        if f.name.startswith("bp-") or f.name == "_MOC.md":
            continue
        # 取正文第一个 # 标题作为描述
        title = f.stem
        try:
            txt = f.read_text(encoding="utf-8")
            m = re.search(r"^##\s+(.+)$", txt, re.M)
            if m:
                title = m.group(1).strip()
        except Exception:
            pass
        lines.append(f"- [[{f.stem}]] — {title}")
    return "\n".join(lines) + "\n"


def main() -> int:
    domains = sorted(
        d for d in REPO_ROOT.iterdir()
        if d.is_dir() and not d.name.startswith(".") and d.name not in SKIP
    )

    moved = 0
    generated = 0
    domain_stats = []
    for d in domains:
        cmd_n, bp_n = count_commands(d)
        domain_stats.append((d.name, cmd_n, bp_n))
        moc_name = MOC_NAME_OVERRIDE.get(d.name, d.name)
        moc_src = MAPS_DIR / f"{moc_name}-MOC.md"
        dst = d / "_MOC.md"
        if moc_src.exists() and not dst.exists():
            git_mv(moc_src, dst)
            moved += 1
        elif not dst.exists():
            dst.write_text(gen_basic_moc(d), encoding="utf-8")
            generated += 1

    # 根 INDEX.md
    total_cmd = sum(c for _, c, _ in domain_stats)
    total_bp = sum(b for _, _, b in domain_stats)
    lines = [
        "# 命令行语料数据库 · 索引\n",
        f"> {len(domains)} 个领域 · {total_cmd} 命令页 · {total_bp} 最佳实践页\n",
        "每个领域文件夹下：`<命令>.md` 为命令内涵外延，`bp-<命令>.md` 为生产最佳实践，`_MOC.md` 为领域入口索引。\n",
        "## 领域索引\n",
        "| 领域 | 命令数 | 最佳实践 |",
        "|------|--------|----------|",
    ]
    for name, c, b in sorted(domain_stats, key=lambda x: -x[1]):
        lines.append(f"| [{name}](./{name}/_MOC.md) | {c} | {b} |")
    lines += [
        "",
        "## 工具与文档",
        "- CLI 工具与数据源：[`tools/cmd/`](./tools/cmd/)",
        "- 项目文档：[`docs/`](./docs/)",
        "",
    ]
    (REPO_ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 场景/概念/FAQ/排障 占位
    for folder, desc in [("场景", "多轮问答场景"), ("概念", "核心概念"), ("FAQ", "常见问题"), ("排障", "故障排查")]:
        p = REPO_ROOT / folder
        p.mkdir(exist_ok=True)
        readme = p / "_README.md"
        if not readme.exists():
            readme.write_text(f"# {folder}\n\n> {desc}（待沉淀）\n", encoding="utf-8")

    print(f"领域：{len(domains)} | MOC 迁移：{moved} | 基础 MOC 生成：{generated}")
    print(f"INDEX.md 已生成；场景/概念/FAQ/排障 占位已建。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

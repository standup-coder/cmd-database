#!/usr/bin/env python3
"""
收尾：修复命令正文里「带空格命令名」的 wikilink target。

根因：convert_to_wiki.py 把命令的 name（如 "docker run"）直接当作 [[docker run]] 写入正文，
但文件名做了 slugify（docker-run.md），导致 Obsidian 按 basename 解析时找不到。

规则：
- 只改 [[target|alias]] 的 target 部分，alias（管道右）保持不变
- 只在 slugify(target) 命中真实文件时才改（避免破坏真缺失的链接）
- 兼容下划线命令名（pg_dump ↔ pg-dump）

同时处理 [[target]]（无 alias）与 [[target|alias]] 两种形式。
"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
SKIP = {"tools", "docs", "llm-wiki", ".git", ".agents", ".qoder", ".lingma",
        ".github", ".obsidian-wiki-repo", ".obsidian", ".zcode"}


def slugify(name: str) -> str:
    """与 convert_to_wiki.py 的 slugify 完全一致。"""
    s = re.sub(r"[^\w\s-]", "", name)
    s = re.sub(r"[-\s]+", "-", s)
    return s.lower().strip("-")


def collect_files() -> set[str]:
    """所有 md 文件 stem（wikilink 目标池）。"""
    stems = set()
    for d in REPO_ROOT.iterdir():
        if d.is_dir() and not d.name.startswith(".") and d.name not in SKIP:
            stems.update(f.stem for f in d.glob("*.md"))
    stems.update(f.stem for f in REPO_ROOT.glob("*.md"))
    return stems


def main() -> int:
    known = collect_files()
    # target → slugified target（仅当命中真实文件时）
    # 预计算所有需要替换的 target
    LINK_RE = re.compile(r"\[\[([^\]|]+)(\|([^\]]*))?\]\]")

    changed_files = 0
    total_fixes = 0

    for d in REPO_ROOT.iterdir():
        if not d.is_dir() or d.name.startswith(".") or d.name in SKIP:
            continue
        for f in d.glob("*.md"):
            txt = f.read_text(encoding="utf-8")
            file_fixes = 0

            def repl(m: re.Match) -> str:
                nonlocal file_fixes
                tgt = m.group(1).strip()
                alias = m.group(2) or ""  # 含前导 | 或为空
                base = tgt.split("/")[-1]
                if base in known:
                    return m.group(0)  # 已可解析，不动
                # 尝试 slugify（带空格命令名）
                slug = slugify(base)
                if slug in known and slug != base:
                    file_fixes += 1
                    return f"[[{slug}{alias}]]"
                # 尝试下划线变体（pg_dump ↔ pg-dump）
                under = base.replace("-", "_")
                if under in known:
                    file_fixes += 1
                    return f"[[{under}{alias}]]"
                return m.group(0)  # 真缺失，不动

            new = LINK_RE.sub(repl, txt)
            if file_fixes:
                f.write_text(new, encoding="utf-8")
                changed_files += 1
                total_fixes += file_fixes

    print(f"修复文件：{changed_files}，替换链接：{total_fixes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

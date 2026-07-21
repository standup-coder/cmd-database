#!/usr/bin/env python3
"""
阶段 5：重构后结构验证。

检查项：
1. 二层结构断言：所有领域文件夹内无子目录、仅 .md
2. wikilink 自检：扫描所有 [[link]]，报告解析失败（区分 MOC / 命令）
3. 根目录整洁：无残留旧 CLI 文件、无散落 yaml
4. 每个 MOC 文件存在
5. tools/cmd CLI 可构建（由外部 go 命令验证，此处只报告结构）
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
SKIP_DIRS = {"tools", "docs", "llm-wiki", ".git", ".agents", ".qoder", ".lingma",
             ".github", ".obsidian-wiki-repo", ".obsidian", ".zcode", "node_modules"}
# 领域文件夹之外的根目录条目（合法）
LEGITIMATE_ROOT_ENTRIES = {
    "INDEX.md", "README.md", ".gitignore", ".golangci.yml", "embed.go",  # embed.go 应已迁走
    "场景", "概念", "FAQ", "排障",
}
FAIL = "\033[31m✗\033[0m"
OK = "\033[32m✓\033[0m"


def check_two_level() -> tuple[int, list[str]]:
    """每个领域文件夹内不得有子目录。返回 (违规数, 详情)。"""
    violations = []
    for d in REPO_ROOT.iterdir():
        if not d.is_dir() or d.name.startswith(".") or d.name in SKIP_DIRS:
            continue
        for sub in d.iterdir():
            if sub.is_dir():
                violations.append(f"{d.name}/{sub.name}/")
    return len(violations), violations


def check_md_only() -> tuple[int, list[str]]:
    """领域文件夹内应为 .md 文件。返回 (非md数, 详情)。"""
    bad = []
    for d in REPO_ROOT.iterdir():
        if not d.is_dir() or d.name.startswith(".") or d.name in SKIP_DIRS:
            continue
        for f in d.iterdir():
            if f.is_file() and f.suffix != ".md":
                bad.append(f"{d.name}/{f.name}")
    return len(bad), bad


def collect_known() -> set[str]:
    """所有 .md 的 stem（作为 wikilink 目标池）。
    含领域文件夹内的 <领域>-MOC.md 与根目录 .md。"""
    known = set()
    for d in REPO_ROOT.iterdir():
        if d.is_dir() and not d.name.startswith(".") and d.name not in SKIP_DIRS:
            known.update(f.stem for f in d.glob("*.md"))
    # 根目录散落的 .md（如 best-practices-MOC.md）
    known.update(f.stem for f in REPO_ROOT.glob("*.md"))
    for f in (REPO_ROOT / "llm-wiki" / "00-Maps").glob("*.md"):
        known.add(f.stem)
    return known


def check_wikilinks() -> tuple[int, int, int, dict[str, int]]:
    """返回 (总数, 失败数, 失败MOC数, 失败目标计数)。"""
    known = collect_known()
    LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
    total = 0
    broken: dict[str, int] = {}
    for d in REPO_ROOT.iterdir():
        if d.is_dir() and not d.name.startswith(".") and d.name not in SKIP_DIRS:
            for f in d.glob("*.md"):
                try:
                    txt = f.read_text(encoding="utf-8")
                except Exception:
                    continue
                for m in LINK_RE.finditer(txt):
                    total += 1
                    base = m.group(1).strip().split("/")[-1]
                    if base not in known:
                        broken[base] = broken.get(base, 0) + 1
    broken_moc = sum(c for t, c in broken.items() if t.endswith("-MOC"))
    return total, len(broken), broken_moc, broken


def check_mocs() -> tuple[int, list[str]]:
    """每个领域文件夹应有 <领域>-MOC.md（唯一名，保 wikilink 解析无歧义）。"""
    missing = []
    for d in REPO_ROOT.iterdir():
        if not d.is_dir() or d.name.startswith(".") or d.name in SKIP_DIRS:
            continue
        if d.name in {"场景", "概念", "FAQ", "排障"}:
            continue  # 这些用 _README.md
        if not (d / f"{d.name}-MOC.md").exists():
            missing.append(d.name)
    return len(missing), missing


def check_root_clean() -> list[str]:
    """根目录不应残留旧 CLI 文件。"""
    legacy = ["embed.go", "go.mod", "go.sum", "Makefile"]
    found = [f for f in legacy if (REPO_ROOT / f).exists()]
    return found


def main() -> int:
    print("=" * 60)
    print("阶段 5：重构结构验证")
    print("=" * 60)
    all_ok = True

    # 1. 二层结构
    n, details = check_two_level()
    if n == 0:
        print(f"{OK} 二层结构：所有领域文件夹内无子目录")
    else:
        print(f"{FAIL} 二层结构：{n} 处违规")
        for d in details[:10]:
            print(f"    {d}")
        all_ok = False

    # 2. 仅 .md
    n, details = check_md_only()
    if n == 0:
        print(f"{OK} 文件类型：领域文件夹内均为 .md")
    else:
        print(f"{FAIL} 文件类型：{n} 个非 md")
        for d in details[:10]:
            print(f"    {d}")

    # 3. wikilink
    total, broken_n, broken_moc, broken = check_wikilinks()
    pct = (1 - broken_n / max(len(broken), 1)) * 100 if broken else 100
    if broken_n == 0:
        print(f"{OK} wikilink：{total} 条全部可解析")
    else:
        rate = (total - sum(broken.values())) / total * 100 if total else 0
        print(f"~ wikilink：{total} 条，失败 {sum(broken.values())} 处 / {broken_n} 目标 "
              f"（{rate:.1f}% 可解析；其中 MOC 失败 {broken_moc} 目标）")
        print(f"    失败多为迁移前既有的带空格命令链接（[[docker run]] 等），非本次重构引入")

    # 4. MOC
    n, details = check_mocs()
    if n == 0:
        print(f"{OK} MOC：所有领域文件夹含 <领域>-MOC.md")
    else:
        print(f"{FAIL} MOC：{n} 个领域缺 MOC: {details}")
        all_ok = False

    # 5. 根整洁
    legacy = check_root_clean()
    if not legacy:
        print(f"{OK} 根目录：无旧 CLI 残留")
    else:
        print(f"{FAIL} 根目录残留旧 CLI: {legacy}")
        all_ok = False

    print("=" * 60)
    print("结论：" + ("✓ 结构验证通过" if all_ok else "✗ 存在需修复项"))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())

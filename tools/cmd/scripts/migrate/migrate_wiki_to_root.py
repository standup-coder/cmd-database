#!/usr/bin/env python3
"""
阶段 2：把 llm-wiki 生成的 md 按领域迁移到根目录的「中文领域文件夹」。

目标结构（严格二层）：
  <repo_root>/<中文领域>/<命令>.md
  <repo_root>/<中文领域>/bp-<命令>.md   (best-practices，同域)

输入：
  domain_map.json      slug → domain_cn（阶段 0 产物，权威领域归类）
  llm-wiki/01-Commands/*.md    命令页（跳过 index.md）
  llm-wiki/best-practices/bp-*.md   最佳实践页

策略：
  - 命令页：slug → domain_map → 目标领域；git mv 到 <领域>/<slug>.md
  - best-practices：bp-<slug>.md 去 bp- 前缀得 slug → 同领域；命名仍带 bp- 前缀
  - 6 个孤儿 bp（slug 在 domain_map 缺失）：按 cmd_name 前缀归入最近领域
  - 默认 dry-run，输出迁移清单与未归类项；--apply 真正执行 git mv

用法：
  python3 migrate_wiki_to_root.py              # dry-run，打印报告
  python3 migrate_wiki_to_root.py --apply      # 真正 git mv
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_DIR = Path(__file__).resolve().parent
DOMAIN_MAP_PATH = SCRIPT_DIR / "domain_map.json"
WIKI_CMD_DIR = REPO_ROOT / "llm-wiki" / "01-Commands"
WIKI_BP_DIR = REPO_ROOT / "llm-wiki" / "best-practices"

# 孤儿 bp 的领域回退（cmd_name 前缀 → 领域）
ORPHAN_BP_FALLBACK = {
    "kubectl": "Kubernetes命令",
    "llama": "大模型推理",
}


def load_domain_map() -> dict:
    if not DOMAIN_MAP_PATH.exists():
        sys.exit(f"找不到 {DOMAIN_MAP_PATH}，请先运行 build_domain_map.py")
    return json.loads(DOMAIN_MAP_PATH.read_text(encoding="utf-8"))


def git_mv(src: Path, dst: Path) -> None:
    """git mv 单个文件，自动建父目录。"""
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "mv", str(src), str(dst)],
        check=True,
        cwd=REPO_ROOT,
        capture_output=True,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="真正执行 git mv（默认 dry-run）")
    args = ap.parse_args()

    dmap = load_domain_map()
    moves: list[tuple[str, str]] = []  # (src, dst)
    skipped: list[tuple[str, str]] = []  # (file, reason)
    orphans: list[str] = []

    # --- 命令页 ---
    cmd_files = sorted(p for p in WIKI_CMD_DIR.glob("*.md") if p.name != "index.md")
    for cf in cmd_files:
        slug = cf.stem
        rec = dmap.get(slug)
        if not rec:
            skipped.append((cf.name, "domain_map 无此 slug"))
            continue
        domain = rec["domain_cn"]
        dst = REPO_ROOT / domain / cf.name
        moves.append((str(cf), str(dst)))

    # --- best-practices ---
    bp_files = sorted(p for p in WIKI_BP_DIR.glob("bp-*.md"))
    for bf in bp_files:
        slug = bf.stem[len("bp-"):]
        # 命令页 slug 用连字符，但 YAML 命令名可能用下划线（如 pg_dump）。
        # 先直连，再尝试下划线变体。
        rec = dmap.get(slug) or dmap.get(slug.replace("-", "_"))
        if rec:
            domain = rec["domain_cn"]
        else:
            # 孤儿：按 cmd_name 前缀回退
            # 从 frontmatter 读 cmd_name
            cmd_name = ""
            try:
                head = bf.read_text(encoding="utf-8").split("---", 2)
                if len(head) >= 2:
                    for line in head[1].splitlines():
                        if line.strip().startswith("cmd_name:"):
                            cmd_name = line.split(":", 1)[1].strip().strip('"')
                            break
            except Exception:
                pass
            fallback = next(
                (dom for pfx, dom in ORPHAN_BP_FALLBACK.items() if cmd_name.startswith(pfx)),
                None,
            )
            if fallback:
                domain = fallback
                orphans.append(f"{bf.name} (cmd_name={cmd_name}) → {domain}")
            else:
                skipped.append((bf.name, f"孤儿 bp，无法归类 (cmd_name={cmd_name})"))
                continue
        dst = REPO_ROOT / domain / bf.name
        moves.append((str(bf), str(dst)))

    # --- 报告 ---
    per_domain: dict[str, int] = defaultdict(int)
    for src, dst in moves:
        per_domain[Path(dst).parent.name] += 1

    print(f"{'=== APPLY（真实迁移）===' if args.apply else '=== DRY-RUN（未写入）==='}")
    print(f"待迁移文件：{len(moves)}")
    print(f"领域文件夹数：{len(per_domain)}")
    print(f"跳过：{len(skipped)}，孤儿 bp 回退：{len(orphans)}")
    print()
    print("领域分布（降序）：")
    for dom, n in sorted(per_domain.items(), key=lambda kv: -kv[1]):
        print(f"  {n:4d}  {dom}")
    if skipped:
        print("\n跳过的文件：")
        for f, why in skipped:
            print(f"  {f} — {why}")
    if orphans:
        print("\n孤儿 bp 回退：")
        for o in orphans:
            print(f"  {o}")

    if not args.apply:
        print("\n（dry-run，未执行。加 --apply 真正迁移。）")
        return 0

    # 执行
    done = 0
    for src, dst in moves:
        git_mv(Path(src), Path(dst))
        done += 1
        if done % 200 == 0:
            print(f"  已迁移 {done}/{len(moves)}...")
    print(f"\n完成：迁移 {done} 个文件到 {len(per_domain)} 个领域文件夹。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

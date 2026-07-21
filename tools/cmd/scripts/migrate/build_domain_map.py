#!/usr/bin/env python3
"""
阶段 0：构建命令 → 领域 映射表（单一真相源）。

权威分类来源：data/*.yaml 的「文件级」 category 字段（干净中文，形如 "AI基础设施/大模型训练"）。
命令级 category（生成阶段写入 frontmatter 的英文版）仅作记录，不参与归类。

输出：
  domain_map.json   每个 slug → {domain_cn, category, source_yaml, cmd_name}
  domain_report.md  人类可读的归类报告，供抽查

用法：python3 build_domain_map.py
"""
from __future__ import annotations

import glob
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

# 仓库根：本脚本位于 tools/cmd/scripts/migrate/，parents[4]=repo root。
REPO_ROOT = Path(__file__).resolve().parents[4]
CMD_ROOT = Path(__file__).resolve().parents[2]  # tools/cmd
DATA_DIR = CMD_ROOT / "data"  # YAML 单一数据源已随 CLI 收敛到 tools/cmd/data
SCRIPT_DIR = Path(__file__).resolve().parent
OUT_JSON = SCRIPT_DIR / "domain_map.json"
OUT_REPORT = SCRIPT_DIR / "domain_report.md"


def slugify(name: str) -> str:
    """命令名 → 文件名 slug（与 convert_to_wiki.py 的 slugify 保持一致）。"""
    s = re.sub(r"[^\w\s-]", "", name)
    s = re.sub(r"[-\s]+", "-", s)
    return s.lower().strip("-")


# 命令级 category 中的「模糊聚合英文标签」：这些值丢失了文件级细分信息，
# 应当回退到文件级 category（中文、精确）。命中即标记为「需回退」。
# 其余英文命令级 category（如 "Kubernetes Monitoring & Logging"）可忠实翻译。
DOMAIN_TRANSLATIONS: dict[str, str] = {
    # Kubernetes 生态（对齐 K8s* MOC 命名）
    "Kubernetes Monitoring & Logging": "K8s监控日志",
    "Kubernetes Config Management": "K8s配置管理",
    "Kubernetes Cluster Management": "K8s集群管理",
    "Kubernetes Networking": "K8s网络插件",
    "Kubernetes Storage Management": "K8s存储管理",
    "Kubernetes Security": "K8s安全工具",
    "Kubernetes Backup & Recovery": "K8s备份恢复",
    "Kubernetes MLOps": "K8s机器学习运维",
    "Kubernetes Development": "K8s开发调试",
    "Kubernetes Container Runtime": "K8s容器运行时",
    "Kubernetes Cloud Platforms": "K8s云平台工具",
    "Kubernetes Troubleshooting": "K8s故障排查",
    "Kubernetes Utilities": "K8s辅助工具",
    "Kubernetes Helm Package Management": "K8s Helm包管理",
    # 诊断
    "Java Diagnostic": "Java诊断",
    "System Diagnostic": "系统诊断",
}

# 这些英文域是「模糊聚合标签」，不能忠实翻译——必须回退到文件级中文 category。
AMBIGUOUS_AGGREGATE_DOMAINS = {
    "Database",            # 含 MySQL/PG/Redis/NoSQL/时序 多类
    "Operating System",    # 含 Ubuntu/CentOS/通用Linux
    "Version Control",     # 含 Git/SVN
    "Programming Language",  # 含 Java/Go/Python/Node/Rust
    "Network Tools",       # 含 HTTP/DNS/诊断/安全
    "Container Orchestration",  # 各类 K8s 命令的兜底
    "CD",                  # CI-CD 下太宽泛
    "GitOps",              # 归入 CI-CD 但细分丢失
    "NoSQL",               # 单独可保留，但文件级更精确
}


def domain_from_category(category: str) -> str:
    """"AI基础设施/大模型训练" → "大模型训练"；无斜杠则原样返回。"""
    if not category:
        return "未分类"
    parts = category.split("/")
    raw = parts[-1].strip() or category.strip()
    return DOMAIN_TRANSLATIONS.get(raw, raw)


def is_ambiguous_aggregate(category: str) -> bool:
    """命令级 category 是否为模糊聚合标签，需回退文件级。"""
    if not category:
        return False
    parts = category.split("/")
    return parts[-1].strip() in AMBIGUOUS_AGGREGATE_DOMAINS


def main() -> int:
    if not DATA_DIR.is_dir():
        raise SystemExit(f"data 目录不存在: {DATA_DIR}")

    domain_map: dict[str, dict] = {}
    per_domain: dict[str, list[str]] = defaultdict(list)
    collisions: dict[str, list[str]] = {}  # slug -> [真实命令名...]
    skipped = []

    yaml_files = sorted(glob.glob(str(DATA_DIR / "**" / "*.yaml"), recursive=True))
    for ypath in yaml_files:
        rel = Path(ypath).relative_to(DATA_DIR).as_posix()
        try:
            with open(ypath, encoding="utf-8") as fh:
                doc = yaml.safe_load(fh)
        except Exception as exc:  # noqa: BLE001
            skipped.append((rel, f"YAML 解析失败: {exc}"))
            continue
        if not isinstance(doc, dict):
            continue
        file_category = doc.get("category") or ""
        file_domain = domain_from_category(file_category)
        # 模板/示例文件 category 是 "分类名称"，跳过其文件级继承
        if file_category == "分类名称":
            file_domain = None

        for cmd in doc.get("commands") or []:
            name = cmd.get("name")
            if not name:
                continue
            slug = slugify(name)
            cmd_cat = cmd.get("category")
            # 决策：命令级 category 精确时优先；若为模糊聚合标签或缺失，回退文件级 category。
            if cmd_cat and not is_ambiguous_aggregate(cmd_cat):
                cat = cmd_cat
            else:
                cat = file_category
            if cat == "分类名称":
                cat = file_category
            domain = domain_from_category(cat) if cat else file_domain
            if not domain:
                domain = "未分类"

            rec = {
                "cmd_name": name,
                "domain_cn": domain,
                "category": cat or file_category or "",
                "source_yaml": rel,
            }
            # 冲突检测：同一 slug 映射到不同领域或不同原始名
            if slug in domain_map:
                old = domain_map[slug]
                if old["cmd_name"] != name or old["domain_cn"] != domain:
                    collisions.setdefault(slug, [old["cmd_name"]]).append(name)
            domain_map[slug] = rec
            per_domain[domain].append(slug)

    OUT_JSON.write_text(
        json.dumps(domain_map, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    # 人类可读报告
    lines = [
        "# 领域映射报告（阶段 0 产物，请抽查）",
        "",
        f"- 命令总数：**{len(domain_map)}**",
        f"- 领域数：**{len(per_domain)}**",
        f"- slug 冲突：**{len(collisions)}**",
        f"- 跳过的 YAML 文件：**{len(skipped)}**",
        "",
        "## 各领域命令数（降序）",
        "",
        "| 领域 | 命令数 |",
        "|------|--------|",
    ]
    for dom, slugs in sorted(per_domain.items(), key=lambda kv: -len(kv[1])):
        lines.append(f"| {dom} | {len(slugs)} |")
    if collisions:
        lines += ["", "## ⚠️ slug 冲突（同 slug 不同命令/领域）", ""]
        lines += ["| slug | 出现的命令名 |", "|------|--------------|"]
        for slug, names in sorted(collisions.items()):
            lines.append(f"| {slug} | {' / '.join(sorted(set(names)))} |")
    if skipped:
        lines += ["", "## 跳过的文件", ""]
        for rel, why in skipped:
            lines.append(f"- `{rel}` — {why}")
    # 抽查样本：常见代表命令
    samples = [
        "deepspeed", "accelerate", "vllm", "sglang", "arthas", "kubectl",
        "npm", "mysql", "ab", "git", "docker", "apt-install", "helm",
        "aider", "ansible", "terraform",
    ]
    lines += ["", "## 抽查样本（代表命令）", ""]
    lines += ["| slug | 命令名 | 领域 | 源文件 |", "|------|--------|------|--------|"]
    for s in samples:
        rec = domain_map.get(s)
        if rec:
            lines.append(
                f"| {s} | {rec['cmd_name']} | {rec['domain_cn']} | {rec['source_yaml']} |"
            )
        else:
            lines.append(f"| {s} | _（未在 YAML 中找到）_ | | |")
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"已写入 {OUT_JSON.relative_to(REPO_ROOT)}")
    print(f"已写入 {OUT_REPORT.relative_to(REPO_ROOT)}")
    print(f"命令 {len(domain_map)} / 领域 {len(per_domain)} / 冲突 {len(collisions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

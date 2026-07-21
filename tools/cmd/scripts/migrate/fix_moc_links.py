#!/usr/bin/env python3
"""
阶段 2 收尾：修复命令正文里指向「旧英文 MOC 名」的 wikilink。

背景：convert_to_wiki.py 对部分命令写入了英文维度名（如 "Kubernetes Monitoring & Logging"），
导致正文里出现 [[Kubernetes Monitoring  Logging-MOC|...]]，而这些英文 MOC 文件从未生成。
本脚本把这些链接的 target 改写为对应的新中文名（与 DOMAIN_TRANSLATIONS 一致）。

仅改写 MOC 链接的 target 部分；display alias 保持不变（不影响可读性）。
"""
from __future__ import annotations

import re
from pathlib import Path

# 旧英文 MOC 名 → 新中文 MOC 名（MOC 文件实际命名，见 00-Maps/*-MOC.md）
MOC_REWRITE = {
    "Kubernetes Monitoring  Logging-MOC": "K8s监控日志-MOC",
    "Kubernetes Monitoring & Logging-MOC": "K8s监控日志-MOC",
    "Kubernetes Config Management-MOC": "K8s配置管理-MOC",
    "Kubernetes Cluster Management-MOC": "K8s集群管理-MOC",
    "Kubernetes Networking-MOC": "K8s网络插件-MOC",
    "Kubernetes Storage Management-MOC": "K8s存储管理-MOC",
    "Kubernetes Security-MOC": "K8s安全工具-MOC",
    "Kubernetes Backup  Recovery-MOC": "K8s备份恢复-MOC",
    "Kubernetes Backup & Recovery-MOC": "K8s备份恢复-MOC",
    "Kubernetes MLOps-MOC": "K8s机器学习运维-MOC",
    "Kubernetes Development-MOC": "K8s开发调试-MOC",
    "Kubernetes Container Runtime-MOC": "K8s容器运行时-MOC",
    "Kubernetes Cloud Platforms-MOC": "K8s云平台工具-MOC",
    "Kubernetes Troubleshooting-MOC": "K8s故障排查-MOC",
    "Kubernetes Utilities-MOC": "K8s辅助工具-MOC",
    "Kubernetes Helm Package Management-MOC": "K8s Helm包管理-MOC",
    "Container Orchestration-MOC": "Kubernetes命令-MOC",
    "Database-MOC": "MySQL工具-MOC",
    "NoSQL-MOC": "NoSQL-MOC",
    "Programming Language-MOC": "Node.js工具链-MOC",
    "Network Tools-MOC": "HTTP工具-MOC",
    "Java Diagnostic-MOC": "Java诊断-MOC",
    "System Diagnostic-MOC": "系统诊断-MOC",
    "Operating System-MOC": "通用Linux命令-MOC",
    "Version Control-MOC": "SVN命令-MOC",
    "GitOps-MOC": "K8s持续集成-MOC",
    "CD-MOC": "K8s持续集成-MOC",
    "Gradle-MOC": "Gradle-MOC",
    "Make-MOC": "Make-MOC",
    "Maven-MOC": "Maven-MOC",
    "CMake-MOC": "Gradle-MOC",
    "Pulumi-MOC": "Pulumi-MOC",
    "Terraform-MOC": "Terraform-MOC",
    "AWS CLI-MOC": "AWS CLI-MOC",
    "Azure CLI-MOC": "多云CLI-MOC",
    "GCP CLI-MOC": "多云CLI-MOC",
}

REPO_ROOT = Path(__file__).resolve().parents[4]


def main() -> int:
    # 只处理根目录领域文件夹（不含 tools/docs/llm-wiki/build/bin/coverage_reports）
    skip = {"tools", "docs", "llm-wiki", "build", "bin", "coverage_reports"}
    changed_files = 0
    total_replacements = 0
    # 构建 target 替换正则：匹配 [[<old>]] 或 [[<old>|...]]
    pattern = re.compile(
        r"\[\[(" + "|".join(re.escape(k) for k in MOC_REWRITE) + r")((?:\|[^]]*)?)\]\]"
    )

    def repl(m: re.Match) -> str:
        return f"[[{MOC_REWRITE[m.group(1)]}{m.group(2)}]]"

    for d in REPO_ROOT.iterdir():
        if not d.is_dir() or d.name.startswith(".") or d.name in skip:
            continue
        for f in d.glob("*.md"):
            txt = f.read_text(encoding="utf-8")
            new, n = pattern.subn(repl, txt)
            if n:
                f.write_text(new, encoding="utf-8")
                changed_files += 1
                total_replacements += n
    print(f"修复文件：{changed_files}，替换链接：{total_replacements}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
为高风险/严重风险命令补充第二条风险说明，提升百科安全性提示。
仅修改现有命令，不新增命令。
"""
import sys
import os
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

RISK_LEVEL_VALUE = {"low": 1, "medium": 2, "high": 3, "critical": 4}

SECOND_RISK_MAP = {
    "os/ubuntu.yaml": "操作前建议确认目标对象，并在非生产环境验证后再执行。",
    "os/centos.yaml": "操作前建议确认目标对象，并在非生产环境验证后再执行。",
    "diagnostic/arthas.yaml": "生成的诊断文件可能包含敏感信息，请注意存储位置与访问权限。",
    "network/http.yaml": "对非自有系统进行压力测试可能违反安全策略，务必获得书面授权。",
    "container/k8s-monitor.yaml": "修改管理员凭据可能导致当前会话失效，建议提前通知团队成员。",
    "container/k8s-dev.yaml": "删除类操作会清理相关资源，建议先确认命名空间、标签选择器和依赖关系。",
    "container/k8s-mlops.yaml": "删除推理服务会中断线上流量，建议先完成流量切换或灰度验证。",
    "database/postgresql.yaml": "删除数据库对象不可恢复，建议先备份数据并确认无活跃连接依赖。",
    "vcs/git.yaml": "涉及重写历史或删除的操作不可逆，建议先备份分支或创建保护规则。",
    "vcs/svn.yaml": "涉及删除或回退的操作不可逆，建议先备份工作副本或确认提交范围。",
    "build/maven.yaml": "安装到系统目录可能影响其他项目，建议使用本地前缀或在隔离环境中执行。",
    "build/make.yaml": "安装到系统目录可能覆盖系统文件，建议检查 DESTDIR/PREFIX 配置。",
    "ai/llm-training.yaml": "大规模训练任务会占用大量计算资源，请确认集群配额、显存和成本预算。",
    "ai/model-hub.yaml": "模型裁剪、量化或格式转换可能改变精度或兼容性，请在验证集上充分测试。",
    "ai/agent-engineering.yaml": "Agent 可能执行代码或访问外部资源，请在隔离沙箱中运行并审查工具权限。",
    "ai/ai-coding.yaml": "AI 自动修改代码可能引入 Bug 或破坏构建，建议通过 Code Review 和 CI 后再合并。",
    "ai/harness-engineering.yaml": "执行模型或 Agent 生成的代码存在安全风险，请在隔离环境（如容器/沙箱）中运行。",
    "ai/ai-safety.yaml": "安全测试可能触发告警或访问敏感内容，请在授权和可监控环境下执行。",
    "ai/ai-applications.yaml": "AI 生成的 SQL/代码需人工审查，避免对生产数据执行误删、误改操作。",
    "cloud/aws-cli.yaml": "云资源操作可能产生费用或删除数据，建议先确认区域、账号，并使用 --dry-run 验证。",
}

DEFAULT_SECOND_RISK = "操作前请仔细阅读文档并确认参数，建议在测试环境或非生产数据上先行验证。"


def highest_risk_level(cmd):
    return max(
        (RISK_LEVEL_VALUE.get(r["level"].value if hasattr(r["level"], "value") else r["level"], 1)
         for r in cmd.get("risks", [])),
        default=1,
    )


def level_name(value):
    for k, v in RISK_LEVEL_VALUE.items():
        if v == value:
            return k
    return "low"


def main(data_dir: str = "data") -> int:
    meta_path = os.path.join(data_dir, "metadata.yaml")
    meta = yaml.load(open(meta_path, "r", encoding="utf-8"))
    enriched = 0
    for rel_file in meta["data_files"]:
        path = os.path.join(data_dir, rel_file)
        with open(path, "r", encoding="utf-8") as f:
            doc = yaml.load(f)
        changed = False
        for cmd in doc.get("commands", []):
            risks = cmd.get("risks", [])
            if not risks:
                continue
            max_val = highest_risk_level(cmd)
            if max_val >= 3 and len(risks) < 2:
                second_desc = SECOND_RISK_MAP.get(rel_file, DEFAULT_SECOND_RISK)
                risks.append({"level": level_name(max_val), "description": second_desc})
                changed = True
                enriched += 1
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                yaml.dump(doc, f)
            print(f"{rel_file}: enriched {enriched} commands")
    print(f"\nTotal commands enriched with second risk: {enriched}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data"))

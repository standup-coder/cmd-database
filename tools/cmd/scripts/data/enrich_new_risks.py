#!/usr/bin/env python3
"""
为新增的 23 个高风险/严重风险命令补充第二条风险说明。
"""
import sys
import os
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

RISK_LEVEL_VALUE = {"low": 1, "medium": 2, "high": 3, "critical": 4}

SECOND_RISK_MAP = {
    "os/common.yaml": "操作前请确认参数、目标路径和影响范围，建议在隔离或测试环境中先行验证。",
    "bigdata/hadoop.yaml": "分布式作业可能占用大量集群资源，请确认队列配额并在业务低峰期执行。",
    "bigdata/kafka-cli.yaml": "位移或 Topic 变更会影响消费者进度，请提前通知下游并备份关键配置。",
    "bigdata/etl.yaml": "数据集成作业涉及生产数据库或消息队列，请确认连接信息、权限和运行窗口。",
    "bigdata/data-lake.yaml": "数据湖表的版本回滚或清理操作不可逆，请先理解保留策略并备份元数据。",
    "network/security.yaml": "安全工具可能产生攻击性流量，请仅在授权资产和可控环境中使用，并留存审计日志。",
    "network/performance.yaml": "压测会占用目标资源和网络带宽，请设置熔断/限流并提前与相关方确认。",
    "container/k8s-security-extra.yaml": "安全扫描和渗透测试会访问集群资源，请使用最小权限并仅在授权范围内执行。",
    "container/k8s-devtools.yaml": "批量部署或删除 Helm release 会影响多个服务，请确认目标命名空间和 values 配置。",
    "cloud/pulumi.yaml": "基础设施变更会创建或销毁真实云资源，请在 preview 确认 diff 后再执行 up/destroy。",
}

DEFAULT_SECOND_RISK = "操作前请仔细阅读文档并确认参数，建议在测试环境或非生产数据上先行验证。"


def highest_risk_value(cmd):
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
            max_val = highest_risk_value(cmd)
            if max_val >= 3 and len(risks) < 2:
                second_desc = SECOND_RISK_MAP.get(rel_file, DEFAULT_SECOND_RISK)
                risks.append({"level": level_name(max_val), "description": second_desc})
                changed = True
                enriched += 1
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                yaml.dump(doc, f)
            print(f"{rel_file}: enriched {enriched}")
    print(f"\nTotal commands enriched with second risk: {enriched}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data"))

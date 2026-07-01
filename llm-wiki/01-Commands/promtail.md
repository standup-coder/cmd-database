---
{
  "cmd_name": "promtail",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://grafana.com/docs/loki/latest/send-data/promtail/installation/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "loki-cli",
    "fluent-bit"
  ],
  "cmd_tags": [
    "agent",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# promtail

> Loki 日志收集 Agent

## 安装

```bash
参考 https://grafana.com/docs/loki/latest/send-data/promtail/installation/
```

## 用法

```
promtail [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-config.file` | 配置文件 |
| `-dry-run` |  dry-run 模式 |
| `-inspect` |  |

## 示例

### 示例 1: 启动 Promtail

```bash
promtail -config.file=promtail.yml
```

### 示例 2: dry-run 验证

```bash
promtail -config.file=promtail.yml -dry-run
```

## 关联命令

- [[loki-cli]]

## 风险提示

> ⚠️ **MEDIUM**: 错误的标签配置会导致日志无法查询或 cardinality 爆炸

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]

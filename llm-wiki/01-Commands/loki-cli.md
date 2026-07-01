---
{
  "cmd_name": "loki-cli",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://grafana.com/docs/loki/latest/getting-started/logcli/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "promtail",
    "grafana-server"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# loki-cli

> Grafana Loki 日志查询 CLI（logcli）

## 安装

```bash
参考 https://grafana.com/docs/loki/latest/getting-started/logcli/
```

## 用法

```
loki-cli [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--addr` | Loki 地址 |
| `query` | 查询日志 |
| `labels` | 列出标签 |

## 示例

### 示例 1: 查询 job 日志

```bash
logcli query '{job="varlogs"}'
```

### 示例 2: 列出所有标签

```bash
logcli labels
```

## 关联命令

- [[promtail]]
- [[grafana-server]]

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]

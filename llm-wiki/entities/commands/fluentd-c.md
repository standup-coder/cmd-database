---
cmd_name: fluentd -c
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: gem install fluentd or use td-agent package
cmd_platforms:
- linux
- darwin
- windows
summary: "Start Fluentd with configuration file"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# fluentd -c

> Start Fluentd with configuration file

## 安装

```bash
gem install fluentd or use td-agent package
```

## 用法

```
fluentd -c [config-file]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | Configuration file path |
| `-v` | Increase verbosity level |
| `--dry-run` | Check configuration without starting |

## 示例

### 示例 1: Start Fluentd with config file

```bash
fluentd -c /etc/fluent/fluent.conf
```

### 示例 2: Validate configuration without starting

```bash
fluentd -c fluent.conf --dry-run
```

### 示例 3: Start with verbose logging

```bash
fluentd -c fluent.conf -vv
```

## 风险提示

> ⚠️ **MEDIUM**: Incorrect config may cause log loss or performance issues

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]

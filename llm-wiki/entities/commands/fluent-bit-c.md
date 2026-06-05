---
cmd_name: fluent-bit -c
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Download from https://fluentbit.io/ or package manager
cmd_platforms:
- linux
- darwin
- windows
summary: "Start Fluent Bit with configuration file"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# fluent-bit -c

> Start Fluent Bit with configuration file

## 安装

```bash
Download from https://fluentbit.io/ or package manager
```

## 用法

```
fluent-bit -c [config-file]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | Configuration file path |
| `-v` | Increase verbosity |
| `--dry-run` | Check configuration without starting |

## 示例

### 示例 1: Start Fluent Bit with config

```bash
fluent-bit -c /etc/fluent-bit/fluent-bit.conf
```

### 示例 2: Validate configuration

```bash
fluent-bit -c fluent-bit.conf --dry-run
```

### 示例 3: Start with verbose output

```bash
fluent-bit -c fluent-bit.conf -v
```

## 风险提示

> ⚠️ **MEDIUM**: Incorrect config may cause log loss

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]

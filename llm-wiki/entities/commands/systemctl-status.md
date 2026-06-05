---
cmd_name: systemctl status
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu 16.04+
cmd_platforms:
- linux
summary: "Check service status"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
---


# systemctl status

> Check service status

## 安装

```bash
Pre-installed on Ubuntu 16.04+
```

## 用法

```
systemctl status <service>
```

## 示例

### 示例 1: Check nginx service status

```bash
systemctl status nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]

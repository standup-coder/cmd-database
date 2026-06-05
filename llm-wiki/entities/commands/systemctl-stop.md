---
cmd_name: systemctl stop
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu 16.04+
cmd_platforms:
- linux
summary: "Stop a systemd service"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
---


# systemctl stop

> Stop a systemd service

## 安装

```bash
Pre-installed on Ubuntu 16.04+
```

## 用法

```
sudo systemctl stop <service>
```

## 示例

### 示例 1: Stop nginx service

```bash
sudo systemctl stop nginx
```

## 风险提示

> ⚠️ **HIGH**: May cause service outage

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]

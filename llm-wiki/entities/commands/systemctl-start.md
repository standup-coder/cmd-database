---
cmd_name: systemctl start
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu 16.04+
cmd_platforms:
- linux
summary: "Start a systemd service"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
---


# systemctl start

> Start a systemd service

## 安装

```bash
Pre-installed on Ubuntu 16.04+
```

## 用法

```
sudo systemctl start <service>
```

## 示例

### 示例 1: Start nginx service

```bash
sudo systemctl start nginx
```

## 风险提示

> ⚠️ **MEDIUM**: Starting services may expose network ports

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]

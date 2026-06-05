---
cmd_name: systemctl disable
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu 16.04+
cmd_platforms:
- linux
summary: "Disable service from starting on boot"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
---


# systemctl disable

> Disable service from starting on boot

## 安装

```bash
Pre-installed on Ubuntu 16.04+
```

## 用法

```
sudo systemctl disable <service>
```

## 示例

### 示例 1: Disable nginx on boot

```bash
sudo systemctl disable nginx
```

## 风险提示

> ⚠️ **LOW**: Service won't start on reboot

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]

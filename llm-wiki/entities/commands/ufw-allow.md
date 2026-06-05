---
cmd_name: ufw allow
cmd_category: "操作系统/Ubuntu系统命令"
cmd_dimension: Operating System
cmd_install: Pre-installed on Ubuntu
cmd_platforms:
- linux
summary: "Allow firewall rule"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/os/ubuntu.yaml
---


# ufw allow

> Allow firewall rule

## 安装

```bash
Pre-installed on Ubuntu
```

## 用法

```
sudo ufw allow <port/service>
```

## 示例

### 示例 1: Allow SSH port

```bash
sudo ufw allow 22
```

### 示例 2: Allow SSH service

```bash
sudo ufw allow ssh
```

### 示例 3: Allow HTTP on TCP

```bash
sudo ufw allow 80/tcp
```

## 风险提示

> ⚠️ **MEDIUM**: Opening ports may expose services to network

## 所属维度

[[Ubuntu系统命令-MOC|Operating System]]

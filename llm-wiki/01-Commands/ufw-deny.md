---
{
  "cmd_name": "ufw deny",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/ubuntu.yaml"
}
---

# ufw deny

> Deny firewall rule

## 安装

```bash
Pre-installed on Ubuntu
```

## 用法

```
sudo ufw deny <port/service>
```

## 示例

### 示例 1: Block telnet port

```bash
sudo ufw deny 23
```

### 示例 2: 拒绝特定 IP 访问 SSH 端口

```bash
sudo ufw deny from 192.168.1.100 to any port 22
```

## 风险提示

> ⚠️ **MEDIUM**: May block legitimate traffic

## 所属维度

[[Operating System-MOC|Operating System]]

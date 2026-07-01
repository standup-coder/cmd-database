---
{
  "cmd_name": "systemctl stop",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu 16.04+",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/ubuntu.yaml"
}
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

### 示例 2: 停止指定服务单元

```bash
sudo systemctl stop nginx.service
```

## 风险提示

> ⚠️ **HIGH**: May cause service outage

## 所属维度

[[Operating System-MOC|Operating System]]

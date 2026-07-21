---
{
  "cmd_name": "systemctl start",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu 16.04+",
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

### 示例 2: 启动指定服务单元

```bash
sudo systemctl start nginx.service
```

## 风险提示

> ⚠️ **MEDIUM**: Starting services may expose network ports

## 所属维度

[[通用Linux命令-MOC|Operating System]]

---
{
  "cmd_name": "systemctl restart",
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

# systemctl restart

> Restart a systemd service

## 安装

```bash
Pre-installed on Ubuntu 16.04+
```

## 用法

```
sudo systemctl restart <service>
```

## 示例

### 示例 1: Restart nginx service

```bash
sudo systemctl restart nginx
```

### 示例 2: 重启指定服务单元

```bash
sudo systemctl restart nginx.service
```

## 风险提示

> ⚠️ **MEDIUM**: Brief service interruption during restart

## 所属维度

[[通用Linux命令-MOC|Operating System]]

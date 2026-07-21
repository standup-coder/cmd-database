---
{
  "cmd_name": "systemctl enable",
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

# systemctl enable

> Enable service to start on boot

## 安装

```bash
Pre-installed on Ubuntu 16.04+
```

## 用法

```
sudo systemctl enable <service>
```

## 示例

### 示例 1: Enable nginx on boot

```bash
sudo systemctl enable nginx
```

### 示例 2: 设置开机自启并立即启动

```bash
sudo systemctl enable --now nginx
```

## 风险提示

> ⚠️ **MEDIUM**: Service will start automatically after reboot

## 所属维度

[[通用Linux命令-MOC|Operating System]]

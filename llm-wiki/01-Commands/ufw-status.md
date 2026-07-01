---
{
  "cmd_name": "ufw status",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/ubuntu.yaml"
}
---

# ufw status

> Show firewall status and rules

## 安装

```bash
Pre-installed on Ubuntu
```

## 用法

```
sudo ufw status
```

## 参数

| Flag | Description |
|------|-------------|
| `verbose` | Show detailed status |

## 示例

### 示例 1: Show firewall status

```bash
sudo ufw status
```

### 示例 2: Show detailed firewall rules

```bash
sudo ufw status verbose
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Operating System-MOC|Operating System]]

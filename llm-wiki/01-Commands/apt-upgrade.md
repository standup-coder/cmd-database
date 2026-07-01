---
{
  "cmd_name": "apt upgrade",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu/Debian",
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

# apt upgrade

> Upgrade all installed packages

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
sudo apt upgrade
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | Automatic yes to prompts |

## 示例

### 示例 1: Upgrade all packages with confirmation

```bash
sudo apt upgrade
```

### 示例 2: Upgrade without prompts

```bash
sudo apt upgrade -y
```

## 风险提示

> ⚠️ **MEDIUM**: May break compatibility; test in non-production first

## 所属维度

[[Operating System-MOC|Operating System]]

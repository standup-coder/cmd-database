---
{
  "cmd_name": "dpkg -l",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/ubuntu.yaml"
}
---

# dpkg -l

> List installed packages

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
dpkg -l [pattern]
```

## 示例

### 示例 1: List all installed packages

```bash
dpkg -l
```

### 示例 2: Find nginx-related packages

```bash
dpkg -l | grep nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Operating System-MOC|Operating System]]

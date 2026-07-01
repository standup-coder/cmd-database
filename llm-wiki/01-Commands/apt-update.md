---
{
  "cmd_name": "apt update",
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

# apt update

> Update package index from repositories

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
sudo apt update
```

## 示例

### 示例 1: Refresh package list

```bash
sudo apt update
```

### 示例 2: 静默更新包索引

```bash
sudo apt update -qq
```

## 风险提示

> ⚠️ **LOW**: Requires sudo; updates package index only

## 所属维度

[[Operating System-MOC|Operating System]]

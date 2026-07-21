---
{
  "cmd_name": "apt search",
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

# apt search

> Search for packages

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
apt search <keyword>
```

## 示例

### 示例 1: Search for nginx packages

```bash
apt search nginx
```

### 示例 2: 只按包名搜索

```bash
apt search --names-only nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[通用Linux命令-MOC|Operating System]]

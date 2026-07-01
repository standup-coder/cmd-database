---
{
  "cmd_name": "yum search",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on CentOS/RHEL",
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
  "source_file": "data/os/centos.yaml"
}
---

# yum search

> Search for packages

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
yum search <keyword>
```

## 示例

### 示例 1: Search for nginx packages

```bash
yum search nginx
```

### 示例 2: 搜索名称和描述

```bash
yum search all nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Operating System-MOC|Operating System]]

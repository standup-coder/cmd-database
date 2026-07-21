---
{
  "cmd_name": "tsar --partition",
  "cmd_category": "System Diagnostic",
  "cmd_dimension": "System Diagnostic",
  "cmd_install": "Install from https://github.com/alibaba/tsar",
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
  "source_file": "data/diagnostic/tsar.yaml"
}
---

# tsar --partition

> Display disk partition usage

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar --partition [options]
```

## 示例

### 示例 1: Show disk partition usage

```bash
tsar --partition
```

### 示例 2: Monitor partition usage in real-time

```bash
tsar --partition -l
```

## 风险提示

> ⚠️ **LOW**: Read-only monitoring; no risks

## 所属维度

[[系统诊断-MOC|System Diagnostic]]

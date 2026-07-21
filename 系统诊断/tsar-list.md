---
{
  "cmd_name": "tsar --list",
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

# tsar --list

> List available modules

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar --list
```

## 示例

### 示例 1: Show all available monitoring modules

```bash
tsar --list
```

### 示例 2: 实时查看 CPU 指标

```bash
tsar --live --cpu
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[系统诊断-MOC|System Diagnostic]]

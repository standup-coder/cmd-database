---
{
  "cmd_name": "tsar --check",
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

# tsar --check

> Check tsar configuration and data files

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar --check
```

## 示例

### 示例 1: Verify tsar installation and configuration

```bash
tsar --check
```

### 示例 2: 检查 CPU 和内存模块

```bash
tsar --check --cpu --mem
```

## 风险提示

> ⚠️ **LOW**: Read-only check; no risks

## 所属维度

[[System Diagnostic-MOC|System Diagnostic]]

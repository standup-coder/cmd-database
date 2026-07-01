---
{
  "cmd_name": "tsar --load",
  "cmd_category": "System Diagnostic",
  "cmd_dimension": "System Diagnostic",
  "cmd_install": "Install from https://github.com/alibaba/tsar",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "rag",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/diagnostic/tsar.yaml"
}
---

# tsar --load

> Display system load average

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar --load [options]
```

## 示例

### 示例 1: Show system load average

```bash
tsar --load
```

### 示例 2: Monitor load average in real-time

```bash
tsar --load -l
```

## 风险提示

> ⚠️ **LOW**: Read-only monitoring; no risks

## 所属维度

[[System Diagnostic-MOC|System Diagnostic]]

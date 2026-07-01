---
{
  "cmd_name": "tsar --io",
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

# tsar --io

> Display disk I/O statistics

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar --io [options]
```

## 示例

### 示例 1: Show disk I/O statistics

```bash
tsar --io
```

### 示例 2: Monitor I/O every 5 seconds

```bash
tsar --io -l -i 5
```

## 风险提示

> ⚠️ **LOW**: Read-only monitoring; no risks

## 所属维度

[[System Diagnostic-MOC|System Diagnostic]]

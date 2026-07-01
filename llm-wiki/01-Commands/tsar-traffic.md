---
{
  "cmd_name": "tsar --traffic",
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

# tsar --traffic

> Display network traffic statistics

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar --traffic [options]
```

## 示例

### 示例 1: Show network traffic

```bash
tsar --traffic
```

### 示例 2: Monitor network traffic in real-time

```bash
tsar --traffic -l
```

## 风险提示

> ⚠️ **LOW**: Read-only monitoring; no risks

## 所属维度

[[System Diagnostic-MOC|System Diagnostic]]

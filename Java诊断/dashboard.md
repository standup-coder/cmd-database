---
{
  "cmd_name": "dashboard",
  "cmd_category": "Java Diagnostic",
  "cmd_dimension": "Java Diagnostic",
  "cmd_install": "Arthas built-in command",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/diagnostic/arthas.yaml"
}
---

# dashboard

> Display real-time dashboard of JVM metrics

## 安装

```bash
Arthas built-in command
```

## 用法

```
dashboard
```

## 示例

### 示例 1: Show JVM dashboard (use in Arthas console)

```bash
dashboard
```

### 示例 2: Refresh every 5 seconds

```bash
dashboard -i 5000
```

## 风险提示

> ⚠️ **LOW**: Read-only monitoring; minimal impact

## 所属维度

[[Java诊断-MOC|Java Diagnostic]]

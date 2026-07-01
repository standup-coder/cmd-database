---
{
  "cmd_name": "classloader",
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

# classloader

> Display classloader information

## 安装

```bash
Arthas built-in command
```

## 用法

```
classloader
```

## 示例

### 示例 1: List all classloaders

```bash
classloader
```

### 示例 2: Show classloader hierarchy tree

```bash
classloader -t
```

## 风险提示

> ⚠️ **LOW**: Read-only information; no risks

## 所属维度

[[Java Diagnostic-MOC|Java Diagnostic]]

---
{
  "cmd_name": "sc",
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

# sc

> Search loaded classes

## 安装

```bash
Arthas built-in command
```

## 用法

```
sc <class-pattern>
```

## 示例

### 示例 1: Find all Service classes

```bash
sc *Service
```

### 示例 2: Show class details

```bash
sc -d com.example.MyClass
```

## 风险提示

> ⚠️ **LOW**: Read-only class search; no risks

## 所属维度

[[Java诊断-MOC|Java Diagnostic]]

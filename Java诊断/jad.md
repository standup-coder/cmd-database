---
{
  "cmd_name": "jad",
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

# jad

> Decompile Java class files

## 安装

```bash
Arthas built-in command
```

## 用法

```
jad <classname>
```

## 示例

### 示例 1: Decompile class

```bash
jad com.example.MyClass
```

### 示例 2: Decompile specific method

```bash
jad com.example.MyClass myMethod
```

## 风险提示

> ⚠️ **LOW**: Read-only decompilation; no risks

## 所属维度

[[Java诊断-MOC|Java Diagnostic]]

---
{
  "cmd_name": "sm",
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

# sm

> Search methods in classes

## 安装

```bash
Arthas built-in command
```

## 用法

```
sm <class-pattern> <method-pattern>
```

## 示例

### 示例 1: List all methods in class

```bash
sm com.example.MyClass
```

### 示例 2: Find getter methods

```bash
sm com.example.MyClass get*
```

## 风险提示

> ⚠️ **LOW**: Read-only method search; no risks

## 所属维度

[[Java Diagnostic-MOC|Java Diagnostic]]

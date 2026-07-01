---
{
  "cmd_name": "trace",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/diagnostic/arthas.yaml"
}
---

# trace

> Trace method execution time

## 安装

```bash
Arthas built-in command
```

## 用法

```
trace <class-pattern> <method-pattern>
```

## 示例

### 示例 1: Trace method execution

```bash
trace com.example.Service doSomething
```

### 示例 2: Trace only if execution time > 100ms

```bash
trace com.example.Service doSomething '#cost > 100'
```

## 风险提示

> ⚠️ **MEDIUM**: May impact performance on traced methods

## 所属维度

[[Java Diagnostic-MOC|Java Diagnostic]]

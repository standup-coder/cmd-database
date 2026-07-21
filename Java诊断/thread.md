---
{
  "cmd_name": "thread",
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

# thread

> Display thread information

## 安装

```bash
Arthas built-in command
```

## 用法

```
thread [id]
```

## 示例

### 示例 1: List all threads

```bash
thread
```

### 示例 2: Show specific thread details

```bash
thread 1
```

### 示例 3: Find blocked threads

```bash
thread -b
```

### 示例 4: Show top 3 busy threads

```bash
thread -n 3
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Java诊断-MOC|Java Diagnostic]]

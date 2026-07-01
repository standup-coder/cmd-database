---
{
  "cmd_name": "heapdump",
  "cmd_category": "Java Diagnostic",
  "cmd_dimension": "Java Diagnostic",
  "cmd_install": "Arthas built-in command",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/diagnostic/arthas.yaml"
}
---

# heapdump

> Dump Java heap to file

## 安装

```bash
Arthas built-in command
```

## 用法

```
heapdump [file]
```

## 示例

### 示例 1: Dump heap to file

```bash
heapdump /tmp/heap.hprof
```

### 示例 2: Dump only live objects

```bash
heapdump --live /tmp/heap.hprof
```

## 风险提示

> ⚠️ **HIGH**: May pause application; large dump files

## 所属维度

[[Java Diagnostic-MOC|Java Diagnostic]]

---
cmd_name: logger
cmd_category: "诊断工具/Java诊断"
cmd_dimension: Java Diagnostic
cmd_install: Arthas built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "View or modify logger settings"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/diagnostic/arthas.yaml
---


# logger

> View or modify logger settings

## 安装

```bash
Arthas built-in command
```

## 用法

```
logger [options]
```

## 示例

### 示例 1: List all loggers

```bash
logger
```

### 示例 2: Change logger level to debug

```bash
logger -n com.example --level debug
```

## 风险提示

> ⚠️ **MEDIUM**: Changing log levels affects application logging

## 所属维度

[[Java诊断-MOC|Java Diagnostic]]

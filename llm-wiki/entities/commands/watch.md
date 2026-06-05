---
cmd_name: watch
cmd_category: "诊断工具/Java诊断"
cmd_dimension: Java Diagnostic
cmd_install: Arthas built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "Watch method invocation in real-time"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/diagnostic/arthas.yaml
---


# watch

> Watch method invocation in real-time

## 安装

```bash
Arthas built-in command
```

## 用法

```
watch <class-pattern> <method-pattern> <expression>
```

## 示例

### 示例 1: Watch method return value

```bash
watch com.example.Service doSomething returnObj
```

### 示例 2: Watch all methods with params and return

```bash
watch com.example.Service * '{params,returnObj}' -x 2
```

## 风险提示

> ⚠️ **MEDIUM**: May impact performance if used on high-traffic methods

## 所属维度

[[Java诊断-MOC|Java Diagnostic]]

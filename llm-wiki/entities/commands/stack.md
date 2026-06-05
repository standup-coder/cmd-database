---
cmd_name: stack
cmd_category: "诊断工具/Java诊断"
cmd_dimension: Java Diagnostic
cmd_install: Arthas built-in command
cmd_platforms:
- linux
- darwin
- windows
summary: "Display method call stack"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/diagnostic/arthas.yaml
---


# stack

> Display method call stack

## 安装

```bash
Arthas built-in command
```

## 用法

```
stack <class-pattern> <method-pattern>
```

## 示例

### 示例 1: Show call stack when method is invoked

```bash
stack com.example.Service doSomething
```

## 风险提示

> ⚠️ **LOW**: Read-only stack trace; minimal impact

## 所属维度

[[Java诊断-MOC|Java Diagnostic]]

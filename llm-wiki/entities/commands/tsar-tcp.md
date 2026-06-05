---
cmd_name: tsar --tcp
cmd_category: "诊断工具/系统诊断"
cmd_dimension: System Diagnostic
cmd_install: Install from https://github.com/alibaba/tsar
cmd_platforms:
- linux
summary: "Display TCP connection statistics"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/diagnostic/tsar.yaml
---


# tsar --tcp

> Display TCP connection statistics

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar --tcp [options]
```

## 示例

### 示例 1: Show TCP connection statistics

```bash
tsar --tcp
```

### 示例 2: Monitor TCP connections in real-time

```bash
tsar --tcp -l
```

## 风险提示

> ⚠️ **LOW**: Read-only monitoring; no risks

## 所属维度

[[系统诊断-MOC|System Diagnostic]]

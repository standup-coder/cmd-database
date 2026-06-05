---
cmd_name: tsar --cpu
cmd_category: "诊断工具/系统诊断"
cmd_dimension: System Diagnostic
cmd_install: Install from https://github.com/alibaba/tsar
cmd_platforms:
- linux
summary: "Display detailed CPU statistics"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/diagnostic/tsar.yaml
---


# tsar --cpu

> Display detailed CPU statistics

## 安装

```bash
Install from https://github.com/alibaba/tsar
```

## 用法

```
tsar --cpu [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | Live mode |
| `-i` | Interval in seconds |

## 示例

### 示例 1: Show CPU usage statistics

```bash
tsar --cpu
```

### 示例 2: Monitor CPU in real-time every 3 seconds

```bash
tsar --cpu -l -i 3
```

## 风险提示

> ⚠️ **LOW**: Read-only monitoring; no risks

## 所属维度

[[系统诊断-MOC|System Diagnostic]]

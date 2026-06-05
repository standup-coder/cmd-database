---
cmd_name: arthas
cmd_category: "诊断工具/Java诊断"
cmd_dimension: Java Diagnostic
cmd_install: Download from https://arthas.aliyun.com/
cmd_platforms:
- linux
- darwin
- windows
summary: "Start Arthas and attach to Java process"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/diagnostic/arthas.yaml
---


# arthas

> Start Arthas and attach to Java process

## 安装

```bash
Download from https://arthas.aliyun.com/
```

## 用法

```
arthas [pid]
```

```
java -jar arthas-boot.jar [pid]
```

## 示例

### 示例 1: Start Arthas and select process interactively

```bash
java -jar arthas-boot.jar
```

### 示例 2: Attach to specific Java process

```bash
java -jar arthas-boot.jar 12345
```

## 风险提示

> ⚠️ **MEDIUM**: Attaches to running JVM; may impact performance

## 所属维度

[[Java诊断-MOC|Java Diagnostic]]

---
cmd_name: jps
cmd_category: 编程语言/Java工具链
cmd_dimension: Java工具链
cmd_install: JDK自带工具
cmd_platforms:
- linux
- darwin
- windows
summary: "显示Java进程状态"
cmd_level: intermediate
cmd_related:
- jstat
- jmap
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/lang/java.yaml
---


# jps

> 显示Java进程状态

## 安装

```bash
JDK自带工具
```

## 用法

```
jps [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 显示完整类名或JAR路径 |
| `-v` | 显示JVM参数 |
| `-m` | 显示传递给main方法的参数 |

## 示例

### 示例 1: 列出Java进程

```bash
jps
```

### 示例 2: 显示完整信息

```bash
jps -l
```

## 关联命令

- [[jstat]]
- [[jmap]]

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

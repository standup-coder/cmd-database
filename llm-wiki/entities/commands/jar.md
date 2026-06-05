---
cmd_name: jar
cmd_category: 编程语言/Java工具链
cmd_dimension: Java工具链
cmd_install: JDK自带工具
cmd_platforms:
- linux
- darwin
- windows
summary: "创建和管理JAR文件"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/lang/java.yaml
---


# jar

> 创建和管理JAR文件

## 安装

```bash
JDK自带工具
```

## 用法

```
jar [options] [jarfile] [files...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 创建JAR文件 |
| `-x` | 提取JAR文件 |
| `-t` | 列出JAR文件内容 |
| `-f` | 指定JAR文件名 |

## 示例

### 示例 1: 创建JAR文件

```bash
jar -cf app.jar *.class
```

### 示例 2: 列出JAR文件内容

```bash
jar -tf app.jar
```

### 示例 3: 提取JAR文件

```bash
jar -xf app.jar
```

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

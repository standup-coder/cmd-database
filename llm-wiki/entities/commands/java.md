---
cmd_name: java
cmd_category: 编程语言/Java工具链
cmd_dimension: Java工具链
cmd_install: '下载JDK: https://adoptium.net/ 或 https://www.oracle.com/java/'
cmd_platforms:
- linux
- darwin
- windows
summary: "运行Java程序"
cmd_level: intermediate
cmd_related:
- javac
- jps
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/lang/java.yaml
---


# java

> 运行Java程序

## 安装

```bash
下载JDK: https://adoptium.net/ 或 https://www.oracle.com/java/
```

## 用法

```
java [options] class [args...]
```

```
java [options] -jar jarfile [args...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-cp, -classpath` | 指定类路径 |
| `-jar` | 运行JAR文件 |
| `-Xmx<size>` | 设置最大堆内存 |
| `-Xms<size>` | 设置初始堆内存 |
| `-D<name>=<value>` | 设置系统属性 |

## 示例

### 示例 1: 运行JAR文件

```bash
java -jar app.jar
```

### 示例 2: 设置最大堆内存2GB

```bash
java -Xmx2g -jar app.jar
```

### 示例 3: 设置系统属性运行

```bash
java -Dspring.profiles.active=prod -jar app.jar
```

## 关联命令

- [[javac]]
- [[jps]]

## 参考链接

- [https://docs.oracle.com/en/java/javase/](https://docs.oracle.com/en/java/javase/)

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

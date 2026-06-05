---
cmd_name: jhat
cmd_category: 编程语言/Java工具链
cmd_dimension: Java工具链
cmd_install: ''
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- jmap
- jcmd
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: Java堆分析工具，分析堆转储文件
created: '2026-06-04'
source_file: data/lang/java.yaml
---
# jhat

> Java堆分析工具，分析堆转储文件

## 安装

```bash
已预装
```

## 用法

```
jhat [选项] <堆转储文件>
```

## 参数

| Flag | Description |
|------|-------------|
| `-port <port>` | HTTP服务器端口（默认7000） |
| `-J<flag>` | 传递给JVM的选项 |

## 示例

### 分析堆转储文件

```bash
jhat heapdump.hprof
```

### 在8080端口启动分析服务

```bash
jhat -port 8080 heapdump.hprof
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

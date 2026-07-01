---
{
  "cmd_name": "jhat",
  "cmd_category": "编程语言/Java工具链",
  "cmd_dimension": "Java工具链",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "jmap",
    "jcmd",
    "jvisualvm"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/java.yaml"
}
---

# jhat

> Java堆分析工具，分析堆转储文件

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

### 示例 1: 分析堆转储文件

```bash
jhat heapdump.hprof
```

### 示例 2: 在8080端口启动分析服务

```bash
jhat -port 8080 heapdump.hprof
```

## 关联命令

- [[jmap]]
- [[jcmd]]

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

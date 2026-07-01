---
{
  "cmd_name": "jcmd",
  "cmd_category": "编程语言/Java工具链",
  "cmd_dimension": "Java工具链",
  "cmd_install": "JDK自带工具",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "jmap",
    "jstack"
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

# jcmd

> 向运行JVM发送诊断命令

## 安装

```bash
JDK自带工具
```

## 用法

```
jcmd <pid> <command>
```

## 示例

### 示例 1: 查看JVM版本

```bash
jcmd 12345 VM.version
```

### 示例 2: 生成堆转储

```bash
jcmd 12345 GC.heap_dump heap.hprof
```

### 示例 3: 打印线程堆栈

```bash
jcmd 12345 Thread.print
```

## 关联命令

- [[jmap]]
- [[jstack]]

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

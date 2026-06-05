---
cmd_name: jmap
cmd_category: 编程语言/Java工具链
cmd_dimension: Java工具链
cmd_install: JDK自带工具
cmd_platforms:
- linux
- darwin
- windows
summary: "生成堆转储和内存映射"
cmd_level: intermediate
cmd_related:
- jstack
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/lang/java.yaml
---


# jmap

> 生成堆转储和内存映射

## 安装

```bash
JDK自带工具
```

## 用法

```
jmap [option] <pid>
```

## 参数

| Flag | Description |
|------|-------------|
| `-dump:format=b,file=<file>` | 生成堆转储文件 |
| `-heap` | 显示堆信息 |
| `-histo` | 显示堆中对象统计 |

## 示例

### 示例 1: 查看堆信息

```bash
jmap -heap 12345
```

### 示例 2: 生成堆转储文件

```bash
jmap -dump:format=b,file=heap.bin 12345
```

## 关联命令

- [[jstack]]

## 风险提示

> ⚠️ **MEDIUM**: 堆转储操作会暂停应用，建议在低峰期执行

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

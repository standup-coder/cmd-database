---
{
  "cmd_name": "jstack",
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
    "jcmd"
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

# jstack

> 打印Java线程堆栈

## 安装

```bash
JDK自带工具
```

## 用法

```
jstack [option] <pid>
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 显示锁信息 |
| `-F` | 强制打印堆栈 |

## 示例

### 示例 1: 打印线程堆栈

```bash
jstack 12345
```

### 示例 2: 导出线程信息到文件

```bash
jstack -l 12345 > thread.txt
```

## 关联命令

- [[jmap]]
- [[jcmd]]

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

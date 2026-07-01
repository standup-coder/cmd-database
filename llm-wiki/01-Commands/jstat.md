---
{
  "cmd_name": "jstat",
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
    "jps",
    "jmap"
  ],
  "cmd_tags": [
    "monitoring",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/java.yaml"
}
---

# jstat

> 监控JVM统计信息

## 安装

```bash
JDK自带工具
```

## 用法

```
jstat [option] <vmid> [interval] [count]
```

## 参数

| Flag | Description |
|------|-------------|
| `-gc` | 显示GC统计信息 |
| `-gcutil` | 显示GC利用率 |
| `-class` | 显示类加载统计 |

## 示例

### 示例 1: 显示进程GC信息

```bash
jstat -gc 12345
```

### 示例 2: 每秒显示GC利用率10次

```bash
jstat -gcutil 12345 1000 10
```

## 关联命令

- [[jps]]
- [[jmap]]

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]

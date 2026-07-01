---
{
  "cmd_name": "ltrace",
  "cmd_category": "系统诊断/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "多数 Linux 预装或包管理器安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "strace",
    "perf"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/diagnostic/more.yaml"
}
---

# ltrace

> 跟踪库函数调用

## 安装

```bash
多数 Linux 预装或包管理器安装
```

## 用法

```
ltrace [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 过滤函数 |
| `-f` | 跟踪子进程 |
| `-o` | 输出文件 |
| `-p` | 附加 PID |

## 示例

### 示例 1: 跟踪内存分配

```bash
ltrace -e malloc,free ./app
```

### 示例 2: 附加到进程

```bash
ltrace -p 1234
```

## 关联命令

- [[strace]]
- [[perf]]

## 所属维度

[[扩展工具-MOC|系统诊断/扩展工具]]

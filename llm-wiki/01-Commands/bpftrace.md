---
{
  "cmd_name": "bpftrace",
  "cmd_category": "系统诊断/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://github.com/iovisor/bpftrace/blob/master/INSTALL.md",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "bcc",
    "perf"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/diagnostic/more.yaml"
}
---

# bpftrace

> 高级 eBPF 跟踪语言

## 安装

```bash
参考 https://github.com/iovisor/bpftrace/blob/master/INSTALL.md
```

## 用法

```
bpftrace [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 程序 |
| `-l` | 列出探针 |
| `-p` | PID |

## 示例

### 示例 1: 跟踪 openat

```bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_openat { printf("%s %s\n", comm, str(args->filename)); }'
```

### 示例 2: 列出探针

```bash
sudo bpftrace -l 'tracepoint:syscalls:*'
```

## 关联命令

- [[bcc]]
- [[perf]]

## 风险提示

> ⚠️ **MEDIUM**: bpftrace 在内核运行，脚本错误可能影响性能

## 所属维度

[[扩展工具-MOC|系统诊断/扩展工具]]

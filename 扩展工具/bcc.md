---
{
  "cmd_name": "bcc",
  "cmd_category": "系统诊断/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://github.com/iovisor/bcc/blob/master/INSTALL.md",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "bpftrace",
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

# bcc

> BPF Compiler Collection 工具集

## 安装

```bash
参考 https://github.com/iovisor/bcc/blob/master/INSTALL.md
```

## 用法

```
bcc [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `tools` | 目录脚本 |
| `-p` | PID |

## 示例

### 示例 1: 监控文件打开

```bash
sudo /usr/share/bcc/tools/opensnoop
```

### 示例 2: 块设备延迟

```bash
sudo /usr/share/bcc/tools/biolatency
```

## 关联命令

- [[bpftrace]]
- [[perf]]

## 风险提示

> ⚠️ **MEDIUM**: bcc 工具在内核运行，注意对生产系统的影响

## 所属维度

[[扩展工具-MOC|系统诊断/扩展工具]]

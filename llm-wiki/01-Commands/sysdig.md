---
{
  "cmd_name": "sysdig",
  "cmd_category": "系统诊断/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://github.com/draios/sysdig",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "bpftrace",
    "strace"
  ],
  "cmd_tags": [
    "monitoring",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/diagnostic/more.yaml"
}
---

# sysdig

> 系统级监控与故障排查

## 安装

```bash
参考 https://github.com/draios/sysdig
```

## 用法

```
sysdig [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 凿子 |
| `-p` | 输出格式 |
| `-w` | 写入文件 |
| `filter` | 过滤 |

## 示例

### 示例 1: 实时监控系统调用

```bash
sudo sysdig
```

### 示例 2: CPU 占用最高进程

```bash
sudo sysdig -c topprocs_cpu
```

## 关联命令

- [[bpftrace]]
- [[strace]]

## 风险提示

> ⚠️ **MEDIUM**: sysdig 会捕获系统调用，注意敏感数据

## 所属维度

[[扩展工具-MOC|系统诊断/扩展工具]]

---
{
  "cmd_name": "numactl",
  "cmd_category": "硬件/系统信息",
  "cmd_dimension": "系统信息",
  "cmd_install": "多数 Linux 预装或包管理器安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "taskset",
    "lstopo"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/info.yaml"
}
---

# numactl

> 控制进程的 NUMA 内存与 CPU 策略

## 安装

```bash
多数 Linux 预装或包管理器安装
```

## 用法

```
numactl [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `--cpunodebind` | 绑定 CPU 节点 |
| `--membind` | 绑定内存节点 |
| `--interleave` | 交错 |
| `--show` | 显示当前策略 |

## 示例

### 示例 1: 显示当前 NUMA 策略

```bash
numactl --show
```

### 示例 2: 绑定到节点 0

```bash
numactl --cpunodebind=0 --membind=0 ./app
```

## 关联命令

- [[taskset]]
- [[lstopo]]

## 风险提示

> ⚠️ **MEDIUM**: 错误绑定会降低性能或导致 OOM，请了解 NUMA 拓扑

## 所属维度

[[系统信息-MOC|硬件/系统信息]]

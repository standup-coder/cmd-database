---
{
  "cmd_name": "cgexec",
  "cmd_category": "硬件/性能与调度",
  "cmd_dimension": "性能与调度",
  "cmd_install": "随 cgroup-tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "systemd-run",
    "cset"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/perf.yaml"
}
---

# cgexec

> 在指定 cgroup 中运行命令

## 安装

```bash
随 cgroup-tools 安装
```

## 用法

```
cgexec [OPTIONS] GROUP COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `-g` | 控制器:路径 |
| `-b` | 忽略 systemd |

## 示例

### 示例 1: 在 mygroup 中运行

```bash
sudo cgexec -g cpu,memory:mygroup ./app
```

### 示例 2: 限制数据库 CPU 集合

```bash
sudo cgexec -g cpuset:db python server.py
```

## 关联命令

- [[cset]]

## 风险提示

> ⚠️ **MEDIUM**: cgroup 限制过严会导致 OOM 或 CPU 饥饿

## 所属维度

[[性能与调度-MOC|硬件/性能与调度]]

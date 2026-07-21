---
{
  "cmd_name": "renice",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nice",
    "top"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# renice

> 修改运行中进程的优先级

## 用法

```
renice [OPTIONS] PRIORITY [[-p] PID...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 按 PID |
| `-u` | 按用户 |
| `-g` | 按进程组 |

## 示例

### 示例 1: 提升进程 1234 的优先级

```bash
sudo renice -n -5 -p 1234
```

### 示例 2: 降低 alice 所有进程优先级

```bash
sudo renice -n 10 -u alice
```

## 关联命令

- [[nice]]

## 风险提示

> ⚠️ **MEDIUM**: 调整关键系统进程优先级可能影响稳定性，请谨慎

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]

---
{
  "cmd_name": "tc",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "iptables",
    "ip"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# tc

> Linux 流量控制（Traffic Control）

## 用法

```
tc [OPTIONS] qdisc|class|filter ...
```

## 参数

| Flag | Description |
|------|-------------|
| `show` | 显示配置 |
| `add` | 添加 qdisc |
| `change` | 修改 |
| `del` | 删除 |

## 示例

### 示例 1: 显示当前 qdisc

```bash
tc qdisc show
```

### 示例 2: 模拟 100ms 延迟

```bash
sudo tc qdisc add dev eth0 root netem delay 100ms
```

## 关联命令

- [[iptables]]
- [[ip]]

## 风险提示

> ⚠️ **HIGH**: 流量控制会改变网络延迟和带宽，生产环境请谨慎

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]

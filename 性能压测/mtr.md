---
{
  "cmd_name": "mtr",
  "cmd_category": "网络工具/性能压测",
  "cmd_dimension": "性能压测",
  "cmd_install": "包管理器安装，如 sudo apt install mtr / sudo yum install mtr",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ping",
    "traceroute"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/network/performance.yaml"
}
---

# mtr

> 结合 ping 和 traceroute 的网络路径诊断工具

## 安装

```bash
包管理器安装，如 sudo apt install mtr / sudo yum install mtr
```

## 用法

```
mtr [OPTIONS] HOST
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 生成报告模式 |
| `-c` | 发送探测包数量 |
| `-n` | 禁用 DNS 解析 |

## 示例

### 示例 1: 生成 100 个包的路径质量报告

```bash
mtr -r -c 100 example.com
```

### 示例 2: 不解析 DNS 地诊断到 8.8.8.8 的路径

```bash
mtr -n 8.8.8.8
```

## 关联命令

- [[ping]]
- [[traceroute]]

## 风险提示

> ⚠️ **LOW**: 持续发送探测包可能被视为扫描，请遵守目标网络策略

## 所属维度

[[性能压测-MOC|网络工具/性能压测]]

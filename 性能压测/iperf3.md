---
{
  "cmd_name": "iperf3",
  "cmd_category": "网络工具/性能压测",
  "cmd_dimension": "性能压测",
  "cmd_install": "包管理器安装，如 sudo apt install iperf3 / sudo yum install iperf3",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ping",
    "mtr"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/performance.yaml"
}
---

# iperf3

> TCP/UDP 网络带宽测试工具

## 安装

```bash
包管理器安装，如 sudo apt install iperf3 / sudo yum install iperf3
```

## 用法

```
iperf3 [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | 服务端模式 |
| `-c` | 客户端模式，指定服务器地址 |
| `-u` | 使用 UDP 测试 |
| `-t` | 测试持续时间 |

## 示例

### 示例 1: 启动 iperf3 服务端

```bash
iperf3 -s
```

### 示例 2: 测试到服务器的 TCP 带宽 30 秒

```bash
iperf3 -c 192.168.1.1 -t 30
```

## 关联命令

- [[ping]]
- [[mtr]]

## 风险提示

> ⚠️ **MEDIUM**: 带宽测试会占满链路，可能影响其他业务流量，请选择合适的时间窗口

## 所属维度

[[性能压测-MOC|网络工具/性能压测]]

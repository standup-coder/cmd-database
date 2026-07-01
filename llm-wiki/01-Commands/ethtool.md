---
{
  "cmd_name": "ethtool",
  "cmd_category": "硬件/网络硬件",
  "cmd_dimension": "网络硬件",
  "cmd_install": "多数 Linux 预装或包管理器安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ip",
    "iw"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/network.yaml"
}
---

# ethtool

> 查看和设置网卡参数

## 安装

```bash
多数 Linux 预装或包管理器安装
```

## 用法

```
ethtool [OPTIONS] INTERFACE
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 驱动信息 |
| `-S` | 统计 |
| `-s` | 设置 |
| `-a` | 查看 PAUSE |

## 示例

### 示例 1: 查看 eth0 信息

```bash
ethtool eth0
```

### 示例 2: 设置速率和双工

```bash
sudo ethtool -s eth0 speed 1000 duplex full
```

## 关联命令

- [[ip]]
- [[iw]]

## 风险提示

> ⚠️ **MEDIUM**: 修改网卡参数可能断开网络，远程操作时谨慎

## 所属维度

[[网络硬件-MOC|硬件/网络硬件]]

---
{
  "cmd_name": "iftop",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "包管理器安装，如 sudo apt install iftop",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nethogs",
    "bmon"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# iftop

> 实时显示网络接口带宽使用

## 安装

```bash
包管理器安装，如 sudo apt install iftop
```

## 用法

```
iftop [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 指定网卡 |
| `-n` | 禁用 DNS |
| `-B` | 以字节显示 |

## 示例

### 示例 1: 查看 eth0 实时流量

```bash
sudo iftop -i eth0
```

### 示例 2: 以字节显示且不做 DNS 解析

```bash
sudo iftop -nB -i eth0
```

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]

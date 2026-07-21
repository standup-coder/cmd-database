---
{
  "cmd_name": "hping3",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "包管理器安装，如 sudo apt install hping3",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "nmap",
    "nping"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# hping3

> 自定义 TCP/IP 数据包生成与探测工具

## 安装

```bash
包管理器安装，如 sudo apt install hping3
```

## 用法

```
hping3 [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-S` | SYN 扫描 |
| `-p` | 目标端口 |
| `-c` | 发送次数 |
| `--flood` | 泛洪模式 |

## 示例

### 示例 1: 发送 SYN 探测 80 端口

```bash
sudo hping3 -S -p 80 -c 4 example.com
```

### 示例 2: 泛洪测试（谨慎）

```bash
sudo hping3 --flood -p 80 example.com
```

## 关联命令

- [[nmap]]

## 风险提示

> ⚠️ **CRITICAL**: 泛洪模式会制造拒绝服务，严禁对未授权目标使用

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]

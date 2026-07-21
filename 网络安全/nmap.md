---
{
  "cmd_name": "nmap",
  "cmd_category": "网络工具/网络安全",
  "cmd_dimension": "网络安全",
  "cmd_install": "包管理器安装，如 sudo apt install nmap / sudo yum install nmap",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "masscan",
    "httpx"
  ],
  "cmd_tags": [
    "safety",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/security.yaml"
}
---

# nmap

> 网络发现与安全审计扫描工具

## 安装

```bash
包管理器安装，如 sudo apt install nmap / sudo yum install nmap
```

## 用法

```
nmap [OPTIONS] TARGET
```

## 参数

| Flag | Description |
|------|-------------|
| `-sS` | SYN 半开放扫描（需要 root） |
| `-sV` | 探测服务版本 |
| `-O` | 探测操作系统 |
| `-p` | 指定端口范围 |

## 示例

### 示例 1: 扫描目标主机的常用端口

```bash
nmap 192.168.1.1
```

### 示例 2: 扫描网段并识别服务和操作系统

```bash
sudo nmap -sS -sV -O 192.168.1.0/24
```

## 关联命令

- [[masscan]]
- [[httpx]]

## 风险提示

> ⚠️ **HIGH**: 对未授权目标扫描可能违反法律或安全策略，请确保获得书面授权

## 所属维度

[[网络安全-MOC|网络工具/网络安全]]

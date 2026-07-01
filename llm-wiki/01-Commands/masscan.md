---
{
  "cmd_name": "masscan",
  "cmd_category": "网络工具/网络安全",
  "cmd_dimension": "网络安全",
  "cmd_install": "参考 https://github.com/robertdavidgraham/masscan",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "nmap"
  ],
  "cmd_tags": [
    "safety",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/network/security.yaml"
}
---

# masscan

> 高速互联网规模端口扫描器

## 安装

```bash
参考 https://github.com/robertdavidgraham/masscan
```

## 用法

```
masscan [OPTIONS] TARGET -p PORTS
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 指定端口范围，如 1-65535 |
| `--rate` | 设置每秒发送数据包数量 |

## 示例

### 示例 1: 扫描网段的 80 和 443 端口

```bash
sudo masscan 192.168.1.0/24 -p80,443 --rate 1000
```

### 示例 2: 全互联网端口扫描（需合法授权）

```bash
sudo masscan 0.0.0.0/0 -p0-65535 --max-rate 10000
```

## 关联命令

- [[nmap]]

## 风险提示

> ⚠️ **CRITICAL**: 高速扫描会产生大量流量，极易被检测并可能触发法律后果，严禁对未授权目标使用

## 所属维度

[[网络安全-MOC|网络工具/网络安全]]

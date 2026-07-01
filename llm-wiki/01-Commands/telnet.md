---
{
  "cmd_name": "telnet",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "多数系统预装或包管理器安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nc",
    "ssh"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# telnet

> 基于文本的远程登录/端口探测工具

## 安装

```bash
多数系统预装或包管理器安装
```

## 用法

```
telnet [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-4` | 只使用 IPv4 |
| `-6` | 只使用 IPv6 |
| `port` | 指定端口 |

## 示例

### 示例 1: 测试本地 25 端口

```bash
telnet localhost 25
```

### 示例 2: 探测远程 80 端口

```bash
telnet example.com 80
```

## 关联命令

- [[nc]]
- [[ssh]]

## 风险提示

> ⚠️ **MEDIUM**: telnet 明文传输，不建议用于生产认证，优先使用 ssh

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]

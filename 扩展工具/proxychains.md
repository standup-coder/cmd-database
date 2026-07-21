---
{
  "cmd_name": "proxychains",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "包管理器安装，如 sudo apt install proxychains4",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nc",
    "sshuttle"
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

# proxychains

> 强制任意程序通过代理连接网络

## 安装

```bash
包管理器安装，如 sudo apt install proxychains4
```

## 用法

```
proxychains [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-q` | 静默模式 |
| `-f` | 指定配置文件 |

## 示例

### 示例 1: 通过代理访问目标

```bash
proxychains curl https://example.com
```

### 示例 2: 通过代理进行 TCP 扫描

```bash
proxychains -q nmap -sT target
```

## 关联命令

- [[nc]]
- [[sshuttle]]

## 风险提示

> ⚠️ **MEDIUM**: 代理配置错误会导致流量绕行或泄露，请确认代理安全

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]

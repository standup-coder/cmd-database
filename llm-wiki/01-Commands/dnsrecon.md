---
{
  "cmd_name": "dnsrecon",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://github.com/darkoperator/dnsrecon",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dig",
    "amass"
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

# dnsrecon

> DNS 枚举与区域传送检测

## 安装

```bash
参考 https://github.com/darkoperator/dnsrecon
```

## 用法

```
dnsrecon [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 目标域名 |
| `-t` | 枚举类型 |
| `-D` | 字典文件 |

## 示例

### 示例 1: 枚举 DNS 记录

```bash
dnsrecon -d example.com
```

### 示例 2: 检测区域传送漏洞

```bash
dnsrecon -d example.com -t axfr
```

## 关联命令

- [[dig]]
- [[amass]]

## 风险提示

> ⚠️ **MEDIUM**: 大量 DNS 查询可能被目标视为扫描，请控制速率

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]

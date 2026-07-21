---
{
  "cmd_name": "traceroute",
  "cmd_category": "网络工具/网络诊断",
  "cmd_dimension": "网络诊断",
  "cmd_install": "apt install traceroute (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/network/diagnostic.yaml"
}
---

# traceroute

> 跟踪数据包的路由路径

## 安装

```bash
apt install traceroute (Ubuntu)
```

## 用法

```
traceroute [options] <host>
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 不解析IP地址 |
| `-m <hops>` | 最大跳数 |

## 示例

### 示例 1: 跟踪路由

```bash
traceroute google.com
```

### 示例 2: 跟踪路由不解析域名

```bash
traceroute -n 8.8.8.8
```

## 所属维度

[[网络诊断-MOC|网络工具/网络诊断]]

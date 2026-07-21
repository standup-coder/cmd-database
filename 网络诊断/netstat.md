---
{
  "cmd_name": "netstat",
  "cmd_category": "网络工具/网络诊断",
  "cmd_dimension": "网络诊断",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/network/diagnostic.yaml"
}
---

# netstat

> 显示网络连接和路由表

## 用法

```
netstat [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 显示所有连接和监听端口 |
| `-n` | 以数字形式显示地址 |
| `-t` | 显示TCP连接 |
| `-u` | 显示UDP连接 |
| `-p` | 显示进程/程序ID |

## 示例

### 示例 1: 显示所有连接

```bash
netstat -an
```

### 示例 2: 显示监听端口和进程

```bash
netstat -tunlp
```

## 所属维度

[[网络诊断-MOC|网络工具/网络诊断]]

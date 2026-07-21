---
{
  "cmd_name": "ss",
  "cmd_category": "网络工具/网络诊断",
  "cmd_dimension": "网络诊断",
  "cmd_install": "",
  "cmd_platforms": [
    "linux"
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

# ss

> socket统计信息(替代netstat)

## 用法

```
ss [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 显示所有socket |
| `-t` | 显示TCP socket |
| `-u` | 显示UDP socket |
| `-l` | 显示监听socket |
| `-n` | 不解析服务名 |
| `-p` | 显示进程信息 |

## 示例

### 示例 1: 显示监听TCP/UDP端口

```bash
ss -tunlp
```

### 示例 2: 显示统计信息

```bash
ss -s
```

## 所属维度

[[网络诊断-MOC|网络工具/网络诊断]]

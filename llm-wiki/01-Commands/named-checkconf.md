---
{
  "cmd_name": "named-checkconf",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "rndc",
    "dnsmasq"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/network/infra.yaml"
}
---

# named-checkconf

> 检查 BIND DNS 配置文件语法

## 用法

```
named-checkconf [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-z` | 检查所有 zone |
| `-p` | 打印配置 |
| `-t` | 指定 chroot |

## 示例

### 示例 1: 检查 named.conf

```bash
sudo named-checkconf
```

### 示例 2: 检查所有 zone

```bash
sudo named-checkconf -z
```

## 关联命令

- [[rndc]]
- [[dnsmasq]]

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]

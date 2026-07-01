---
{
  "cmd_name": "nsupdate",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "rndc",
    "dig"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/infra.yaml"
}
---

# nsupdate

> 动态更新 DNS 记录

## 用法

```
nsupdate [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-k` | 密钥文件 |
| `-v` | 详细 |
| `-d` | 调试 |

## 示例

### 示例 1: 使用 TSIG 密钥更新

```bash
nsupdate -k Kexample.+157+12345.key
```

### 示例 2: 添加 A 记录

```bash
echo -e 'update add host.example.com 300 A 1.2.3.4
send' | nsupdate
```

## 关联命令

- [[rndc]]
- [[dig]]

## 风险提示

> ⚠️ **HIGH**: nsupdate 会修改 DNS 记录，错误的更新会影响域名解析

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]

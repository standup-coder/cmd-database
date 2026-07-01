---
{
  "cmd_name": "unbound-control",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dnsmasq",
    "resolvectl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/infra.yaml"
}
---

# unbound-control

> Unbound DNS 服务器远程控制

## 用法

```
unbound-control [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `status` | 状态 |
| `reload` | 重载 |
| `lookup` | 查询 |
| `flush` | 清空缓存 |

## 示例

### 示例 1: 查看 Unbound 状态

```bash
sudo unbound-control status
```

### 示例 2: 清空指定域名缓存

```bash
sudo unbound-control flush example.com
```

## 关联命令

- [[dnsmasq]]
- [[resolvectl]]

## 风险提示

> ⚠️ **MEDIUM**: 重载或 flush 会影响 DNS 解析，请确认影响范围

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]

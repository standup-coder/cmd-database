---
{
  "cmd_name": "rndc",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "named-checkconf",
    "nsupdate"
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

# rndc

> BIND DNS 服务器远程控制

## 用法

```
rndc [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `reload` | 重载 |
| `status` | 状态 |
| `flush` | 清空缓存 |
| `stop` | 停止 |

## 示例

### 示例 1: 重载 BIND

```bash
sudo rndc reload
```

### 示例 2: 查看状态

```bash
sudo rndc status
```

## 关联命令

- [[named-checkconf]]
- [[nsupdate]]

## 风险提示

> ⚠️ **MEDIUM**: rndc stop/reload 会影响 DNS 服务，请在维护窗口执行

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]

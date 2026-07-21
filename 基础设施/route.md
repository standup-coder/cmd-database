---
{
  "cmd_name": "route",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "ip",
    "ifconfig"
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

# route

> 传统路由表管理

## 用法

```
route [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `add` | 添加路由 |
| `del` | 删除路由 |
| `-n` | 数字显示 |

## 示例

### 示例 1: 显示路由表

```bash
route -n
```

### 示例 2: 添加静态路由

```bash
sudo route add -net 10.0.0.0/8 gw 192.168.1.1
```

## 关联命令

- [[ip]]
- [[ifconfig]]

## 风险提示

> ⚠️ **HIGH**: 错误路由可能导致网络不可达，远程服务器请通过带外管理操作

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]

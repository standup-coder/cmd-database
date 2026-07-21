---
{
  "cmd_name": "bridge",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ip",
    "nmcli"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# bridge

> 以太网桥管理

## 用法

```
bridge [OPTIONS] OBJECT {COMMAND}
```

## 参数

| Flag | Description |
|------|-------------|
| `link` | show 显示桥接端口 |
| `fdb` | show 显示转发数据库 |
| `vlan` | show 显示 VLAN |

## 示例

### 示例 1: 显示桥接接口

```bash
bridge link show
```

### 示例 2: 显示 MAC 转发表

```bash
bridge fdb show
```

## 关联命令

- [[ip]]
- [[nmcli]]

## 风险提示

> ⚠️ **MEDIUM**: 桥接配置错误会导致二层网络异常

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]

---
{
  "cmd_name": "netplan",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "nmcli",
    "ip"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# netplan

> Ubuntu 网络配置管理工具

## 用法

```
netplan [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `generate` | 生成配置 |
| `apply` | 应用配置 |
| `try` | 试用配置 |
| `info` | 显示信息 |

## 示例

### 示例 1: 生成网络配置

```bash
sudo netplan generate
```

### 示例 2: 应用网络配置

```bash
sudo netplan apply
```

## 关联命令

- [[nmcli]]
- [[ip]]

## 风险提示

> ⚠️ **HIGH**: netplan apply 会立即修改网络，远程服务器请先用 netplan try

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]

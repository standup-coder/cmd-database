---
{
  "cmd_name": "ipmicfg",
  "cmd_category": "硬件/远程带外管理",
  "cmd_dimension": "远程带外管理",
  "cmd_install": "参考 Supermicro 官方工具",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "ipmitool",
    "redfish"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/hardware/ipmi.yaml"
}
---

# ipmicfg

> Supermicro IPMI 配置工具

## 安装

```bash
参考 Supermicro 官方工具
```

## 用法

```
ipmicfg [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-m` | 设置 IP |
| `-k` | 设置子网掩码 |
| `-g` | 设置网关 |
| `-r` | 重置 |

## 示例

### 示例 1: 设置 BMC IP

```bash
ipmicfg -m 192.168.1.50
```

### 示例 2: 重置 BMC

```bash
ipmicfg -r
```

## 关联命令

- [[ipmitool]]
- [[redfish]]

## 风险提示

> ⚠️ **HIGH**: 重置 BMC 会中断带外管理，请谨慎

## 所属维度

[[远程带外管理-MOC|硬件/远程带外管理]]

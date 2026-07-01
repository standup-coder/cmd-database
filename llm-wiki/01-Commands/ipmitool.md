---
{
  "cmd_name": "ipmitool",
  "cmd_category": "硬件/远程带外管理",
  "cmd_dimension": "远程带外管理",
  "cmd_install": "包管理器安装，如 sudo apt install ipmitool",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "ipmicfg",
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

# ipmitool

> IPMI 带外管理工具

## 安装

```bash
包管理器安装，如 sudo apt install ipmitool
```

## 用法

```
ipmitool [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `-I` | 接口 |
| `-H` | 主机 |
| `-U` | 用户 |
| `-P` | 密码 |
| `chassis` | status |
| `sol` | activate |

## 示例

### 示例 1: 查看 chassis 状态

```bash
ipmitool -I lanplus -H 192.168.1.100 -U admin -P pass chassis status
```

### 示例 2: 启动 SOL 控制台

```bash
ipmitool -H 192.168.1.100 -U admin -I lanplus sol activate
```

## 关联命令

- [[ipmicfg]]
- [[redfish]]

## 风险提示

> ⚠️ **HIGH**: IPMI 可远程开关机、重置，请保护好凭据

## 所属维度

[[远程带外管理-MOC|硬件/远程带外管理]]

---
{
  "cmd_name": "redfish",
  "cmd_category": "硬件/远程带外管理",
  "cmd_dimension": "远程带外管理",
  "cmd_install": "pip install redfish 或参考厂商工具",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ipmitool",
    "curl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/ipmi.yaml"
}
---

# redfish

> Redfish API 客户端（python-redfish 或 curl 示例）

## 安装

```bash
pip install redfish 或参考厂商工具
```

## 用法

```
redfish [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--user` |  |
| `--password` |  |
| `--rhost` |  |
| `--ServiceRoot` |  |

## 示例

### 示例 1: 查询系统信息

```bash
curl -u admin:pass https://bmc/redfish/v1/Systems
```

### 示例 2: 使用 python-redfish

```bash
python -m redfish --rhost bmc --user admin --password pass Systems
```

## 关联命令

- [[ipmitool]]
- [[curl]]

## 风险提示

> ⚠️ **MEDIUM**: Redfish 可执行电源操作，请保护好凭据

## 所属维度

[[远程带外管理-MOC|硬件/远程带外管理]]

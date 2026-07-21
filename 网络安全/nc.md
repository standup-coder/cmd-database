---
{
  "cmd_name": "nc",
  "cmd_category": "网络工具/网络安全",
  "cmd_dimension": "网络安全",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nmap",
    "socat"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/security.yaml"
}
---

# nc

> Netcat，网络工具中的瑞士军刀，用于读写网络连接

## 用法

```
nc [OPTIONS] HOST PORT
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 监听模式 |
| `-v` | 显示详细输出 |
| `-z` | 零 I/O 扫描模式 |

## 示例

### 示例 1: 扫描目标主机的 22 端口是否开放

```bash
nc -zv 192.168.1.1 22
```

### 示例 2: 在本地 8080 端口监听连接

```bash
nc -l 8080
```

## 关联命令

- [[nmap]]
- [[socat]]

## 风险提示

> ⚠️ **MEDIUM**: 监听模式可能暴露服务到网络，请确认防火墙和访问范围

## 所属维度

[[网络安全-MOC|网络工具/网络安全]]

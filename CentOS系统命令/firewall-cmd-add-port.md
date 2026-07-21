---
{
  "cmd_name": "firewall-cmd --add-port",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on CentOS/RHEL 7+",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/centos.yaml"
}
---

# firewall-cmd --add-port

> Open firewall port

## 安装

```bash
Pre-installed on CentOS/RHEL 7+
```

## 用法

```
sudo firewall-cmd --add-port=<port>/<protocol>
```

## 参数

| Flag | Description |
|------|-------------|
| `--permanent` | Make rule persistent across reboots |
| `--zone` | Specify firewall zone |

## 示例

### 示例 1: Open HTTP port temporarily

```bash
sudo firewall-cmd --add-port=80/tcp
```

### 示例 2: Permanently open HTTPS port

```bash
sudo firewall-cmd --permanent --add-port=443/tcp
```

### 示例 3: Reload firewall rules

```bash
sudo firewall-cmd --reload
```

## 风险提示

> ⚠️ **MEDIUM**: Opening ports may expose services to network

## 所属维度

[[通用Linux命令-MOC|Operating System]]

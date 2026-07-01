---
{
  "cmd_name": "systemctl status",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu 16.04+",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/ubuntu.yaml"
}
---

# systemctl status

> Check service status

## 安装

```bash
Pre-installed on Ubuntu 16.04+
```

## 用法

```
systemctl status <service>
```

## 示例

### 示例 1: Check nginx service status

```bash
systemctl status nginx
```

### 示例 2: 不分页显示服务状态

```bash
systemctl status nginx --no-pager
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Operating System-MOC|Operating System]]

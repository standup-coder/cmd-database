---
{
  "cmd_name": "getenforce",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on CentOS/RHEL",
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
  "source_file": "data/os/centos.yaml"
}
---

# getenforce

> Get current SELinux mode

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
getenforce
```

## 示例

### 示例 1: Show current SELinux mode

```bash
getenforce
```

### 示例 2: 同时查看模式和详细状态

```bash
getenforce && sestatus
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Operating System-MOC|Operating System]]

---
{
  "cmd_name": "sestatus",
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

# sestatus

> Display SELinux status

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sestatus
```

## 示例

### 示例 1: Show detailed SELinux status

```bash
sestatus
```

### 示例 2: 显示详细策略状态

```bash
sestatus -v
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[通用Linux命令-MOC|Operating System]]

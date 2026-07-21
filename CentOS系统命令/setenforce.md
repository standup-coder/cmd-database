---
{
  "cmd_name": "setenforce",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on CentOS/RHEL",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/centos.yaml"
}
---

# setenforce

> Change SELinux mode temporarily

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sudo setenforce <0|1>
```

## 示例

### 示例 1: Set SELinux to permissive mode

```bash
sudo setenforce 0
```

### 示例 2: Set SELinux to enforcing mode

```bash
sudo setenforce 1
```

## 风险提示

> ⚠️ **HIGH**: Disabling SELinux reduces system security

## 所属维度

[[通用Linux命令-MOC|Operating System]]

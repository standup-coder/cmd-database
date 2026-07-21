---
{
  "cmd_name": "ansible-config dump",
  "cmd_category": "Kubernetes Config Management",
  "cmd_dimension": "Kubernetes Config Management",
  "cmd_install": "pip install ansible",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-config.yaml"
}
---

# ansible-config dump

> Show Ansible configuration

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-config dump
```

## 示例

### 示例 1: Show current configuration

```bash
ansible-config dump
```

### 示例 2: List all config options

```bash
ansible-config list
```

### 示例 3: Show only changed settings

```bash
ansible-config dump --only-changed
```

## 风险提示

> ⚠️ **LOW**: Read-only configuration display

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]

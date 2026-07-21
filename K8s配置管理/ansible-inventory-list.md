---
{
  "cmd_name": "ansible-inventory --list",
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

# ansible-inventory --list

> Display Ansible inventory information

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-inventory [options]
```

## 示例

### 示例 1: List all inventory hosts

```bash
ansible-inventory --list
```

### 示例 2: Display inventory as graph

```bash
ansible-inventory --graph
```

### 示例 3: List from specific inventory

```bash
ansible-inventory -i inventory.yml --list
```

## 风险提示

> ⚠️ **LOW**: Read-only inventory display

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]

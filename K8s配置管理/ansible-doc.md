---
{
  "cmd_name": "ansible-doc",
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

# ansible-doc

> Display Ansible module documentation

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-doc [module-name]
```

## 示例

### 示例 1: Show Kubernetes module docs

```bash
ansible-doc k8s
```

### 示例 2: List Kubernetes-related modules

```bash
ansible-doc -l | grep k8s
```

### 示例 3: Show SSH connection plugin docs

```bash
ansible-doc -t connection ssh
```

## 风险提示

> ⚠️ **LOW**: Documentation display only

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]

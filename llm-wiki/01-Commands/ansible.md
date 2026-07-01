---
{
  "cmd_name": "ansible",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-config.yaml"
}
---

# ansible

> Execute ad-hoc commands on hosts

## 安装

```bash
pip install ansible
```

## 用法

```
ansible [hosts] [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-m` | Module to execute |
| `-a` | Module arguments |
| `-i` | Inventory file |

## 示例

### 示例 1: Ping all hosts

```bash
ansible all -m ping
```

### 示例 2: Check uptime on web servers

```bash
ansible webservers -m command -a 'uptime'
```

### 示例 3: Execute kubectl on Kubernetes nodes

```bash
ansible k8s-nodes -i inventory.yml -m shell -a 'kubectl get nodes'
```

## 风险提示

> ⚠️ **MEDIUM**: Executes commands on remote hosts

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]

---
{
  "cmd_name": "ansible all -m ping",
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

# ansible all -m ping

> Test connectivity to all hosts in inventory

## 安装

```bash
pip install ansible
```

## 用法

```
ansible [hosts] -m [module] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | Inventory file path |
| `-m` | Module name to execute |

## 示例

### 示例 1: Ping all hosts in inventory

```bash
ansible all -m ping
```

### 示例 2: Ping with specific inventory

```bash
ansible all -m ping -i inventory.yml
```

### 示例 3: Execute command on Kubernetes master nodes

```bash
ansible k8s-masters -m shell -a 'kubectl get nodes'
```

## 风险提示

> ⚠️ **LOW**: Read-only connectivity test; no changes made

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]

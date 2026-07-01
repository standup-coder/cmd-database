---
{
  "cmd_name": "ansible-galaxy install",
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

# ansible-galaxy install

> Install Ansible roles from Galaxy or Git

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-galaxy install [role-name]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | Install from requirements file |
| `-p` | Installation path |

## 示例

### 示例 1: Install Docker role

```bash
ansible-galaxy install geerlingguy.docker
```

### 示例 2: Install roles from requirements

```bash
ansible-galaxy install -r requirements.yml
```

### 示例 3: Install Kubespray role

```bash
ansible-galaxy install kubernetes-sigs.kubespray
```

## 风险提示

> ⚠️ **LOW**: Downloads roles; no system changes

## 所属维度

[[Kubernetes Config Management-MOC|Kubernetes Config Management]]

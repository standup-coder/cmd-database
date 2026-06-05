---
cmd_name: ansible-playbook
cmd_category: "容器编排/K8s配置管理"
cmd_dimension: Kubernetes Config Management
cmd_install: pip install ansible
cmd_platforms:
- linux
- darwin
- windows
summary: "Execute Ansible playbook"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/k8s-config.yaml
---


# ansible-playbook

> Execute Ansible playbook

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-playbook [playbook.yml] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | Inventory file path |
| `--check` | Dry run mode; don't make changes |
| `-v` | Verbose mode |
| `--tags` | Run only tasks with specific tags |

## 示例

### 示例 1: Run playbook with inventory

```bash
ansible-playbook playbook.yml -i inventory/hosts.yml
```

### 示例 2: Dry run to preview changes

```bash
ansible-playbook playbook.yml --check
```

### 示例 3: Run only Kubernetes-tagged tasks

```bash
ansible-playbook playbook.yml --tags kubernetes
```

### 示例 4: Deploy Kubernetes cluster with Kubespray

```bash
ansible-playbook cluster.yml -i inventory/mycluster/hosts.yaml
```

## 风险提示

> ⚠️ **HIGH**: Executes configuration changes on target hosts

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]

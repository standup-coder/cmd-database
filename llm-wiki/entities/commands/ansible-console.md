---
cmd_name: ansible-console
cmd_category: "容器编排/K8s配置管理"
cmd_dimension: Kubernetes Config Management
cmd_install: pip install ansible
cmd_platforms:
- linux
- darwin
- windows
summary: "Interactive Ansible console"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-config.yaml
---


# ansible-console

> Interactive Ansible console

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-console [hosts]
```

## 示例

### 示例 1: Start interactive console

```bash
ansible-console
```

### 示例 2: Console for Kubernetes masters

```bash
ansible-console k8s-masters
```

### 示例 3: Console for web servers

```bash
ansible-console -i inventory.yml webservers
```

## 风险提示

> ⚠️ **MEDIUM**: Interactive command execution on hosts

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]

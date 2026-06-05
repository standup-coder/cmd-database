---
cmd_name: ansible-vault encrypt
cmd_category: "容器编排/K8s配置管理"
cmd_dimension: Kubernetes Config Management
cmd_install: pip install ansible
cmd_platforms:
- linux
- darwin
- windows
summary: "Encrypt Ansible files with vault"
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


# ansible-vault encrypt

> Encrypt Ansible files with vault

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-vault encrypt [file]
```

## 示例

### 示例 1: Encrypt secrets file

```bash
ansible-vault encrypt secrets.yml
```

### 示例 2: Encrypt production variables

```bash
ansible-vault encrypt vars/production.yml
```

### 示例 3: Encrypt with specific vault ID

```bash
ansible-vault encrypt --vault-id prod@prompt secrets.yml
```

## 风险提示

> ⚠️ **MEDIUM**: Encrypts sensitive data; keep vault password safe

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]

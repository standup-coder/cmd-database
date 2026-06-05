---
cmd_name: ansible-vault decrypt
cmd_category: "容器编排/K8s配置管理"
cmd_dimension: Kubernetes Config Management
cmd_install: pip install ansible
cmd_platforms:
- linux
- darwin
- windows
summary: "Decrypt Ansible vault files"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-config.yaml
---


# ansible-vault decrypt

> Decrypt Ansible vault files

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-vault decrypt [file]
```

## 示例

### 示例 1: Decrypt secrets file

```bash
ansible-vault decrypt secrets.yml
```

### 示例 2: Decrypt to different file

```bash
ansible-vault decrypt --output=plain.yml secrets.yml
```

### 示例 3: Decrypt with password file

```bash
ansible-vault decrypt --vault-password-file=.vault_pass secrets.yml
```

## 风险提示

> ⚠️ **MEDIUM**: Exposes encrypted data

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]

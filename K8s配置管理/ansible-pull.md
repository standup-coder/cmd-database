---
{
  "cmd_name": "ansible-pull",
  "cmd_category": "Kubernetes Config Management",
  "cmd_dimension": "Kubernetes Config Management",
  "cmd_install": "pip install ansible",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-config.yaml"
}
---

# ansible-pull

> Pull and execute Ansible playbooks from VCS

## 安装

```bash
pip install ansible
```

## 用法

```
ansible-pull [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-U` | Repository URL |
| `-d` | Destination directory |

## 示例

### 示例 1: Pull and run playbooks from Git

```bash
ansible-pull -U https://github.com/user/playbooks.git
```

### 示例 2: Pull Kubernetes config and apply

```bash
ansible-pull -U https://github.com/user/k8s-config.git -i localhost, local.yml
```

### 示例 3: Pull and check without applying

```bash
ansible-pull -U https://github.com/user/playbooks.git --check
```

## 风险提示

> ⚠️ **MEDIUM**: Pulls and executes remote playbooks

## 所属维度

[[K8s配置管理-MOC|Kubernetes Config Management]]

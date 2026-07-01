---
{
  "cmd_name": "terraform",
  "cmd_category": "云平台/Terraform",
  "cmd_dimension": "Terraform",
  "cmd_install": "参考 https://developer.hashicorp.com/terraform/install",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "terraform plan",
    "terraform apply",
    "terraform init"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/cloud/terraform.yaml"
}
---

# terraform

> 基础设施即代码工具，管理云资源

## 安装

```bash
参考 https://developer.hashicorp.com/terraform/install
```

## 用法

```
terraform <子命令> [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `-version` | 显示版本信息 |
| `-help` | 显示帮助信息 |

## 示例

### 示例 1: 初始化工作目录

```bash
terraform init
```

### 示例 2: 预览将要执行的资源变更

```bash
terraform plan
```

### 示例 3: 应用配置创建/更新资源

```bash
terraform apply
```

### 示例 4: 销毁所有管理的基础设施

```bash
terraform destroy
```

## 关联命令

- [[terraform plan]]
- [[terraform apply]]
- [[terraform init]]

## 所属维度

[[Terraform-MOC|云平台/Terraform]]

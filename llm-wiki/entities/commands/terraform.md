---
cmd_name: terraform
cmd_category: 云平台/Terraform
cmd_dimension: Terraform
cmd_install: 参考 https://developer.hashicorp.com/terraform/install
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- terraform plan
- terraform apply
- terraform init
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: 基础设施即代码工具，管理云资源
created: '2026-06-04'
source_file: data/cloud/terraform.yaml
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

### 初始化工作目录

```bash
terraform init
```

### 预览将要执行的资源变更

```bash
terraform plan
```

### 应用配置创建/更新资源

```bash
terraform apply
```

### 销毁所有管理的基础设施

```bash
terraform destroy
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Terraform-MOC|云平台/Terraform]]

---
cmd_name: aws sts
cmd_category: 云平台/AWS CLI
cmd_dimension: AWS CLI
cmd_install: 参考 https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- aws configure
- aws s3
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: AWS Security Token Service，管理临时凭证
created: '2026-06-04'
source_file: data/cloud/aws-cli.yaml
---
# aws sts

> AWS Security Token Service，管理临时凭证

## 安装

```bash
参考 https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

## 用法

```
aws sts <命令> [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--duration-seconds` | 临时凭证有效期（秒） |

## 示例

### 获取当前调用者身份

```bash
aws sts get-caller-identity
```

### 扮演IAM角色获取临时凭证

```bash
aws sts assume-role --role-arn arn:aws:iam::123456789012:role/MyRole --role-session-name mysession
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[AWS CLI-MOC|云平台/AWS CLI]]

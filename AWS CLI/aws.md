---
{
  "cmd_name": "aws",
  "cmd_category": "云平台/AWS CLI",
  "cmd_dimension": "AWS CLI",
  "cmd_install": "pip install awscli 或 brew install awscli (macOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "aws configure",
    "aws sts"
  ],
  "cmd_tags": [
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/cloud/aws-cli.yaml"
}
---

# aws

> AWS 命令行接口，管理 AWS 服务和资源

## 安装

```bash
pip install awscli 或 brew install awscli (macOS)
```

## 用法

```
aws [服务] [操作] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--profile` | 指定 AWS 配置文件 |
| `--region` | 指定 AWS 区域 |
| `--output` | 输出格式 (json/text/table) |
| `--query` | JMESPath 查询过滤输出 |
| `--dry-run` | 模拟运行不实际执行 |

## 示例

### 示例 1: 列出所有 S3 存储桶

```bash
aws s3 ls
```

### 示例 2: 查询 EC2 实例 ID 和状态

```bash
aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,State.Name]'
```

### 示例 3: 查看当前认证身份

```bash
aws sts get-caller-identity
```

### 示例 4: 使用 prod 配置上传文件

```bash
aws --profile prod s3 cp file.txt s3://my-bucket/
```

## 关联命令

- [[aws configure]]
- [[aws sts]]

## 风险提示

> ⚠️ **HIGH**: 误操作可能产生费用或删除重要资源，建议开启 MFA

## 所属维度

[[AWS CLI-MOC|云平台/AWS CLI]]

---
{
  "cmd_name": "aws s3",
  "cmd_category": "云平台/AWS CLI",
  "cmd_dimension": "AWS CLI",
  "cmd_install": "同 aws cli",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "aws",
    "aws configure"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/cloud/aws-cli.yaml"
}
---

# aws s3

> S3 存储桶和对象管理

## 安装

```bash
同 aws cli
```

## 用法

```
aws s3 [命令] [参数]
```

## 参数

| Flag | Description |
|------|-------------|
| `--recursive` | 递归操作 |
| `--exclude` | 排除匹配的文件 |
| `--include` | 包含匹配的文件 |
| `--acl` | 设置访问控制 (private/public-read) |

## 示例

### 示例 1: 创建存储桶

```bash
aws s3 mb s3://my-bucket
```

### 示例 2: 递归上传目录

```bash
aws s3 cp ./dist s3://my-bucket/ --recursive
```

### 示例 3: 同步本地目录到 S3（删除多余文件）

```bash
aws s3 sync ./local s3://my-bucket/ --delete
```

### 示例 4: 清空存储桶所有对象

```bash
aws s3 rm s3://my-bucket/ --recursive
```

## 关联命令

- [[aws]]
- [[aws-configure]]

## 风险提示

> ⚠️ **HIGH**: sync --delete 会删除目标端多余文件，操作不可逆

## 所属维度

[[AWS CLI-MOC|云平台/AWS CLI]]

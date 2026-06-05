---
cmd_name: aws eks
cmd_category: 云平台/AWS CLI
cmd_dimension: AWS CLI
cmd_install: 同 aws cli
cmd_platforms:
- linux
- darwin
- windows
summary: "EKS Kubernetes 集群管理"
cmd_level: intermediate
cmd_related:
- aws
cmd_tags:
- kubernetes
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/cloud/aws-cli.yaml
---


# aws eks

> EKS Kubernetes 集群管理

## 安装

```bash
同 aws cli
```

## 用法

```
aws eks [命令] [参数]
```

## 示例

### 示例 1: 列出所有 EKS 集群

```bash
aws eks list-clusters
```

### 示例 2: 更新 kubeconfig 连接 EKS

```bash
aws eks update-kubeconfig --name my-cluster
```

### 示例 3: 查看集群详情

```bash
aws eks describe-cluster --name my-cluster
```

## 关联命令

- [[aws]]

## 所属维度

[[AWS CLI-MOC|云平台/AWS CLI]]

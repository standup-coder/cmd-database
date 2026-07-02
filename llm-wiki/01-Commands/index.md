---
title: 命令索引
tags: ["index", "commands"]
updated: "2026-07-02"
---

# 命令索引

> 01-Commands 目录包含所有 1112 个命令的详细文档页面。

## 统计

- **命令总数**: 1112 个
- **分类数**: 106 个

## 浏览方式

### 按 MOC 分类浏览

完整分类请参阅 [[00-Maps/index|MOC 索引总览]]，按领域浏览命令。

### 按字母顺序

命令文件按命令名称的首字母组织：

| 首字母 | 示例命令 |
|--------|----------|
| a | [[ab]], [[accelerate]], [[ansible]], [[aws]] |
| b | [[bash]], [[buildah]], [[bazel]] |
| c | [[cargo]], [[curl]], [[containerd]] |
| d | [[docker-run]], [[deepspeed]], [[dig]] |
| e | [[etcdctl-get]], [[eksctl-create-cluster]] |
| f | [[fio]], [[flink]], [[flux-bootstrap-git]] |
| g | [[git-clone]], [[gcloud]], [[grafana-server]] |
| h | [[helm-install]], [[huggingface-cli]] |
| i | [[istioctl-version]], [[iperf3]] |
| j | [[jq]], [[journalctl]] |
| k | [[kubectl-apply]], [[kafka-console-producer]] |
| l | [[llama-factory]], [[lm-eval]] |
| m | [[make]], [[minikube]], [[mlflow]] |
| n | [[nmap]], [[nginx]], [[npm-install]] |
| o | [[ollama]], [[onnxruntime]] |
| p | [[pip]], [[podman]], [[prometheus]] |
| q | [[qdrant]] |
| r | [[redis-cli]], [[rsync]], [[rustc]] |
| s | [[ssh]], [[spark-submit]], [[systemctl-status]] |
| t | [[terraform-apply]], [[torchrun]], [[trivy-image]] |
| u | [[unsloth]], [[ufw-allow]] |
| v | [[vllm]], [[vmstat]] |
| w | [[wget]], [[wrk]] |
| x | [[xargs]] |
| y | [[yarn]], [[yum-install]] |
| z | [[zookeeper-shell]] |

## Dataview 动态列表

```dataview
TABLE cmd_category, cmd_level
FROM "01-Commands"
SORT file.name
LIMIT 50
```

## 相关索引

- [[00-Maps/index|MOC 索引总览]] — 按领域分类浏览
- [[../index|Wiki 首页]] — 返回主页

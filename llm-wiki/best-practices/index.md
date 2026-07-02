---
title: 最佳实践索引
tags: ["index", "best-practices"]
updated: "2026-07-02"
---

# 最佳实践索引

> best-practices 目录包含所有命令的最佳实践指南，以 `bp-` 前缀命名。

## 统计

- **最佳实践总数**: 718 个

## 浏览方式

### 按领域浏览

最佳实践与命令一一对应，可通过 MOC 分类浏览：

- [[00-Maps/index|MOC 索引总览]] — 按领域分类查看相关最佳实践
- [[01-Commands/index|命令索引]] — 查看命令详情时获取最佳实践

### 示例

| 命令 | 最佳实践 |
|------|----------|
| [[01-Commands/docker-run\|docker-run]] | [[bp-docker-run]] |
| [[01-Commands/kubectl-apply\|kubectl-apply]] | [[bp-kubectl-apply]] |
| [[01-Commands/terraform-apply\|terraform-apply]] | [[bp-terraform-apply]] |
| [[01-Commands/deepspeed\|deepspeed]] | [[bp-deepspeed]] |
| [[01-Commands/vllm\|vllm]] | [[bp-vllm]] |

## Dataview 动态列表

```dataview
TABLE file.name AS "最佳实践"
FROM "best-practices"
WHERE file.name != "index.md"
SORT file.name
LIMIT 50
```

## 相关索引

- [[../index|Wiki 首页]]
- [[01-Commands/index|命令索引]]

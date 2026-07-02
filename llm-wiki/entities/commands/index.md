---
title: 命令实体索引
tags: ["index", "entities", "commands"]
updated: "2026-07-02"
---

# 命令实体索引

> entities/commands 目录包含所有命令的结构化实体数据。

## 统计

- **命令实体总数**: 717 个

## 说明

本目录包含命令的结构化元数据，与 `01-Commands/` 目录下的文档页面一一对应。

- `01-Commands/` — 面向用户的文档格式
- `entities/commands/` — 结构化数据格式（供程序处理）

## Dataview 动态列表

```dataview
TABLE cmd_category, cmd_level
FROM "entities/commands"
SORT file.name
LIMIT 50
```

## 相关索引

- [[../index|实体索引]]
- [[../../01-Commands/index|命令文档索引]]
- [[../../index|Wiki 首页]]

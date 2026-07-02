# data/ 目录索引

> YAML 单一数据源，包含所有命令定义

## 数据统计

- **总命令数**: 1112
- **分类数**: 106
- **数据格式**: YAML

## 目录结构

| 子目录 | 命令数 | 说明 |
|--------|--------|------|
| [`ai/`](ai/) | 240 | AI 基础设施 |
| [`bigdata/`](bigdata/) | 53 | 大数据工具 |
| [`build-tools/`](build-tools/) | 10 | 构建工具 |
| [`cicd/`](cicd/) | 9 | CI/CD 工具 |
| [`cloud/`](cloud/) | 13 | 云平台 |
| [`container/`](container/) | 339 | 容器编排 |
| [`database/`](database/) | 64 | 数据库 |
| [`diagnostic/`](diagnostic/) | 27 | 系统诊断 |
| [`hardware/`](hardware/) | 64 | 硬件工具 |
| [`lang/`](lang/) | 47 | 编程语言 |
| [`network/`](network/) | 57 | 网络工具 |
| [`os/`](os/) | 153 | 操作系统 |
| [`shell/`](shell/) | 5 | Shell 脚本 |
| [`vcs/`](vcs/) | 31 | 版本控制 |

## 元数据文件

- [`metadata.yaml`](metadata.yaml) — 分类元数据定义

## 数据格式

每个命令定义包含：

```yaml
name: command-name
description: "命令描述"
category: "分类名称"
level: "基础|进阶|高级"
tags: ["tag1", "tag2"]
usage: "使用示例"
```

## 相关文件

- [`README.md`](README.md) — 详细说明
- [`../INDEX.md`](../INDEX.md) — 项目主索引
- [`../COMMANDS.md`](../COMMANDS.md) — 完整命令清单
# cmd4coder 项目索引

> 本文件是 cmd4coder 的全局导航图，按功能领域列出各层级的入口。  
> 如果第一次访问，建议先阅读 [`README.md`](README.md)。

---

## 📊 项目概览

| 指标 | 数值 |
|------|------|
| 总命令 | **1112** |
| 分类 | **106** |
| AI 命令 | 240（22 分类） |
| LLM-Wiki 页面 | 755 |
| Wiki 双向链接 | 2105+ |
| Agent Skills | 43 |
| Go 版本 | ≥ 1.24 |
| 当前版本 | 1.8.0 |

---

## 🧭 一级索引

| 层级 | 说明 | 索引文件 |
|------|------|----------|
| **CLI 入口** | Go 命令行程序 | [`cmd/README.md`](cmd/README.md) |
| **内部实现** | 数据模型、加载、服务、TUI | [`internal/README.md`](internal/README.md) |
| **可复用包** | JSON/Markdown/YAML 导出 | [`pkg/README.md`](pkg/README.md) |
| **数据源** | YAML 单一数据源 | [`data/README.md`](data/README.md) |
| **脚本工具** | 构建、数据维护、Wiki 转换 | [`scripts/README.md`](scripts/README.md) |
| **项目文档** | 报告、指南、架构说明、GitHub Pages | [`docs/README.md`](docs/README.md) |
| **LLM-Wiki** | Obsidian 知识库 | [`llm-wiki/index.md`](llm-wiki/index.md) |

---

## 🚀 快速开始

### 模式 A：CLI 工具

```bash
# 列出分类
go run ./cmd/cli categories -d ./data

# 搜索命令
go run ./cmd/cli search "distributed training" -d ./data

# 查看详情
go run ./cmd/cli show deepspeed -d ./data

# TUI 交互模式
go run ./cmd/cli -d ./data

# 构建二进制
go build -o bin/cmd4coder ./cmd/cli
```

### 模式 B：LLM-Wiki

```bash
# 在 Obsidian 中打开 Vault
open -a Obsidian ./llm-wiki

# YAML 变更后重新生成 Wiki
python3 scripts/wiki/convert_to_wiki.py

# 检查 Wiki 健康
python3 scripts/wiki/wiki_status.py
```

---

## 📚 关键文件

| 文件 | 用途 |
|------|------|
| [`README.md`](README.md) | 项目主介绍 |
| [`COMMANDS.md`](COMMANDS.md) | 完整 1112 条命令清单 |
| [`data/metadata.yaml`](data/metadata.yaml) | 106 分类元数据 |
| [`go.mod`](go.mod) / [`go.sum`](go.sum) | Go 依赖 |
| [`Makefile`](Makefile) | 常用构建任务 |
| [`embed.go`](embed.go) | 嵌入静态资源 |

---

## 🗺️ 领域地图

| 领域 | 命令数 | 数据目录 |
|------|--------|----------|
| 容器编排 | 339 | [`data/container/`](data/container/) |
| AI 基础设施 | 240 | [`data/ai/`](data/ai/) |
| 操作系统 | 153 | [`data/os/`](data/os/) |
| 硬件 | 64 | [`data/hardware/`](data/hardware/) |
| 数据库 | 64 | [`data/database/`](data/database/) |
| 大数据 | 53 | [`data/bigdata/`](data/bigdata/) |
| 网络工具 | 57 | [`data/network/`](data/network/) |
| 编程语言 | 47 | [`data/lang/`](data/lang/) |
| 版本控制 | 31 | [`data/vcs/`](data/vcs/) |
| 系统诊断 | 27 | [`data/diagnostic/`](data/diagnostic/) |
| 云平台 | 13 | [`data/cloud/`](data/cloud/) |
| 构建工具 | 10 | [`data/build-tools/`](data/build-tools/) |
| CI/CD | 9 | [`data/cicd/`](data/cicd/) |
| Shell 脚本 | 5 | [`data/shell/`](data/shell/) |

# 命令行语料数据库

持续沉淀每一条命令行的**内涵外延、使用方式与风险**，最终支撑智能体问答与问题排查。

![License](https://img.shields.io/badge/license-MIT-green)

## 📖 这是什么

一个以 **Markdown** 为核心的命令行知识库。根目录按领域扁平化为「**中文领域文件夹 / 命令 md**」的**二层**结构：每个命令一篇 `md`，记录它的用途、用法、选项、示例、风险与关联命令。配套一个 Go CLI（位于 [`tools/cmd/`](./tools/cmd/)）做检索与验证。

```
cmd-database/
├── 大模型训练/            ← 领域文件夹（中文）
│   ├── _MOC.md            ← 领域入口索引
│   ├── deepspeed.md       ← 命令内涵外延
│   ├── accelerate.md
│   └── bp-deepspeed.md    ← 生产最佳实践
├── 大模型推理/            ← vllm, sglang, tensorrt-llm ...
├── Java诊断/             ← arthas, jad, watch ...
├── Linux核心/            ← ls, grep, find ...
├── Kubernetes命令/       ← kubectl 及生态
├── Docker命令/           ← docker 全家桶
├── …（共 100 个领域）
├── 场景/  概念/  FAQ/  排障/   ← 多轮问答与沉淀（待填充）
├── tools/cmd/            ← CLI 工具与 YAML 数据源（收敛于此）
├── docs/                 ← 项目文档与报告
├── llm-wiki/             ← Obsidian Vault 源（生成中间产物）
└── INDEX.md              ← 全领域索引
```

> 完整领域列表与命令计数见 [`INDEX.md`](./INDEX.md)。

## 🔍 怎么用

### 浏览语料
直接按领域文件夹查阅，或打开 `INDEX.md`。每个领域 `_MOC.md` 是该领域的命令速查入口。

### CLI 检索（开发/运维）
```bash
cd tools/cmd

# 列出分类
go run ./cmd/cli categories -d ./data

# 搜索命令
go run ./cmd/cli search "distributed training" -d ./data

# 查看详情
go run ./cmd/cli show deepspeed -d ./data

# 构建二进制
go build -o bin/cmd4coder ./cmd/cli
```

### 用 Obsidian 浏览（可视化双向链接）
```bash
open -a Obsidian .   # 把整个仓库当作 Vault 打开
```

## 🧱 内容来源与生成链路

```
tools/cmd/data/*.yaml   ──(单一数据源)──→   cmd4coder CLI（检索/验证）
        │
        └──(convert_to_wiki.py)──→  根目录 <领域>/<命令>.md（本库主体）
```

- **YAML 单一数据源**：[`tools/cmd/data/`](./tools/cmd/data/) 下的 YAML 是命令定义的权威来源。
- **Wiki 转换**：[`tools/cmd/scripts/wiki/convert_to_wiki.py`](./tools/cmd/scripts/wiki/convert_to_wiki.py) 把 YAML 生成带 frontmatter 与双向链接的 md。
- 修改 YAML → 重新生成 md → CLI 自动同步。

### 添加 / 修改命令
1. 编辑 `tools/cmd/data/<领域>/<文件>.yaml`。
2. 校验：`cd tools/cmd && go run ./cmd/validator -d ./data -v`
3. 重新生成 md：`python3 tools/cmd/scripts/wiki/convert_to_wiki.py`
4. 提交。

## 🛠️ 开发

```bash
cd tools/cmd
go test ./...                              # 测试
go build -o bin/cmd4coder ./cmd/cli        # 构建
go run ./cmd/validator -d ./data -v        # 校验数据
```

## 📚 目录速查

| 入口 | 内容 |
|------|------|
| [`INDEX.md`](./INDEX.md) | 全领域索引与命令计数 |
| [`tools/cmd/`](./tools/cmd/) | Go CLI、YAML 数据源、生成/校验脚本 |
| [`docs/`](./docs/) | 项目文档、改造报告 |
| [`llm-wiki/`](./llm-wiki/) | Obsidian Vault 源（生成中间产物） |

## 📄 许可证

MIT License。详见 [docs/legal/LICENSE](./docs/legal/LICENSE)。

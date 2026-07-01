# cmd4coder — 命令行工具大全 + LLM-Wiki 知识库

![Version](https://img.shields.io/badge/version-1.8.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Go Version](https://img.shields.io/badge/go-%3E%3D1.24-blue)
![Test Coverage](https://img.shields.io/badge/coverage-80.7%25-green)
![Wiki Pages](https://img.shields.io/badge/llm--wiki-755%20pages-purple)
![AI Commands](https://img.shields.io/badge/AI%20commands-240-orange)

## 📖 简介

cmd4coder 是一个**双模态**开发者工具项目：

- **模式 A**：Go CLI 工具 — 面向运维工程师和开发者的命令行速查手册
- **模式 B**：LLM-Wiki 知识库 — 基于 Obsidian 的大模型领域多轮问答语料库

> **单一数据源**：所有内容从 `data/*.yaml` 生成，修改 YAML → CLI 和 Wiki 自动同步。

---

## 🔄 双模态架构

```
┌─────────────────┐     ┌──────────────────┐
│   data/*.yaml   │────→│   cmd4coder CLI  │  Mode A: 终端查询
│   (1112 命令)   │     │   (Go + Bubbletea)│
└─────────────────┘     └──────────────────┘
         │
         ↓
┌──────────────────┐
│   LLM-Wiki       │  Mode B: 知识库 + 多轮问答
│   (Obsidian)     │
│   755 页面       │
│   2105+ 双向链接 │
└──────────────────┘
```

| 维度 | CLI 模式 | Wiki 模式 |
|------|----------|-----------|
| **交互** | 单轮查询 `search "training"` | 多轮对话场景引导 |
| **检索** | 模糊搜索 + 优先级排序 | 分层检索 + 语义关联 |
| **关联** | `related_commands` 文本 | `[[wikilinks]]` 双向链接 |
| **输出** | 表格/JSON/Markdown | Markdown + frontmatter |
| **适用** | 快速查命令 | 学习路线、故障排查 |

---

## 📑 层级索引

快速定位项目各层级入口：

| 层级 | 内容 | 索引 |
|------|------|------|
| **全局导航** | 项目地图与关键数字 | [`INDEX.md`](INDEX.md) |
| **CLI 入口** | `cmd/cli` 主程序、`cmd/validator` 验证器 | [`cmd/README.md`](cmd/README.md) |
| **内部实现** | model / data / service / ui / version | [`internal/README.md`](internal/README.md) |
| **可复用包** | JSON / Markdown / YAML 导出 | [`pkg/README.md`](pkg/README.md) |
| **数据源** | YAML 单一数据源与 12 大领域 | [`data/README.md`](data/README.md) |
| **脚本工具** | 构建、数据维护、Wiki 转换 | [`scripts/README.md`](scripts/README.md) |
| **项目文档** | 报告、指南、GitHub Pages | [`docs/README.md`](docs/README.md) |
| **LLM-Wiki** | Obsidian 知识库入口 | [`llm-wiki/index.md`](llm-wiki/index.md) |

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
# 1. 在 Obsidian 中打开 Vault
open -a Obsidian ./llm-wiki

# 2. 使用 Agent Skills 查询
kimi "query the wiki about ZeRO optimization"
kimi "what tool should I use for single-GPU fine-tuning?"

# 3. 摄入新文档
kimi "ingest docs/new-paper.pdf into the wiki"

# 4. 检查 Wiki 健康
python3 scripts/wiki/wiki_status.py
```

---

## 📊 数据统计

| 指标 | CLI | Wiki |
|------|-----|------|
| 总命令 | **1112** | 676 实体页 + 65 MOC |
| 分类 | **106** | 106 维度索引 |
| AI 命令 | 240 (22 分类) | 200+ 含场景/概念/FAQ |
| 搜索速度 | <100ms | Index-only ~18K tokens |
| 双向链接 | — | **2,105** |
| Broken Links | — | **0** |
| 场景页 | — | 4 (多轮问答) |
| 概念页 | — | 4 (ZeRO, KV-Cache, LoRA, Speculative Decoding) |
| FAQ 页 | — | 5 |

---

## 📋 完整命令清单

全部 **1112** 条命令已按功能领域简单分类，详见 [`COMMANDS.md`](COMMANDS.md)。

| 分类 | 命令数 | 覆盖范围 |
|------|--------|----------|
| 容器编排 | 339 | Docker、Podman、Kubernetes、Helm、Istio、Service Mesh、本地 K8s、安全、运行时等 |
| AI 基础设施 | 240 | 大模型训练/推理、Agent、RAG、向量数据库、AI 网关、AI 安全、编码助手、MLOps 等 |
| 硬件 | 64 | CPU/GPU/存储/RAID、传感器、固件、UEFI、IPMI、嵌入式/I2C/GPIO 等 |
| 操作系统 | 153 | Ubuntu/CentOS 包管理、systemd、防火墙、Linux 核心、用户与磁盘管理等 |
| 网络工具 | 57 | curl、nmap、网络安全、性能压测、抓包、代理、Web 服务器、VPN、DNS 等 |
| 数据库 | 64 | MySQL、PostgreSQL、Redis、MongoDB、SQLite、Oracle、SQL Server、NoSQL、时序/OLAP 等 |
| 大数据 | 53 | Hadoop、Spark、Flink、Kafka、Hive、Presto/Trino、Airflow、数据湖、调度等 |
| 编程语言 | 47 | Java/Go/Python/Node.js/Rust/PHP/Ruby/.NET/Scala/Kotlin/Groovy 等工具链 |
| 版本控制 | 31 | Git、SVN |
| 系统诊断 | 27 | Arthas、tsar、strace、perf、bpftrace、JVM 诊断等 |
| 云平台 | 13 | AWS、Azure、GCP、DigitalOcean、Linode、Terraform、Pulumi 等 |
| 构建工具 | 10 | Maven、Gradle、Make、CMake |
| CI/CD | 9 | GitHub Actions、GitLab Runner、Jenkins、Tekton、Skaffold 等 |
| Shell 脚本 | 5 | Bash Shell 编写和调试工具 |

---

## 🗂️ 目录结构

```
cmd4coder/
│
├──  Mode A: CLI 工具
│
├── cmd/
│   ├── cli/                    # 主 CLI 程序 (Go + Cobra + Bubbletea)
│   └── validator/              # YAML 数据验证工具
├── internal/
│   ├── model/                  # 数据模型
│   ├── data/                   # 数据加载和索引
│   ├── service/                # 业务逻辑层
│   └── ui/tui/                 # TUI 用户界面
├── pkg/export/                 # Markdown/JSON 导出
├── data/                       # YAML 命令清单 (单一数据源)
│   ├── metadata.yaml           # 106 分类元数据
│   ├── ai/                     # 22 个 AI 分类 (240 命令)
│   │   ├── llm-training.yaml
│   │   ├── llm-inference.yaml
│   │   ├── agent-engineering.yaml
│   │   ├── harness-engineering.yaml
│   │   ├── ai-compiler.yaml
│   │   ├── model-interpretability.yaml
│   │   ├── federated-learning.yaml
│   │   └── ... (15 more)
│   ├── container/              # 容器与 K8s 生态 (339 命令)
│   │   ├── docker/             # Docker 与替代容器运行时
│   │   ├── k8s/                # Kubernetes 各主题命令
│   │   └── cloudnative/        # Helm、Istio、本地 K8s 等云原生扩展
│   ├── database/               # MySQL/PostgreSQL/Redis/NoSQL/时序
│   ├── build-tools/            # Maven/Gradle/Make/CMake
│   ├── network/                # DNS/HTTP/诊断/安全
│   ├── os/                     # Linux 系统命令
│   ├── hardware/               # CPU/GPU/存储/固件/嵌入式
│   └── ...
│
├──  Mode B: LLM-Wiki
│
├── llm-wiki/                   # Obsidian Vault
│   ├── .obsidian/              # Obsidian 配置
│   ├── entities/commands/      # 676 命令详情页
│   ├── 00-Maps/                # 65 MOC 索引页
│   ├── concepts/               # 4 核心概念页
│   ├── synthesis/scenes/       # 4 多轮问答场景
│   ├── references/faqs/        # 5 FAQ 页
│   ├── _meta/
│   │   ├── manifest.json       # 源文件追踪
│   │   └── taxonomy.md         # 标签分类
│   ├── index.md                # Vault 入口
│   ├── log.md                  # 操作日志
│   ├── hot.md                  # 热缓存
│   └── .env                    # Wiki 配置
│
├── .agents/skills/             # 43 个 obsidian-wiki skills
│   ├── wiki-ingest/            # 文档蒸馏摄入
│   ├── wiki-query/             # 分层检索查询
│   ├── wiki-status/            # 健康仪表盘
│   ├── wiki-lint/              # 链接质量检查
│   └── ...
│
├── scripts/                    # 转换与工具脚本
│   ├── build/                  # 构建脚本（build.sh / build.ps1 / test_core.sh）
│   ├── data/                   # 数据维护（去重、补全、生成 COMMANDS.md）
│   ├── wiki/                   # Wiki 转换与维护
│   │   ├── convert_to_wiki.py  # YAML → Markdown 转换器
│   │   ├── generate_scenes_and_faqs.py
│   │   ├── fix_wiki_links_v3.py
│   │   └── wiki_status.py
│   └── legacy/                 # 一次性批量添加脚本
│
└── docs/                       # 项目文档
    ├── reports/llm-wiki/       # 改造方案与实施报告
    └── ...
```

---

## 🤖 AI 基础设施覆盖 (22 分类, 225 命令)

| 维度 | 命令数 | 代表工具 |
|------|--------|----------|
| 大模型训练 | 27 | DeepSpeed, Accelerate, Unsloth, GRPO, DPO |
| 大模型推理 | 26 | vLLM, SGLang, TensorRT-LLM, Ollama |
| Agent 工程 | 19 | LangChain, AutoGen, DSPy, CrewAI, Dify |
| Harness 工程 | 21 | SWE-Bench, Arena, LiveCodeBench, Red-Teaming |
| 模型生态 | 16 | HuggingFace, ONNX, GGUF, 量化工具 |
| 数据与标注 | 13 | Argilla, Label Studio, FiftyOne |
| 监控与评估 | 16 | MLflow, W&B, Langfuse, Phoenix |
| 向量数据库 | 15 | Chroma, Milvus, Weaviate, Pinecone |
| AI 网关 | 6 | Helicone, Portkey, OpenRouter, Promptfoo |
| AI 安全 | 5 | Garak, ModelScan, LLM Guard, Inspect AI |
| 多模态 | 6 | ComfyUI, Whisper, CLIP, LLaVA |
| AI 编程 | 5 | Aider, OpenHands, SWE-Agent, Continue.dev |
| RAG 基础设施 | 5 | Unstructured, LlamaParse, Docling, Marker |
| 边缘 AI | 4 | TFLite, ExecuTorch, MediaPipe, Paddle Lite |
| AI 编译器 | 6 | TVM, IREE, MLIR, TensorRT, XLA |
| 模型可解释性 | 5 | SHAP, LIME, Captum |
| 联邦学习 | 4 | Flower, Opacus, CrypTen |
| 模型架构 | 9 | transformers-cli, bertviz, calflops, Mamba |
| AI 应用 | 6 | PromptFlow, n8n, Text2SQL, Vanna |
| ML 框架 | 4 | PyTorch, TensorFlow, JAX, Paddle |
| MLOps 平台 | 2 | Kubeflow, MLflow |
| 模型服务 | 4 | BentoML, KServe |

---

## 🔧 开发

### CLI 模式开发

```bash
# 运行测试
go test ./...

# 构建
go build -o bin/cmd4coder ./cmd/cli

# 验证数据
go run ./cmd/validator -d ./data -v
```

### Wiki 模式开发

```bash
# YAML 变更后重新生成 Wiki
python3 scripts/wiki/convert_to_wiki.py

# 修复链接
python3 scripts/wiki/fix_wiki_links_v3.py

# 检查健康
python3 scripts/wiki/wiki_status.py

# 生成场景/FAQ
python3 scripts/wiki/generate_scenes_and_faqs.py
```

### 数据规范

YAML 命令定义示例：

```yaml
category: "AI基础设施/大模型训练"
commands:
  - name: deepspeed
    category: "AI基础设施/大模型训练"
    install_required: true
    install_method: "pip install deepspeed"
    description: "微软DeepSpeed大规模分布式训练框架"
    usage:
      - "deepspeed [OPTIONS] SCRIPT.py"
    options:
      - flag: "--num_gpus"
        description: "使用的GPU数量"
    examples:
      - command: "deepspeed --num_gpus=4 train.py"
        description: "4卡训练"
    platforms: ["linux", "darwin", "windows"]
    related_commands: ["accelerate", "torchrun"]
    risks:
      - level: medium
        description: "大规模训练消耗大量GPU资源"
    references:
      - "https://www.deepspeed.ai/"
```

---

## 📚 文档

| 文档 | 内容 |
|------|------|
| `docs/reports/llm-wiki/IMPLEMENTATION_REPORT.md` | LLM-Wiki 改造实施报告 |
| `docs/reports/ai-commands-gap-analysis.md` | AI 命令缺口分析 |
| `docs/reports/project-evaluation-report.md` | 项目评估报告 |
| `llm-wiki/AGENTS.md` | Agent Bootstrap |
| `llm-wiki/CLAUDE.md` | Claude Code 上下文 |

---

## 🤝 贡献

### 添加新命令

1. 在 `data/` 对应 YAML 文件中添加命令定义
2. 运行 `go run ./cmd/validator -d ./data -v` 验证
3. 运行 `python3 scripts/wiki/convert_to_wiki.py` 同步到 Wiki
4. 提交 PR

### 添加场景页

1. 编辑 `scripts/wiki/generate_scenes_and_faqs.py`
2. 运行脚本生成场景页
3. 验证链接：`python3 scripts/wiki/wiki_status.py`

---

## 📄 许可证

MIT License. 详见 [docs/legal/LICENSE](docs/legal/LICENSE)。

---

⭐ 如果这个项目对你有帮助，请给一个 Star！

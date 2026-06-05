# cmd4coder → LLM-Wiki 改造方案

> 目标：将 cmd4coder 的命令数据从 YAML 结构化数据改造为 Obsidian Wiki 知识库，作为智能体多轮问答语料库  
> 当前规模：693 命令 / 58 分类 / 64 数据文件  
> 版本：v1.0

---

## 一、改造动因分析

### 1.1 当前 cmd4coder 的局限

| 维度 | 现状 | 限制 |
|------|------|------|
| 数据结构 | YAML 结构化 | 非人类可读，不适合 LLM 上下文学习 |
| 交互方式 | CLI list/search/show | 单轮查询，无上下文关联 |
| 知识组织 | 平面分类 | 无概念关联、无场景链路 |
| LLM 友好度 | 低 | YAML 解析成本高，语义关联弱 |

### 1.2 Obsidian Wiki 的优势

| 能力 | 价值 |
|------|------|
| **Markdown + YAML frontmatter** | LLM 原生友好，可直接作为 RAG chunk |
| **双向链接 `[[...]]`** | 构建命令-场景-概念关联图 |
| **Tags `#tag`** | 多维度分类，支持交叉检索 |
| **MOC (Map of Content)** | 场景化知识入口，引导多轮问答 |
| **Dataview 查询** | 动态聚合，替代部分 CLI 功能 |

### 1.3 多轮问答语料库需求

```
用户: "我要训练一个7B模型，只有一张4090，有什么方案？"

第1轮 → 定位场景: 单卡训练 + 7B模型 + 显存受限
第2轮 → 推荐工具: [[unsloth]] + [[qlora]] + [[llama-factory]]
第3轮 → 对比方案: Unsloth(速度) vs LLaMA-Factory(功能全面)
第4轮 → 具体命令: 给出 accelerate + peft 的完整配置
第5轮 → 故障排查: 显存OOM → 推荐 [[gradient-checkpointing]] + [[deepspeed-offload]]
```

这需要：**场景页 → 工具页 → 命令页 → 故障页** 的链路导航。

---

## 二、数据模型改造设计

### 2.1 核心实体映射

```
YAML 实体                    Obsidian 实体
─────────────────────────────────────────────────
category (分类)      →       MOC 索引页 (Map of Content)
command (命令)       →       独立笔记页 (Note)
option (参数)        →       笔记内段落 / 独立概念页
example (示例)       →       笔记内代码块 + 场景标签
related_commands     →       双向链接 [[command]]
risks                →       笔记内警告块 + 故障排查页
references           →       外部链接 + 来源元数据
```

### 2.2 单命令页模板

```markdown
---
cmd_name: "deepspeed"
cmd_category: "AI基础设施/大模型训练"
cmd_dimension: "训练"
cmd_install: "pip install deepspeed"
cmd_platforms: ["linux", "darwin", "windows"]
cmd_level: "advanced"
cmd_related: ["accelerate", "torchrun", "megatron-lm", "colossal-ai"]
cmd_tags: ["分布式训练", "ZeRO", "GPU", "大规模", "微软"]
cmd_risk_level: "medium"
cmd_use_cases: ["7B以上模型训练", "多卡并行", "显存优化"]
created: "2026-05-31"
version: "1.0"
---

# deepspeed

## 一句话描述

微软 DeepSpeed 大规模分布式训练框架，支持 ZeRO 优化、3D 并行、Offload。

## 何时使用

- 训练 **7B 以上** 参数模型
- 拥有 **2 张以上 GPU**
- 需要 **显存优化**（单卡放不下模型）
- 需要 **3D 并行**（数据并行 + 模型并行 + 流水线并行）

## 快速开始

```bash
pip install deepspeed
```

## 核心命令

```bash
deepspeed --num_gpus=4 train.py --deepspeed ds_config.json
```

## 常用参数

| 参数 | 说明 | 典型值 |
|------|------|--------|
| `--num_gpus` | GPU 数量 | 4, 8 |
| `--master_port` | 主节点端口 | 29500 |
| `--include` | 指定 GPU | localhost:0,1,2,3 |

## 完整示例

### 示例1: 4卡 ZeRO-2 训练

```bash
deepspeed --num_gpus=4 train.py --deepspeed ds_config_zero2.json
```

> 适用场景：13B 模型，4x A100 40GB

### 示例2: 8卡 ZeRO-3 训练

```bash
deepspeed --include='localhost:0,1,2,3,4,5,6,7' train.py --deepspeed ds_config_zero3.json
```

> 适用场景：70B 模型，8x A100 80GB

## 关联命令

- [[accelerate]] — HuggingFace 分布式配置简化工具
- [[torchrun]] — PyTorch 原生分布式启动器
- [[megatron-lm]] — NVIDIA 大规模训练框架
- [[colossal-ai]] — 统一并行训练框架

## 场景链路

```
[[模型训练场景]] → [[deepspeed]] → [[deepspeed-config]] → [[显存优化技巧]]
```

## 常见问题

### Q: 单卡 4090 24GB 能训练 7B 模型吗？

A: 可以，使用 ZeRO-Offload + [[qlora]] + [[gradient-checkpointing]]：

```bash
deepspeed train.py --deepspeed ds_config_zero3_offload.json
```

### Q: DeepSpeed 和 Accelerate 怎么选？

A: 简单分布式用 [[accelerate]]，超大规模/极致优化用 [[deepspeed]]。

## 风险提醒

> ⚠️ 大规模分布式训练消耗大量 GPU 资源，需合理配置。错误的并行策略可能导致训练速度比单卡还慢。

## 参考链接

- [DeepSpeed 官方文档](https://www.deepspeed.ai/)
- [[分布式训练入门]]
```

### 2.3 MOC 索引页模板

```markdown
---
moc_type: "dimension"
moc_name: "AI基础设施/大模型训练"
moc_order: 93
tags: ["MOC", "AI", "训练"]
---

# AI基础设施/大模型训练

> 大语言模型训练与微调工具链  
> 涵盖：分布式训练、参数高效微调、量化训练、模型评估

## 按场景导航

### 🚀 快速选型

| 场景 | 推荐工具 | 显存需求 |
|------|----------|----------|
| 单卡 4090 微调 7B | [[unsloth]] + [[qlora]] | 16GB |
| 多卡 A100 预训练 70B | [[deepspeed]] + [[megatron-lm]] | 8x 80GB |
| 云端弹性训练 | [[sky-pilot]] + [[modal]] | 按需 |

### 📚 按能力分类

#### 分布式训练
- [[deepspeed]] — ZeRO 优化、3D 并行
- [[accelerate]] — HuggingFace 简化配置
- [[torchrun]] — PyTorch 原生启动
- [[megatron-lm]] — NVIDIA 大规模框架

#### 参数高效微调 (PEFT)
- [[peft]] — LoRA/QLoRA/Adapter 统一库
- [[unsloth]] — 2-5 倍速度提升的微调
- [[axolotl]] — YAML 配置驱动微调

#### 强化学习
- [[trl]] — PPO/DPO/GRPO 训练
- [[grpo]] — DeepSeek-R1 核心方法
- [[dpo]] — 直接偏好优化

### 🔗 关联维度

- [[AI基础设施/大模型推理]] ← 训练完下一步
- [[AI基础设施/模型生态]] ← 模型格式转换
- [[AI基础设施/监控与评估]] ← 训练过程监控

## Dataview 动态列表

```dataview
table cmd_install, cmd_platforms, cmd_risk_level
from "commands"
where cmd_category = "AI基础设施/大模型训练"
sort cmd_name
```
```

---

## 三、Vault 目录结构设计

```
llm-wiki/
├── 00-Inbox/                    # 待整理素材
├── 01-Maps/                     # MOC 索引页
│   ├── AI-基础设施-MOC.md
│   ├── 模型训练-MOC.md
│   ├── 模型推理-MOC.md
│   └── ...
├── 02-Commands/                 # 命令详情页 (693页)
│   ├── deepspeed.md
│   ├── vllm.md
│   └── ...
├── 03-Scenes/                   # 场景页 (多轮问答核心)
│   ├── 单卡微调7B模型.md
│   ├── 多卡预训练70B模型.md
│   ├── 生产环境推理部署.md
│   ├── RAG应用构建.md
│   ├── 模型量化与压缩.md
│   └── ...
├── 04-Concepts/                 # 概念解释页
│   ├── ZeRO优化.md
│   ├── KV-Cache.md
│   ├── 推测解码.md
│   ├── LoRA原理.md
│   └── ...
├── 05-FAQs/                     # 常见问题 (问答对语料)
│   ├── 训练FAQ.md
│   ├── 推理FAQ.md
│   └── ...
├── 06-Troubleshooting/          # 故障排查
│   ├── OOM显存不足.md
│   ├── 训练发散.md
│   └── ...
├── 07-Templates/                # 模板
│   ├── command-template.md
│   ├── scene-template.md
│   └── faq-template.md
├── 99-Meta/
│   └── tags.md
└── .obsidian/
    ├── plugins/
    │   ├── dataview/            # 动态查询
    │   ├── graph-view/          # 知识图谱
    │   └── templater/           # 模板引擎
    └── graph.json               # 图谱配置
```

---

## 四、多轮问答语料库设计

### 4.1 语料组织策略

传统 RAG 是 "问 → 搜 → 答" 的单轮模式。多轮问答需要 **场景上下文 + 工具链路 + 决策树**。

### 4.2 场景页设计（核心创新）

场景页是引导多轮问答的入口。每个场景页 = 一个完整的用户故事。

```markdown
---
scene_name: "单卡4090微调Llama-3-8B"
scene_tags: ["微调", "LoRA", "单卡", "消费级GPU"]
scene_difficulty: "beginner"
scene_commands: ["unsloth", "peft", "transformers-cli", "accelerate"]
scene_related_scenes: ["多卡预训练", "模型量化部署"]
---

# 场景：单卡 4090 微调 Llama-3-8B

## 用户画像

- 只有 1 张 RTX 4090 (24GB)
- 想微调 Llama-3-8B 做领域适配
- 数据量 10K-100K 条

## 第一轮：确认可行性

**用户**: "我只有一张4090，能微调8B模型吗？"

**Agent**:  
可以。8B 模型 FP16 需要 16GB，但微调需要额外显存存优化器状态和梯度。推荐方案：

- [[qlora]] 4-bit 量化 → 显存降至 ~6GB
- [[gradient-checkpointing]] → 显存换时间
- [[unsloth]] → 2-5 倍速度提升

预估显存占用：**18-20GB**（在 4090 24GB 范围内）。

## 第二轮：工具选择

**用户**: "Unsloth 和 LLaMA-Factory 怎么选？"

**Agent**:

| 维度 | [[unsloth]] | [[llama-factory]] |
|------|-------------|-------------------|
| 速度 | ⭐⭐⭐⭐⭐ 最快 | ⭐⭐⭐ 标准 |
| 易用性 | ⭐⭐⭐⭐ 简单 | ⭐⭐⭐⭐⭐ 最全面 |
| 功能 | LoRA/QLoRA | 全功能预训练/RLHF |
| 推荐 | 快速实验 | 生产环境 |

初学者建议先用 [[unsloth]] 跑通，再迁移到 [[llama-factory]]。

## 第三轮：具体命令

**用户**: "给我具体的命令"

**Agent**:

```bash
# 1. 安装
pip install unsloth

# 2. 训练脚本 (Unsloth)
python train.py \
  --model_name unsloth/Meta-Llama-3.1-8B-bnb-4bit \
  --max_seq_length 2048 \
  --lora_r 16 \
  --batch_size 2 \
  --gradient_accumulation_steps 4
```

详见 [[unsloth]] 命令页。

## 第四轮：故障排查

**用户**: "训练到一半报 OOM 了"

**Agent**:

诊断路径：
1. 检查 [[max_seq_length]] 是否过大 → 降至 1024
2. 启用 [[gradient-checkpointing]] → 显存减半
3. 减小 [[lora_r]] → 8 或 4
4. 使用 [[deepspeed-offload]] 将优化器状态放到 CPU

```bash
# DeepSpeed ZeRO-Offload 配置
deepspeed train.py --deepspeed ds_config_zero2_offload.json
```

## 第五轮：部署推理

**用户**: "微调完了怎么部署推理？"

**Agent**:

推荐 [[vllm]] 或 [[ollama]]：

```bash
# 合并 LoRA 权重
llamafactory-cli export --model_dir ./sft_model --export_dir ./merged

# vLLM 部署
python -m vllm.entrypoints.openai.api_server --model ./merged
```

继续 → [[生产环境推理部署]] 场景
```

### 4.3 FAQ 问答对格式

```markdown
---
faq_tags: ["训练", "显存", "4090"]
faq_related: ["unsloth", "qlora", "gradient-checkpointing"]
---

# FAQ: 单卡 4090 能训练多大的模型？

**Q**: 单卡 RTX 4090 (24GB) 能训练多大的 LLM？

**A**: 取决于精度和优化策略：

| 精度 | 优化 | 最大模型 |
|------|------|----------|
| FP16 | 无 | 3B |
| FP16 | Gradient Checkpointing | 7B |
| INT8 | LoRA | 13B |
| NF4 (QLoRA) | Unsloth | 70B |

详细方案见 [[单卡4090微调Llama-3-8B]] 场景页。

**追问1**: QLoRA 会损失多少精度？  
**A**: 通常 < 1% 性能损失，详见 [[量化对模型影响]]。

**追问2**: 70B 量化后推理速度如何？  
**A**: 使用 [[vllm]]  batch 推理可达 20 tokens/s，详见 [[vllm]]。
```

---

## 五、自动化转换方案

### 5.1 转换流程

```
cmd4coder YAML 数据
       │
       ▼
┌─────────────────┐
│  Go/Python 转换器 │  ← 一次性脚本
│                 │
│  1. 解析 YAML   │
│  2. 生成 Markdown│
│  3. 构建链接图谱 │
│  4. 生成 MOC    │
└─────────────────┘
       │
       ▼
Obsidian Vault (Markdown + frontmatter)
       │
       ▼
┌─────────────────┐
│  RAG 预处理     │
│                 │
│  - Chunking     │
│  - Embedding    │
│  - 图谱索引     │
└─────────────────┘
       │
       ▼
LLM 多轮问答语料库
```

### 5.2 转换脚本设计（Go）

```go
// 核心逻辑
type WikiConverter struct {
    dataDir    string
    outputDir  string
}

func (c *WikiConverter) Convert() error {
    // 1. 加载所有 YAML
    commands := c.loadAllCommands()
    
    // 2. 生成命令页
    for _, cmd := range commands {
        c.writeCommandPage(cmd)
    }
    
    // 3. 生成 MOC 页
    c.writeMOCPages()
    
    // 4. 生成场景页（基于规则/模板）
    c.writeScenePages()
    
    // 5. 构建链接图谱 (graph.json)
    c.writeGraphIndex()
    
    return nil
}
```

### 5.3 Chunking 策略

| 粒度 | 内容 | 用途 |
|------|------|------|
| 页面级 | 整个命令页 | 粗检索，确定相关命令 |
| 段落级 | 描述/参数/示例 | 精检索，获取具体用法 |
| 问答对 | FAQ 条目 | 直接匹配用户问题 |
| 场景级 | 完整场景页 | 多轮对话上下文 |

---

## 六、与 Skills 集成方案

### 6.1 Skill 结构设计

```
.qoder/skills/llm-wiki/
├── SKILL.md                    # Skill 定义
├── knowledge/                  # 知识库（转换后的 Vault）
│   ├── commands/
│   ├── scenes/
│   └── faqs/
├── scripts/
│   └── convert.go              # YAML → Markdown 转换器
└── templates/
    ├── command.md.tmpl
    ├── scene.md.tmpl
    └── faq.md.tmpl
```

### 6.2 SKILL.md 示例

```markdown
# LLM-Wiki Skill

## 描述
基于 cmd4coder 构建的大模型领域知识库，支持多轮问答和场景化工具推荐。

## 使用方式

当用户询问大模型相关工具和命令时：

1. **理解场景**：判断用户处于哪个阶段（训练/推理/部署/应用）
2. **检索知识**：在 llm-wiki 中检索相关命令和场景
3. **构建链路**：按场景链路组织回答，引导用户完成目标
4. **提供命令**：给出具体可执行的命令和配置

## 知识库结构

- `commands/` — 693 个命令详情页
- `scenes/` — 50+ 典型场景页（多轮问答核心）
- `faqs/` — 200+ 问答对
- `concepts/` — 50+ 核心概念解释

## 多轮问答策略

```
用户问题 → 场景识别 → 工具推荐 → 具体命令 → 故障排查
              ↑___________|← 追问澄清
```
```

---

## 七、实施路线图

### Phase 1: 基础设施（1-2 天）
- [ ] 开发 YAML → Markdown 转换器
- [ ] 定义 frontmatter schema
- [ ] 生成 693 命令页
- [ ] 生成 58 分类 MOC 页

### Phase 2: 场景构建（2-3 天）
- [ ] 设计 30+ 核心场景页模板
- [ ] 填充场景内容（基于命令关联规则）
- [ ] 生成 FAQ 问答对
- [ ] 构建概念解释页

### Phase 3: 语料优化（1-2 天）
- [ ] Chunking 策略实现
- [ ] Embedding 生成
- [ ] 图谱索引构建
- [ ] 问答对质量评估

### Phase 4: Skill 集成（1 天）
- [ ] 创建 .qoder/skills/llm-wiki/
- [ ] 编写 SKILL.md
- [ ] 集成到 Agent 工作流
- [ ] 多轮问答测试

**总工期：5-8 天**

---

## 八、预期效果

### 改造前（YAML + CLI）
```
$ cmd4coder search "training"
→ 列出 27 个训练命令（平面列表）
```

### 改造后（Wiki + 智能体）
```
用户: "我想在单卡4090上微调7B模型"

Agent:
1. 识别场景：单卡 + 消费级GPU + 微调
2. 检索知识：[[单卡4090微调Llama-3-8B]] 场景页
3. 推荐链路：Unsloth → QLoRA → vLLM部署
4. 给出命令：具体安装、训练、部署命令
5. 预判问题："如果显存不够，可以试试..."
```

---

## 九、风险评估

| 风险 | 概率 | 影响 | 应对 |
|------|------|------|------|
| 转换脚本复杂度 | 中 | 中 | 分阶段迭代，先核心字段 |
| 场景页内容质量 | 高 | 高 | 规则生成 + 人工审核 |
| 双链维护成本 | 中 | 低 | 自动化脚本定期重建 |
| 数据同步 | 中 | 中 | YAML 为主源，单向转换 |

---

*方案设计完成。是否进入实施阶段？*

# cmd4coder 完整命令清单

**总命令数**: 1112  |  **大分类数**: 14

本清单按功能领域进行简单分类，每个分类下包含命令名称、风险等级和描述。
数据从 `data/*.yaml` 自动生成，与 CLI 和 Wiki 保持单一事实来源。

## AI 基础设施 (240)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `accelerate` | low | HuggingFace Accelerate分布式训练配置工具，简化多GPU/TPU训练 |
| 2 | `accelerate-config` | low | HuggingFace Accelerate配置向导，交互式生成分布式训练配置文件 |
| 3 | `agent-bench` | high | AgentBench多场景Agent能力评测，涵盖OS、数据库、知识图谱、数字卡牌、网页浏览 |
| 4 | `agno` | medium | Agno (原Phidata) 轻量级Agent框架，支持记忆、知识库、工具、多模态 |
| 5 | `aider` | high | Aider终端AI编程助手，多文件编辑、Git集成、支持GPT-4/Claude，自动提交更改 |
| 6 | `aim` | low | Aim开源超大规模实验跟踪工具，支持百万级实验，高性能查询 |
| 7 | `alpaca-eval` | low | 指令跟随能力评估工具，使用GPT-4作为裁判对模型输出进行排序 |
| 8 | `anthropic` | low | Anthropic Claude CLI |
| 9 | `anything-llm` | medium | 本地/私有化知识库与 LLM 对话平台 |
| 10 | `api-bench` | medium | APIBench API理解评测，测试LLM理解REST API文档并生成正确调用的能力 |
| 11 | `arena` | low | LMSYS Chatbot Arena众测平台，人类盲测对比不同LLM的对话质量 |
| 12 | `argilla` | low | Argilla数据标注与质量平台，专注于NLP和LLM数据，支持主动学习工作流 |
| 13 | `arize` | low | Arize AI ML可观测性平台，支持漂移检测、性能监控、根因分析 |
| 14 | `attention-rollout` | low | Attention Rollout跨层注意力传播追踪，识别输入token到输出token的完整注意力路径 |
| 15 | `auto-gptq` | medium | GPTQ后训练量化工具，4-bit量化减少75%显存占用，适合消费级GPU部署 |
| 16 | `autoawq` | medium | AWQ激活感知的权重量化，4-bit量化精度优于GPTQ，推理速度提升3倍 |
| 17 | `autogen` | high | Microsoft AutoGen多Agent对话框架，支持代码生成、工具调用、人机协同 |
| 18 | `axolotl` | medium | YAML配置式LLM微调工具，支持LoRA、QLoRA、全参数微调 |
| 19 | `bentoml` | medium | BentoML 命令行客户端，用于模型打包和服务 |
| 20 | `bertviz` | low | BertViz Transformer注意力可视化工具，交互式查看各层各头的注意力权重分布 |
| 21 | `big-bench` | low | BIG-bench (Beyond the Imitation Game) 大规模行为评测，200+语言理解任务 |
| 22 | `bitsandbytes` | medium | 8-bit/4-bit量化库，支持QLoRA在消费级GPU上训练大模型 |
| 23 | `calflops` | low | CalFlops模型参数量与FLOPs计算工具，精确统计前向/反向传播计算量 |
| 24 | `captum` | low | Captum PyTorch模型可解释性库，集成梯度、DeepLIFT、集成梯度、特征消融等多种归因方法 |
| 25 | `cerebras` | high | Cerebras Wafer-Scale Engine超大规模AI芯片训练平台，支持十亿到万亿参数模型 |
| 26 | `chainlit` | low | Chainlit对话式AI应用框架，专为LLM应用设计的Python框架 |
| 27 | `chroma` | low | Chroma轻量级开源向量数据库，专为AI应用设计，易嵌入到Python项目 |
| 28 | `cleanlab` | low | Cleanlab数据清洗与噪声检测，自动发现标注错误、异常样本和数据冲突 |
| 29 | `clearml` | medium | ClearML端到端MLOps平台，涵盖实验跟踪、数据管理、Pipeline编排、模型服务 |
| 30 | `clip` | low | OpenAI CLIP图文对齐模型，零样本图像分类、图文相似度计算、图像检索 |
| 31 | `codeium` | low | Codeium免费AI代码补全工具，个人版无限使用，支持70+语言和40+IDE |
| 32 | `cohere` | low | Cohere 命令行工具 |
| 33 | `colossal-ai` | medium | Colossal-AI统一深度学习加速系统，支持 Gemini、ZeRO、Pipeline 并行 |
| 34 | `comet` | low | Comet.ml 实验跟踪平台 |
| 35 | `comfyui` | medium | ComfyUI Stable Diffusion节点式可视化工作流，支持图像生成、视频生成、ControlNet |
| 36 | `composer` | low | MosaicML Composer高效训练库，内置100+算法和优化方法 |
| 37 | `continue-dev` | low | Continue.dev开源IDE AI编程助手，支持VS Code/JetBrains，本地/云端模型自由切换 |
| 38 | `coremltools` | low | Apple CoreML模型转换工具，将PyTorch/TensorFlow转换为iOS/macOS原生格式 |
| 39 | `cortex` | low | Cortex本地LLM平台，一键运行和管理多种开源模型 |
| 40 | `crewai` | medium | CrewAI多Agent协作框架，角色扮演、任务委派、团队协作执行复杂工作流 |
| 41 | `crypten` | medium | CrypTen Facebook隐私计算库，基于MPC(安全多方计算)的加密机器学习，支持加密推理和训练 |
| 42 | `ctranslate2` | low | CTranslate2高效推理引擎，支持INT8/INT16/FP16量化，CPU/GPU加速 |
| 43 | `datacompy` | low | 数据集对比工具，比较两个DataFrame的差异，适用于数据验证和回归测试 |
| 44 | `datasets-cli` | low | HuggingFace Datasets命令行工具，支持数据集下载、加载、转换和发布 |
| 45 | `deepspeed` | medium | 微软DeepSpeed大规模分布式训练框架，支持ZeRO优化、3D并行、Offload |
| 46 | `diffusers-cli` | low | HuggingFace Diffusers扩散模型工具，管理文生图/视频模型管线、调度器配置 |
| 47 | `dify` | medium | Dify开源LLM应用开发平台，可视化编排Agent、RAG、工作流，支持自托管 |
| 48 | `distilabel` | low | Distilabel合成数据生成与模型蒸馏框架，用LLM生成高质量训练数据，支持自对弈和批评 |
| 49 | `docling` | low | IBM Docling开源文档解析，支持PDF/HTML/图片/PPT，保留文档结构生成Markdown |
| 50 | `dpo` | medium | DPO (Direct Preference Optimization) 直接偏好优化，无需奖励模型直接从偏好数据微调 |
| 51 | `ds-1000` | high | DS-1000数据科学代码评测基准，1000个真实数据科学问题，测试pandas/numpy/sklearn等库使用 |
| 52 | `dspy` | low | DSPy声明式LLM编程框架，优化提示和权重而非手工工程 |
| 53 | `dvc` | medium | DVC数据版本控制，Git-like管理数据集和模型，支持S3/GS/Azure存储 |
| 54 | `einops` | low | Einops张量操作语义化库，清晰表达reshape、transpose、reduce等维度变换操作 |
| 55 | `elasticsearch` | low | Elasticsearch分布式搜索与分析，8.x版本原生支持dense_vector语义搜索 |
| 56 | `embedchain` | low | EmbedChain RAG框架，简化数据加载、分块、嵌入、查询全流程 |
| 57 | `evidently` | low | Evidently AI模型与数据漂移检测，支持表格数据、NLP、CV全链路监控 |
| 58 | `executorch` | low | ExecuTorch PyTorch移动端运行时，支持iOS/Android/嵌入式，端到端推理优化 |
| 59 | `faiss-cli` | low | Facebook AI Similarity Search (FaisS)高性能向量搜索库，支持GPU加速 |
| 60 | `faster-whisper` | low | Faster-Whisper CTranslate2加速版Whisper，4倍速度提升，更低内存占用 |
| 61 | `feast` | medium | Feast开源特征存储平台，统一管理ML特征的定义、存储和服务 |
| 62 | `fireworks` | low | Fireworks AI快速推理API，针对开源模型优化的高性能端点 |
| 63 | `flash-attn` | low | Flash Attention高效注意力实现，2-4倍加速长序列训练，显著降低内存占用 |
| 64 | `flower` | medium | Flower联邦学习框架，支持横向/纵向联邦、差分隐私、安全聚合，工业级跨设备联合训练 |
| 65 | `flowise` | medium | Flowise可视化LangChain工作流构建器，拖拽式创建LLM应用 |
| 66 | `flyte` | medium | 大规模机器学习与数据工作流平台 |
| 67 | `garak` | high | Garak LLM漏洞扫描框架，探测越狱、提示注入、数据泄露、幻觉等安全风险 |
| 68 | `gguf-convert` | low | GGUF格式转换工具，将HuggingFace模型转换为llama.cpp兼容格式 |
| 69 | `git-lfs` | medium | Git Large File Storage，管理大模型权重文件(GB级)的版本控制 |
| 70 | `gradio` | medium | Gradio快速构建ML模型交互式Demo，自动生成可分享的Web界面 |
| 71 | `great-expectations` | low | Great Expectations数据质量验证框架，定义和监控数据期望 |
| 72 | `groq` | low | Groq极速推理API，基于LPU芯片实现业界最快token生成速度 |
| 73 | `grpo` | medium | GRPO (Group Relative Policy Optimization) 强化学习训练，DeepSeek-R1核心训练方法，无需价值模型 |
| 74 | `guidance` | low | Guidance可控生成库，通过语法约束LLM输出结构，确保JSON/代码格式正确 |
| 75 | `haystack` | medium | Haystack端到端NLP框架，支持RAG、Agent、文档搜索、Pipeline编排 |
| 76 | `helicone` | low | Helicone LLM可观测性网关，一行代码接入，支持缓存、重试、成本追踪、A/B测试 |
| 77 | `huggingface-cli` | low | HuggingFace Hub命令行工具，支持模型/数据集/Space的上传下载管理 |
| 78 | `humaneval` | high | HumanEval代码生成评测基准，164个Python编程问题，测试函数级代码生成能力 |
| 79 | `humaneval-exec` | high | HumanEval代码评测执行器，运行模型生成的代码并通过单元测试，计算pass@k指标 |
| 80 | `img2dataset` | medium | 从URL列表批量下载图像并构建WebDataset格式，支持分布式处理 |
| 81 | `inspect-ai` | low | UK AISI Inspect AI评测框架，系统化评估模型知识、推理、安全性和能力 |
| 82 | `instructor` | low | Instructor结构化输出框架，基于Pydantic让LLM返回类型安全的结构化数据 |
| 83 | `iree-compile` | medium | Google IREE MLIR编译器，将深度学习模型编译为Vulkan/SPIR-V/Metal/WebGPU可执行代码 |
| 84 | `judge-eval` | low | LLM-as-Judge评估框架，系统化评估裁判模型质量，减少位置偏见和长度偏见 |
| 85 | `keywords-ai` | low | Keywords AI统一LLM API管理平台，支持多密钥管理、日志分析、用户追踪 |
| 86 | `kfp` | medium | Kubeflow Pipelines (KFP) 命令行客户端 |
| 87 | `kong-ai-gateway` | medium | Kong企业级AI网关，支持LLM路由、速率限制、语义缓存、令牌消耗控制 |
| 88 | `kserve` | medium | KServe Kubernetes原生模型服务平台，支持自动扩缩容、金丝雀发布、多框架运行时 |
| 89 | `label-studio` | low | Label Studio开源数据标注平台，支持图像、文本、音频、视频、时间序列等多模态标注 |
| 90 | `lancedb` | low | LanceDB无服务器向量数据库，基于Apache Arrow列式存储，支持嵌入和全文搜索 |
| 91 | `langchain` | medium | LangChain LLM应用开发框架，支持Chains、Agents、RAG、工具调用 |
| 92 | `langchain-hub` | low | LangChain Hub Prompt模板共享平台，复用社区验证的Prompt模板和链式组件 |
| 93 | `langfuse` | low | Langfuse开源LLM可观测性平台，支持自托管，追踪成本、延迟、质量指标 |
| 94 | `langgraph` | medium | LangGraph状态机Agent框架，支持循环、条件分支、持久化、人机协同 |
| 95 | `langsmith` | low | LangSmith LLM应用全链路追踪与评估平台，记录输入输出、token消耗、延迟 |
| 96 | `langtrace` | low | Langtrace开源LLM应用追踪，兼容OpenTelemetry，支持多框架 |
| 97 | `lightning` | low | PyTorch Lightning高级训练框架，简化分布式训练、混合精度、Checkpoint管理 |
| 98 | `lime` | low | LIME (Local Interpretable Model-agnostic Explanations) 局部代理模型解释，扰动样本训练可解释模型 |
| 99 | `litellm` | medium | 统一多 LLM API 的网关/代理 |
| 100 | `litellm-proxy` | medium | LiteLLM代理网关，统一管理100+ LLM API，支持负载均衡、速率限制、成本追踪 |
| 101 | `livecodebench` | high | LiveCodeBench实时代码评测，持续更新的编程题 benchmark，防数据污染，反映模型真实代码能力 |
| 102 | `llama-factory` | low | LLaMA-Factory一站式大模型微调框架，支持100+模型，预训练/微调/DPO/RLHF全流程 |
| 103 | `llama-index` | medium | LlamaIndex数据框架，连接LLM与私有数据，支持RAG、Agent、工作流 |
| 104 | `llama.cpp` | low | llama.cpp纯C/C++实现的LLM推理，支持GGUF量化，可在CPU/边缘设备运行 |
| 105 | `llamaparse` | low | LlamaParse LlamaIndex高级PDF解析服务，GenAI原生解析，支持表格、图表、数学公式 |
| 106 | `llava` | low | LLaVA大语言视觉助手，视觉指令微调，支持图像问答、描述、推理 |
| 107 | `llm-as-judge` | low | LLM-as-Judge方法论实现，位置偏见校正、一致性检验、多维度评分 |
| 108 | `llm-factory` | medium | 一站式LLM训练平台，支持100+模型预训练、微调、RLHF、DPO、量化、推理 |
| 109 | `llm-guard` | low | LLM Guard输入输出安全过滤器，检测PII泄露、毒性、越狱、提示注入 |
| 110 | `lm-eval` | low | EleutherAI语言模型评估框架，支持HellaSwag、MMLU、ARC等100+基准测试 |
| 111 | `lmdeploy` | medium | 上海AI Lab开源的大模型部署工具，支持TurboMind引擎和PyTorch引擎 |
| 112 | `long-context-eval` | low | 长上下文评测工具，Needle-in-Haystack、RULER等，测试模型在超长文本中的信息检索能力 |
| 113 | `mamba` | low | Mamba状态空间模型(SSM)实现，线性复杂度序列建模，替代Transformer注意力机制 |
| 114 | `marimo` | low | Marimo响应式Python Notebook，支持交互式数据探索和模型实验 |
| 115 | `marker` | low | Marker高性能PDF转Markdown工具，基于布局模型，准确提取表格、公式、代码块 |
| 116 | `marqo` | low | Marqo端到端向量搜索引擎，内置向量化，零配置语义搜索 |
| 117 | `math-eval` | low | 数学能力评测工具，支持GSM8K、MATH、SVAMP等数据集，验证模型推理和计算准确性 |
| 118 | `mbpp` | high | MBPP (Mostly Basic Python Programming) 代码生成评测，974个Python编程任务 |
| 119 | `mcp` | medium | Model Context Protocol CLI/服务器 |
| 120 | `mediapipe` | low | Google MediaPipe端侧ML流水线，支持人脸检测、姿态估计、手势识别、文本分类 |
| 121 | `megatron-lm` | high | NVIDIA Megatron-LM大规模语言模型训练框架，支持张量/流水线/序列并行 |
| 122 | `meilisearch` | low | 开源即时搜索引擎，支持容错搜索和中文分词 |
| 123 | `mergekit` | low | MergeKit模型合并工具，支持SLERP、TIES、DARE、Model Stock等多种合并算法，无需GPU |
| 124 | `metaflow` | medium | Netflix 机器学习工作流框架 |
| 125 | `milvus-cli` | medium | Milvus分布式向量数据库CLI，支持十亿级向量的高性能ANN搜索 |
| 126 | `mistral` | low | Mistral AI CLI |
| 127 | `mlc-llm` | low | MLC LLM全平台大模型部署，支持手机/浏览器/边缘设备/云端 |
| 128 | `mlflow` | medium | MLflow 命令行客户端，用于模型全生命周期管理 |
| 129 | `mlflow-tracking` | low | MLflow Tracking模块，本地实验跟踪与模型注册 |
| 130 | `mlir-opt` | low | MLIR中间表示优化器，对计算图进行 lowering、融合、循环变换等编译优化 |
| 131 | `modal` | medium | Modal Serverless云平台，按需弹性运行AI训练与推理任务 |
| 132 | `model-card` | low | 模型卡片(model card)编写规范，记录模型用途、限制、训练数据等元信息 |
| 133 | `model-pruner` | high | 模型剪枝工具，移除不重要的权重或神经元，减小模型体积加速推理 |
| 134 | `modelcards` | low | HuggingFace Model Card工具，生成和管理模型文档，确保模型可追溯和合规 |
| 135 | `modelscan` | low | ProtectAI ModelScan模型文件安全扫描，检测Pickle反序列化漏洞、恶意代码注入 |
| 136 | `modelscope` | low | 魔搭社区ModelScope命令行工具，国产开源模型仓库管理 |
| 137 | `mosaicml-streaming` | low | MosaicML Streaming高效数据集流式加载，支持多种云存储和Sharding |
| 138 | `mt-bench` | low | MT-Bench多轮对话评测基准，80个高质量多轮问题，GPT-4作为裁判评分 |
| 139 | `multilingual-eval` | low | 多语言能力评测，支持C-Eval(中文)、MMLU多语言、XCOPA、XNLI等跨语言基准 |
| 140 | `n8n` | medium | n8n开源AI工作流自动化平台，低代码编排LLM、数据库、API、通知等节点 |
| 141 | `neo4j-llm` | medium | Neo4j图数据库+LLM知识图谱构建工具，从非结构化文本自动抽取实体关系构建图谱 |
| 142 | `neptune` | low | Neptune ML实验管理平台，支持指标跟踪、模型版本、数据集版本管理 |
| 143 | `neuralsecure` | medium | NeuralSecure ML模型安全审计，检测对抗样本脆弱性、成员推断攻击、模型窃取风险 |
| 144 | `neuronx-cc` | medium | AWS Neuron编译器，将PyTorch/TensorFlow模型编译为Trainium/Inferentia高效执行格式 |
| 145 | `neuronx-nxdt` | medium | AWS Neuron分布式训练工具，针对Trainium芯片优化的LLM训练 |
| 146 | `ollama` | low | Ollama本地大模型运行管理工具，一键下载和运行各类开源模型 |
| 147 | `onnx-optimizer` | low | ONNX模型图优化器，常量折叠、算子融合、死代码消除，跨平台推理前必备优化 |
| 148 | `onnxruntime` | low | ONNX Runtime跨平台推理加速引擎，支持CPU/GPU/边缘设备 |
| 149 | `opacus` | medium | Opacus PyTorch差分隐私训练库，通过梯度裁剪和噪声注入实现(ε,δ)-差分隐私保证 |
| 150 | `open-webui` | medium | 本地大模型 Web 聊天界面 |
| 151 | `openai` | low | OpenAI 官方 CLI |
| 152 | `openai-agents` | medium | OpenAI官方Agents SDK，支持Responses API、工具调用、网络搜索、文件搜索 |
| 153 | `openai-function-calling` | medium | OpenAI Function Calling工具调用，让LLM自主决定调用外部API获取实时数据或执行操作 |
| 154 | `opencompass` | low | 上海AI Lab开源的模型评测平台，支持50+数据集和多种评测范式 |
| 155 | `openhands` | critical | OpenHands (原OpenDevin) 开源AI软件工程师，自主完成开发任务，支持多Agent协作 |
| 156 | `openrouter` | low | OpenRouter统一访问100+开源和商用模型API，标准化接口、自动竞价 |
| 157 | `opensearch` | low | OpenSearch分布式搜索与分析引擎，支持k-NN向量搜索、ML推理插件 |
| 158 | `openvino` | low | Intel OpenVINO工具包，针对Intel CPU/GPU/NPU优化的推理框架 |
| 159 | `opik` | low | Comet Opik开源LLM评估与追踪平台，支持RAG评估、提示工程、实验管理 |
| 160 | `optimum-cli` | medium | HuggingFace Optimum模型优化工具，支持ONNX/TensorRT/OpenVINO导出和量化 |
| 161 | `outlines` | low | LLM结构化生成库，强制模型输出JSON/Regex格式 |
| 162 | `paddle-lite` | low | Paddle Lite百度端侧推理框架，支持ARM Cortex-M到服务器GPU，极致轻量 |
| 163 | `paddle2onnx` | low | PaddlePaddle到ONNX转换工具，支持Paddle模型导出为ONNX格式 |
| 164 | `pair-wise-eval` | low | Pair-wise成对比较评测，ELO评分系统，适用于模型A/B测试和排序 |
| 165 | `peft` | low | 参数高效微调库，支持LoRA、QLoRA、IA3、Prompt Tuning等方法 |
| 166 | `perplexity` | low | Perplexity API CLI |
| 167 | `pgvector` | medium | pgvector PostgreSQL向量扩展，在关系数据库中直接存储和查询向量 |
| 168 | `phidata` | low | Phidata构建AI助手的框架，支持知识库、结构化输出、多模态(已合并为Agno) |
| 169 | `phoenix` | low | Arize Phoenix开源LLM可观测性和评估工具，支持追踪、评估、数据集管理 |
| 170 | `pinecone` | low | Pinecone全托管向量数据库，零运维，自动扩缩容 |
| 171 | `portkey` | low | Portkey AI网关，支持语义缓存、智能重试、负载均衡、多模型Fallback |
| 172 | `praisonai` | medium | PraisonAI低代码多Agent框架，基于CrewAI，支持AutoGen集成和UI界面 |
| 173 | `prefix-caching` | low | Prefix Caching前缀缓存，复用共享系统Prompt的KV Cache，大幅降低多轮推理延迟和显存 |
| 174 | `prometheus-eval` | low | Prometheus开源LLM评估模型，无需GPT-4即可进行高质量指令评测 |
| 175 | `promptflow` | low | 微软PromptFlow Prompt工程与LLM应用开发框架，可视化编排、评估、部署一体化 |
| 176 | `promptfoo` | low | Promptfoo Prompt测试与回归框架，CI/CD集成，防止Prompt退化 |
| 177 | `promptlayer` | low | PromptLayer提示词版本管理与追踪，记录提示词迭代历史和效果对比 |
| 178 | `pulsar` | medium | Apache Pulsar分布式消息流平台，用于AI流水线事件驱动和数据流处理 |
| 179 | `pydantic-ai` | low | PydanticAI类型安全Agent框架，Samuel Colvin(Pydantic作者)出品，强类型验证 |
| 180 | `pymupdf` | low | PyMuPDF高性能PDF处理库，提取文本/图像/注释，支持PDF编辑和转换 |
| 181 | `pytorch-lightning` | low | PyTorch Lightning高级训练框架，简化分布式训练、混合精度、Checkpoint管理 |
| 182 | `pyvertical` | high | PyVertical垂直联邦学习框架，特征分片联合建模，适用于银行+电商等跨机构数据互补场景 |
| 183 | `qdrant` | low | Qdrant高性能开源向量数据库，支持过滤搜索、分布式部署、Rust实现 |
| 184 | `ray-serve` | medium | Ray Serve可扩展模型服务框架，支持多模型组合、A/B测试、自动扩缩容 |
| 185 | `red-teaming` | high | PyRIT (Python Risk Identification Toolkit) 微软开源红队测试框架，自动化LLM安全测试 |
| 186 | `redisearch` | low | RediSearch Redis向量搜索模块，支持向量相似性搜索+全文搜索混合查询 |
| 187 | `replicate` | low | Replicate模型托管云平台，一键部署和运行开源模型 |
| 188 | `runpod` | medium | RunPod GPU云平台，按需租用GPU进行AI训练和推理 |
| 189 | `safetensors-convert` | low | Safetensors安全模型格式转换工具，替代pickle防止恶意代码执行 |
| 190 | `safety-eval` | low | MLSafety模型安全评测套件，覆盖毒性、偏见、隐私泄露、越狱抗性 |
| 191 | `semantic-kernel` | medium | Microsoft Semantic Kernel SDK，连接LLM、记忆、规划器和插件 |
| 192 | `sglang` | medium | SGLang结构化生成语言模型服务，支持RadixAttention缓存、多模态推理 |
| 193 | `shap` | low | SHAP (SHapley Additive exPlanations) 博弈论特征归因，精确量化每个特征对预测的贡献 |
| 194 | `sky-pilot` | medium | SkyPilot云端ML任务调度器，一键在AWS/GCP/Azure/Lambda运行训练/推理 |
| 195 | `smolagents` | high | HuggingFace SmolAgents极简Agent库，代码优先，最小抽象，高度透明 |
| 196 | `snorkel` | medium | Snorkel弱监督标注框架，通过编程方式生成训练标签，减少人工标注成本 |
| 197 | `speculative-decoding` | low | 推测解码(Speculative Decoding)加速推理，用小草稿模型预测大目标模型输出，2-3倍加速 |
| 198 | `stable-diffusion-cli` | medium | Stable Diffusion文本到图像生成命令行工具，支持多种模型和LoRA |
| 199 | `streamlit` | low | Streamlit数据应用与模型展示框架，纯Python构建数据科学应用 |
| 200 | `swe-agent` | critical | SWE-Agent自动修复GitHub Issue，分析Issue、编辑代码、运行测试验证修复 |
| 201 | `swe-bench` | medium | SWE-bench软件工程评测基准，测试LLM解决真实GitHub Issue的能力 |
| 202 | `sweep` | high | AI 驱动的代码 issue 自动修复助手 |
| 203 | `tensor-parallel` | medium | Tensor Parallel通用张量并行推理库，支持任意HuggingFace模型多卡推理 |
| 204 | `tensorboard` | low | TensorFlow和PyTorch的训练可视化工具 |
| 205 | `tensorboard-profiler` | low | TensorBoard Profiler性能分析插件，分析模型训练中的CPU/GPU瓶颈 |
| 206 | `tensorrt-llm` | medium | NVIDIA TensorRT-LLM推理优化库，针对NVIDIA GPU极致优化 |
| 207 | `text-generation-inference` | medium | HuggingFace TGI文本生成推理服务，生产级部署方案 |
| 208 | `text2sql` | high | Text2SQL自然语言转SQL工具，基于LLM将业务问题转换为可执行的数据库查询 |
| 209 | `tf2onnx` | low | TensorFlow到ONNX转换工具，支持SavedModel、Checkpoint、Keras模型 |
| 210 | `tflite` | low | TensorFlow Lite移动端和嵌入式推理框架，支持Android/iOS/ARM/Raspberry Pi |
| 211 | `timm` | low | PyTorch Image Models库，800+预训练视觉模型，涵盖ViT、ConvNeXt、Swin Transformer等 |
| 212 | `together` | low | Together AI API客户端，访问高性能开源模型推理API |
| 213 | `token-heatmap` | low | Token级别归因热图，可视化每个输入token对模型输出的贡献度，定位幻觉和错误关注 |
| 214 | `tool-bench` | medium | ToolBench工具使用评测基准，16000+ API，测试LLM的工具选择、调用、组合能力 |
| 215 | `torch-titan` | medium | PyTorch官方原生大模型训练参考实现，支持FSDP2、TP、PP、CP |
| 216 | `torchrun` | low | PyTorch分布式训练启动器 |
| 217 | `torchserve` | medium | PyTorch官方模型服务框架，支持模型打包、A/B测试、多模型服务、自定义处理器 |
| 218 | `transformers-cli` | low | HuggingFace Transformers命令行工具，查看模型配置、下载模型、转换格式 |
| 219 | `transformers-pipeline` | low | HuggingFace Transformers Pipeline快速推理接口，一行代码完成文本生成/分类/问答 |
| 220 | `tritonserver` | medium | NVIDIA Triton推理服务器，支持TensorRT、ONNX、PyTorch、Python后端，多模型并行服务 |
| 221 | `trl` | medium | Transformers Reinforcement Learning，支持SFT、DPO、PPO、ORPO训练 |
| 222 | `trtexec` | medium | TensorRT引擎构建与性能测试工具，将ONNX/UFF转为TensorRT序列化引擎，极致NVIDIA GPU优化 |
| 223 | `turbopuffer` | low | Turbopuffer高性能托管向量搜索，专为RAG应用优化，支持混合搜索 |
| 224 | `tvmc` | medium | TVM命令行编译器，将模型编译为高性能机器码，支持ARM/x86/GPU/FPGA多种后端 |
| 225 | `typesense` | low | Typesense开源搜索引擎，支持向量搜索、拼写容错、分面过滤、地理搜索 |
| 226 | `unsloth` | low | 2-5倍加速的LLM微调框架，支持LoRA和QLoRA，内存占用减少80% |
| 227 | `unstructured` | low | Unstructured通用文档解析库，支持PDF/Word/PPT/HTML/图片等50+格式提取文本 |
| 228 | `vanna` | high | Vanna AI SQL生成框架，RAG增强的Text2SQL，支持训练领域Schema并持续优化 |
| 229 | `vespa-cli` | medium | Vespa大规模搜索与推理引擎，支持向量搜索+结构化搜索+机器学习推理 |
| 230 | `vllm` | medium | vLLM高性能大模型推理引擎，采用PagedAttention实现最高24倍吞吐提升 |
| 231 | `wandb` | low | Weights & Biases实验跟踪平台，记录指标、超参数、模型版本、数据集血缘 |
| 232 | `weave` | low | Weights & Biases Weave 可观测工具 |
| 233 | `weaviate-cli` | low | Weaviate AI原生向量数据库，内置向量化和模块化扩展(GraphQL接口) |
| 234 | `webdataset` | low | WebDataset大规模数据集流式处理库，高效处理TB级训练数据 |
| 235 | `weights-biases-sweep` | medium | W&B超参数搜索(Sweep)，支持网格搜索、随机搜索、贝叶斯优化 |
| 236 | `whisper` | low | OpenAI Whisper通用语音识别模型，支持99种语言，多尺寸模型(tiny~large-v3) |
| 237 | `whylogs` | low | WhyLogs数据日志分析，轻量级数据画像和漂移检测 |
| 238 | `xformers` | low | Meta开源的高效Transformer组件库，提供memory_efficient_attention等优化算子 |
| 239 | `xla_compile` | low | TensorFlow XLA(Accelerated Linear Algebra)即时编译，将计算图编译为机器码，TPU训练推理加速 |
| 240 | `zenml` | medium | MLOps 管道编排工具 |

## 大数据 (54)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `airbyte` | medium | Airbyte 数据集成平台 CLI |
| 2 | `airflow` | medium | Apache Airflow 工作流调度命令 |
| 3 | `atlas-admin` | medium | Apache Atlas 元数据管理命令 |
| 4 | `beeline` | low | HiveServer2 JDBC 客户端 |
| 5 | `dbt` | medium | 数据转换工具，支持 SQL 模型版本化与测试 |
| 6 | `debezium` | high | CDC（变更数据捕获）工具，常通过 Kafka Connect 部署 |
| 7 | `delta` | high | Delta Lake 表格式命令入口（通常通过 Spark 或 delta-rs 使用） |
| 8 | `dremio-admin` | high | Dremio 数据湖引擎管理工具 |
| 9 | `flink` | medium | Flink 作业提交与管理 CLI |
| 10 | `flume-ng` | medium | Apache Flume 分布式日志采集命令 |
| 11 | `hadoop` | high | Hadoop 通用命令入口，可调用 fs、jar、dfsadmin 等子命令 |
| 12 | `hbase hbck` | high | HBase 一致性检查与修复 |
| 13 | `hbase shell` | high | HBase 交互式 Shell |
| 14 | `hdfs` | high | Hadoop 分布式文件系统（HDFS）管理命令 |
| 15 | `hive` | medium | Apache Hive 命令行接口 |
| 16 | `hudi-cli` | high | Apache Hudi 表管理命令行工具 |
| 17 | `iceberg` | medium | Apache Iceberg 表格式命令 |
| 18 | `impala-shell` | medium | Impala 交互式 SQL Shell |
| 19 | `kafka` | low | Apache Kafka分布式消息队列 |
| 20 | `kafka-acls.sh` | high | Kafka ACL 权限管理 |
| 21 | `kafka-configs.sh` | high | Kafka 配置管理工具 |
| 22 | `kafka-connect` | medium | Kafka Connect 连接器管理 CLI |
| 23 | `kafka-console-consumer` | low | Kafka 命令行消费者 |
| 24 | `kafka-console-producer` | low | Kafka 命令行生产者 |
| 25 | `kafka-consumer-groups.sh` | high | Kafka 消费者组管理 |
| 26 | `kafka-consumer-perf-test` | medium | Kafka 消费者性能测试 |
| 27 | `kafka-mirror-maker` | high | Kafka 跨集群镜像复制工具 |
| 28 | `kafka-producer-perf-test` | high | Kafka 生产者性能测试 |
| 29 | `kafka-reassign-partitions.sh` | high | Kafka 分区重分配工具 |
| 30 | `kafka-topics.sh` | medium | Kafka Topic 创建、查看与管理 |
| 31 | `ksql` | medium | ksqlDB 交互式 SQL 引擎 CLI |
| 32 | `livy-submit` | medium | 通过 Livy 提交 Spark 作业到集群 |
| 33 | `logstash` | medium | 日志收集与转换管道 |
| 34 | `mapred` | medium | Hadoop MapReduce 管理命令 |
| 35 | `meltano` | medium | ELT 数据管道与 dbt 编排工具 |
| 36 | `metabase` | medium | 开源 BI 与数据探索平台 |
| 37 | `nifi` | medium | Apache NiFi 数据流 CLI |
| 38 | `nifi-toolkit` | high | Apache NiFi 命令行工具包 |
| 39 | `oozie` | medium | Apache Oozie 工作流调度 |
| 40 | `pig` | medium | Apache Pig 大数据分析平台 |
| 41 | `presto` | medium | Presto 分布式 SQL 查询引擎 CLI |
| 42 | `pyspark` | low | Spark 交互式 Python Shell |
| 43 | `rabbitmqctl` | medium | RabbitMQ 消息队列管理 CLI |
| 44 | `spark-shell` | low | Spark 交互式 Scala REPL |
| 45 | `spark-sql` | medium | Spark SQL 交互式命令行 |
| 46 | `spark-submit` | medium | 提交 Spark 应用程序到集群 |
| 47 | `sql-client.sh` | medium | Flink SQL 交互式客户端 |
| 48 | `sqoop` | high | Hadoop 与关系型数据库之间的数据传输工具 |
| 49 | `superset` | medium | Apache Superset 数据可视化平台 |
| 50 | `trino` | medium | Trino 分布式 SQL 查询引擎 CLI |
| 51 | `yarn` | medium | Hadoop 资源调度与作业监控命令 |
| 52 | `zeppelin` | medium | Apache Zeppelin 交互式数据分析笔记本 |
| 53 | `zkCli.sh` | medium | ZooKeeper 命令行客户端 |
| 54 | `zookeeper-shell` | medium | ZooKeeper 命令行客户端 |

## 构建工具 (10)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `cmake` | low | 跨平台构建系统生成器，管理 C/C++ 项目构建 |
| 2 | `gradle` | medium | Gradle 项目自动化构建工具，基于 Groovy/Kotlin DSL |
| 3 | `gradle init` | medium | Gradle Wrapper 初始化，生成 gradlew 脚本 |
| 4 | `gradlew` | medium | Gradle Wrapper 脚本，确保使用项目指定的 Gradle 版本 |
| 5 | `make` | medium | GNU Make 构建自动化工具，通过 Makefile 定义构建规则 |
| 6 | `make install` | high | 安装已编译的程序到系统目录（通常为 /usr/local） |
| 7 | `mvn` | high | Apache Maven 项目管理工具，用于构建和管理 Java 项目 |
| 8 | `mvn archetype` | low | Maven 项目原型生成工具 |
| 9 | `mvn clean` | high | 清理构建输出目录(target) |
| 10 | `mvn dependency` | low | Maven 依赖管理子命令 |

## CI/CD (9)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `act` | medium | 本地运行 GitHub Actions 工作流（无需推送到 GitHub） |
| 2 | `circleci` | low | CircleCI CLI |
| 3 | `gh` | low | GitHub 官方 CLI |
| 4 | `gh action` | low | 管理 GitHub Actions |
| 5 | `gh run` | medium | 查看和管理 GitHub Actions 运行记录 |
| 6 | `gh run cancel` | medium | 取消正在运行的 GitHub Actions 工作流 |
| 7 | `gh workflow` | low | 管理 GitHub Actions 工作流 |
| 8 | `gitlab-runner` | medium | GitLab CI 运行器 |
| 9 | `jenkins-cli` | medium | Jenkins 命令行管理工具 |

## 云平台 (13)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `aws` | high | AWS 命令行接口，管理 AWS 服务和资源 |
| 2 | `aws cloudformation` | high | CloudFormation 基础设施即代码管理 |
| 3 | `aws configure` | high | 配置 AWS CLI 凭证和默认设置 |
| 4 | `aws eks` | low | EKS Kubernetes 集群管理 |
| 5 | `aws s3` | high | S3 存储桶和对象管理 |
| 6 | `aws sts` | low | AWS Security Token Service，管理临时凭证 |
| 7 | `aws-vault` | low | AWS 凭据安全存储与切换工具 |
| 8 | `az` | medium | Azure 官方 CLI |
| 9 | `doctl` | medium | DigitalOcean 官方 CLI |
| 10 | `gcloud` | medium | Google Cloud 官方 CLI |
| 11 | `linode-cli` | medium | Linode 官方 CLI |
| 12 | `pulumi` | high | 使用通用编程语言（TypeScript/Python/Go 等）定义和部署云资源 |
| 13 | `terraform` | low | 基础设施即代码工具，管理云资源 |

## 容器编排 (338)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `alertmanager` | medium | Start Prometheus Alertmanager |
| 2 | `amtool alert query` | low | Query active alerts from Alertmanager |
| 3 | `amtool check-config` | low | Validate Alertmanager configuration |
| 4 | `amtool silence add` | medium | Add silence to Alertmanager |
| 5 | `ansible` | medium | Execute ad-hoc commands on hosts |
| 6 | `ansible all -m ping` | low | Test connectivity to all hosts in inventory |
| 7 | `ansible-config dump` | low | Show Ansible configuration |
| 8 | `ansible-console` | medium | Interactive Ansible console |
| 9 | `ansible-doc` | low | Display Ansible module documentation |
| 10 | `ansible-galaxy install` | low | Install Ansible roles from Galaxy or Git |
| 11 | `ansible-inventory --list` | low | Display Ansible inventory information |
| 12 | `ansible-playbook` | high | Execute Ansible playbook |
| 13 | `ansible-pull` | high | Pull and execute Ansible playbooks from VCS |
| 14 | `ansible-vault decrypt` | high | Decrypt Ansible vault files |
| 15 | `ansible-vault encrypt` | medium | Encrypt Ansible files with vault |
| 16 | `argo-rollouts` | high | Argo Rollouts 渐进式交付 CLI |
| 17 | `argocd app create` | high | Create ArgoCD application |
| 18 | `argocd app delete` | critical | Delete ArgoCD application |
| 19 | `argocd app list` | low | List ArgoCD applications |
| 20 | `argocd app sync` | high | Sync application state with Git repository |
| 21 | `argocd login` | low | Login to ArgoCD server |
| 22 | `atlantis` | high | Terraform 自动化 PR 工作流工具 |
| 23 | `az aks create` | critical | Create Azure AKS Kubernetes cluster |
| 24 | `az aks delete` | critical | Delete Azure AKS cluster |
| 25 | `az aks list` | low | List Azure AKS clusters |
| 26 | `backstage` | low | Backstage 开发者门户 CLI |
| 27 | `buildah` | low | 构建 OCI 容器镜像，无需完整容器运行时 |
| 28 | `buildkit` | medium | Docker/Moby 下一代镜像构建工具包 |
| 29 | `calicoctl apply` | high | Apply Calico network policy configuration |
| 30 | `calicoctl delete networkpolicy` | critical | Delete Calico network policy |
| 31 | `calicoctl get networkpolicies` | low | List Calico network policies |
| 32 | `calicoctl get nodes` | low | List all Calico nodes |
| 33 | `cert-manager` | medium | Kubernetes 证书自动化管理（cmctl） |
| 34 | `certbot` | medium | Let's Encrypt 证书自动申请工具 |
| 35 | `checkov` | low | 基础设施即代码静态安全分析工具 |
| 36 | `cilium connectivity test` | medium | Run connectivity test between pods |
| 37 | `cilium hubble status` | low | Check Hubble observability status |
| 38 | `cilium status` | low | Check Cilium agent status |
| 39 | `clusterctl` | high | Cluster API 集群生命周期管理 |
| 40 | `consul` | medium | HashiCorp Consul 服务网格与发现 |
| 41 | `containerd` | medium | 容器运行时 daemon |
| 42 | `cosign` | medium | 容器镜像签名与验证工具 |
| 43 | `crictl` | medium | 兼容 CRI 的容器运行时 CLI |
| 44 | `crictl exec` | high | Execute command in running container |
| 45 | `crictl images` | low | List container images |
| 46 | `crictl logs` | low | Fetch logs of a container |
| 47 | `crictl pods` | low | List all pods |
| 48 | `crictl ps` | low | List running containers |
| 49 | `crictl stats` | low | Display container resource usage statistics |
| 50 | `crossplane` | medium | Kubernetes 多云控制平面 CLI |
| 51 | `ctr` | medium | containerd 官方 CLI |
| 52 | `ctr containers list` | low | List containers in containerd |
| 53 | `ctr images list` | low | List images in containerd |
| 54 | `dapr` | medium | 分布式应用运行时 CLI |
| 55 | `devspace` | medium | Kubernetes 本地开发工作流 |
| 56 | `docker attach` | low | 附加到正在运行的容器 |
| 57 | `docker build` | medium | 从Dockerfile构建镜像 |
| 58 | `docker buildx` | medium | Docker 高级镜像构建插件 |
| 59 | `docker context` | low | Docker 上下文管理 |
| 60 | `docker exec` | medium | 在运行中的容器内执行命令 |
| 61 | `docker images` | low | 列出本地镜像 |
| 62 | `docker inspect` | low | 获取容器或镜像的底层信息 |
| 63 | `docker logs` | low | 查看容器日志 |
| 64 | `docker network` | low | Docker 网络管理 |
| 65 | `docker ps` | low | 列出运行中的容器 |
| 66 | `docker pull` | low | 从镜像仓库拉取镜像 |
| 67 | `docker push` | low | 将本地镜像推送到镜像仓库 |
| 68 | `docker restart` | medium | 重启一个或多个容器 |
| 69 | `docker rm` | medium | 删除容器 |
| 70 | `docker rmi` | high | 删除本地镜像 |
| 71 | `docker run` | medium | 运行一个新容器 |
| 72 | `docker start` | medium | 启动一个或多个已停止的容器 |
| 73 | `docker stop` | medium | 停止运行中的容器 |
| 74 | `docker system` | high | Docker 系统级维护命令 |
| 75 | `docker volume` | high | Docker 卷管理 |
| 76 | `docker-compose` | low | 管理多容器应用 |
| 77 | `eksctl create cluster` | critical | Create AWS EKS Kubernetes cluster |
| 78 | `eksctl delete cluster` | critical | Delete AWS EKS cluster |
| 79 | `eksctl get cluster` | low | List AWS EKS clusters |
| 80 | `envoy` | medium | 云原生高性能代理 |
| 81 | `esoctl` | medium | External Secrets Operator 工具（kubectl 插件） |
| 82 | `etcdctl get` | low | Get value of specified key from etcd |
| 83 | `etcdctl member list` | low | List all etcd cluster members |
| 84 | `etcdctl snapshot restore` | critical | Restore etcd cluster from backup snapshot |
| 85 | `etcdctl snapshot save` | medium | Create backup snapshot of etcd data |
| 86 | `external-dns` | high | Kubernetes DNS 记录自动同步 |
| 87 | `falco` | low | Start Falco runtime security monitoring |
| 88 | `firecracker` | medium | AWS 开源微虚拟机（microVM） |
| 89 | `flagger` | high | Flagger 渐进式交付控制器 |
| 90 | `fluent-bit -c` | medium | Start Fluent Bit with configuration file |
| 91 | `fluentd -c` | medium | Start Fluentd with configuration file |
| 92 | `flux bootstrap git` | high | Bootstrap Flux to Git repository |
| 93 | `flux get kustomizations` | low | List Flux Kustomization resources |
| 94 | `flux reconcile source git` | medium | Manually trigger Git source reconciliation |
| 95 | `gcloud container clusters create` | critical | Create Google GKE Kubernetes cluster |
| 96 | `gcloud container clusters delete` | critical | Delete Google GKE cluster |
| 97 | `gcloud container clusters list` | low | List Google GKE clusters |
| 98 | `grafana-cli admin reset-admin-password` | high | Reset Grafana admin password |
| 99 | `grafana-cli plugins install` | medium | Install Grafana plugin |
| 100 | `grafana-cli plugins list-remote` | low | List available Grafana plugins |
| 101 | `grafana-cli plugins update` | medium | Update Grafana plugin |
| 102 | `grafana-server` | medium | Start Grafana visualization server |
| 103 | `grype` | low | 容器镜像与文件系统漏洞扫描器 |
| 104 | `helm create` | low | Create new Helm chart |
| 105 | `helm dependency` | low | Manage chart dependencies |
| 106 | `helm env` | low | Display Helm environment information |
| 107 | `helm history` | low | View release history |
| 108 | `helm install` | high | Install Helm chart to Kubernetes cluster |
| 109 | `helm lint` | low | Lint chart for best practices and errors |
| 110 | `helm list` | low | List Helm releases |
| 111 | `helm package` | low | Package chart into versioned archive |
| 112 | `helm plugin list` | low | List installed Helm plugins |
| 113 | `helm repo add` | low | Add Helm chart repository |
| 114 | `helm repo remove` | low | Remove Helm chart repository |
| 115 | `helm repo update` | low | Update local Helm chart repository cache |
| 116 | `helm rollback` | high | Rollback Helm release to previous version |
| 117 | `helm search repo` | low | Search for charts in repositories |
| 118 | `helm status` | low | Display status of Helm release |
| 119 | `helm template` | low | Render chart templates locally |
| 120 | `helm uninstall` | critical | Uninstall Helm release from cluster |
| 121 | `helm upgrade` | high | Upgrade Helm release to new version |
| 122 | `helm version` | low | Display Helm client and server version |
| 123 | `helmfile` | high | Helm Chart 的声明式批量部署工具 |
| 124 | `hubble` | low | Cilium 可观测性 CLI |
| 125 | `img` | medium | 由 buildkit 支持的无 daemon 镜像构建工具 |
| 126 | `incus` | medium | LXD 社区分支（Canonical 替代方案） |
| 127 | `infracost` | low | 云基础设施成本估算工具 |
| 128 | `istioctl analyze` | low | Analyze Istio configuration for potential issues |
| 129 | `istioctl proxy-config` | low | Inspect Envoy proxy configuration |
| 130 | `istioctl proxy-status` | low | Check Envoy proxy status in service mesh |
| 131 | `istioctl version` | low | Check Istio service mesh version |
| 132 | `jaeger-cli` | low | Jaeger 分布式追踪 CLI |
| 133 | `journalctl -u kubelet` | low | View kubelet service logs |
| 134 | `k0s` | medium | 零依赖单二进制 Kubernetes 发行版 |
| 135 | `k3d` | medium | 在 Docker 中运行 k3s 集群 |
| 136 | `k3s` | medium | 轻量级 Kubernetes 发行版 |
| 137 | `k9s` | medium | Interactive terminal UI for Kubernetes |
| 138 | `kaniko` | medium | 无需特权 Docker daemon 的镜像构建工具 |
| 139 | `kata-runtime` | medium | Kata Containers 运行时 |
| 140 | `keptn` | medium | Keptn 云原生应用生命周期编排 |
| 141 | `kfctl apply` | critical | Deploy Kubeflow to Kubernetes cluster |
| 142 | `kfctl delete` | critical | Delete Kubeflow deployment |
| 143 | `kfp experiment create` | low | Create a Kubeflow Pipelines experiment |
| 144 | `kfp pipeline list` | low | List Kubeflow Pipelines |
| 145 | `kfp pipeline upload` | low | Upload a pipeline to Kubeflow Pipelines |
| 146 | `kfp run submit` | medium | Submit a Kubeflow Pipeline run |
| 147 | `kind` | medium | 使用 Docker 容器运行本地 Kubernetes 集群 |
| 148 | `kn` | medium | Knative 命令行工具 |
| 149 | `krew` | medium | kubectl 插件包管理器 |
| 150 | `kube-bench run` | low | Run CIS Kubernetes security benchmark checks |
| 151 | `kube-hunter` | high | Kubernetes 集群渗透测试工具 |
| 152 | `kubeadm config view` | low | View the kubeadm configuration |
| 153 | `kubeadm init` | critical | Initialize Kubernetes control plane node |
| 154 | `kubeadm join` | high | Join worker node to Kubernetes cluster |
| 155 | `kubeadm reset` | critical | Reset node state and undo kubeadm init or join |
| 156 | `kubeadm token list` | low | List bootstrap tokens on the cluster |
| 157 | `kubeadm upgrade` | critical | Upgrade Kubernetes cluster to specified version |
| 158 | `kubectl` | low | Kubernetes命令行工具，管理集群资源 |
| 159 | `kubectl annotate` | low | Update annotations on a resource |
| 160 | `kubectl api-resources` | low | 列出所有可用的 API 资源 |
| 161 | `kubectl api-versions` | low | 显示支持的 API 版本 |
| 162 | `kubectl apply` | high | Apply a configuration to a resource by filename or stdin |
| 163 | `kubectl apply -f inferenceservice.yaml` | medium | Deploy a KServe InferenceService |
| 164 | `kubectl auth can-i` | low | Check if user has specific permissions |
| 165 | `kubectl cluster-info` | low | 显示集群基本信息 |
| 166 | `kubectl config` | high | Modify kubeconfig files |
| 167 | `kubectl config current-context` | medium | 显示当前配置上下文 |
| 168 | `kubectl cordon` | medium | Mark node as unschedulable |
| 169 | `kubectl cp` | high | Copy files between local filesystem and pod |
| 170 | `kubectl create` | medium | Create a resource from a file or stdin |
| 171 | `kubectl debug` | medium | 创建调试容器进行故障排查 |
| 172 | `kubectl delete` | critical | Delete resources by filenames, resources and names, or by label selectors |
| 173 | `kubectl delete inferenceservice` | high | Delete a KServe InferenceService |
| 174 | `kubectl delete pv` | critical | Delete PersistentVolume resources |
| 175 | `kubectl delete pvc` | critical | Delete PersistentVolumeClaim resources |
| 176 | `kubectl describe` | low | Show detailed information about a resource |
| 177 | `kubectl describe inferenceservice` | low | Show detailed information about KServe InferenceService |
| 178 | `kubectl describe pod` | low | 详细查看 Pod 状态和事件信息 |
| 179 | `kubectl drain` | critical | Drain node in preparation for maintenance |
| 180 | `kubectl exec` | high | Execute a command in a container |
| 181 | `kubectl get` | low | Display one or many resources |
| 182 | `kubectl get ciliumclusterwidenetworkpolicies` | low | List CiliumClusterwideNetworkPolicy resources |
| 183 | `kubectl get ciliumnetworkpolicies` | low | List CiliumNetworkPolicy resources for advanced networking |
| 184 | `kubectl get clusterrolebindings` | low | List ClusterRoleBinding resources for cluster-wide access |
| 185 | `kubectl get clusterroles` | low | List ClusterRole resources for cluster-wide permissions |
| 186 | `kubectl get componentstatuses` | low | 检查 Kubernetes 控制平面组件健康状态 |
| 187 | `kubectl get constraints` | low | List Constraint resources enforcing policies |
| 188 | `kubectl get constrainttemplates` | low | List ConstraintTemplate resources for OPA Gatekeeper |
| 189 | `kubectl get csidrivers` | low | List CSIDriver resources for Container Storage Interface drivers |
| 190 | `kubectl get csinodes` | low | List CSINode resources showing node storage capabilities |
| 191 | `kubectl get csistoragecapacities` | low | List CSIStorageCapacity resources showing storage availability |
| 192 | `kubectl get endpointslices` | low | List EndpointSlice resources showing service endpoints |
| 193 | `kubectl get events` | low | 获取集群事件信息，用于故障诊断 |
| 194 | `kubectl get experiments.kubeflow.org` | low | List Kubeflow Katib experiments |
| 195 | `kubectl get gateways` | low | List Gateway resources (Gateway API) |
| 196 | `kubectl get httproutes` | low | List HTTPRoute resources (Gateway API) |
| 197 | `kubectl get imagepolicies` | low | List ImagePolicy resources for image validation |
| 198 | `kubectl get inferenceservices` | low | List KServe InferenceServices |
| 199 | `kubectl get ingress` | low | List Ingress resources for external access |
| 200 | `kubectl get ingressclasses` | low | List IngressClass resources defining ingress controller types |
| 201 | `kubectl get limitrange` | low | 检查资源限制范围 |
| 202 | `kubectl get limitranges` | low | List LimitRange resources for resource constraints |
| 203 | `kubectl get networkpolicies` | low | List NetworkPolicy resources for traffic control |
| 204 | `kubectl get notebooks` | low | List Kubeflow Notebooks |
| 205 | `kubectl get podmonitors` | low | List PodMonitor resources for direct pod monitoring |
| 206 | `kubectl get podsecuritystandards` | medium | Check PodSecurity admission labels on namespaces (v1.23+) |
| 207 | `kubectl get prometheusagents` | low | List Prometheus Agent mode instances for lightweight monitoring |
| 208 | `kubectl get prometheuses` | low | List Prometheus instances managed by Prometheus Operator |
| 209 | `kubectl get prometheusrules` | low | List PrometheusRule resources containing alerting and recording rules |
| 210 | `kubectl get pv` | low | List PersistentVolume resources |
| 211 | `kubectl get pvc` | low | List PersistentVolumeClaim resources |
| 212 | `kubectl get pytorchjobs` | low | List Kubeflow PyTorch training jobs |
| 213 | `kubectl get resourcequota` | low | 检查资源配额限制 |
| 214 | `kubectl get resourcequotas` | low | List ResourceQuota resources for namespace quotas |
| 215 | `kubectl get rolebindings` | low | List RoleBinding resources linking users to roles |
| 216 | `kubectl get roles` | low | List Role resources for namespace-scoped permissions |
| 217 | `kubectl get scrapeconfigs` | low | List ScrapeConfig resources for external target monitoring |
| 218 | `kubectl get serviceaccounts` | low | List ServiceAccount resources for pod identities |
| 219 | `kubectl get servicemonitors` | low | List ServiceMonitor resources for automatic service discovery |
| 220 | `kubectl get storageclass` | low | List StorageClass resources defining storage provisioners |
| 221 | `kubectl get storagepools` | low | List StoragePool resources (specific storage systems) |
| 222 | `kubectl get tfjobs` | low | List Kubeflow TensorFlow training jobs |
| 223 | `kubectl get thanosrulers` | low | List Thanos Ruler instances for distributed alerting |
| 224 | `kubectl get tlsroutes` | low | List TLSRoute resources (Gateway API) |
| 225 | `kubectl get volumeattachments` | low | List VolumeAttachment resources showing volume-node associations |
| 226 | `kubectl get volumesnapshot` | low | List VolumeSnapshot resources for backup and restore |
| 227 | `kubectl get volumesnapshotclass` | low | List VolumeSnapshotClass resources defining snapshot provisioners |
| 228 | `kubectl get volumesnapshotcontent` | low | List VolumeSnapshotContent resources representing actual snapshots |
| 229 | `kubectl get workflows` | low | List Kubeflow Pipelines workflows |
| 230 | `kubectl label` | medium | Update labels on a resource |
| 231 | `kubectl label nodes` | low | Add or remove labels from nodes |
| 232 | `kubectl logs` | low | Print the logs for a container in a pod |
| 233 | `kubectl logs -f deployment/prometheus-operator` | low | Stream logs from Prometheus Operator for troubleshooting |
| 234 | `kubectl logs -l serving.kserve.io/inferenceservice` | low | View logs for KServe model serving pods |
| 235 | `kubectl patch storageclass` | high | Modify StorageClass configuration |
| 236 | `kubectl port-forward` | medium | Forward one or more local ports to a pod |
| 237 | `kubectl port-forward svc/alertmanager-operated` | medium | Port forward to access Alertmanager UI |
| 238 | `kubectl port-forward svc/grafana` | medium | Port forward to access Grafana dashboard |
| 239 | `kubectl port-forward svc/istio-ingressgateway` | low | Access Kubeflow dashboard locally |
| 240 | `kubectl port-forward svc/ml-pipeline-ui` | low | Access Kubeflow Pipelines UI locally |
| 241 | `kubectl port-forward svc/prometheus-operated` | medium | Port forward to access Prometheus web UI |
| 242 | `kubectl rollout` | high | Manage the rollout of a resource |
| 243 | `kubectl scale` | high | Set a new size for a deployment, replica set, or replication controller |
| 244 | `kubectl taint nodes` | medium | Add or remove taints from nodes |
| 245 | `kubectl top` | low | Display resource (CPU/memory) usage |
| 246 | `kubectl top pvc` | low | Show PVC resource usage (if metrics available) |
| 247 | `kubectl-neat` | low | 移除 kubectl get 输出中的默认字段，使 YAML 更简洁 |
| 248 | `kubectl-tree` | low | 以树状结构展示 K8s 资源 ownerReferences 关系 |
| 249 | `kubectl-who-can` | low | 检查谁对某个 K8s 资源拥有特定权限 |
| 250 | `kubectx` | high | Switch between Kubernetes contexts |
| 251 | `kubens` | medium | Switch between Kubernetes namespaces |
| 252 | `kubescape` | low | Kubernetes 安全与合规扫描工具 |
| 253 | `kubeseal` | low | Sealed Secrets 加密 CLI |
| 254 | `kustomize` | low | Kubernetes 声明式配置自定义工具 |
| 255 | `linkerd` | medium | 轻量级 Service Mesh CLI |
| 256 | `loki-cli` | low | Grafana Loki 日志查询 CLI（logcli） |
| 257 | `longhornctl` | high | Longhorn 分布式存储管理 |
| 258 | `lxc` | medium | Linux 容器（LXC）管理 |
| 259 | `lxd` | medium | LXC 系统容器管理守护进程 |
| 260 | `microk8s` | medium | Ubuntu 官方轻量 Kubernetes 发行版 |
| 261 | `minikube` | medium | 本地单节点 Kubernetes 集群工具 |
| 262 | `nerdctl` | medium | containerd 的 Docker 兼容 CLI |
| 263 | `node_exporter` | low | Start Prometheus Node Exporter for hardware and OS metrics |
| 264 | `nomad` | medium | HashiCorp Nomad 工作负载调度器 |
| 265 | `oc` | medium | OpenShift 命令行工具 |
| 266 | `okteto` | medium | 云端到本地的 Kubernetes 开发环境 |
| 267 | `otel-cli span` | low | Send span data to OpenTelemetry endpoint |
| 268 | `otel-cli status server` | low | Check OpenTelemetry endpoint status |
| 269 | `otelcol` | medium | Start OpenTelemetry Collector |
| 270 | `otelcol validate` | low | Validate OpenTelemetry Collector configuration |
| 271 | `otelcol-contrib` | medium | Start OpenTelemetry Collector Contrib distribution |
| 272 | `podman` | medium | 无守护进程的容器引擎，兼容 Docker CLI |
| 273 | `popeye` | low | Kubernetes cluster resource sanitizer and health checker |
| 274 | `prometheus` | medium | Start Prometheus monitoring server |
| 275 | `promtail` | medium | Loki 日志收集 Agent |
| 276 | `promtool check config` | low | Validate Prometheus configuration file |
| 277 | `promtool query instant` | low | Execute instant PromQL query |
| 278 | `promtool test rules` | low | Test Prometheus alerting and recording rules |
| 279 | `promtool tsdb analyze` | low | Analyze Prometheus TSDB blocks |
| 280 | `restic backup` | low | Create restic backup |
| 281 | `restic init` | low | Initialize restic backup repository |
| 282 | `restic restore` | high | Restore from restic backup |
| 283 | `restic snapshots` | low | List restic backup snapshots |
| 284 | `rookctl` | high | Rook Ceph 存储管理 |
| 285 | `skaffold build` | low | Build container images only (no deployment) |
| 286 | `skaffold delete` | high | Delete Skaffold deployments |
| 287 | `skaffold dev` | medium | Start Skaffold continuous development mode |
| 288 | `skaffold run` | high | Build and deploy application once |
| 289 | `skopeo` | medium | 容器镜像仓库操作工具，支持复制、检查签名 |
| 290 | `snyk` | low | 开发者安全扫描平台 CLI |
| 291 | `sops` | high | 文件加密编辑器（支持 AWS/GCP/Azure/KMS） |
| 292 | `stern` | low | Multi-pod and container log tailing for Kubernetes |
| 293 | `subctl` | high | Submariner 跨集群网络 CLI |
| 294 | `systemctl status containerd` | high | Check containerd service status |
| 295 | `systemctl status falco` | medium | Check Falco runtime security service status |
| 296 | `systemctl status fluentd` | medium | Check Fluentd service status |
| 297 | `systemctl status grafana-server` | medium | Check Grafana service status |
| 298 | `systemctl status kube-state-metrics` | low | Check kube-state-metrics service status |
| 299 | `systemctl status kubelet` | low | Check kubelet service status |
| 300 | `systemctl status loki` | medium | Check Loki service status |
| 301 | `systemctl status prometheus` | medium | Check Prometheus service status |
| 302 | `systemctl status promtail` | medium | Check Promtail service status |
| 303 | `telepresence` | high | 本地开发连接远程 Kubernetes 服务 |
| 304 | `telepresence connect` | medium | Connect local environment to Kubernetes cluster |
| 305 | `telepresence intercept` | critical | Intercept traffic to service and redirect to local process |
| 306 | `tempo-cli` | low | Grafana Tempo 追踪查询 CLI |
| 307 | `terraform apply` | critical | Apply Terraform configuration changes |
| 308 | `terraform destroy` | critical | Destroy Terraform-managed infrastructure |
| 309 | `terraform fmt` | low | Format Terraform configuration files |
| 310 | `terraform import` | medium | Import existing infrastructure into Terraform state |
| 311 | `terraform init` | low | Initialize Terraform working directory |
| 312 | `terraform output` | low | Display Terraform output values |
| 313 | `terraform plan` | low | Generate and show Terraform execution plan |
| 314 | `terraform refresh` | medium | Update Terraform state with real infrastructure |
| 315 | `terraform state list` | low | List resources in Terraform state |
| 316 | `terraform state rm` | high | Remove resource from Terraform state |
| 317 | `terraform state show` | low | Show detailed resource state |
| 318 | `terraform taint` | high | Mark resource for recreation on next apply |
| 319 | `terraform validate` | low | Validate Terraform configuration syntax |
| 320 | `terraform workspace list` | low | List Terraform workspaces |
| 321 | `terraform workspace new` | medium | Create new Terraform workspace |
| 322 | `terraform workspace select` | medium | Switch to different Terraform workspace |
| 323 | `tfsec` | low | Terraform 静态安全扫描工具 |
| 324 | `tilt down` | medium | Stop Tilt and cleanup resources |
| 325 | `tilt up` | medium | Start Tilt development environment |
| 326 | `tkn pipeline list` | low | List Tekton pipelines |
| 327 | `tkn pipeline start` | high | Start Tekton pipeline execution |
| 328 | `tkn pipelinerun logs` | low | View Tekton pipeline run logs |
| 329 | `trivy config` | low | Scan configuration files for misconfigurations |
| 330 | `trivy fs` | low | Scan filesystem for vulnerabilities and misconfigurations |
| 331 | `trivy image` | low | Scan container image for vulnerabilities |
| 332 | `trivy k8s` | low | Scan Kubernetes cluster for security issues |
| 333 | `vault` | critical | HashiCorp Vault 密钥管理 CLI |
| 334 | `vcluster` | medium | Kubernetes 虚拟集群 |
| 335 | `velero backup create` | medium | Create backup of Kubernetes resources |
| 336 | `velero backup list` | low | List all Velero backups |
| 337 | `velero restore create` | critical | Restore from Velero backup |
| 338 | `velero schedule create` | low | Create scheduled backup |

## 数据库 (64)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `arangosh` | medium | ArangoDB 多模型数据库 Shell |
| 2 | `cassandra-stress` | high | Cassandra 压力测试工具 |
| 3 | `clickhouse-client` | medium | ClickHouse 交互式 SQL 客户端 |
| 4 | `cockroach` | high | CockroachDB 分布式 SQL 数据库 CLI |
| 5 | `cqlsh` | medium | Cassandra CQL 交互式 Shell |
| 6 | `createdb` | medium | Create a new PostgreSQL database |
| 7 | `createuser` | high | Create a new PostgreSQL user |
| 8 | `cypher-shell` | medium | Neo4j 图数据库 Cypher 查询命令行客户端 |
| 9 | `databricks` | medium | Databricks CLI |
| 10 | `db2` | medium | IBM Db2 命令行处理器 |
| 11 | `dropdb` | critical | Remove a PostgreSQL database |
| 12 | `dropuser` | high | Remove a PostgreSQL user |
| 13 | `influx` | medium | InfluxDB 命令行客户端 |
| 14 | `influxd` | medium | InfluxDB 数据库服务守护进程 |
| 15 | `memcached` | medium | Memcached 内存对象缓存守护进程 |
| 16 | `mongodump` | medium | MongoDB 逻辑备份工具 |
| 17 | `mongoexport` | medium | 将 MongoDB 集合导出为 JSON 或 CSV |
| 18 | `mongoimport` | medium | 将 JSON/CSV/TSV 导入 MongoDB |
| 19 | `mongorestore` | high | 从 mongodump 备份恢复 MongoDB 数据 |
| 20 | `mongosh` | medium | MongoDB 官方交互式 Shell |
| 21 | `mongostat` | low | 实时显示 MongoDB 实例统计信息 |
| 22 | `mongotop` | low | 实时显示 MongoDB 集合级读写时间 |
| 23 | `mydumper` | low | 多线程 MySQL 逻辑备份工具 |
| 24 | `myloader` | high | 多线程恢复 mydumper 备份 |
| 25 | `mysql` | high | MySQL command-line client for database operations |
| 26 | `mysql_secure_installation` | medium | Script to improve MySQL installation security |
| 27 | `mysqladmin` | critical | MySQL server administration utility |
| 28 | `mysqlbinlog` | high | Process MySQL binary log files |
| 29 | `mysqlcheck` | medium | Check, repair, analyze, and optimize MySQL tables |
| 30 | `mysqldump` | medium | MySQL database backup utility |
| 31 | `mysqlimport` | high | Import data from text files into MySQL tables |
| 32 | `mysqlshow` | low | Display database, table, and column information |
| 33 | `mysqlslap` | high | MySQL 负载模拟与压测工具 |
| 34 | `neo4j-admin` | high | Neo4j 图数据库管理工具 |
| 35 | `pg_basebackup` | medium | Take a base backup of a PostgreSQL cluster |
| 36 | `pg_dump` | medium | PostgreSQL database backup utility |
| 37 | `pg_isready` | low | Check PostgreSQL server connection status |
| 38 | `pg_restore` | high | Restore PostgreSQL database from archive |
| 39 | `pgbench` | high | PostgreSQL 基准测试工具 |
| 40 | `psql` | high | PostgreSQL interactive terminal |
| 41 | `pt-query-digest` | low | Percona Toolkit 慢查询分析工具 |
| 42 | `redis` | low | 启动Redis服务器 |
| 43 | `redis-benchmark` | medium | Redis performance benchmarking tool |
| 44 | `redis-check-aof` | high | Check and repair Redis AOF (Append-Only File) |
| 45 | `redis-check-rdb` | low | Check Redis RDB snapshot file |
| 46 | `redis-cli` | high | Redis command-line interface client |
| 47 | `redis-cli FLUSHDB` | critical | Delete all keys in current database |
| 48 | `redis-cli INFO` | low | Get Redis server information and statistics |
| 49 | `redis-cli MONITOR` | medium | Monitor all commands processed by Redis server |
| 50 | `redis-cli SAVE` | high | Synchronously save dataset to disk |
| 51 | `redis-sentinel` | high | Redis Sentinel for high availability |
| 52 | `redis-server` | high | Redis server daemon |
| 53 | `rethinkdb` | medium | RethinkDB 分布式文档数据库 |
| 54 | `scylla` | medium | ScyllaDB 高性能 Cassandra 兼容数据库 |
| 55 | `snowsql` | low | Snowflake 数据仓库命令行客户端 |
| 56 | `sqlcmd` | medium | SQL Server 命令行工具 |
| 57 | `sqlite3` | low | SQLite 命令行数据库客户端 |
| 58 | `sqlplus` | high | Oracle 数据库 SQL*Plus 客户端 |
| 59 | `tidb-ctl` | medium | TiDB 集群诊断与管理工具 |
| 60 | `vacuumdb` | medium | Garbage-collect and analyze a PostgreSQL database |
| 61 | `xtrabackup` | medium | Percona XtraBackup 热备份工具 |
| 62 | `ycqlsh` | low | YugabyteDB Cassandra 兼容 CQL Shell |
| 63 | `ysqlsh` | low | YugabyteDB 兼容 PostgreSQL 的 SQL Shell |
| 64 | `yugabyted` | high | YugabyteDB 集群生命周期管理命令 |

## 系统诊断 (27)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `arthas` | medium | Start Arthas and attach to Java process |
| 2 | `bcc` | medium | BPF Compiler Collection 工具集 |
| 3 | `bpftrace` | medium | 高级 eBPF 跟踪语言 |
| 4 | `classloader` | low | Display classloader information |
| 5 | `dashboard` | low | Display real-time dashboard of JVM metrics |
| 6 | `heapdump` | high | Dump Java heap to file |
| 7 | `jad` | low | Decompile Java class files |
| 8 | `logger` | medium | View or modify logger settings |
| 9 | `ltrace` | low | 跟踪库函数调用 |
| 10 | `sc` | low | Search loaded classes |
| 11 | `sm` | low | Search methods in classes |
| 12 | `stack` | low | Display method call stack |
| 13 | `strace` | low | 跟踪系统调用 |
| 14 | `sysdig` | medium | 系统级监控与故障排查 |
| 15 | `thread` | low | Display thread information |
| 16 | `trace` | medium | Trace method execution time |
| 17 | `tsar` | low | Display system performance statistics |
| 18 | `tsar --check` | low | Check tsar configuration and data files |
| 19 | `tsar --cpu` | low | Display detailed CPU statistics |
| 20 | `tsar --io` | low | Display disk I/O statistics |
| 21 | `tsar --list` | low | List available modules |
| 22 | `tsar --load` | low | Display system load average |
| 23 | `tsar --mem` | low | Display memory usage statistics |
| 24 | `tsar --partition` | low | Display disk partition usage |
| 25 | `tsar --tcp` | low | Display TCP connection statistics |
| 26 | `tsar --traffic` | low | Display network traffic statistics |
| 27 | `watch` | medium | Watch method invocation in real-time |

## 硬件 (64)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `avrdude` | medium | AVR 单片机烧录 |
| 2 | `biosdecode` | low | 解析 BIOS 信息 |
| 3 | `bluetoothctl` | low | 蓝牙设备管理交互式工具 |
| 4 | `bonnie++` | high | 文件系统性能基准测试 |
| 5 | `cgexec` | medium | 在指定 cgroup 中运行命令 |
| 6 | `chrt` | high | 设置实时调度策略 |
| 7 | `clinfo` | low | 显示 OpenCL 平台与设备信息 |
| 8 | `cpupower` | medium | CPU 频率与空闲状态管理 |
| 9 | `cset` | medium | cpuset 资源隔离工具 |
| 10 | `dfu-util` | medium | USB DFU 设备固件更新 |
| 11 | `efibootmgr` | critical | 管理 UEFI 启动项 |
| 12 | `efivar` | high | 读取和写入 UEFI 变量 |
| 13 | `esptool` | medium | ESP8266/ESP32 烧录工具 |
| 14 | `ethtool` | medium | 查看和设置网卡参数 |
| 15 | `fio` | high | 灵活的 I/O 测试器 |
| 16 | `flashrom` | critical | 读取/写入/擦除闪存芯片 |
| 17 | `fwupd` | high | Linux 固件更新守护进程与工具 |
| 18 | `gpio` | medium | Linux GPIO 命令行工具（libgpiod） |
| 19 | `hardinfo` | low | 图形/命令行系统信息与基准测试 |
| 20 | `hddtemp` | low | 显示硬盘温度 |
| 21 | `hwloc` | low | 硬件拓扑抽象层工具 |
| 22 | `i2cdetect` | low | 扫描 I2C 总线上的设备 |
| 23 | `i2cget` | low | 读取 I2C 设备寄存器 |
| 24 | `i2cset` | medium | 写入 I2C 设备寄存器 |
| 25 | `intel-gpu-top` | low | Intel GPU 占用监控 |
| 26 | `inxi` | low | 友好的系统/硬件信息汇总工具 |
| 27 | `ionice` | low | 设置进程 I/O 调度优先级 |
| 28 | `ipmicfg` | high | Supermicro IPMI 配置工具 |
| 29 | `ipmitool` | high | IPMI 带外管理工具 |
| 30 | `iw` | medium | 新一代无线设备配置工具 |
| 31 | `iwconfig` | medium | 传统无线接口配置 |
| 32 | `lshw` | low | 列出详细硬件配置 |
| 33 | `lsscsi` | low | 列出 SCSI/SAS 设备 |
| 34 | `lstopo` | low | 图形/文本化硬件拓扑查看器 |
| 35 | `mdadm` | critical | Linux 软 RAID 管理 |
| 36 | `minicom` | low | 串口通信终端 |
| 37 | `mokutil` | high | 管理 UEFI Secure Boot MOK |
| 38 | `numactl` | medium | 控制进程的 NUMA 内存与 CPU 策略 |
| 39 | `numastat` | low | 显示每个 NUMA 节点的内存统计 |
| 40 | `nvidia-smi` | medium | NVIDIA GPU 管理与监控 |
| 41 | `nvme` | high | NVMe 设备管理 CLI |
| 42 | `openocd` | medium | 开源片上调试器 |
| 43 | `partprobe` | medium | 通知内核分区表变化 |
| 44 | `perf` | low | Linux 性能分析工具 |
| 45 | `picocom` | low | 极简串口终端 |
| 46 | `powertop` | medium | 电源消耗与节能诊断 |
| 47 | `radeontop` | low | AMD GPU 占用监控 |
| 48 | `raspi-gpio` | medium | 树莓派 GPIO 工具 |
| 49 | `redfish` | medium | Redfish API 客户端（python-redfish 或 curl 示例） |
| 50 | `rfkill` | high | 无线设备软开关管理 |
| 51 | `rocm-smi` | medium | AMD ROCm GPU 管理 |
| 52 | `s-tui` | medium | 终端 CPU 压力与监控 TUI |
| 53 | `sensors` | low | 读取硬件传感器数据（lm-sensors） |
| 54 | `sensors-detect` | medium | 检测系统中的传感器芯片 |
| 55 | `sg_scan` | low | 扫描 SCSI 通用设备 |
| 56 | `smartctl` | low | SMART 硬盘健康检测 |
| 57 | `st-flash` | medium | STM32 ST-Link 烧录工具 |
| 58 | `stress` | high | 简单的系统压力测试 |
| 59 | `stress-ng` | high | 更全面的系统压力测试 |
| 60 | `taskset` | medium | 设置或查看进程 CPU 亲和性 |
| 61 | `thermald` | medium | Intel 平台热量管理守护进程 |
| 62 | `tlp` | medium | Linux 笔记本电源管理 |
| 63 | `turbostat` | low | Intel CPU 频率与功耗监控 |
| 64 | `vpddecode` | low | 解析 VPD（重要产品数据） |

## 编程语言 (47)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `bundle` | low | Ruby 项目依赖管理 |
| 2 | `cargo` | low | Rust 包管理器和构建工具 |
| 3 | `cargo clippy` | low | Rust 代码 lint 工具，检测常见错误和改进建议 |
| 4 | `cargo fmt` | low | Rust 代码格式化工具 |
| 5 | `dotnet` | low | .NET 命令行工具 |
| 6 | `gem` | low | Ruby 包管理器 |
| 7 | `go build` | medium | 编译Go包和依赖 |
| 8 | `go fmt` | medium | 格式化Go代码 |
| 9 | `go get` | medium | 添加依赖到当前模块 |
| 10 | `go install` | medium | 编译并安装Go包到$GOPATH/bin |
| 11 | `go mod` | medium | 模块维护 |
| 12 | `go run` | low | 编译并运行Go程序 |
| 13 | `go test` | low | 运行测试 |
| 14 | `go vet` | low | 检查Go代码中的常见错误 |
| 15 | `groovy` | low | Groovy 脚本语言 |
| 16 | `jar` | low | 创建和管理JAR文件 |
| 17 | `java` | low | 运行Java程序 |
| 18 | `javac` | low | 编译Java源代码 |
| 19 | `javadoc` | low | 生成Java文档 |
| 20 | `jcmd` | low | 向运行JVM发送诊断命令 |
| 21 | `jhat` | low | Java堆分析工具，分析堆转储文件 |
| 22 | `jmap` | medium | 生成堆转储和内存映射 |
| 23 | `jps` | low | 显示Java进程状态 |
| 24 | `jstack` | low | 打印Java线程堆栈 |
| 25 | `jstat` | low | 监控JVM统计信息 |
| 26 | `kotlin` | low | Kotlin 命令行编译器 |
| 27 | `node` | medium | Execute JavaScript code using Node.js runtime |
| 28 | `npm audit` | medium | Check for security vulnerabilities |
| 29 | `npm install` | medium | Install package dependencies |
| 30 | `npm outdated` | low | Check for outdated packages |
| 31 | `npm publish` | high | Publish package to npm registry |
| 32 | `npm run` | medium | Run arbitrary package scripts |
| 33 | `npm start` | medium | Run the start script defined in package.json |
| 34 | `npm test` | low | Run the test script defined in package.json |
| 35 | `npm update` | medium | Update packages to their latest versions |
| 36 | `npx` | medium | Execute npm package binaries |
| 37 | `php` | low | PHP 命令行解释器 |
| 38 | `pip` | medium | Python包管理器 |
| 39 | `pylint` | low | Python代码检查工具 |
| 40 | `pytest` | low | Python测试框架 |
| 41 | `python` | low | 运行Python解释器 |
| 42 | `ruby` | low | Ruby 解释器 |
| 43 | `rustc` | low | Rust 编译器 |
| 44 | `rustup` | medium | Rust 工具链安装器和版本管理器 |
| 45 | `sbt` | low | Scala 构建工具 |
| 46 | `scala` | low | Scala 解释器与运行器 |
| 47 | `virtualenv` | medium | 创建Python虚拟环境 |

## 网络工具 (57)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `ab` | high | Apache HTTP server benchmarking tool |
| 2 | `amass` | medium | 深度子域名枚举与资产发现 |
| 3 | `artillery` | high | 现代 Node.js 负载测试与 SRE 工具 |
| 4 | `caddy` | medium | 易用且默认 HTTPS 的 Web 服务器 |
| 5 | `curl` | low | 命令行HTTP客户端 |
| 6 | `dig` | low | DNS查询工具 |
| 7 | `dnsmasq` | medium | 轻量级 DNS 转发与 DHCP 服务器 |
| 8 | `dnsrecon` | medium | DNS 枚举与区域传送检测 |
| 9 | `dog` | low | 友好的命令行 DNS 客户端 |
| 10 | `fortio` | high | Istio 配套的负载测试与 echo 服务器 |
| 11 | `haproxy` | medium | TCP/HTTP 负载均衡器 |
| 12 | `host` | low | 简单的DNS查询工具 |
| 13 | `hping3` | critical | 自定义 TCP/IP 数据包生成与探测工具 |
| 14 | `httpie` | medium | User-friendly HTTP client |
| 15 | `httpx` | medium | 快速多线程 HTTP 探活与信息收集工具 |
| 16 | `ifconfig` | medium | 传统网络接口配置工具 |
| 17 | `iftop` | low | 实时显示网络接口带宽使用 |
| 18 | `iperf3` | medium | TCP/UDP 网络带宽测试工具 |
| 19 | `k6` | high | 现代化负载测试工具，使用 JavaScript 编写测试脚本 |
| 20 | `locust` | high | Python 编写的可编程负载测试工具 |
| 21 | `masscan` | critical | 高速互联网规模端口扫描器 |
| 22 | `mitmproxy` | high | 交互式 HTTPS 代理与流量分析工具 |
| 23 | `mtr` | low | 结合 ping 和 traceroute 的网络路径诊断工具 |
| 24 | `named-checkconf` | low | 检查 BIND DNS 配置文件语法 |
| 25 | `nc` | medium | Netcat，网络工具中的瑞士军刀，用于读写网络连接 |
| 26 | `netstat` | low | 显示网络连接和路由表 |
| 27 | `nginx` | medium | 高性能 Web 服务器与反向代理 |
| 28 | `ngrep` | high | 网络数据包内容过滤工具 |
| 29 | `nmap` | high | 网络发现与安全审计扫描工具 |
| 30 | `nslookup` | low | 查询DNS信息 |
| 31 | `nsupdate` | high | 动态更新 DNS 记录 |
| 32 | `nuclei` | high | 基于模板的快速漏洞扫描器 |
| 33 | `oha` | high | Rust 编写的实时 HTTP 负载生成器 |
| 34 | `openvpn` | medium | SSL/TLS VPN 解决方案 |
| 35 | `ping` | low | 测试网络连通性 |
| 36 | `postman` | low | API development and testing platform (CLI) |
| 37 | `proxychains` | medium | 强制任意程序通过代理连接网络 |
| 38 | `rndc` | medium | BIND DNS 服务器远程控制 |
| 39 | `route` | high | 传统路由表管理 |
| 40 | `siege` | high | HTTP load testing and benchmarking utility |
| 41 | `socat` | medium | 双向数据转发工具，号称 netcat 增强版 |
| 42 | `ss` | low | socket统计信息(替代netstat) |
| 43 | `sshuttle` | medium | 基于 SSH 的透明代理 VPN |
| 44 | `subfinder` | medium | 子域名发现工具 |
| 45 | `tcpdump` | medium | 抓取和分析网络包 |
| 46 | `tcpflow` | high | TCP 流重组与捕获工具 |
| 47 | `telnet` | medium | 基于文本的远程登录/端口探测工具 |
| 48 | `termshark` | high | 终端交互式 TUI 抓包工具 |
| 49 | `traceroute` | low | 跟踪数据包的路由路径 |
| 50 | `traefik` | medium | 云原生边缘路由/反向代理 |
| 51 | `tshark` | high | Wireshark 命令行抓包工具 |
| 52 | `unbound-control` | medium | Unbound DNS 服务器远程控制 |
| 53 | `vegeta` | high | 多功能的 HTTP 负载测试 CLI 和库 |
| 54 | `wg` | medium | WireGuard 快速、现代、安全的 VPN |
| 55 | `wget` | medium | Download files from the web |
| 56 | `wrk` | high | 高性能 HTTP 基准测试工具 |
| 57 | `wrk2` | high | 支持恒定吞吐量请求与精确延迟测量的 HTTP 压测工具 |

## 操作系统 (153)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `anacron` | medium | 用于非 24x7 机器执行周期性任务 |
| 2 | `apropos` | low | 按关键字搜索手册页 |
| 3 | `apt install` | medium | Install new packages |
| 4 | `apt remove` | high | Remove installed packages |
| 5 | `apt search` | low | Search for packages |
| 6 | `apt update` | low | Update package index from repositories |
| 7 | `apt upgrade` | medium | Upgrade all installed packages |
| 8 | `apt-cache show` | low | Show package information |
| 9 | `at` | high | 在指定时间执行一次性任务 |
| 10 | `awk` | low | 文本处理语言，按模式扫描和处理文件 |
| 11 | `blkid` | low | 显示块设备属性（UUID、文件系统类型等） |
| 12 | `bridge` | medium | 以太网桥管理 |
| 13 | `bzip2` | low | 块排序文件压缩工具 |
| 14 | `cat` | low | 连接文件并输出到标准输出 |
| 15 | `cd` | low | 切换当前工作目录 |
| 16 | `chmod` | high | 修改文件或目录权限 |
| 17 | `chown` | high | 修改文件或目录所有者 |
| 18 | `cp` | medium | 复制文件或目录 |
| 19 | `crontab` | high | 管理用户定时任务 |
| 20 | `cryptsetup` | critical | LUKS/dm-crypt 磁盘加密工具 |
| 21 | `date` | medium | 显示或设置系统日期时间 |
| 22 | `df` | low | 报告文件系统磁盘空间使用情况 |
| 23 | `dmesg` | low | 查看内核环形缓冲区消息 |
| 24 | `dmidecode` | low | 从 DMI 表读取硬件信息 |
| 25 | `dnf install` | medium | Install packages (newer package manager for CentOS 8+) |
| 26 | `dpkg -i` | high | Install .deb package file |
| 27 | `dpkg -l` | low | List installed packages |
| 28 | `dpkg -r` | high | Remove installed package |
| 29 | `du` | low | 估算文件和目录的磁盘使用空间 |
| 30 | `egrep` | low | 扩展正则表达式grep（等同于grep -E） |
| 31 | `env` | low | 显示或修改环境变量后执行命令 |
| 32 | `export` | low | 设置或显示环境变量 |
| 33 | `fdisk` | critical | 磁盘分区表管理工具 |
| 34 | `fgrep` | low | 固定字符串grep（等同于grep -F），禁用正则表达式 |
| 35 | `file` | low | 识别文件类型 |
| 36 | `find` | high | 在目录树中搜索文件 |
| 37 | `firewall-cmd --add-port` | medium | Open firewall port |
| 38 | `firewall-cmd --list-all` | low | List all firewall rules |
| 39 | `free` | low | 显示系统内存使用情况 |
| 40 | `fsck` | critical | 检查并修复文件系统 |
| 41 | `getenforce` | low | Get current SELinux mode |
| 42 | `getent` | low | 查询系统数据库条目 |
| 43 | `grep` | low | 在文件中搜索文本模式 |
| 44 | `groupadd` | medium | 创建用户组 |
| 45 | `groupdel` | medium | 删除用户组 |
| 46 | `gzip` | medium | GNU 文件压缩工具 |
| 47 | `hdparm` | medium | 查看和设置 SATA/IDE 硬盘参数 |
| 48 | `head` | low | 显示文件开头部分 |
| 49 | `hostnamectl` | low | 查看和设置主机名 |
| 50 | `htop` | low | 交互式进程查看器 |
| 51 | `iconv` | low | 字符编码转换 |
| 52 | `ip` | high | Linux 网络配置与路由管理核心工具 |
| 53 | `ipset` | medium | IP 集合管理，常与 iptables 配合 |
| 54 | `iptables` | high | IPv4 包过滤与 NAT 防火墙 |
| 55 | `journalctl` | low | 查询 systemd 日志 |
| 56 | `jq` | low | 命令行 JSON 处理器 |
| 57 | `kill` | high | 向进程发送信号以终止或控制 |
| 58 | `less` | low | 分页查看文件内容，支持前后翻页 |
| 59 | `ln` | medium | 创建文件链接 |
| 60 | `locale` | low | 显示和设置区域设置 |
| 61 | `locate` | low | 通过预建数据库快速查找文件 |
| 62 | `ls` | low | 列出目录内容 |
| 63 | `lsblk` | low | 列出块设备信息 |
| 64 | `lscpu` | low | 显示 CPU 架构与信息 |
| 65 | `lsmem` | low | 列出内存信息 |
| 66 | `lsof` | low | 列出已打开的文件及对应进程 |
| 67 | `lspci` | low | 列出 PCI 设备 |
| 68 | `lsusb` | low | 列出 USB 设备 |
| 69 | `lvcreate` | high | 创建逻辑卷（LVM） |
| 70 | `lvs` | low | 显示逻辑卷信息（LVM） |
| 71 | `man` | low | 查看命令/函数手册页 |
| 72 | `md5sum` | low | 计算或校验 MD5 校验和 |
| 73 | `mkdir` | low | 创建目录 |
| 74 | `mkfs` | critical | 创建文件系统 |
| 75 | `more` | low | 分页查看文件内容（less的简化版） |
| 76 | `mount` | high | 挂载文件系统 |
| 77 | `mv` | medium | 移动或重命名文件和目录 |
| 78 | `netplan` | high | Ubuntu 网络配置管理工具 |
| 79 | `nftables` | high | 新一代 nftables 防火墙（nft 命令） |
| 80 | `nice` | low | 以指定优先级运行命令 |
| 81 | `nmcli` | medium | NetworkManager 命令行工具 |
| 82 | `parted` | critical | 高级磁盘分区工具 |
| 83 | `passwd` | high | 修改用户密码 |
| 84 | `pvcreate` | critical | 初始化物理卷（LVM） |
| 85 | `pvs` | low | 显示物理卷信息（LVM） |
| 86 | `pwd` | low | 显示当前工作目录的完整路径 |
| 87 | `rename` | low | 批量重命名文件（Perl正则表达式版或util-linux版） |
| 88 | `renice` | medium | 修改运行中进程的优先级 |
| 89 | `resolvectl` | low | systemd-resolved DNS 解析控制 |
| 90 | `rm` | critical | 删除文件或目录 |
| 91 | `rmdir` | low | 删除空目录 |
| 92 | `rpm -e` | high | Erase (remove) installed package |
| 93 | `rpm -i` | high | Install RPM package file |
| 94 | `rpm -qa` | low | Query all installed packages |
| 95 | `rpm -qi` | low | Query package information |
| 96 | `rsync` | low | 远程和本地文件同步工具，支持增量传输 |
| 97 | `scp` | medium | 基于 SSH 的安全文件复制 |
| 98 | `sed` | low | 流编辑器，执行基本的文本转换 |
| 99 | `sestatus` | low | Display SELinux status |
| 100 | `setenforce` | high | Change SELinux mode temporarily |
| 101 | `sh` | low | Bourne Shell，标准的Unix命令解释器 |
| 102 | `sha256sum` | low | 计算或校验 SHA-256 校验和 |
| 103 | `snap install` | low | Install snap package |
| 104 | `ssh` | medium | OpenSSH 远程登录客户端 |
| 105 | `su` | medium | 切换用户身份 |
| 106 | `sudo` | high | 以超级用户或其他用户身份执行命令 |
| 107 | `sysctl` | high | 运行时内核参数管理 |
| 108 | `systemctl disable` | low | Disable service from starting on boot |
| 109 | `systemctl enable` | medium | Enable service to start on boot |
| 110 | `systemctl restart` | medium | Restart a systemd service |
| 111 | `systemctl start` | medium | Start a systemd service |
| 112 | `systemctl status` | low | Check service status |
| 113 | `systemctl stop` | high | Stop a systemd service |
| 114 | `tail` | low | 显示文件末尾部分，支持实时跟踪 |
| 115 | `tar` | medium | 归档和压缩工具 |
| 116 | `tc` | high | Linux 流量控制（Traffic Control） |
| 117 | `timedatectl` | medium | 查看和设置系统时间与日期 |
| 118 | `timeout` | low | 在指定时间后终止命令 |
| 119 | `tmux` | low | 终端复用器，支持会话持久化和多窗口 |
| 120 | `touch` | low | 更新文件时间戳或创建空文件 |
| 121 | `trash` | low | 将文件移动到回收站而非永久删除 |
| 122 | `tune2fs` | high | 调整 ext2/3/4 文件系统参数 |
| 123 | `ufw allow` | medium | Allow firewall rule |
| 124 | `ufw deny` | medium | Deny firewall rule |
| 125 | `ufw enable` | high | Enable Ubuntu firewall |
| 126 | `ufw status` | low | Show firewall status and rules |
| 127 | `ulimit` | medium | 显示或设置 shell 资源限制 |
| 128 | `umask` | medium | 显示或设置默认文件权限掩码 |
| 129 | `umount` | high | 卸载文件系统 |
| 130 | `uname` | low | 显示系统内核信息 |
| 131 | `unzip` | medium | 解压 ZIP 归档 |
| 132 | `uptime` | low | 显示系统运行时长和平均负载 |
| 133 | `useradd` | medium | 创建用户账户 |
| 134 | `userdel` | high | 删除用户账户 |
| 135 | `usermod` | medium | 修改用户账户 |
| 136 | `vgcreate` | high | 创建卷组（LVM） |
| 137 | `vgs` | low | 显示卷组信息（LVM） |
| 138 | `visudo` | critical | 安全编辑 sudoers 文件 |
| 139 | `whatis` | low | 显示命令简短描述 |
| 140 | `whereis` | low | 定位命令的二进制、源码和手册页文件 |
| 141 | `which` | low | 查找命令的可执行文件路径 |
| 142 | `xargs` | high | 从标准输入构建并执行命令 |
| 143 | `xxd` | low | 十六进制查看器和编辑器 |
| 144 | `xz` | low | 高压缩比文件压缩工具 |
| 145 | `yq` | high | 命令行 YAML/JSON/TOML 处理器 |
| 146 | `yum info` | low | Show package information |
| 147 | `yum install` | medium | Install new packages |
| 148 | `yum list installed` | low | List all installed packages |
| 149 | `yum remove` | high | Remove installed packages |
| 150 | `yum search` | low | Search for packages |
| 151 | `yum update` | medium | Update all installed packages |
| 152 | `zip` | low | 创建 ZIP 归档 |
| 153 | `zsh` | low | Z Shell，功能强大的交互式Shell，兼容Bash |

## Shell 脚本 (5)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `bash` | low | Bash Shell 解释器，执行脚本文件或交互式命令 |
| 2 | `shellcheck` | low | Shell 脚本静态分析工具，检测常见错误和最佳实践 |
| 3 | `shfmt` | low | Shell 脚本格式化工具 |
| 4 | `source` | medium | 在当前 Shell 环境中执行脚本（不创建子进程） |
| 5 | `trap` | low | 捕获信号并在脚本中执行清理操作 |

## 版本控制 (31)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `git add` | low | 添加文件到暂存区 |
| 2 | `git branch` | low | 列出、创建或删除分支 |
| 3 | `git checkout` | medium | 切换分支或恢复文件 |
| 4 | `git clone` | low | 克隆远程仓库到本地 |
| 5 | `git commit` | low | 提交暂存区的更改 |
| 6 | `git diff` | low | 显示工作区与暂存区或提交之间的差异 |
| 7 | `git fetch` | low | 从远程仓库下载对象和引用，但不合并 |
| 8 | `git init` | low | 初始化新的Git仓库 |
| 9 | `git log` | low | 查看提交历史 |
| 10 | `git merge` | medium | 合并分支 |
| 11 | `git pull` | low | 拉取远程更改并合并 |
| 12 | `git push` | high | 推送本地提交到远程仓库 |
| 13 | `git rebase` | medium | 将当前分支变基到另一分支，重写提交历史 |
| 14 | `git restore` | low | 恢复工作区或暂存区文件（Git 2.23+ 推荐替代checkout） |
| 15 | `git show` | low | 显示提交、标签或对象的详细信息和差异 |
| 16 | `git status` | low | 显示工作区状态 |
| 17 | `git switch` | low | 切换分支（Git 2.23+ 推荐替代checkout） |
| 18 | `svn add` | low | Add files to version control |
| 19 | `svn checkout` | low | Check out a working copy from a repository |
| 20 | `svn cleanup` | low | Clean up working copy (remove locks, fix interrupted operations) |
| 21 | `svn commit` | medium | Send changes to repository |
| 22 | `svn copy` | medium | Create a copy (branch/tag) in repository |
| 23 | `svn delete` | high | Remove files from version control |
| 24 | `svn diff` | low | Show differences between revisions |
| 25 | `svn info` | low | Display information about working copy or repository |
| 26 | `svn log` | low | Show commit log messages |
| 27 | `svn merge` | high | Merge changes from another branch |
| 28 | `svn revert` | high | Undo local changes |
| 29 | `svn status` | low | Show working copy status |
| 30 | `svn switch` | medium | Switch working copy to different URL |
| 31 | `svn update` | medium | Update working copy to latest revision |

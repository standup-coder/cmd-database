# AI 命令缺口分析 Phase 2

> 当前状态：11 个分类，148 个命令  
> 目标：覆盖大模型领域全链路最后一公里

---

## 已覆盖领域 ✅

- ML框架、MLOps平台、模型服务
- 大模型训练 (21命令)、推理 (22命令)
- 模型生态 (16命令)、数据标注 (13命令)
- 监控评估 (16命令)、向量数据库 (15命令)
- Agent工程 (19命令)、Harness工程 (16命令)

---

## 关键缺失领域 🔴

### 1. AI网关与API管理（生产部署核心）
LLM应用上线必用：统一路由、负载均衡、成本追踪、Fallback策略
- **Helicone** — LLM可观测性网关
- **Portkey** — AI网关与语义缓存
- **OpenRouter** — 统一访问100+模型API
- **Promptfoo** — Prompt测试与回归
- **Keywords AI** — 统一LLM API管理
- **Kong AI Gateway** — 企业级API网关

### 2. AI安全与模型扫描（合规刚需）
模型部署前的安全检查：漏洞扫描、偏见检测、对抗攻击
- **Garak** — LLM漏洞扫描框架
- **ModelScan** — Pickle/模型文件恶意代码扫描
- **LLM Guard** — 输入输出安全过滤器
- **Inspect AI** — UK AISI评估框架
- **Protect AI** — 端到端ML安全平台

### 3. 多模态（大模型核心扩展）
图像理解、语音处理、视频生成是当前大模型最活跃方向
- **ComfyUI** — Stable Diffusion节点式工作流
- **Whisper** — OpenAI语音识别
- **Faster-Whisper** — 极速Whisper推理
- **LLaVA** — 大语言视觉助手
- **CLIP** — 图文对齐模型
- **Stable Diffusion CLI** — 文本到图像生成

### 4. AI辅助编程（开发效率革命）
AI Coding Agent正重塑软件开发流程
- **Aider** — 终端AI编程助手
- **OpenHands** (原OpenDevin) — 开源AI软件工程师
- **SWE-Agent** — 自动修复GitHub Issue
- **Continue.dev** — IDE内AI编程助手
- **Supermaven** — 免费AI代码补全

### 5. RAG基础设施/文档解析
RAG应用的核心痛点：PDF解析、OCR、文档结构化
- **Unstructured** — 通用文档解析
- **LlamaParse** — LlamaIndex高级PDF解析
- **Docling** — IBM开源文档解析
- **Marker** — PDF转Markdown
- **PyMuPDF** — 高性能PDF处理

### 6. 边缘AI部署（端侧推理）
手机、IoT、嵌入式设备上的模型部署
- **TensorFlow Lite** — 移动端推理
- **ExecuTorch** — PyTorch移动端运行时
- **MediaPipe** — Google端侧ML流水线
- **Paddle Lite** — 百度端侧推理

---

## 补齐计划

新增 5 个分类，约 30-35 个命令：
- `ai/ai-gateway.yaml` — 6个命令
- `ai/ai-safety.yaml` — 5个命令
- `ai/multimodal.yaml` — 6个命令
- `ai/ai-coding.yaml` — 5个命令
- `ai/rag-infra.yaml` — 5个命令
- `ai/edge-ai.yaml` — 4个命令

预计完成后：17 个AI分类，~180 个AI命令

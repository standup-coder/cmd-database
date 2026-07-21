# 领域映射报告（阶段 0 产物，请抽查）

- 命令总数：**1235**
- 领域数：**120**
- slug 冲突：**3**
- 跳过的 YAML 文件：**1**

## 各领域命令数（降序）

| 领域 | 命令数 |
|------|--------|
| 扩展工具 | 51 |
| 通用Linux命令 | 44 |
| 扩展命令 | 41 |
| K8s监控日志 | 39 |
| Linux核心 | 37 |
| Linux扩展命令 | 36 |
| 云原生扩展 | 29 |
| 大模型推理 | 27 |
| 大模型训练 | 27 |
| K8s配置管理 | 27 |
| 云原生扩展二 | 26 |
| Harness工程 | 21 |
| K8s安全工具 | 20 |
| Ubuntu系统命令 | 20 |
| K8s Helm包管理 | 19 |
| K8s网络插件 | 19 |
| Agent工程 | 18 |
| K8s机器学习运维 | 18 |
| Kubernetes命令 | 17 |
| Git命令 | 17 |
| 模型生态 | 16 |
| 监控与评估 | 16 |
| 向量数据库 | 16 |
| Docker命令 | 16 |
| K8s存储管理 | 16 |
| CentOS系统命令 | 16 |
| K8s集群管理 | 14 |
| 基础设施 | 14 |
| SVN命令 | 14 |
| 数据与标注 | 13 |
| Java诊断 | 12 |
| 嵌入式与IoT | 12 |
| K8s持续集成 | 11 |
| Redis工具 | 11 |
| 性能与调度 | 11 |
| K8s故障排查 | 10 |
| PostgreSQL工具 | 10 |
| 系统诊断 | 10 |
| Java工具链 | 10 |
| Node.js工具链 | 10 |
| Git高级操作 | 10 |
| 模型架构 | 9 |
| GitOps | 9 |
| 平台工具 | 9 |
| Azure CLI | 9 |
| GCP CLI | 9 |
| K8s云平台工具 | 9 |
| K8s容器运行时 | 9 |
| 扩展工具链 | 9 |
| 现代工具 | 9 |
| K8s备份恢复 | 8 |
| K8s开发调试 | 8 |
| K8s辅助工具 | 8 |
| MySQL工具 | 8 |
| 存储与RAID | 8 |
| Go工具链 | 8 |
| AI应用 | 7 |
| 固件与UEFI | 7 |
| 系统信息 | 7 |
| Go工具链扩展 | 7 |
| 性能压测 | 7 |
| 网络安全 | 7 |
| Systemd服务管理 | 7 |
| AI编译器 | 6 |
| AI网关 | 6 |
| 多模态 | 6 |
| 包管理 | 6 |
| AWS CLI | 6 |
| NoSQL | 6 |
| 传感器与电源 | 6 |
| 网络诊断 | 6 |
| AI编程 | 5 |
| AI安全 | 5 |
| 模型可解释性 | 5 |
| RAG基础设施 | 5 |
| 数据集成与ETL | 5 |
| Kafka工具 | 5 |
| 查询引擎 | 5 |
| CMake | 5 |
| GitHub Actions | 5 |
| 配置管理 | 5 |
| 多云CLI | 5 |
| K8s安全扩展 | 5 |
| GPU与加速器 | 5 |
| 网络硬件 | 5 |
| Python工具链扩展 | 5 |
| Python工具链 | 5 |
| Rust工具链 | 5 |
| HTTP工具 | 5 |
| 安全扫描 | 5 |
| 服务网格 | 5 |
| Bash工具 | 5 |
| 文本处理 | 5 |
| 终端复用 | 5 |
| 边缘AI | 4 |
| 联邦学习 | 4 |
| 模型服务 | 4 |
| Spark计算 | 4 |
| 流处理 | 4 |
| Maven | 4 |
| 容器替代方案 | 4 |
| 性能分析 | 4 |
| ML框架 | 3 |
| 数据湖 | 3 |
| Hadoop生态 | 3 |
| 调度与转换 | 3 |
| Gradle | 3 |
| Make | 3 |
| K8s开发工具 | 3 |
| 本地K8s | 3 |
| 运维操作 | 3 |
| 远程带外管理 | 3 |
| DNS工具 | 3 |
| MLOps平台 | 2 |
| Flink流计算 | 2 |
| Docker高级 | 2 |
| 时序与OLAP | 2 |
| 消息队列 | 1 |
| Pulumi | 1 |
| Terraform | 1 |

## ⚠️ slug 冲突（同 slug 不同命令/领域）

| slug | 出现的命令名 |
|------|--------------|
| ansible-playbook | ansible playbook / ansible-playbook |
| docker-compose | docker compose / docker-compose |
| git-lfs | git lfs / git-lfs |

## 跳过的文件

- `shell/text-processing 2.yaml` — YAML 解析失败: mapping values are not allowed here
  in "/Users/allengaller/Documents/GitHub/standup-coder/cmd-database/tools/cmd/data/shell/text-processing 2.yaml", line 129, column 20

## 抽查样本（代表命令）

| slug | 命令名 | 领域 | 源文件 |
|------|--------|------|--------|
| deepspeed | deepspeed | 大模型训练 | ai/llm-training.yaml |
| accelerate | accelerate | 大模型训练 | ai/llm-training.yaml |
| vllm | vllm | 大模型推理 | ai/llm-inference.yaml |
| sglang | sglang | 大模型推理 | ai/llm-inference.yaml |
| arthas | arthas | Java诊断 | diagnostic/arthas.yaml |
| kubectl | kubectl | Kubernetes命令 | container/k8s/kubernetes.yaml |
| npm | npm | 包管理 | build-tools/pkg-mgmt.yaml |
| mysql | mysql | MySQL工具 | database/mysql.yaml |
| ab | ab | HTTP工具 | network/http.yaml |
| git | _（未在 YAML 中找到）_ | | |
| docker | _（未在 YAML 中找到）_ | | |
| apt-install | apt install | Ubuntu系统命令 | os/ubuntu.yaml |
| helm | _（未在 YAML 中找到）_ | | |
| aider | aider | AI编程 | ai/ai-coding.yaml |
| ansible | ansible | K8s配置管理 | container/k8s/k8s-config.yaml |
| terraform | terraform | Terraform | cloud/terraform.yaml |

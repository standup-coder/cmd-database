# cmd4coder 内容广度与深度差距分析

> 分析时间：2026-07-19（更新于扩充完成后）  
> 分析版本：v1.9.0（1,238 命令 / 123 分类 / 127 个 YAML 数据文件）  
> 基线版本：v1.8.0（1,112 命令 / 106 分类 / 87 个 YAML 数据文件）  
> 本轮净增：+126 命令 / +17 分类 / +21 个 YAML 文件  
> 目标：识别各领域覆盖盲区与深度不足，为内容扩充提供优先级路线图

---

## 1. 现状总览

### 1.1 各领域覆盖密度（v1.9.0 扩充后）

| 领域 | 命令数 | YAML 文件 | 密度评级 | 说明 |
|------|--------|-----------|----------|------|
| container/k8s | 263 | 18 | ★★★★★ | 覆盖极全，17 个子主题 |
| ai | 240 | 24 | ★★★★★ | 22 个 AI 子方向，已完成 3 轮 gap fill |
| os | 160 | 6 | ★★★★☆ | 核心命令齐全，新增 systemd 服务管理 |
| container/docker | 22 | 3 | ★★★★☆ | Docker 本体 + 替代品 + 高级操作 |
| container/cloudnative | 55 | 2 | ★★★★☆ | Istio/Envoy/Linkerd 等已覆盖 |
| database | 67 | 8 | ★★★★☆ | 主流 DB + 运维操作（备份/调优） |
| hardware | 64 | 9 | ★★★★☆ | GPU/IPMI/嵌入式/存储均有 |
| network | 67 | 9 | ★★★★☆ | 基础 + 安全工具 + 服务网格 |
| bigdata | 61 | 12 | ★★★☆☆ | 新增流处理/编排，部分仍为 thin |
| lang | 59 | 8 | ★★★☆☆ | 新增 Python/Go 工具链 |
| cloud | 36 | 7 | ★★★☆☆ | 新增 GCP/Azure/配置管理 |
| vcs | 41 | 3 | ★★★☆☆ | 新增 Git 高级操作 + GitHub CLI |
| diagnostic | 31 | 4 | ★★★☆☆ | 新增性能分析/eBPF 工具 |
| build-tools | 21 | 5 | ★★★☆☆ | 新增 CMake/包管理工具 |
| cicd | 27 | 4 | ★★★☆☆ | 新增 GitOps/平台工具 |
| shell | 24 | 4 | ★★★☆☆ | 新增 tmux/文本处理/现代工具 |

### 1.2 深度评估标准

每条命令的"深度"由以下维度衡量：

| 深度等级 | 标准 |
|----------|------|
| **Stub** | 仅有 name + description，无 options/examples |
| **Thin** | 1-2 个 options，1 个 example |
| **Medium** | 3-5 个 options，2-3 个 examples，有 risks |
| **Deep** | 5+ options，3-5 examples，完整 risks + related_commands + references |

当前分布估算：Deep ~60%，Medium ~25%，Thin/Stub ~15%（集中在 bigdata、cloud、cicd、build-tools）。

---

## 2. 广度差距（按优先级排序）

### P0 — 严重缺失（核心开发运维工具链空白）

#### 2.1 Cloud 云平台（当前 13 条 → 建议 60+）

| 缺失工具 | 重要性 | 建议命令数 | 说明 |
|----------|--------|-----------|------|
| `gcloud` (GCP CLI) | 极高 | 10-12 | 三大云之一，完全缺失 |
| `az` (Azure CLI) | 极高 | 10-12 | 三大云之一，完全缺失 |
| `terraform` | 极高 | 8-10 | 当前仅 1 条，应覆盖 init/plan/apply/state/module/import |
| `pulumi` | 高 | 5-6 | 当前仅 1 条 |
| `kubectl` 云托管扩展 | 高 | 5 | EKS/AKS/GKE 特定操作（已在 k8s-cloud 有 9 条，可补充） |
| `aws` 深度补充 | 高 | 8-10 | 当前 6 条，缺 S3/Lambda/ECS/CloudFormation 深度 |
| `ansible` | 高 | 6-8 | 配置管理核心工具，完全缺失 |
| `packer` | 中 | 3-4 | 镜像构建 |
| `vault` (HashiCorp) | 高 | 5-6 | 密钥管理，完全缺失 |
| `consul` | 中 | 4-5 | 服务发现 |

#### 2.2 CI/CD（当前 9 条 → 建议 45+）

| 缺失工具 | 重要性 | 建议命令数 | 说明 |
|----------|--------|-----------|------|
| `jenkins-cli` / Jenkins Pipeline | 极高 | 6-8 | 企业 CI 占有率第一，完全缺失 |
| `gitlab-ci` (glab CLI) | 高 | 5-6 | GitLab 生态 |
| `argocd` | 极高 | 8-10 | GitOps 标杆，完全缺失 |
| `flux` | 高 | 5-6 | GitOps 另一极 |
| `tekton` (tkn CLI) | 中 | 4-5 | 云原生 CI |
| `drone` | 中 | 3-4 | 轻量 CI |
| `circleci` | 中 | 3-4 | SaaS CI |
| `buildkite` | 低 | 2-3 | |
| `dagger` | 中 | 3-4 | 可编程 CI/CD |
| `goreleaser` | 中 | 3-4 | Go 发布自动化 |

#### 2.3 Shell & 核心工具（当前 5 条 → 建议 40+）

| 缺失工具 | 重要性 | 建议命令数 | 说明 |
|----------|--------|-----------|------|
| `zsh` | 高 | 5-6 | macOS 默认 shell |
| `fish` | 中 | 3-4 | 现代 shell |
| `tmux` | 极高 | 6-8 | 终端复用，运维必备 |
| `screen` | 中 | 3-4 | 经典终端复用 |
| `xargs` / `parallel` | 高 | 4-5 | 并行执行 |
| `jq` / `yq` | 极高 | 6-8 | JSON/YAML 处理，现代运维核心 |
| `sed` / `awk` | 高 | 6-8 | 文本处理双雄 |
| `curl` 深度 | 高 | 5-6 | 当前可能在 network 中，需确认深度 |
| `rsync` | 高 | 3-4 | 文件同步 |
| `cron` / `systemd-timer` | 中 | 3-4 | 定时任务 |

#### 2.4 Build Tools（当前 10 条 → 建议 35+）

| 缺失工具 | 重要性 | 建议命令数 | 说明 |
|----------|--------|-----------|------|
| `make` 深度补充 | 高 | +5 | 当前 3 条，缺 Makefile 调试/模式规则/函数 |
| `cmake` | 高 | 5-6 | C/C++ 构建标准 |
| `bazel` | 中 | 4-5 | Google  monorepo 构建 |
| `ninja` | 中 | 3-4 | 快速构建 |
| `cargo` 深度 | 高 | +4 | 当前在 lang/rust 有 5 条，构建维度不足 |
| `npm`/`pnpm`/`yarn` 深度 | 高 | +6 | 当前在 lang/nodejs 有 10 条，包管理深度不够 |
| `pip`/`uv`/`poetry` | 高 | 5-6 | Python 包管理，当前 python 仅 5 条 |
| `docker buildx` | 高 | 4-5 | 多平台构建 |

### P1 — 明显不足（影响工具完整性）

#### 2.5 BigData（当前 54 条，多 stub → 建议 80+）

| 缺失/不足 | 当前状态 | 建议 |
|-----------|----------|------|
| `kafka` (kafka-topics/kafka-console/kafka-consumer-groups) | 1 条 stub + kafka-cli 5 条 | 补充至 10-12 条 |
| `flink` (flink run/flink list/flink savepoint) | 2 条 thin | 补充至 6-8 条 |
| `spark` (spark-submit/spark-shell/pyspark) | 4 条 | 补充至 8-10 条 |
| `hadoop` (hdfs/yarn/mapred) | 3 条 | 补充至 6-8 条 |
| `airflow` | 完全缺失 | 新增 6-8 条 |
| `dbt` | 完全缺失 | 新增 4-5 条 |
| `presto`/`trino` | 在 query-engines 有 5 条 | 可补充 |
| `clickhouse` | 完全缺失 | 新增 4-5 条 |
| `superset`/`metabase` CLI | 完全缺失 | 新增 3-4 条 |

#### 2.6 VCS / Git 深度（当前 17 条 → 建议 35+）

| 缺失子命令 | 说明 |
|-----------|------|
| `git rebase` (interactive) | 高频操作，当前可能仅一条 |
| `git bisect` | 二分查找 bug |
| `git worktree` | 多工作树 |
| `git stash` 深度 | 高级用法 |
| `git reflog` | 恢复操作 |
| `git cherry-pick` | 选择性合并 |
| `git submodule` / `git subtree` | 依赖管理 |
| `git lfs` | 大文件 |
| `git archive` | 归档导出 |
| `git shortlog` / `git describe` | 版本管理 |
| `gh` (GitHub CLI) 深度 | PR/Issue/Actions/Release 操作 |
| `glab` (GitLab CLI) | 完全缺失 |

#### 2.7 Language 工具链深度（当前 47 条 → 建议 80+）

| 语言 | 当前 | 缺失 |
|------|------|------|
| Python | 5 条 | `uv`、`poetry`、`ruff`、`black`、`mypy`、`pytest`、`tox`、`pyenv` |
| Go | 8 条 | `golangci-lint`、`gopls`、`staticcheck`、`delve`、`pprof`、`go generate` |
| Node.js | 10 条 | `pnpm`、`bun`、`tsx`、`eslint`、`prettier`、`vitest` |
| Rust | 5 条 | `clippy`、`rustfmt`、`cargo-expand`、`cross`、`wasm-pack` |
| Java | 10 条 | `jlink`、`jpackage`、`jshell`、`mvnd`、`sdkman` |
| 缺失语言 | — | `dotnet` CLI、`swift`、`kotlin`/`gradle-kts`、`elixir`/`mix` |

#### 2.8 可观测性 & 诊断（当前 27 条 → 建议 50+）

| 缺失工具 | 重要性 | 说明 |
|----------|--------|------|
| `perf` (Linux perf_events) | 极高 | CPU/内存/IO 性能分析 |
| `bpftrace` / `bcc` | 极高 | eBPF 动态追踪 |
| `strace` / `ltrace` | 高 | 系统调用/库调用追踪 |
| `tcpdump` 深度 | 高 | 当前可能在 network，需确认 |
| `wireshark`/`tshark` | 中 | 协议分析 |
| `flamegraph` | 高 | 火焰图生成 |
| `py-spy` / `async-profiler` | 中 | 语言级 profiler |
| `dtrace` (macOS/Solaris) | 中 | 动态追踪 |
| `sysdig` / `falco` | 中 | 容器级诊断/安全 |
| `pixie` | 中 | K8s 可观测 |

### P2 — 锦上添花（扩展覆盖面）

#### 2.9 安全工具

| 缺失工具 | 说明 |
|----------|------|
| `nmap` 深度 | 当前可能在 network/security |
| `trivy` | 容器/依赖漏洞扫描 |
| `grype` / `syft` | SBOM + 漏洞扫描 |
| `snyk` | 依赖安全 |
| `opa` (Open Policy Agent) | 策略即代码 |
| `cert-manager` (kubectl 扩展) | 证书管理 |
| `age` / `sops` | 加密工具 |

#### 2.10 开发者体验工具

| 缺失工具 | 说明 |
|----------|------|
| `lazygit` / `tig` | Git TUI |
| `fzf` | 模糊搜索 |
| `ripgrep` (rg) / `fd` | 现代搜索 |
| `bat` / `delta` | 现代 cat/diff |
| `httpie` | 现代 HTTP 客户端 |
| `direnv` / `mise` (rtx) | 环境管理 |
| `just` | 现代 make |
| `task` (Taskfile) | 任务运行器 |
| `tilt` / `skaffold` | K8s 开发循环 |
| `kind` / `k3d` 深度 | 本地 K8s（local-k8s 仅 3 条） |

#### 2.11 数据格式 & 序列化

| 缺失工具 | 说明 |
|----------|------|
| `protoc` (Protocol Buffers) | gRPC 生态核心 |
| `flatc` (FlatBuffers) | 零拷贝序列化 |
| `avro-tools` | Kafka 生态 |
| `thrift` | RPC 框架 |
| `cue` | 配置语言 |
| `jsonnet` / `ksonnet` | 配置生成 |

---

## 3. 深度差距（现有条目需加强）

### 3.1 Stub/Thin 文件清单

| 文件 | 当前命令数 | 问题 | 建议 |
|------|-----------|------|------|
| `cloud/terraform.yaml` | 1 | 仅 `terraform` 一条 | 扩展至 8-10 条（init/plan/apply/destroy/state/import/workspace/output） |
| `cloud/pulumi.yaml` | 1 | 仅 `pulumi` 一条 | 扩展至 5-6 条 |
| `bigdata/kafka.yaml` | 1 | stub 级 | 合并至 kafka-cli 或扩展 |
| `bigdata/flink.yaml` | 2 | thin | 扩展至 6-8 条 |
| `bigdata/hadoop.yaml` | 3 | thin | 扩展至 6-8 条 |
| `bigdata/data-lake.yaml` | 3 | thin | 扩展至 5-6 条 |
| `cicd/more.yaml` | 4 | 有空 description 字段 | 修复 + 扩展 |
| `build-tools/make.yaml` | 3 | thin | 扩展至 6-8 条 |
| `build-tools/gradle.yaml` | 3 | thin | 扩展至 5-6 条 |
| `lang/python.yaml` | 5 | 仅覆盖 python 本体 | 新增 python-tooling.yaml |
| `shell/bash.yaml` | 5 | 仅 bash 本体 | 新增 shell-tools.yaml |
| `container/k8s/local-k8s.yaml` | 3 | 仅 kind/minikube/k3d 各一 | 扩展深度 |

### 3.2 深度不足的中等文件

| 文件 | 命令数 | 缺失深度 |
|------|--------|----------|
| `database/mysql.yaml` | 8 | 缺 mysqldump 高级选项、性能调优、复制管理 |
| `database/postgresql.yaml` | 10 | 缺 pg_dump/pg_restore 深度、VACUUM、逻辑复制 |
| `database/redis.yaml` | 11 | 缺 Redis Cluster 操作、Stream、Lua 脚本 |
| `vcs/git.yaml` | 17 | 缺 rebase/bisect/worktree/reflog 等高级操作 |
| `network/http.yaml` | 5 | 缺 HTTP/2、gRPC、WebSocket 调试 |
| `os/ubuntu.yaml` | 20 | 缺 snap/netplan/cloud-init |
| `container/docker/docker.yaml` | 16 | 缺 Buildx/Compose V2/多阶段构建深度 |

### 3.3 Schema 一致性问题

| 问题 | 影响范围 | 修复建议 |
|------|----------|----------|
| category 字段中英混用 | ~30% 文件 | 统一为中文（与 metadata.yaml 一致） |
| risk level 引号不一致 | os/ubuntu.yaml 等 | 统一为不带引号 |
| `references` 字段仅 AI 领域有 | 其他领域缺失 | 为所有领域补充参考链接 |
| `notes` 字段仅个别文件有 | 不统一 | 纳入标准 schema |
| `install_method` 格式不统一 | 部分为命令，部分为描述 | 统一为可执行命令 |
| metadata.yaml 引号风格漂移 | 后半段无引号 | 重新生成 |
| metadata.yaml order 值重复 | 多个 200/300/400 | 重新编号 |

---

## 4. 扩充路线图

### Phase 1：填补核心空白（P0）— ✅ 已完成

| 批次 | 领域 | 新增命令数 | 新增文件 | 状态 |
|------|------|-----------|----------|------|
| 1.1 | Cloud（gcloud/az/ansible/vault/packer） | +23 | `cloud/gcloud.yaml`、`cloud/azure.yaml`、`cloud/config-mgmt.yaml` | ✅ |
| 1.2 | CI/CD（argocd/flux/glab/tekton/dagger） | +18 | `cicd/gitops.yaml`、`cicd/platforms.yaml` | ✅ |
| 1.3 | Shell & 核心工具（tmux/parallel/fzf/rg/bat） | +19 | `shell/tmux.yaml`、`shell/text-processing.yaml`、`shell/modern-tools.yaml` | ✅ |
| 1.4 | Build Tools（ninja/bazel/uv/poetry/pnpm/bun） | +11 | `build-tools/cmake.yaml`、`build-tools/pkg-mgmt.yaml` | ✅ |

### Phase 2：加强深度（P1）— ✅ 已完成

| 批次 | 领域 | 新增命令数 | 方式 | 状态 |
|------|------|-----------|------|------|
| 2.1 | BigData（kafka-topics/flink-sql/airflow/dbt） | +7 | 新增 `bigdata/streaming.yaml`、`bigdata/orchestration.yaml` | ✅ |
| 2.2 | Git 深度 + GitHub CLI | +10 | 新增 `vcs/git-advanced.yaml` | ✅ |
| 2.3 | Language 工具链（ruff/mypy/golangci-lint/dlv） | +10 | 新增 `lang/python-tooling.yaml`、`lang/go-tooling.yaml` | ✅ |
| 2.4 | 可观测性（py-spy/async-profiler/flamegraph） | +4 | 新增 `diagnostic/profiling.yaml` | ✅ |
| 2.5 | Docker 深度（Compose/多阶段构建） | +2 | 新增 `container/docker/docker-advanced.yaml` | ✅ |
| 2.6 | Database 深度（redis-cli高级/mysql调优/psql运维） | +3 | 新增 `database/operations.yaml` | ✅ |
| 2.7 | 安全工具（trivy/opa/conftest/age） | +5 | 新增 `network/security-tools.yaml` | ✅ |

### Phase 3：扩展覆盖（P2）— ✅ 已完成

| 批次 | 领域 | 新增命令数 | 状态 |
|------|------|-----------|------|
| 3.1 | Systemd 服务管理（systemctl/journalctl/timer） | +7 | ✅ `os/systemd.yaml` |
| 3.2 | 服务网格深度（istioctl/linkerd viz/envoy） | +5 | ✅ `network/service-mesh.yaml` |

### 实际成果（v1.9.0）

| 指标 | v1.8.0（基线） | v1.9.0（当前） | 增幅 |
|------|--------------|--------------|------|
| 总命令数 | 1,112 | 1,238 | +126 (+11.3%) |
| 分类数 | 106 | 123 | +17 |
| YAML 文件数 | 87 → 106 | 127 | +21 |
| 验证通过率 | 100% | 100% (127/127) | — |
| 重复命令 | 0 | 0 | — |
| 领域覆盖完整度 | 70% | ~88% | +18% |

### 后续建议（Phase 4，未执行）

| 方向 | 预计命令数 | 说明 |
|------|-----------|------|
| 数据格式（protoc/flatc/cue/jsonnet） | +12 | 序列化/配置语言 |
| 更多语言（dotnet/swift/kotlin/elixir） | +15 | 长尾语言覆盖 |
| 现有 stub 文件深度扩充 | +25 | terraform/pulumi/kafka/flink 原地扩展 |
| Schema 一致性修复 + references 补充 | 全量 | category 统一、risk level 规范化 |
| 开发者体验（lazygit/tig/tilt/skaffold） | +10 | TUI/开发循环工具 |

---

## 5. 质量保障建议

### 5.1 Schema 强化

```yaml
# 建议的标准 Schema（每条命令必须包含）
name: string          # 必填
category: string      # 必填，中文，与 metadata.yaml 一致
description: string   # 必填，一句话描述
usage: list[string]   # 必填，至少 1 条
options:              # 必填，至少 3 个核心选项
  - flag: string
    description: string
examples:             # 必填，至少 2 个实用示例
  - command: string
    description: string
platforms: list[enum] # 必填，linux/darwin/windows/unix
risks:                # 推荐，有风险时必填
  - level: enum       # low/medium/high/critical（不带引号）
    description: string
related_commands: list[string]  # 推荐
install_required: bool          # 必填
install_method: string          # 条件必填（install_required=true 时）
version_check: string           # 推荐
references: list[string]        # 推荐，官方文档链接
notes: string                   # 可选，重要提示/废弃警告
tags: list[string]              # 新增建议，用于搜索增强
difficulty: enum                # 新增建议，basic/intermediate/advanced
```

### 5.2 Validator 增强

- [ ] 校验 category 值必须在 metadata.yaml 中存在
- [ ] 校验 examples 数量 ≥ 2
- [ ] 校验 options 数量 ≥ 3
- [ ] 校验 risk level 枚举值
- [ ] 校验 references URL 格式
- [ ] 检测重复命令名（跨文件）
- [ ] 输出覆盖率报告（每个分类的命令数 vs 预期）

### 5.3 命名规范

- 文件名：`{domain}/{tool-or-topic}.yaml`（小写 kebab-case）
- 禁止 `more.yaml`、`extra.yaml` 作为新增文件名（历史遗留保留）
- 新增命令归入已有文件或按工具名新建，不再使用 catch-all 文件

---

## 6. 与现有 Gap Analysis 的关系

| 已有文档 | 状态 | 本报告的覆盖 |
|----------|------|-------------|
| ai-commands-gap-analysis.md | ✅ 已完成（5→148） | AI 领域不再扩充 |
| ai-commands-gap-analysis-phase2.md | ✅ 已完成（148→~200） | 同上 |
| ai-commands-recommendations.md | ✅ 已完成（compiler/interpretability/federated） | 同上 |
| DEVELOPMENT_PLAN.md | ⚠️ 过时（停在 v1.5.0/474 条） | 本报告取代其路线图功能 |
| PROJECT_STATUS.md | ❌ 严重过时（v1.0.0/5 条） | 建议归档 |

**本报告是首个覆盖全域（非仅 AI）的差距分析。**

---

*路径：`docs/reports/content-gap-analysis.md`*  
*生成时间：2026-07-19*

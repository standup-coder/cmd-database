#!/usr/bin/env python3
"""
generate_best_practices.py
从 data/*.yaml 全量生成 llm-wiki/best-practices/ 最佳实践文档。

每个命令生成一个 bp-<command>.md，包含：
  - 生产环境配置建议
  - 安全加固
  - 性能调优
  - 监控告警
  - 常见反模式
  - 高可用 / 灾备
  - 生产示例
  - 运维 Checklist
"""

import os, sys, re, glob, json
from pathlib import Path
from datetime import date

import yaml

# ── paths ────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(__file__).resolve().parents[2] / "data"  # YAML 源已随 CLI 收敛到 tools/cmd/data
WIKI_DIR = ROOT / "llm-wiki"
BP_DIR = WIKI_DIR / "best-practices"
MAPS_DIR = WIKI_DIR / "00-Maps"
MANIFEST_PATH = WIKI_DIR / "_meta" / "manifest.json"

TODAY = date.today().isoformat()

# ── category → dimension mapping ─────────────────────────────────
CATEGORY_DOMAIN = {
    "操作系统": "system",
    "编程语言": "devtool",
    "诊断工具": "observability",
    "网络工具": "network",
    "容器编排": "container",
    "数据库工具": "database",
    "版本控制": "vcs",
    "构建工具": "build",
    "AI基础设施": "ai-infra",
    "Shell脚本": "shell",
    "CI-CD": "cicd",
    "云平台": "cloud",
}

# risk emoji & label
RISK_BADGE = {
    "low": "🟢 低风险",
    "medium": "🟡 中风险",
    "high": "🟠 高风险",
    "critical": "🔴 严重风险",
}


def safe_filename(name: str) -> str:
    """把命令名转成安全的文件名。"""
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff\-]", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "unknown"


def get_domain(category: str) -> str:
    for prefix, domain in CATEGORY_DOMAIN.items():
        if category.startswith(prefix):
            return domain
    return "general"


def highest_risk(cmd: dict) -> str:
    levels = ["low", "medium", "high", "critical"]
    worst = "low"
    for r in cmd.get("risks", []):
        lvl = r.get("level", "low")
        if levels.index(lvl) > levels.index(worst):
            worst = lvl
    return worst


def has_risk_info(cmd: dict) -> bool:
    return bool(cmd.get("risks"))


# ── domain-specific content generators ───────────────────────────

def _container_prod_config(cmd: dict) -> list[str]:
    tips = []
    opts = {o["flag"] for o in cmd.get("options", [])}
    name = cmd.get("name", "")
    if "docker" in name:
        tips.append("- 生产环境禁止使用 `latest` 标签，固定镜像版本或 digest (`nginx:1.25.3@sha256:...`)")
        tips.append("- 使用 `--read-only` 将根文件系统设为只读，配合 tmpfs 挂载 `/tmp`")
        tips.append("- 设置 `--memory` 和 `--cpus` 资源限制，防止 noisy-neighbor")
        tips.append("- 使用 `--restart=unless-stopped` 或配合 systemd unit 管理容器生命周期")
        if "-d" in opts or "--detach" in opts:
            tips.append("- 后台容器务必配置日志轮转：`--log-opt max-size=10m --log-opt max-file=5`")
        if "-v" in opts or "--volume" in opts:
            tips.append("- 使用 named volume 或 bind mount + `:ro` 最小化写权限")
    elif "kubectl" in name or "helm" in name:
        tips.append("- 所有 Deployment 配置 `resources.requests` 和 `resources.limits`")
        tips.append("- 设置 `PodDisruptionBudget` 保障滚动更新期间的可用性")
        tips.append("- 使用 `NetworkPolicy` 限制 Pod 间网络通信")
        tips.append("- 生产 namespace 启用 `PodSecurityAdmission` enforced 模式")
    elif "kubeadm" in name or "kops" in name or "k3s" in name:
        tips.append("- 控制平面节点至少 3 个以实现 etcd 高可用")
        tips.append("- 启用 etcd 加密 `EncryptionConfiguration` 保护 Secrets")
        tips.append("- 定期执行 CIS Benchmark 扫描集群配置")
    else:
        tips.append("- 生产部署前在 staging 环境充分验证配置")
        tips.append("- 使用 IaC 工具（Terraform/Pulumi）管理资源，避免手动操作")
    return tips


def _database_prod_config(cmd: dict) -> list[str]:
    tips = []
    name = cmd.get("name", "")
    if "mysql" in name:
        tips.append("- 生产环境使用 `innodb_buffer_pool_size` 设为物理内存的 60-80%")
        tips.append("- 启用 `slow_query_log` 并设置 `long_query_time=1` 捕获慢查询")
        tips.append("- 配置 `binlog_format=ROW` + `sync_binlog=1` 保证事务安全")
        tips.append("- 主从复制使用 `semi-sync replication` 减少数据丢失风险")
    elif "redis" in name:
        tips.append("- 生产环境设置 `maxmemory` + `maxmemory-policy` 防止 OOM")
        tips.append("- 启用 `requirepass` 或 ACL 认证，禁止无密码暴露")
        tips.append("- 使用 Sentinel 或 Cluster 模式保障高可用")
        tips.append("- 配置 `tcp-backlog` 和 `timeout` 参数适配高并发场景")
    elif "psql" in name or "pg_" in name:
        tips.append("- 调优 `shared_buffers` (25% RAM)、`work_mem`、`effective_cache_size`")
        tips.append("- 启用 `pg_stat_statements` 扩展监控查询性能")
        tips.append("- 配置流复制 (`streaming replication`) + 自动故障转移")
        tips.append("- 定期 `VACUUM ANALYZE` 或配置 autovacuum 参数")
    else:
        tips.append("- 生产数据库开启 TLS 加密传输")
        tips.append("- 配置自动备份策略并定期验证恢复流程")
    return tips


def _ai_infra_prod_config(cmd: dict) -> list[str]:
    tips = []
    name = cmd.get("name", "")
    if any(kw in name for kw in ["vllm", "sglang", "lmdeploy", "triton", "tgi"]):
        tips.append("- 推理服务前置负载均衡器（Nginx/Envoy），配置请求超时和重试策略")
        tips.append("- 设置 `--max-num-seqs` 限制并发推理数，防止 GPU OOM")
        tips.append("- 监控 GPU 利用率、显存占用、推理延迟 P99，接入 Prometheus")
        tips.append("- 使用 `--tensor-parallel-size` 合理分配 GPU 卡数")
    elif any(kw in name for kw in ["deepspeed", "accelerate", "torchrun"]):
        tips.append("- 训练任务使用 spot/preemptible 实例时配置 checkpoint 自动保存与恢复")
        tips.append("- 使用 WandB/MLflow 记录超参数和训练指标")
        tips.append("- 多节点训练确保 NCCL 网络带宽 ≥ 25Gbps，推荐使用 RoCE/InfiniBand")
    elif any(kw in name for kw in ["ollama", "llama.cpp", "mlx"]):
        tips.append("- 生产环境不要直接暴露 Ollama 端口，前置 API Gateway 做认证和限流")
        tips.append("- 模型文件使用独立存储卷，避免与应用混在一起")
    else:
        tips.append("- GPU 工作负载使用 node selector/taint 调度到专用节点池")
        tips.append("- 配置 GPU 监控 (nvidia-smi → Prometheus exporter)")
    return tips


def _network_prod_config(cmd: dict) -> list[str]:
    return [
        "- 网络诊断命令仅用于排查，不要作为常规监控手段（使用 Prometheus + exporter）",
        "- 生产环境防火墙规则变更需走变更管理流程，先 dry-run 验证",
        "- DNS 查询使用内部 DNS 缓存，避免绕过企业 DNS 策略",
        "- 抓包（tcpdump/Wireshark）需限制范围，避免在高流量环境产生性能问题",
    ]


def _os_prod_config(cmd: dict) -> list[str]:
    return [
        "- 关键系统命令变更（如 sysctl、systemctl）记录到变更管理系统",
        "- 使用 Ansible/Salt 等配置管理工具统一管理系统参数",
        "- 日志文件配置 logrotate 防止磁盘空间耗尽",
        "- 定期执行安全更新，使用 `unattended-upgrades` 或等效工具自动化补丁",
    ]


def _vcs_prod_config(cmd: dict) -> list[str]:
    return [
        "- 生产分支启用分支保护规则，禁止 force-push 和直接提交",
        "- 使用 GPG/SSH 签名提交，保证代码来源可验证",
        "- 大文件使用 Git LFS 管理，避免仓库膨胀",
        "- 配置 pre-commit hooks 执行代码风格检查和安全扫描",
    ]


def _build_prod_config(cmd: dict) -> list[str]:
    return [
        "- CI/CD 构建使用固定版本的依赖，禁止 SNAPSHOT 或 `*` 版本范围",
        "- 构建产物签名并发布到私有制品仓库",
        "- 构建缓存合理配置，避免使用过期缓存导致不可复现的构建",
        "- 构建超时设置为合理上限，防止卡死任务占用资源",
    ]


def _cloud_prod_config(cmd: dict) -> list[str]:
    return [
        "- 所有云资源使用 Terraform/Pulumi 管理，禁止手动控制台操作",
        "- IAM 策略遵循最小权限原则，定期审计权限范围",
        "- 启用 CloudTrail/审计日志记录所有 API 调用",
        "- 关键资源启用删除保护（Deletion Protection）",
    ]


def _cicd_prod_config(cmd: dict) -> list[str]:
    return [
        "- 生产部署流水线必须包含自动化测试、安全扫描和审批步骤",
        "- Secrets 使用 Vault/SSM 管理，禁止明文存储在配置文件中",
        "- 构建镜像使用固定 digest 而非 `latest` 标签",
        "- 配置流水线超时和并发限制，防止资源争抢",
    ]


def _shell_prod_config(cmd: dict) -> list[str]:
    return [
        "- 生产脚本使用 `set -euo pipefail` 确保错误不被忽略",
        "- 敏感信息通过环境变量或 secret 管理，不硬编码在脚本中",
        "- 脚本添加幂等性检查，重复执行不产生副作用",
        "- 长时间运行的脚本配置超时和日志轮转",
    ]


# ── dispatch table ───────────────────────────────────────────────

DOMAIN_PROD_CONFIG = {
    "container": _container_prod_config,
    "database": _database_prod_config,
    "ai-infra": _ai_infra_prod_config,
    "network": _network_prod_config,
    "system": _os_prod_config,
    "devtool": _os_prod_config,
    "vcs": _vcs_prod_config,
    "build": _build_prod_config,
    "cloud": _cloud_prod_config,
    "cicd": _cicd_prod_config,
    "shell": _shell_prod_config,
    "observability": _os_prod_config,
    "general": _os_prod_config,
}


def _gen_security(cmd: dict, domain: str) -> list[str]:
    items = []
    risk = highest_risk(cmd)
    name = cmd.get("name", "")
    for r in cmd.get("risks", []):
        items.append(f"- **{r.get('level', 'medium').upper()}**: {r.get('description', '')}")

    if domain == "container":
        items.append("- 禁止以 `--privileged` 模式运行容器")
        items.append("- 使用非 root 用户运行容器内进程 (`USER appuser`)")
        if "docker" in name:
            items.append("- Docker Socket (`/var/run/docker.sock`) 不得挂载到容器内")
    elif domain == "database":
        items.append("- 数据库连接强制使用 TLS 加密")
        items.append("- 定期轮换数据库凭据，使用 Vault 动态 Secret")
    elif domain == "ai-infra":
        items.append("- 模型服务 API 接入认证（JWT/API Key），禁止匿名访问")
        items.append("- 输入数据做长度和格式校验，防止 Prompt 注入")
    elif domain == "network":
        items.append("- 网络扫描和抓包工具需要特权，使用 capabilities 而非 root")
    elif domain == "cloud":
        items.append("- 使用临时凭证（STS AssumeRole）而非长期 AccessKey")
        items.append("- S3 存储桶默认拒绝公开访问")

    if risk in ("high", "critical"):
        items.insert(0, f"- ⚠️ 此命令风险等级为 **{risk.upper()}**，生产环境使用前必须经过变更审批")
        items.append("- 操作前务必在 staging 环境验证，制定回滚方案")

    if not items:
        items.append("- 遵循最小权限原则，仅授予执行所需的最小权限")
        items.append("- 敏感操作记录审计日志")

    return items


def _gen_performance(cmd: dict, domain: str) -> list[str]:
    items = []
    name = cmd.get("name", "")
    opts = cmd.get("options", [])
    if domain == "container" and "docker" in name:
        items.append("- 使用多阶段构建 (`multi-stage build`) 减小镜像体积")
        items.append("- 合理利用构建缓存，将不常变化的层放在 Dockerfile 前面")
        items.append("- 生产容器使用 Alpine 或 Distroless 基础镜像")
    elif domain == "database":
        items.append("- 连接池配置：最小连接数 ≥ 应用实例数，最大连接数根据数据库 max_connections 合理设置")
        items.append("- 大表操作（ALTER、DELETE）使用分批执行或在线 DDL 工具")
    elif domain == "ai-infra":
        if any(kw in name for kw in ["vllm", "sglang", "lmdeploy", "triton"]):
            items.append("- 启用 KV-Cache 复用（vLLM 的 PagedAttention、SGLang 的 RadixAttention）")
            items.append("- 考虑 Continuous Batching 提升吞吐量")
            items.append("- 量化模型 (AWQ/GPTQ/FP8) 可减少 50-75% 显存，推理延迟增加 <5%")
        else:
            items.append("- GPU 工作负载配置 GPU 分时复用或 MIG 切分")
    elif domain == "network":
        items.append("- 网络诊断命令本身有开销，避免在高负载时执行大量诊断")
    else:
        items.append("- 大数据量操作使用分批或流式处理，避免一次性加载")
        items.append("- 耗时命令考虑后台执行 + 进度通知机制")

    if not items:
        items.append("- 生产环境避免同步阻塞操作，使用异步或后台任务")

    return items


def _gen_monitoring(cmd: dict, domain: str) -> list[str]:
    items = []
    name = cmd.get("name", "")
    if domain == "container":
        if "docker" in name:
            items.append("- 容器指标通过 cAdvisor / Docker stats API 采集")
            items.append("- 关键指标：CPU/Memory 使用率、重启次数、OOM 事件")
        else:
            items.append("- 集群指标通过 kube-state-metrics + node-exporter 采集")
            items.append("- 配置 Prometheus alerting rules：Pod 异常重启、节点 NotReady、PV 空间不足")
    elif domain == "database":
        items.append("- 监控连接数、慢查询数、复制延迟、磁盘使用率")
        items.append("- 配置告警：连接池耗尽、主从延迟 > 5s、磁盘使用率 > 80%")
    elif domain == "ai-infra":
        items.append("- GPU 监控：利用率、显存、温度、ECC 错误（通过 DCGM exporter）")
        if any(kw in name for kw in ["vllm", "sglang", "lmdeploy"]):
            items.append("- 推理服务监控：请求延迟 P50/P95/P99、吞吐量、排队深度")
    elif domain == "network":
        items.append("- 使用 Prometheus blackbox exporter 替代手动网络诊断")
    else:
        items.append("- 关键命令执行结果记录日志，异常时触发告警")

    if not items:
        items.append("- 命令执行耗时和退出码纳入监控，非零退出触发告警")

    return items


def _gen_antipatterns(cmd: dict, domain: str) -> list[str]:
    items = []
    name = cmd.get("name", "")
    risk = highest_risk(cmd)

    if domain == "container" and "docker" in name:
        items.append("- ❌ 使用 `docker exec` 手动修改运行中的容器（应修改 Dockerfile 重新构建）")
        items.append("- ❌ 使用 `latest` 标签部署（镜像内容不可预期，回滚困难）")
        items.append("- ❌ 不设置资源限制运行容器（noisy-neighbor 导致宿主机不稳定）")
    elif domain == "container":
        items.append("- ❌ 手动 `kubectl edit` 修改生产资源（绕过 GitOps 审计链）")
        items.append("- ❌ 使用 `kubectl delete pod` 排查问题（破坏自愈机制，应先 drain）")
    elif domain == "database":
        items.append("- ❌ 在生产库直接执行未经审核的 DDL（应走 schema migration 流程）")
        items.append("- ❌ 使用 root/superuser 连接应用（应创建最小权限的应用专用账号）")
        items.append("- ❌ 关闭 binlog/WAL 提升性能（牺牲恢复能力）")
    elif domain == "ai-infra":
        items.append("- ❌ 推理服务不设置超时（长请求占用 GPU 资源导致后续请求排队）")
        items.append("- ❌ 训练任务不保存 checkpoint（spot 实例抢占导致训练丢失）")
        items.append("- ❌ 模型服务直接暴露公网（应前置 API Gateway + 认证）")
    elif domain == "vcs":
        items.append("- ❌ `git push --force` 到共享分支（覆盖他人提交）")
        items.append("- ❌ 提交密钥或密码到仓库（即使后续删除也保留在历史中）")
    elif domain == "cloud":
        items.append("- ❌ 手动在控制台修改资源（与 IaC 状态漂移）")
        items.append("- ❌ 使用 root 账号日常操作（应使用 IAM 角色 + 临时凭证）")
    else:
        items.append("- ❌ 在生产环境使用 `rm -rf` 等不可逆命令（应先移到临时目录确认后再删除）")
        if risk in ("high", "critical"):
            items.append("- ❌ 未经审批直接执行高风险操作")

    if not items:
        items.append("- ❌ 在不理解命令影响的情况下直接在生产环境执行")

    return items


def _gen_ha_dr(cmd: dict, domain: str) -> list[str]:
    items = []
    name = cmd.get("name", "")
    if domain == "container":
        items.append("- 关键工作负载至少 2 副本，跨可用区调度（`topologySpreadConstraints`）")
        items.append("- 配置 HPA 自动扩缩容应对流量波动")
        if "helm" in name:
            items.append("- Helm release values 文件纳入版本管理，支持快速回滚 (`helm rollback`)")
    elif domain == "database":
        items.append("- 配置自动故障转移（RDS Multi-AZ / Patroni / Redis Sentinel）")
        items.append("- 定期执行备份恢复演练，验证 RTO/RPO 是否满足 SLA")
        items.append("- 备份存储跨区域复制，防止区域级故障")
    elif domain == "ai-infra":
        items.append("- 推理服务部署多副本 + 负载均衡，单点故障自动摘除")
        items.append("- 模型文件存储在共享存储（S3/NFS），多副本可独立加载")
        items.append("- 训练 checkpoint 定期上传到持久化存储，支持断点续训")
    else:
        items.append("- 关键操作使用幂等设计，故障恢复后可安全重试")
        items.append("- 配置文件和脚本纳入版本管理，支持快速恢复")

    return items


def _gen_checklist(cmd: dict, domain: str) -> list[str]:
    risk = highest_risk(cmd)
    items = [
        f"- [ ] 命令风险等级：{RISK_BADGE.get(risk, risk)}",
        "- [ ] 已在 staging 环境验证命令效果",
        "- [ ] 已确认操作范围不会影响其他服务",
    ]
    if risk in ("high", "critical"):
        items.append("- [ ] 已获得变更审批")
        items.append("- [ ] 已制定回滚方案")
        items.append("- [ ] 已通知相关 oncall 人员")
    if domain in ("container", "database", "ai-infra"):
        items.append("- [ ] 已确认备份/快照是最新的")
        items.append("- [ ] 已配置监控告警")
    items.append("- [ ] 执行结果已记录到变更管理系统")
    return items


def _gen_prod_examples(cmd: dict, domain: str) -> list[str]:
    """基于已有 examples 筛选/增强生产示例。"""
    items = []
    for ex in cmd.get("examples", []):
        desc = ex.get("description", "")
        cmdline = ex.get("command", "")
        if any(kw in desc for kw in ["生产", "prod", "部署", "集群", "安全", "高可用"]):
            items.append(f"**{desc}**:\n```bash\n{cmdline}\n```")
    if not items and cmd.get("examples"):
        ex = cmd["examples"][0]
        items.append(f"**{ex.get('description', '基本用法')}**:\n```bash\n{ex.get('command', '')}\n```")
    return items


# ── page renderer ────────────────────────────────────────────────

def render_page(cmd: dict, category: str, source_file: str, known_cmds: set[str] | None = None) -> str:
    name = cmd["name"]
    domain = get_domain(category)
    risk = highest_risk(cmd)
    desc = cmd.get("description", "")
    platforms = cmd.get("platforms", [])
    install = cmd.get("install_method", "")
    related = cmd.get("related_commands", [])
    references = cmd.get("references", [])
    notes = cmd.get("notes", [])
    fname = safe_filename(name)

    config_fn = DOMAIN_PROD_CONFIG.get(domain, DOMAIN_PROD_CONFIG["general"])
    prod_config = config_fn(cmd)
    security = _gen_security(cmd, domain)
    performance = _gen_performance(cmd, domain)
    monitoring = _gen_monitoring(cmd, domain)
    antipatterns = _gen_antipatterns(cmd, domain)
    ha_dr = _gen_ha_dr(cmd, domain)
    checklist = _gen_checklist(cmd, domain)
    prod_examples = _gen_prod_examples(cmd, domain)

    # related wikilinks — only link to pages that actually exist
    if related:
        related_lines = []
        for r in related:
            r_fname = safe_filename(r)
            if known_cmds and r_fname in known_cmds:
                related_lines.append(f"- [[bp-{r_fname}|{r}]]")
            else:
                related_lines.append(f"- {r}")
        related_links = "\n".join(related_lines)
    else:
        related_links = "- (无关联命令)"

    # references
    ref_links = "\n".join(f"- [{r}]({r})" for r in references) if references else "- (无外部参考)"

    # notes section
    notes_section = ""
    if notes:
        notes_items = "\n".join(f"- {n}" for n in notes)
        notes_section = f"\n## 补充说明\n\n{notes_items}\n"

    # tags
    tags = [domain, f"risk-{risk}"]
    for p in platforms[:3]:
        tags.append(p)

    page = f"""---
title: "{name} 生产环境最佳实践"
cmd_name: "{name}"
cmd_category: "{category}"
source_page: "[[{fname}]]"
domain: "{domain}"
risk_level: "{risk}"
platforms: {json.dumps(platforms)}
tags: {json.dumps(tags)}
created: "{TODAY}"
source_file: "{source_file}"
---

# {name} — 生产环境最佳实践

> {desc}

| 属性 | 值 |
|------|------|
| 风险等级 | {RISK_BADGE.get(risk, risk)} |
| 领域 | `{domain}` |
| 平台 | {', '.join(f'`{p}`' for p in platforms) or '—'} |
| 安装 | {install or '系统自带'} |

---

## 生产环境配置

{chr(10).join(prod_config)}

## 安全加固

{chr(10).join(security)}

## 性能调优

{chr(10).join(performance)}

## 监控与告警

{chr(10).join(monitoring)}

## 常见反模式与避坑

{chr(10).join(antipatterns)}

## 高可用与灾备

{chr(10).join(ha_dr)}
{notes_section}
## 生产示例

{chr(10).join(prod_examples) if prod_examples else "- 参考上方配置建议组合使用"}

## 参考链接

{ref_links}

## 关联命令最佳实践

{related_links}

---

## 运维 Checklist

{chr(10).join(checklist)}

---

[[{fname}|命令详情]] | [[best-practices-MOC|最佳实践总索引]]
"""
    return page


def render_moc(categories_cmds: dict) -> str:
    """生成 best-practices-MOC.md 总索引页。"""
    lines = [
        "---",
        'title: "生产环境最佳实践 — 总索引"',
        f'created: "{TODAY}"',
        'tags: ["best-practices", "production", "MOC"]',
        "---",
        "",
        "# 生产环境最佳实践 — 总索引",
        "",
        f"> 共覆盖 **{sum(len(v) for v in categories_cmds.values())}** 个命令的生产环境最佳实践，按 **{len(categories_cmds)}** 个分类组织。",
        "",
        "---",
        "",
    ]
    for cat_name in sorted(categories_cmds.keys()):
        cmds = categories_cmds[cat_name]
        lines.append(f"## {cat_name}")
        lines.append("")
        lines.append(f"共 {len(cmds)} 个命令：")
        lines.append("")
        for c in sorted(cmds, key=lambda x: x["name"]):
            fname = safe_filename(c["name"])
            risk = highest_risk(c)
            badge = RISK_BADGE.get(risk, risk)
            lines.append(f"- [[bp-{fname}|{c['name']}]] {badge}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("[[index|Wiki 首页]]")
    return "\n".join(lines)


# ── main ─────────────────────────────────────────────────────────

def load_all_commands():
    """从 data/ 加载所有 YAML 命令数据。"""
    all_cmds = []
    yaml_files = sorted(glob.glob(str(DATA_DIR / "**" / "*.yaml"), recursive=True))
    for yf in yaml_files:
        if os.path.basename(yf) == "metadata.yaml":
            continue
        with open(yf, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not data or "commands" not in data:
            continue
        rel = os.path.relpath(yf, str(DATA_DIR))
        cat = data.get("category", "未分类")
        for cmd in data["commands"]:
            cmd["_source_file"] = rel
            cmd["_category"] = cat
            all_cmds.append(cmd)
    return all_cmds


def main():
    print("📖 加载命令数据...")
    all_cmds = load_all_commands()
    print(f"   找到 {len(all_cmds)} 个命令")

    BP_DIR.mkdir(parents=True, exist_ok=True)

    # Pre-collect all known command filenames for wikilink validation
    known_cmds = set()
    for cmd in all_cmds:
        name = cmd.get("name", "")
        if name:
            known_cmds.add(safe_filename(name))

    categories_cmds = {}
    generated = 0
    skipped = 0

    print("📝 生成最佳实践文档...")
    for cmd in all_cmds:
        name = cmd.get("name", "")
        if not name:
            skipped += 1
            continue

        cat = cmd["_category"]
        source = cmd["_source_file"]
        fname = f"bp-{safe_filename(name)}.md"
        fpath = BP_DIR / fname

        page = render_page(cmd, cat, source, known_cmds)
        fpath.write_text(page, encoding="utf-8")
        generated += 1

        categories_cmds.setdefault(cat, []).append(cmd)

    print(f"   ✅ 生成 {generated} 个文档")
    if skipped:
        print(f"   ⏭️  跳过 {skipped} 个无效条目")

    print("📋 生成 MOC 索引页...")
    moc = render_moc(categories_cmds)
    (BP_DIR / "best-practices-MOC.md").write_text(moc, encoding="utf-8")
    # Also put in 00-Maps
    (MAPS_DIR / "best-practices-MOC.md").write_text(moc, encoding="utf-8")
    print(f"   ✅ MOC 索引已生成")

    # Update manifest if exists
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        manifest["best_practices_count"] = generated
        manifest["best_practices_generated"] = TODAY
        with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print(f"   ✅ manifest.json 已更新")

    print(f"\n🎉 完成！共生成 {generated} 个最佳实践文档")
    print(f"   输出目录: {BP_DIR}")


if __name__ == "__main__":
    main()

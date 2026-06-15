---
title: "swe-agent 生产环境最佳实践"
cmd_name: "swe-agent"
cmd_category: "AI基础设施/AI编程"
source_page: "[[swe-agent]]"
domain: "ai-infra"
risk_level: "critical"
platforms: ["linux", "darwin"]
tags: ["ai-infra", "risk-critical", "linux", "darwin"]
created: "2026-06-06"
source_file: "ai/ai-coding.yaml"
---

# swe-agent — 生产环境最佳实践

> SWE-Agent自动修复GitHub Issue，分析Issue、编辑代码、运行测试验证修复

| 属性 | 值 |
|------|------|
| 风险等级 | 🔴 严重风险 |
| 领域 | `ai-infra` |
| 平台 | `linux`, `darwin` |
| 安装 | git clone https://github.com/princeton-nlp/SWE-agent.git && pip install -e . |

---

## 生产环境配置

- GPU 工作负载使用 node selector/taint 调度到专用节点池
- 配置 GPU 监控 (nvidia-smi → Prometheus exporter)

## 安全加固

- ⚠️ 此命令风险等级为 **CRITICAL**，生产环境使用前必须经过变更审批
- **CRITICAL**: 执行真实代码修改，需隔离环境
- 模型服务 API 接入认证（JWT/API Key），禁止匿名访问
- 输入数据做长度和格式校验，防止 Prompt 注入
- 操作前务必在 staging 环境验证，制定回滚方案

## 性能调优

- GPU 工作负载配置 GPU 分时复用或 MIG 切分

## 监控与告警

- GPU 监控：利用率、显存、温度、ECC 错误（通过 DCGM exporter）

## 常见反模式与避坑

- ❌ 推理服务不设置超时（长请求占用 GPU 资源导致后续请求排队）
- ❌ 训练任务不保存 checkpoint（spot 实例抢占导致训练丢失）
- ❌ 模型服务直接暴露公网（应前置 API Gateway + 认证）

## 高可用与灾备

- 推理服务部署多副本 + 负载均衡，单点故障自动摘除
- 模型文件存储在共享存储（S3/NFS），多副本可独立加载
- 训练 checkpoint 定期上传到持久化存储，支持断点续训

## 生产示例

**自动修复Django Issue**:
```bash
sweagent run --agent_config config/default.yaml --model_name gpt-4 --data_path https://github.com/django/django/issues/xxxxx
```

## 参考链接

- [https://github.com/princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent)

## 关联命令最佳实践

- [[bp-aider|aider]]
- [[bp-openhands|openhands]]

---

## 运维 Checklist

- [ ] 命令风险等级：🔴 严重风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已获得变更审批
- [ ] 已制定回滚方案
- [ ] 已通知相关 oncall 人员
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[swe-agent|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

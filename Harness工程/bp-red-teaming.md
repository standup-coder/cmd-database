---
title: "red-teaming 生产环境最佳实践"
cmd_name: "red-teaming"
cmd_category: "AI基础设施/Harness工程"
source_page: "[[red-teaming]]"
domain: "ai-infra"
risk_level: "high"
platforms: ["linux", "darwin", "windows"]
tags: ["ai-infra", "risk-high", "linux", "darwin", "windows"]
created: "2026-06-06"
source_file: "ai/harness-engineering.yaml"
---

# red-teaming — 生产环境最佳实践

> PyRIT (Python Risk Identification Toolkit) 微软开源红队测试框架，自动化LLM安全测试

| 属性 | 值 |
|------|------|
| 风险等级 | 🟠 高风险 |
| 领域 | `ai-infra` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | pip install pyrit |

---

## 生产环境配置

- GPU 工作负载使用 node selector/taint 调度到专用节点池
- 配置 GPU 监控 (nvidia-smi → Prometheus exporter)

## 安全加固

- ⚠️ 此命令风险等级为 **HIGH**，生产环境使用前必须经过变更审批
- **HIGH**: 红队测试可能触发安全机制，需授权环境
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

**树形攻击策略红队测试**:
```bash
python red_team.py --strategy tree_of_attacks --target gpt-4 --max_depth 5
```

## 参考链接

- [https://github.com/Azure/PyRIT](https://github.com/Azure/PyRIT)

## 关联命令最佳实践

- [[bp-safety-eval|safety-eval]]
- [[bp-agent-bench|agent-bench]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟠 高风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已获得变更审批
- [ ] 已制定回滚方案
- [ ] 已通知相关 oncall 人员
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[red-teaming|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

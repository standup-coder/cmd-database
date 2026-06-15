---
title: "vllm 生产环境最佳实践"
cmd_name: "vllm"
cmd_category: "AI基础设施/大模型推理"
source_page: "[[vllm]]"
domain: "ai-infra"
risk_level: "medium"
platforms: ["linux", "darwin"]
tags: ["ai-infra", "risk-medium", "linux", "darwin"]
created: "2026-06-06"
source_file: "ai/llm-inference.yaml"
---

# vllm — 生产环境最佳实践

> vLLM高性能大模型推理引擎，采用PagedAttention实现最高24倍吞吐提升

| 属性 | 值 |
|------|------|
| 风险等级 | 🟡 中风险 |
| 领域 | `ai-infra` |
| 平台 | `linux`, `darwin` |
| 安装 | pip install vllm |

---

## 生产环境配置

- 推理服务前置负载均衡器（Nginx/Envoy），配置请求超时和重试策略
- 设置 `--max-num-seqs` 限制并发推理数，防止 GPU OOM
- 监控 GPU 利用率、显存占用、推理延迟 P99，接入 Prometheus
- 使用 `--tensor-parallel-size` 合理分配 GPU 卡数

## 安全加固

- **MEDIUM**: 高并发推理可能耗尽GPU资源
- 模型服务 API 接入认证（JWT/API Key），禁止匿名访问
- 输入数据做长度和格式校验，防止 Prompt 注入

## 性能调优

- 启用 KV-Cache 复用（vLLM 的 PagedAttention、SGLang 的 RadixAttention）
- 考虑 Continuous Batching 提升吞吐量
- 量化模型 (AWQ/GPTQ/FP8) 可减少 50-75% 显存，推理延迟增加 <5%

## 监控与告警

- GPU 监控：利用率、显存、温度、ECC 错误（通过 DCGM exporter）
- 推理服务监控：请求延迟 P50/P95/P99、吞吐量、排队深度

## 常见反模式与避坑

- ❌ 推理服务不设置超时（长请求占用 GPU 资源导致后续请求排队）
- ❌ 训练任务不保存 checkpoint（spot 实例抢占导致训练丢失）
- ❌ 模型服务直接暴露公网（应前置 API Gateway + 认证）

## 高可用与灾备

- 推理服务部署多副本 + 负载均衡，单点故障自动摘除
- 模型文件存储在共享存储（S3/NFS），多副本可独立加载
- 训练 checkpoint 定期上传到持久化存储，支持断点续训

## 生产示例

**2卡张量并行部署LLaMA-3.1-8B**:
```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 2
```
**8卡部署Qwen2-72B，支持32K上下文**:
```bash
vllm serve Qwen/Qwen2-72B --tensor-parallel-size 8 --max-model-len 32768
```
**AWQ量化部署，节省显存**:
```bash
vllm serve TheBloke/Llama-2-70B-AWQ --quantization awq --gpu-memory-utilization 0.9
```

## 参考链接

- [https://docs.vllm.ai/](https://docs.vllm.ai/)

## 关联命令最佳实践

- [[bp-sglang|sglang]]
- [[bp-lmdeploy|lmdeploy]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟡 中风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[vllm|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

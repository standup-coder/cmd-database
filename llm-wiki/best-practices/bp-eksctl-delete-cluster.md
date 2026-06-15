---
title: "eksctl delete cluster 生产环境最佳实践"
cmd_name: "eksctl delete cluster"
cmd_category: "容器编排/K8s云平台工具"
source_page: "[[eksctl-delete-cluster]]"
domain: "container"
risk_level: "critical"
platforms: ["linux", "darwin", "windows"]
tags: ["container", "risk-critical", "linux", "darwin", "windows"]
created: "2026-06-06"
source_file: "container/k8s-cloud.yaml"
---

# eksctl delete cluster — 生产环境最佳实践

> Delete AWS EKS cluster

| 属性 | 值 |
|------|------|
| 风险等级 | 🔴 严重风险 |
| 领域 | `container` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | Download from https://eksctl.io/introduction/#installation |

---

## 生产环境配置

- 生产部署前在 staging 环境充分验证配置
- 使用 IaC 工具（Terraform/Pulumi）管理资源，避免手动操作

## 安全加固

- ⚠️ 此命令风险等级为 **CRITICAL**，生产环境使用前必须经过变更审批
- **CRITICAL**: Permanently deletes cluster and all resources
- **CRITICAL**: Cannot be undone; backup data before deleting
- 禁止以 `--privileged` 模式运行容器
- 使用非 root 用户运行容器内进程 (`USER appuser`)
- 操作前务必在 staging 环境验证，制定回滚方案

## 性能调优

- 大数据量操作使用分批或流式处理，避免一次性加载
- 耗时命令考虑后台执行 + 进度通知机制

## 监控与告警

- 集群指标通过 kube-state-metrics + node-exporter 采集
- 配置 Prometheus alerting rules：Pod 异常重启、节点 NotReady、PV 空间不足

## 常见反模式与避坑

- ❌ 手动 `kubectl edit` 修改生产资源（绕过 GitOps 审计链）
- ❌ 使用 `kubectl delete pod` 排查问题（破坏自愈机制，应先 drain）

## 高可用与灾备

- 关键工作负载至少 2 副本，跨可用区调度（`topologySpreadConstraints`）
- 配置 HPA 自动扩缩容应对流量波动

## 生产示例

**Delete EKS cluster**:
```bash
eksctl delete cluster --name my-cluster
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- (无关联命令)

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

[[eksctl-delete-cluster|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

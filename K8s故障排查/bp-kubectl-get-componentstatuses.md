---
title: "kubectl get componentstatuses 生产环境最佳实践"
cmd_name: "kubectl get componentstatuses"
cmd_category: "容器编排/K8s故障排查"
source_page: "[[kubectl-get-componentstatuses]]"
domain: "container"
risk_level: "low"
platforms: ["linux", "darwin", "windows"]
tags: ["container", "risk-low", "linux", "darwin", "windows"]
created: "2026-06-06"
source_file: "container/k8s-troubleshooting.yaml"
---

# kubectl get componentstatuses — 生产环境最佳实践

> 检查 Kubernetes 控制平面组件健康状态

| 属性 | 值 |
|------|------|
| 风险等级 | 🟢 低风险 |
| 领域 | `container` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | kubectl 内置命令 |

---

## 生产环境配置

- 所有 Deployment 配置 `resources.requests` 和 `resources.limits`
- 设置 `PodDisruptionBudget` 保障滚动更新期间的可用性
- 使用 `NetworkPolicy` 限制 Pod 间网络通信
- 生产 namespace 启用 `PodSecurityAdmission` enforced 模式

## 安全加固

- **LOW**: 只读健康检查；无修改风险
- 禁止以 `--privileged` 模式运行容器
- 使用非 root 用户运行容器内进程 (`USER appuser`)

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

**检查控制平面组件状态**:
```bash
kubectl get cs
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- (无关联命令)

---

## 运维 Checklist

- [ ] 命令风险等级：🟢 低风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[kubectl-get-componentstatuses|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

---
title: "aws configure 生产环境最佳实践"
cmd_name: "aws configure"
cmd_category: "云平台/AWS CLI"
source_page: "[[aws-configure]]"
domain: "cloud"
risk_level: "high"
platforms: ["linux", "darwin", "windows"]
tags: ["cloud", "risk-high", "linux", "darwin", "windows"]
created: "2026-06-06"
source_file: "cloud/aws-cli.yaml"
---

# aws configure — 生产环境最佳实践

> 配置 AWS CLI 凭证和默认设置

| 属性 | 值 |
|------|------|
| 风险等级 | 🟠 高风险 |
| 领域 | `cloud` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | 同 aws cli |

---

## 生产环境配置

- 所有云资源使用 Terraform/Pulumi 管理，禁止手动控制台操作
- IAM 策略遵循最小权限原则，定期审计权限范围
- 启用 CloudTrail/审计日志记录所有 API 调用
- 关键资源启用删除保护（Deletion Protection）

## 安全加固

- ⚠️ 此命令风险等级为 **HIGH**，生产环境使用前必须经过变更审批
- **HIGH**: 凭证明文存储在 ~/.aws/credentials，确保文件权限为 600
- 使用临时凭证（STS AssumeRole）而非长期 AccessKey
- S3 存储桶默认拒绝公开访问
- 操作前务必在 staging 环境验证，制定回滚方案

## 性能调优

- 大数据量操作使用分批或流式处理，避免一次性加载
- 耗时命令考虑后台执行 + 进度通知机制

## 监控与告警

- 关键命令执行结果记录日志，异常时触发告警

## 常见反模式与避坑

- ❌ 手动在控制台修改资源（与 IaC 状态漂移）
- ❌ 使用 root 账号日常操作（应使用 IAM 角色 + 临时凭证）

## 高可用与灾备

- 关键操作使用幂等设计，故障恢复后可安全重试
- 配置文件和脚本纳入版本管理，支持快速恢复

## 生产示例

**配置生产环境凭证**:
```bash
aws configure --profile production
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-aws|aws]]
- [[bp-aws-sts|aws sts]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟠 高风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已获得变更审批
- [ ] 已制定回滚方案
- [ ] 已通知相关 oncall 人员
- [ ] 执行结果已记录到变更管理系统

---

[[aws-configure|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

---
title: "gh action 生产环境最佳实践"
cmd_name: "gh action"
cmd_category: "CI-CD/GitHub Actions"
source_page: "[[gh-action]]"
domain: "cicd"
risk_level: "low"
platforms: ["linux", "darwin", "windows"]
tags: ["cicd", "risk-low", "linux", "darwin", "windows"]
created: "2026-06-06"
source_file: "cicd/github-actions.yaml"
---

# gh action — 生产环境最佳实践

> 管理 GitHub Actions

| 属性 | 值 |
|------|------|
| 风险等级 | 🟢 低风险 |
| 领域 | `cicd` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | brew install gh (macOS) 或 apt install gh (Ubuntu) |

---

## 生产环境配置

- 生产部署流水线必须包含自动化测试、安全扫描和审批步骤
- Secrets 使用 Vault/SSM 管理，禁止明文存储在配置文件中
- 构建镜像使用固定 digest 而非 `latest` 标签
- 配置流水线超时和并发限制，防止资源争抢

## 安全加固

- 遵循最小权限原则，仅授予执行所需的最小权限
- 敏感操作记录审计日志

## 性能调优

- 大数据量操作使用分批或流式处理，避免一次性加载
- 耗时命令考虑后台执行 + 进度通知机制

## 监控与告警

- 关键命令执行结果记录日志，异常时触发告警

## 常见反模式与避坑

- ❌ 在生产环境使用 `rm -rf` 等不可逆命令（应先移到临时目录确认后再删除）

## 高可用与灾备

- 关键操作使用幂等设计，故障恢复后可安全重试
- 配置文件和脚本纳入版本管理，支持快速恢复

## 生产示例

**列出仓库中可用的 Actions**:
```bash
gh action list
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-gh-workflow|gh workflow]]
- [[bp-gh-run|gh run]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟢 低风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 执行结果已记录到变更管理系统

---

[[gh-action|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

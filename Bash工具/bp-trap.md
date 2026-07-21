---
title: "trap 生产环境最佳实践"
cmd_name: "trap"
cmd_category: "Shell脚本/Bash工具"
source_page: "[[trap]]"
domain: "shell"
risk_level: "low"
platforms: ["linux", "darwin"]
tags: ["shell", "risk-low", "linux", "darwin"]
created: "2026-06-06"
source_file: "shell/bash.yaml"
---

# trap — 生产环境最佳实践

> 捕获信号并在脚本中执行清理操作

| 属性 | 值 |
|------|------|
| 风险等级 | 🟢 低风险 |
| 领域 | `shell` |
| 平台 | `linux`, `darwin` |
| 安装 | 系统自带 |

---

## 生产环境配置

- 生产脚本使用 `set -euo pipefail` 确保错误不被忽略
- 敏感信息通过环境变量或 secret 管理，不硬编码在脚本中
- 脚本添加幂等性检查，重复执行不产生副作用
- 长时间运行的脚本配置超时和日志轮转

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

**脚本退出时清理临时文件**:
```bash
trap 'rm -f $tmpfile' EXIT
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-bash|bash]]
- [[bp-kill|kill]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟢 低风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 执行结果已记录到变更管理系统

---

[[trap|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

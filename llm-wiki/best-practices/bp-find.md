---
title: "find 生产环境最佳实践"
cmd_name: "find"
cmd_category: "操作系统/通用Linux命令"
source_page: "[[find]]"
domain: "system"
risk_level: "high"
platforms: ["linux", "darwin", "unix"]
tags: ["system", "risk-high", "linux", "darwin", "unix"]
created: "2026-06-06"
source_file: "os/common.yaml"
---

# find — 生产环境最佳实践

> 在目录树中搜索文件

| 属性 | 值 |
|------|------|
| 风险等级 | 🟠 高风险 |
| 领域 | `system` |
| 平台 | `linux`, `darwin`, `unix` |
| 安装 | 系统自带 |

---

## 生产环境配置

- 关键系统命令变更（如 sysctl、systemctl）记录到变更管理系统
- 使用 Ansible/Salt 等配置管理工具统一管理系统参数
- 日志文件配置 logrotate 防止磁盘空间耗尽
- 定期执行安全更新，使用 `unattended-upgrades` 或等效工具自动化补丁

## 安全加固

- ⚠️ 此命令风险等级为 **HIGH**，生产环境使用前必须经过变更审批
- **HIGH**: 使用-delete选项可能误删重要文件，建议先用-print预览
- **MEDIUM**: 在大目录树中搜索可能消耗大量系统资源
- 操作前务必在 staging 环境验证，制定回滚方案

## 性能调优

- 大数据量操作使用分批或流式处理，避免一次性加载
- 耗时命令考虑后台执行 + 进度通知机制

## 监控与告警

- 关键命令执行结果记录日志，异常时触发告警

## 常见反模式与避坑

- ❌ 在生产环境使用 `rm -rf` 等不可逆命令（应先移到临时目录确认后再删除）
- ❌ 未经审批直接执行高风险操作

## 高可用与灾备

- 关键操作使用幂等设计，故障恢复后可安全重试
- 配置文件和脚本纳入版本管理，支持快速恢复

## 补充说明

- find命令功能强大但要小心使用-delete选项
- 使用-exec时，{}代表找到的文件名

## 生产示例

**在当前目录下查找所有.log文件**:
```bash
find . -name '*.log'
```

## 参考链接

- [https://man7.org/linux/man-pages/man1/find.1.html](https://man7.org/linux/man-pages/man1/find.1.html)

## 关联命令最佳实践

- [[bp-locate|locate]]
- [[bp-which|which]]
- [[bp-whereis|whereis]]

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

[[find|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

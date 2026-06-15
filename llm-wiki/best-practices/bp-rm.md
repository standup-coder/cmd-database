---
title: "rm 生产环境最佳实践"
cmd_name: "rm"
cmd_category: "操作系统/通用Linux命令"
source_page: "[[rm]]"
domain: "system"
risk_level: "critical"
platforms: ["linux", "darwin", "unix"]
tags: ["system", "risk-critical", "linux", "darwin", "unix"]
created: "2026-06-06"
source_file: "os/common.yaml"
---

# rm — 生产环境最佳实践

> 删除文件或目录

| 属性 | 值 |
|------|------|
| 风险等级 | 🔴 严重风险 |
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

- ⚠️ 此命令风险等级为 **CRITICAL**，生产环境使用前必须经过变更审批
- **CRITICAL**: rm -rf可能导致数据永久丢失，使用前必须仔细确认路径
- **CRITICAL**: 绝对不要执行'rm -rf /'命令，会删除整个系统
- **HIGH**: 使用通配符时要格外小心，可能匹配到不想删除的文件
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

- 删除的文件无法恢复，使用前务必确认
- 不要在根目录(/)使用rm -rf命令
- 建议使用-i选项进行确认

## 生产示例

**删除单个文件**:
```bash
rm file.txt
```

## 参考链接

- [https://man7.org/linux/man-pages/man1/rm.1.html](https://man7.org/linux/man-pages/man1/rm.1.html)

## 关联命令最佳实践

- [[bp-rmdir|rmdir]]
- [[bp-trash|trash]]
- [[bp-mv|mv]]

---

## 运维 Checklist

- [ ] 命令风险等级：🔴 严重风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已获得变更审批
- [ ] 已制定回滚方案
- [ ] 已通知相关 oncall 人员
- [ ] 执行结果已记录到变更管理系统

---

[[rm|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

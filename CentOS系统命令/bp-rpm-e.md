---
title: "rpm -e 生产环境最佳实践"
cmd_name: "rpm -e"
cmd_category: "操作系统/CentOS系统命令"
source_page: "[[rpm-e]]"
domain: "system"
risk_level: "high"
platforms: ["linux"]
tags: ["system", "risk-high", "linux"]
created: "2026-06-06"
source_file: "os/centos.yaml"
---

# rpm -e — 生产环境最佳实践

> Erase (remove) installed package

| 属性 | 值 |
|------|------|
| 风险等级 | 🟠 高风险 |
| 领域 | `system` |
| 平台 | `linux` |
| 安装 | Pre-installed on CentOS/RHEL |

---

## 生产环境配置

- 关键系统命令变更（如 sysctl、systemctl）记录到变更管理系统
- 使用 Ansible/Salt 等配置管理工具统一管理系统参数
- 日志文件配置 logrotate 防止磁盘空间耗尽
- 定期执行安全更新，使用 `unattended-upgrades` 或等效工具自动化补丁

## 安全加固

- ⚠️ 此命令风险等级为 **HIGH**，生产环境使用前必须经过变更审批
- **HIGH**: May break dependencies; use yum remove instead
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

## 生产示例

**Remove nginx package**:
```bash
sudo rpm -e nginx
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- (无关联命令)

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

[[rpm-e|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

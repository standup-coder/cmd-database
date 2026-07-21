---
title: "mysqladmin 生产环境最佳实践"
cmd_name: "mysqladmin"
cmd_category: "数据库工具/MySQL工具"
source_page: "[[mysqladmin]]"
domain: "database"
risk_level: "critical"
platforms: ["linux", "darwin", "windows"]
tags: ["database", "risk-critical", "linux", "darwin", "windows"]
created: "2026-06-06"
source_file: "database/mysql.yaml"
---

# mysqladmin — 生产环境最佳实践

> MySQL server administration utility

| 属性 | 值 |
|------|------|
| 风险等级 | 🔴 严重风险 |
| 领域 | `database` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | Included with MySQL Server installation |

---

## 生产环境配置

- 生产环境使用 `innodb_buffer_pool_size` 设为物理内存的 60-80%
- 启用 `slow_query_log` 并设置 `long_query_time=1` 捕获慢查询
- 配置 `binlog_format=ROW` + `sync_binlog=1` 保证事务安全
- 主从复制使用 `semi-sync replication` 减少数据丢失风险

## 安全加固

- ⚠️ 此命令风险等级为 **CRITICAL**，生产环境使用前必须经过变更审批
- **CRITICAL**: Can shutdown server or drop databases; use with extreme caution
- **HIGH**: Administrative commands can affect all users and databases
- 数据库连接强制使用 TLS 加密
- 定期轮换数据库凭据，使用 Vault 动态 Secret
- 操作前务必在 staging 环境验证，制定回滚方案

## 性能调优

- 连接池配置：最小连接数 ≥ 应用实例数，最大连接数根据数据库 max_connections 合理设置
- 大表操作（ALTER、DELETE）使用分批执行或在线 DDL 工具

## 监控与告警

- 监控连接数、慢查询数、复制延迟、磁盘使用率
- 配置告警：连接池耗尽、主从延迟 > 5s、磁盘使用率 > 80%

## 常见反模式与避坑

- ❌ 在生产库直接执行未经审核的 DDL（应走 schema migration 流程）
- ❌ 使用 root/superuser 连接应用（应创建最小权限的应用专用账号）
- ❌ 关闭 binlog/WAL 提升性能（牺牲恢复能力）

## 高可用与灾备

- 配置自动故障转移（RDS Multi-AZ / Patroni / Redis Sentinel）
- 定期执行备份恢复演练，验证 RTO/RPO 是否满足 SLA
- 备份存储跨区域复制，防止区域级故障

## 生产示例

**Display server status**:
```bash
mysqladmin -u root -p status
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

[[mysqladmin|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

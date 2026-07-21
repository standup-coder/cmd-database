---
title: "dig 生产环境最佳实践"
cmd_name: "dig"
cmd_category: "网络工具/DNS工具"
source_page: "[[dig]]"
domain: "network"
risk_level: "low"
platforms: ["linux", "darwin", "unix"]
tags: ["network", "risk-low", "linux", "darwin", "unix"]
created: "2026-06-06"
source_file: "network/dns.yaml"
---

# dig — 生产环境最佳实践

> DNS查询工具

| 属性 | 值 |
|------|------|
| 风险等级 | 🟢 低风险 |
| 领域 | `network` |
| 平台 | `linux`, `darwin`, `unix` |
| 安装 | apt install dnsutils (Ubuntu) 或 yum install bind-utils (CentOS) |

---

## 生产环境配置

- 网络诊断命令仅用于排查，不要作为常规监控手段（使用 Prometheus + exporter）
- 生产环境防火墙规则变更需走变更管理流程，先 dry-run 验证
- DNS 查询使用内部 DNS 缓存，避免绕过企业 DNS 策略
- 抓包（tcpdump/Wireshark）需限制范围，避免在高流量环境产生性能问题

## 安全加固

- **LOW**: 常规操作，无特殊风险
- 网络扫描和抓包工具需要特权，使用 capabilities 而非 root

## 性能调优

- 网络诊断命令本身有开销，避免在高负载时执行大量诊断

## 监控与告警

- 使用 Prometheus blackbox exporter 替代手动网络诊断

## 常见反模式与避坑

- ❌ 在生产环境使用 `rm -rf` 等不可逆命令（应先移到临时目录确认后再删除）

## 高可用与灾备

- 关键操作使用幂等设计，故障恢复后可安全重试
- 配置文件和脚本纳入版本管理，支持快速恢复

## 生产示例

**查询域名A记录**:
```bash
dig example.com
```

## 参考链接

- [https://linux.die.net/man/1/dig](https://linux.die.net/man/1/dig)

## 关联命令最佳实践

- [[bp-nslookup|nslookup]]
- [[bp-host|host]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟢 低风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 执行结果已记录到变更管理系统

---

[[dig|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

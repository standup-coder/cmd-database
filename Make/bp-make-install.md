---
title: "make install 生产环境最佳实践"
cmd_name: "make install"
cmd_category: "构建工具/Make"
source_page: "[[make-install]]"
domain: "build"
risk_level: "high"
platforms: ["linux", "darwin"]
tags: ["build", "risk-high", "linux", "darwin"]
created: "2026-06-06"
source_file: "build/make.yaml"
---

# make install — 生产环境最佳实践

> 安装已编译的程序到系统目录（通常为 /usr/local）

| 属性 | 值 |
|------|------|
| 风险等级 | 🟠 高风险 |
| 领域 | `build` |
| 平台 | `linux`, `darwin` |
| 安装 | 系统自带 |

---

## 生产环境配置

- CI/CD 构建使用固定版本的依赖，禁止 SNAPSHOT 或 `*` 版本范围
- 构建产物签名并发布到私有制品仓库
- 构建缓存合理配置，避免使用过期缓存导致不可复现的构建
- 构建超时设置为合理上限，防止卡死任务占用资源

## 安全加固

- ⚠️ 此命令风险等级为 **HIGH**，生产环境使用前必须经过变更审批
- **HIGH**: 需要 root 权限，可能覆盖系统文件
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

**安装到默认目录 /usr/local**:
```bash
make install
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

[[make-install|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

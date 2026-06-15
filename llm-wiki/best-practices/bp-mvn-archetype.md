---
title: "mvn archetype 生产环境最佳实践"
cmd_name: "mvn archetype"
cmd_category: "构建工具/Maven"
source_page: "[[mvn-archetype]]"
domain: "build"
risk_level: "low"
platforms: ["linux", "darwin", "windows"]
tags: ["build", "risk-low", "linux", "darwin", "windows"]
created: "2026-06-06"
source_file: "build/maven.yaml"
---

# mvn archetype — 生产环境最佳实践

> Maven 项目原型生成工具

| 属性 | 值 |
|------|------|
| 风险等级 | 🟢 低风险 |
| 领域 | `build` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | 同 mvn |

---

## 生产环境配置

- CI/CD 构建使用固定版本的依赖，禁止 SNAPSHOT 或 `*` 版本范围
- 构建产物签名并发布到私有制品仓库
- 构建缓存合理配置，避免使用过期缓存导致不可复现的构建
- 构建超时设置为合理上限，防止卡死任务占用资源

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

**生成 Maven 快速启动项目**:
```bash
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart
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
- [ ] 执行结果已记录到变更管理系统

---

[[mvn-archetype|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

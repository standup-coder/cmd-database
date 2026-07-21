---
title: "docker rm 生产环境最佳实践"
cmd_name: "docker rm"
cmd_category: "容器编排/Docker命令"
source_page: "[[docker-rm]]"
domain: "container"
risk_level: "medium"
platforms: ["linux", "darwin", "windows"]
tags: ["container", "risk-medium", "linux", "darwin", "windows"]
created: "2026-06-06"
source_file: "container/docker.yaml"
---

# docker rm — 生产环境最佳实践

> 删除容器

| 属性 | 值 |
|------|------|
| 风险等级 | 🟡 中风险 |
| 领域 | `container` |
| 平台 | `linux`, `darwin`, `windows` |
| 安装 | 参考 https://docs.docker.com/engine/install/ |

---

## 生产环境配置

- 生产环境禁止使用 `latest` 标签，固定镜像版本或 digest (`nginx:1.25.3@sha256:...`)
- 使用 `--read-only` 将根文件系统设为只读，配合 tmpfs 挂载 `/tmp`
- 设置 `--memory` 和 `--cpus` 资源限制，防止 noisy-neighbor
- 使用 `--restart=unless-stopped` 或配合 systemd unit 管理容器生命周期
- 使用 named volume 或 bind mount + `:ro` 最小化写权限

## 安全加固

- **MEDIUM**: 删除容器会丢失容器内的数据(除非使用卷)
- 禁止以 `--privileged` 模式运行容器
- 使用非 root 用户运行容器内进程 (`USER appuser`)
- Docker Socket (`/var/run/docker.sock`) 不得挂载到容器内

## 性能调优

- 使用多阶段构建 (`multi-stage build`) 减小镜像体积
- 合理利用构建缓存，将不常变化的层放在 Dockerfile 前面
- 生产容器使用 Alpine 或 Distroless 基础镜像

## 监控与告警

- 容器指标通过 cAdvisor / Docker stats API 采集
- 关键指标：CPU/Memory 使用率、重启次数、OOM 事件

## 常见反模式与避坑

- ❌ 使用 `docker exec` 手动修改运行中的容器（应修改 Dockerfile 重新构建）
- ❌ 使用 `latest` 标签部署（镜像内容不可预期，回滚困难）
- ❌ 不设置资源限制运行容器（noisy-neighbor 导致宿主机不稳定）

## 高可用与灾备

- 关键工作负载至少 2 副本，跨可用区调度（`topologySpreadConstraints`）
- 配置 HPA 自动扩缩容应对流量波动

## 生产示例

**删除已停止的容器**:
```bash
docker rm my-container
```

## 参考链接

- (无外部参考)

## 关联命令最佳实践

- [[bp-docker-rmi|docker rmi]]
- [[bp-docker-ps|docker ps]]

---

## 运维 Checklist

- [ ] 命令风险等级：🟡 中风险
- [ ] 已在 staging 环境验证命令效果
- [ ] 已确认操作范围不会影响其他服务
- [ ] 已确认备份/快照是最新的
- [ ] 已配置监控告警
- [ ] 执行结果已记录到变更管理系统

---

[[docker-rm|命令详情]] | [[best-practices-MOC|最佳实践总索引]]

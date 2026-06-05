---
cmd_name: openhands
cmd_category: AI基础设施/AI编程
cmd_dimension: AI编程
cmd_install: docker pull ghcr.io/all-hands-ai/runtime
cmd_platforms:
- linux
- darwin
- windows
summary: "OpenHands (原OpenDevin) 开源AI软件工程师，自主完成开发任务，支持多Agent协作"
cmd_level: advanced
cmd_related:
- aider
- swe-agent
cmd_tags:
- agent
- advanced
- linux
- open-source
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/ai/ai-coding.yaml
---


# openhands

> OpenHands (原OpenDevin) 开源AI软件工程师，自主完成开发任务，支持多Agent协作

## 安装

```bash
docker pull ghcr.io/all-hands-ai/runtime
```

## 用法

```
docker run [OPTIONS] ghcr.io/all-hands-ai/runtime
```

```
make build && make run
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | 任务名称 |
| `WORKSPACE_MOUNT_PATH` | 工作目录挂载 |

## 示例

### 示例 1: Docker Compose启动OpenHands

```bash
WORKSPACE_BASE=$(pwd) docker compose up
```

### 示例 2: 命令行指定任务

```bash
python -m openhands.core.main -t 'Implement a REST API for user authentication'
```

## 关联命令

- [[aider]]
- [[swe-agent]]

## 风险提示

> ⚠️ **CRITICAL**: AI自主执行命令需沙箱隔离，防止破坏系统

## 参考链接

- [https://github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)

## 所属维度

[[AI编程-MOC|AI基础设施/AI编程]]

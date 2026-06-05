---
cmd_name: kill
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related: []
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 向进程发送信号以终止或控制
created: '2026-06-04'
source_file: data/os/common.yaml
---
# kill

> 向进程发送信号以终止或控制

## 安装

```bash
已预装
```

## 用法

```
kill [信号] PID...
```

## 参数

| Flag | Description |
|------|-------------|
| `-9` | SIGKILL，强制终止（不可捕获） |
| `-15` | SIGTERM，优雅终止（默认） |
| `-l` | 列出所有信号名称 |

## 示例

### 优雅终止PID 1234

```bash
kill 1234
```

### 强制终止PID 1234

```bash
kill -9 1234
```

### 列出所有可用信号

```bash
kill -l
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]

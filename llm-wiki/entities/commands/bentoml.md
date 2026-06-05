---
cmd_name: bentoml
cmd_category: AI基础设施/模型服务
cmd_dimension: 模型服务
cmd_install: pip install bentoml
cmd_platforms:
- linux
- darwin
- windows
summary: "BentoML 命令行客户端，用于模型打包和服务"
cmd_level: intermediate
cmd_related:
- mlflow
- torchrun
cmd_tags:
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/model-serving.yaml
---


# bentoml

> BentoML 命令行客户端，用于模型打包和服务

## 安装

```bash
pip install bentoml
```

## 用法

```
bentoml [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `serve` | 启动BentoML服务 |
| `build` | 从bentofile.yaml构建一个Bento |
| `models` | 管理本地模型库 (list, get, delete, import, export) |
| `containerize` | 将Bento打包成Docker镜像 |

## 示例

### 示例 1: 启动最新的'my_service'服务

```bash
bentoml serve my_service:latest
```

### 示例 2: 根据当前目录的bentofile.yaml构建Bento

```bash
bentoml build
```

### 示例 3: 列出所有本地保存的模型

```bash
bentoml models list
```

### 示例 4: 将Bento打包为Docker镜像

```bash
bentoml containerize my_service:latest -t my_service_image:1.0
```

## 关联命令

- [[mlflow]]
- [[torchrun]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 参考链接

- [https://docs.bentoml.com/en/latest/reference/cli.html](https://docs.bentoml.com/en/latest/reference/cli.html)

## 所属维度

[[模型服务-MOC|AI基础设施/模型服务]]

---
cmd_name: torchserve
cmd_category: AI基础设施/模型服务
cmd_dimension: 模型服务
cmd_install: pip install torchserve torch-model-archiver
cmd_platforms:
- linux
- darwin
- windows
summary: "PyTorch官方模型服务框架，支持模型打包、A/B测试、多模型服务、自定义处理器"
cmd_level: intermediate
cmd_related:
- bentoml
- tritonserver
cmd_tags:
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/model-serving.yaml
---


# torchserve

> PyTorch官方模型服务框架，支持模型打包、A/B测试、多模型服务、自定义处理器

## 安装

```bash
pip install torchserve torch-model-archiver
```

## 用法

```
torchserve [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--start` | 启动服务 |
| `--stop` | 停止服务 |
| `--model-store` | 模型存储目录 |
| `--models` | 加载的模型列表 |
| `--ts-config` | 配置文件路径 |

## 示例

### 示例 1: 启动服务并加载模型

```bash
torchserve --start --model-store model_store --models my_model=my_model.mar
```

### 示例 2: 将PyTorch模型打包为.mar文件

```bash
torch-model-archiver --model-name my_model --version 1.0 --model-file model.py --serialized-file model.pt --handler custom_handler.py --export-path model_store
```

### 示例 3: 停止TorchServe服务

```bash
torchserve --stop
```

## 关联命令

- [[bentoml]]
- [[tritonserver]]

## 风险提示

> ⚠️ **MEDIUM**: 生产部署需配置安全策略

## 参考链接

- [https://pytorch.org/serve/](https://pytorch.org/serve/)

## 所属维度

[[模型服务-MOC|AI基础设施/模型服务]]

---
{
  "cmd_name": "ray-serve",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install ray[serve]",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "vllm",
    "tritonserver"
  ],
  "cmd_tags": [
    "inference",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# ray-serve

> Ray Serve可扩展模型服务框架，支持多模型组合、A/B测试、自动扩缩容

## 安装

```bash
pip install ray[serve]
```

## 用法

```
serve run [OPTIONS]
```

```
serve deploy [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行Serve应用 |
| `deploy` | 部署到Ray集群 |
| `config_file` | Serve配置文件 |

## 示例

### 示例 1: 本地运行模型服务

```bash
serve run app:my_model
```

### 示例 2: 部署多模型服务配置

```bash
serve deploy config.yaml
```

## 关联命令

- [[vllm]]
- [[tritonserver]]

## 风险提示

> ⚠️ **MEDIUM**: 生产部署需配置资源限制

## 参考链接

- [https://docs.ray.io/en/latest/serve/index.html](https://docs.ray.io/en/latest/serve/index.html)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]

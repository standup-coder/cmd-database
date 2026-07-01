---
{
  "cmd_name": "replicate",
  "cmd_category": "AI基础设施/大模型推理",
  "cmd_dimension": "大模型推理",
  "cmd_install": "pip install replicate",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "modal",
    "sky-pilot"
  ],
  "cmd_tags": [
    "inference",
    "deployment",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-inference.yaml"
}
---

# replicate

> Replicate模型托管云平台，一键部署和运行开源模型

## 安装

```bash
pip install replicate
```

## 用法

```
python app.py (使用replicate库)
```

## 参数

| Flag | Description |
|------|-------------|
| `replicate.run()` | 运行模型预测 |
| `replicate.deploy()` | 部署自定义模型 |

## 示例

### 示例 1: 运行Replicate托管的LLaMA-3模型

```bash
python -c "import replicate; output = replicate.run('meta/meta-llama-3-70b', input={'prompt':'Hello'})"
```

### 示例 2: 部署自己的模型

```bash
replicate deploy --model=my-model
```

## 关联命令

- [[modal]]
- [[sky-pilot]]

## 风险提示

> ⚠️ **LOW**: 托管服务，按量计费

## 参考链接

- [https://replicate.com/](https://replicate.com/)

## 所属维度

[[大模型推理-MOC|AI基础设施/大模型推理]]

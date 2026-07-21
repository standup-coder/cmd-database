---
{
  "cmd_name": "ctranslate2",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "pip install ctranslate2",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "optimum-cli",
    "onnxruntime"
  ],
  "cmd_tags": [
    "inference",
    "quantization",
    "gpu",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# ctranslate2

> CTranslate2高效推理引擎，支持INT8/INT16/FP16量化，CPU/GPU加速

## 安装

```bash
pip install ctranslate2
```

## 用法

```
ct2-transformers-converter [OPTIONS]
```

```
python inference.py (使用ctranslate2)
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | 源模型路径 |
| `--output_dir` | 输出目录 |
| `--quantization` | 量化类型 (int8, int8_float16, int16, float16) |
| `--force` | 强制覆盖 |

## 示例

### 示例 1: INT8量化转换M2M100模型

```bash
ct2-transformers-converter --model facebook/m2m100_418M --output_dir m2m100_ct2 --quantization int8
```

### 示例 2: CTranslate2翻译推理

```bash
python -c "import ctranslate2 as ct2; t = ct2.Translator('./m2m100_ct2'); print(t.translate_batch([['Hello world']]))"
```

## 关联命令

- [[optimum-cli]]
- [[onnxruntime]]

## 风险提示

> ⚠️ **LOW**: 格式转换安全

## 参考链接

- [https://github.com/OpenNMT/CTranslate2](https://github.com/OpenNMT/CTranslate2)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]

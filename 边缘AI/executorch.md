---
{
  "cmd_name": "executorch",
  "cmd_category": "AI基础设施/边缘AI",
  "cmd_dimension": "边缘AI",
  "cmd_install": "git clone https://github.com/pytorch/executorch.git && ./install_requirements.sh",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tflite",
    "coremltools"
  ],
  "cmd_tags": [
    "inference",
    "edge",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/edge-ai.yaml"
}
---

# executorch

> ExecuTorch PyTorch移动端运行时，支持iOS/Android/嵌入式，端到端推理优化

## 安装

```bash
git clone https://github.com/pytorch/executorch.git && ./install_requirements.sh
```

## 用法

```
python -m executorch.exir [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `to_edge` | 导出Edge Dialect |
| `to_executorch` | 导出ExecuTorch |
| `--quantization` | 量化配置 |

## 示例

### 示例 1: XNNPack后端导出MobileNet

```bash
python export.py --model mv3 --backend xnnpack --quantization 
```

### 示例 2: 导出示例模型

```bash
python -m examples.portable.scripts.export --model_name=add
```

## 关联命令

- [[tflite]]
- [[coremltools]]

## 风险提示

> ⚠️ **LOW**: 导出操作安全

## 参考链接

- [https://pytorch.org/executorch/](https://pytorch.org/executorch/)

## 所属维度

[[边缘AI-MOC|AI基础设施/边缘AI]]

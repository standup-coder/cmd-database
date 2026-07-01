---
{
  "cmd_name": "modelscan",
  "cmd_category": "AI基础设施/AI安全",
  "cmd_dimension": "AI安全",
  "cmd_install": "pip install modelscan",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "safetensors-convert",
    "garak"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/ai-safety.yaml"
}
---

# modelscan

> ProtectAI ModelScan模型文件安全扫描，检测Pickle反序列化漏洞、恶意代码注入

## 安装

```bash
pip install modelscan
```

## 用法

```
modelscan [OPTIONS] PATH
```

## 参数

| Flag | Description |
|------|-------------|
| `--path` | 扫描路径 |
| `--format` | 输出格式 (json, table) |

## 示例

### 示例 1: 扫描模型目录

```bash
modelscan /path/to/models/
```

### 示例 2: 扫描单个Pickle文件并输出JSON

```bash
modelscan model.pkl --format json
```

## 关联命令

- [[safetensors-convert]]
- [[garak]]

## 风险提示

> ⚠️ **LOW**: 只读扫描不改变文件

## 参考链接

- [https://github.com/protectai/modelscan](https://github.com/protectai/modelscan)

## 所属维度

[[AI安全-MOC|AI基础设施/AI安全]]

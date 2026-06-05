---
cmd_name: runpod
cmd_category: AI基础设施/AI应用
cmd_dimension: AI应用
cmd_install: pip install runpod
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- modal
- sky-pilot
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: RunPod GPU云平台，按需租用GPU进行AI训练和推理
created: '2026-06-04'
source_file: data/ai/ai-applications.yaml
---
# runpod

> RunPod GPU云平台，按需租用GPU进行AI训练和推理

## 安装

```bash
pip install runpod
```

## 用法

```
runpodctl [选项] [命令]
```

## 参数

| Flag | Description |
|------|-------------|
| `--api-key` | 指定API密钥 |

## 示例

### 配置API密钥

```bash
runpodctl config --apiKey YOUR_API_KEY
```

### 创建A100 GPU实例

```bash
runpodctl create pod --gpu A100 --image pytorch/pytorch
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[AI应用-MOC|AI基础设施/AI应用]]

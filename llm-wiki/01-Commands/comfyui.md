---
{
  "cmd_name": "comfyui",
  "cmd_category": "AI基础设施/多模态",
  "cmd_dimension": "多模态",
  "cmd_install": "git clone https://github.com/comfyanonymous/ComfyUI.git && pip install -r requirements.txt",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "stable-diffusion-cli",
    "clip"
  ],
  "cmd_tags": [
    "multimodal",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/multimodal.yaml"
}
---

# comfyui

> ComfyUI Stable Diffusion节点式可视化工作流，支持图像生成、视频生成、ControlNet

## 安装

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git && pip install -r requirements.txt
```

## 用法

```
python main.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--listen` | 监听地址 |
| `--port` | 端口号 |
| `--extra-model-paths-config` | 额外模型路径配置 |
| `--lowvram` | 低显存模式 |

## 示例

### 示例 1: 启动ComfyUI服务

```bash
python main.py --listen 0.0.0.0 --port 8188
```

### 示例 2: 低显存模式启动

```bash
python main.py --lowvram --disable-xformers
```

## 关联命令

- [[stable-diffusion-cli]]
- [[clip]]

## 风险提示

> ⚠️ **MEDIUM**: 模型下载占用大量存储

## 参考链接

- [https://github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 所属维度

[[多模态-MOC|AI基础设施/多模态]]

---
{
  "cmd_name": "label-studio",
  "cmd_category": "AI基础设施/数据与标注",
  "cmd_dimension": "数据与标注",
  "cmd_install": "pip install label-studio",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "argilla",
    "cleanlab"
  ],
  "cmd_tags": [
    "multimodal",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/data-labeling.yaml"
}
---

# label-studio

> Label Studio开源数据标注平台，支持图像、文本、音频、视频、时间序列等多模态标注

## 安装

```bash
pip install label-studio
```

## 用法

```
label-studio [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `start` | 启动标注服务 |
| `init` | 初始化项目 |
| `--port` | 服务端口号(默认8080) |
| `--username` | 管理员用户名 |

## 示例

### 示例 1: 启动标注平台

```bash
label-studio start
```

### 示例 2: 指定端口和账号启动

```bash
label-studio start --port 8080 --username admin --password admin123
```

### 示例 3: 初始化图像分类项目

```bash
label-studio init my_project --template image_classification
```

## 关联命令

- [[argilla]]
- [[cleanlab]]

## 风险提示

> ⚠️ **LOW**: 本地标注平台，注意数据安全

## 参考链接

- [https://labelstud.io/](https://labelstud.io/)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]

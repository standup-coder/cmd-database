---
{
  "cmd_name": "whisper",
  "cmd_category": "AI基础设施/多模态",
  "cmd_dimension": "多模态",
  "cmd_install": "pip install openai-whisper",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "faster-whisper",
    "transformers-pipeline"
  ],
  "cmd_tags": [
    "multimodal",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/multimodal.yaml"
}
---

# whisper

> OpenAI Whisper通用语音识别模型，支持99种语言，多尺寸模型(tiny~large-v3)

## 安装

```bash
pip install openai-whisper
```

## 用法

```
whisper [OPTIONS] AUDIO_FILE
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | 模型尺寸 (tiny, base, small, medium, large-v3) |
| `--language` | 语言代码 |
| `--task` | 任务类型 (transcribe, translate) |
| `--output_format` | 输出格式 (txt, vtt, srt, json) |

## 示例

### 示例 1: 中文语音识别

```bash
whisper audio.mp3 --model large-v3 --language Chinese
```

### 示例 2: 语音翻译为英文并输出字幕

```bash
whisper audio.mp3 --model medium --task translate --output_format srt
```

## 关联命令

- [[faster-whisper]]
- [[transformers-pipeline]]

## 风险提示

> ⚠️ **LOW**: 本地推理安全

## 参考链接

- [https://github.com/openai/whisper](https://github.com/openai/whisper)

## 所属维度

[[多模态-MOC|AI基础设施/多模态]]

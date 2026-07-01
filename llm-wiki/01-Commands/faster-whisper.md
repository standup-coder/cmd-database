---
{
  "cmd_name": "faster-whisper",
  "cmd_category": "AI基础设施/多模态",
  "cmd_dimension": "多模态",
  "cmd_install": "pip install faster-whisper",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "whisper",
    "ctranslate2"
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

# faster-whisper

> Faster-Whisper CTranslate2加速版Whisper，4倍速度提升，更低内存占用

## 安装

```bash
pip install faster-whisper
```

## 用法

```
python transcribe.py (使用faster_whisper库)
```

## 参数

| Flag | Description |
|------|-------------|
| `WhisperModel` | 加载模型 |
| `compute_type` | 计算类型 (int8, int8_float16, float16) |

## 示例

### 示例 1: GPU加速语音识别

```bash
python -c "from faster_whisper import WhisperModel; m = WhisperModel('large-v3', device='cuda', compute_type='float16'); segs, info = m.transcribe('audio.mp3')"
```

### 示例 2: 查看转录 API 帮助

```bash
python -c "from faster_whisper import WhisperModel; help(WhisperModel.transcribe)"
```

## 关联命令

- [[whisper]]
- [[ctranslate2]]

## 风险提示

> ⚠️ **LOW**: 本地推理安全

## 参考链接

- [https://github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)

## 所属维度

[[多模态-MOC|AI基础设施/多模态]]

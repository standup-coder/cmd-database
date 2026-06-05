---
cmd_name: mediapipe
cmd_category: AI基础设施/边缘AI
cmd_dimension: 边缘AI
cmd_install: pip install mediapipe
cmd_platforms:
- linux
- darwin
- windows
summary: "Google MediaPipe端侧ML流水线，支持人脸检测、姿态估计、手势识别、文本分类"
cmd_level: intermediate
cmd_related:
- tflite
- coremltools
cmd_tags:
- edge
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/edge-ai.yaml
---


# mediapipe

> Google MediaPipe端侧ML流水线，支持人脸检测、姿态估计、手势识别、文本分类

## 安装

```bash
pip install mediapipe
```

## 用法

```
python app.py (使用mediapipe库)
```

## 参数

| Flag | Description |
|------|-------------|
| `FaceDetection` | 人脸检测 |
| `Pose` | 姿态估计 |
| `Hands` | 手势识别 |
| `ImageClassifier` | 图像分类 |

## 示例

### 示例 1: 人脸检测

```bash
python -c "import mediapipe as mp; detector = mp.solutions.face_detection.FaceDetection(); results = detector.process(image)"
```

### 示例 2: 人体姿态估计

```bash
python -c "import mediapipe as mp; pose = mp.solutions.pose.Pose(); results = pose.process(image)"
```

## 关联命令

- [[tflite]]
- [[coremltools]]

## 风险提示

> ⚠️ **LOW**: 端侧推理安全

## 参考链接

- [https://mediapipe.dev/](https://mediapipe.dev/)

## 所属维度

[[边缘AI-MOC|AI基础设施/边缘AI]]

---
{
  "cmd_name": "git-lfs",
  "cmd_category": "AI基础设施/模型生态",
  "cmd_dimension": "模型生态",
  "cmd_install": "git lfs install",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "huggingface-cli",
    "safetensors-convert"
  ],
  "cmd_tags": [
    "rag",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/model-hub.yaml"
}
---

# git-lfs

> Git Large File Storage，管理大模型权重文件(GB级)的版本控制

## 安装

```bash
git lfs install
```

## 用法

```
git lfs [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `track` | 追踪指定格式的文件 |
| `pull` | 下载LFS文件 |
| `push` | 上传LFS文件 |
| `ls-files` | 列出已追踪的LFS文件 |

## 示例

### 示例 1: 追踪模型权重文件

```bash
git lfs track '*.bin' '*.safetensors' '*.gguf'
```

### 示例 2: 下载所有LFS文件

```bash
git lfs pull
```

### 示例 3: 列出LFS文件及大小

```bash
git lfs ls-files --size
```

## 关联命令

- [[huggingface-cli]]
- [[safetensors-convert]]

## 风险提示

> ⚠️ **MEDIUM**: LFS文件占用大量存储空间，push/pull可能耗时

## 参考链接

- [https://git-lfs.com/](https://git-lfs.com/)

## 所属维度

[[模型生态-MOC|AI基础设施/模型生态]]

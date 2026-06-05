---
cmd_name: neuralsecure
cmd_category: AI基础设施/AI安全
cmd_dimension: AI安全
cmd_install: pip install neuralsecure
cmd_platforms:
- linux
- darwin
- windows
summary: "NeuralSecure ML模型安全审计，检测对抗样本脆弱性、成员推断攻击、模型窃取风险"
cmd_level: intermediate
cmd_related:
- modelscan
- garak
cmd_tags:
- safety
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/ai-safety.yaml
---


# neuralsecure

> NeuralSecure ML模型安全审计，检测对抗样本脆弱性、成员推断攻击、模型窃取风险

## 安装

```bash
pip install neuralsecure
```

## 用法

```
python audit.py (使用neuralsecure库)
```

## 参数

| Flag | Description |
|------|-------------|
| `adversarial_robustness` | 对抗鲁棒性测试 |
| `membership_inference` | 成员推断攻击测试 |
| `model_extraction` | 模型提取攻击测试 |

## 示例

### 示例 1: 全面安全审计

```bash
python audit.py --model ./model.pt --tests adversarial,membership,extraction --output report.json
```

## 关联命令

- [[modelscan]]
- [[garak]]

## 风险提示

> ⚠️ **MEDIUM**: 攻击测试需在隔离环境执行

## 参考链接

- [https://github.com/protectai/neuralsecure](https://github.com/protectai/neuralsecure)

## 所属维度

[[AI安全-MOC|AI基础设施/AI安全]]

---
{
  "cmd_name": "meltano",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install meltano",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "airbyte",
    "dbt"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# meltano

> ELT 数据管道与 dbt 编排工具

## 安装

```bash
pip install meltano
```

## 用法

```
meltano [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化 |
| `add` | 添加 tap/target |
| `run` | 运行管道 |
| `test` | 测试 |

## 示例

### 示例 1: 初始化项目

```bash
meltano init myproject
```

### 示例 2: 运行完整 ELT

```bash
meltano run tap-gitlab target-postgres dbt:run
```

## 关联命令

- [[airbyte]]
- [[dbt]]

## 风险提示

> ⚠️ **MEDIUM**: meltano run 会读写数据源和目标，请确认环境配置

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]

# data/

> cmd4coder 的**单一数据源**。  
> CLI 和 LLM-Wiki 的所有命令内容均从此目录生成。

## 设计原则

- **单一事实来源**：修改 YAML 后，CLI 和 Wiki 同步更新。
- **分类元数据驱动**：`metadata.yaml` 定义全部 106 个分类。
- **领域目录组织**：按技术领域分组，便于维护。

## 目录结构

```
data/
├── metadata.yaml      # 106 分类元数据
├── ai/                # AI 基础设施（24 个 YAML，240 命令）
├── bigdata/           # 大数据（10 个 YAML，53 命令）
├── build-tools/       # 构建工具（3 个 YAML，10 命令）
├── cicd/              # CI/CD（2 个 YAML，9 命令）
├── cloud/             # 云平台（4 个 YAML，13 命令）
├── container/         # 容器编排（23 个 YAML，339 命令）
├── database/          # 数据库（7 个 YAML，64 命令）
├── diagnostic/        # 系统诊断（3 个 YAML，27 命令）
├── hardware/          # 硬件（9 个 YAML，64 命令）
├── lang/              # 编程语言（6 个 YAML，47 命令）
├── network/           # 网络工具（7 个 YAML，57 命令）
├── os/                # 操作系统（5 个 YAML，153 命令）
├── shell/             # Shell 脚本（1 个 YAML，5 命令）
└── vcs/               # 版本控制（2 个 YAML，31 命令）
```

## 数据规范

每条命令包含以下字段：

```yaml
category: "AI基础设施/大模型训练"
commands:
  - name: deepspeed
    category: "AI基础设施/大模型训练"
    install_required: true
    install_method: "pip install deepspeed"
    description: "微软DeepSpeed大规模分布式训练框架"
    usage:
      - "deepspeed [OPTIONS] SCRIPT.py"
    options:
      - flag: "--num_gpus"
        description: "使用的GPU数量"
    examples:
      - command: "deepspeed --num_gpus=4 train.py"
        description: "4卡训练"
    platforms: ["linux", "darwin", "windows"]
    related_commands: ["accelerate", "torchrun"]
    risks:
      - level: medium
        description: "大规模训练消耗大量GPU资源"
    references:
      - "https://www.deepspeed.ai/"
```

## 验证与同步

```bash
# 验证 YAML 格式与分类一致性
go run ./cmd/validator -d ./data -v

# YAML 变更后同步到 Wiki
python3 scripts/wiki/convert_to_wiki.py

# 重新生成 COMMANDS.md
python3 scripts/data/generate_commands_md.py
```

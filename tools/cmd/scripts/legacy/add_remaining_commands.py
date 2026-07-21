#!/usr/bin/env python3
"""Add remaining missing commands to YAML source files."""

import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]  # auto: repo root (scripts live in tools/cmd/scripts/<sub>/)
DATA_DIR = Path(__file__).resolve().parents[2] / "data"  # YAML 源已随 CLI 收敛到 tools/cmd/data

REMAINING = {
    "data/os/common.yaml": [
        {
            "name": "egrep",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "扩展正则表达式grep（等同于grep -E）",
            "usage": ["egrep [选项] 模式 [文件...]"],
            "options": [
                {"flag": "-i", "description": "忽略大小写"},
                {"flag": "-v", "description": "反向匹配"},
                {"flag": "-n", "description": "显示行号"},
            ],
            "examples": [
                {"command": "egrep 'error|warning' log.txt", "description": "匹配error或warning"},
                {"command": "egrep -i '^[a-z]+@[a-z]+\\.com' emails.txt", "description": "匹配邮箱格式"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["grep", "fgrep", "awk"],
        },
        {
            "name": "fgrep",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "固定字符串grep（等同于grep -F），禁用正则表达式",
            "usage": ["fgrep [选项] 字符串 [文件...]"],
            "options": [
                {"flag": "-i", "description": "忽略大小写"},
                {"flag": "-x", "description": "整行匹配"},
                {"flag": "-f", "description": "从文件读取匹配模式"},
            ],
            "examples": [
                {"command": "fgrep 'a*b' file.txt", "description": "按字面匹配a*b（不解释正则）"},
                {"command": "fgrep -f patterns.txt log.txt", "description": "从文件读取多个匹配字符串"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["grep", "egrep", "awk"],
        },
        {
            "name": "more",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "分页查看文件内容（less的简化版）",
            "usage": ["more [选项] [文件...]"],
            "options": [
                {"flag": "-N", "description": "显示行号"},
                {"flag": "+N", "description": "从第N行开始显示"},
            ],
            "examples": [
                {"command": "more file.txt", "description": "分页查看文件"},
                {"command": "cat file.txt | more", "description": "管道分页查看"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["less", "cat", "head"],
        },
        {
            "name": "rename",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "批量重命名文件（Perl正则表达式版或util-linux版）",
            "usage": ["rename [选项] 表达式 替换 文件..."],
            "options": [
                {"flag": "-n", "description": "模拟运行，不实际修改"},
                {"flag": "-v", "description": "显示详细操作"},
            ],
            "examples": [
                {"command": "rename 's/\\.txt$/.bak/' *.txt", "description": "将所有txt改为bak"},
                {"command": "rename -n 's/foo/bar/' *", "description": "模拟替换文件名中的foo为bar"},
            ],
            "platforms": ["linux"],
            "related_commands": ["mv", "cp", "find"],
        },
        {
            "name": "rmdir",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "删除空目录",
            "usage": ["rmdir [选项] 目录..."],
            "options": [
                {"flag": "-p, --parents", "description": "删除目录及其祖先空目录"},
                {"flag": "-v, --verbose", "description": "显示每个被删除的目录"},
            ],
            "examples": [
                {"command": "rmdir emptydir", "description": "删除空目录"},
                {"command": "rmdir -p a/b/c", "description": "删除c、b、a（如果都为空）"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["rm", "mkdir", "rm -rf"],
        },
        {
            "name": "sh",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "Bourne Shell，标准的Unix命令解释器",
            "usage": ["sh [选项] [脚本文件] [参数...]"],
            "options": [
                {"flag": "-c", "description": "执行命令字符串"},
                {"flag": "-x", "description": "打印执行的每条命令"},
                {"flag": "-e", "description": "命令失败时立即退出"},
            ],
            "examples": [
                {"command": "sh -c 'echo hello'", "description": "执行命令字符串"},
                {"command": "sh script.sh arg1 arg2", "description": "执行shell脚本并传递参数"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["bash", "zsh", "chmod"],
        },
        {
            "name": "zsh",
            "category": "操作系统/通用Linux命令",
            "install_required": True,
            "install_method": "apt install zsh (Ubuntu) 或 brew install zsh (macOS)",
            "description": "Z Shell，功能强大的交互式Shell，兼容Bash",
            "usage": ["zsh [选项] [脚本文件] [参数...]"],
            "options": [
                {"flag": "-c", "description": "执行命令字符串"},
                {"flag": "-l", "description": "作为登录Shell启动"},
            ],
            "examples": [
                {"command": "zsh", "description": "启动Zsh Shell"},
                {"command": "chsh -s $(which zsh)", "description": "将Zsh设为默认Shell"},
            ],
            "platforms": ["linux", "darwin"],
            "related_commands": ["bash", "sh", "oh-my-zsh"],
        },
    ],
    "data/cloud/terraform.yaml": {
        "category": "云平台/Terraform",
        "description": "基础设施即代码工具，管理云资源生命周期",
        "commands": [
            {
                "name": "terraform",
                "category": "云平台/Terraform",
                "install_required": True,
                "install_method": "参考 https://developer.hashicorp.com/terraform/install",
                "description": "基础设施即代码工具，管理云资源",
                "usage": ["terraform <子命令> [选项]"],
                "options": [
                    {"flag": "-version", "description": "显示版本信息"},
                    {"flag": "-help", "description": "显示帮助信息"},
                ],
                "examples": [
                    {"command": "terraform init", "description": "初始化工作目录"},
                    {"command": "terraform plan", "description": "预览将要执行的资源变更"},
                    {"command": "terraform apply", "description": "应用配置创建/更新资源"},
                    {"command": "terraform destroy", "description": "销毁所有管理的基础设施"},
                ],
                "platforms": ["linux", "darwin", "windows"],
                "related_commands": ["terraform plan", "terraform apply", "terraform init"],
            }
        ],
    },
    "data/container/kafka.yaml": {
        "category": "容器编排/消息队列",
        "description": "Apache Kafka分布式流处理平台",
        "commands": [
            {
                "name": "kafka",
                "category": "容器编排/消息队列",
                "install_required": True,
                "install_method": "参考 https://kafka.apache.org/quickstart",
                "description": "Apache Kafka分布式消息队列",
                "usage": ["kafka-server-start.sh [选项] server.properties"],
                "options": [
                    {"flag": "--override", "description": "覆盖配置属性"},
                ],
                "examples": [
                    {"command": "kafka-server-start.sh config/server.properties", "description": "启动Kafka服务器"},
                    {"command": "kafka-topics.sh --create --topic mytopic --bootstrap-server localhost:9092", "description": "创建Topic"},
                ],
                "platforms": ["linux", "darwin", "windows"],
                "related_commands": ["zookeeper", "kafka-console-producer", "kafka-console-consumer"],
            }
        ],
    },
    "data/ai/vector-db.yaml": {
        "name": "meilisearch",
        "category": "AI基础设施/向量数据库",
        "install_required": True,
        "install_method": "curl -L https://install.meilisearch.com | sh",
        "description": "开源即时搜索引擎，支持容错搜索和中文分词",
        "usage": ["meilisearch [选项]"],
        "options": [
            {"flag": "--master-key", "description": "设置API主密钥"},
            {"flag": "--db-path", "description": "指定数据库路径"},
        ],
        "examples": [
            {"command": "meilisearch --master-key mykey", "description": "带密钥启动搜索服务"},
            {"command": "curl -X POST 'http://localhost:7700/indexes/docs/search' -H 'Authorization: Bearer mykey' -d '{\"q\":\"hello\"}'", "description": "搜索文档"},
        ],
        "platforms": ["linux", "darwin", "windows"],
        "related_commands": ["elasticsearch", "typesense", "vespa-cli"],
    },
    "data/ai/llm-inference.yaml": {
        "name": "outlines",
        "category": "AI基础设施/大模型推理",
        "install_required": True,
        "install_method": "pip install outlines",
        "description": "LLM结构化生成库，强制模型输出JSON/Regex格式",
        "usage": ["python -c \"import outlines; ...\""],
        "options": [],
        "examples": [
            {"command": "python -c \"import outlines; model = outlines.models.transformers('gpt2')\"", "description": "加载模型"},
            {"command": "python -c \"import outlines; generator = outlines.generate.json(model, schema)\"", "description": "生成JSON格式输出"},
        ],
        "platforms": ["linux", "darwin", "windows"],
        "related_commands": ["instructor", "guidance", "langchain"],
    },
    "data/ai/ai-applications.yaml": {
        "name": "runpod",
        "category": "AI基础设施/AI应用",
        "install_required": True,
        "install_method": "pip install runpod",
        "description": "RunPod GPU云平台，按需租用GPU进行AI训练和推理",
        "usage": ["runpodctl [选项] [命令]"],
        "options": [
            {"flag": "--api-key", "description": "指定API密钥"},
        ],
        "examples": [
            {"command": "runpodctl config --apiKey YOUR_API_KEY", "description": "配置API密钥"},
            {"command": "runpodctl create pod --gpu A100 --image pytorch/pytorch", "description": "创建A100 GPU实例"},
        ],
        "platforms": ["linux", "darwin", "windows"],
        "related_commands": ["modal", "sky-pilot", "vast.ai"],
    },
    "data/ai/federated-learning.yaml": {
        "name": "crypTen",
        "category": "AI基础设施/联邦学习",
        "install_required": True,
        "install_method": "pip install crypten",
        "description": "Meta开源的隐私保护机器学习框架，支持安全多方计算",
        "usage": ["python -c \"import crypten; ...\""],
        "options": [],
        "examples": [
            {"command": "python -c \"import crypten; crypten.init()\"", "description": "初始化CrypTen"},
        ],
        "platforms": ["linux", "darwin"],
        "related_commands": ["opacus", "flower", "pyvertical"],
    },
}

def add_to_existing_yaml(yaml_path: Path, commands: list):
    text = yaml_path.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    existing = {c["name"] for c in data.get("commands", [])}
    added = 0
    for cmd in commands:
        if cmd["name"] in existing:
            print(f"  ⚠️  Duplicate: {cmd['name']}")
            continue
        if "category" not in cmd:
            cmd["category"] = data.get("category", "")
        data.setdefault("commands", []).append(cmd)
        added += 1
    if added:
        yaml_path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        print(f"  ✅ Added {added} to {yaml_path.name}")
    return added

def create_new_yaml(yaml_path: Path, data: dict):
    if yaml_path.exists():
        # It's a single command to append to existing file
        text = yaml_path.read_text(encoding="utf-8")
        existing = yaml.safe_load(text)
        existing.setdefault("commands", []).append(data)
        yaml_path.write_text(yaml.dump(existing, allow_unicode=True, sort_keys=False), encoding="utf-8")
        print(f"  ✅ Appended to {yaml_path.name}")
        return 1
    else:
        # Create new file
        if "commands" not in data:
            # Wrap single command
            cat = data.pop("category", "")
            desc = data.pop("description", "")
            data = {
                "category": cat,
                "description": desc,
                "commands": [data],
            }
        yaml_path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        print(f"  ✅ Created {yaml_path.name}")
        return len(data.get("commands", []))

def main():
    total = 0
    for rel_path, payload in REMAINING.items():
        yaml_path = PROJECT_ROOT / rel_path
        yaml_path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(payload, list):
            total += add_to_existing_yaml(yaml_path, payload)
        elif isinstance(payload, dict) and "commands" in payload:
            total += create_new_yaml(yaml_path, payload)
        else:
            total += create_new_yaml(yaml_path, payload)
    print(f"\nTotal added: {total}")

if __name__ == "__main__":
    main()

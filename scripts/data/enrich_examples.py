#!/usr/bin/env python3
"""
为只有 1 个示例的命令补充第二条真实示例，进一步降低 validator 警告。
不新增命令，仅丰富现有命令的示例字段。
"""
import sys
import os
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

# (file relative to data dir, command name) -> second example dict
SECOND_EXAMPLES = {
    ("os/common.yaml", "pwd"): {
        "command": "pwd -P",
        "description": "显示物理路径（解析所有符号链接）",
    },
    ("os/ubuntu.yaml", "apt update"): {
        "command": "sudo apt update -qq",
        "description": "静默更新包索引",
    },
    ("os/ubuntu.yaml", "apt search"): {
        "command": "apt search --names-only nginx",
        "description": "只按包名搜索",
    },
    ("os/ubuntu.yaml", "apt-cache show"): {
        "command": "apt-cache depends nginx",
        "description": "查看包的依赖关系",
    },
    ("os/ubuntu.yaml", "dpkg -i"): {
        "command": "sudo dpkg -i --force-confold package.deb",
        "description": "安装时保留旧配置文件",
    },
    ("os/ubuntu.yaml", "dpkg -r"): {
        "command": "sudo dpkg -r --purge nginx",
        "description": "彻底移除包及配置",
    },
    ("os/ubuntu.yaml", "systemctl start"): {
        "command": "sudo systemctl start nginx.service",
        "description": "启动指定服务单元",
    },
    ("os/ubuntu.yaml", "systemctl stop"): {
        "command": "sudo systemctl stop nginx.service",
        "description": "停止指定服务单元",
    },
    ("os/ubuntu.yaml", "systemctl status"): {
        "command": "systemctl status nginx --no-pager",
        "description": "不分页显示服务状态",
    },
    ("os/ubuntu.yaml", "systemctl enable"): {
        "command": "sudo systemctl enable --now nginx",
        "description": "设置开机自启并立即启动",
    },
    ("os/ubuntu.yaml", "systemctl disable"): {
        "command": "sudo systemctl disable --now nginx",
        "description": "禁用开机自启并立即停止",
    },
    ("os/ubuntu.yaml", "systemctl restart"): {
        "command": "sudo systemctl restart nginx.service",
        "description": "重启指定服务单元",
    },
    ("os/ubuntu.yaml", "ufw enable"): {
        "command": "sudo ufw enable --force",
        "description": "非交互式启用防火墙",
    },
    ("os/ubuntu.yaml", "ufw deny"): {
        "command": "sudo ufw deny from 192.168.1.100 to any port 22",
        "description": "拒绝特定 IP 访问 SSH 端口",
    },
    ("os/centos.yaml", "yum remove"): {
        "command": "sudo yum remove -y nginx",
        "description": "无需确认移除包",
    },
    ("os/centos.yaml", "yum search"): {
        "command": "yum search all nginx",
        "description": "搜索名称和描述",
    },
    ("os/centos.yaml", "yum info"): {
        "command": "yum info available nginx",
        "description": "查看可安装版本信息",
    },
    ("os/centos.yaml", "rpm -i"): {
        "command": "sudo rpm -ivh --nodeps package.rpm",
        "description": "忽略依赖强制安装（谨慎使用）",
    },
    ("os/centos.yaml", "rpm -e"): {
        "command": "sudo rpm -e --nodeps nginx",
        "description": "忽略依赖强制卸载（谨慎使用）",
    },
    ("os/centos.yaml", "rpm -qi"): {
        "command": "rpm -qi -p package.rpm",
        "description": "查看未安装 RPM 包信息",
    },
    ("os/centos.yaml", "getenforce"): {
        "command": "getenforce && sestatus",
        "description": "同时查看模式和详细状态",
    },
    ("os/centos.yaml", "sestatus"): {
        "command": "sestatus -v",
        "description": "显示详细策略状态",
    },
    ("lang/java.yaml", "javadoc"): {
        "command": "javadoc -private -d docs src/main/java/com/example/*.java",
        "description": "生成包含私有成员的文档",
    },
    ("lang/go.yaml", "go fmt"): {
        "command": "gofmt -w -s main.go",
        "description": "简化并格式化单个文件",
    },
    ("lang/go.yaml", "go vet"): {
        "command": "go vet -tags=integration ./...",
        "description": "检查指定构建标签的包",
    },
    ("lang/python.yaml", "pylint"): {
        "command": "pylint --disable=C0103 mymodule.py",
        "description": "禁用指定警告后检查",
    },
    ("lang/nodejs.yaml", "npm start"): {
        "command": "npm start -- --port=3000",
        "description": "启动并传递自定义端口参数",
    },
    ("diagnostic/arthas.yaml", "stack"): {
        "command": "stack com.example.Service doSomething -n 5",
        "description": "只打印前 5 次调用栈",
    },
    ("diagnostic/tsar.yaml", "tsar --check"): {
        "command": "tsar --check --cpu --mem",
        "description": "检查 CPU 和内存模块",
    },
    ("diagnostic/tsar.yaml", "tsar --list"): {
        "command": "tsar --live --cpu",
        "description": "实时查看 CPU 指标",
    },
    ("container/docker.yaml", "docker attach"): {
        "command": "docker attach --sig-proxy=false mycontainer",
        "description": "附加时忽略键盘中断转发",
    },
    ("container/k8s-dev.yaml", "tilt down"): {
        "command": "tilt down --delete-namespaces",
        "description": "删除 Tilt 资源及创建的命名空间",
    },
    (
        "container/k8s-mlops.yaml",
        "kubectl port-forward svc/istio-ingressgateway",
    ): {
        "command": "kubectl port-forward --address=0.0.0.0 svc/istio-ingressgateway 8080:80 -n istio-system",
        "description": "绑定到所有网络接口以便外部访问",
    },
    ("database/mysql.yaml", "mysql_secure_installation"): {
        "command": "sudo mysql_secure_installation --defaults-file=/etc/mysql/my.cnf",
        "description": "指定配置文件运行安全向导",
    },
    ("database/redis.yaml", "redis-check-rdb"): {
        "command": "redis-check-rdb --verbose dump.rdb",
        "description": "详细输出 RDB 检查结果",
    },
    ("database/redis.yaml", "redis-cli MONITOR"): {
        "command": "redis-cli MONITOR | head -n 20",
        "description": "只监控前 20 条命令",
    },
    ("build/maven.yaml", "mvn dependency"): {
        "command": "mvn dependency:tree -DoutputFile=deps.txt",
        "description": "导出依赖树到文件",
    },
    ("build/maven.yaml", "mvn archetype"): {
        "command": "mvn archetype:generate -B -DarchetypeArtifactId=maven-archetype-quickstart",
        "description": "非交互式生成项目",
    },
    ("build/maven.yaml", "mvn clean"): {
        "command": "mvn clean package -DskipTests",
        "description": "清理并打包（跳过测试）",
    },
    ("build/gradle.yaml", "gradle init"): {
        "command": "gradle init --type java-application --dsl groovy",
        "description": "生成 Groovy DSL 的 Java 应用",
    },
    ("ai/ml-frameworks.yaml", "torchrun"): {
        "command": "torchrun --nproc_per_node=2 --nnodes=1 train.py",
        "description": "单机双卡启动训练",
    },
    ("ai/ml-frameworks.yaml", "tensorboard"): {
        "command": "tensorboard --logdir=runs --host=0.0.0.0 --port=6006",
        "description": "绑定所有 IP 并指定端口",
    },
    ("ai/llm-training.yaml", "neuronx-nxdt"): {
        "command": "neuronx-nxdt --help",
        "description": "查看 Trainium 分布式训练工具帮助",
    },
    ("ai/llm-training.yaml", "cerebras"): {
        "command": "csrun_wse --help",
        "description": "查看 Cerebras 运行工具帮助",
    },
    ("ai/llm-inference.yaml", "tensor-parallel"): {
        "command": 'python -c "import tensor_parallel as tp; help(tp.TensorParallelPreTrainedModel)"',
        "description": "查看张量并行 API 帮助",
    },
    ("ai/llm-inference.yaml", "together"): {
        "command": 'python -c "from together import Together; c=Together(); r=c.chat.completions.create(model=\'meta-llama/Llama-3-8b\', messages=[{\'role\':\'user\',\'content\':\'Hi\'}], max_tokens=128, temperature=0.7)"',
        "description": "控制生成长度和随机性",
    },
    ("ai/llm-inference.yaml", "fireworks"): {
        "command": 'python -c "from fireworks.client import Fireworks; fw=Fireworks(); r=fw.completion.create(model=\'accounts/fireworks/models/llama-v3-8b\', prompt=\'Hello\', max_tokens=100, temperature=0.5)"',
        "description": "使用采样参数调用 Fireworks",
    },
    ("ai/llm-inference.yaml", "groq"): {
        "command": 'python -c "from groq import Groq; g=Groq(); r=g.chat.completions.create(model=\'llama-3.1-8b\', messages=[{\'role\':\'user\',\'content\':\'Hi\'}], max_tokens=1024)"',
        "description": "限制最大输出 token 数",
    },
    ("ai/model-hub.yaml", "autoawq"): {
        "command": 'python -c "from awq import AutoAWQForCausalLM; help(AutoAWQForCausalLM.from_quantized)"',
        "description": "查看量化加载 API",
    },
    ("ai/model-hub.yaml", "model-card"): {
        "command": "huggingface-cli upload my-model ./model README.md",
        "description": "上传模型文件到 Hub",
    },
    ("ai/model-hub.yaml", "neuronx-cc"): {
        "command": "neuronx-cc --help",
        "description": "查看 Neuron 编译器帮助",
    },
    ("ai/model-hub.yaml", "coremltools"): {
        "command": 'python -c "import coremltools as ct; help(ct.convert)"',
        "description": "查看 CoreML 转换 API",
    },
    ("ai/model-hub.yaml", "paddle2onnx"): {
        "command": "paddle2onnx --help",
        "description": "查看 ONNX 转换帮助",
    },
    ("ai/data-labeling.yaml", "datacompy"): {
        "command": 'python -c "import datacompy; help(datacompy.Compare)"',
        "description": "查看比较 API 帮助",
    },
    ("ai/monitoring.yaml", "arize"): {
        "command": 'python -c "from arize.api import Client; help(Client.log)"',
        "description": "查看日志 API 帮助",
    },
    ("ai/vector-db.yaml", "weaviate-cli"): {
        "command": "docker logs weaviate",
        "description": "查看 Weaviate 容器日志",
    },
    ("ai/vector-db.yaml", "pinecone"): {
        "command": 'python -c "from pinecone import Pinecone; help(Pinecone.create_index)"',
        "description": "查看索引创建 API",
    },
    ("ai/vector-db.yaml", "turbopuffer"): {
        "command": 'python -c "import turbopuffer as tp; help(tp.Namespace.query)"',
        "description": "查看查询 API 帮助",
    },
    ("ai/vector-db.yaml", "typesense"): {
        "command": "docker exec typesense curl http://localhost:8108/health",
        "description": "检查 Typesense 健康状态",
    },
    ("ai/vector-db.yaml", "elasticsearch"): {
        "command": "curl http://localhost:9200/_cluster/health",
        "description": "查看集群健康状态",
    },
    ("ai/agent-engineering.yaml", "phidata"): {
        "command": "python assistant.py --storage postgres --model claude-3-sonnet",
        "description": "使用 PostgreSQL 存储和 Claude 模型",
    },
    ("ai/agent-engineering.yaml", "pydantic-ai"): {
        "command": 'python -c "from pydantic_ai import Agent; help(Agent.run_sync)"',
        "description": "查看同步运行 API",
    },
    ("ai/harness-engineering.yaml", "ds-1000"): {
        "command": "python test_ds1000.py --mode completion --input_path ./predictions",
        "description": "按完成模式评测",
    },
    ("ai/harness-engineering.yaml", "big-bench"): {
        "command": "python bigbench/evaluate_task.py --task simple_arithmetic --models gpt-4 --max_examples 10",
        "description": "只评测 10 个样例",
    },
    ("ai/harness-engineering.yaml", "arena"): {
        "command": "curl https://chat.lmsys.org/api/leaderboard | jq .",
        "description": "以 JSON 格式查看排行榜",
    },
    ("ai/harness-engineering.yaml", "prometheus-eval"): {
        "command": "python evaluate.py --model prometheus-eval/prometheus-7b-v2.0 --data eval_set.json --feedback",
        "description": "生成评估反馈",
    },
    ("ai/harness-engineering.yaml", "tool-bench"): {
        "command": "python inference.py --tool_root_dir data/toolenv/tools --model_path gpt-4 --top_k 5",
        "description": "设置候选工具数量",
    },
    ("ai/harness-engineering.yaml", "api-bench"): {
        "command": "python evaluate.py --api_spec swagger.json --test_cases tests.json --output results.json",
        "description": "指定结果输出文件",
    },
    ("ai/harness-engineering.yaml", "pair-wise-eval"): {
        "command": "python evaluate.py --comparisons results.json --method bootstrap",
        "description": "Bootstrap 置信区间排名",
    },
    ("ai/ai-gateway.yaml", "keywords-ai"): {
        "command": 'python -c "from keywordsai import KeywordsAIClient; help(KeywordsAIClient.log_inference)"',
        "description": "查看推理日志 API",
    },
    ("ai/ai-safety.yaml", "neuralsecure"): {
        "command": "python audit.py --model ./model.pt --tests adversarial --output report.json --verbose",
        "description": "只进行对抗样本审计",
    },
    ("ai/multimodal.yaml", "faster-whisper"): {
        "command": 'python -c "from faster_whisper import WhisperModel; help(WhisperModel.transcribe)"',
        "description": "查看转录 API 帮助",
    },
    ("ai/ai-coding.yaml", "continue-dev"): {
        "command": "continue-dev --version",
        "description": "查看 Continue 版本",
    },
    ("ai/ai-coding.yaml", "codeium"): {
        "command": "codeium --status",
        "description": "查看 Codeium 服务状态",
    },
    ("ai/rag-infra.yaml", "llamaparse"): {
        "command": 'python -c "from llama_parse import LlamaParse; help(LlamaParse.load_data)"',
        "description": "查看 PDF 加载 API",
    },
    ("ai/rag-infra.yaml", "docling"): {
        "command": 'python -c "from docling.document_converter import DocumentConverter; help(DocumentConverter.convert)"',
        "description": "查看文档转换 API",
    },
}


def main(data_dir: str = "data") -> int:
    enriched = 0
    for (rel_file, name), example in SECOND_EXAMPLES.items():
        path = os.path.join(data_dir, rel_file)
        with open(path, "r", encoding="utf-8") as f:
            doc = yaml.load(f)
        changed = False
        for cmd in doc.get("commands", []):
            if cmd["name"] != name:
                continue
            examples = cmd.setdefault("examples", [])
            if len(examples) < 2:
                examples.append(
                    {
                        "command": example["command"],
                        "description": example["description"],
                    }
                )
                changed = True
                enriched += 1
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                yaml.dump(doc, f)
            print(f"{rel_file}: added second example for '{name}'")
    print(f"\nTotal commands enriched with second example: {enriched}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data"))

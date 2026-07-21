#!/usr/bin/env python3
"""
Add missing commands to YAML source files.
These commands were referenced in cmd_related but missing from source data.
"""

import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]  # auto: repo root (scripts live in tools/cmd/scripts/<sub>/)
DATA_DIR = Path(__file__).resolve().parents[2] / "data"  # YAML 源已随 CLI 收敛到 tools/cmd/data

# Define missing commands grouped by target YAML file
MISSING_COMMANDS = {
    "data/container/docker.yaml": [
        {
            "name": "docker push",
            "category": "容器编排/Docker命令",
            "install_required": True,
            "install_method": "参考 https://docs.docker.com/engine/install/",
            "description": "将本地镜像推送到镜像仓库",
            "usage": ["docker push [OPTIONS] NAME[:TAG]"],
            "options": [
                {"flag": "--all-tags", "description": "推送所有标签"},
                {"flag": "--disable-content-trust", "description": "跳过镜像签名验证"},
            ],
            "examples": [
                {"command": "docker push myrepo/myimage:latest", "description": "推送镜像到仓库"},
                {"command": "docker push username/nginx:v1.0", "description": "推送带标签的镜像"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["docker pull", "docker build", "docker tag"],
        },
        {
            "name": "docker inspect",
            "category": "容器编排/Docker命令",
            "install_required": True,
            "install_method": "参考 https://docs.docker.com/engine/install/",
            "description": "获取容器或镜像的底层信息",
            "usage": ["docker inspect [OPTIONS] NAME|ID [NAME|ID...]"],
            "options": [
                {"flag": "-f, --format", "description": "使用Go模板格式化输出"},
                {"flag": "-s, --size", "description": "显示总文件大小"},
                {"flag": "--type", "description": "指定对象类型（container/image/network/volume）"},
            ],
            "examples": [
                {"command": "docker inspect nginx", "description": "查看nginx镜像详细信息"},
                {"command": "docker inspect -f '{{.NetworkSettings.IPAddress}}' mycontainer", "description": "获取容器IP地址"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["docker ps", "docker logs", "docker exec"],
        },
        {
            "name": "docker rmi",
            "category": "容器编排/Docker命令",
            "install_required": True,
            "install_method": "参考 https://docs.docker.com/engine/install/",
            "description": "删除本地镜像",
            "usage": ["docker rmi [OPTIONS] IMAGE [IMAGE...]"],
            "options": [
                {"flag": "-f, --force", "description": "强制删除镜像"},
                {"flag": "--no-prune", "description": "不删除未标记的父镜像"},
            ],
            "examples": [
                {"command": "docker rmi nginx:latest", "description": "删除指定镜像"},
                {"command": "docker rmi $(docker images -q -f dangling=true)", "description": "删除所有悬空镜像"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["docker images", "docker pull", "docker system prune"],
        },
        {
            "name": "docker start",
            "category": "容器编排/Docker命令",
            "install_required": True,
            "install_method": "参考 https://docs.docker.com/engine/install/",
            "description": "启动一个或多个已停止的容器",
            "usage": ["docker start [OPTIONS] CONTAINER [CONTAINER...]"],
            "options": [
                {"flag": "-a, --attach", "description": "附加到容器的标准输出"},
                {"flag": "-i, --interactive", "description": "附加标准输入"},
            ],
            "examples": [
                {"command": "docker start mycontainer", "description": "启动已停止的容器"},
                {"command": "docker start -a mycontainer", "description": "启动并查看输出"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["docker stop", "docker restart", "docker run"],
        },
        {
            "name": "docker restart",
            "category": "容器编排/Docker命令",
            "install_required": True,
            "install_method": "参考 https://docs.docker.com/engine/install/",
            "description": "重启一个或多个容器",
            "usage": ["docker restart [OPTIONS] CONTAINER [CONTAINER...]"],
            "options": [
                {"flag": "-t, --time", "description": "关闭前等待的秒数（默认10秒）"},
            ],
            "examples": [
                {"command": "docker restart mycontainer", "description": "重启容器"},
                {"command": "docker restart -t 30 mycontainer", "description": "30秒优雅重启"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["docker start", "docker stop", "docker kill"],
        },
        {
            "name": "docker attach",
            "category": "容器编排/Docker命令",
            "install_required": True,
            "install_method": "参考 https://docs.docker.com/engine/install/",
            "description": "附加到正在运行的容器",
            "usage": ["docker attach [OPTIONS] CONTAINER"],
            "options": [
                {"flag": "--detach-keys", "description": "覆盖分离序列键"},
                {"flag": "--no-stdin", "description": "不附加标准输入"},
                {"flag": "--sig-proxy", "description": "代理所有接收到的信号（默认true）"},
            ],
            "examples": [
                {"command": "docker attach mycontainer", "description": "附加到运行中的容器"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["docker exec", "docker run", "docker logs"],
        },
    ],
    "data/vcs/git.yaml": [
        {
            "name": "git fetch",
            "category": "版本控制/Git命令",
            "install_required": True,
            "install_method": "apt install git (Ubuntu) 或 yum install git (CentOS)",
            "description": "从远程仓库下载对象和引用，但不合并",
            "usage": ["git fetch [<remote>] [<refspec>...]"],
            "options": [
                {"flag": "--all", "description": "获取所有远程仓库的更新"},
                {"flag": "--prune", "description": "删除远程已不存在的分支跟踪"},
                {"flag": "--tags", "description": "获取所有标签"},
                {"flag": "--depth <n>", "description": "浅获取，限制历史深度"},
            ],
            "examples": [
                {"command": "git fetch origin", "description": "获取origin远程的最新提交"},
                {"command": "git fetch --all --prune", "description": "获取所有远程并清理已删除分支"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["git pull", "git merge", "git clone"],
        },
        {
            "name": "git diff",
            "category": "版本控制/Git命令",
            "install_required": True,
            "install_method": "apt install git (Ubuntu) 或 yum install git (CentOS)",
            "description": "显示工作区与暂存区或提交之间的差异",
            "usage": ["git diff [<options>] [<commit>] [--] [<path>...]"],
            "options": [
                {"flag": "--cached", "description": "显示暂存区与最新提交的差异"},
                {"flag": "--stat", "description": "显示统计摘要而非完整差异"},
                {"flag": "-w", "description": "忽略空白字符差异"},
            ],
            "examples": [
                {"command": "git diff", "description": "查看未暂存的修改"},
                {"command": "git diff --cached", "description": "查看已暂存但未提交的修改"},
                {"command": "git diff HEAD~1", "description": "查看最近一次提交的差异"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["git status", "git add", "git log"],
        },
        {
            "name": "git rebase",
            "category": "版本控制/Git命令",
            "install_required": True,
            "install_method": "apt install git (Ubuntu) 或 yum install git (CentOS)",
            "description": "将当前分支变基到另一分支，重写提交历史",
            "usage": ["git rebase [-i | --interactive] [<branch>]"],
            "options": [
                {"flag": "-i, --interactive", "description": "交互式变基，可编辑/合并提交"},
                {"flag": "--continue", "description": "解决冲突后继续变基"},
                {"flag": "--abort", "description": "中止变基，恢复到变基前状态"},
                {"flag": "--onto <newbase>", "description": "将当前分支变基到新基础提交"},
            ],
            "examples": [
                {"command": "git rebase main", "description": "将当前分支变基到main"},
                {"command": "git rebase -i HEAD~3", "description": "交互式合并最近3个提交"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["git merge", "git cherry-pick", "git log"],
        },
        {
            "name": "git switch",
            "category": "版本控制/Git命令",
            "install_required": True,
            "install_method": "apt install git (Ubuntu) 或 yum install git (CentOS)",
            "description": "切换分支（Git 2.23+ 推荐替代checkout）",
            "usage": ["git switch [<options>] [<branch-name>]"],
            "options": [
                {"flag": "-c, --create", "description": "创建并切换到新分支"},
                {"flag": "-", "description": "切换到上一个分支"},
                {"flag": "--detach", "description": "切换到分离HEAD状态"},
            ],
            "examples": [
                {"command": "git switch feature-branch", "description": "切换到feature分支"},
                {"command": "git switch -c new-feature", "description": "创建并切换到新分支"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["git branch", "git checkout", "git merge"],
        },
        {
            "name": "git restore",
            "category": "版本控制/Git命令",
            "install_required": True,
            "install_method": "apt install git (Ubuntu) 或 yum install git (CentOS)",
            "description": "恢复工作区或暂存区文件（Git 2.23+ 推荐替代checkout）",
            "usage": ["git restore [<options>] [<pathspec>...]"],
            "options": [
                {"flag": "--staged", "description": "恢复暂存区中的文件"},
                {"flag": "--source <tree>", "description": "从指定提交恢复文件"},
                {"flag": "--worktree", "description": "恢复工作区文件（默认）"},
            ],
            "examples": [
                {"command": "git restore file.txt", "description": "撤销对file.txt的修改"},
                {"command": "git restore --staged file.txt", "description": "取消暂存file.txt"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["git checkout", "git reset", "git status"],
        },
        {
            "name": "git show",
            "category": "版本控制/Git命令",
            "install_required": True,
            "install_method": "apt install git (Ubuntu) 或 yum install git (CentOS)",
            "description": "显示提交、标签或对象的详细信息和差异",
            "usage": ["git show [<options>] [<object>...]"],
            "options": [
                {"flag": "--stat", "description": "显示修改统计"},
                {"flag": "--name-only", "description": "仅显示修改的文件名"},
                {"flag": "-p", "description": "显示补丁（默认）"},
            ],
            "examples": [
                {"command": "git show HEAD", "description": "显示最新提交的详细信息"},
                {"command": "git show abc1234", "description": "显示指定提交的详细信息"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["git log", "git diff", "git cat-file"],
        },
    ],
    "data/os/common.yaml": [
        {
            "name": "awk",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "文本处理语言，按模式扫描和处理文件",
            "usage": ["awk 'pattern { action }' [file...]"],
            "options": [
                {"flag": "-F", "description": "指定字段分隔符"},
                {"flag": "-v", "description": "赋值变量"},
                {"flag": "-f", "description": "从文件读取awk脚本"},
            ],
            "examples": [
                {"command": "awk '{print $1}' file.txt", "description": "打印每行第一个字段"},
                {"command": "awk -F: '{print $1}' /etc/passwd", "description": "以冒号分隔打印第一个字段"},
                {"command": "awk '/pattern/ {print $0}' file.txt", "description": "匹配pattern的行"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["sed", "grep", "cut"],
        },
        {
            "name": "sed",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "流编辑器，执行基本的文本转换",
            "usage": ["sed [选项] '命令' [文件...]"],
            "options": [
                {"flag": "-i", "description": "直接修改文件"},
                {"flag": "-e", "description": "执行多个命令"},
                {"flag": "-n", "description": "静默模式，只打印指定行"},
                {"flag": "-r", "description": "使用扩展正则表达式"},
            ],
            "examples": [
                {"command": "sed 's/old/new/g' file.txt", "description": "全局替换文本"},
                {"command": "sed -i 's/old/new/g' file.txt", "description": "直接修改文件内容"},
                {"command": "sed -n '5,10p' file.txt", "description": "打印第5到10行"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["awk", "grep", "tr"],
        },
        {
            "name": "kill",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "向进程发送信号以终止或控制",
            "usage": ["kill [信号] PID..."],
            "options": [
                {"flag": "-9", "description": "SIGKILL，强制终止（不可捕获）"},
                {"flag": "-15", "description": "SIGTERM，优雅终止（默认）"},
                {"flag": "-l", "description": "列出所有信号名称"},
            ],
            "examples": [
                {"command": "kill 1234", "description": "优雅终止PID 1234"},
                {"command": "kill -9 1234", "description": "强制终止PID 1234"},
                {"command": "kill -l", "description": "列出所有可用信号"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["ps", "top", "killall"],
        },
        {
            "name": "which",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "查找命令的可执行文件路径",
            "usage": ["which [选项] 命令..."],
            "options": [
                {"flag": "-a", "description": "显示所有匹配路径"},
            ],
            "examples": [
                {"command": "which python", "description": "查找python可执行文件位置"},
                {"command": "which -a python", "description": "查找所有python路径"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["whereis", "type", "command"],
        },
        {
            "name": "whereis",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "定位命令的二进制、源码和手册页文件",
            "usage": ["whereis [选项] 命令..."],
            "options": [
                {"flag": "-b", "description": "只搜索二进制文件"},
                {"flag": "-m", "description": "只搜索手册页"},
                {"flag": "-s", "description": "只搜索源码"},
            ],
            "examples": [
                {"command": "whereis python", "description": "查找python的所有相关文件"},
                {"command": "whereis -b python", "description": "只查找python二进制文件"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["which", "locate", "find"],
        },
        {
            "name": "locate",
            "category": "操作系统/通用Linux命令",
            "install_required": True,
            "install_method": "apt install mlocate (Ubuntu) 或 yum install mlocate (CentOS)",
            "description": "通过预建数据库快速查找文件",
            "usage": ["locate [选项] 模式..."],
            "options": [
                {"flag": "-i", "description": "忽略大小写"},
                {"flag": "-r", "description": "使用正则表达式"},
                {"flag": "-c", "description": "只显示匹配数量"},
                {"flag": "-n <N>", "description": "最多显示N个结果"},
            ],
            "examples": [
                {"command": "locate nginx.conf", "description": "快速查找nginx配置文件"},
                {"command": "locate -i '*.log'", "description": "忽略大小写查找日志文件"},
            ],
            "platforms": ["linux", "darwin"],
            "related_commands": ["find", "whereis", "updatedb"],
        },
        {
            "name": "less",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "分页查看文件内容，支持前后翻页",
            "usage": ["less [选项] [文件...]"],
            "options": [
                {"flag": "-N", "description": "显示行号"},
                {"flag": "-i", "description": "搜索时忽略大小写"},
                {"flag": "-S", "description": "截断长行不换行"},
                {"flag": "+F", "description": "类似tail -f，实时跟踪文件"},
            ],
            "examples": [
                {"command": "less /var/log/syslog", "description": "分页查看系统日志"},
                {"command": "less +F /var/log/nginx/access.log", "description": "实时跟踪日志文件"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["more", "cat", "tail"],
        },
        {
            "name": "head",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "显示文件开头部分",
            "usage": ["head [选项] [文件...]"],
            "options": [
                {"flag": "-n <N>", "description": "显示前N行（默认10行）"},
                {"flag": "-c <N>", "description": "显示前N字节"},
                {"flag": "-q", "description": "不显示文件名标题"},
            ],
            "examples": [
                {"command": "head -n 20 file.txt", "description": "显示文件前20行"},
                {"command": "head -c 100 file.bin", "description": "显示文件前100字节"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["tail", "cat", "less"],
        },
        {
            "name": "tail",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "显示文件末尾部分，支持实时跟踪",
            "usage": ["tail [选项] [文件...]"],
            "options": [
                {"flag": "-n <N>", "description": "显示最后N行（默认10行）"},
                {"flag": "-f", "description": "实时跟踪文件追加内容"},
                {"flag": "-F", "description": "跟踪并处理日志轮转"},
            ],
            "examples": [
                {"command": "tail -f /var/log/syslog", "description": "实时跟踪系统日志"},
                {"command": "tail -n 50 file.txt", "description": "显示文件最后50行"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["head", "less", "watch"],
        },
        {
            "name": "rsync",
            "category": "操作系统/通用Linux命令",
            "install_required": True,
            "install_method": "apt install rsync (Ubuntu) 或 yum install rsync (CentOS)",
            "description": "远程和本地文件同步工具，支持增量传输",
            "usage": ["rsync [选项] 源 目标"],
            "options": [
                {"flag": "-a, --archive", "description": "归档模式，保留权限和属性"},
                {"flag": "-v, --verbose", "description": "显示详细输出"},
                {"flag": "-z, --compress", "description": "传输时压缩数据"},
                {"flag": "-P", "description": "显示进度并支持断点续传"},
                {"flag": "--delete", "description": "删除目标中源没有的文件"},
                {"flag": "-e ssh", "description": "使用SSH作为传输通道"},
            ],
            "examples": [
                {"command": "rsync -avz /local/dir/ user@remote:/remote/dir/", "description": "同步本地目录到远程"},
                {"command": "rsync -avz --delete /src/ /dest/", "description": "镜像同步，删除目标多余文件"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["scp", "cp", "sftp"],
        },
        {
            "name": "export",
            "category": "操作系统/通用Linux命令",
            "install_required": False,
            "description": "设置或显示环境变量",
            "usage": ["export [选项] [名称[=值]...]"],
            "options": [
                {"flag": "-p", "description": "以可复用格式显示所有变量"},
                {"flag": "-n", "description": "从导出列表中移除变量"},
            ],
            "examples": [
                {"command": "export PATH=$PATH:/usr/local/bin", "description": "添加路径到PATH"},
                {"command": "export MY_VAR=value", "description": "设置环境变量"},
                {"command": "export -p", "description": "显示所有导出的变量"},
            ],
            "platforms": ["linux", "darwin", "unix"],
            "related_commands": ["env", "set", "unset"],
        },
    ],
    "data/container/kubernetes.yaml": [
        {
            "name": "kubectl",
            "category": "容器编排/Kubernetes命令",
            "install_required": True,
            "install_method": "参考 https://kubernetes.io/docs/tasks/tools/",
            "description": "Kubernetes命令行工具，管理集群资源",
            "usage": ["kubectl [命令] [类型] [名称] [选项]"],
            "options": [
                {"flag": "--namespace, -n", "description": "指定命名空间"},
                {"flag": "--context", "description": "指定kubeconfig上下文"},
                {"flag": "--kubeconfig", "description": "指定kubeconfig文件路径"},
                {"flag": "-o wide", "description": "显示更多列信息"},
                {"flag": "-o yaml", "description": "以YAML格式输出"},
                {"flag": "-o json", "description": "以JSON格式输出"},
            ],
            "examples": [
                {"command": "kubectl get nodes", "description": "查看所有节点"},
                {"command": "kubectl get pods -n kube-system", "description": "查看kube-system命名空间的Pod"},
                {"command": "kubectl describe pod mypod", "description": "查看Pod详细信息"},
                {"command": "kubectl apply -f deployment.yaml", "description": "应用YAML配置文件"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["kubectl get", "kubectl apply", "helm"],
        },
    ],
    "data/cloud/aws-cli.yaml": [
        {
            "name": "aws sts",
            "category": "云平台/AWS CLI",
            "install_required": True,
            "install_method": "参考 https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html",
            "description": "AWS Security Token Service，管理临时凭证",
            "usage": ["aws sts <命令> [选项]"],
            "options": [
                {"flag": "--duration-seconds", "description": "临时凭证有效期（秒）"},
            ],
            "examples": [
                {"command": "aws sts get-caller-identity", "description": "获取当前调用者身份"},
                {"command": "aws sts assume-role --role-arn arn:aws:iam::123456789012:role/MyRole --role-session-name mysession", "description": "扮演IAM角色获取临时凭证"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["aws configure", "aws iam", "aws s3"],
        },
    ],
    "data/lang/go.yaml": [
        {
            "name": "go install",
            "category": "编程语言/Go工具链",
            "install_required": False,
            "description": "编译并安装Go包到$GOPATH/bin",
            "usage": ["go install [选项] [包路径]@版本"],
            "options": [
                {"flag": "-x", "description": "打印执行的命令"},
            ],
            "examples": [
                {"command": "go install golang.org/x/tools/cmd/goimports@latest", "description": "安装最新版goimports"},
                {"command": "go install ./cmd/myapp", "description": "安装当前项目的命令"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["go get", "go build", "go run"],
        },
    ],
    "data/database/redis.yaml": [
        {
            "name": "redis",
            "category": "数据库工具/Redis工具",
            "install_required": True,
            "install_method": "apt install redis-server (Ubuntu) 或 yum install redis (CentOS)",
            "description": "启动Redis服务器",
            "usage": ["redis-server [配置文件] [选项]"],
            "options": [
                {"flag": "--port <port>", "description": "指定监听端口（默认6379）"},
                {"flag": "--daemonize yes", "description": "后台运行"},
                {"flag": "--requirepass <password>", "description": "设置密码"},
            ],
            "examples": [
                {"command": "redis-server /etc/redis/redis.conf", "description": "使用配置文件启动Redis"},
                {"command": "redis-server --port 6380", "description": "在6380端口启动Redis"},
            ],
            "platforms": ["linux", "darwin"],
            "related_commands": ["redis-cli", "redis-benchmark", "redis-sentinel"],
        },
    ],
    "data/lang/java.yaml": [
        {
            "name": "jhat",
            "category": "编程语言/Java工具链",
            "install_required": False,
            "description": "Java堆分析工具，分析堆转储文件",
            "usage": ["jhat [选项] <堆转储文件>"],
            "options": [
                {"flag": "-port <port>", "description": "HTTP服务器端口（默认7000）"},
                {"flag": "-J<flag>", "description": "传递给JVM的选项"},
            ],
            "examples": [
                {"command": "jhat heapdump.hprof", "description": "分析堆转储文件"},
                {"command": "jhat -port 8080 heapdump.hprof", "description": "在8080端口启动分析服务"},
            ],
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["jmap", "jcmd", "jvisualvm"],
        },
    ],
}


def add_commands_to_yaml(yaml_path: Path, new_commands: list):
    """Append new commands to existing YAML file."""
    text = yaml_path.read_text(encoding="utf-8")
    data = yaml.safe_load(text)

    existing_names = {c["name"] for c in data.get("commands", [])}
    added = 0

    for cmd in new_commands:
        if cmd["name"] in existing_names:
            print(f"  ⚠️  Skipping duplicate: {cmd['name']}")
            continue

        # Inherit category from file-level if not specified
        if "category" not in cmd:
            cmd["category"] = data.get("category", "")

        data.setdefault("commands", []).append(cmd)
        added += 1

    if added > 0:
        yaml_path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        print(f"  ✅ Added {added} commands to {yaml_path.name}")
    else:
        print(f"  ℹ️  No new commands for {yaml_path.name}")


def main():
    total_added = 0
    for rel_path, commands in MISSING_COMMANDS.items():
        yaml_path = PROJECT_ROOT / rel_path
        if not yaml_path.exists():
            print(f"  ❌ File not found: {yaml_path}")
            continue
        add_commands_to_yaml(yaml_path, commands)
        total_added += len(commands)

    print(f"\nTotal commands added: {total_added}")


if __name__ == "__main__":
    main()

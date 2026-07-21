#!/usr/bin/env python3
"""
补齐 Database、大数据、云原生、AI 等领域剩余高频真实命令。
"""
import sys
from pathlib import Path
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

DATA_DIR = Path("data")
META_PATH = DATA_DIR / "metadata.yaml"


def opt(flag_desc: str) -> dict:
    parts = flag_desc.split(" ", 1)
    return {"flag": parts[0], "description": parts[1] if len(parts) > 1 else ""}


def ex(cmd: str, desc: str) -> dict:
    return {"command": cmd, "description": desc}


def make_cmd(
    name: str,
    desc: str,
    category: str,
    usage: str = None,
    options: list = None,
    examples: list = None,
    related: list = None,
    install_required: bool = False,
    install_method: str = None,
    platforms: list = None,
    risk: str = "low",
    risk_desc: str = None,
) -> dict:
    if usage is None:
        usage = f"{name} [OPTIONS] [ARGS]"
    if options is None:
        options = ["--help 显示帮助信息", "--version 显示版本信息"]
    if examples is None:
        examples = [[f"{name} --help", "查看帮助"], [f"{name} --version", "查看版本"]]
    if platforms is None:
        platforms = ["linux", "darwin"]
    if related is None:
        related = []
    cmd = {
        "name": name,
        "category": category,
        "install_required": install_required,
        "description": desc,
        "usage": [usage],
        "options": [opt(o) for o in options],
        "examples": [ex(e[0], e[1]) for e in examples],
        "platforms": platforms,
        "related_commands": related,
    }
    if install_required and install_method:
        cmd["install_method"] = install_method
    if risk in ("medium", "high", "critical"):
        if risk_desc is None:
            risk_desc = "操作前请确认参数、目标环境和影响范围，建议在测试环境先行验证。"
        cmd["risks"] = [{"level": risk, "description": risk_desc}]
    return cmd


BATCH = {
    "database/more.yaml": {
        "category": "数据库工具/扩展命令",
        "description": "商业数据库、缓存、备份与云数据仓库扩展命令",
        "commands": [
            make_cmd("sqlplus", "Oracle 数据库 SQL*Plus 客户端", "数据库工具/扩展命令",
                     install_required=True, install_method="随 Oracle 客户端或 Instant Client 安装",
                     options=["-s 静默模式", "-l 只登录", "/@TNS 连接串"],
                     examples=[["sqlplus username/password@database", "连接 Oracle"], ["sqlplus -s / as sysdba <<EOF\nSELECT * FROM dual;\nEOF", "以 sysdba 执行 SQL"]],
                     related=["mysql", "psql"], risk="high", risk_desc="以 SYSDBA 连接可操作整个数据库，请严格控制权限"),
            make_cmd("sqlcmd", "SQL Server 命令行工具", "数据库工具/扩展命令",
                     install_required=True, install_method="参考 https://docs.microsoft.com/sql/tools/sqlcmd-utility",
                     options=["-S 服务器", "-d 数据库", "-U 用户", "-Q 查询", "-i 输入文件"],
                     examples=[["sqlcmd -S localhost -d mydb -U sa -Q 'SELECT @@VERSION'", "执行查询"], ["sqlcmd -S localhost -i script.sql -o output.txt", "执行脚本并输出"]],
                     related=["osql", "tsql"], risk="medium", risk_desc="sqlcmd 可直接执行 DDL/DML，生产环境请确认脚本内容"),
            make_cmd("db2", "IBM Db2 命令行处理器", "数据库工具/扩展命令",
                     install_required=True, install_method="随 IBM Db2 安装",
                     options=["connect to 连接", "list tables", "terminate"],
                     examples=[["db2 connect to sample", "连接 sample 数据库"], ["db2 'SELECT * FROM staff'", "执行 SQL"]],
                     related=["sqlplus", "sqlcmd"], risk="medium", risk_desc="Db2 命令可修改数据库对象，请在测试环境验证"),
            make_cmd("memcached", "Memcached 内存对象缓存守护进程", "数据库工具/扩展命令",
                     install_required=True, install_method="包管理器安装，如 sudo apt install memcached",
                     options=["-p 端口", "-m 内存大小", "-d 守护进程", "-l 监听地址"],
                     examples=[["memcached -m 64 -p 11211 -u nobody -l 127.0.0.1", "启动 memcached"], ["memcached -d -m 128 -c 1024", "后台运行 128MB 缓存"]],
                     related=["redis-cli", "telnet"], risk="medium", risk_desc="默认无认证，请勿直接暴露到公网，建议使用 SASL 或防火墙"),
            make_cmd("redis-benchmark", "Redis 性能测试工具", "数据库工具/扩展命令",
                     install_required=True, install_method="随 Redis 安装",
                     options=["-h 主机", "-p 端口", "-c 并发", "-n 请求数", "-t 测试命令"],
                     examples=[["redis-benchmark -q -n 100000", "快速压测"], ["redis-benchmark -t set,get -n 100000 -c 50", "测试 set/get"]],
                     related=["redis-cli", "memcached"], risk="high", risk_desc="压测会消耗 Redis 资源，请避开生产高峰"),
            make_cmd("redis-sentinel", "Redis 高可用 Sentinel 模式", "数据库工具/扩展命令",
                     install_required=True, install_method="随 Redis 安装",
                     options=["--sentinel", "--daemonize", "--port"],
                     examples=[["redis-sentinel /etc/redis/sentinel.conf", "启动 Sentinel"], ["redis-sentinel --sentinel --port 26379", "指定端口启动 Sentinel"]],
                     related=["redis-cli", "redis-server"], risk="medium", risk_desc="Sentinel 负责故障转移，配置错误会导致脑裂"),
            make_cmd("pt-query-digest", "Percona Toolkit 慢查询分析工具", "数据库工具/扩展命令",
                     install_required=True, install_method="参考 https://docs.percona.com/percona-toolkit/installation.html",
                     options=["--filter 过滤", "--limit 限制输出", "--output 输出格式"],
                     examples=[["pt-query-digest /var/log/mysql/slow.log", "分析慢查询日志"], ["pt-query-digest --limit 10 slow.log", "只显示 Top 10"]],
                     related=["mysql", "mysqldumpslow"], risk="low"),
            make_cmd("xtrabackup", "Percona XtraBackup 热备份工具", "数据库工具/扩展命令",
                     install_required=True, install_method="参考 https://docs.percona.com/percona-xtrabackup",
                     options=["--backup", "--prepare", "--target-dir", "--user", "--password"],
                     examples=[["xtrabackup --backup --target-dir=/backup/full", "全量热备份"], ["xtrabackup --prepare --target-dir=/backup/full", "准备备份"]],
                     related=["mysql", "mysqldump"], risk="medium", risk_desc="prepare 会修改备份文件，请保留原始备份副本"),
            make_cmd("mydumper", "多线程 MySQL 逻辑备份工具", "数据库工具/扩展命令",
                     install_required=True, install_method="参考 https://github.com/mydumper/mydumper/releases",
                     options=["--outputdir", "--threads", "--rows", "--regex"],
                     examples=[["mydumper -u root -p password -B mydb -o /backup", "备份数据库"], ["mydumper -B mydb --threads 4 -o /backup", "4 线程备份"]],
                     related=["myloader", "mysqldump"], risk="low", risk_desc="备份过程会加 FTWRL，可能影响写入，请在低峰期执行"),
            make_cmd("myloader", "多线程恢复 mydumper 备份", "数据库工具/扩展命令",
                     install_required=True, install_method="随 mydumper 安装",
                     options=["--directory", "--threads", "--database", "--overwrite-tables"],
                     examples=[["myloader -u root -p password -d /backup -B mydb", "恢复备份"], ["myloader -d /backup --threads 4", "4 线程恢复"]],
                     related=["mydumper", "mysql"], risk="high", risk_desc="恢复会覆盖目标库数据，请确认目标数据库正确"),
            make_cmd("scylla", "ScyllaDB 高性能 Cassandra 兼容数据库", "数据库工具/扩展命令",
                     install_required=True, install_method="参考 https://opensource.docs.scylladb.com/stable/getting-started/installation.html",
                     options=["--version", "--workdir", "--options-file"],
                     examples=[["scylla --version", "查看版本"], ["sudo systemctl start scylla-server", "启动 Scylla 服务"]],
                     related=["cqlsh", "cassandra-stress"], risk="medium", risk_desc="Scylla 是系统级服务，启动前请确认资源配置"),
            make_cmd("yugabyted", "YugabyteDB 集群生命周期管理命令", "数据库工具/扩展命令",
                     install_required=True, install_method="随 YugabyteDB 安装",
                     options=["start 启动", "stop 停止", "status 状态", "destroy 销毁"],
                     examples=[["yugabyted start", "启动本地集群"], ["yugabyted status", "查看状态"]],
                     related=["ysqlsh", "ycqlsh"], risk="high", risk_desc="destroy 会删除所有本地数据，请谨慎"),
            make_cmd("arangosh", "ArangoDB 多模型数据库 Shell", "数据库工具/扩展命令",
                     install_required=True, install_method="随 ArangoDB 安装",
                     options=["--server.endpoint", "--server.username", "--javascript.execute"],
                     examples=[["arangosh --server.endpoint tcp://localhost:8529", "连接 ArangoDB"], ["arangosh --javascript.execute script.js", "执行 JS 脚本"]],
                     related=["cypher-shell", "mongosh"], risk="medium", risk_desc="JS 脚本可删除数据库，请确认脚本内容"),
            make_cmd("rethinkdb", "RethinkDB 分布式文档数据库", "数据库工具/扩展命令",
                     install_required=True, install_method="参考 https://rethinkdb.com/docs/install/",
                     options=["--bind all", "--join 加入集群", "--directory 数据目录"],
                     examples=[["rethinkdb --bind all", "监听所有接口启动"], ["rethinkdb --join host:29015 --directory ./data", "加入集群"]],
                     related=["mongo", "redis"], risk="medium", risk_desc="默认无认证，请勿直接暴露公网"),
            make_cmd("influxd", "InfluxDB 数据库服务守护进程", "数据库工具/扩展命令",
                     install_required=True, install_method="参考 https://docs.influxdata.com/influxdb/latest/install/",
                     options=["--bolt-path", "--engine-path", "--http-bind-address", "--reporting-disabled"],
                     examples=[["influxd", "前台启动 InfluxDB"], ["influxd --http-bind-address=:8086", "指定 HTTP 地址"]],
                     related=["influx", "telegraf"], risk="medium", risk_desc="influxd 会监听网络端口，请配置认证和防火墙"),
            make_cmd("snowsql", "Snowflake 数据仓库命令行客户端", "数据库工具/扩展命令",
                     install_required=True, install_method="参考 https://docs.snowflake.com/en/user-guide/snowsql-install-config",
                     options=["-a 账户", "-u 用户", "-d 数据库", "-q 查询", "-f 文件"],
                     examples=[["snowsql -a myaccount -u myuser -d mydb", "登录 Snowflake"], ["snowsql -q 'SELECT CURRENT_VERSION()'", "执行查询"]],
                     related=["psql", "bigquery"], risk="low", risk_desc="请妥善保管账户名和凭据，避免在命令行中明文输入密码"),
            make_cmd("databricks", "Databricks CLI", "数据库工具/扩展命令",
                     install_required=True, install_method="pip install databricks-cli",
                     options=["clusters 管理集群", "jobs 管理作业", "fs DBFS 文件", "runs"],
                     examples=[["databricks clusters list", "列出集群"], ["databricks jobs run-now --job-id 1", "立即运行作业"]],
                     related=["spark-submit", "aws"], risk="medium", risk_desc="databricks 操作会产生云费用并影响作业，请确认参数"),
        ],
    },
    "bigdata/more.yaml": {
        "category": "大数据/扩展命令",
        "description": "大数据生态的扩展工具、调度与消息队列命令",
        "commands": [
            make_cmd("zkCli.sh", "ZooKeeper 命令行客户端", "大数据/扩展命令",
                     install_required=True, install_method="随 Apache ZooKeeper 安装",
                     options=["-server 服务器", "-timeout 超时"],
                     examples=[["zkCli.sh -server localhost:2181", "连接 ZooKeeper"], ["echo 'ls /' | zkCli.sh -server localhost:2181", "列出根节点"]],
                     related=["zookeeper-shell", "kafka-topics.sh"], risk="medium", risk_desc="删除 ZooKeeper 节点会影响依赖服务，请确认"),
            make_cmd("hbase hbck", "HBase 一致性检查与修复", "大数据/扩展命令",
                     usage="hbase hbck [OPTIONS]",
                     install_required=True, install_method="随 Apache HBase 安装",
                     options=["-details 详细信息", "-fix 修复", "-repair 修复所有"],
                     examples=[["hbase hbck", "检查 HBase 一致性"], ["hbase hbck -fix", "修复不一致"]],
                     related=["hbase shell", "hdfs"], risk="high", risk_desc="-fix/-repair 会修改 HBase 元数据，请在备份后执行"),
            make_cmd("pig", "Apache Pig 大数据分析平台", "大数据/扩展命令",
                     install_required=True, install_method="随 Apache Hadoop/Pig 安装",
                     options=["-x local|mapreduce", "-f 脚本", "-param 参数"],
                     examples=[["pig -x mapreduce script.pig", "以 MapReduce 模式运行"], ["pig -x local", "本地交互模式"]],
                     related=["hadoop", "hive"], risk="medium", risk_desc="Pig 脚本会读写 HDFS，请确认输入输出路径"),
            make_cmd("oozie", "Apache Oozie 工作流调度", "大数据/扩展命令",
                     install_required=True, install_method="随 Apache Oozie 安装",
                     options=["job 作业管理", "validate 验证", "info 信息"],
                     examples=[["oozie job -oozie http://localhost:11000/oozie -config job.properties -run", "提交工作流"], ["oozie validate workflow.xml", "验证 workflow"]],
                     related=["airflow", "hue"], risk="medium", risk_desc="Oozie 作业会调度 MapReduce/Hive 等，请确认依赖和资源"),
            make_cmd("airbyte", "Airbyte 数据集成平台 CLI", "大数据/扩展命令",
                     install_required=True, install_method="参考 https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart",
                     options=["local 本地部署", "status", "connections"],
                     examples=[["airbyte local deploy", "本地部署 Airbyte"], ["airbyte status", "查看状态"]],
                     related=["fivetran", "airflow", "dbt"], risk="medium", risk_desc="连接源和目标会涉及凭据，请使用 Secret 管理"),
            make_cmd("meltano", "ELT 数据管道与 dbt 编排工具", "大数据/扩展命令",
                     install_required=True, install_method="pip install meltano",
                     options=["init 初始化", "add 添加 tap/target", "run 运行管道", "test 测试"],
                     examples=[["meltano init myproject", "初始化项目"], ["meltano run tap-gitlab target-postgres dbt:run", "运行完整 ELT"]],
                     related=["airbyte", "dbt"], risk="medium", risk_desc="meltano run 会读写数据源和目标，请确认环境配置"),
            make_cmd("dremio-admin", "Dremio 数据湖引擎管理工具", "大数据/扩展命令",
                     install_required=True, install_method="随 Dremio 安装",
                     options=["backup 备份", "restore 恢复", "set-password"],
                     examples=[["dremio-admin backup -f /backup/dremio.zip", "备份 Dremio"], ["dremio-admin restore -f /backup/dremio.zip", "恢复"]],
                     related=["presto", "hive"], risk="high", risk_desc="restore 会覆盖现有元数据，请确认备份来源"),
            make_cmd("zeppelin", "Apache Zeppelin 交互式数据分析笔记本", "大数据/扩展命令",
                     install_required=True, install_method="参考 https://zeppelin.apache.org/docs/latest/quickstart/install.html",
                     options=["daemon.sh 启动/停止", "--config"],
                     examples=[["bin/zeppelin-daemon.sh start", "启动 Zeppelin"], ["bin/zeppelin-daemon.sh stop", "停止 Zeppelin"]],
                     related=["jupyter", "spark-submit"], risk="medium", risk_desc="Zeppelin 解释器可执行任意代码，请配置认证和权限"),
            make_cmd("superset", "Apache Superset 数据可视化平台", "大数据/扩展命令",
                     install_required=True, install_method="pip install apache-superset",
                     options=["db upgrade 升级元数据库", "fab create-admin", "run -p 端口", "load_examples"],
                     examples=[["superset db upgrade", "升级元数据库"], ["superset run -p 8088 --with-threads --reload --debugger", "开发模式启动"]],
                     related=["metabase", "dbt"], risk="medium", risk_desc="生产环境请关闭 debugger 和 reload，并配置认证"),
            make_cmd("metabase", "开源 BI 与数据探索平台", "大数据/扩展命令",
                     install_required=True, install_method="参考 https://www.metabase.com/start/oss/",
                     options=["-Xmx 最大内存", "-Dlog4j.configurationFile", "--add-to-start"],
                     examples=[["java -jar metabase.jar", "启动 Metabase"], ["MB_DB_CONNECTION_URI='...' java -jar metabase.jar", "使用外部数据库"]],
                     related=["superset", "grafana"], risk="medium", risk_desc="Metabase 会连接数据库，请使用只读账户并限制权限"),
            make_cmd("atlas-admin", "Apache Atlas 元数据管理命令", "大数据/扩展命令",
                     install_required=True, install_method="随 Apache Atlas 安装",
                     options=["-import", "-export", "-status"],
                     examples=[["bin/atlas_admin.py -status", "查看 Atlas 状态"], ["bin/import-export.py -i metadata.json", "导入元数据"]],
                     related=["hive", "kafka"], risk="medium", risk_desc="导入导出元数据会影响数据目录，请确认内容"),
            make_cmd("nifi-toolkit", "Apache NiFi 命令行工具包", "大数据/扩展命令",
                     install_required=True, install_method="随 Apache NiFi 安装",
                     options=["tls 证书生成", "encrypt-config", "file-manager"],
                     examples=[["bin/tls-toolkit.sh standalone -n 'nifi[1-3].example.com' -C 'CN=admin'", "生成 TLS 证书"], ["bin/encrypt-config.sh", "加密配置"]],
                     related=["nifi", "openssl"], risk="high", risk_desc="加密配置前请备份，丢失密钥将无法解密"),
            make_cmd("kafka-mirror-maker", "Kafka 跨集群镜像复制工具", "大数据/扩展命令",
                     install_required=True, install_method="随 Apache Kafka 安装",
                     options=["--consumer.config", "--producer.config", "--whitelist"],
                     examples=[["kafka-mirror-maker.sh --consumer.config consumer.properties --producer.config producer.properties --whitelist '.*'", "镜像所有 topic"], ["kafka-mirror-maker.sh --whitelist 'topic1,topic2'", "只镜像指定 topic"]],
                     related=["kafka-topics.sh", "debezium"], risk="high", risk_desc="镜像会复制大量数据并可能覆盖目标集群，请确认白名单和 offset 策略"),
            make_cmd("kafka-acls.sh", "Kafka ACL 权限管理", "大数据/扩展命令",
                     install_required=True, install_method="随 Apache Kafka 安装",
                     options=["--add 添加", "--remove 删除", "--list 列出", "--allow-principal", "--operation"],
                     examples=[["kafka-acls.sh --bootstrap-server localhost:9092 --list", "列出 ACL"], ["kafka-acls.sh --add --allow-principal User:alice --operation Read --topic mytopic", "添加读权限"]],
                     related=["kafka-topics.sh", "kafka-configs.sh"], risk="high", risk_desc="错误的 ACL 会导致服务无法访问或过度授权"),
            make_cmd("kafka-reassign-partitions.sh", "Kafka 分区重分配工具", "大数据/扩展命令",
                     install_required=True, install_method="随 Apache Kafka 安装",
                     options=["--bootstrap-server", "--topics-to-move-json-file", "--generate", "--execute", "--verify"],
                     examples=[["kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --topics-to-move-json-file topics.json --broker-list 0,1,2 --generate", "生成分配计划"], ["kafka-reassign-partitions.sh --reassignment-json-file plan.json --execute", "执行重分配"]],
                     related=["kafka-topics.sh", "kafka-configs.sh"], risk="high", risk_desc="分区重分配会移动大量数据并影响性能，请先在低峰期验证"),
            make_cmd("rabbitmqctl", "RabbitMQ 消息队列管理 CLI", "大数据/扩展命令",
                     install_required=True, install_method="随 RabbitMQ 安装",
                     options=["list_queues 列出队列", "list_exchanges", "add_user", "set_permissions"],
                     examples=[["rabbitmqctl list_queues", "列出队列"], ["rabbitmqctl add_user admin password && rabbitmqctl set_user_tags admin administrator", "添加管理员"]],
                     related=["kafka-topics.sh", "mqtt"], risk="medium", risk_desc="修改用户/权限会影响消息队列访问，请确认策略"),
        ],
    },
    "container/cloudnative-more.yaml": {
        "category": "容器编排/云原生扩展二",
        "description": "容器运行时、本地开发、多集群、Secret 管理等云原生扩展命令",
        "commands": [
            make_cmd("containerd", "容器运行时 daemon", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://github.com/containerd/containerd/blob/main/docs/getting-started.md",
                     options=["--config 配置文件", "--log-level"],
                     examples=[["sudo containerd", "启动 containerd"], ["sudo containerd -c /etc/containerd/config.toml", "指定配置启动"]],
                     related=["ctr", "nerdctl"], risk="medium", risk_desc="containerd 是底层运行时，配置错误会导致容器无法启动"),
            make_cmd("ctr", "containerd 官方 CLI", "容器编排/云原生扩展二",
                     install_required=True, install_method="随 containerd 安装",
                     options=["images 镜像", "containers 容器", "run 运行", "pull 拉取"],
                     examples=[["ctr images ls", "列出镜像"], ["ctr run docker.io/library/nginx:latest nginx", "运行容器"]],
                     related=["nerdctl", "crictl"], risk="medium", risk_desc="ctr 直接操作 containerd，可能影响 Kubernetes 容器"),
            make_cmd("crictl", "兼容 CRI 的容器运行时 CLI", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md",
                     options=["pods", "ps", "images", "logs", "exec"],
                     examples=[["crictl pods", "列出 Pod"], ["crictl logs <container-id>", "查看容器日志"]],
                     related=["kubectl", "ctr"], risk="medium", risk_desc="crictl 可直接删除运行中容器，生产环境请谨慎"),
            make_cmd("lxc", "Linux 容器（LXC）管理", "容器编排/云原生扩展二",
                     install_required=True, install_method="包管理器安装，如 sudo apt install lxc",
                     options=["launch 创建", "list 列出", "exec 执行", "stop 停止"],
                     examples=[["lxc launch ubuntu:22.04 mycontainer", "创建容器"], ["lxc exec mycontainer -- bash", "进入容器"]],
                     related=["lxd", "docker"], risk="medium", risk_desc="特权容器可能逃逸，请限制权限"),
            make_cmd("lxd", "LXC 系统容器管理守护进程", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://documentation.ubuntu.com/lxd/en/latest/installing/",
                     options=["init 初始化", "list", "launch", "exec"],
                     examples=[["lxd init", "初始化 LXD"], ["lxc list", "列出 LXD 容器"]],
                     related=["lxc", "incus"], risk="medium", risk_desc="LXD 是系统级服务，请正确配置存储和网络"),
            make_cmd("incus", "LXD 社区分支（Canonical 替代方案）", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://linuxcontainers.org/incus/docs/main/installing/",
                     options=["admin init", "list", "launch", "exec"],
                     examples=[["incus admin init", "初始化 Incus"], ["incus launch images:ubuntu/22.04 c1", "创建容器"]],
                     related=["lxd", "lxc"], risk="medium", risk_desc="同 LXD，需注意存储和网络配置"),
            make_cmd("firecracker", "AWS 开源微虚拟机（microVM）", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://github.com/firecracker-microvm/firecracker",
                     options=["--api-sock", "--config-file", "--id"],
                     examples=[["firecracker --api-sock /tmp/firecracker.sock", "启动 API 服务"], ["curl --unix-socket /tmp/firecracker.sock -X PUT http://localhost/mmds -d '{\"latest\":{}}'", "配置 MMDS"]],
                     related=["kata-runtime", "containerd"], risk="medium", risk_desc="Firecracker 直接运行微虚拟机，需配置安全组和资源限制"),
            make_cmd("kata-runtime", "Kata Containers 运行时", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://github.com/kata-containers/kata-containers/blob/main/docs/install/README.md",
                     options=["version", "check", "factory"],
                     examples=[["kata-runtime version", "查看版本"], ["kata-runtime check", "检查系统兼容性"]],
                     related=["containerd", "firecracker"], risk="medium", risk_desc="Kata 使用 VM，需确认内核和虚拟化支持"),
            make_cmd("telepresence", "本地开发连接远程 Kubernetes 服务", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://www.telepresence.io/docs/latest/install/",
                     options=["connect 连接", "intercept 拦截", "list 列出", "quit 退出"],
                     examples=[["telepresence connect", "连接集群"], ["telepresence intercept myservice --port 8080:http", "拦截服务到本地"]],
                     related=["kubectl", "devspace"], risk="high", risk_desc="intercept 会将生产流量引到本地，请确认目标环境和回滚策略"),
            make_cmd("devspace", "Kubernetes 本地开发工作流", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://www.devspace.sh/docs/getting-started/install",
                     options=["dev 启动开发模式", "deploy 部署", "purge 清理", "logs"],
                     examples=[["devspace dev", "进入开发模式"], ["devspace deploy", "部署到集群"]],
                     related=["telepresence", "okteto"], risk="medium", risk_desc="devspace deploy 会修改集群，请确认 namespace 和 values"),
            make_cmd("okteto", "云端到本地的 Kubernetes 开发环境", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://www.okteto.com/docs/getting-started/",
                     options=["up 启动开发环境", "down 停止", "context", "deploy"],
                     examples=[["okteto up", "启动 Okteto 开发环境"], ["okteto context use https://okteto.example.com", "切换上下文"]],
                     related=["devspace", "telepresence"], risk="medium", risk_desc="okteto up 会同步本地代码到集群，请确认忽略文件"),
            make_cmd("vcluster", "Kubernetes 虚拟集群", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://www.vcluster.com/docs/getting-started/install",
                     options=["create 创建", "connect 连接", "list", "delete"],
                     examples=[["vcluster create my-vcluster", "创建虚拟集群"], ["vcluster connect my-vcluster", "连接虚拟集群"]],
                     related=["kind", "k3s"], risk="medium", risk_desc="vcluster 共享宿主机集群资源，请注意配额和权限"),
            make_cmd("kn", "Knative 命令行工具", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://knative.dev/docs/client/install/",
                     options=["service 管理服务", "revision", "route", "plugin"],
                     examples=[["kn service create hello --image gcr.io/knative-samples/helloworld-go", "创建 Knative 服务"], ["kn service list", "列出服务"]],
                     related=["kubectl", "istio"], risk="medium", risk_desc="kn service delete 会删除 Serverless 服务，请确认"),
            make_cmd("dapr", "分布式应用运行时 CLI", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://docs.dapr.io/getting-started/install-dapr-cli/",
                     options=["init 初始化", "run 运行", "publish", "invoke"],
                     examples=[["dapr init", "初始化 Dapr"], ["dapr run --app-id myapp --app-port 8080 -- python app.py", "带 Dapr sidecar 运行应用"]],
                     related=["kubectl", "service-mesh"], risk="medium", risk_desc="dapr init 会部署控制平面，请确认 Kubernetes 上下文"),
            make_cmd("kubeseal", "Sealed Secrets 加密 CLI", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://github.com/bitnami-labs/sealed-secrets/releases",
                     options=["--format yaml|json", "--scope", "--cert"],
                     examples=[["kubeseal < secret.yaml > sealedsecret.yaml", "加密 Secret"], ["kubeseal --controller-namespace=kube-system --fetch-cert > cert.pem", "获取公钥"]],
                     related=["kubectl", "sops"], risk="low", risk_desc="Sealed Secrets 是单向加密，请保留原始 Secret 备份"),
            make_cmd("sops", "文件加密编辑器（支持 AWS/GCP/Azure/KMS）", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://github.com/getsops/sops/releases",
                     options=["-e 加密", "-d 解密", "--kms", "--pgp"],
                     examples=[["sops -e -i secret.yaml", "原地加密"], ["sops -d secret.yaml", "解密查看"]],
                     related=["kubeseal", "gpg"], risk="high", risk_desc="加密后丢失 KMS/PGP 密钥将无法解密，请妥善保存"),
            make_cmd("esoctl", "External Secrets Operator 工具（kubectl 插件）", "容器编排/云原生扩展二",
                     install_required=True, install_method="kubectl krew install external-secrets",
                     options=["get secrets", "get secretstores", "validate"],
                     examples=[["kubectl externalsecrets get secrets", "列出外部同步的 Secret"], ["kubectl externalsecrets get secretstores", "列出 SecretStore"]],
                     related=["kubeseal", "vault"], risk="medium", risk_desc="错误的 SecretStore 会同步错误凭据，请确认 provider 配置"),
            make_cmd("hubble", "Cilium 可观测性 CLI", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://docs.cilium.io/en/stable/gettingstarted/hubble_setup/",
                     options=["observe 观察流", "status 状态", "list nodes"],
                     examples=[["hubble observe", "观察网络流"], ["hubble observe --pod default/myapp", "观察指定 Pod 流"]],
                     related=["cilium", "kubectl"], risk="low", risk_desc="observe 会采集网络元数据，注意隐私合规"),
            make_cmd("subctl", "Submariner 跨集群网络 CLI", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://submariner.io/operations/deployment/subctl/",
                     options=["deploy-broker", "join", "show connections", "verify"],
                     examples=[["subctl deploy-broker", "部署 broker"], ["subctl join --kubeconfig cluster2.kubeconfig broker-info.subm", "加入集群"]],
                     related=["kubectl", "cilium"], risk="high", risk_desc="跨集群网络会打通多个集群，请确认 CIDR 不冲突"),
            make_cmd("longhornctl", "Longhorn 分布式存储管理", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://longhorn.io/docs/",
                     options=["install", "uninstall", "check"],
                     examples=[["longhornctl install", "安装 Longhorn"], ["longhornctl check", "检查环境"]],
                     related=["kubectl", "rookctl"], risk="high", risk_desc="卸载 Longhorn 会丢失卷数据，请先备份"),
            make_cmd("rookctl", "Rook Ceph 存储管理", "容器编排/云原生扩展二",
                     install_required=True, install_method="Rook 使用 kubectl 与 CRD 管理，无独立 CLI，可用 kubectl rook-ceph 插件",
                     options=["mon", "osd", "status"],
                     examples=[["kubectl rook-ceph health", "查看 Ceph 健康"], ["kubectl rook-ceph ceph status", "执行 ceph status"]],
                     related=["kubectl", "longhornctl"], risk="high", risk_desc="直接操作 Ceph 集群会影响存储，请确认命令影响"),
            make_cmd("certbot", "Let's Encrypt 证书自动申请工具", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://certbot.eff.org/instructions",
                     options=["certonly", "--standalone", "--nginx", "--dns-cloudflare", "--renew"],
                     examples=[["sudo certbot certonly --standalone -d example.com", "申请证书"], ["sudo certbot renew --dry-run", "测试续期"]],
                     related=["cert-manager", "openssl"], risk="medium", risk_desc="生产环境 renew 前请先用 dry-run 验证"),
            make_cmd("argo-rollouts", "Argo Rollouts 渐进式交付 CLI", "容器编排/云原生扩展二",
                     install_required=True, install_method="kubectl krew install argo-rollouts",
                     options=["list", "get", "promote", "abort", "restart"],
                     examples=[["kubectl argo rollouts list rollouts", "列出 Rollouts"], ["kubectl argo rollouts promote my-rollout", "推进 rollout"]],
                     related=["argocd", "flagger"], risk="high", risk_desc="promote/abort 会改变生产流量分布，请确认指标健康"),
            make_cmd("flagger", "Flagger 渐进式交付控制器", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://flagger.app/install/flagger-install-on-kubernetes/",
                     options=["loadtester", "generate"],
                     examples=[["kubectl apply -k github.com/fluxcd/flagger//kustomize/base", "安装 Flagger"], ["flagger generate -n test", "生成示例 canary"]],
                     related=["argocd", "argo-rollouts"], risk="high", risk_desc="Canary 发布会影响生产流量，请配置正确阈值"),
            make_cmd("keptn", "Keptn 云原生应用生命周期编排", "容器编排/云原生扩展二",
                     install_required=True, install_method="参考 https://keptn.sh/docs/install/",
                     options=["install", "create project", "trigger delivery", "get event"],
                     examples=[["keptn install", "安装 Keptn"], ["keptn trigger delivery --project=myproj --service=mysvc --image=myimage:v2", "触发交付"]],
                     related=["argocd", "flagger"], risk="medium", risk_desc="Keptn 编排会影响部署和 SLO 评估，请确认配置"),
            make_cmd("backstage", "Backstage 开发者门户 CLI", "容器编排/云原生扩展二",
                     install_required=True, install_method="npx @backstage/create-app@latest",
                     options=["create-app", "dev", "build", "test"],
                     examples=[["npx @backstage/create-app@latest", "创建 Backstage 应用"], ["yarn dev", "启动开发服务器"]],
                     related=["port", "kubernetes"], risk="low", risk_desc="backstage 应用涉及大量插件，注意依赖版本安全"),
        ],
    },
    "ai/more.yaml": {
        "category": "AI基础设施/扩展命令",
        "description": "大模型 API 客户端、AI 编码助手、MLOps 与可观测扩展命令",
        "commands": [
            make_cmd("openai", "OpenAI 官方 CLI", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install openai",
                     options=["api 调用 API", "chat.completions.create", "models list"],
                     examples=[["openai api chat.completions.create -m gpt-4 -g user 'Hello'", "调用 ChatGPT"], ["openai api models.list", "列出模型"]],
                     related=["groq", "anthropic"], risk="low", risk_desc="注意 API key 不要硬编码，建议使用环境变量"),
            make_cmd("anthropic", "Anthropic Claude CLI", "AI基础设施/扩展命令",
                     install_required=True, install_method="npm install -g @anthropic-ai/claude-cli 或参考官方",
                     options=["--model", "--max-tokens", "--temperature"],
                     examples=[["anthropic 'Explain transformers'", "向 Claude 提问"], ["anthropic --model claude-3-opus --max-tokens 2048", "指定模型"]],
                     related=["openai", "claude"], risk="low"),
            make_cmd("cohere", "Cohere 命令行工具", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install cohere 或参考官方 SDK",
                     options=["chat", "embed", "classify"],
                     examples=[["cohere chat --message 'Hello'", "聊天"], ["cohere embed --texts 'hello world'", "生成向量"]],
                     related=["openai", "mistral"], risk="low"),
            make_cmd("mistral", "Mistral AI CLI", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install mistralai 或参考官方",
                     options=["chat", "list models"],
                     examples=[["mistral chat --message 'Explain RAG'", "聊天"], ["mistral list-models", "列出模型"]],
                     related=["openai", "cohere"], risk="low"),
            make_cmd("aider", "AI 结对编程助手", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install aider-chat",
                     options=["--model", "--edit-format", "--commit"],
                     examples=[["aider", "启动交互式会话"], ["aider --model gpt-4 --commit", "指定模型并自动提交"]],
                     related=["swe-agent", "continue-dev"], risk="high", risk_desc="aider 会自动修改代码并提交，请使用 git 分支并通过 CI 审查"),
            make_cmd("litellm", "统一多 LLM API 的网关/代理", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install 'litellm[proxy]'",
                     options=["--model", "--temperature", "--proxy 启动代理"],
                     examples=[["litellm --model gpt-4 --temperature 0.2", "CLI 调用"], ["litellm --proxy --model gpt-4", "启动代理"]],
                     related=["openai", "groq"], risk="medium", risk_desc="代理会转发 API key，请配置访问控制和日志脱敏"),
            make_cmd("metaflow", "Netflix 机器学习工作流框架", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install metaflow",
                     options=["run 运行 flow", "status", "logs", "card"],
                     examples=[["python flow.py run", "运行 Metaflow"], ["python flow.py card view", "查看结果卡片"]],
                     related=["airflow", "mlflow"], risk="medium", risk_desc="Metaflow 会访问云存储和计算资源，请确认配置"),
            make_cmd("zenml", "MLOps 管道编排工具", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install zenml",
                     options=["init 初始化", "stack register", "pipeline run", "server"],
                     examples=[["zenml init", "初始化项目"], ["zenml stack set default", "设置默认 stack"]],
                     related=["mlflow", "metaflow"], risk="medium", risk_desc="zenml stack 涉及云凭据，请安全存储"),
            make_cmd("flyte", "大规模机器学习与数据工作流平台", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install flytekit",
                     options=["run 本地运行", "register 注册", "pyflyte"],
                     examples=[["pyflyte run workflow.py my_workflow", "本地运行 workflow"], ["pyflyte register workflow.py", "注册到 Flyte"]],
                     related=["airflow", "kubeflow"], risk="medium", risk_desc="register 会部署到 Flyte 集群，请确认版本和依赖"),
            make_cmd("weave", "Weights & Biases Weave 可观测工具", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install weave",
                     options=["init", "trace", "eval"],
                     examples=[["weave.init('project')", "初始化项目"], ["weave trace my_function()", "追踪函数调用"]],
                     related=["wandb", "mlflow"], risk="low"),
            make_cmd("comet", "Comet.ml 实验跟踪平台", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install comet-ml",
                     options=["init", "online", "offline", "upload"],
                     examples=[["comet init", "初始化"], ["comet upload offline.zip", "上传离线实验"]],
                     related=["wandb", "neptune"], risk="low"),
            make_cmd("neptune", "Neptune.ai 实验跟踪", "AI基础设施/扩展命令",
                     install_required=True, install_method="pip install neptune",
                     options=["run", "status", "sync"],
                     examples=[["neptune run", "运行并跟踪实验"], ["neptune sync", "同步离线数据"]],
                     related=["wandb", "comet"], risk="low"),
        ],
    },
}


def main() -> int:
    meta = yaml.load(open(META_PATH, "r", encoding="utf-8"))
    existing_names = set()
    for rel_file in meta["data_files"]:
        path = DATA_DIR / rel_file
        if not path.exists():
            continue
        doc = yaml.load(open(path, "r", encoding="utf-8"))
        for cmd in doc.get("commands", []):
            existing_names.add(cmd["name"])

    total_added = 0
    for rel_file, spec in BATCH.items():
        path = DATA_DIR / rel_file
        path.parent.mkdir(parents=True, exist_ok=True)
        commands = []
        skipped = []
        for cmd in spec["commands"]:
            if cmd["name"] in existing_names:
                skipped.append(cmd["name"])
                continue
            commands.append(cmd)
            existing_names.add(cmd["name"])
        if not commands:
            print(f"{rel_file}: all commands already exist, skipped")
            continue
        doc = {"category": spec["category"], "description": spec["description"], "commands": commands}
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(doc, f)
        cat_id = rel_file.replace("/", "_").replace("-", "_").replace(".", "_")
        meta["categories"][cat_id] = {
            "id": cat_id,
            "name": spec["category"],
            "description": spec["description"],
            "parent": "",
            "order": 300,
        }
        if rel_file not in meta["data_files"]:
            meta["data_files"].append(rel_file)
        print(f"{rel_file}: added {len(commands)}, skipped {len(skipped)}")
        total_added += len(commands)

    cmd_count = 0
    for rel_file in meta["data_files"]:
        doc = yaml.load(open(DATA_DIR / rel_file, "r", encoding="utf-8"))
        cmd_count += len(doc["commands"])
    meta["description"] = f"cmd4coder 命令行工具大全数据文件 - 覆盖 {len(meta['categories'])} 个分类, {cmd_count} 命令"

    with open(META_PATH, "w", encoding="utf-8") as f:
        yaml.dump(meta, f)
    print(f"\nTotal added: {total_added}, total commands: {cmd_count}, categories: {len(meta['categories'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

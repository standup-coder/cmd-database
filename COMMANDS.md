# cmd4coder 完整命令清单

**总命令数**: 459

| 序号 | 命令 | 风险等级 | 平台 | 描述 |
| --- | --- | --- | --- | --- |
| 1 | `otelcol-contrib` | medium |  | Start OpenTelemetry Collector Contrib distribution |
| 2 | `kubectl port-forward svc/istio-ingressgateway` | low |  | Access Kubeflow dashboard locally |
| 3 | `fluent-bit -c` | medium |  | Start Fluent Bit with configuration file |
| 4 | `kubectl get tfjobs` | low |  | List Kubeflow TensorFlow training jobs |
| 5 | `ufw status` | low |  | Show firewall status and rules |
| 6 | `kubectl config current-context` | medium |  | 显示当前配置上下文 |
| 7 | `host` | low |  | 简单的DNS查询工具 |
| 8 | `createuser` | high |  | Create a new PostgreSQL user |
| 9 | `dashboard` | low |  | Display real-time dashboard of JVM metrics |
| 10 | `pg_isready` | low |  | Check PostgreSQL server connection status |
| 11 | `mysqldump` | medium |  | MySQL database backup utility |
| 12 | `redis-cli INFO` | low |  | Get Redis server information and statistics |
| 13 | `yum list installed` | low |  | List all installed packages |
| 14 | `mysqlbinlog` | high |  | Process MySQL binary log files |
| 15 | `terraform taint` | high |  | Mark resource for recreation on next apply |
| 16 | `etcdctl snapshot restore` | critical |  | Restore etcd cluster from backup snapshot |
| 17 | `systemctl restart` | medium |  | Restart a systemd service |
| 18 | `helm uninstall` | critical |  | Uninstall Helm release from cluster |
| 19 | `kubectl get workflows` | low |  | List Kubeflow Pipelines workflows |
| 20 | `kfp pipeline list` | low |  | List Kubeflow Pipelines |
| 21 | `cilium connectivity test` | medium |  | Run connectivity test between pods |
| 22 | `docker stop` | low |  | 停止运行中的容器 |
| 23 | `trivy k8s` | low |  | Scan Kubernetes cluster for security issues |
| 24 | `pwd` | low |  | 显示当前工作目录的完整路径 |
| 25 | `kubectl exec` | high |  | Execute a command in a container |
| 26 | `vacuumdb` | medium |  | Garbage-collect and analyze a PostgreSQL database |
| 27 | `kubectl get storagepools` | low |  | List StoragePool resources (specific storage systems) |
| 28 | `mvn archetype` | low |  | Maven 项目原型生成工具 |
| 29 | `act` | medium |  | 本地运行 GitHub Actions 工作流（无需推送到 GitHub） |
| 30 | `docker pull` | low |  | 从镜像仓库拉取镜像 |
| 31 | `eksctl get cluster` | low |  | List AWS EKS clusters |
| 32 | `helm version` | low |  | Display Helm client and server version |
| 33 | `terraform workspace select` | medium |  | Switch to different Terraform workspace |
| 34 | `mvn` | high |  | Apache Maven 项目管理工具，用于构建和管理 Java 项目 |
| 35 | `kubectl get scrapeconfigs` | low |  | List ScrapeConfig resources for external target monitoring |
| 36 | `kubectl top` | low |  | 查看资源使用情况，识别性能瓶颈 |
| 37 | `rustc` | low |  | Rust 编译器 |
| 38 | `gcloud container clusters list` | low |  | List Google GKE clusters |
| 39 | `kubectl exec -it` | medium |  | 进入容器执行网络诊断命令 |
| 40 | `kubectl get storageclass` | low |  | List StorageClass resources defining storage provisioners |
| 41 | `crictl pods` | low |  | List all pods |
| 42 | `thread` | low |  | Display thread information |
| 43 | `trivy config` | low |  | Scan configuration files for misconfigurations |
| 44 | `otel-cli status server` | low |  | Check OpenTelemetry endpoint status |
| 45 | `nslookup` | low |  | 查询DNS信息 |
| 46 | `helm upgrade` | high |  | Upgrade Helm release to new version |
| 47 | `apt update` | low |  | Update package index from repositories |
| 48 | `amtool silence add` | medium |  | Add silence to Alertmanager |
| 49 | `ss` | low |  | socket统计信息(替代netstat) |
| 50 | `getenforce` | low |  | Get current SELinux mode |
| 51 | `shfmt` | low |  | Shell 脚本格式化工具 |
| 52 | `kubens` | medium |  | Switch between Kubernetes namespaces |
| 53 | `yum info` | low |  | Show package information |
| 54 | `kubectl get volumesnapshotcontent` | low |  | List VolumeSnapshotContent resources representing actual snapshots |
| 55 | `kubeadm token list` | low |  | List bootstrap tokens on the cluster |
| 56 | `bash` | low |  | Bash Shell 解释器，执行脚本文件或交互式命令 |
| 57 | `terraform output` | low |  | Display Terraform output values |
| 58 | `cat` | low |  | 连接文件并输出到标准输出 |
| 59 | `telepresence intercept` | critical |  | Intercept traffic to service and redirect to local process |
| 60 | `grafana-server` | medium |  | Start Grafana visualization server |
| 61 | `k9s` | medium |  | Interactive terminal UI for Kubernetes |
| 62 | `gh action` | low |  | 管理 GitHub Actions |
| 63 | `eksctl create cluster` | critical |  | Create AWS EKS Kubernetes cluster |
| 64 | `kubectl get networkpolicies` | low |  | List NetworkPolicy resources for traffic control |
| 65 | `otelcol` | medium |  | Start OpenTelemetry Collector |
| 66 | `systemctl disable` | low |  | Disable service from starting on boot |
| 67 | `classloader` | low |  | Display classloader information |
| 68 | `systemctl status falco` | medium |  | Check Falco runtime security service status |
| 69 | `crictl images` | low |  | List container images |
| 70 | `kubectl get limitranges` | low |  | List LimitRange resources for resource constraints |
| 71 | `kubectl cp` | high |  | Copy files between local filesystem and pod |
| 72 | `httpie` | medium |  | User-friendly HTTP client |
| 73 | `snap install` | low |  | Install snap package |
| 74 | `systemctl status promtail` | medium |  | Check Promtail service status |
| 75 | `ping` | low |  | 测试网络连通性 |
| 76 | `kubectl get imagepolicies` | low |  | List ImagePolicy resources for image validation |
| 77 | `cp` | medium |  | 复制文件或目录 |
| 78 | `git commit` | low |  | 提交暂存区的更改 |
| 79 | `npm start` | medium |  | Run the start script defined in package.json |
| 80 | `kubectl get endpointslices` | low |  | List EndpointSlice resources showing service endpoints |
| 81 | `alertmanager` | medium |  | Start Prometheus Alertmanager |
| 82 | `mysql_secure_installation` | medium |  | Script to improve MySQL installation security |
| 83 | `ansible-playbook` | high |  | Execute Ansible playbook |
| 84 | `velero schedule create` | low |  | Create scheduled backup |
| 85 | `tsar --check` | low |  | Check tsar configuration and data files |
| 86 | `siege` | high |  | HTTP load testing and benchmarking utility |
| 87 | `kubectl rollout` | high |  | Manage the rollout of a resource |
| 88 | `cilium status` | low |  | Check Cilium agent status |
| 89 | `ctr containers list` | low |  | List containers in containerd |
| 90 | `kubectl top pvc` | low |  | Show PVC resource usage (if metrics available) |
| 91 | `npm run` | medium |  | Run arbitrary package scripts |
| 92 | `kubectl port-forward svc/ml-pipeline-ui` | low |  | Access Kubeflow Pipelines UI locally |
| 93 | `redis-sentinel` | high |  | Redis Sentinel for high availability |
| 94 | `kubectl get events` | low |  | 获取集群事件信息，用于故障诊断 |
| 95 | `helm repo update` | low |  | Update local Helm chart repository cache |
| 96 | `kubectl logs -l serving.kserve.io/inferenceservice` | low |  | View logs for KServe model serving pods |
| 97 | `docker-compose` | low |  | 管理多容器应用 |
| 98 | `git pull` | low |  | 拉取远程更改并合并 |
| 99 | `git log` | low |  | 查看提交历史 |
| 100 | `kubectl logs -f deployment/prometheus-operator` | low |  | Stream logs from Prometheus Operator for troubleshooting |
| 101 | `traceroute` | low |  | 跟踪数据包的路由路径 |
| 102 | `istioctl proxy-status` | low |  | Check Envoy proxy status in service mesh |
| 103 | `grafana-cli plugins update` | medium |  | Update Grafana plugin |
| 104 | `systemctl status kube-state-metrics` | low |  | Check kube-state-metrics service status |
| 105 | `mvn dependency` | low |  | Maven 依赖管理子命令 |
| 106 | `docker rm` | medium |  | 删除容器 |
| 107 | `ls` | low |  | 列出目录内容 |
| 108 | `kubeadm join` | high |  | Join worker node to Kubernetes cluster |
| 109 | `ufw enable` | high |  | Enable Ubuntu firewall |
| 110 | `calicoctl get networkpolicies` | low |  | List Calico network policies |
| 111 | `kubectl get ingressclasses` | low |  | List IngressClass resources defining ingress controller types |
| 112 | `crictl stats` | low |  | Display container resource usage statistics |
| 113 | `apt remove` | high |  | Remove installed packages |
| 114 | `amtool check-config` | low |  | Validate Alertmanager configuration |
| 115 | `kfp run submit` | medium |  | Submit a Kubeflow Pipeline run |
| 116 | `redis-check-aof` | high |  | Check and repair Redis AOF (Append-Only File) |
| 117 | `helm dependency` | low |  | Manage chart dependencies |
| 118 | `kubectl get` | low |  | Display one or many resources |
| 119 | `kubectl get servicemonitors` | low |  | List ServiceMonitor resources for automatic service discovery |
| 120 | `gh run` | medium |  | 查看和管理 GitHub Actions 运行记录 |
| 121 | `kubectl get ciliumnetworkpolicies` | low |  | List CiliumNetworkPolicy resources for advanced networking |
| 122 | `systemctl status containerd` | high |  | Check containerd service status |
| 123 | `svn info` | low |  | Display information about working copy or repository |
| 124 | `etcdctl member list` | low |  | List all etcd cluster members |
| 125 | `mysqlcheck` | medium |  | Check, repair, analyze, and optimize MySQL tables |
| 126 | `rpm -i` | high |  | Install RPM package file |
| 127 | `npx` | medium |  | Execute npm package binaries |
| 128 | `ctr images list` | low |  | List images in containerd |
| 129 | `git branch` | low |  | 列出、创建或删除分支 |
| 130 | `kubectl get prometheusrules` | low |  | List PrometheusRule resources containing alerting and recording rules |
| 131 | `calicoctl delete networkpolicy` | critical |  | Delete Calico network policy |
| 132 | `kubectl get ingress` | low |  | List Ingress resources for external access |
| 133 | `kubectl get pv` | low |  | List PersistentVolume resources |
| 134 | `restic init` | low |  | Initialize restic backup repository |
| 135 | `terraform apply` | critical |  | Apply Terraform configuration changes |
| 136 | `istioctl version` | low |  | Check Istio service mesh version |
| 137 | `istioctl analyze` | low |  | Analyze Istio configuration for potential issues |
| 138 | `tsar --list` | low |  | List available modules |
| 139 | `kubectl get limitrange` | low |  | 检查资源限制范围 |
| 140 | `netstat` | low |  | 显示网络连接和路由表 |
| 141 | `terraform workspace list` | low |  | List Terraform workspaces |
| 142 | `kubectl get volumesnapshotclass` | low |  | List VolumeSnapshotClass resources defining snapshot provisioners |
| 143 | `kubectl scale` | high |  | Set a new size for a deployment, replica set, or replication controller |
| 144 | `jstack` | low |  | 打印Java线程堆栈 |
| 145 | `systemctl status` | low |  | Check service status |
| 146 | `terraform import` | medium |  | Import existing infrastructure into Terraform state |
| 147 | `az aks create` | critical |  | Create Azure AKS Kubernetes cluster |
| 148 | `stack` | low |  | Display method call stack |
| 149 | `kubectl get volumesnapshot` | low |  | List VolumeSnapshot resources for backup and restore |
| 150 | `tsar --partition` | low |  | Display disk partition usage |
| 151 | `firewall-cmd --add-port` | medium |  | Open firewall port |
| 152 | `helm package` | low |  | Package chart into versioned archive |
| 153 | `skaffold build` | low |  | Build container images only (no deployment) |
| 154 | `aws eks` | low |  | EKS Kubernetes 集群管理 |
| 155 | `pip` | low |  | Python包管理器 |
| 156 | `gradle` | low |  | Gradle 项目自动化构建工具，基于 Groovy/Kotlin DSL |
| 157 | `kubectl get gateways` | low |  | List Gateway resources (Gateway API) |
| 158 | `svn status` | low |  | Show working copy status |
| 159 | `restic snapshots` | low |  | List restic backup snapshots |
| 160 | `kubectl delete` | critical |  | Delete resources by filenames, resources and names, or by label selectors |
| 161 | `go build` | low |  | 编译Go包和依赖 |
| 162 | `docker images` | low |  | 列出本地镜像 |
| 163 | `kubectl get clusterrolebindings` | low |  | List ClusterRoleBinding resources for cluster-wide access |
| 164 | `skaffold dev` | medium |  | Start Skaffold continuous development mode |
| 165 | `node` | medium |  | Execute JavaScript code using Node.js runtime |
| 166 | `psql` | high |  | PostgreSQL interactive terminal |
| 167 | `gcloud container clusters delete` | critical |  | Delete Google GKE cluster |
| 168 | `kubectl debug` | medium |  | 创建调试容器进行故障排查 |
| 169 | `jmap` | medium |  | 生成堆转储和内存映射 |
| 170 | `kubectl get prometheuses` | low |  | List Prometheus instances managed by Prometheus Operator |
| 171 | `npm outdated` | low |  | Check for outdated packages |
| 172 | `go run` | low |  | 编译并运行Go程序 |
| 173 | `rpm -e` | high |  | Erase (remove) installed package |
| 174 | `bentoml` | low |  | BentoML 命令行客户端，用于模型打包和服务 |
| 175 | `logger` | medium |  | View or modify logger settings |
| 176 | `rm` | critical |  | 删除文件或目录 |
| 177 | `kubectl config` | high |  | Modify kubeconfig files |
| 178 | `mlflow` | low |  | MLflow 命令行客户端，用于模型全生命周期管理 |
| 179 | `docker exec` | low |  | 在运行中的容器内执行命令 |
| 180 | `kubectl get podsecuritystandards` | medium |  | Check PodSecurity admission labels on namespaces (v1.23+) |
| 181 | `flux reconcile source git` | medium |  | Manually trigger Git source reconciliation |
| 182 | `az aks delete` | critical |  | Delete Azure AKS cluster |
| 183 | `arthas` | medium |  | Start Arthas and attach to Java process |
| 184 | `kubectl get volumeattachments` | low |  | List VolumeAttachment resources showing volume-node associations |
| 185 | `etcdctl get` | low |  | Get value of specified key from etcd |
| 186 | `jcmd` | low |  | 向运行JVM发送诊断命令 |
| 187 | `redis-cli FLUSHDB` | critical |  | Delete all keys in current database |
| 188 | `helm rollback` | high |  | Rollback Helm release to previous version |
| 189 | `ansible-config dump` | low |  | Show Ansible configuration |
| 190 | `promtool check config` | low |  | Validate Prometheus configuration file |
| 191 | `kubectl describe inferenceservice` | low |  | Show detailed information about KServe InferenceService |
| 192 | `kubeadm init` | critical |  | Initialize Kubernetes control plane node |
| 193 | `systemctl stop` | high |  | Stop a systemd service |
| 194 | `systemctl status loki` | medium |  | Check Loki service status |
| 195 | `heapdump` | high |  | Dump Java heap to file |
| 196 | `kubectl get clusterroles` | low |  | List ClusterRole resources for cluster-wide permissions |
| 197 | `mv` | medium |  | 移动或重命名文件和目录 |
| 198 | `yum remove` | high |  | Remove installed packages |
| 199 | `kubectl get podmonitors` | low |  | List PodMonitor resources for direct pod monitoring |
| 200 | `svn switch` | medium |  | Switch working copy to different URL |
| 201 | `argocd app delete` | critical |  | Delete ArgoCD application |
| 202 | `flux bootstrap git` | high |  | Bootstrap Flux to Git repository |
| 203 | `pg_dump` | medium |  | PostgreSQL database backup utility |
| 204 | `kubectx` | high |  | Switch between Kubernetes contexts |
| 205 | `dpkg -i` | high |  | Install .deb package file |
| 206 | `dig` | low |  | DNS查询工具 |
| 207 | `helm template` | low |  | Render chart templates locally |
| 208 | `go fmt` | low |  | 格式化Go代码 |
| 209 | `systemctl status kubelet` | low |  | Check kubelet service status |
| 210 | `dropuser` | high |  | Remove a PostgreSQL user |
| 211 | `gh run cancel` | medium |  | 取消正在运行的 GitHub Actions 工作流 |
| 212 | `terraform fmt` | low |  | Format Terraform configuration files |
| 213 | `istioctl proxy-config` | low |  | Inspect Envoy proxy configuration |
| 214 | `jad` | low |  | Decompile Java class files |
| 215 | `skaffold delete` | high |  | Delete Skaffold deployments |
| 216 | `pytest` | low |  | Python测试框架 |
| 217 | `helm list` | low |  | List Helm releases |
| 218 | `ansible-vault encrypt` | medium |  | Encrypt Ansible files with vault |
| 219 | `aws s3` | high |  | S3 存储桶和对象管理 |
| 220 | `tkn pipelinerun logs` | low |  | View Tekton pipeline run logs |
| 221 | `tensorboard` | low |  | TensorFlow和PyTorch的训练可视化工具 |
| 222 | `restic backup` | low |  | Create restic backup |
| 223 | `systemctl enable` | medium |  | Enable service to start on boot |
| 224 | `argocd login` | low |  | Login to ArgoCD server |
| 225 | `tsar --io` | low |  | Display disk I/O statistics |
| 226 | `jar` | low |  | 创建和管理JAR文件 |
| 227 | `kubectl port-forward svc/prometheus-operated` | medium |  | Port forward to access Prometheus web UI |
| 228 | `yum search` | low |  | Search for packages |
| 229 | `systemctl start` | medium |  | Start a systemd service |
| 230 | `trap` | low |  | 捕获信号并在脚本中执行清理操作 |
| 231 | `calicoctl apply` | high |  | Apply Calico network policy configuration |
| 232 | `kubectl get ciliumclusterwidenetworkpolicies` | low |  | List CiliumClusterwideNetworkPolicy resources |
| 233 | `kubectl patch storageclass` | high |  | Modify StorageClass configuration |
| 234 | `kubectl label nodes` | low |  | Add or remove labels from nodes |
| 235 | `javac` | low |  | 编译Java源代码 |
| 236 | `make` | medium |  | GNU Make 构建自动化工具，通过 Makefile 定义构建规则 |
| 237 | `watch` | medium |  | Watch method invocation in real-time |
| 238 | `promtool test rules` | low |  | Test Prometheus alerting and recording rules |
| 239 | `argocd app list` | low |  | List ArgoCD applications |
| 240 | `mysqlimport` | high |  | Import data from text files into MySQL tables |
| 241 | `kubectl drain` | critical |  | Drain node in preparation for maintenance |
| 242 | `npm test` | low |  | Run the test script defined in package.json |
| 243 | `wget` | medium |  | Download files from the web |
| 244 | `restic restore` | high |  | Restore from restic backup |
| 245 | `kubectl label` | medium |  | Update labels on a resource |
| 246 | `otelcol validate` | low |  | Validate OpenTelemetry Collector configuration |
| 247 | `cargo clippy` | low |  | Rust 代码 lint 工具，检测常见错误和改进建议 |
| 248 | `kubectl get csistoragecapacities` | low |  | List CSIStorageCapacity resources showing storage availability |
| 249 | `velero restore create` | critical |  | Restore from Velero backup |
| 250 | `aws configure` | high |  | 配置 AWS CLI 凭证和默认设置 |
| 251 | `tcpdump` | medium |  | 抓取和分析网络包 |
| 252 | `createdb` | medium |  | Create a new PostgreSQL database |
| 253 | `pg_basebackup` | medium |  | Take a base backup of a PostgreSQL cluster |
| 254 | `kubectl get pytorchjobs` | low |  | List Kubeflow PyTorch training jobs |
| 255 | `eksctl delete cluster` | critical |  | Delete AWS EKS cluster |
| 256 | `ansible-galaxy install` | low |  | Install Ansible roles from Galaxy or Git |
| 257 | `dpkg -l` | low |  | List installed packages |
| 258 | `node_exporter` | low |  | Start Prometheus Node Exporter for hardware and OS metrics |
| 259 | `terraform destroy` | critical |  | Destroy Terraform-managed infrastructure |
| 260 | `svn diff` | low |  | Show differences between revisions |
| 261 | `kubectl get resourcequotas` | low |  | List ResourceQuota resources for namespace quotas |
| 262 | `kubectl get csidrivers` | low |  | List CSIDriver resources for Container Storage Interface drivers |
| 263 | `telepresence connect` | medium |  | Connect local environment to Kubernetes cluster |
| 264 | `kubectl create` | medium |  | Create a resource from a file or stdin |
| 265 | `kubectl port-forward svc/grafana` | medium |  | Port forward to access Grafana dashboard |
| 266 | `curl` | low |  | 命令行HTTP客户端 |
| 267 | `crictl ps` | low |  | List running containers |
| 268 | `svn revert` | high |  | Undo local changes |
| 269 | `kubectl get constrainttemplates` | low |  | List ConstraintTemplate resources for OPA Gatekeeper |
| 270 | `ab` | high |  | Apache HTTP server benchmarking tool |
| 271 | `terraform init` | low |  | Initialize Terraform working directory |
| 272 | `jstat` | low |  | 监控JVM统计信息 |
| 273 | `rustup` | medium |  | Rust 工具链安装器和版本管理器 |
| 274 | `az aks list` | low |  | List Azure AKS clusters |
| 275 | `kubeadm upgrade` | critical |  | Upgrade Kubernetes cluster to specified version |
| 276 | `mysql` | high |  | MySQL command-line client for database operations |
| 277 | `ansible-console` | medium |  | Interactive Ansible console |
| 278 | `kubectl get rolebindings` | low |  | List RoleBinding resources linking users to roles |
| 279 | `kubectl get tlsroutes` | low |  | List TLSRoute resources (Gateway API) |
| 280 | `kubectl delete pv` | critical |  | Delete PersistentVolume resources |
| 281 | `kfctl apply` | critical |  | Deploy Kubeflow to Kubernetes cluster |
| 282 | `kubectl cluster-info` | low |  | 显示集群基本信息 |
| 283 | `pg_restore` | high |  | Restore PostgreSQL database from archive |
| 284 | `terraform state show` | low |  | Show detailed resource state |
| 285 | `torchrun` | low |  | PyTorch分布式训练启动器 |
| 286 | `kubectl cordon` | medium |  | Mark node as unschedulable |
| 287 | `apt upgrade` | medium |  | Upgrade all installed packages |
| 288 | `kubectl port-forward svc/alertmanager-operated` | medium |  | Port forward to access Alertmanager UI |
| 289 | `helm history` | low |  | View release history |
| 290 | `gh workflow` | low |  | 管理 GitHub Actions 工作流 |
| 291 | `git add` | low |  | 添加文件到暂存区 |
| 292 | `git push` | high |  | 推送本地提交到远程仓库 |
| 293 | `velero backup create` | medium |  | Create backup of Kubernetes resources |
| 294 | `sestatus` | low |  | Display SELinux status |
| 295 | `go test` | low |  | 运行测试 |
| 296 | `grafana-cli admin reset-admin-password` | high |  | Reset Grafana admin password |
| 297 | `systemctl status fluentd` | medium |  | Check Fluentd service status |
| 298 | `pylint` | low |  | Python代码检查工具 |
| 299 | `helm repo remove` | low |  | Remove Helm chart repository |
| 300 | `terraform workspace new` | medium |  | Create new Terraform workspace |
| 301 | `terraform refresh` | medium |  | Update Terraform state with real infrastructure |
| 302 | `kubectl annotate` | low |  | Update annotations on a resource |
| 303 | `grafana-cli plugins list-remote` | low |  | List available Grafana plugins |
| 304 | `virtualenv` | low |  | 创建Python虚拟环境 |
| 305 | `dropdb` | critical |  | Remove a PostgreSQL database |
| 306 | `git init` | low |  | 初始化新的Git仓库 |
| 307 | `ufw allow` | medium |  | Allow firewall rule |
| 308 | `kubectl get inferenceservices` | low |  | List KServe InferenceServices |
| 309 | `svn commit` | medium |  | Send changes to repository |
| 310 | `tsar --tcp` | low |  | Display TCP connection statistics |
| 311 | `redis-server` | high |  | Redis server daemon |
| 312 | `cargo` | low |  | Rust 包管理器和构建工具 |
| 313 | `svn add` | low |  | Add files to version control |
| 314 | `svn cleanup` | low |  | Clean up working copy (remove locks, fix interrupted operations) |
| 315 | `otel-cli span` | low |  | Send span data to OpenTelemetry endpoint |
| 316 | `go mod` | low |  | 模块维护 |
| 317 | `redis-cli` | high |  | Redis command-line interface client |
| 318 | `gradle init` | low |  | Gradle Wrapper 初始化，生成 gradlew 脚本 |
| 319 | `crictl logs` | low |  | Fetch logs of a container |
| 320 | `svn copy` | medium |  | Create a copy (branch/tag) in repository |
| 321 | `tilt down` | medium |  | Stop Tilt and cleanup resources |
| 322 | `argocd app sync` | high |  | Sync application state with Git repository |
| 323 | `tkn pipeline list` | low |  | List Tekton pipelines |
| 324 | `cargo fmt` | low |  | Rust 代码格式化工具 |
| 325 | `go vet` | low |  | 检查Go代码中的常见错误 |
| 326 | `ansible-vault decrypt` | high |  | Decrypt Ansible vault files |
| 327 | `rpm -qa` | low |  | Query all installed packages |
| 328 | `npm install` | medium |  | Install package dependencies |
| 329 | `redis-cli MONITOR` | medium |  | Monitor all commands processed by Redis server |
| 330 | `helm search repo` | low |  | Search for charts in repositories |
| 331 | `kfctl delete` | critical |  | Delete Kubeflow deployment |
| 332 | `helm env` | low |  | Display Helm environment information |
| 333 | `mysqladmin` | critical |  | MySQL server administration utility |
| 334 | `git checkout` | medium |  | 切换分支或恢复文件 |
| 335 | `grafana-cli plugins install` | medium |  | Install Grafana plugin |
| 336 | `ansible all -m ping` | low |  | Test connectivity to all hosts in inventory |
| 337 | `sc` | low |  | Search loaded classes |
| 338 | `journalctl -u kubelet` | low |  | View kubelet service logs |
| 339 | `skaffold run` | high |  | Build and deploy application once |
| 340 | `gradlew` | low |  | Gradle Wrapper 脚本，确保使用项目指定的 Gradle 版本 |
| 341 | `svn update` | medium |  | Update working copy to latest revision |
| 342 | `etcdctl snapshot save` | medium |  | Create backup snapshot of etcd data |
| 343 | `npm audit` | medium |  | Check for security vulnerabilities |
| 344 | `helm status` | low |  | Display status of Helm release |
| 345 | `mysqlshow` | low |  | Display database, table, and column information |
| 346 | `crictl exec` | high |  | Execute command in running container |
| 347 | `kubectl describe` | low |  | Show detailed information about a resource |
| 348 | `tsar --load` | low |  | Display system load average |
| 349 | `apt install` | medium |  | Install new packages |
| 350 | `redis-benchmark` | medium |  | Redis performance benchmarking tool |
| 351 | `falco` | low |  | Start Falco runtime security monitoring |
| 352 | `kubectl delete pvc` | critical |  | Delete PersistentVolumeClaim resources |
| 353 | `argocd app create` | high |  | Create ArgoCD application |
| 354 | `npm publish` | high |  | Publish package to npm registry |
| 355 | `ansible` | medium |  | Execute ad-hoc commands on hosts |
| 356 | `calicoctl get nodes` | low |  | List all Calico nodes |
| 357 | `git merge` | low |  | 合并分支 |
| 358 | `tilt up` | medium |  | Start Tilt development environment |
| 359 | `amtool alert query` | low |  | Query active alerts from Alertmanager |
| 360 | `kubectl api-versions` | low |  | 显示支持的 API 版本 |
| 361 | `ansible-pull` | high |  | Pull and execute Ansible playbooks from VCS |
| 362 | `svn log` | low |  | Show commit log messages |
| 363 | `git clone` | low |  | 克隆远程仓库到本地 |
| 364 | `kubectl logs` | low |  | 查看容器日志用于问题诊断 |
| 365 | `kube-bench run` | low |  | Run CIS Kubernetes security benchmark checks |
| 366 | `gcloud container clusters create` | critical |  | Create Google GKE Kubernetes cluster |
| 367 | `prometheus` | medium |  | Start Prometheus monitoring server |
| 368 | `kubectl describe pod` | low |  | 详细查看 Pod 状态和事件信息 |
| 369 | `postman` | low |  | API development and testing platform (CLI) |
| 370 | `tsar` | low |  | Display system performance statistics |
| 371 | `setenforce` | high |  | Change SELinux mode temporarily |
| 372 | `aws` | high |  | AWS 命令行接口，管理 AWS 服务和资源 |
| 373 | `kubectl delete inferenceservice` | high |  | Delete a KServe InferenceService |
| 374 | `rpm -qi` | low |  | Query package information |
| 375 | `promtool tsdb analyze` | low |  | Analyze Prometheus TSDB blocks |
| 376 | `kubectl api-resources` | low |  | 列出所有可用的 API 资源 |
| 377 | `sm` | low |  | Search methods in classes |
| 378 | `kubeadm config view` | low |  | View the kubeadm configuration |
| 379 | `dnf install` | medium |  | Install packages (newer package manager for CentOS 8+) |
| 380 | `mvn clean` | high |  | 清理构建输出目录(target) |
| 381 | `shellcheck` | low |  | Shell 脚本静态分析工具，检测常见错误和最佳实践 |
| 382 | `tkn pipeline start` | high |  | Start Tekton pipeline execution |
| 383 | `python` | low |  | 运行Python解释器 |
| 384 | `terraform validate` | low |  | Validate Terraform configuration syntax |
| 385 | `kubectl get httproutes` | low |  | List HTTPRoute resources (Gateway API) |
| 386 | `docker build` | low |  | 从Dockerfile构建镜像 |
| 387 | `svn merge` | high |  | Merge changes from another branch |
| 388 | `find` | high |  | 在目录树中搜索文件 |
| 389 | `kubectl get pvc` | low |  | List PersistentVolumeClaim resources |
| 390 | `systemctl status prometheus` | medium |  | Check Prometheus service status |
| 391 | `tsar --traffic` | low |  | Display network traffic statistics |
| 392 | `apt-cache show` | low |  | Show package information |
| 393 | `go get` | low |  | 添加依赖到当前模块 |
| 394 | `git status` | low |  | 显示工作区状态 |
| 395 | `firewall-cmd --list-all` | low |  | List all firewall rules |
| 396 | `systemctl status grafana-server` | medium |  | Check Grafana service status |
| 397 | `kubectl get resourcequota` | low |  | 检查资源配额限制 |
| 398 | `docker run` | low |  | 运行一个新容器 |
| 399 | `kubectl get roles` | low |  | List Role resources for namespace-scoped permissions |
| 400 | `kubectl get constraints` | low |  | List Constraint resources enforcing policies |
| 401 | `source` | medium |  | 在当前 Shell 环境中执行脚本（不创建子进程） |
| 402 | `ansible-doc` | low |  | Display Ansible module documentation |
| 403 | `cd` | low |  | 切换当前工作目录 |
| 404 | `kubectl port-forward` | medium |  | 端口转发用于本地调试和测试 |
| 405 | `kfp pipeline upload` | low |  | Upload a pipeline to Kubeflow Pipelines |
| 406 | `kubectl get serviceaccounts` | low |  | List ServiceAccount resources for pod identities |
| 407 | `helm repo add` | low |  | Add Helm chart repository |
| 408 | `kubectl get notebooks` | low |  | List Kubeflow Notebooks |
| 409 | `kubectl get componentstatuses` | low |  | 检查 Kubernetes 控制平面组件健康状态 |
| 410 | `helm install` | high |  | Install Helm chart to Kubernetes cluster |
| 411 | `terraform state rm` | high |  | Remove resource from Terraform state |
| 412 | `jps` | low |  | 显示Java进程状态 |
| 413 | `popeye` | low |  | Kubernetes cluster resource sanitizer and health checker |
| 414 | `cilium hubble status` | low |  | Check Hubble observability status |
| 415 | `tsar --cpu` | low |  | Display detailed CPU statistics |
| 416 | `kfp` | low |  | Kubeflow Pipelines (KFP) 命令行客户端 |
| 417 | `helm create` | low |  | Create new Helm chart |
| 418 | `helm plugin list` | low |  | List installed Helm plugins |
| 419 | `terraform state list` | low |  | List resources in Terraform state |
| 420 | `trivy fs` | low |  | Scan filesystem for vulnerabilities and misconfigurations |
| 421 | `yum install` | medium |  | Install new packages |
| 422 | `promtool query instant` | low |  | Execute instant PromQL query |
| 423 | `kubectl get prometheusagents` | low |  | List Prometheus Agent mode instances for lightweight monitoring |
| 424 | `redis-check-rdb` | low |  | Check Redis RDB snapshot file |
| 425 | `flux get kustomizations` | low |  | List Flux Kustomization resources |
| 426 | `stern` | low |  | Multi-pod and container log tailing for Kubernetes |
| 427 | `kubectl apply -f inferenceservice.yaml` | medium |  | Deploy a KServe InferenceService |
| 428 | `kubectl auth can-i` | low |  | 检查用户权限 |
| 429 | `terraform plan` | low |  | Generate and show Terraform execution plan |
| 430 | `ansible-inventory --list` | low |  | Display Ansible inventory information |
| 431 | `tsar --mem` | low |  | Display memory usage statistics |
| 432 | `make install` | high |  | 安装已编译的程序到系统目录（通常为 /usr/local） |
| 433 | `redis-cli SAVE` | high |  | Synchronously save dataset to disk |
| 434 | `svn checkout` | low |  | Check out a working copy from a repository |
| 435 | `kubectl taint nodes` | medium |  | Add or remove taints from nodes |
| 436 | `aws cloudformation` | high |  | CloudFormation 基础设施即代码管理 |
| 437 | `javadoc` | low |  | 生成Java文档 |
| 438 | `cmake` | low |  | 跨平台构建系统生成器，管理 C/C++ 项目构建 |
| 439 | `grep` | low |  | 在文件中搜索文本模式 |
| 440 | `kubectl apply` | high |  | Apply a configuration to a resource by filename or stdin |
| 441 | `svn delete` | high |  | Remove files from version control |
| 442 | `trivy image` | low |  | Scan container image for vulnerabilities |
| 443 | `kubectl get csinodes` | low |  | List CSINode resources showing node storage capabilities |
| 444 | `java` | low |  | 运行Java程序 |
| 445 | `fluentd -c` | medium |  | Start Fluentd with configuration file |
| 446 | `npm update` | medium |  | Update packages to their latest versions |
| 447 | `kfp experiment create` | low |  | Create a Kubeflow Pipelines experiment |
| 448 | `docker logs` | low |  | 查看容器日志 |
| 449 | `kubeadm reset` | critical |  | Reset node state and undo kubeadm init or join |
| 450 | `apt search` | low |  | Search for packages |
| 451 | `trace` | medium |  | Trace method execution time |
| 452 | `velero backup list` | low |  | List all Velero backups |
| 453 | `helm lint` | low |  | Lint chart for best practices and errors |
| 454 | `kubectl get experiments.kubeflow.org` | low |  | List Kubeflow Katib experiments |
| 455 | `yum update` | medium |  | Update all installed packages |
| 456 | `dpkg -r` | high |  | Remove installed package |
| 457 | `ufw deny` | medium |  | Deny firewall rule |
| 458 | `kubectl get thanosrulers` | low |  | List Thanos Ruler instances for distributed alerting |
| 459 | `docker ps` | low |  | 列出运行中的容器 |
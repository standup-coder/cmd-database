# cmd4coder 完整命令清单

**总命令数**: 734  |  **大分类数**: 12

本清单按功能领域进行简单分类，每个分类下包含命令名称、风险等级和描述。

## Kubernetes 生态 (248)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `alertmanager` | medium | Start Prometheus Alertmanager |
| 2 | `amtool alert query` | low | Query active alerts from Alertmanager |
| 3 | `amtool check-config` | low | Validate Alertmanager configuration |
| 4 | `amtool silence add` | medium | Add silence to Alertmanager |
| 5 | `ansible` | medium | Execute ad-hoc commands on hosts |
| 6 | `ansible all -m ping` | low | Test connectivity to all hosts in inventory |
| 7 | `ansible-config dump` | low | Show Ansible configuration |
| 8 | `ansible-console` | medium | Interactive Ansible console |
| 9 | `ansible-doc` | low | Display Ansible module documentation |
| 10 | `ansible-galaxy install` | low | Install Ansible roles from Galaxy or Git |
| 11 | `ansible-inventory --list` | low | Display Ansible inventory information |
| 12 | `ansible-playbook` | high | Execute Ansible playbook |
| 13 | `ansible-pull` | medium | Pull and execute Ansible playbooks from VCS |
| 14 | `ansible-vault decrypt` | medium | Decrypt Ansible vault files |
| 15 | `ansible-vault encrypt` | medium | Encrypt Ansible files with vault |
| 16 | `argocd app create` | high | Create ArgoCD application |
| 17 | `argocd app delete` | critical | Delete ArgoCD application |
| 18 | `argocd app list` | low | List ArgoCD applications |
| 19 | `argocd app sync` | high | Sync application state with Git repository |
| 20 | `argocd login` | low | Login to ArgoCD server |
| 21 | `az aks create` | critical | Create Azure AKS Kubernetes cluster |
| 22 | `az aks delete` | critical | Delete Azure AKS cluster |
| 23 | `az aks list` | low | List Azure AKS clusters |
| 24 | `calicoctl apply` | high | Apply Calico network policy configuration |
| 25 | `calicoctl delete networkpolicy` | high | Delete Calico network policy |
| 26 | `calicoctl get networkpolicies` | low | List Calico network policies |
| 27 | `calicoctl get nodes` | low | List all Calico nodes |
| 28 | `cilium connectivity test` | low | Run connectivity test between pods |
| 29 | `cilium hubble status` | low | Check Hubble observability status |
| 30 | `cilium status` | low | Check Cilium agent status |
| 31 | `crictl exec` | high | Execute command in running container |
| 32 | `crictl images` | low | List container images |
| 33 | `crictl logs` | low | Fetch logs of a container |
| 34 | `crictl pods` | low | List all pods |
| 35 | `crictl ps` | low | List running containers |
| 36 | `crictl stats` | low | Display container resource usage statistics |
| 37 | `ctr containers list` | low | List containers in containerd |
| 38 | `ctr images list` | low | List images in containerd |
| 39 | `eksctl create cluster` | critical | Create AWS EKS Kubernetes cluster |
| 40 | `eksctl delete cluster` | critical | Delete AWS EKS cluster |
| 41 | `eksctl get cluster` | low | List AWS EKS clusters |
| 42 | `etcdctl get` | low | Get value of specified key from etcd |
| 43 | `etcdctl member list` | low | List all etcd cluster members |
| 44 | `etcdctl snapshot restore` | critical | Restore etcd cluster from backup snapshot |
| 45 | `etcdctl snapshot save` | low | Create backup snapshot of etcd data |
| 46 | `falco` | low | Start Falco runtime security monitoring |
| 47 | `fluent-bit -c` | medium | Start Fluent Bit with configuration file |
| 48 | `fluentd -c` | medium | Start Fluentd with configuration file |
| 49 | `flux bootstrap git` | high | Bootstrap Flux to Git repository |
| 50 | `flux get kustomizations` | low | List Flux Kustomization resources |
| 51 | `flux reconcile source git` | medium | Manually trigger Git source reconciliation |
| 52 | `gcloud container clusters create` | critical | Create Google GKE Kubernetes cluster |
| 53 | `gcloud container clusters delete` | critical | Delete Google GKE cluster |
| 54 | `gcloud container clusters list` | low | List Google GKE clusters |
| 55 | `grafana-cli admin reset-admin-password` | high | Reset Grafana admin password |
| 56 | `grafana-cli plugins install` | medium | Install Grafana plugin |
| 57 | `grafana-cli plugins list-remote` | low | List available Grafana plugins |
| 58 | `grafana-cli plugins update` | medium | Update Grafana plugin |
| 59 | `grafana-server` | medium | Start Grafana visualization server |
| 60 | `helm create` | low | Create new Helm chart |
| 61 | `helm dependency` | low | Manage chart dependencies |
| 62 | `helm env` | low | Display Helm environment information |
| 63 | `helm history` | low | View release history |
| 64 | `helm install` | high | Install Helm chart to Kubernetes cluster |
| 65 | `helm install` | high | Install Helm chart to Kubernetes cluster |
| 66 | `helm lint` | low | Lint chart for best practices and errors |
| 67 | `helm list` | low | List Helm releases |
| 68 | `helm list` | low | List Helm releases |
| 69 | `helm package` | low | Package chart into versioned archive |
| 70 | `helm plugin list` | low | List installed Helm plugins |
| 71 | `helm repo add` | low | Add Helm chart repository |
| 72 | `helm repo add` | low | Add Helm chart repository |
| 73 | `helm repo remove` | low | Remove Helm chart repository |
| 74 | `helm repo update` | low | Update local Helm chart repository cache |
| 75 | `helm repo update` | low | Update local Helm chart repository cache |
| 76 | `helm rollback` | high | Rollback Helm release to previous version |
| 77 | `helm search repo` | low | Search for charts in repositories |
| 78 | `helm status` | low | Display status of Helm release |
| 79 | `helm status` | low | Display status of Helm release |
| 80 | `helm template` | low | Render Helm chart templates locally |
| 81 | `helm template` | low | Render chart templates locally |
| 82 | `helm uninstall` | critical | Uninstall Helm release from cluster |
| 83 | `helm uninstall` | critical | Uninstall Helm release from cluster |
| 84 | `helm upgrade` | high | Upgrade Helm release to new version |
| 85 | `helm upgrade` | high | Upgrade Helm release to new version |
| 86 | `helm version` | low | Display Helm client and server version |
| 87 | `istioctl analyze` | low | Analyze Istio configuration for potential issues |
| 88 | `istioctl proxy-config` | low | Inspect Envoy proxy configuration |
| 89 | `istioctl proxy-status` | low | Check Envoy proxy status in service mesh |
| 90 | `istioctl version` | low | Check Istio service mesh version |
| 91 | `journalctl -u kubelet` | low | View kubelet service logs |
| 92 | `k9s` | low | Interactive terminal UI for Kubernetes |
| 93 | `kfctl apply` | critical | Deploy Kubeflow to Kubernetes cluster |
| 94 | `kfctl delete` | critical | Delete Kubeflow deployment |
| 95 | `kfp experiment create` | low | Create a Kubeflow Pipelines experiment |
| 96 | `kfp pipeline list` | low | List Kubeflow Pipelines |
| 97 | `kfp pipeline upload` | low | Upload a pipeline to Kubeflow Pipelines |
| 98 | `kfp run submit` | medium | Submit a Kubeflow Pipeline run |
| 99 | `kube-bench run` | low | Run CIS Kubernetes security benchmark checks |
| 100 | `kubeadm config view` | low | View the kubeadm configuration |
| 101 | `kubeadm init` | critical | Initialize Kubernetes control plane node |
| 102 | `kubeadm join` | high | Join worker node to Kubernetes cluster |
| 103 | `kubeadm reset` | critical | Reset node state and undo kubeadm init or join |
| 104 | `kubeadm token list` | low | List bootstrap tokens on the cluster |
| 105 | `kubeadm upgrade` | critical | Upgrade Kubernetes cluster to specified version |
| 106 | `kubectl api-resources` | low | 列出所有可用的 API 资源 |
| 107 | `kubectl api-versions` | low | 显示支持的 API 版本 |
| 108 | `kubectl apply -f inferenceservice.yaml` | medium | Deploy a KServe InferenceService |
| 109 | `kubectl auth can-i` | low | Check if user has specific permissions |
| 110 | `kubectl auth can-i` | low | 检查用户权限 |
| 111 | `kubectl cluster-info` | low | 显示集群基本信息 |
| 112 | `kubectl config current-context` | medium | 显示当前配置上下文 |
| 113 | `kubectl cp` | medium | Copy files between local filesystem and pod |
| 114 | `kubectl debug` | medium | 创建调试容器进行故障排查 |
| 115 | `kubectl delete inferenceservice` | high | Delete a KServe InferenceService |
| 116 | `kubectl delete pv` | critical | Delete PersistentVolume resources |
| 117 | `kubectl delete pvc` | critical | Delete PersistentVolumeClaim resources |
| 118 | `kubectl describe inferenceservice` | low | Show detailed information about KServe InferenceService |
| 119 | `kubectl describe pod` | low | 详细查看 Pod 状态和事件信息 |
| 120 | `kubectl exec -it` | medium | Enter pod for network troubleshooting |
| 121 | `kubectl exec -it` | medium | 进入容器执行网络诊断命令 |
| 122 | `kubectl exec -it` | medium | Enter pod to diagnose storage issues |
| 123 | `kubectl get ciliumclusterwidenetworkpolicies` | low | List CiliumClusterwideNetworkPolicy resources |
| 124 | `kubectl get ciliumnetworkpolicies` | low | List CiliumNetworkPolicy resources for advanced networking |
| 125 | `kubectl get clusterrolebindings` | low | List ClusterRoleBinding resources for cluster-wide access |
| 126 | `kubectl get clusterroles` | low | List ClusterRole resources for cluster-wide permissions |
| 127 | `kubectl get componentstatuses` | low | 检查 Kubernetes 控制平面组件健康状态 |
| 128 | `kubectl get constraints` | low | List Constraint resources enforcing policies |
| 129 | `kubectl get constrainttemplates` | low | List ConstraintTemplate resources for OPA Gatekeeper |
| 130 | `kubectl get csidrivers` | low | List CSIDriver resources for Container Storage Interface drivers |
| 131 | `kubectl get csinodes` | low | List CSINode resources showing node storage capabilities |
| 132 | `kubectl get csistoragecapacities` | low | List CSIStorageCapacity resources showing storage availability |
| 133 | `kubectl get endpointslices` | low | List EndpointSlice resources showing service endpoints |
| 134 | `kubectl get events` | low | 获取集群事件信息，用于故障诊断 |
| 135 | `kubectl get experiments.kubeflow.org` | low | List Kubeflow Katib experiments |
| 136 | `kubectl get gateways` | low | List Gateway resources (Gateway API) |
| 137 | `kubectl get httproutes` | low | List HTTPRoute resources (Gateway API) |
| 138 | `kubectl get imagepolicies` | low | List ImagePolicy resources for image validation |
| 139 | `kubectl get inferenceservices` | low | List KServe InferenceServices |
| 140 | `kubectl get ingress` | low | List Ingress resources for external access |
| 141 | `kubectl get ingressclasses` | low | List IngressClass resources defining ingress controller types |
| 142 | `kubectl get limitrange` | low | 检查资源限制范围 |
| 143 | `kubectl get limitranges` | low | List LimitRange resources for resource constraints |
| 144 | `kubectl get networkpolicies` | low | List NetworkPolicy resources for traffic control |
| 145 | `kubectl get notebooks` | low | List Kubeflow Notebooks |
| 146 | `kubectl get podmonitors` | low | List PodMonitor resources for direct pod monitoring |
| 147 | `kubectl get podsecuritystandards` | medium | Check PodSecurity admission labels on namespaces (v1.23+) |
| 148 | `kubectl get prometheusagents` | low | List Prometheus Agent mode instances for lightweight monitoring |
| 149 | `kubectl get prometheuses` | low | List Prometheus instances managed by Prometheus Operator |
| 150 | `kubectl get prometheusrules` | low | List PrometheusRule resources containing alerting and recording rules |
| 151 | `kubectl get pv` | low | List PersistentVolume resources |
| 152 | `kubectl get pvc` | low | List PersistentVolumeClaim resources |
| 153 | `kubectl get pytorchjobs` | low | List Kubeflow PyTorch training jobs |
| 154 | `kubectl get resourcequota` | low | 检查资源配额限制 |
| 155 | `kubectl get resourcequotas` | low | List ResourceQuota resources for namespace quotas |
| 156 | `kubectl get rolebindings` | low | List RoleBinding resources linking users to roles |
| 157 | `kubectl get roles` | low | List Role resources for namespace-scoped permissions |
| 158 | `kubectl get scrapeconfigs` | low | List ScrapeConfig resources for external target monitoring |
| 159 | `kubectl get serviceaccounts` | low | List ServiceAccount resources for pod identities |
| 160 | `kubectl get servicemonitors` | low | List ServiceMonitor resources for automatic service discovery |
| 161 | `kubectl get storageclass` | low | List StorageClass resources defining storage provisioners |
| 162 | `kubectl get storagepools` | low | List StoragePool resources (specific storage systems) |
| 163 | `kubectl get tfjobs` | low | List Kubeflow TensorFlow training jobs |
| 164 | `kubectl get thanosrulers` | low | List Thanos Ruler instances for distributed alerting |
| 165 | `kubectl get tlsroutes` | low | List TLSRoute resources (Gateway API) |
| 166 | `kubectl get volumeattachments` | low | List VolumeAttachment resources showing volume-node associations |
| 167 | `kubectl get volumesnapshot` | low | List VolumeSnapshot resources for backup and restore |
| 168 | `kubectl get volumesnapshotclass` | low | List VolumeSnapshotClass resources defining snapshot provisioners |
| 169 | `kubectl get volumesnapshotcontent` | low | List VolumeSnapshotContent resources representing actual snapshots |
| 170 | `kubectl get workflows` | low | List Kubeflow Pipelines workflows |
| 171 | `kubectl label nodes` | low | Add or remove labels from nodes |
| 172 | `kubectl logs` | low | 查看容器日志用于问题诊断 |
| 173 | `kubectl logs -f deployment/prometheus-operator` | low | Stream logs from Prometheus Operator for troubleshooting |
| 174 | `kubectl logs -l serving.kserve.io/inferenceservice` | low | View logs for KServe model serving pods |
| 175 | `kubectl patch storageclass` | medium | Modify StorageClass configuration |
| 176 | `kubectl port-forward` | medium | Forward local ports to pod for network testing |
| 177 | `kubectl port-forward` | medium | 端口转发用于本地调试和测试 |
| 178 | `kubectl port-forward svc/alertmanager-operated` | medium | Port forward to access Alertmanager UI |
| 179 | `kubectl port-forward svc/grafana` | medium | Port forward to access Grafana dashboard |
| 180 | `kubectl port-forward svc/istio-ingressgateway` | low | Access Kubeflow dashboard locally |
| 181 | `kubectl port-forward svc/ml-pipeline-ui` | low | Access Kubeflow Pipelines UI locally |
| 182 | `kubectl port-forward svc/prometheus-operated` | medium | Port forward to access Prometheus web UI |
| 183 | `kubectl taint nodes` | medium | Add or remove taints from nodes |
| 184 | `kubectl top` | low | 查看资源使用情况，识别性能瓶颈 |
| 185 | `kubectl top pvc` | low | Show PVC resource usage (if metrics available) |
| 186 | `kubectx` | high | Switch between Kubernetes contexts |
| 187 | `kubens` | medium | Switch between Kubernetes namespaces |
| 188 | `node_exporter` | low | Start Prometheus Node Exporter for hardware and OS metrics |
| 189 | `otel-cli span` | low | Send span data to OpenTelemetry endpoint |
| 190 | `otel-cli status server` | low | Check OpenTelemetry endpoint status |
| 191 | `otelcol` | medium | Start OpenTelemetry Collector |
| 192 | `otelcol validate` | low | Validate OpenTelemetry Collector configuration |
| 193 | `otelcol-contrib` | medium | Start OpenTelemetry Collector Contrib distribution |
| 194 | `popeye` | low | Kubernetes cluster resource sanitizer and health checker |
| 195 | `prometheus` | medium | Start Prometheus monitoring server |
| 196 | `promtool check config` | low | Validate Prometheus configuration file |
| 197 | `promtool query instant` | low | Execute instant PromQL query |
| 198 | `promtool test rules` | low | Test Prometheus alerting and recording rules |
| 199 | `promtool tsdb analyze` | low | Analyze Prometheus TSDB blocks |
| 200 | `restic backup` | low | Create restic backup |
| 201 | `restic init` | low | Initialize restic backup repository |
| 202 | `restic restore` | high | Restore from restic backup |
| 203 | `restic snapshots` | low | List restic backup snapshots |
| 204 | `skaffold build` | low | Build container images only (no deployment) |
| 205 | `skaffold delete` | high | Delete Skaffold deployments |
| 206 | `skaffold dev` | medium | Start Skaffold continuous development mode |
| 207 | `skaffold run` | high | Build and deploy application once |
| 208 | `stern` | low | Multi-pod and container log tailing for Kubernetes |
| 209 | `systemctl status containerd` | low | Check containerd service status |
| 210 | `systemctl status falco` | low | Check Falco runtime security service status |
| 211 | `systemctl status fluentd` | low | Check Fluentd service status |
| 212 | `systemctl status grafana-server` | low | Check Grafana service status |
| 213 | `systemctl status kube-state-metrics` | low | Check kube-state-metrics service status |
| 214 | `systemctl status kubelet` | low | Check kubelet service status |
| 215 | `systemctl status loki` | low | Check Loki service status |
| 216 | `systemctl status prometheus` | low | Check Prometheus service status |
| 217 | `systemctl status promtail` | low | Check Promtail service status |
| 218 | `telepresence connect` | medium | Connect local environment to Kubernetes cluster |
| 219 | `telepresence intercept` | critical | Intercept traffic to service and redirect to local process |
| 220 | `terraform apply` | critical | Apply Terraform configuration changes |
| 221 | `terraform destroy` | critical | Destroy Terraform-managed infrastructure |
| 222 | `terraform fmt` | low | Format Terraform configuration files |
| 223 | `terraform import` | medium | Import existing infrastructure into Terraform state |
| 224 | `terraform init` | low | Initialize Terraform working directory |
| 225 | `terraform output` | low | Display Terraform output values |
| 226 | `terraform plan` | low | Generate and show Terraform execution plan |
| 227 | `terraform refresh` | medium | Update Terraform state with real infrastructure |
| 228 | `terraform state list` | low | List resources in Terraform state |
| 229 | `terraform state rm` | high | Remove resource from Terraform state |
| 230 | `terraform state show` | low | Show detailed resource state |
| 231 | `terraform taint` | medium | Mark resource for recreation on next apply |
| 232 | `terraform validate` | low | Validate Terraform configuration syntax |
| 233 | `terraform workspace list` | low | List Terraform workspaces |
| 234 | `terraform workspace new` | medium | Create new Terraform workspace |
| 235 | `terraform workspace select` | medium | Switch to different Terraform workspace |
| 236 | `tilt down` | medium | Stop Tilt and cleanup resources |
| 237 | `tilt up` | medium | Start Tilt development environment |
| 238 | `tkn pipeline list` | low | List Tekton pipelines |
| 239 | `tkn pipeline start` | high | Start Tekton pipeline execution |
| 240 | `tkn pipelinerun logs` | low | View Tekton pipeline run logs |
| 241 | `trivy config` | low | Scan configuration files for misconfigurations |
| 242 | `trivy fs` | low | Scan filesystem for vulnerabilities and misconfigurations |
| 243 | `trivy image` | low | Scan container image for vulnerabilities |
| 244 | `trivy k8s` | low | Scan Kubernetes cluster for security issues |
| 245 | `velero backup create` | low | Create backup of Kubernetes resources |
| 246 | `velero backup list` | low | List all Velero backups |
| 247 | `velero restore create` | critical | Restore from Velero backup |
| 248 | `velero schedule create` | low | Create scheduled backup |

## AI 基础设施 (227)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `accelerate` | low | HuggingFace Accelerate分布式训练配置工具，简化多GPU/TPU训练 |
| 2 | `accelerate` | low | HuggingFace Accelerate分布式训练配置工具，简化多GPU/TPU训练 |
| 3 | `accelerate-config` | low | HuggingFace Accelerate配置向导，交互式生成分布式训练配置文件 |
| 4 | `agent-bench` | high | AgentBench多场景Agent能力评测，涵盖OS、数据库、知识图谱、数字卡牌、网页浏览 |
| 5 | `agno` | medium | Agno (原Phidata) 轻量级Agent框架，支持记忆、知识库、工具、多模态 |
| 6 | `aider` | high | Aider终端AI编程助手，多文件编辑、Git集成、支持GPT-4/Claude，自动提交更改 |
| 7 | `aim` | low | Aim开源超大规模实验跟踪工具，支持百万级实验，高性能查询 |
| 8 | `alpaca-eval` | low | 指令跟随能力评估工具，使用GPT-4作为裁判对模型输出进行排序 |
| 9 | `api-bench` | medium | APIBench API理解评测，测试LLM理解REST API文档并生成正确调用的能力 |
| 10 | `arena` | low | LMSYS Chatbot Arena众测平台，人类盲测对比不同LLM的对话质量 |
| 11 | `argilla` | low | Argilla数据标注与质量平台，专注于NLP和LLM数据，支持主动学习工作流 |
| 12 | `arize` | low | Arize AI ML可观测性平台，支持漂移检测、性能监控、根因分析 |
| 13 | `attention-rollout` | low | Attention Rollout跨层注意力传播追踪，识别输入token到输出token的完整注意力路径 |
| 14 | `auto-gptq` | medium | GPTQ后训练量化工具，4-bit量化减少75%显存占用，适合消费级GPU部署 |
| 15 | `autoawq` | medium | AWQ激活感知的权重量化，4-bit量化精度优于GPTQ，推理速度提升3倍 |
| 16 | `autogen` | high | Microsoft AutoGen多Agent对话框架，支持代码生成、工具调用、人机协同 |
| 17 | `axolotl` | medium | YAML配置式LLM微调工具，支持LoRA、QLoRA、全参数微调 |
| 18 | `bentoml` | medium | BentoML 命令行客户端，用于模型打包和服务 |
| 19 | `bertviz` | low | BertViz Transformer注意力可视化工具，交互式查看各层各头的注意力权重分布 |
| 20 | `big-bench` | low | BIG-bench (Beyond the Imitation Game) 大规模行为评测，200+语言理解任务 |
| 21 | `bitsandbytes` | medium | 8-bit/4-bit量化库，支持QLoRA在消费级GPU上训练大模型 |
| 22 | `calflops` | low | CalFlops模型参数量与FLOPs计算工具，精确统计前向/反向传播计算量 |
| 23 | `captum` | low | Captum PyTorch模型可解释性库，集成梯度、DeepLIFT、集成梯度、特征消融等多种归因方法 |
| 24 | `cerebras` | high | Cerebras Wafer-Scale Engine超大规模AI芯片训练平台，支持十亿到万亿参数模型 |
| 25 | `chainlit` | low | Chainlit对话式AI应用框架，专为LLM应用设计的Python框架 |
| 26 | `chroma` | low | Chroma轻量级开源向量数据库，专为AI应用设计，易嵌入到Python项目 |
| 27 | `cleanlab` | low | Cleanlab数据清洗与噪声检测，自动发现标注错误、异常样本和数据冲突 |
| 28 | `clearml` | medium | ClearML端到端MLOps平台，涵盖实验跟踪、数据管理、Pipeline编排、模型服务 |
| 29 | `clip` | low | OpenAI CLIP图文对齐模型，零样本图像分类、图文相似度计算、图像检索 |
| 30 | `codeium` | low | Codeium免费AI代码补全工具，个人版无限使用，支持70+语言和40+IDE |
| 31 | `colossal-ai` | medium | Colossal-AI统一深度学习加速系统，支持 Gemini、ZeRO、Pipeline 并行 |
| 32 | `comfyui` | medium | ComfyUI Stable Diffusion节点式可视化工作流，支持图像生成、视频生成、ControlNet |
| 33 | `composer` | low | MosaicML Composer高效训练库，内置100+算法和优化方法 |
| 34 | `continue-dev` | low | Continue.dev开源IDE AI编程助手，支持VS Code/JetBrains，本地/云端模型自由切换 |
| 35 | `coremltools` | low | Apple CoreML模型转换工具，将PyTorch/TensorFlow转换为iOS/macOS原生格式 |
| 36 | `cortex` | low | Cortex本地LLM平台，一键运行和管理多种开源模型 |
| 37 | `crewai` | medium | CrewAI多Agent协作框架，角色扮演、任务委派、团队协作执行复杂工作流 |
| 38 | `crypten` | medium | CrypTen Facebook隐私计算库，基于MPC(安全多方计算)的加密机器学习，支持加密推理和训练 |
| 39 | `ctranslate2` | low | CTranslate2高效推理引擎，支持INT8/INT16/FP16量化，CPU/GPU加速 |
| 40 | `datacompy` | low | 数据集对比工具，比较两个DataFrame的差异，适用于数据验证和回归测试 |
| 41 | `datasets-cli` | low | HuggingFace Datasets命令行工具，支持数据集下载、加载、转换和发布 |
| 42 | `deepspeed` | medium | 微软DeepSpeed大规模分布式训练框架，支持ZeRO优化、3D并行、Offload |
| 43 | `diffusers-cli` | low | HuggingFace Diffusers扩散模型工具，管理文生图/视频模型管线、调度器配置 |
| 44 | `dify` | medium | Dify开源LLM应用开发平台，可视化编排Agent、RAG、工作流，支持自托管 |
| 45 | `distilabel` | low | Distilabel合成数据生成与模型蒸馏框架，用LLM生成高质量训练数据，支持自对弈和批评 |
| 46 | `docling` | low | IBM Docling开源文档解析，支持PDF/HTML/图片/PPT，保留文档结构生成Markdown |
| 47 | `dpo` | medium | DPO (Direct Preference Optimization) 直接偏好优化，无需奖励模型直接从偏好数据微调 |
| 48 | `ds-1000` | high | DS-1000数据科学代码评测基准，1000个真实数据科学问题，测试pandas/numpy/sklearn等库使用 |
| 49 | `dspy` | low | DSPy声明式LLM编程框架，优化提示和权重而非手工工程 |
| 50 | `dvc` | medium | DVC数据版本控制，Git-like管理数据集和模型，支持S3/GS/Azure存储 |
| 51 | `einops` | low | Einops张量操作语义化库，清晰表达reshape、transpose、reduce等维度变换操作 |
| 52 | `elasticsearch` | low | Elasticsearch分布式搜索与分析，8.x版本原生支持dense_vector语义搜索 |
| 53 | `embedchain` | low | EmbedChain RAG框架，简化数据加载、分块、嵌入、查询全流程 |
| 54 | `evidently` | low | Evidently AI模型与数据漂移检测，支持表格数据、NLP、CV全链路监控 |
| 55 | `executorch` | low | ExecuTorch PyTorch移动端运行时，支持iOS/Android/嵌入式，端到端推理优化 |
| 56 | `faiss-cli` | low | Facebook AI Similarity Search (FaisS)高性能向量搜索库，支持GPU加速 |
| 57 | `faster-whisper` | low | Faster-Whisper CTranslate2加速版Whisper，4倍速度提升，更低内存占用 |
| 58 | `feast` | medium | Feast开源特征存储平台，统一管理ML特征的定义、存储和服务 |
| 59 | `fireworks` | low | Fireworks AI快速推理API，针对开源模型优化的高性能端点 |
| 60 | `flash-attn` | low | Flash Attention高效注意力实现，2-4倍加速长序列训练，显著降低内存占用 |
| 61 | `flower` | medium | Flower联邦学习框架，支持横向/纵向联邦、差分隐私、安全聚合，工业级跨设备联合训练 |
| 62 | `flowise` | medium | Flowise可视化LangChain工作流构建器，拖拽式创建LLM应用 |
| 63 | `garak` | high | Garak LLM漏洞扫描框架，探测越狱、提示注入、数据泄露、幻觉等安全风险 |
| 64 | `gguf-convert` | low | GGUF格式转换工具，将HuggingFace模型转换为llama.cpp兼容格式 |
| 65 | `git-lfs` | medium | Git Large File Storage，管理大模型权重文件(GB级)的版本控制 |
| 66 | `gradio` | medium | Gradio快速构建ML模型交互式Demo，自动生成可分享的Web界面 |
| 67 | `great-expectations` | low | Great Expectations数据质量验证框架，定义和监控数据期望 |
| 68 | `groq` | low | Groq极速推理API，基于LPU芯片实现业界最快token生成速度 |
| 69 | `grpo` | medium | GRPO (Group Relative Policy Optimization) 强化学习训练，DeepSeek-R1核心训练方法，无需价值模型 |
| 70 | `guidance` | low | Guidance可控生成库，通过语法约束LLM输出结构，确保JSON/代码格式正确 |
| 71 | `haystack` | medium | Haystack端到端NLP框架，支持RAG、Agent、文档搜索、Pipeline编排 |
| 72 | `helicone` | low | Helicone LLM可观测性网关，一行代码接入，支持缓存、重试、成本追踪、A/B测试 |
| 73 | `huggingface-cli` | low | HuggingFace Hub命令行工具，支持模型/数据集/Space的上传下载管理 |
| 74 | `humaneval` | high | HumanEval代码生成评测基准，164个Python编程问题，测试函数级代码生成能力 |
| 75 | `humaneval-exec` | high | HumanEval代码评测执行器，运行模型生成的代码并通过单元测试，计算pass@k指标 |
| 76 | `img2dataset` | medium | 从URL列表批量下载图像并构建WebDataset格式，支持分布式处理 |
| 77 | `inspect-ai` | low | UK AISI Inspect AI评测框架，系统化评估模型知识、推理、安全性和能力 |
| 78 | `instructor` | low | Instructor结构化输出库，基于Pydantic验证LLM响应，确保类型安全 |
| 79 | `instructor` | low | Instructor结构化输出框架，基于Pydantic让LLM返回类型安全的结构化数据 |
| 80 | `iree-compile` | medium | Google IREE MLIR编译器，将深度学习模型编译为Vulkan/SPIR-V/Metal/WebGPU可执行代码 |
| 81 | `judge-eval` | low | LLM-as-Judge评估框架，系统化评估裁判模型质量，减少位置偏见和长度偏见 |
| 82 | `keywords-ai` | low | Keywords AI统一LLM API管理平台，支持多密钥管理、日志分析、用户追踪 |
| 83 | `kfp` | medium | Kubeflow Pipelines (KFP) 命令行客户端 |
| 84 | `kong-ai-gateway` | medium | Kong企业级AI网关，支持LLM路由、速率限制、语义缓存、令牌消耗控制 |
| 85 | `kserve` | medium | KServe Kubernetes原生模型服务平台，支持自动扩缩容、金丝雀发布、多框架运行时 |
| 86 | `label-studio` | low | Label Studio开源数据标注平台，支持图像、文本、音频、视频、时间序列等多模态标注 |
| 87 | `lancedb` | low | LanceDB无服务器向量数据库，基于Apache Arrow列式存储，支持嵌入和全文搜索 |
| 88 | `langchain` | medium | LangChain LLM应用开发框架，支持Chains、Agents、RAG、工具调用 |
| 89 | `langchain-hub` | low | LangChain Hub Prompt模板共享平台，复用社区验证的Prompt模板和链式组件 |
| 90 | `langfuse` | low | Langfuse开源LLM可观测性平台，支持自托管，追踪成本、延迟、质量指标 |
| 91 | `langgraph` | medium | LangGraph状态机Agent框架，支持循环、条件分支、持久化、人机协同 |
| 92 | `langsmith` | low | LangSmith LLM应用全链路追踪与评估平台，记录输入输出、token消耗、延迟 |
| 93 | `langtrace` | low | Langtrace开源LLM应用追踪，兼容OpenTelemetry，支持多框架 |
| 94 | `lightning` | low | PyTorch Lightning高级训练框架，简化分布式训练、混合精度、Checkpoint管理 |
| 95 | `lime` | low | LIME (Local Interpretable Model-agnostic Explanations) 局部代理模型解释，扰动样本训练可解释模型 |
| 96 | `litellm-proxy` | medium | LiteLLM代理网关，统一管理100+ LLM API，支持负载均衡、速率限制、成本追踪 |
| 97 | `livecodebench` | high | LiveCodeBench实时代码评测，持续更新的编程题 benchmark，防数据污染，反映模型真实代码能力 |
| 98 | `llama-factory` | low | LLaMA-Factory一站式大模型微调框架，支持100+模型，预训练/微调/DPO/RLHF全流程 |
| 99 | `llama-index` | medium | LlamaIndex数据框架，连接LLM与私有数据，支持RAG、Agent、工作流 |
| 100 | `llama.cpp` | low | llama.cpp纯C/C++实现的LLM推理，支持GGUF量化，可在CPU/边缘设备运行 |
| 101 | `llamaparse` | low | LlamaParse LlamaIndex高级PDF解析服务，GenAI原生解析，支持表格、图表、数学公式 |
| 102 | `llava` | low | LLaVA大语言视觉助手，视觉指令微调，支持图像问答、描述、推理 |
| 103 | `llm-as-judge` | low | LLM-as-Judge方法论实现，位置偏见校正、一致性检验、多维度评分 |
| 104 | `llm-factory` | medium | 一站式LLM训练平台，支持100+模型预训练、微调、RLHF、DPO、量化、推理 |
| 105 | `llm-guard` | low | LLM Guard输入输出安全过滤器，检测PII泄露、毒性、越狱、提示注入 |
| 106 | `lm-eval` | low | EleutherAI语言模型评估框架，支持HellaSwag、MMLU、ARC等100+基准测试 |
| 107 | `lmdeploy` | medium | 上海AI Lab开源的大模型部署工具，支持TurboMind引擎和PyTorch引擎 |
| 108 | `long-context-eval` | low | 长上下文评测工具，Needle-in-Haystack、RULER等，测试模型在超长文本中的信息检索能力 |
| 109 | `mamba` | low | Mamba状态空间模型(SSM)实现，线性复杂度序列建模，替代Transformer注意力机制 |
| 110 | `marimo` | low | Marimo响应式Python Notebook，支持交互式数据探索和模型实验 |
| 111 | `marker` | low | Marker高性能PDF转Markdown工具，基于布局模型，准确提取表格、公式、代码块 |
| 112 | `marqo` | low | Marqo端到端向量搜索引擎，内置向量化，零配置语义搜索 |
| 113 | `math-eval` | low | 数学能力评测工具，支持GSM8K、MATH、SVAMP等数据集，验证模型推理和计算准确性 |
| 114 | `mbpp` | high | MBPP (Mostly Basic Python Programming) 代码生成评测，974个Python编程任务 |
| 115 | `mediapipe` | low | Google MediaPipe端侧ML流水线，支持人脸检测、姿态估计、手势识别、文本分类 |
| 116 | `megatron-lm` | high | NVIDIA Megatron-LM大规模语言模型训练框架，支持张量/流水线/序列并行 |
| 117 | `meilisearch` | - | 开源即时搜索引擎，支持容错搜索和中文分词 |
| 118 | `mergekit` | low | MergeKit模型合并工具，支持SLERP、TIES、DARE、Model Stock等多种合并算法，无需GPU |
| 119 | `milvus-cli` | medium | Milvus分布式向量数据库CLI，支持十亿级向量的高性能ANN搜索 |
| 120 | `mlc-llm` | low | MLC LLM全平台大模型部署，支持手机/浏览器/边缘设备/云端 |
| 121 | `mlflow` | medium | MLflow 命令行客户端，用于模型全生命周期管理 |
| 122 | `mlflow-tracking` | low | MLflow Tracking模块，本地实验跟踪与模型注册 |
| 123 | `mlir-opt` | low | MLIR中间表示优化器，对计算图进行 lowering、融合、循环变换等编译优化 |
| 124 | `modal` | medium | Modal Serverless云平台，按需弹性运行AI训练与推理任务 |
| 125 | `model-card` | low | 模型卡片(model card)编写规范，记录模型用途、限制、训练数据等元信息 |
| 126 | `model-pruner` | high | 模型剪枝工具，移除不重要的权重或神经元，减小模型体积加速推理 |
| 127 | `modelcards` | low | HuggingFace Model Card工具，生成和管理模型文档，确保模型可追溯和合规 |
| 128 | `modelscan` | low | ProtectAI ModelScan模型文件安全扫描，检测Pickle反序列化漏洞、恶意代码注入 |
| 129 | `modelscope` | low | 魔搭社区ModelScope命令行工具，国产开源模型仓库管理 |
| 130 | `mosaicml-streaming` | low | MosaicML Streaming高效数据集流式加载，支持多种云存储和Sharding |
| 131 | `mt-bench` | low | MT-Bench多轮对话评测基准，80个高质量多轮问题，GPT-4作为裁判评分 |
| 132 | `multilingual-eval` | low | 多语言能力评测，支持C-Eval(中文)、MMLU多语言、XCOPA、XNLI等跨语言基准 |
| 133 | `n8n` | medium | n8n开源AI工作流自动化平台，低代码编排LLM、数据库、API、通知等节点 |
| 134 | `neo4j-llm` | medium | Neo4j图数据库+LLM知识图谱构建工具，从非结构化文本自动抽取实体关系构建图谱 |
| 135 | `neptune` | low | Neptune ML实验管理平台，支持指标跟踪、模型版本、数据集版本管理 |
| 136 | `neuralsecure` | medium | NeuralSecure ML模型安全审计，检测对抗样本脆弱性、成员推断攻击、模型窃取风险 |
| 137 | `neuronx-cc` | medium | AWS Neuron编译器，将PyTorch/TensorFlow模型编译为Trainium/Inferentia高效执行格式 |
| 138 | `neuronx-nxdt` | medium | AWS Neuron分布式训练工具，针对Trainium芯片优化的LLM训练 |
| 139 | `ollama` | low | Ollama本地大模型运行管理工具，一键下载和运行各类开源模型 |
| 140 | `onnx-optimizer` | low | ONNX模型图优化器，常量折叠、算子融合、死代码消除，跨平台推理前必备优化 |
| 141 | `onnxruntime` | low | ONNX Runtime跨平台推理加速引擎，支持CPU/GPU/边缘设备 |
| 142 | `opacus` | medium | Opacus PyTorch差分隐私训练库，通过梯度裁剪和噪声注入实现(ε,δ)-差分隐私保证 |
| 143 | `openai-agents` | medium | OpenAI官方Agents SDK，支持Responses API、工具调用、网络搜索、文件搜索 |
| 144 | `openai-function-calling` | medium | OpenAI Function Calling工具调用，让LLM自主决定调用外部API获取实时数据或执行操作 |
| 145 | `opencompass` | low | 上海AI Lab开源的模型评测平台，支持50+数据集和多种评测范式 |
| 146 | `openhands` | critical | OpenHands (原OpenDevin) 开源AI软件工程师，自主完成开发任务，支持多Agent协作 |
| 147 | `openrouter` | low | OpenRouter统一访问100+开源和商用模型API，标准化接口、自动竞价 |
| 148 | `opensearch` | low | OpenSearch分布式搜索与分析引擎，支持k-NN向量搜索、ML推理插件 |
| 149 | `openvino` | low | Intel OpenVINO工具包，针对Intel CPU/GPU/NPU优化的推理框架 |
| 150 | `opik` | low | Comet Opik开源LLM评估与追踪平台，支持RAG评估、提示工程、实验管理 |
| 151 | `optimum-cli` | medium | HuggingFace Optimum模型优化工具，支持ONNX/TensorRT/OpenVINO导出和量化 |
| 152 | `outlines` | - | LLM结构化生成库，强制模型输出JSON/Regex格式 |
| 153 | `paddle-lite` | low | Paddle Lite百度端侧推理框架，支持ARM Cortex-M到服务器GPU，极致轻量 |
| 154 | `paddle2onnx` | low | PaddlePaddle到ONNX转换工具，支持Paddle模型导出为ONNX格式 |
| 155 | `pair-wise-eval` | low | Pair-wise成对比较评测，ELO评分系统，适用于模型A/B测试和排序 |
| 156 | `peft` | low | 参数高效微调库，支持LoRA、QLoRA、IA3、Prompt Tuning等方法 |
| 157 | `pgvector` | medium | pgvector PostgreSQL向量扩展，在关系数据库中直接存储和查询向量 |
| 158 | `phidata` | low | Phidata构建AI助手的框架，支持知识库、结构化输出、多模态(已合并为Agno) |
| 159 | `phoenix` | low | Arize Phoenix开源LLM可观测性和评估工具，支持追踪、评估、数据集管理 |
| 160 | `pinecone` | low | Pinecone全托管向量数据库，零运维，自动扩缩容 |
| 161 | `portkey` | low | Portkey AI网关，支持语义缓存、智能重试、负载均衡、多模型Fallback |
| 162 | `praisonai` | medium | PraisonAI低代码多Agent框架，基于CrewAI，支持AutoGen集成和UI界面 |
| 163 | `prefix-caching` | low | Prefix Caching前缀缓存，复用共享系统Prompt的KV Cache，大幅降低多轮推理延迟和显存 |
| 164 | `prometheus-eval` | low | Prometheus开源LLM评估模型，无需GPT-4即可进行高质量指令评测 |
| 165 | `promptflow` | low | 微软PromptFlow Prompt工程与LLM应用开发框架，可视化编排、评估、部署一体化 |
| 166 | `promptfoo` | low | Promptfoo Prompt测试与回归框架，CI/CD集成，防止Prompt退化 |
| 167 | `promptlayer` | low | PromptLayer提示词版本管理与追踪，记录提示词迭代历史和效果对比 |
| 168 | `pulsar` | medium | Apache Pulsar分布式消息流平台，用于AI流水线事件驱动和数据流处理 |
| 169 | `pydantic-ai` | low | PydanticAI类型安全Agent框架，Samuel Colvin(Pydantic作者)出品，强类型验证 |
| 170 | `pymupdf` | low | PyMuPDF高性能PDF处理库，提取文本/图像/注释，支持PDF编辑和转换 |
| 171 | `pytorch-lightning` | low | PyTorch Lightning高级训练框架，简化分布式训练、混合精度、Checkpoint管理 |
| 172 | `pyvertical` | high | PyVertical垂直联邦学习框架，特征分片联合建模，适用于银行+电商等跨机构数据互补场景 |
| 173 | `qdrant` | low | Qdrant高性能开源向量数据库，支持过滤搜索、分布式部署、Rust实现 |
| 174 | `ray-serve` | medium | Ray Serve可扩展模型服务框架，支持多模型组合、A/B测试、自动扩缩容 |
| 175 | `red-teaming` | high | PyRIT (Python Risk Identification Toolkit) 微软开源红队测试框架，自动化LLM安全测试 |
| 176 | `redisearch` | low | RediSearch Redis向量搜索模块，支持向量相似性搜索+全文搜索混合查询 |
| 177 | `replicate` | low | Replicate模型托管云平台，一键部署和运行开源模型 |
| 178 | `runpod` | - | RunPod GPU云平台，按需租用GPU进行AI训练和推理 |
| 179 | `safetensors-convert` | low | Safetensors安全模型格式转换工具，替代pickle防止恶意代码执行 |
| 180 | `safety-eval` | low | MLSafety模型安全评测套件，覆盖毒性、偏见、隐私泄露、越狱抗性 |
| 181 | `semantic-kernel` | medium | Microsoft Semantic Kernel SDK，连接LLM、记忆、规划器和插件 |
| 182 | `sglang` | medium | SGLang结构化生成语言模型服务，支持RadixAttention缓存、多模态推理 |
| 183 | `shap` | low | SHAP (SHapley Additive exPlanations) 博弈论特征归因，精确量化每个特征对预测的贡献 |
| 184 | `sky-pilot` | medium | SkyPilot云端ML任务调度器，一键在AWS/GCP/Azure/Lambda运行训练/推理 |
| 185 | `smolagents` | high | HuggingFace SmolAgents极简Agent库，代码优先，最小抽象，高度透明 |
| 186 | `snorkel` | medium | Snorkel弱监督标注框架，通过编程方式生成训练标签，减少人工标注成本 |
| 187 | `speculative-decoding` | low | 推测解码(Speculative Decoding)加速推理，用小草稿模型预测大目标模型输出，2-3倍加速 |
| 188 | `stable-diffusion-cli` | medium | Stable Diffusion文本到图像生成命令行工具，支持多种模型和LoRA |
| 189 | `streamlit` | low | Streamlit数据应用与模型展示框架，纯Python构建数据科学应用 |
| 190 | `swe-agent` | critical | SWE-Agent自动修复GitHub Issue，分析Issue、编辑代码、运行测试验证修复 |
| 191 | `swe-bench` | medium | SWE-bench软件工程评测基准，测试LLM解决真实GitHub Issue的能力 |
| 192 | `tensor-parallel` | medium | Tensor Parallel通用张量并行推理库，支持任意HuggingFace模型多卡推理 |
| 193 | `tensorboard` | low | TensorFlow和PyTorch的训练可视化工具 |
| 194 | `tensorboard-profiler` | low | TensorBoard Profiler性能分析插件，分析模型训练中的CPU/GPU瓶颈 |
| 195 | `tensorrt-llm` | medium | NVIDIA TensorRT-LLM推理优化库，针对NVIDIA GPU极致优化 |
| 196 | `text-generation-inference` | medium | HuggingFace TGI文本生成推理服务，生产级部署方案 |
| 197 | `text2sql` | high | Text2SQL自然语言转SQL工具，基于LLM将业务问题转换为可执行的数据库查询 |
| 198 | `tf2onnx` | low | TensorFlow到ONNX转换工具，支持SavedModel、Checkpoint、Keras模型 |
| 199 | `tflite` | low | TensorFlow Lite移动端和嵌入式推理框架，支持Android/iOS/ARM/Raspberry Pi |
| 200 | `timm` | low | PyTorch Image Models库，800+预训练视觉模型，涵盖ViT、ConvNeXt、Swin Transformer等 |
| 201 | `together` | low | Together AI API客户端，访问高性能开源模型推理API |
| 202 | `token-heatmap` | low | Token级别归因热图，可视化每个输入token对模型输出的贡献度，定位幻觉和错误关注 |
| 203 | `tool-bench` | medium | ToolBench工具使用评测基准，16000+ API，测试LLM的工具选择、调用、组合能力 |
| 204 | `torch-titan` | medium | PyTorch官方原生大模型训练参考实现，支持FSDP2、TP、PP、CP |
| 205 | `torchrun` | low | PyTorch分布式训练启动器 |
| 206 | `torchserve` | medium | PyTorch官方模型服务框架，支持模型打包、A/B测试、多模型服务、自定义处理器 |
| 207 | `transformers-cli` | low | HuggingFace Transformers命令行工具，查看模型配置、下载模型、转换格式 |
| 208 | `transformers-pipeline` | low | HuggingFace Transformers Pipeline快速推理接口，一行代码完成文本生成/分类/问答 |
| 209 | `tritonserver` | medium | NVIDIA Triton推理服务器，支持TensorRT、ONNX、PyTorch、Python后端，多模型并行服务 |
| 210 | `trl` | medium | Transformers Reinforcement Learning，支持SFT、DPO、PPO、ORPO训练 |
| 211 | `trtexec` | medium | TensorRT引擎构建与性能测试工具，将ONNX/UFF转为TensorRT序列化引擎，极致NVIDIA GPU优化 |
| 212 | `turbopuffer` | low | Turbopuffer高性能托管向量搜索，专为RAG应用优化，支持混合搜索 |
| 213 | `tvmc` | medium | TVM命令行编译器，将模型编译为高性能机器码，支持ARM/x86/GPU/FPGA多种后端 |
| 214 | `typesense` | low | Typesense开源搜索引擎，支持向量搜索、拼写容错、分面过滤、地理搜索 |
| 215 | `unsloth` | low | 2-5倍加速的LLM微调框架，支持LoRA和QLoRA，内存占用减少80% |
| 216 | `unstructured` | low | Unstructured通用文档解析库，支持PDF/Word/PPT/HTML/图片等50+格式提取文本 |
| 217 | `vanna` | high | Vanna AI SQL生成框架，RAG增强的Text2SQL，支持训练领域Schema并持续优化 |
| 218 | `vespa-cli` | medium | Vespa大规模搜索与推理引擎，支持向量搜索+结构化搜索+机器学习推理 |
| 219 | `vllm` | medium | vLLM高性能大模型推理引擎，采用PagedAttention实现最高24倍吞吐提升 |
| 220 | `wandb` | low | Weights & Biases实验跟踪平台，记录指标、超参数、模型版本、数据集血缘 |
| 221 | `weaviate-cli` | low | Weaviate AI原生向量数据库，内置向量化和模块化扩展(GraphQL接口) |
| 222 | `webdataset` | low | WebDataset大规模数据集流式处理库，高效处理TB级训练数据 |
| 223 | `weights-biases-sweep` | medium | W&B超参数搜索(Sweep)，支持网格搜索、随机搜索、贝叶斯优化 |
| 224 | `whisper` | low | OpenAI Whisper通用语音识别模型，支持99种语言，多尺寸模型(tiny~large-v3) |
| 225 | `whylogs` | low | WhyLogs数据日志分析，轻量级数据画像和漂移检测 |
| 226 | `xformers` | low | Meta开源的高效Transformer组件库，提供memory_efficient_attention等优化算子 |
| 227 | `xla_compile` | low | TensorFlow XLA(Accelerated Linear Algebra)即时编译，将计算图编译为机器码，TPU训练推理加速 |

## 操作系统 (69)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `apt install` | medium | Install new packages |
| 2 | `apt remove` | high | Remove installed packages |
| 3 | `apt search` | low | Search for packages |
| 4 | `apt update` | low | Update package index from repositories |
| 5 | `apt upgrade` | medium | Upgrade all installed packages |
| 6 | `apt-cache show` | low | Show package information |
| 7 | `awk` | - | 文本处理语言，按模式扫描和处理文件 |
| 8 | `bash` | - | Bash Shell 解释器，执行脚本文件或交互式命令 |
| 9 | `cat` | - | 连接文件并输出到标准输出 |
| 10 | `cd` | - | 切换当前工作目录 |
| 11 | `cp` | medium | 复制文件或目录 |
| 12 | `dnf install` | medium | Install packages (newer package manager for CentOS 8+) |
| 13 | `dpkg -i` | high | Install .deb package file |
| 14 | `dpkg -l` | low | List installed packages |
| 15 | `dpkg -r` | high | Remove installed package |
| 16 | `egrep` | - | 扩展正则表达式grep（等同于grep -E） |
| 17 | `export` | - | 设置或显示环境变量 |
| 18 | `fgrep` | - | 固定字符串grep（等同于grep -F），禁用正则表达式 |
| 19 | `find` | high | 在目录树中搜索文件 |
| 20 | `firewall-cmd --add-port` | medium | Open firewall port |
| 21 | `firewall-cmd --list-all` | low | List all firewall rules |
| 22 | `getenforce` | low | Get current SELinux mode |
| 23 | `grep` | - | 在文件中搜索文本模式 |
| 24 | `head` | - | 显示文件开头部分 |
| 25 | `kill` | - | 向进程发送信号以终止或控制 |
| 26 | `less` | - | 分页查看文件内容，支持前后翻页 |
| 27 | `locate` | - | 通过预建数据库快速查找文件 |
| 28 | `ls` | - | 列出目录内容 |
| 29 | `more` | - | 分页查看文件内容（less的简化版） |
| 30 | `mv` | medium | 移动或重命名文件和目录 |
| 31 | `pwd` | - | 显示当前工作目录的完整路径 |
| 32 | `rename` | - | 批量重命名文件（Perl正则表达式版或util-linux版） |
| 33 | `rm` | critical | 删除文件或目录 |
| 34 | `rmdir` | - | 删除空目录 |
| 35 | `rpm -e` | high | Erase (remove) installed package |
| 36 | `rpm -i` | high | Install RPM package file |
| 37 | `rpm -qa` | low | Query all installed packages |
| 38 | `rpm -qi` | low | Query package information |
| 39 | `rsync` | - | 远程和本地文件同步工具，支持增量传输 |
| 40 | `sed` | - | 流编辑器，执行基本的文本转换 |
| 41 | `sestatus` | low | Display SELinux status |
| 42 | `setenforce` | high | Change SELinux mode temporarily |
| 43 | `sh` | - | Bourne Shell，标准的Unix命令解释器 |
| 44 | `shellcheck` | - | Shell 脚本静态分析工具，检测常见错误和最佳实践 |
| 45 | `shfmt` | - | Shell 脚本格式化工具 |
| 46 | `snap install` | low | Install snap package |
| 47 | `source` | medium | 在当前 Shell 环境中执行脚本（不创建子进程） |
| 48 | `systemctl disable` | low | Disable service from starting on boot |
| 49 | `systemctl enable` | medium | Enable service to start on boot |
| 50 | `systemctl restart` | medium | Restart a systemd service |
| 51 | `systemctl start` | medium | Start a systemd service |
| 52 | `systemctl status` | low | Check service status |
| 53 | `systemctl stop` | high | Stop a systemd service |
| 54 | `tail` | - | 显示文件末尾部分，支持实时跟踪 |
| 55 | `trap` | - | 捕获信号并在脚本中执行清理操作 |
| 56 | `trash` | - | 将文件移动到回收站而非永久删除 |
| 57 | `ufw allow` | medium | Allow firewall rule |
| 58 | `ufw deny` | medium | Deny firewall rule |
| 59 | `ufw enable` | high | Enable Ubuntu firewall |
| 60 | `ufw status` | low | Show firewall status and rules |
| 61 | `whereis` | - | 定位命令的二进制、源码和手册页文件 |
| 62 | `which` | - | 查找命令的可执行文件路径 |
| 63 | `yum info` | low | Show package information |
| 64 | `yum install` | medium | Install new packages |
| 65 | `yum list installed` | low | List all installed packages |
| 66 | `yum remove` | high | Remove installed packages |
| 67 | `yum search` | low | Search for packages |
| 68 | `yum update` | medium | Update all installed packages |
| 69 | `zsh` | - | Z Shell，功能强大的交互式Shell，兼容Bash |

## 编程语言 (38)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `cargo` | - | Rust 包管理器和构建工具 |
| 2 | `cargo clippy` | - | Rust 代码 lint 工具，检测常见错误和改进建议 |
| 3 | `cargo fmt` | - | Rust 代码格式化工具 |
| 4 | `go build` | medium | 编译Go包和依赖 |
| 5 | `go fmt` | medium | 格式化Go代码 |
| 6 | `go get` | medium | 添加依赖到当前模块 |
| 7 | `go install` | - | 编译并安装Go包到$GOPATH/bin |
| 8 | `go mod` | medium | 模块维护 |
| 9 | `go run` | low | 编译并运行Go程序 |
| 10 | `go test` | low | 运行测试 |
| 11 | `go vet` | low | 检查Go代码中的常见错误 |
| 12 | `jar` | - | 创建和管理JAR文件 |
| 13 | `java` | - | 运行Java程序 |
| 14 | `javac` | - | 编译Java源代码 |
| 15 | `javadoc` | - | 生成Java文档 |
| 16 | `jcmd` | - | 向运行JVM发送诊断命令 |
| 17 | `jhat` | - | Java堆分析工具，分析堆转储文件 |
| 18 | `jmap` | medium | 生成堆转储和内存映射 |
| 19 | `jps` | - | 显示Java进程状态 |
| 20 | `jstack` | - | 打印Java线程堆栈 |
| 21 | `jstat` | - | 监控JVM统计信息 |
| 22 | `node` | medium | Execute JavaScript code using Node.js runtime |
| 23 | `npm audit` | medium | Check for security vulnerabilities |
| 24 | `npm install` | medium | Install package dependencies |
| 25 | `npm outdated` | low | Check for outdated packages |
| 26 | `npm publish` | high | Publish package to npm registry |
| 27 | `npm run` | medium | Run arbitrary package scripts |
| 28 | `npm start` | medium | Run the start script defined in package.json |
| 29 | `npm test` | low | Run the test script defined in package.json |
| 30 | `npm update` | medium | Update packages to their latest versions |
| 31 | `npx` | medium | Execute npm package binaries |
| 32 | `pip` | medium | Python包管理器 |
| 33 | `pylint` | low | Python代码检查工具 |
| 34 | `pytest` | low | Python测试框架 |
| 35 | `python` | low | 运行Python解释器 |
| 36 | `rustc` | - | Rust 编译器 |
| 37 | `rustup` | medium | Rust 工具链安装器和版本管理器 |
| 38 | `virtualenv` | medium | 创建Python虚拟环境 |

## 容器编排 (34)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `docker attach` | - | 附加到正在运行的容器 |
| 2 | `docker build` | - | 从Dockerfile构建镜像 |
| 3 | `docker exec` | - | 在运行中的容器内执行命令 |
| 4 | `docker images` | - | 列出本地镜像 |
| 5 | `docker inspect` | - | 获取容器或镜像的底层信息 |
| 6 | `docker logs` | - | 查看容器日志 |
| 7 | `docker ps` | - | 列出运行中的容器 |
| 8 | `docker pull` | - | 从镜像仓库拉取镜像 |
| 9 | `docker push` | - | 将本地镜像推送到镜像仓库 |
| 10 | `docker restart` | - | 重启一个或多个容器 |
| 11 | `docker rm` | medium | 删除容器 |
| 12 | `docker rmi` | - | 删除本地镜像 |
| 13 | `docker run` | - | 运行一个新容器 |
| 14 | `docker start` | - | 启动一个或多个已停止的容器 |
| 15 | `docker stop` | - | 停止运行中的容器 |
| 16 | `docker-compose` | - | 管理多容器应用 |
| 17 | `kafka` | - | Apache Kafka分布式消息队列 |
| 18 | `kubectl` | - | Kubernetes命令行工具，管理集群资源 |
| 19 | `kubectl annotate` | low | Update annotations on a resource |
| 20 | `kubectl apply` | high | Apply a configuration to a resource by filename or stdin |
| 21 | `kubectl config` | high | Modify kubeconfig files |
| 22 | `kubectl cordon` | medium | Mark node as unschedulable |
| 23 | `kubectl create` | medium | Create a resource from a file or stdin |
| 24 | `kubectl delete` | critical | Delete resources by filenames, resources and names, or by label selectors |
| 25 | `kubectl describe` | low | Show detailed information about a resource |
| 26 | `kubectl drain` | critical | Drain node in preparation for maintenance |
| 27 | `kubectl exec` | high | Execute a command in a container |
| 28 | `kubectl get` | low | Display one or many resources |
| 29 | `kubectl label` | medium | Update labels on a resource |
| 30 | `kubectl logs` | low | Print the logs for a container in a pod |
| 31 | `kubectl port-forward` | medium | Forward one or more local ports to a pod |
| 32 | `kubectl rollout` | high | Manage the rollout of a resource |
| 33 | `kubectl scale` | high | Set a new size for a deployment, replica set, or replication controller |
| 34 | `kubectl top` | low | Display resource (CPU/memory) usage |

## 版本控制 (31)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `git add` | - | 添加文件到暂存区 |
| 2 | `git branch` | - | 列出、创建或删除分支 |
| 3 | `git checkout` | medium | 切换分支或恢复文件 |
| 4 | `git clone` | - | 克隆远程仓库到本地 |
| 5 | `git commit` | - | 提交暂存区的更改 |
| 6 | `git diff` | - | 显示工作区与暂存区或提交之间的差异 |
| 7 | `git fetch` | - | 从远程仓库下载对象和引用，但不合并 |
| 8 | `git init` | - | 初始化新的Git仓库 |
| 9 | `git log` | - | 查看提交历史 |
| 10 | `git merge` | - | 合并分支 |
| 11 | `git pull` | - | 拉取远程更改并合并 |
| 12 | `git push` | high | 推送本地提交到远程仓库 |
| 13 | `git rebase` | - | 将当前分支变基到另一分支，重写提交历史 |
| 14 | `git restore` | - | 恢复工作区或暂存区文件（Git 2.23+ 推荐替代checkout） |
| 15 | `git show` | - | 显示提交、标签或对象的详细信息和差异 |
| 16 | `git status` | - | 显示工作区状态 |
| 17 | `git switch` | - | 切换分支（Git 2.23+ 推荐替代checkout） |
| 18 | `svn add` | low | Add files to version control |
| 19 | `svn checkout` | low | Check out a working copy from a repository |
| 20 | `svn cleanup` | low | Clean up working copy (remove locks, fix interrupted operations) |
| 21 | `svn commit` | medium | Send changes to repository |
| 22 | `svn copy` | medium | Create a copy (branch/tag) in repository |
| 23 | `svn delete` | high | Remove files from version control |
| 24 | `svn diff` | low | Show differences between revisions |
| 25 | `svn info` | low | Display information about working copy or repository |
| 26 | `svn log` | low | Show commit log messages |
| 27 | `svn merge` | high | Merge changes from another branch |
| 28 | `svn revert` | high | Undo local changes |
| 29 | `svn status` | low | Show working copy status |
| 30 | `svn switch` | medium | Switch working copy to different URL |
| 31 | `svn update` | medium | Update working copy to latest revision |

## 数据库 (29)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `createdb` | medium | Create a new PostgreSQL database |
| 2 | `createuser` | high | Create a new PostgreSQL user |
| 3 | `dropdb` | critical | Remove a PostgreSQL database |
| 4 | `dropuser` | high | Remove a PostgreSQL user |
| 5 | `mysql` | high | MySQL command-line client for database operations |
| 6 | `mysql_secure_installation` | medium | Script to improve MySQL installation security |
| 7 | `mysqladmin` | critical | MySQL server administration utility |
| 8 | `mysqlbinlog` | high | Process MySQL binary log files |
| 9 | `mysqlcheck` | medium | Check, repair, analyze, and optimize MySQL tables |
| 10 | `mysqldump` | medium | MySQL database backup utility |
| 11 | `mysqlimport` | high | Import data from text files into MySQL tables |
| 12 | `mysqlshow` | low | Display database, table, and column information |
| 13 | `pg_basebackup` | medium | Take a base backup of a PostgreSQL cluster |
| 14 | `pg_dump` | medium | PostgreSQL database backup utility |
| 15 | `pg_isready` | low | Check PostgreSQL server connection status |
| 16 | `pg_restore` | high | Restore PostgreSQL database from archive |
| 17 | `psql` | high | PostgreSQL interactive terminal |
| 18 | `redis` | - | 启动Redis服务器 |
| 19 | `redis-benchmark` | medium | Redis performance benchmarking tool |
| 20 | `redis-check-aof` | high | Check and repair Redis AOF (Append-Only File) |
| 21 | `redis-check-rdb` | low | Check Redis RDB snapshot file |
| 22 | `redis-cli` | high | Redis command-line interface client |
| 23 | `redis-cli FLUSHDB` | critical | Delete all keys in current database |
| 24 | `redis-cli INFO` | low | Get Redis server information and statistics |
| 25 | `redis-cli MONITOR` | medium | Monitor all commands processed by Redis server |
| 26 | `redis-cli SAVE` | high | Synchronously save dataset to disk |
| 27 | `redis-sentinel` | high | Redis Sentinel for high availability |
| 28 | `redis-server` | high | Redis server daemon |
| 29 | `vacuumdb` | medium | Garbage-collect and analyze a PostgreSQL database |

## 系统诊断 (22)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `arthas` | medium | Start Arthas and attach to Java process |
| 2 | `classloader` | low | Display classloader information |
| 3 | `dashboard` | low | Display real-time dashboard of JVM metrics |
| 4 | `heapdump` | high | Dump Java heap to file |
| 5 | `jad` | low | Decompile Java class files |
| 6 | `logger` | medium | View or modify logger settings |
| 7 | `sc` | low | Search loaded classes |
| 8 | `sm` | low | Search methods in classes |
| 9 | `stack` | low | Display method call stack |
| 10 | `thread` | low | Display thread information |
| 11 | `trace` | medium | Trace method execution time |
| 12 | `tsar` | low | Display system performance statistics |
| 13 | `tsar --check` | low | Check tsar configuration and data files |
| 14 | `tsar --cpu` | low | Display detailed CPU statistics |
| 15 | `tsar --io` | low | Display disk I/O statistics |
| 16 | `tsar --list` | low | List available modules |
| 17 | `tsar --load` | low | Display system load average |
| 18 | `tsar --mem` | low | Display memory usage statistics |
| 19 | `tsar --partition` | low | Display disk partition usage |
| 20 | `tsar --tcp` | low | Display TCP connection statistics |
| 21 | `tsar --traffic` | low | Display network traffic statistics |
| 22 | `watch` | medium | Watch method invocation in real-time |

## 网络工具 (14)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `ab` | high | Apache HTTP server benchmarking tool |
| 2 | `curl` | - | 命令行HTTP客户端 |
| 3 | `dig` | low | DNS查询工具 |
| 4 | `host` | low | 简单的DNS查询工具 |
| 5 | `httpie` | medium | User-friendly HTTP client |
| 6 | `netstat` | - | 显示网络连接和路由表 |
| 7 | `nslookup` | low | 查询DNS信息 |
| 8 | `ping` | - | 测试网络连通性 |
| 9 | `postman` | low | API development and testing platform (CLI) |
| 10 | `siege` | high | HTTP load testing and benchmarking utility |
| 11 | `ss` | - | socket统计信息(替代netstat) |
| 12 | `tcpdump` | medium | 抓取和分析网络包 |
| 13 | `traceroute` | - | 跟踪数据包的路由路径 |
| 14 | `wget` | medium | Download files from the web |

## 构建工具 (10)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `cmake` | - | 跨平台构建系统生成器，管理 C/C++ 项目构建 |
| 2 | `gradle` | medium | Gradle 项目自动化构建工具，基于 Groovy/Kotlin DSL |
| 3 | `gradle init` | medium | Gradle Wrapper 初始化，生成 gradlew 脚本 |
| 4 | `gradlew` | medium | Gradle Wrapper 脚本，确保使用项目指定的 Gradle 版本 |
| 5 | `make` | medium | GNU Make 构建自动化工具，通过 Makefile 定义构建规则 |
| 6 | `make install` | high | 安装已编译的程序到系统目录（通常为 /usr/local） |
| 7 | `mvn` | medium | Apache Maven 项目管理工具，用于构建和管理 Java 项目 |
| 8 | `mvn archetype` | - | Maven 项目原型生成工具 |
| 9 | `mvn clean` | high | 清理构建输出目录(target) |
| 10 | `mvn dependency` | - | Maven 依赖管理子命令 |

## 云平台 (7)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `aws` | high | AWS 命令行接口，管理 AWS 服务和资源 |
| 2 | `aws cloudformation` | high | CloudFormation 基础设施即代码管理 |
| 3 | `aws configure` | high | 配置 AWS CLI 凭证和默认设置 |
| 4 | `aws eks` | - | EKS Kubernetes 集群管理 |
| 5 | `aws s3` | high | S3 存储桶和对象管理 |
| 6 | `aws sts` | - | AWS Security Token Service，管理临时凭证 |
| 7 | `terraform` | - | 基础设施即代码工具，管理云资源 |

## CI/CD (5)

| 序号 | 命令 | 风险等级 | 描述 |
| --- | --- | --- | --- |
| 1 | `act` | medium | 本地运行 GitHub Actions 工作流（无需推送到 GitHub） |
| 2 | `gh action` | - | 管理 GitHub Actions |
| 3 | `gh run` | medium | 查看和管理 GitHub Actions 运行记录 |
| 4 | `gh run cancel` | medium | 取消正在运行的 GitHub Actions 工作流 |
| 5 | `gh workflow` | - | 管理 GitHub Actions 工作流 |

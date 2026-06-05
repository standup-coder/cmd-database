---
cmd_name: flower
cmd_category: AI基础设施/联邦学习
cmd_dimension: 联邦学习
cmd_install: pip install flwr
cmd_platforms:
- linux
- darwin
- windows
summary: "Flower联邦学习框架，支持横向/纵向联邦、差分隐私、安全聚合，工业级跨设备联合训练"
cmd_level: intermediate
cmd_related:
- opacus
- pyvertical
cmd_tags:
- training
- safety
- federated
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/federated-learning.yaml
---


# flower

> Flower联邦学习框架，支持横向/纵向联邦、差分隐私、安全聚合，工业级跨设备联合训练

## 安装

```bash
pip install flwr
```

## 用法

```
flwr [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行Flower应用 |
| `server` | 启动聚合服务器 |
| `superlink` | 启动SuperLink |
| `supernode` | 启动SuperNode |

## 示例

### 示例 1: 运行Flower项目

```bash
flwr run .
```

### 示例 2: 启动开发模式服务器

```bash
flwr server --insecure
```

### 示例 3: 自定义联邦平均策略，3客户端聚合

```bash
python server.py --min_available_clients=3 --strategy FedAvg
```

## 关联命令

- [[opacus]]
- [[pyvertical]]

## 风险提示

> ⚠️ **MEDIUM**: 通信安全需配置TLS，防止模型参数泄露

## 参考链接

- [https://flower.ai/](https://flower.ai/)

## 所属维度

[[联邦学习-MOC|AI基础设施/联邦学习]]

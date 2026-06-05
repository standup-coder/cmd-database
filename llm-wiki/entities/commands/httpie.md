---
cmd_name: httpie
cmd_category: "网络工具/HTTP工具"
cmd_dimension: Network Tools
cmd_install: pip install httpie
cmd_platforms:
- linux
- darwin
- windows
summary: "User-friendly HTTP client"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/network/http.yaml
---


# httpie

> User-friendly HTTP client

## 安装

```bash
pip install httpie
```

## 用法

```
http [method] URL [items]
```

## 示例

### 示例 1: GET request

```bash
http GET https://api.example.com/users
```

### 示例 2: POST with JSON data

```bash
http POST https://api.example.com/users name=John
```

### 示例 3: PUT with typed JSON field

```bash
http PUT https://api.example.com/users/1 age:=25
```

### 示例 4: Request with authentication

```bash
http --auth user:pass https://api.example.com
```

## 风险提示

> ⚠️ **MEDIUM**: Credentials may be visible in command history

## 所属维度

[[HTTP工具-MOC|Network Tools]]

# cmd4coder GitHub Pages

这是 cmd4coder 项目的 GitHub Pages 官网源码。

## 📚 文档索引

本 `docs/` 目录包含项目文档与 GitHub Pages 网站源码。

| 子目录 | 内容 |
|--------|------|
| [`architecture/`](architecture/) | 架构说明文档 |
| [`guides/`](guides/) | 使用指南 |
| [`reference/`](reference/) | 参考手册 |
| [`reports/`](reports/) | 项目报告（LLM-Wiki 改造、AI 命令缺口分析等） |
| [`changelog/`](changelog/) | 更新日志 |
| [`build/`](build/) | 构建相关文档 |
| [`legal/`](legal/) | 许可证与法律文件 |
| [`assets/`](assets/) | 图标与图片资源 |
| [`css/`](css/) / [`js/`](js/) | GitHub Pages 样式与脚本 |

关键报告：

- [`reports/llm-wiki/IMPLEMENTATION_REPORT.md`](reports/llm-wiki/IMPLEMENTATION_REPORT.md) — LLM-Wiki 改造实施报告
- [`reports/ai-commands-gap-analysis.md`](reports/ai-commands-gap-analysis.md) — AI 命令缺口分析
- [`reports/project-evaluation-report.md`](reports/project-evaluation-report.md) — 项目评估报告

## 📁 目录结构

```
docs/
├── index.html          # 主页面
├── css/               # 样式文件
│   ├── reset.css      # CSS 重置
│   ├── variables.css  # CSS 变量
│   ├── layout.css     # 布局样式
│   ├── components.css # 组件样式
│   └── responsive.css # 响应式样式
├── js/                # JavaScript 文件
│   └── main.js        # 主要交互逻辑
└── assets/            # 资源文件
    └── icons/
        └── sprite.svg # SVG 图标集合
```

## 🚀 启用 GitHub Pages

### 步骤 1: 提交代码

确保 `docs/` 目录下的所有文件已提交到 main 分支：

```bash
git add docs/
git commit -m "Add GitHub Pages"
git push origin main
```

### 步骤 2: 配置 GitHub Pages

1. 打开 GitHub 仓库页面
2. 点击 **Settings** (设置)
3. 在左侧菜单中找到 **Pages**
4. 在 **Source** 部分：
   - Branch: 选择 `main`
   - Folder: 选择 `/docs`
5. 点击 **Save** (保存)

### 步骤 3: 等待部署

- GitHub 会自动构建和部署网站
- 通常需要 1-2 分钟
- 部署完成后，访问地址将显示在 Pages 设置页面

### 步骤 4: 访问网站

网站地址格式：
```
https://[用户名].github.io/cmd4coder/
```

例如：
```
https://cmd4coder.github.io/cmd4coder/
```

## 🔧 本地预览

### 使用 Python (推荐)

Python 3:
```bash
cd docs
python -m http.server 8000
```

Python 2:
```bash
cd docs
python -m SimpleHTTPServer 8000
```

然后在浏览器访问: `http://localhost:8000`

### 使用 Node.js

安装 http-server:
```bash
npm install -g http-server
```

运行服务器:
```bash
cd docs
http-server
```

### 使用 VS Code

安装 **Live Server** 扩展，右键点击 `index.html` 选择 "Open with Live Server"

## 📝 维护和更新

### 更新版本号

需要更新的位置：
1. `index.html` - Hero Section 的版本徽章
2. `index.html` - Download Section 的版本号

### 更新下载链接

所有下载按钮都指向 GitHub Releases 页面，会自动显示最新版本。

如需指向特定版本，修改链接格式为：
```html
https://github.com/cmd4coder/cmd4coder/releases/download/v1.0.0/cmd4coder-v1.0.0-linux-amd64.tar.gz
```

### 更新内容

1. 修改 `docs/index.html` 中的对应内容
2. 如需修改样式，编辑 `docs/css/` 下的对应文件
3. 提交并推送到 main 分支
4. GitHub Pages 会自动重新部署（1-2分钟）

## 🎨 设计规范

### 色彩方案

采用极简主义黑白配色：
- 主文字: `#000000`
- 次要文字: `#666666`
- 背景: `#FFFFFF`
- 边框: `#E0E0E0`
- 代码背景: `#1E1E1E`

### 字体

使用系统字体栈，确保跨平台一致性：
```css
-apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif
```

### 响应式断点

- 移动端: < 768px
- 平板: 768px - 1024px
- 桌面: > 1024px

## 🧪 测试检查清单

发布前请检查：

- [ ] 所有导航链接正常工作
- [ ] 代码复制功能正常
- [ ] 外部链接正确指向 GitHub
- [ ] 移动端显示正常
- [ ] 所有浏览器兼容（Chrome、Firefox、Safari）
- [ ] 无控制台错误

## 📄 许可证

与主项目相同，采用 MIT License。

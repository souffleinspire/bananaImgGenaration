# bananaImgGenaration

一个用于生成视觉故事卡片的工具，可以将长文本内容转化为精美的卡片式视觉故事。

## 项目特点

- 自动生成精美的视觉故事卡片
- 支持多种布局模板（覆盖布局、经典布局、倒置布局）
- 一键下载所有卡片为 ZIP 压缩包
- 支持两种部署方式：Base64 嵌入或外部图片引用

## 在线预览

访问 GitHub Pages 查看示例：
- [visual-story_base64.html](https://souffleinspire.github.io/bananaImgGenaration/visual-story_base64.html) - 单文件版本（包含所有图片）
- [visual-story.html](https://souffleinspire.github.io/bananaImgGenaration/visual-story.html) - 外部图片版本（加载更快）

## 本地使用

### 前置要求

- Python 3.7+
- 现代浏览器（Chrome、Firefox、Safari 等）

### 快速开始

1. 克隆仓库
```bash
git clone https://github.com/souffleinspire/bananaImgGenaration.git
cd bananaImgGenaration
```

2. 直接在浏览器中打开 HTML 文件
```bash
open visual-story.html
```

### 下载卡片

在浏览器中打开 HTML 文件后，点击页面顶部的"下载全部卡片 (Zip)"按钮，即可将所有卡片打包下载。

## 项目结构

```
bananaImgGenaration/
├── images/                    # 生成的图片目录
├── visual-story.html          # 外部图片引用版本（推荐）
├── visual-story_base64.html   # Base64 嵌入版本
├── visual-story.html.backup   # 备份文件
├── config.json                # 配置文件（请勿提交到公开仓库）
├── generate_images.py         # 图片生成脚本
├── update_html.py             # HTML 更新脚本
└── README.md                  # 项目说明
```

## 安全说明

⚠️ **重要提示**：
- `config.json` 包含敏感的 API 配置信息，请勿提交到公开仓库
- 建议将 `config.json` 添加到 `.gitignore` 文件
- 如果不小心提交了，请立即删除并重新生成 API Key

## 自定义内容

### 修改卡片内容

直接编辑 `visual-story.html` 或 `visual-story_base64.html` 文件中的 HTML 内容：

```html
<div class="card layout-c">
    <div class="illustration-area" style="background-image: url('images/your-image.png');"></div>
    <div class="info-area">
        <h1>你的标题</h1>
        <p>你的内容描述</p>
    </div>
</div>
```

### 布局模板

项目提供三种布局模板：

- **layout-a**: 经典布局（图上文下）
- **layout-b**: 倒置布局（文上图下）
- **layout-c**: 覆盖布局（图底文上，带渐变蒙层）

## 部署到 GitHub Pages

1. 将项目推送到 GitHub 仓库
2. 进入仓库的 Settings → Pages
3. Source 选择 `Deploy from a branch`
4. Branch 选择 `main` 分支，目录选择 `/ (root)`
5. 点击 Save，等待部署完成

## 技术栈

- HTML5 + CSS3
- JavaScript (ES6+)
- html2canvas - 将 DOM 转换为图片
- JSZip - 创建 ZIP 压缩包
- FileSaver.js - 文件下载

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

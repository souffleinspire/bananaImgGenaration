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

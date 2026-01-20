# 图片生成工具使用说明

## 前置要求

1. Python 3.7+
2. pip install requests

安装依赖：
```bash
pip install requests
```

## 配置步骤

### 1. 配置API Key

编辑 `config.json` 文件，填入您的API信息：

```json
{
    "api_key": "YOUR_API_KEY_HERE",
    "api_url": "YOUR_API_URL_HERE",
    "model": "gemini-2.5-flash-image-preview",
    "output_dir": "images"
}
```

### 2. API信息获取

根据您使用的API提供商，填写相应的信息：

#### 魔搭（ModelScope）API
- API URL: `https://api-inference.modelscope.cn/v1/images/generations`
- API Key: 从 https://modelscope.cn/ 获取

#### Google Cloud API
- API URL: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image-preview:generateImage`
- API Key: 从 Google Cloud Console 获取

#### 其他API提供商
请参考相应API文档填写正确的URL和认证方式。

## 使用方法

### 运行脚本

```bash
python3 generate_images.py
```

### 输出

脚本会在 `images` 目录下生成7张图片：
- card_00_*.png - 封面
- card_01_*.png - 卡片1
- card_02_*.png - 卡片2
- card_03_*.png - 卡片3
- card_04_*.png - 卡片4
- card_05_*.png - 卡片5
- card_06_*.png - 卡片6

同时会生成 `image_list.json` 文件，包含所有生成的图片路径。

## 更新HTML文件

生成图片后，运行以下命令更新HTML文件：

```bash
python3 update_html.py
```

这会自动将生成的图片路径插入到 `visual-story.html` 文件中。

## 故障排除

### 问题1: API调用失败
- 检查API key是否正确
- 检查API URL是否正确
- 检查网络连接

### 问题2: 权限错误
- 确保 `images` 目录有写入权限
- 使用 `chmod +x` 给脚本添加执行权限

### 问题3: 图片生成失败
- 检查提示词是否符合API要求
- 查看错误日志获取详细信息

## 自定义提示词

如需自定义图片提示词，编辑 `generate_images.py` 文件中的 `prompts` 列表。# bananaImgGenaration

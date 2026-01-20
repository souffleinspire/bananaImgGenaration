#!/usr/bin/env python3
"""
将图片转换为base64编码，内嵌到HTML中，解决跨域问题
"""

import base64
import json
import os

def image_to_base64(image_path):
    """
    将图片文件转换为base64编码
    
    Args:
        image_path: 图片文件路径
    
    Returns:
        base64编码的字符串
    """
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')

def update_html_with_base64(html_file="visual-story.html", image_list_file="image_list.json"):
    """
    更新HTML文件，将图片URL替换为base64编码
    
    Args:
        html_file: HTML文件路径
        image_list_file: 图片列表文件路径
    """
    # 读取图片列表
    if not os.path.exists(image_list_file):
        print(f"错误: 图片列表文件 {image_list_file} 不存在")
        return False
    
    with open(image_list_file, 'r', encoding='utf-8') as f:
        image_paths = json.load(f)
    
    # 读取HTML文件
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 备份原文件
    backup_file = html_file + ".backup"
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✓ 原文件已备份到: {backup_file}")
    
    # 将每个图片转换为base64并替换
    for i, image_path in enumerate(image_paths):
        print(f"\n正在处理图片 {i + 1}/{len(image_paths)}: {image_path}")
        
        if not os.path.exists(image_path):
            print(f"  警告: 图片文件不存在，跳过")
            continue
        
        # 转换为base64
        base64_data = image_to_base64(image_path)
        
        # 根据文件扩展名确定MIME类型
        ext = os.path.splitext(image_path)[1].lower()
        if ext == '.png':
            mime_type = 'image/png'
        elif ext in ['.jpg', '.jpeg']:
            mime_type = 'image/jpeg'
        elif ext == '.gif':
            mime_type = 'image/gif'
        elif ext == '.webp':
            mime_type = 'image/webp'
        else:
            mime_type = 'image/png'
        
        # 构建data URI
        data_uri = f"data:{mime_type};base64,{base64_data}"
        
        # 在HTML中查找并替换
        old_pattern = f"url('{image_path}')"
        new_pattern = f"url('{data_uri}')"
        
        if old_pattern in html_content:
            html_content = html_content.replace(old_pattern, new_pattern)
            print(f"  ✓ 已替换为base64编码")
        else:
            print(f"  警告: 在HTML中未找到该图片的引用")
    
    # 保存更新后的HTML
    output_file = html_file.replace('.html', '_base64.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✓ 更新完成！")
    print(f"✓ 新文件已保存: {output_file}")
    print(f"\n请在浏览器中打开 {output_file} 查看效果")
    
    return True


def main():
    """主函数"""
    print("=" * 60)
    print("将图片转换为base64编码并内嵌到HTML中")
    print("=" * 60)
    
    success = update_html_with_base64()
    
    if success:
        print("\n✓ 转换完成！")
        print(f"\n现在可以在浏览器中打开 visual-story_base64.html")
        print("点击'下载全部卡片'按钮应该可以正常工作了")
    else:
        print("\n✗ 转换失败，请检查错误信息")


if __name__ == "__main__":
    main()
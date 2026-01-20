#!/usr/bin/env python3
"""
更新HTML文件，将生成的图片路径插入到卡片中
"""

import json
import os
import re

def update_html(html_file="visual-story.html", image_list_file="image_list.json"):
    """
    更新HTML文件
    
    Args:
        html_file: HTML文件路径
        image_list_file: 图片列表文件路径
    """
    # 读取图片列表
    if not os.path.exists(image_list_file):
        print(f"错误: 图片列表文件 {image_list_file} 不存在")
        print("请先运行 python3 generate_images.py 生成图片")
        return False
    
    with open(image_list_file, 'r', encoding='utf-8') as f:
        image_paths = json.load(f)
    
    if len(image_paths) < 7:
        print(f"错误: 需要至少7张图片，当前只有 {len(image_paths)} 张")
        return False
    
    # 读取HTML文件
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 替换CSS背景为图片背景
    # 找到所有的 .illustration-area 元素并替换其背景
    
    # 封面卡片 (layout-c)
    for i in range(len(image_paths)):
        # 查找对应卡片的 illustration-area
        pattern = rf'(<div class="card layout-[abc]">\s*<div class="illustration-area pattern-\d+"></div>)'
        
        # 替换为使用图片
        replacement = rf'<div class="card layout-{["c", "a", "b", "a", "b", "a", "b"][i]}">\n        <div class="illustration-area" style="background-image: url(\'{image_paths[i]}\');"></div>'
        
        # 只替换第一个匹配项
        html_content = re.sub(pattern, replacement, html_content, count=1)
    
    # 保存更新后的HTML
    backup_file = html_file + ".backup"
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ 原文件已备份到: {backup_file}")
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ HTML文件已更新: {html_file}")
    print(f"✓ 已插入 {len(image_paths)} 张图片")
    
    return True


def main():
    """主函数"""
    print("=" * 60)
    print("更新HTML文件")
    print("=" * 60)
    
    success = update_html()
    
    if success:
        print("\n✓ 更新完成！")
        print(f"\n现在可以在浏览器中打开 visual-story.html 查看效果")
    else:
        print("\n✗ 更新失败，请检查错误信息")


if __name__ == "__main__":
    main()
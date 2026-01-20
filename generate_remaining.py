#!/usr/bin/env python3
"""
生成剩余的图片（只生成不存在的图片）
"""

import requests
import json
import os
from datetime import datetime
import time

class ImageGenerator:
    def __init__(self, config_file="config.json"):
        """
        初始化图片生成器
        
        Args:
            config_file: 配置文件路径
        """
        self.config = self.load_config(config_file)
        self.output_dir = self.config.get("output_dir", "images")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_config(self, config_file):
        """加载配置文件"""
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print(f"警告: 配置文件 {config_file} 不存在")
            return {
                "api_key": "",
                "api_url": "",
                "model": "gemini-2.5-flash-image-preview",
                "output_dir": "images"
            }
    
    def generate_image(self, prompt, filename_prefix="card", index=0):
        """
        生成图片
        
        Args:
            prompt: 图片生成提示词
            filename_prefix: 文件名前缀
            index: 卡片序号
        
        Returns:
            生成的图片文件路径，失败返回None
        """
        api_key = self.config.get("api_key", "")
        api_url = self.config.get("api_url", "")
        model = self.config.get("model", "gemini-2.5-flash-image-preview")
        
        if not api_key or not api_url:
            print("错误: API key或API URL未配置，请在config.json中配置")
            print(f"当前配置: {self.config}")
            return None
        
        # 生成文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{index:02d}_{timestamp}.png"
        output_path = os.path.join(self.output_dir, filename)
        
        print(f"\n正在生成图片 {index + 1}...")
        print(f"提示词: {prompt[:100]}...")
        
        # 构建请求
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "prompt": prompt,
            "model": model,
            "size": "1024x1024",
            "quality": "standard"
        }
        
        try:
            # 发送请求
            response = requests.post(api_url, headers=headers, json=data, timeout=60)
            
            print(f"状态码: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    result = response.json()
                except json.JSONDecodeError as e:
                    print(f"错误: 无法解析JSON响应: {e}")
                    print(f"完整响应内容: {response.text}")
                    return None
                
                # 根据API响应格式提取图片URL
                if "data" in result and len(result["data"]) > 0:
                    image_url = result["data"][0].get("url")
                    
                    if image_url:
                        # 下载图片
                        img_response = requests.get(image_url, timeout=30)
                        img_response.raise_for_status()
                        
                        # 保存图片
                        with open(output_path, 'wb') as f:
                            f.write(img_response.content)
                        
                        print(f"✓ 图片已保存: {output_path}")
                        return output_path
                    else:
                        print("错误: 响应中没有图片URL")
                        print(f"响应内容: {result}")
                        return None
                else:
                    print("错误: 响应格式不正确")
                    print(f"响应内容: {result}")
                    return None
            else:
                print(f"错误: API调用失败，状态码: {response.status_code}")
                print(f"响应内容: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"错误: 请求异常: {e}")
            return None
        except Exception as e:
            print(f"错误: 未知异常: {e}")
            return None
    
    def generate_remaining(self, prompts, filename_prefix="card"):
        """
        只生成剩余的图片（跳过已存在的）
        
        Args:
            prompts: 提示词列表
            filename_prefix: 文件名前缀
        
        Returns:
            生成的图片文件路径列表
        """
        results = []
        
        # 检查已存在的图片
        existing_indices = set()
        for filename in os.listdir(self.output_dir):
            if filename.startswith(filename_prefix + "_"):
                try:
                    index = int(filename.split("_")[1])
                    existing_indices.add(index)
                except (ValueError, IndexError):
                    pass
        
        print(f"已存在的图片索引: {sorted(existing_indices)}")
        
        for i, prompt in enumerate(prompts):
            if i in existing_indices:
                print(f"\n跳过图片 {i + 1}（已存在）")
                continue
            
            result = self.generate_image(prompt, filename_prefix, i)
            if result:
                results.append(result)
            
            # 避免请求过于频繁
            if i < len(prompts) - 1:
                time.sleep(1)
        
        return results


def main():
    """主函数"""
    generator = ImageGenerator()
    
    # 定义所有卡片的提示词
    prompts = [
        "封面: A powerful, thought-provoking illustration showing a concerned parent looking at a child, with AI neural networks and digital transformation elements in the background. The scene represents the challenge of raising children in the AI era. Modern, clean, illustrative style with warm lighting. Full-bleed image with no borders or frames.",
        
        "卡片1: A dramatic visual showing traditional university diplomas, professional symbols (stethoscope, calculator, gavel, code) dissolving into digital particles, with a glowing AI neural network emerging. Represents how AI is disrupting traditional professions. Modern infographic style, clean composition. Full-bleed image with no borders or frames.",
        
        "卡片2: A powerful visual metaphor: a crowd of identical gray silhouettes standing together, with one vibrant, colorful, unique figure standing apart and glowing with energy. The unique figure is surrounded by small icons representing diverse skills and experiences. Illustrates how uniqueness beats conformity in AI era. Modern, clean, illustrative style. Full-bleed image with no borders or frames.",
        
        "卡片3: A young artisan carefully crafting a detailed miniature house model with tiny furniture and decorations. The scene shows the craftsmanship and creativity of a micro-landscape designer creating personalized memory pieces. Warm lighting, detailed workbench with tools. Modern, clean, illustrative style. Full-bleed image with no borders or frames.",
        
        "卡片4: A diverse group of people from different professions (teacher, security guard, chef, engineer, artist) connecting with a child through glowing lines of communication. Shows how diverse human connections expand a child's world. Warm, inviting atmosphere. Modern, clean, illustrative style. Full-bleed image with no borders or frames.",
        
        "卡片5: Students in a modern workshop working on real-world projects, creating prototypes and products. Shows the journey from idea to market launch with flowchart elements and arrows. Represents 'entrepreneurship from day one' education. Dynamic, energetic scene. Modern, clean, illustrative style. Full-bleed image with no borders or frames.",
        
        "卡片6: A child holding a smartphone with a glowing rulebook and digital keys floating around. Shows establishing a relationship with technology through rules and boundaries. A balance between freedom and structure. Warm, educational atmosphere. Modern, clean, illustrative style. Full-bleed image with no borders or frames."
    ]
    
    print("=" * 60)
    print("只生成剩余的图片")
    print("=" * 60)
    
    results = generator.generate_remaining(prompts, filename_prefix="card")
    
    print("\n" + "=" * 60)
    print(f"生成完成！本次共生成 {len(results)} 张新图片")
    print("=" * 60)
    
    # 输出所有生成的图片路径
    print("\n本次生成的图片:")
    for i, path in enumerate(results, 1):
        print(f"{i}. {path}")
    
    # 更新图片列表文件
    all_images = []
    for i in range(len(prompts)):
        for filename in sorted(os.listdir(generator.output_dir)):
            if filename.startswith(f"card_{i:02d}_"):
                all_images.append(os.path.join(generator.output_dir, filename))
                break
    
    with open("image_list.json", 'w', encoding='utf-8') as f:
        json.dump(all_images, f, indent=2, ensure_ascii=False)
    
    print(f"\n图片列表已更新: image_list.json")
    print(f"总共有 {len(all_images)} 张图片")


if __name__ == "__main__":
    main()
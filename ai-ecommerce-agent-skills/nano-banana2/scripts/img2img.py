#!/usr/bin/env python3
"""Nano Banana2 图生图 - 基于参考图生成风格化版本"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

import requests

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyBn_AbjUeM4ZRcOOihp4Jdkt4sRdo--Kak")
GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta"
MODEL_IMAGE = "gemini-2.0-flash-exp-image-generation"

def encode_image(image_path):
    """将图片转为base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def call_gemini_image_to_image(image_path, prompt):
    """调用 Gemini 图生图 API"""
    url = f"{GEMINI_BASE}/models/{MODEL_IMAGE}:generateContent?key={GEMINI_API_KEY}"
    
    # 读取并编码图片
    image_b64 = encode_image(image_path)
    
    headers = {"Content-Type": "application/json"}
    
    # 构建多模态请求（图片 + 文本）
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "inlineData": {
                            "mimeType": "image/jpeg",
                            "data": image_b64
                        }
                    },
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"]
        }
    }
    
    resp = requests.post(url, headers=headers, json=payload, timeout=180)
    resp.raise_for_status()
    return resp.json()

def process_response(data, output_dir):
    """处理API响应，提取文本和图片"""
    results = []
    candidates = data.get("candidates", [])
    
    if not candidates:
        error = data.get("error", {})
        print(f"API Error: {error.get('message', 'Unknown error')}", file=sys.stderr)
        return results
    
    parts = candidates[0].get("content", {}).get("parts", [])
    
    os.makedirs(output_dir, exist_ok=True)
    image_count = 0
    
    for part in parts:
        if "text" in part:
            text = part["text"]
            if text.strip():
                print(f"AI描述: {text}")
                results.append({"type": "text", "text": text})
        
        elif "inlineData" in part:
            inline = part["inlineData"]
            mime_type = inline.get("mimeType", "image/png")
            b64_data = inline.get("data", "")
            
            if b64_data:
                ext = "png" if "png" in mime_type else "jpg"
                image_count += 1
                filename = f"nano_banana_img_{int(time.time())}_{image_count}.{ext}"
                filepath = os.path.join(output_dir, filename)
                
                with open(filepath, "wb") as f:
                    f.write(base64.b64decode(b64_data))
                
                print(f"✅ 图片已保存: {filepath}")
                results.append({"type": "image", "path": filepath, "mime": mime_type})
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Nano Banana2 图生图")
    parser.add_argument("--image", required=True, help="参考图片路径")
    parser.add_argument("--prompt", required=True, help="风格化提示词")
    parser.add_argument("--output", default="/tmp/nano_banana2_output/", help="输出目录")
    
    args = parser.parse_args()
    
    print(f"🎨 正在使用 Nano Banana 处理图片...")
    print(f"📸 参考图: {args.image}")
    print(f"💭 提示词: {args.prompt}")
    print("⏳ 生成中，请稍候...\n")
    
    try:
        data = call_gemini_image_to_image(args.image, args.prompt)
        results = process_response(data, args.output)
        
        # 保存结果摘要
        summary = {
            "status": "ok",
            "input_image": args.image,
            "prompt": args.prompt,
            "results": results
        }
        summary_path = os.path.join(args.output, "img2img_result.json")
        with open(summary_path, "w") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
            
        print(f"\n🎉 生成完成！结果保存在: {args.output}")
        
    except Exception as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

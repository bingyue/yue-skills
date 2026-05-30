#!/usr/bin/env python3
"""Nano Banana2 / Gemini multimodal API client for OpenClaw skill.

Uses Google Generative AI (Gemini) public API.
Supports text generation and image generation (Gemini 2.0 Flash).
"""

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
MODEL_TEXT = "gemini-2.5-flash"
MODEL_IMAGE = "gemini-2.5-flash-image"

VALID_RATIOS = [
    "21:9", "16:9", "4:3", "3:2",
    "1:1",
    "9:16", "3:4", "2:3",
    "5:4", "4:5",
]


def call_gemini(prompt, mode="text", image_path=None):
    """Call Gemini API via REST. Pass image_path for img2img reference."""
    model = MODEL_IMAGE if mode == "image" else MODEL_TEXT
    url = f"{GEMINI_BASE}/models/{model}:generateContent?key={GEMINI_API_KEY}"

    headers = {"Content-Type": "application/json"}

    parts = []
    if image_path:
        import mimetypes
        mime = mimetypes.guess_type(image_path)[0] or "image/jpeg"
        with open(image_path, "rb") as img_f:
            b64 = base64.b64encode(img_f.read()).decode()
        parts.append({"inlineData": {"mimeType": mime, "data": b64}})
    parts.append({"text": prompt})

    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {}
    }

    if mode == "image":
        payload["generationConfig"]["responseModalities"] = ["TEXT", "IMAGE"]

    resp = requests.post(url, headers=headers, json=payload, timeout=120)
    resp.raise_for_status()
    return resp.json()


def process_response(data, output_dir):
    """Process Gemini API response, extract text and save images."""
    results = []
    candidates = data.get("candidates", [])

    if not candidates:
        error = data.get("error", {})
        if error:
            print(f"API Error: {error.get('message', 'Unknown error')}", file=sys.stderr)
        else:
            print("No response from API.", file=sys.stderr)
        return results

    parts = candidates[0].get("content", {}).get("parts", [])

    os.makedirs(output_dir, exist_ok=True)
    image_count = 0

    for part in parts:
        if "text" in part:
            text = part["text"]
            if text.strip():
                print(text, end="")
                results.append({"type": "text", "text": text})

        elif "inlineData" in part:
            inline = part["inlineData"]
            mime_type = inline.get("mimeType", "image/png")
            b64_data = inline.get("data", "")

            if b64_data:
                ext = "png" if "png" in mime_type else "jpg"
                image_count += 1
                filename = f"gemini_{int(time.time())}_{image_count}.{ext}"
                filepath = os.path.join(output_dir, filename)

                with open(filepath, "wb") as f:
                    f.write(base64.b64decode(b64_data))

                print(f"\n[Image saved: {filepath}]")
                results.append({"type": "image", "path": filepath, "mime": mime_type})

    print()  # Final newline
    return results


def main():
    parser = argparse.ArgumentParser(description="Gemini Multimodal API Client")
    parser.add_argument("--mode", choices=["text", "image"], default="text",
                        help="Generation mode: text or image")
    parser.add_argument("--prompt", required=True, help="User prompt")
    parser.add_argument("--aspect-ratio", default="1:1",
                        help=f"Image aspect ratio (hint only). Options: {', '.join(VALID_RATIOS)}")
    parser.add_argument("--output", default="/root/.openclaw/media/nano_banana2_output/",
                        help="Output directory for generated images")
    parser.add_argument("--image", default=None, help="Input image path for img2img (reference image)")
    parser.add_argument("--system", default=None, help="Optional system prompt")
    parser.add_argument("--model", default=None, help="Override model name")

    args = parser.parse_args()

    # Build prompt
    full_prompt = args.prompt
    if args.mode == "image" and args.aspect_ratio != "1:1":
        full_prompt = f"{args.prompt} (aspect ratio: {args.aspect_ratio})"

    if args.model:
        global MODEL_TEXT, MODEL_IMAGE
        MODEL_TEXT = args.model
        MODEL_IMAGE = args.model

    try:
        data = call_gemini(full_prompt, mode=args.mode, image_path=args.image)
        results = process_response(data, args.output)

        # Write summary
        usage = data.get("usageMetadata", {})
        summary = {
            "status": "ok",
            "mode": args.mode,
            "model": MODEL_IMAGE if args.mode == "image" else MODEL_TEXT,
            "results": results,
            "usage": {
                "prompt_tokens": usage.get("promptTokenCount", 0),
                "completion_tokens": usage.get("candidatesTokenCount", 0),
                "total_tokens": usage.get("totalTokenCount", 0),
            },
        }
        summary_path = os.path.join(args.output, "last_result.json")
        os.makedirs(args.output, exist_ok=True)
        with open(summary_path, "w") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

    except requests.exceptions.HTTPError as e:
        body = ""
        if e.response is not None:
            body = e.response.text[:500]
        print(f"API Error: {e}\n{body}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

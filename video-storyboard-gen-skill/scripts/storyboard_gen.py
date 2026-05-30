#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
视频分镜脚本生成器
融合剧情结构与画面精细描述，生成完整的视频分镜脚本
"""

from __future__ import print_function
import argparse
import random

# ==================== 故事结构模板 ====================

STORY_STRUCTURES = {
    "戏剧式": {
        "name": "三幕式戏剧结构",
        "acts": [
            {"name": "建置", "ratio": 0.15, "purpose": "引入人物、场景、核心冲突"},
            {"name": "对抗", "ratio": 0.70, "purpose": "遭遇阻碍、尝试解决、冲突升级"},
            {"name": "解决", "ratio": 0.15, "purpose": "问题解决、情感升华"},
        ],
        "suitable_for": ["剧情片", "短片", "微电影"]
    },
    "广告式": {
        "name": "痛点-方案-效果结构",
        "acts": [
            {"name": "痛点", "ratio": 0.20, "purpose": "痛点刺激、建立共鸣"},
            {"name": "方案", "ratio": 0.30, "purpose": "产品登场、解决方案"},
            {"name": "效果", "ratio": 0.40, "purpose": "效果展示、变化呈现"},
            {"name": "号召", "ratio": 0.10, "purpose": "CTA、引导行动"},
        ],
        "suitable_for": ["广告片", "带货视频", "产品推广"]
    },
    "宣传式": {
        "name": "吸引-展示-号召结构",
        "acts": [
            {"name": "吸引", "ratio": 0.25, "purpose": "精彩开场、建立兴趣"},
            {"name": "展示", "ratio": 0.55, "purpose": "核心内容展示"},
            {"name": "号召", "ratio": 0.20, "purpose": "行动号召"},
        ],
        "suitable_for": ["宣传片", "品牌视频", "活动视频"]
    },
}

# ==================== 景别库 ====================

SHOT_SIZES = {
    "大远景": {"range": "环境+极小人物", "purpose": "展示环境全貌、交代地理位置"},
    "远景": {"range": "人物全身+环境", "purpose": "展示人物与环境关系、开场定位"},
    "全景": {"range": "人物全身", "purpose": "展示完整动作、人物形象"},
    "中景": {"range": "膝上/腰部以上", "purpose": "常用景别、人物交流、动作展示"},
    "近景": {"range": "胸部以上", "purpose": "表情细节、人物互动"},
    "特写": {"range": "面部/局部", "purpose": "强调细节、情感传递"},
    "大特写": {"range": "极局部", "purpose": "强调关键信息、视觉冲击"},
}

# ==================== 运镜方式库 ====================

CAMERA_MOVEMENTS = {
    "固定": {"effect": "稳定、客观、专注", "emotion": "平静"},
    "推镜头": {"effect": "强调、关注、压缩空间", "emotion": "紧张、期待"},
    "拉镜头": {"effect": "揭示、扩展、释放", "emotion": "释然、转折"},
    "摇镜头": {"effect": "观察、浏览、跟随视线", "emotion": "探索"},
    "移镜头": {"effect": "跟随、展示、流动", "emotion": "伴随"},
    "跟拍": {"effect": "伴随感、代入感", "emotion": "参与"},
    "环绕": {"effect": "展示全方位、立体感", "emotion": "强调"},
    "升降": {"effect": "视点变化、揭示信息", "emotion": "变化"},
    "手持": {"effect": "真实感、紧张感", "emotion": "临场"},
}

# ==================== 转场方式库 ====================

TRANSITIONS = {
    "硬切": {"effect": "干净利落", "suitable": "动作连续、节奏快"},
    "叠化": {"effect": "流畅柔和", "suitable": "时间流逝、情绪变化"},
    "淡入": {"effect": "开场感", "suitable": "视频/场景开始"},
    "淡出": {"effect": "结束感", "suitable": "视频/场景结束"},
    "白场": {"effect": "梦幻、回忆", "suitable": "时间跳跃、意识流"},
    "遮罩": {"effect": "自然流畅", "suitable": "人物移动场景"},
}

# ==================== 情绪-光线对照 ====================

EMOTION_LIGHTING = {
    "焦虑": {"色调": "冷色、灰蓝", "光质": "硬光或柔光", "光位": "侧光、逆光", "光比": "高对比"},
    "希望": {"色调": "淡黄、淡粉", "光质": "柔光", "光位": "侧逆光", "光比": "中对比"},
    "温暖": {"色调": "暖黄、金黄", "光质": "柔光、漫射", "光位": "顺光、侧光", "光比": "低对比"},
    "成功": {"色调": "暖色、明亮", "光质": "柔光", "光位": "顺光", "光比": "低对比"},
    "神秘": {"色调": "冷暖对比", "光质": "硬光、局部光", "光位": "逆光、侧光", "光比": "高对比"},
    "紧张": {"色调": "冷色偏蓝", "光质": "硬光", "光位": "侧光、底光", "光比": "高对比"},
}

# ==================== 情绪-音乐对照 ====================

EMOTION_MUSIC = {
    "焦虑": {"特点": "低沉、不和谐、重复", "乐器": "低音提琴、电子音"},
    "希望": {"特点": "明亮、上升、和谐", "乐器": "钢琴、弦乐"},
    "温暖": {"特点": "柔和、温暖、中速", "乐器": "吉他、钢琴"},
    "紧张": {"特点": "快速、尖锐、不和谐", "乐器": "打击乐、电子音"},
    "感动": {"特点": "柔美、上升、高潮", "乐器": "弦乐、钢琴"},
    "喜悦": {"特点": "明快、跳跃、节奏感", "乐器": "打击乐、管乐"},
}

# ==================== 生成函数 ====================

def generate_storyboard(title, video_type, duration, subject=None, platform="抖音"):
    """
    生成完整分镜脚本
    
    参数:
        title: 视频标题
        video_type: 视频类型（剧情/广告/宣传）
        duration: 时长（秒）
        subject: 主题描述（可选）
        platform: 目标平台
    """
    
    # 选择结构
    if video_type in ["广告", "带货"]:
        structure = STORY_STRUCTURES["广告式"]
    elif video_type in ["宣传", "品牌"]:
        structure = STORY_STRUCTURES["宣传式"]
    else:
        structure = STORY_STRUCTURES["戏剧式"]
    
    # 生成基本框架
    print("=" * 80)
    print(f"🎬 视频分镜脚本")
    print("=" * 80)
    print()
    
    # 项目信息
    print("## 项目信息")
    print()
    print("| 项目 | 内容 |")
    print("|------|------|")
    print(f"| **名称** | {title} |")
    print(f"| **类型** | {video_type}视频 |")
    print(f"| **时长** | {duration}秒 |")
    print(f"| **平台** | {platform} |")
    if subject:
        print(f"| **主题** | {subject} |")
    print()
    
    # 结构图
    print("## 故事结构")
    print()
    print(f"**{structure['name']}**")
    print()
    print("| 幕 | 时间占比 | 时长 | 核心任务 |")
    print("|------|---------|------|---------|")
    for act in structure["acts"]:
        act_duration = int(duration * act["ratio"])
        print(f"| {act['name']} | {int(act['ratio']*100)}% | {act_duration}秒 | {act['purpose']} |")
    print()
    
    # 分镜表
    print("## 分镜脚本")
    print()
    generate_shots(structure, duration)
    
    # 剪辑节奏
    print()
    print("## 剪辑节奏建议")
    print()
    print("```\n情绪强度变化曲线：开场 → 发展（节奏加快）→ 高潮 → 收尾（节奏回落）\n```")
    print()
    
    # 色调建议
    print("## 色调变化建议")
    print()
    print("| 阶段 | 色调 | 光线 | 后期调色 |")
    print("|------|------|------|---------|")
    
    stages = ["开场", "发展", "高潮", "收尾"]
    tones = [
        ("冷色偏蓝", "室内柔光、侧光", "降低饱和度，偏蓝"),
        ("淡黄渐入", "自然光、侧逆光", "暖色调渐入"),
        ("暖色金黄", "顺光、明亮", "饱和度提升，偏暖"),
        ("暖色稳定", "柔和顺光", "保持暖调，自然"),
    ]
    
    for i, stage in enumerate(stages):
        print(f"| {stage} | {tones[i][0]} | {tones[i][1]} | {tones[i][2]} |")
    print()
    
    # 音乐建议
    print("## 配乐情绪建议")
    print()
    print("| 阶段 | 音乐特点 | 建议乐器 |")
    print("|------|---------|---------|")
    
    music_stages = [
        ("开场/建置", "低沉平稳", "钢琴、弦乐"),
        ("发展", "渐进增强", "弦乐渐强"),
        ("高潮", "明快高潮", "弦乐+钢琴"),
        ("收尾", "渐弱收尾", "钢琴渐弱"),
    ]
    
    for stage, mood, inst in music_stages:
        print(f"| {stage} | {mood} | {inst} |")
    print()
    
    print("---")
    print(f"*脚本生成完成 | 总时长：{duration}秒 | 镜头数：参考生成*")


def generate_shots(structure, duration):
    """生成具体分镜"""
    
    print("| 镜号 | 时间 | 景别 | 画面描述 | 运镜 | 声音 | 转场 |")
    print("|------|------|------|----------|------|------|------|")
    
    shot_num = 1
    current_time = 0
    
    # 运镜选项
    movements = ["固定", "推镜头", "拉镜头", "摇镜头", "移镜头", "跟拍", "环绕"]
    transitions = ["硬切", "叠化", "硬切", "硬切", "遮罩"]  # 硬切最常用
    
    # 景别序列（按情绪递进）
    size_sequence = ["中景", "近景", "特写", "近景", "中景", "全景"]
    
    for act in structure["acts"]:
        act_duration = int(duration * act["ratio"])
        shot_count = max(2, act_duration // 8)  # 每幕至少2个镜头，平均每个8秒
        
        for i in range(shot_count):
            # 计算时间
            shot_duration = act_duration // shot_count
            end_time = current_time + shot_duration
            
            # 选择景别
            size_idx = min(i, len(size_sequence) - 1)
            shot_size = size_sequence[size_idx]
            
            # 选择运镜
            movement = movements[shot_num % len(movements)]
            
            # 选择转场
            transition = transitions[shot_num % len(transitions)]
            
            # 画面描述模板
            if act["name"] in ["建置", "痛点", "吸引"]:
                desc = f"【{act['name']}】人物出场，环境交代，建立情境。"
            elif act["name"] in ["对抗", "方案", "展示"]:
                desc = f"【{act['name']}】事件发展，动作推进，节奏加快。"
            else:
                desc = f"【{act['name']}】情感升华，问题解决，自然收尾。"
            
            # 声音模板
            if act["name"] in ["建置", "痛点", "吸引"]:
                sound = "旁白/环境音"
            elif act["name"] in ["对抗", "方案", "展示"]:
                sound = "台词+音乐进"
            else:
                sound = "台词/CTA"
            
            print(f"| {shot_num} | {current_time}-{end_time}s | {shot_size} | {desc} | {movement} | {sound} | {transition} |")
            
            shot_num += 1
            current_time = end_time


def print_reference():
    """打印参考信息"""
    
    print("=" * 80)
    print("📚 镜头语言参考")
    print("=" * 80)
    print()
    
    # 景别
    print("## 景别系统")
    print()
    print("| 景别 | 取景范围 | 功能作用 |")
    print("|------|---------|---------|")
    for name, info in SHOT_SIZES.items():
        print(f"| {name} | {info['range']} | {info['purpose']} |")
    print()
    
    # 运镜
    print("## 运镜方式")
    print()
    print("| 运镜 | 效果 | 情绪 |")
    print("|------|------|------|")
    for name, info in CAMERA_MOVEMENTS.items():
        print(f"| {name} | {info['effect']} | {info['emotion']} |")
    print()
    
    # 转场
    print("## 转场方式")
    print()
    print("| 转场 | 效果 | 适用场景 |")
    print("|------|------|---------|")
    for name, info in TRANSITIONS.items():
        print(f"| {name} | {info['effect']} | {info['suitable']} |")
    print()
    
    # 情绪-光线
    print("## 情绪-光线对照")
    print()
    print("| 情绪 | 色调 | 光质 | 光位 | 光比 |")
    print("|------|------|------|------|------|")
    for emotion, info in EMOTION_LIGHTING.items():
        print(f"| {emotion} | {info['色调']} | {info['光质']} | {info['光位']} | {info['光比']} |")
    print()


def main():
    parser = argparse.ArgumentParser(description="视频分镜脚本生成器")
    subparsers = parser.add_subparsers(dest="command")
    
    # generate 命令
    gen_parser = subparsers.add_parser("generate", help="生成分镜脚本")
    gen_parser.add_argument("title", help="视频标题")
    gen_parser.add_argument("--type", default="剧情", choices=["剧情", "广告", "宣传", "带货"], help="视频类型")
    gen_parser.add_argument("--duration", type=int, default=60, help="视频时长（秒）")
    gen_parser.add_argument("--subject", default=None, help="主题描述")
    gen_parser.add_argument("--platform", default="抖音", help="目标平台")
    
    # reference 命令
    ref_parser = subparsers.add_parser("reference", help="显示镜头语言参考")
    
    args = parser.parse_args()
    
    if args.command == "generate":
        generate_storyboard(args.title, args.type, args.duration, args.subject, args.platform)
    elif args.command == "reference":
        print_reference()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
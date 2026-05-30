#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音剧情带货脚本生成器（专业版）
融合优秀脚本创作方法论与影视美术设计
"""

from __future__ import print_function
import sys
import random
import argparse

# ==================== 剧情模板库 ====================

DRAMA_TEMPLATES = {
    "逆袭": {
        "name": "逆袭反转类",
        "keywords": ["逆袭", "翻身", "改变", "打脸", "重生"],
        "emotion_hook": "谁都不想被看不起",
        "structure": [
            ("困境建置", "主角遭遇困境/体检异常/被轻视", "焦虑", "室内偏暗", "冷色"),
            ("尝试失败", "试过很多方法都没用", "挫败", "室内", "灰暗"),
            ("转机出现", "得到推荐/发现产品", "好奇", "室内转户外", "淡黄"),
            ("坚持使用", "每天使用/慢慢变化", "期待", "日常场景", "暖黄"),
            ("效果爆发", "复查惊喜/变化显著", "爽", "明亮场景", "橙黄"),
            ("反转满足", "曾经质疑的人都来问", "满足", "户外阳光", "暖色"),
        ],
        "product_role": "产品是转运的关键道具",
    },
    "温情": {
        "name": "温情治愈类",
        "keywords": ["感动", "亲情", "爱情", "和解", "暖心"],
        "emotion_hook": "每个人都渴望被理解、被爱",
        "structure": [
            ("情感困境", "家庭/感情出现矛盾", "焦虑", "室内", "冷色"),
            ("内心独白", "主角的委屈无奈", "心疼", "特写", "暗调"),
            ("意外触发", "某个契机想到办法", "希望", "自然光", "淡暖"),
            ("产品出场", "用产品表达心意", "温暖", "明亮", "暖色"),
            ("化解误会", "矛盾改善/关系变化", "感动", "柔光", "暖黄"),
            ("温情收尾", "彼此理解/关系升温", "治愈", "阳光", "金黄"),
        ],
        "product_role": "产品是心意的载体",
    },
    "职场": {
        "name": "职场成长类",
        "keywords": ["升职", "加薪", "突破", "逆袭", "成长"],
        "emotion_hook": "谁不想升职加薪、被人高看？",
        "structure": [
            ("职场困境", "工作不顺/被批评", "焦虑", "办公室偏暗", "冷色"),
            ("内心挣扎", "怀疑自己/想放弃", "压抑", "特写", "暗调"),
            ("秘密武器", "发现产品/同事推荐", "好奇", "办公室", "中性"),
            ("悄悄改变", "使用产品/能力提升", "期待", "明亮", "暖色"),
            ("高光时刻", "业绩爆发/升职加薪", "爽", "明亮", "金黄"),
            ("人生感悟", "分享经验/帮助他人", "满足", "户外", "暖色"),
        ],
        "product_role": "产品是职场秘密武器",
    },
    "家庭": {
        "name": "家庭关系类",
        "keywords": ["婆媳", "夫妻", "亲子", "家庭", "和解"],
        "emotion_hook": "家家有本难念的经",
        "structure": [
            ("家庭矛盾", "婆媳/夫妻矛盾", "焦虑", "客厅", "冷色"),
            ("两难处境", "夹在中间", "压抑", "室内", "暗调"),
            ("意外转机", "发现产品可解决", "希望", "室内", "淡暖"),
            ("巧妙应用", "用产品化解尴尬", "期待", "明亮", "暖色"),
            ("关系改善", "对方态度改变", "温暖", "柔光", "暖黄"),
            ("家庭温馨", "全家和谐", "治愈", "阳光", "金黄"),
        ],
        "product_role": "产品是化解矛盾的工具",
    },
    "搞笑": {
        "name": "搞笑反差类",
        "keywords": ["搞笑", "反转", "夸张", "对比"],
        "emotion_hook": "快乐是最好的购买驱动力",
        "structure": [
            ("夸张困境", "夸张展示问题", "搞笑", "室内", "明亮"),
            ("尝试失败", "搞笑土办法", "爆笑", "室内", "明亮"),
            ("意外发现", "偶然发现产品", "好奇", "特写", "中性"),
            ("神奇效果", "效果立竿见影", "惊喜", "明亮", "暖色"),
            ("搞笑反转", "意想不到结果", "爆笑", "室内", "明亮"),
            ("欢乐收尾", "开心推荐", "愉悦", "阳光", "暖色"),
        ],
        "product_role": "产品是搞笑反转的关键道具",
    },
}

# 产品类型与剧情匹配
PRODUCT_DRAMA_MATCH = {
    "护肤品": "逆袭",
    "美妆": "逆袭",
    "保健品": "逆袭",
    "健康": "逆袭",
    "礼品": "温情",
    "母婴": "温情",
    "家居": "家庭",
    "家电": "家庭",
    "零食": "搞笑",
    "食品": "搞笑",
    "学习": "职场",
    "培训": "职场",
    "书籍": "职场",
    "办公": "职场",
}

# 开场钩子库
HOOK_TEMPLATES = [
    {"type": "痛点刺激", "template": "{时间}，{关键人物}看我的眼神越来越{负面情绪}...", "example": "结婚三年，他看我的眼神越来越冷淡..."},
    {"type": "痛点刺激", "template": "{事件}出来那天，我整个人都懵了...", "example": "体检报告出来那天，我整个人都懵了..."},
    {"type": "痛点刺激", "template": "做了{n}年{职业}，我都快{负面状态}了...", "example": "做了十年打工人，我都快怀疑人生了..."},
    {"type": "悬念制造", "template": "邻居说我{产品}像{负面评价}，结果{反转}...", "example": "邻居说我这茶像发霉了，结果她现在天天问我要..."},
    {"type": "悬念制造", "template": "用了{n}天，医生都问我做了什么...", "example": "用了三个月，医生都问我做了什么..."},
    {"type": "反常识", "template": "我以为这辈子就这样了，直到...", "example": "我以为这辈子就这样了，直到那天..."},
    {"type": "数字冲击", "template": "{指标}从{数字1}到{数字2}，我只用了{方法}...", "example": "血压从165到正常，我只用了这一招..."},
]

# 软性CTA话术库
SOFT_CTA_TEMPLATES = [
    {"type": "分享型", "template": "如果你也遇到同样的问题，评论区告诉我，我分享给你..."},
    {"type": "隐晦型", "template": "不是广告，纯分享，效果太明显了藏不住..."},
    {"type": "对比型", "template": "用了{n}天才发现，原来之前的努力都白费了..."},
    {"type": "故事型", "template": "我把老家的链接放评论区了，需要的自取..."},
    {"type": "求助型", "template": "有姐妹知道怎么买吗？我帮你们问问..."},
]

# 角色模板库
CHARACTER_TEMPLATES = {
    "女主": {
        "age_range": "25-60岁",
        "traits": ["外表坚强内心柔软", "不愿给家人添麻烦", "隐忍但有底线"],
        "habits": ["紧张时抿嘴唇", "开心时眼睛会笑", "思考时微微皱眉"],
        "styles": ["朴素干净", "略带疲惫（困境时）", "精神焕发（成功时）"],
    },
    "男主": {
        "age_range": "28-65岁",
        "traits": ["外冷内热", "话不多但行动力强", "责任感强"],
        "habits": ["思考时微微皱眉", "重视的人面前放松", "生气时沉默"],
        "styles": ["成熟稳重", "有故事感", "气质干净"],
    },
    "闺蜜/邻居": {
        "age_range": "25-70岁",
        "traits": ["热心肠", "爱分享", "直爽真诚"],
        "habits": ["说话直接", "爱给建议", "笑点低"],
        "styles": ["打扮得体", "精神饱满", "亲和力强"],
    },
}


def generate_full_script(product, product_type, drama_type=None, duration=90):
    """生成完整脚本（专业版）"""
    
    # 自动匹配剧情类型
    if drama_type is None:
        for key, match in PRODUCT_DRAMA_MATCH.items():
            if key in product_type or product_type in key:
                drama_type = match
                break
        if drama_type is None:
            drama_type = "逆袭"
    
    # 模糊匹配
    matched = None
    for key in DRAMA_TEMPLATES:
        if key in drama_type or drama_type in key:
            matched = key
            break
    if matched is None:
        matched = "逆袭"
    
    template = DRAMA_TEMPLATES[matched]
    structure = template["structure"]
    
    # 计算时间分配
    time_per_stage = duration // len(structure)
    
    # ==================== 输出脚本 ====================
    
    print("=" * 70)
    print(f"🎬 剧情带货脚本（专业版）")
    print(f"   产品：{product} | 类型：{template['name']} | 时长：{duration}秒")
    print("=" * 70)
    print()
    
    # 一、基本信息卡片
    print("## 一、基本信息卡片")
    print()
    print("| 项目 | 内容 |")
    print("|------|------|")
    print(f"| **产品** | {product} |")
    print(f"| **产品类型** | {product_type} |")
    print(f"| **剧情类型** | {template['name']} |")
    print(f"| **情感钩子** | {template['emotion_hook']} |")
    print(f"| **产品角色** | {template['product_role']} |")
    print(f"| **视频时长** | {duration}秒 |")
    print()
    
    # 二、三幕式结构
    print("## 二、三幕式结构")
    print()
    
    # 找到结构分割点
    act1_end = max(1, len(structure) // 6)  # 第一幕约15%
    act2_end = len(structure) - 1  # 第二幕到倒数第二
    
    print("```")
    print("【第一幕：建置】0-15%")
    for i, (stage, desc, emotion, scene, color) in enumerate(structure[:act1_end]):
        print(f"  第{i+1}阶段：{stage} — {desc} 【{emotion}】")
    print()
    print("【第二幕：对抗】15-85%")
    for i, (stage, desc, emotion, scene, color) in enumerate(structure[act1_end:act2_end], act1_end):
        print(f"  第{i+1}阶段：{stage} — {desc} 【{emotion}】")
    print()
    print("【第三幕：解决】85-100%")
    for i, (stage, desc, emotion, scene, color) in enumerate(structure[act2_end:], act2_end):
        print(f"  第{i+1}阶段：{stage} — {desc} 【{emotion}】")
    print("```")
    print()
    
    # 三、完整分镜脚本
    print("## 三、完整分镜脚本")
    print()
    print("| 镜头 | 时间 | 画面内容 | 台词/旁白 | 美术设计 | 情绪 |")
    print("|------|------|----------|-----------|----------|------|")
    
    hook_used = random.choice([h for h in HOOK_TEMPLATES if h["type"] == "痛点刺激"])
    cta_used = random.choice(SOFT_CTA_TEMPLATES)
    
    for i, (stage, desc, emotion, scene, color) in enumerate(structure):
        start = i * time_per_stage
        end = (i + 1) * time_per_stage
        
        # 台词
        if i == 0:
            台词 = f"「{hook_used['example']}」"
        elif "转机" in stage or "产品" in stage or "发现" in stage:
            台词 = f"「这就是{product}...（产品自然露出）」"
        elif i == len(structure) - 1:
            台词 = f"「{cta_used['template']}」"
        else:
            台词 = f"「（{stage}内容...）」"
        
        # 美术设计
        美术 = f"场景:{scene} | 色调:{color}"
        
        print(f"| {i+1} | {start}-{end}s | 【{stage}】{desc} | {台词} | {美术} | 【{emotion}】 |")
    
    print()
    
    # 四、口播稿
    print("## 四、口播稿（带标注）")
    print()
    print("```")
    
    for i, (stage, desc, emotion, scene, color) in enumerate(structure):
        start = i * time_per_stage
        end = (i + 1) * time_per_stage
        
        print(f"【{stage} {start}-{end}s】（情绪：{emotion}）")
        print(f"（场景：{scene} | 色调：{color}）")
        
        if i == 0:
            print(f"（停顿0.5秒）")
            print(f"{hook_used['example']}")
        elif "转机" in stage or "产品" in stage:
            print(f"（产品自然露出）")
            print(f"「这就是{product}，邻居老姐妹说...」")
        elif i == len(structure) - 1:
            print(f"（真诚、自然的语气）")
            print(f"{cta_used['template']}")
        else:
            print(f"「（{stage}的台词内容...）」")
        
        print()
    
    print("```")
    print()
    
    # 五、美术设计指导
    print("## 五、美术设计指导")
    print()
    print("### 场景与氛围")
    print()
    print("| 阶段 | 场景 | 光线 | 色调 | 服装 |")
    print("|------|------|------|------|------|")
    
    for stage, desc, emotion, scene, color in structure:
        if "困境" in stage or "失败" in stage or "矛盾" in stage:
            costume = "略显疲惫"
            light = "侧光/逆光"
        elif "转机" in stage or "发现" in stage:
            costume = "日常"
            light = "自然光"
        else:
            costume = "精神、整洁"
            light = "明亮顺光"
        
        print(f"| {stage} | {scene} | {light} | {color} | {costume} |")
    
    print()
    print("### 道具设计")
    print()
    print(f"- **核心道具**：{product}（叙事功能+塑造人物）")
    print("- **辅助道具**：根据剧情需要（体检报告/药盒/茶杯等）")
    print("- **道具展示**：产品需在合适光线和角度下露出")
    print()
    
    # 六、标题与封面
    print("## 六、标题与封面建议")
    print()
    print("### 爆款标题")
    print()
    
    titles = [
        f"「{hook_used['example'][:20]}...」",
        f"「用了{n}个月，医生都问我做了什么...」" if (n := random.randint(1, 6)) else "",
        f"「邻居说我这茶像发霉，结果她现在天天问我要...」",
        f"「{product}真的有用吗？我亲测了{random.randint(30,90)}天...」",
    ]
    
    for i, title in enumerate(titles[:3], 1):
        print(f"{i}. {title}")
    
    print()
    print("### 封面文案")
    print()
    print("| 主文案 | 副文案 |")
    print("|--------|--------|")
    print(f"| {hook_used['example'][:15]}... | 坚持了{random.randint(30,90)}天 |")
    print()
    
    # 七、质量检查清单
    print("## 七、质量检查清单")
    print()
    print("### 故事层面")
    print("- [ ] 开场前3秒有强钩子吗？")
    print("- [ ] 冲突是否贯穿始终？")
    print("- [ ] 每15秒有小悬念/小反转吗？")
    print("- [ ] 情感共鸣点清晰吗？")
    print()
    print("### 美术层面")
    print("- [ ] 场景氛围与情绪匹配吗？")
    print("- [ ] 光影变化配合剧情节奏吗？")
    print("- [ ] 产品展示光线和角度合适吗？")
    print()
    print("### 带货层面")
    print("- [ ] 产品植入时机自然吗？")
    print("- [ ] CTA是否软性不生硬？")
    print("- [ ] 是否符合广告法合规？")
    print()
    
    print("---")
    print(f"*脚本生成完成 | 产品：{product} | 类型：{template['name']}*")


def generate_character(char_type):
    """生成角色人设"""
    
    matched = None
    for key in CHARACTER_TEMPLATES:
        if key in char_type or char_type in key:
            matched = key
            break
    
    if matched is None:
        print(f"可用角色类型：{', '.join(CHARACTER_TEMPLATES.keys())}")
        return
    
    template = CHARACTER_TEMPLATES[matched]
    
    print("=" * 60)
    print(f"👤 角色人设 | 类型：{matched}")
    print("=" * 60)
    print()
    
    print("## 基本信息")
    print()
    print(f"- **年龄范围：** {template['age_range']}")
    print(f"- **性格特质：** {' / '.join(template['traits'])}")
    print()
    
    print("## 外形设计")
    print()
    print("**服装风格：**")
    for s in template['styles']:
        print(f"- {s}")
    print()
    
    print("## 行为习惯")
    print()
    for h in template['habits']:
        print(f"- {h}")
    print()
    
    print("## 情绪状态对照")
    print()
    print("| 状态 | 外形 | 表情 | 动作 |")
    print("|------|------|------|------|")
    print("| 困境 | 略显疲惫、朴素 | 眉头微皱、眼神疲惫 | 抿嘴、叹气 |")
    print("| 转机 | 日常、干净 | 眼神微亮、好奇 | 倾听、点头 |")
    print("| 成功 | 精神、整洁 | 眼睛有光、微笑 | 自信、放松 |")
    print()


def main():
    parser = argparse.ArgumentParser(description="抖音剧情带货脚本生成器（专业版）")
    subparsers = parser.add_subparsers(dest="command")
    
    # script 命令
    script_parser = subparsers.add_parser("script", help="生成完整脚本")
    script_parser.add_argument("product", help="产品名称")
    script_parser.add_argument("--type", default="保健品", help="产品类型")
    script_parser.add_argument("--drama", default=None, help="剧情类型（逆袭/温情/职场/家庭/搞笑）")
    script_parser.add_argument("--duration", type=int, default=90, help="视频时长（秒）")
    
    # character 命令
    char_parser = subparsers.add_parser("character", help="生成角色人设")
    char_parser.add_argument("type", help="角色类型（女主/男主/闺蜜/邻居）")
    
    args = parser.parse_args()
    
    if args.command == "script":
        generate_full_script(args.product, args.type, args.drama, args.duration)
    elif args.command == "character":
        generate_character(args.type)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
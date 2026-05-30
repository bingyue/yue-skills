---
name: pitfall-experience
description: "踩坑经验库 - 遇到问题时自动查阅 GitHub 上的历史踩坑记录(Capsule)，解决后自动提交新经验回 GitHub Issue。激活条件：(1) 遇到报错/异常/失败时 (2) 配置不生效或行为异常时 (3) 成功解决一个非显而易见的问题后 (4) 用户要求查阅或记录经验时。关键词：踩坑、经验、报错、failed、error、不生效、为什么、pitfall、experience"
metadata:
  openclaw:
    version: 1.0.0
    userInvocable: true
    emoji: "📝"
  requires:
    bins: ["curl", "python3"]
---

# 踩坑经验库 (Pitfall Experience)

遇到问题时查阅 GitHub 上的历史经验，解决问题后将新经验提交回去。

## 核心规则

1. **遇到任何报错或异常时**，先查阅经验库再尝试修复
2. **成功解决非显而易见的问题后**，必须提交新 Capsule 回 GitHub
3. 所有操作通过 GitHub API 完成，不需要 git clone

## 经验仓库

- **GitHub**: https://github.com/BENZEMA216/openclaw-pitfalls
- **Capsule 目录**: capsules/ (YAML 格式)
- **API Token**: 存储在 /root/.openclaw-claw2/credentials/github_token

## 工作流

### Phase 1: 查阅经验（遇到问题时）

当遭遇错误/异常/配置不生效时，立即执行：

**步骤 1 — 获取 Capsule 索引**

```bash
curl -s https://api.github.com/repos/BENZEMA216/openclaw-pitfalls/contents/capsules | python3 -c "import sys,json; [print(f['name'], f['download_url']) for f in sorted(json.load(sys.stdin), key=lambda x: x['name'])]"
```

**步骤 2 — 读取相关 Capsule**

```bash
curl -s https://raw.githubusercontent.com/BENZEMA216/openclaw-pitfalls/main/capsules/PIT-XXX.yaml
```

**步骤 3 — 批量搜索关键词**

```bash
GITHUB_TOKEN=$(cat /root/.openclaw-claw2/credentials/github_token)
curl -s -H "Authorization: token $GITHUB_TOKEN" "https://api.github.com/search/code?q=关键词+repo:BENZEMA216/openclaw-pitfalls+path:capsules"
```

**步骤 4 — 读取 README 索引表**

```bash
curl -s https://raw.githubusercontent.com/BENZEMA216/openclaw-pitfalls/main/README.md
```

### Phase 2: 应用经验

1. 读取 Capsule 的 correct_process 字段
2. **严格按照 correct_process 的步骤执行**，不要自行发挥
3. 执行完后验证修复结果

### Phase 3: 提交新经验（成功解决问题后）

当成功解决了一个非显而易见的问题后，**必须**将经验提交回 GitHub。

**步骤 1 — 确定新 Capsule 编号**

```bash
LAST_ID=$(curl -s https://api.github.com/repos/BENZEMA216/openclaw-pitfalls/contents/capsules | python3 -c "import sys,json; files=json.load(sys.stdin); ids=[int(f['name'].replace('PIT-','').replace('.yaml','')) for f in files if f['name'].startswith('PIT-')]; print(max(ids) if ids else 0)")
NEW_ID=$((LAST_ID + 1))
NEW_PIT=$(printf 'PIT-%03d' $NEW_ID)
echo "New capsule: $NEW_PIT"
```

**步骤 2 — 用 Python 脚本提交 Issue**

```bash
python3 /root/.openclaw-claw2/skills/pitfall-experience/scripts/submit_capsule.py \
  --id "$NEW_PIT" \
  --title "简短问题描述" \
  --severity "high" \
  --category "config" \
  --yaml-file /tmp/capsule.yaml
```

## Capsule YAML 格式

```yaml
id: PIT-XXX
trigger_time: "YYYY-MM-DD HH:MM"
category: repair | config | env
severity: critical | high | medium | low

problem:
  signal: "具体的错误信号/日志"
  description: "问题的本质是什么"
  env_fingerprint:
    platform: linux
    openclaw: "2026.2.9"
    profile: "claw2"

error_process:
  - step: "做了什么"
    result: "得到了什么错误结果"

correct_process:
  - step: "应该怎么做"
    detail: "具体操作"
  - step: "验证"
    detail: "如何确认修复成功"

root_cause: "根因分析"
confidence: 0.9
blast_radius:
  files: ["affected_files"]
  scope: "影响范围"
```

## 判断标准

提交新经验:
- 配置修改后重启不生效，发现需要额外步骤
- 命令报错但错误信息有误导性
- 文档没提到的隐含依赖或前置条件
- 不同环境/profile 下行为不一致

不需要提交:
- 简单拼写错误
- 文档已明确说明的已知限制

## 严重度判断

| 级别 | 标准 |
|------|------|
| critical | 服务完全不可用，或数据丢失风险 |
| high | 核心功能受损但有 workaround |
| medium | 非核心功能受影响，或需要较多时间排查 |
| low | 体验问题，不影响核心功能 |

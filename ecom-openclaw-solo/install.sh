#!/usr/bin/env bash
# =============================================================================
# openclaw-one-person-company-skill — install.sh
# 安装脚本：自动检测 OpenClaw 根目录并完成 18 人 AI 公司完整安装
# =============================================================================

set -euo pipefail

# ── 颜色定义 ──────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

info()    { echo -e "${BLUE}[INFO]${RESET}  $*"; }
success() { echo -e "${GREEN}[OK]${RESET}    $*"; }
warn()    { echo -e "${YELLOW}[WARN]${RESET}  $*"; }
error()   { echo -e "${RED}[ERROR]${RESET} $*" >&2; exit 1; }
step()    { echo -e "\n${CYAN}${BOLD}▶ $*${RESET}"; }

# ── 脚本所在目录（Skill 根目录）──────────────────────────────────────────────
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="openclaw-one-person-company"
SKILL_VERSION="2.0.0"

# 全部 18 个 Agent ID（按组织架构顺序）
AGENT_IDS=(
  # 总办
  "ceo"
  # 产品增长中心
  "product_lead" "user_researcher" "data_analyst" "feature_planner" "ux_optimizer"
  # 技术平台中心
  "tech_lead" "architect" "backend_dev" "frontend_dev" "qa_engineer" "devops_engineer"
  # 营销增长中心
  "growth_lead" "content_planner" "seo_specialist" "ads_optimizer" "user_operator" "crm_analyst"
)

# 旧版需要清理的 Agent ID（从 v1.0.0 迁移）
LEGACY_AGENT_IDS=("ceo" "product" "tech" "growth")

echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${BOLD}║   OpenClaw One Person Company Skill — Installer v${SKILL_VERSION}      ║${RESET}"
echo -e "${BOLD}║   18 人 AI 公司：总办 + 产品增长 + 技术平台 + 营销增长       ║${RESET}"
echo -e "${BOLD}╚══════════════════════════════════════════════════════════════╝${RESET}"
echo ""

# ── Step 1: 检测 jq 依赖 ───────────────────────────────────────────────────
step "Step 1/10 — 检查依赖项"
if ! command -v jq &>/dev/null; then
  warn "未检测到 jq，尝试自动安装..."
  if command -v brew &>/dev/null; then
    brew install jq
  elif command -v apt-get &>/dev/null; then
    sudo apt-get install -y jq
  elif command -v yum &>/dev/null; then
    sudo yum install -y jq
  else
    error "无法自动安装 jq，请手动安装：https://stedolan.github.io/jq/download/"
  fi
fi
success "jq 已就绪：$(jq --version)"

# ── Step 2: 自动检测 OpenClaw 根目录 ──────────────────────────────────────
step "Step 2/10 — 检测 OpenClaw 根目录"

detect_openclaw_root() {
  local search_paths=(
    "$HOME/.openclaw"
    "$HOME/.claude"
    "$(pwd)"
    "$(pwd)/.."
    "$(pwd)/../.."
    "$HOME/Documents/openclaw"
    "$HOME/openclaw"
    "/usr/local/openclaw"
  )
  for p in "${search_paths[@]}"; do
    p="$(realpath "$p" 2>/dev/null || echo "$p")"
    if [[ -f "$p/openclaw.json" ]]; then echo "$p"; return 0; fi
    if [[ -d "$p/claude" ]] || [[ -d "$p/skills" ]]; then echo "$p"; return 0; fi
  done
  return 1
}

if [[ -n "${OPENCLAW_ROOT:-}" ]]; then
  info "使用环境变量 OPENCLAW_ROOT: $OPENCLAW_ROOT"
  OC_ROOT="$OPENCLAW_ROOT"
elif OC_ROOT="$(detect_openclaw_root)"; then
  info "自动检测到 OpenClaw 根目录: $OC_ROOT"
else
  warn "无法自动检测 OpenClaw 根目录"
  read -rp "请手动输入 OpenClaw 根目录路径（回车使用当前目录）: " user_input
  OC_ROOT="${user_input:-$(pwd)}"
fi

mkdir -p "$OC_ROOT"
success "OpenClaw 根目录: $OC_ROOT"

# ── Step 3: 检测/创建 openclaw.json ────────────────────────────────────────
step "Step 3/10 — 检查 openclaw.json"
OC_JSON="$OC_ROOT/openclaw.json"

if [[ ! -f "$OC_JSON" ]]; then
  warn "openclaw.json 不存在，创建初始配置..."
  cat > "$OC_JSON" <<'INIT_JSON'
{
  "version": "1.0.0",
  "skills": [],
  "agents": [],
  "config": {
    "agentToAgent": {
      "enabled": false,
      "allowCrossAgent": false,
      "logCommunication": false
    },
    "maxRecursion": 1,
    "memory": { "enabled": false }
  }
}
INIT_JSON
  success "已创建 openclaw.json"
else
  success "openclaw.json 已存在"
fi

BACKUP_PATH="${OC_JSON}.backup.$(date +%Y%m%d_%H%M%S)"
cp "$OC_JSON" "$BACKUP_PATH"
info "已备份 openclaw.json → $BACKUP_PATH"

# ── Step 4: 清理旧版 Agent（v1.0.0 遗留）─────────────────────────────────
step "Step 4/10 — 清理旧版 Agent（如有）"
LEGACY_IDS_JSON='["ceo","product","tech","growth"]'
LEGACY_COUNT=$(jq --argjson ids "$LEGACY_IDS_JSON" \
  '[.agents[]? | select(.id as $id | $ids | index($id) != null)] | length' \
  "$OC_JSON")

if [[ "$LEGACY_COUNT" -gt 0 ]]; then
  warn "检测到旧版 v1.0.0 的 ${LEGACY_COUNT} 个 Agent，自动清理..."
  UPDATED_JSON="$(jq --argjson ids "$LEGACY_IDS_JSON" \
    '.agents = [.agents[]? | select(.id as $id | $ids | index($id) == null)]' \
    "$OC_JSON")"
  echo "$UPDATED_JSON" > "$OC_JSON"
  success "旧版 Agent 已清理"
else
  info "未发现旧版 Agent，跳过清理"
fi

# ── Step 5: 拷贝 souls 目录 ─────────────────────────────────────────────────
step "Step 5/10 — 安装 Soul 文件（共 ${#AGENT_IDS[@]} 个）"
SOULS_SRC="$SKILL_DIR/souls"
SOULS_DST="$OC_ROOT/souls"
mkdir -p "$SOULS_DST"

SOUL_INSTALLED=0
for agent_id in "${AGENT_IDS[@]}"; do
  src="$SOULS_SRC/${agent_id}.md"
  dst="$SOULS_DST/${agent_id}.md"
  if [[ -f "$src" ]]; then
    cp "$src" "$dst"
    success "Soul 已安装: ${agent_id}.md"
    SOUL_INSTALLED=$((SOUL_INSTALLED + 1))
  else
    warn "Soul 文件缺失: $src（跳过）"
  fi
done
success "共安装 ${SOUL_INSTALLED}/${#AGENT_IDS[@]} 个 Soul 文件 → $SOULS_DST"

# ── Step 6: 合并 agents.json 到 openclaw.json ──────────────────────────────
step "Step 6/10 — 合并 18 个 Agent 到 openclaw.json"
AGENTS_SRC="$SKILL_DIR/agents.json"

if [[ ! -f "$AGENTS_SRC" ]]; then
  error "agents.json 文件不存在: $AGENTS_SRC"
fi

NEW_AGENTS="$(jq '.agents' "$AGENTS_SRC")"

# 将 soul 路径更新为绝对路径
NEW_AGENTS_ABS="$(echo "$NEW_AGENTS" | jq --arg souls_dir "$SOULS_DST" '
  map(.soul = ($souls_dir + "/" + (.id) + ".md"))
')"

# 合并：移除已有同 id 的 Agent，追加新 Agent
ALL_NEW_IDS="$(echo "$NEW_AGENTS_ABS" | jq '[.[].id]')"
UPDATED_JSON="$(jq \
  --argjson new_agents "$NEW_AGENTS_ABS" \
  --argjson new_ids "$ALL_NEW_IDS" \
  '.agents = ((.agents // []) | map(select(.id as $id | $new_ids | index($id) | not))) + $new_agents' \
  "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "已合并 ${#AGENT_IDS[@]} 个 Agent 到 openclaw.json"

# ── Step 7: 开启 agentToAgent ─────────────────────────────────────────────
step "Step 7/10 — 启用 agentToAgent 通信"
UPDATED_JSON="$(jq '
  .config.agentToAgent.enabled = true |
  .config.agentToAgent.allowCrossAgent = true |
  .config.agentToAgent.logCommunication = true
' "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "agentToAgent 已启用（跨中心通信 + 通信日志）"

# ── Step 8: 设置 maxRecursion = 3 ────────────────────────────────────────
step "Step 8/10 — 设置 maxRecursion = 3"
UPDATED_JSON="$(jq '.config.maxRecursion = 3' "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "maxRecursion 已设置为 3（CEO → 中心负责人 → 执行角色）"

# ── Step 9: 启用 memory ────────────────────────────────────────────────────
step "Step 9/10 — 启用 Memory 系统"
UPDATED_JSON="$(jq '.config.memory.enabled = true' "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "Memory 系统已启用"

# ── Step 10: 注册 Skill ──────────────────────────────────────────────────────
step "Step 10/10 — 注册 Skill"
SKILL_ENTRY="{
  \"name\": \"$SKILL_NAME\",
  \"version\": \"$SKILL_VERSION\",
  \"path\": \"$SKILL_DIR\",
  \"agentCount\": ${#AGENT_IDS[@]},
  \"installedAt\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"
}"
UPDATED_JSON="$(jq \
  --argjson skill_entry "$SKILL_ENTRY" \
  '.skills = ((.skills // []) | map(select(.name != $skill_entry.name))) + [$skill_entry]' \
  "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "Skill '$SKILL_NAME@$SKILL_VERSION' 已注册"

# ── 最终验证 ──────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}────────────────────── 安装验证 ──────────────────────────────${RESET}"
echo ""
echo -e "${BOLD}【总办】${RESET}"
jq -r '.agents[] | select(.center == "总办") | "  \(.id) — \(.name) | KPI: \(.kpi)"' "$OC_JSON"
echo ""
echo -e "${BOLD}【产品增长中心】${RESET}"
jq -r '.agents[] | select(.center == "产品增长中心") | "  \(.id) — \(.name) | \(.role) | KPI: \(.kpi)"' "$OC_JSON"
echo ""
echo -e "${BOLD}【技术平台中心】${RESET}"
jq -r '.agents[] | select(.center == "技术平台中心") | "  \(.id) — \(.name) | \(.role) | KPI: \(.kpi)"' "$OC_JSON"
echo ""
echo -e "${BOLD}【营销增长中心】${RESET}"
jq -r '.agents[] | select(.center == "营销增长中心") | "  \(.id) — \(.name) | \(.role) | KPI: \(.kpi)"' "$OC_JSON"
echo ""
AGENT_COUNT=$(jq '.agents | length' "$OC_JSON")
echo -e "  总计已注册 Agent 数：${GREEN}${BOLD}${AGENT_COUNT}${RESET}"
echo ""

# ── 完成提示 ──────────────────────────────────────────────────────────────
echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}${BOLD}║     ✅ 安装成功！18 人 AI 公司 Skill 已就绪                  ║${RESET}"
echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════════════╝${RESET}"
echo ""
echo -e "  ${BOLD}Skill:${RESET}      $SKILL_NAME v$SKILL_VERSION"
echo -e "  ${BOLD}安装目录:${RESET}  $OC_ROOT"
echo -e "  ${BOLD}配置文件:${RESET}  $OC_JSON"
echo -e "  ${BOLD}Soul 目录:${RESET} $SOULS_DST"
echo -e "  ${BOLD}备份文件:${RESET}  $BACKUP_PATH"
echo ""
echo -e "  ${YELLOW}如需卸载，运行：./uninstall.sh${RESET}"
echo ""

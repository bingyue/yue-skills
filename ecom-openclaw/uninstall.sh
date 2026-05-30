#!/usr/bin/env bash
# =============================================================================
# openclaw-ecommerce-skill — uninstall.sh
# 卸载脚本：从 openclaw.json 中移除所有电商爆款分析 Agent
# =============================================================================

set -euo pipefail

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

SKILL_NAME="openclaw-ecommerce"
AGENT_IDS=(
  "ecommerce_agent"
  "product_fetcher"
  "hot_score_analyzer"
  "report_generator"
)

echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${BOLD}║   OpenClaw Ecommerce Skill — Uninstaller                     ║${RESET}"
echo -e "${BOLD}╚══════════════════════════════════════════════════════════════╝${RESET}"
echo ""

# ── 确认卸载 ─────────────────────────────────────────────────────────────────
echo -e "${YELLOW}⚠️  此操作将从 openclaw.json 中移除以下 Agent：${RESET}"
for id in "${AGENT_IDS[@]}"; do
  echo -e "   - $id"
done
echo ""
read -rp "确认卸载？(y/N): " confirm
[[ "${confirm,,}" == "y" ]] || { info "已取消卸载"; exit 0; }

# ── Step 1: 检测 OpenClaw 根目录 ─────────────────────────────────────────────
step "Step 1/3 — 检测 OpenClaw 根目录"

detect_openclaw_root() {
  local search_paths=(
    "$HOME/.openclaw"
    "$HOME/.claude"
    "$(pwd)"
    "$(pwd)/.."
    "$HOME/Documents/openclaw"
    "$HOME/openclaw"
  )
  for p in "${search_paths[@]}"; do
    p="$(realpath "$p" 2>/dev/null || echo "$p")"
    if [[ -f "$p/openclaw.json" ]]; then echo "$p"; return 0; fi
  done
  return 1
}

if [[ -n "${OPENCLAW_ROOT:-}" ]]; then
  OC_ROOT="$OPENCLAW_ROOT"
elif OC_ROOT="$(detect_openclaw_root)"; then
  info "检测到 OpenClaw 根目录: $OC_ROOT"
else
  error "无法找到 openclaw.json，请设置环境变量 OPENCLAW_ROOT"
fi

OC_JSON="$OC_ROOT/openclaw.json"
[[ -f "$OC_JSON" ]] || error "openclaw.json 不存在: $OC_JSON"

# ── Step 2: 备份并移除 Agent ──────────────────────────────────────────────────
step "Step 2/3 — 移除 Agent"
BACKUP_PATH="${OC_JSON}.uninstall.$(date +%Y%m%d_%H%M%S)"
cp "$OC_JSON" "$BACKUP_PATH"
info "已备份 openclaw.json → $BACKUP_PATH"

AGENT_IDS_JSON="$(printf '%s\n' "${AGENT_IDS[@]}" | jq -R . | jq -s .)"
UPDATED_JSON="$(jq \
  --argjson ids "$AGENT_IDS_JSON" \
  '.agents = [.agents[]? | select(.id as $id | $ids | index($id) | not)]' \
  "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "已移除 ${#AGENT_IDS[@]} 个 Agent"

# ── Step 3: 注销 Skill ──────────────────────────────────────────────────────
step "Step 3/3 — 注销 Skill"
UPDATED_JSON="$(jq \
  --arg name "$SKILL_NAME" \
  '.skills = [.skills[]? | select(.name != $name)]' \
  "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "Skill '$SKILL_NAME' 已注销"

echo ""
echo -e "${GREEN}${BOLD}✅ 卸载完成${RESET}"
echo -e "  移除 Agent：${#AGENT_IDS[@]} 个"
echo -e "  备份文件：$BACKUP_PATH"
echo ""

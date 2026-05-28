#!/usr/bin/env bash
# =============================================================================
# openclaw-one-person-company-skill — uninstall.sh
# 卸载脚本：从 openclaw.json 删除全部 18 个 Agent 并清理 souls
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

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="openclaw-one-person-company"

# 全部 18 个 Agent ID
AGENT_IDS=(
  "ceo"
  "product_lead" "user_researcher" "data_analyst" "feature_planner" "ux_optimizer"
  "tech_lead" "architect" "backend_dev" "frontend_dev" "qa_engineer" "devops_engineer"
  "growth_lead" "content_planner" "seo_specialist" "ads_optimizer" "user_operator" "crm_analyst"
)

echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${BOLD}║   OpenClaw One Person Company Skill — Uninstaller v2.0.0   ║${RESET}"
echo -e "${BOLD}╚══════════════════════════════════════════════════════════════╝${RESET}"
echo ""
echo -e "${YELLOW}${BOLD}⚠️  此操作将删除 18 个 Agent 及对应 Soul 文件${RESET}"
echo ""

if [[ "${FORCE_UNINSTALL:-}" != "true" ]]; then
  read -rp "确认卸载 '$SKILL_NAME' 吗？(输入 yes 确认，其他取消): " confirm
  if [[ "$confirm" != "yes" ]]; then
    echo ""
    warn "卸载已取消"
    exit 0
  fi
fi

# ── Step 1: 检查 jq ───────────────────────────────────────────────────────
step "Step 1/5 — 检查依赖项"
if ! command -v jq &>/dev/null; then
  error "未检测到 jq，请先安装：https://stedolan.github.io/jq/download/"
fi
success "jq 已就绪"

# ── Step 2: 检测 openclaw.json 路径 ───────────────────────────────────────
step "Step 2/5 — 检测 openclaw.json 位置"

detect_openclaw_root() {
  local search_paths=(
    "$HOME/.openclaw" "$HOME/.claude"
    "$(pwd)" "$(pwd)/.." "$(pwd)/../.."
    "$HOME/Documents/openclaw" "$HOME/openclaw" "/usr/local/openclaw"
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
  info "自动检测到 OpenClaw 根目录: $OC_ROOT"
else
  warn "无法自动检测 OpenClaw 根目录"
  read -rp "请手动输入 OpenClaw 根目录路径: " user_input
  OC_ROOT="${user_input:-$(pwd)}"
fi

OC_JSON="$OC_ROOT/openclaw.json"
[[ ! -f "$OC_JSON" ]] && error "openclaw.json 不存在: $OC_JSON"
success "找到 openclaw.json: $OC_JSON"

BACKUP_PATH="${OC_JSON}.backup.uninstall.$(date +%Y%m%d_%H%M%S)"
cp "$OC_JSON" "$BACKUP_PATH"
info "已备份 openclaw.json → $BACKUP_PATH"

# ── Step 3: 从 openclaw.json 删除所有 18 个 Agent ─────────────────────────
step "Step 3/5 — 从 openclaw.json 删除 Agent"

# 构建 JSON 数组
AGENT_IDS_JSON="$(printf '%s\n' "${AGENT_IDS[@]}" | jq -R . | jq -s .)"

existing_count=$(jq --argjson ids "$AGENT_IDS_JSON" \
  '[.agents[]? | select(.id as $id | $ids | index($id) != null)] | length' \
  "$OC_JSON")

if [[ "$existing_count" -eq 0 ]]; then
  warn "openclaw.json 中未找到本 Skill 的 Agent（可能已卸载）"
else
  info "将删除 ${existing_count} 个 Agent..."
  UPDATED_JSON="$(jq --argjson ids "$AGENT_IDS_JSON" \
    '.agents = [.agents[]? | select(.id as $id | $ids | index($id) == null)]' \
    "$OC_JSON")"
  echo "$UPDATED_JSON" > "$OC_JSON"
  success "已删除 ${existing_count} 个 Agent"
fi

# ── Step 4: 删除 Skill 注册记录 ───────────────────────────────────────────
step "Step 4/5 — 删除 Skill 注册记录"

if jq -e --arg name "$SKILL_NAME" '.skills[]? | select(.name == $name)' "$OC_JSON" &>/dev/null; then
  UPDATED_JSON="$(jq --arg name "$SKILL_NAME" \
    '.skills = [.skills[]? | select(.name != $name)]' \
    "$OC_JSON")"
  echo "$UPDATED_JSON" > "$OC_JSON"
  success "已删除 Skill 注册记录: $SKILL_NAME"
else
  warn "Skill 注册记录不存在，跳过"
fi

# ── Step 5: 删除 Soul 文件 ────────────────────────────────────────────────
step "Step 5/5 — 删除 Soul 文件"
SOULS_DST="$OC_ROOT/souls"
SOUL_DELETED=0

for agent_id in "${AGENT_IDS[@]}"; do
  soul_file="$SOULS_DST/${agent_id}.md"
  if [[ -f "$soul_file" ]]; then
    rm -f "$soul_file"
    success "已删除: ${agent_id}.md"
    SOUL_DELETED=$((SOUL_DELETED + 1))
  else
    warn "不存在（跳过）: ${agent_id}.md"
  fi
done

if [[ -d "$SOULS_DST" ]] && [[ -z "$(ls -A "$SOULS_DST" 2>/dev/null)" ]]; then
  read -rp "souls 目录已为空，是否删除该目录？(y/N): " del_dir
  if [[ "$del_dir" =~ ^[Yy]$ ]]; then
    rmdir "$SOULS_DST"
    success "已删除空目录: $SOULS_DST"
  fi
fi

# ── 完成提示 ──────────────────────────────────────────────────────────────
REMAINING=$(jq '.agents | length' "$OC_JSON")
echo ""
echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}${BOLD}║              ✅ 卸载完成！                                   ║${RESET}"
echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════════════╝${RESET}"
echo ""
echo -e "  ${BOLD}Skill:${RESET}        $SKILL_NAME"
echo -e "  ${BOLD}已删除 Agent:${RESET} ${existing_count:-0} 个"
echo -e "  ${BOLD}已删除 Soul:${RESET}  ${SOUL_DELETED} 个"
echo -e "  ${BOLD}剩余 Agent:${RESET}   ${REMAINING} 个"
echo -e "  ${BOLD}备份文件:${RESET}     $BACKUP_PATH"
echo ""
echo -e "  ${YELLOW}如需重新安装，运行：./install.sh${RESET}"
echo ""

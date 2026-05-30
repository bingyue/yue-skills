#!/usr/bin/env bash
# =============================================================================
# openclaw-ecommerce-skill — install.sh
# 安装脚本：自动检测 OpenClaw 根目录并完成电商爆款分析 4 个 Agent 安装
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
SKILL_NAME="openclaw-ecommerce"
SKILL_VERSION="1.0.0"

# 全部 4 个 Agent ID
AGENT_IDS=(
  "ecommerce_agent"
  "product_fetcher"
  "hot_score_analyzer"
  "report_generator"
)

echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${BOLD}║   OpenClaw Ecommerce Skill — Installer v${SKILL_VERSION}               ║${RESET}"
echo -e "${BOLD}║   电商爆款分析：商品采集 → 热度计算 → 报表生成              ║${RESET}"
echo -e "${BOLD}╚══════════════════════════════════════════════════════════════╝${RESET}"
echo ""

# ── Step 1: 检测 jq 依赖 ────────────────────────────────────────────────────
step "Step 1/8 — 检查依赖项"
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

# ── Step 2: 检测 curl 依赖（用于验证 API 可达性）──────────────────────────
step "Step 2/8 — 检测 curl"
if command -v curl &>/dev/null; then
  success "curl 已就绪：$(curl --version | head -1)"
else
  warn "curl 未安装，跳过 API 连通性检查"
fi

# ── Step 3: 检测 OpenClaw 版本 ──────────────────────────────────────────────
step "Step 3/8 — 检测 OpenClaw"
if command -v openclaw &>/dev/null; then
  OC_VERSION="$(openclaw -v 2>/dev/null || echo 'unknown')"
  success "OpenClaw 已安装：$OC_VERSION"
else
  warn "未检测到 openclaw 命令，请确认已安装 OpenClaw"
  warn "安装命令：npm install -g openclaw"
fi

# ── Step 4: 自动检测 OpenClaw 根目录 ────────────────────────────────────────
step "Step 4/8 — 检测 OpenClaw 根目录"

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
    if [[ -d "$p/skills" ]] || [[ -d "$p/souls" ]]; then echo "$p"; return 0; fi
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

# ── Step 5: 检测/创建 openclaw.json ─────────────────────────────────────────
step "Step 5/8 — 检查 openclaw.json"
OC_JSON="$OC_ROOT/openclaw.json"

if [[ ! -f "$OC_JSON" ]]; then
  warn "openclaw.json 不存在，创建初始配置..."
  cat > "$OC_JSON" <<'INIT_JSON'
{
  "version": "1.0.0",
  "skills": [],
  "agents": [],
  "plugins": [],
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

# ── Step 6: 拷贝 souls 目录 ──────────────────────────────────────────────────
step "Step 6/8 — 安装 Soul 文件（共 ${#AGENT_IDS[@]} 个）"
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

# ── Step 7: 合并 agents.json 到 openclaw.json ───────────────────────────────
step "Step 7/8 — 合并 ${#AGENT_IDS[@]} 个 Agent 到 openclaw.json"
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

# ── 开启 agentToAgent + memory ──────────────────────────────────────────────
UPDATED_JSON="$(jq '
  .config.agentToAgent.enabled = true |
  .config.agentToAgent.allowCrossAgent = true |
  .config.agentToAgent.logCommunication = true |
  .config.maxRecursion = 3 |
  .config.memory.enabled = true
' "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "agentToAgent 已启用（跨 Agent 协作 + 通信日志）"

# ── Step 8: 注册 Skill & 验证 API 连通性 ────────────────────────────────────
step "Step 8/8 — 注册 Skill & 验证数据源"

SKILL_ENTRY="{
  \"name\": \"$SKILL_NAME\",
  \"version\": \"$SKILL_VERSION\",
  \"path\": \"$SKILL_DIR\",
  \"agentCount\": ${#AGENT_IDS[@]},
  \"description\": \"电商爆款分析：商品采集 → 热度计算 → 报表生成\",
  \"dataSource\": \"https://fakestoreapi.com/products\",
  \"installedAt\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"
}"
UPDATED_JSON="$(jq \
  --argjson skill_entry "$SKILL_ENTRY" \
  '.skills = ((.skills // []) | map(select(.name != $skill_entry.name))) + [$skill_entry]' \
  "$OC_JSON")"
echo "$UPDATED_JSON" > "$OC_JSON"
success "Skill '$SKILL_NAME@$SKILL_VERSION' 已注册"

# 验证 Fake Store API 连通性
if command -v curl &>/dev/null; then
  info "验证 Fake Store API 连通性..."
  HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 \
    "https://fakestoreapi.com/products?limit=1" 2>/dev/null || echo "000")
  if [[ "$HTTP_STATUS" == "200" ]]; then
    success "Fake Store API 连通正常（HTTP $HTTP_STATUS）"
  else
    warn "Fake Store API 暂时无法访问（HTTP $HTTP_STATUS），请检查网络连接"
    warn "API 地址：https://fakestoreapi.com/products"
  fi
fi

# ── 最终验证 ─────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}────────────────────── 安装验证 ──────────────────────────────${RESET}"
echo ""
echo -e "${BOLD}【主控 Agent】${RESET}"
jq -r '.agents[] | select(.center_node == true) | "  \(.id) — \(.name) | \(.role)"' "$OC_JSON"
echo ""
echo -e "${BOLD}【子 Agent（按执行顺序）】${RESET}"
jq -r '.agents[] | select(.center_node != true) | "  \(.id) — \(.name) | \(.role)"' "$OC_JSON"
echo ""
AGENT_COUNT=$(jq '.agents | length' "$OC_JSON")
echo -e "  已注册 Agent 总数：${GREEN}${BOLD}${AGENT_COUNT}${RESET}"
echo ""
echo -e "${BOLD}【数据流水线】${RESET}"
echo -e "  ${CYAN}fetch-products${RESET}  →  Fake Store API 商品采集"
echo -e "  ${CYAN}hot-score${RESET}       →  score = rating.rate × rating.count"
echo -e "  ${CYAN}report-generator${RESET} →  Markdown 热度分析报表"
echo ""

# ── 完成提示 ─────────────────────────────────────────────────────────────────
echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}${BOLD}║     ✅ 安装成功！电商爆款分析 Skill 已就绪                  ║${RESET}"
echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════════════╝${RESET}"
echo ""
echo -e "  ${BOLD}Skill:${RESET}      $SKILL_NAME v$SKILL_VERSION"
echo -e "  ${BOLD}安装目录:${RESET}  $OC_ROOT"
echo -e "  ${BOLD}配置文件:${RESET}  $OC_JSON"
echo -e "  ${BOLD}Soul 目录:${RESET} $SOULS_DST"
echo -e "  ${BOLD}备份文件:${RESET}  $BACKUP_PATH"
echo -e "  ${BOLD}数据来源:${RESET}  https://fakestoreapi.com/products"
echo ""
echo -e "  ${CYAN}${BOLD}快速体验：${RESET}"
echo -e "  ${YELLOW}openclaw chat --agent ecommerce_agent${RESET}"
echo -e "  ${YELLOW}> 帮我分析当前电商热门商品，生成爆款报表${RESET}"
echo ""
echo -e "  ${CYAN}更多示例：${RESET}"
echo -e "  ${YELLOW}> 找出 electronics 类目评分最高的商品${RESET}"
echo -e "  ${YELLOW}> 帮我筛选价格低于 30 美元的爆款商品${RESET}"
echo -e "  ${YELLOW}> 生成 Top 10 爆款分析报告${RESET}"
echo ""
echo -e "  ${YELLOW}如需卸载，运行：./uninstall.sh${RESET}"
echo ""

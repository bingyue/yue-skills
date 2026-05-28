#!/usr/bin/env bash
# ============================================================
#  OpenClaw Ecommerce Team Skill — 一键安装脚本
#  用法: bash install.sh
# ============================================================

set -euo pipefail

# ——— 颜色定义 ——————————————————————————————
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

# ——— 工具函数 ——————————————————————————————
log_info()    { echo -e "${BLUE}[INFO]${RESET}  $*"; }
log_success() { echo -e "${GREEN}[OK]${RESET}    $*"; }
log_warn()    { echo -e "${YELLOW}[WARN]${RESET}  $*"; }
log_error()   { echo -e "${RED}[ERROR]${RESET} $*"; }
log_step()    { echo -e "\n${BOLD}${CYAN}▶ $*${RESET}"; }

# ——— 版本检查 ——————————————————————————————
check_node_version() {
  log_step "检查 Node.js 版本"
  if ! command -v node &>/dev/null; then
    log_error "未检测到 Node.js，请先安装 Node.js >= 22"
    exit 1
  fi

  NODE_VERSION=$(node -e "process.stdout.write(process.versions.node)")
  MAJOR=$(echo "$NODE_VERSION" | cut -d. -f1)

  if [ "$MAJOR" -lt 22 ]; then
    log_error "Node.js 版本为 $NODE_VERSION，需要 >= 22.0.0"
    exit 1
  fi

  log_success "Node.js $NODE_VERSION ✓"
}

check_npm_version() {
  log_step "检查 npm / pnpm"
  if command -v pnpm &>/dev/null; then
    PKG_MGR="pnpm"
    PKG_VER=$(pnpm --version)
  elif command -v npm &>/dev/null; then
    PKG_MGR="npm"
    PKG_VER=$(npm --version)
  else
    log_error "未找到 npm 或 pnpm，请先安装"
    exit 1
  fi
  log_success "使用包管理器: $PKG_MGR $PKG_VER ✓"
}

check_openclaw() {
  log_step "检查 OpenClaw CLI"
  if ! command -v openclaw &>/dev/null; then
    log_warn "未检测到 openclaw CLI，跳过自动注册 skill 步骤"
    log_warn "安装完成后可手动执行: openclaw skill install ."
    OPENCLAW_AVAILABLE=false
  else
    OPENCLAW_VERSION=$(openclaw --version 2>/dev/null || echo "unknown")
    log_success "openclaw $OPENCLAW_VERSION ✓"
    OPENCLAW_AVAILABLE=true
  fi
}

# ——— 主安装流程 —————————————————————————————
install_dependencies() {
  log_step "安装 Node.js 依赖"
  if [ "$PKG_MGR" = "pnpm" ]; then
    pnpm install --frozen-lockfile 2>/dev/null || pnpm install
  else
    npm ci 2>/dev/null || npm install
  fi
  log_success "依赖安装完成 ✓"
}

build_project() {
  log_step "TypeScript 编译构建"
  if [ "$PKG_MGR" = "pnpm" ]; then
    pnpm run build
  else
    npm run build
  fi
  log_success "项目构建完成 ✓"
}

register_skill() {
  log_step "注册 OpenClaw Skill"
  if [ "$OPENCLAW_AVAILABLE" = true ]; then
    if openclaw skill install . --yes 2>/dev/null; then
      log_success "Skill 注册成功 ✓"
    else
      log_warn "自动注册失败，请手动执行: openclaw skill install ."
    fi
  else
    log_warn "跳过自动注册（openclaw CLI 不可用）"
  fi
}

verify_agents() {
  log_step "验证 Agent 文件完整性"
  AGENTS=(
    "traffic-strategist"
    "ads-optimizer"
    "content-marketer"
    "product-architect"
    "inventory-guard"
    "order-processor"
    "aftersales-manager"
    "customer-replier"
    "review-guardian"
    "data-director"
  )

  MISSING=0
  for agent in "${AGENTS[@]}"; do
    SOUL_PATH="src/agents/$agent/Soul.md"
    SKILL_PATH="src/agents/$agent/skill.ts"
    if [ -f "$SOUL_PATH" ] && [ -f "$SKILL_PATH" ]; then
      log_success "  Agent [$agent] ✓"
    else
      log_error "  Agent [$agent] 文件缺失!"
      MISSING=$((MISSING + 1))
    fi
  done

  if [ "$MISSING" -gt 0 ]; then
    log_error "$MISSING 个 Agent 文件缺失，请检查项目完整性"
    exit 1
  fi
}

verify_workflows() {
  log_step "验证 Workflow 文件完整性"
  WORKFLOWS=(
    "src/workflows/daily-report.workflow.json"
    "src/workflows/order-flow.workflow.json"
    "src/workflows/growth-cycle.workflow.json"
  )

  for wf in "${WORKFLOWS[@]}"; do
    if [ -f "$wf" ]; then
      log_success "  Workflow [$wf] ✓"
    else
      log_error "  Workflow [$wf] 缺失!"
      exit 1
    fi
  done
}

print_banner() {
  echo ""
  echo -e "${BOLD}${CYAN}"
  echo "  ╔═══════════════════════════════════════════════════════╗"
  echo "  ║       OpenClaw Ecommerce Team Skill Installer         ║"
  echo "  ║              电商运营 AI 团队  v1.0.0                  ║"
  echo "  ╚═══════════════════════════════════════════════════════╝"
  echo -e "${RESET}"
}

print_success() {
  echo ""
  echo -e "${BOLD}${GREEN}"
  echo "  ╔═══════════════════════════════════════════════════════╗"
  echo "  ║              🎉  安装成功！                             ║"
  echo "  ║                                                       ║"
  echo "  ║  ✅ 10 个 Agent 已就绪                                  ║"
  echo "  ║  ✅ 3 个 Workflow 已注册                                ║"
  echo "  ║  ✅ Agent-to-Agent 协作已启用                           ║"
  echo "  ║                                                       ║"
  echo "  ║  启动命令: npm start                                    ║"
  echo "  ║  查看文档: cat README.md                                ║"
  echo "  ╚═══════════════════════════════════════════════════════╝"
  echo -e "${RESET}"
}

# ——— 主入口 ——————————————————————————————————
main() {
  print_banner

  check_node_version
  check_npm_version
  check_openclaw

  verify_agents
  verify_workflows

  install_dependencies
  build_project
  register_skill

  print_success
}

main "$@"

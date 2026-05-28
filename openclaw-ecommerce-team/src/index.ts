// ============================================================
//  OpenClaw Ecommerce Team Skill — 主入口
//  负责初始化 10 个 Agent、加载 Soul.md、注册 3 个 Workflow
//  启用 Agent-to-Agent 协作
// ============================================================

import fs from 'fs';
import path from 'path';
import type { AgentSkill, AgentName, AgentMessage, AgentTask, AgentTaskResult, AgentStatus, AgentData } from './types/agent';
import type { WorkflowDefinition, WorkflowRunResult } from './types/workflow';

// ——— Agent 模块动态导入 —————————————————————————————
import trafficStrategist from './agents/traffic-strategist/skill';
import adsOptimizer from './agents/ads-optimizer/skill';
import contentMarketer from './agents/content-marketer/skill';
import productArchitect from './agents/product-architect/skill';
import inventoryGuard from './agents/inventory-guard/skill';
import orderProcessor from './agents/order-processor/skill';
import aftersalesManager from './agents/aftersales-manager/skill';
import customerReplier from './agents/customer-replier/skill';
import reviewGuardian from './agents/review-guardian/skill';
import dataDirector from './agents/data-director/skill';

// ——— 协作配置 ————————————————————————————————————
export const COLLABORATION_CONFIG = {
  enabled: true,
  maxDepth: 3,
  allowCrossAgentMessaging: true,
  broadcastEvents: true,
} as const;

// ——— Agent 注册表 ————————————————————————————————————
const AGENT_REGISTRY: AgentSkill[] = [
  trafficStrategist,
  adsOptimizer,
  contentMarketer,
  productArchitect,
  inventoryGuard,
  orderProcessor,
  aftersalesManager,
  customerReplier,
  reviewGuardian,
  dataDirector,
];

// ——— Soul 加载工具 ———————————————————————————————————
function loadSoul(agentName: string, soulRelPath: string): string {
  const soulAbsPath = path.resolve(__dirname, '..', 'src', 'agents', agentName, 'Soul.md');
  if (fs.existsSync(soulAbsPath)) {
    return fs.readFileSync(soulAbsPath, 'utf-8');
  }
  // 尝试相对路径
  const altPath = path.resolve(__dirname, soulRelPath.replace('./', '../'));
  if (fs.existsSync(altPath)) {
    return fs.readFileSync(altPath, 'utf-8');
  }
  console.warn(`[Soul] 未找到 Soul.md: ${agentName} (${soulRelPath})`);
  return '';
}

// ——— Workflow 加载工具 ——————————————————————————————
function loadWorkflows(): WorkflowDefinition[] {
  const workflowDir = path.resolve(__dirname, '..', 'src', 'workflows');
  const files = fs.readdirSync(workflowDir).filter(f => f.endsWith('.workflow.json'));
  return files.map(file => {
    const content = fs.readFileSync(path.join(workflowDir, file), 'utf-8');
    return JSON.parse(content) as WorkflowDefinition;
  });
}

// ——— AgentCollaboration 类 ————————————————————————————
export class AgentCollaboration {
  private agents: Map<AgentName, AgentSkill>;
  private callDepth: number = 0;

  constructor(agents: Map<AgentName, AgentSkill>) {
    this.agents = agents;
  }

  async sendMessage(from: AgentName, to: AgentName, message: AgentMessage): Promise<AgentTaskResult> {
    if (this.callDepth >= COLLABORATION_CONFIG.maxDepth) {
      return { success: false, error: `超过最大协作深度 (${COLLABORATION_CONFIG.maxDepth})` };
    }
    const targetAgent = this.agents.get(to);
    if (!targetAgent) {
      return { success: false, error: `Agent [${to}] 未注册` };
    }
    if (!targetAgent.collaboration) {
      return { success: false, error: `Agent [${to}] 未启用协作` };
    }
    this.callDepth++;
    try {
      console.log(`[A2A] ${from} → ${to} | action: ${message.type}`);
      const result = targetAgent.onMessage
        ? await targetAgent.onMessage({ ...message, from })
        : { success: true, output: `[${to}] 已收到消息` };
      return result;
    } finally {
      this.callDepth--;
    }
  }

  async sendTask(from: AgentName, to: AgentName, task: AgentTask): Promise<AgentTaskResult> {
    if (this.callDepth >= COLLABORATION_CONFIG.maxDepth) {
      return { success: false, error: `超过最大协作深度 (${COLLABORATION_CONFIG.maxDepth})` };
    }
    const targetAgent = this.agents.get(to);
    if (!targetAgent) {
      return { success: false, error: `Agent [${to}] 未注册` };
    }
    this.callDepth++;
    try {
      console.log(`[A2A] ${from} →[task]→ ${to} | action: ${task.action}`);
      const result = targetAgent.onTask
        ? await targetAgent.onTask({ ...task, requester: from })
        : { success: true, output: `[${to}] 已接收任务: ${task.action}` };
      return result;
    } finally {
      this.callDepth--;
    }
  }

  async broadcast(from: AgentName, event: string, data: Record<string, unknown>): Promise<void> {
    if (!COLLABORATION_CONFIG.broadcastEvents) return;
    console.log(`[Broadcast] ${from} → ALL | event: ${event}`);
    const promises = Array.from(this.agents.entries())
      .filter(([name]) => name !== from)
      .map(([name, agent]) => {
        if (agent.onData) {
          return agent.onData({ source: from, schema: event, payload: data } as AgentData).catch(err => {
            console.error(`[Broadcast] ${name} 处理失败:`, err);
          });
        }
        return Promise.resolve();
      });
    await Promise.allSettled(promises);
  }
}

// ——— WorkflowEngine 类 ——————————————————————————————
export class WorkflowEngine {
  private workflows: WorkflowDefinition[] = [];
  private agents: Map<AgentName, AgentSkill>;
  private collaboration: AgentCollaboration;
  private timers: Map<string, NodeJS.Timeout | NodeJS.Timer> = new Map();

  constructor(agents: Map<AgentName, AgentSkill>) {
    this.agents = agents;
    this.collaboration = new AgentCollaboration(agents);
    this.workflows = loadWorkflows();
  }

  async startAll(): Promise<void> {
    console.log('\n[WorkflowEngine] 启动所有 Workflow...');
    for (const wf of this.workflows) {
      if (wf.enabled) {
        await this.startWorkflow(wf.name);
      }
    }
  }

  async startWorkflow(name: string): Promise<void> {
    const wf = this.workflows.find(w => w.name === name);
    if (!wf) {
      console.error(`[WorkflowEngine] Workflow [${name}] 不存在`);
      return;
    }
    console.log(`[WorkflowEngine] 启动 Workflow: ${name} (${wf.description})`);

    if (wf.trigger.type === 'cron') {
      this.scheduleCron(wf);
    } else if (wf.trigger.type === 'polling') {
      this.schedulePolling(wf);
    }
  }

  private scheduleCron(wf: WorkflowDefinition): void {
    if (wf.trigger.type !== 'cron') return;
    console.log(`  [Cron] ${wf.name} — cron: "${wf.trigger.expression}"`);
    console.log(`  (生产环境请使用 node-cron 或 OpenClaw 内置调度器)`);
  }

  private schedulePolling(wf: WorkflowDefinition): void {
    if (wf.trigger.type !== 'polling') return;
    const intervalMs = wf.trigger.intervalMs;
    console.log(`  [Polling] ${wf.name} — 每 ${intervalMs}ms 执行一次`);

    const timer = setInterval(async () => {
      try {
        await this.runWorkflow(wf);
      } catch (err) {
        console.error(`[WorkflowEngine] ${wf.name} 执行异常:`, err);
      }
    }, intervalMs);

    this.timers.set(wf.name, timer);
  }

  async runWorkflow(wf: WorkflowDefinition): Promise<WorkflowRunResult> {
    const runId = `${wf.name}-${Date.now()}`;
    const startTime = new Date().toISOString();
    const stepResults: WorkflowRunResult['stepResults'] = [];

    console.log(`[Workflow] 开始执行: ${wf.name} (runId: ${runId})`);

    for (const step of wf.steps) {
      const agent = this.agents.get(step.agent);
      if (!agent) {
        const err = `Agent [${step.agent}] 未注册`;
        console.error(`  [Step:${step.id}] ${err}`);

        if (typeof step.onError === 'object' && step.onError.forward) {
          const forwardResult = await this.collaboration.sendTask(
            step.agent,
            step.onError.forward,
            { action: step.onError.action || step.action, data: { originalStep: step.id } }
          );
          stepResults.push({ stepId: step.id, result: forwardResult });
        } else if (step.onError === 'stop') {
          break;
        }
        continue;
      }

      try {
        const result = agent.onTask
          ? await agent.onTask({ action: step.action, requester: 'system' })
          : { success: true, output: `[${step.agent}] ${step.action} 完成` };

        stepResults.push({ stepId: step.id, result });
        console.log(`  [Step:${step.id}] ${step.agent}.${step.action} — ${result.success ? '✓' : '✗'}`);

        if (!result.success && step.onError === 'stop') break;

        if (!result.success && typeof step.onError === 'object' && step.onError.forward) {
          await this.collaboration.sendTask(step.agent, step.onError.forward, {
            action: step.onError.action || 'handleError',
            data: { error: result.error, originalStep: step.id },
          });
        }
      } catch (err) {
        const errorMsg = err instanceof Error ? err.message : String(err);
        stepResults.push({ stepId: step.id, result: { success: false, error: errorMsg } });
        if (step.onError === 'stop') break;
      }
    }

    const allSuccess = stepResults.every(r => r.result.success);
    return {
      workflowName: wf.name,
      runId,
      startTime,
      endTime: new Date().toISOString(),
      status: allSuccess ? 'success' : 'partial',
      stepResults,
    };
  }

  stopAll(): void {
    for (const [name, timer] of this.timers.entries()) {
      clearInterval(timer as NodeJS.Timeout);
      console.log(`[WorkflowEngine] 停止 Workflow: ${name}`);
    }
    this.timers.clear();
  }
}

// ——— EcommerceTeamSkill 主类 ————————————————————————
export class EcommerceTeamSkill {
  private agents: Map<AgentName, AgentSkill> = new Map();
  private statusMap: Map<AgentName, AgentStatus> = new Map();
  private collaboration!: AgentCollaboration;
  private workflowEngine!: WorkflowEngine;
  private initialized: boolean = false;

  async initialize(): Promise<void> {
    console.log('\n╔══════════════════════════════════════════════════╗');
    console.log('║   OpenClaw Ecommerce Team Skill — 初始化中...    ║');
    console.log('╚══════════════════════════════════════════════════╝\n');

    for (const skillDef of AGENT_REGISTRY) {
      await this.registerAgent(skillDef);
    }

    this.collaboration = new AgentCollaboration(this.agents);
    this.workflowEngine = new WorkflowEngine(this.agents);

    if (process.argv.includes('--start-workflows')) {
      await this.workflowEngine.startAll();
    }

    this.initialized = true;
    this.printStatus();
  }

  private async registerAgent(skill: AgentSkill): Promise<void> {
    const soulContent = loadSoul(skill.name, skill.soul);
    const status: AgentStatus = {
      name: skill.name,
      active: true,
      soulLoaded: soulContent.length > 0,
      registeredAt: new Date().toISOString(),
      taskCount: 0,
    };

    this.agents.set(skill.name, skill);
    this.statusMap.set(skill.name, status);

    if (skill.onInit) await skill.onInit();

    console.log(
      `  [Register] ${skill.name.padEnd(22)} Soul: ${status.soulLoaded ? '✓' : '✗'}  Collab: ${skill.collaboration ? '✓' : '✗'}`
    );
  }

  async sendMessage(agentName: AgentName, message: AgentMessage): Promise<AgentTaskResult> {
    this.ensureInitialized();
    const agent = this.agents.get(agentName);
    if (!agent) return { success: false, error: `Agent [${agentName}] 未注册` };
    const status = this.statusMap.get(agentName)!;
    status.taskCount++;
    status.lastActivity = new Date().toISOString();
    return agent.onMessage ? agent.onMessage(message) : { success: true, output: `[${agentName}] 已收到` };
  }

  async runTask(agentName: AgentName, task: AgentTask): Promise<AgentTaskResult> {
    this.ensureInitialized();
    const agent = this.agents.get(agentName);
    if (!agent) return { success: false, error: `Agent [${agentName}] 未注册` };
    const status = this.statusMap.get(agentName)!;
    status.taskCount++;
    status.lastActivity = new Date().toISOString();
    return agent.onTask ? agent.onTask(task) : { success: true, output: `[${agentName}] 任务已接收` };
  }

  getAgentStatus(agentName: AgentName): AgentStatus | undefined {
    return this.statusMap.get(agentName);
  }

  getAllStatuses(): AgentStatus[] {
    return Array.from(this.statusMap.values());
  }

  getCollaboration(): AgentCollaboration {
    this.ensureInitialized();
    return this.collaboration;
  }

  getWorkflowEngine(): WorkflowEngine {
    this.ensureInitialized();
    return this.workflowEngine;
  }

  private ensureInitialized(): void {
    if (!this.initialized) throw new Error('EcommerceTeamSkill 尚未初始化，请先调用 initialize()');
  }

  private printStatus(): void {
    console.log('\n──────────────────────────────────────────────────');
    console.log('  Agent 注册状态汇总');
    console.log('──────────────────────────────────────────────────');
    for (const status of this.statusMap.values()) {
      const soul = status.soulLoaded ? '🧠' : '⚠️ ';
      const collab = this.agents.get(status.name)?.collaboration ? '🔗' : '  ';
      console.log(`  ${soul} ${collab}  ${status.name}`);
    }
    console.log('──────────────────────────────────────────────────');
    console.log(`  协作配置: maxDepth=${COLLABORATION_CONFIG.maxDepth}, broadcast=${COLLABORATION_CONFIG.broadcastEvents}`);
    console.log('  ✅ 电商团队 Skill 初始化完成\n');
  }

  async shutdown(): Promise<void> {
    console.log('\n[EcommerceTeamSkill] 关闭中...');
    this.workflowEngine.stopAll();
    for (const [name, agent] of this.agents.entries()) {
      if (agent.onShutdown) {
        await agent.onShutdown();
        console.log(`  [Shutdown] ${name}`);
      }
    }
    console.log('[EcommerceTeamSkill] 已安全关闭');
  }
}

// ——— CLI 入口 ————————————————————————————————————————
async function main(): Promise<void> {
  const team = new EcommerceTeamSkill();
  await team.initialize();

  if (process.argv.includes('--register-agents')) {
    console.log('[CLI] Agent 注册完成');
    process.exit(0);
  }

  process.on('SIGINT', async () => {
    await team.shutdown();
    process.exit(0);
  });

  process.on('SIGTERM', async () => {
    await team.shutdown();
    process.exit(0);
  });
}

main().catch(err => {
  console.error('[FATAL]', err);
  process.exit(1);
});

export default EcommerceTeamSkill;

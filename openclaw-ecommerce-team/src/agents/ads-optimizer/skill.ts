import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'ads-optimizer',
  description: '广告优化师 —— 负责付费广告投放、ROI 优化与预算智能分配',
  soul: './Soul.md',
  collaboration: true,
  role: 'ads-optimizer',

  capabilities: [
    'optimizeAdCampaign',
    'adjustBidStrategy',
    'allocateBudget',
    'analyzeAdPerformance',
    'runABTest',
    'audienceTargeting',
    'roasTracking',
  ],

  allowedTools: [
    'ad-platform-api',
    'analytics-api',
    'data-query',
    'report-generator',
    'agent-messenger',
    'notification-sender',
  ],

  collaborationConfig: {
    enabled: true,
    maxDepth: 3,
    allowCrossAgentMessaging: true,
    broadcastEvents: true,
  },

  async onInit(): Promise<void> {
    console.log(`  [ads-optimizer] 已就绪 — 广告优化师上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [ads-optimizer] 收到消息 from ${message.from}: ${message.content}`);

    switch (message.type) {
      case 'analyze':
        return {
          success: true,
          output: {
            agent: 'ads-optimizer',
            action: 'analyzeAdPerformance',
            summary: '广告表现分析完成',
            metrics: { ctr: '3.2%', cvr: '8.5%', cpc: '¥2.8', roas: 3.6 },
            insight: 'ROAS 低于目标值 4.0，建议暂停低效广告组并集中预算',
          },
        };

      default:
        return {
          success: true,
          output: { agent: 'ads-optimizer', message: `已处理消息: ${message.content}` },
        };
    }
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [ads-optimizer] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'optimizeAdCampaign':
        return {
          success: true,
          output: {
            agent: 'ads-optimizer',
            action: 'optimizeAdCampaign',
            changes: [
              { campaignId: 'C001', action: '提高出价 15%', reason: 'CVR 高于均值 2x' },
              { campaignId: 'C002', action: '暂停低效关键词 x12', reason: 'CPC 超出阈值' },
              { campaignId: 'C003', action: '扩展相似受众', reason: '原受众已饱和' },
            ],
            estimatedROASImprovement: '+0.4',
          },
          duration: 1800,
        };

      case 'adjustBidStrategy':
        return {
          success: true,
          output: {
            agent: 'ads-optimizer',
            action: 'adjustBidStrategy',
            strategy: task.data?.strategy ?? '目标 ROAS 智能出价',
            targetROAS: task.data?.targetROAS ?? 4.0,
            applied: true,
          },
          duration: 600,
        };

      case 'allocateBudget':
        return {
          success: true,
          output: {
            agent: 'ads-optimizer',
            action: 'allocateBudget',
            totalBudget: task.data?.budget ?? 100000,
            allocation: {
              searchAds: '45%',
              feedAds: '35%',
              displayAds: '10%',
              retargeting: '10%',
            },
          },
          duration: 900,
        };

      case 'runABTest':
        return {
          success: true,
          output: {
            agent: 'ads-optimizer',
            action: 'runABTest',
            testName: task.data?.testName ?? '素材 A/B 测试',
            status: 'launched',
            expectedDuration: '7 天',
            minSampleSize: 5000,
          },
          duration: 400,
        };

      default:
        return {
          success: true,
          output: { agent: 'ads-optimizer', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [ads-optimizer] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'ads-optimizer', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [ads-optimizer] 已安全下线`);
  },
};

export default skill;

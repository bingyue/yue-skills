import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'product-architect',
  description: '商品架构师 —— 负责选品决策、定价策略与商品类目管理',
  soul: './Soul.md',
  collaboration: true,
  role: 'product-architect',

  capabilities: [
    'designProductMatrix',
    'setPricingStrategy',
    'selectNewProducts',
    'auditSKUStructure',
    'competitorProductAnalysis',
    'categoryPlanning',
    'profitAnalysis',
  ],

  allowedTools: [
    'web-search',
    'data-query',
    'analytics-api',
    'report-generator',
    'agent-messenger',
  ],

  collaborationConfig: {
    enabled: true,
    maxDepth: 3,
    allowCrossAgentMessaging: true,
    broadcastEvents: true,
  },

  async onInit(): Promise<void> {
    console.log(`  [product-architect] 已就绪 — 商品架构师上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [product-architect] 收到消息 from ${message.from}: ${message.content}`);
    return {
      success: true,
      output: { agent: 'product-architect', message: `已处理消息: ${message.content}` },
    };
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [product-architect] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'designProductMatrix':
        return {
          success: true,
          output: {
            agent: 'product-architect',
            action: 'designProductMatrix',
            matrix: {
              trafficDrivers: ['爆款引流款 x5', '季节性特价款 x3'],
              profitMakers: ['高毛利利润款 x8', '套餐捆绑款 x4'],
              brandBuilders: ['形象旗舰款 x2', '联名限定款 x1'],
            },
            totalActiveSKU: 68,
          },
          duration: 2000,
        };

      case 'setPricingStrategy':
        return {
          success: true,
          output: {
            agent: 'product-architect',
            action: 'setPricingStrategy',
            strategy: '竞争导向 + 成本加成混合定价',
            avgMargin: '38%',
            priceAdjustments: [
              { sku: 'SKU-001', action: '降价 5%', reason: '竞品价格下调' },
              { sku: 'SKU-015', action: '涨价 8%', reason: '原材料成本上升' },
            ],
          },
          duration: 1500,
        };

      case 'selectNewProducts':
        return {
          success: true,
          output: {
            agent: 'product-architect',
            action: 'selectNewProducts',
            candidates: task.data?.count ?? 5,
            selected: 3,
            criteria: ['市场容量 > 1亿', '竞争密度中等', '毛利率 > 35%', '退货率预估 < 5%'],
          },
          duration: 3000,
        };

      case 'auditSKUStructure':
        return {
          success: true,
          output: {
            agent: 'product-architect',
            action: 'auditSKUStructure',
            totalSKU: 156,
            activeHealthy: 89,
            needOptimization: 34,
            recommendedRemoval: 33,
            action: '建议清退 33 个长尾低效 SKU，释放运营资源',
          },
          duration: 1800,
        };

      default:
        return {
          success: true,
          output: { agent: 'product-architect', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [product-architect] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'product-architect', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [product-architect] 已安全下线`);
  },
};

export default skill;

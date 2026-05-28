import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'inventory-guard',
  description: '库存守护者 —— 负责库存实时监控、补货预警与滞销处理',
  soul: './Soul.md',
  collaboration: true,
  role: 'inventory-guard',

  capabilities: [
    'monitorInventory',
    'triggerRestockAlert',
    'forecastDemand',
    'handleSlowMoving',
    'conductInventoryAudit',
    'optimizeStockLevel',
    'warehouseAnomalyDetection',
  ],

  allowedTools: [
    'inventory-api',
    'data-query',
    'analytics-api',
    'notification-sender',
    'agent-messenger',
    'report-generator',
  ],

  collaborationConfig: {
    enabled: true,
    maxDepth: 3,
    allowCrossAgentMessaging: true,
    broadcastEvents: true,
  },

  async onInit(): Promise<void> {
    console.log(`  [inventory-guard] 已就绪 — 库存守护者上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [inventory-guard] 收到消息 from ${message.from}: ${message.content}`);
    return {
      success: true,
      output: { agent: 'inventory-guard', message: `已处理消息: ${message.content}` },
    };
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [inventory-guard] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'monitorInventory':
        return {
          success: true,
          output: {
            agent: 'inventory-guard',
            action: 'monitorInventory',
            totalSKUs: 156,
            healthy: 118,
            lowStock: 12,
            outOfStock: 3,
            overStock: 23,
            alerts: [
              { sku: 'SKU-003', stock: 8, safetyStock: 50, status: '紧急补货' },
              { sku: 'SKU-017', stock: 15, safetyStock: 30, status: '低库存预警' },
              { sku: 'SKU-042', stock: 0, safetyStock: 20, status: '已断货' },
            ],
          },
          duration: 1200,
        };

      case 'triggerRestockAlert':
        return {
          success: true,
          output: {
            agent: 'inventory-guard',
            action: 'triggerRestockAlert',
            alertSent: true,
            skuCount: task.data?.count ?? 3,
            notifiedAgents: ['order-processor', 'product-architect'],
            urgencyLevel: task.data?.urgency ?? 'high',
          },
          duration: 400,
        };

      case 'forecastDemand':
        return {
          success: true,
          output: {
            agent: 'inventory-guard',
            action: 'forecastDemand',
            forecastPeriod: '未来 30 天',
            topDemandSKUs: [
              { sku: 'SKU-001', forecastQty: 2800, confidence: '88%' },
              { sku: 'SKU-008', forecastQty: 1500, confidence: '82%' },
            ],
            recommendedRestock: { totalUnits: 15000, estimatedCost: '¥380,000' },
          },
          duration: 2000,
        };

      case 'handleSlowMoving':
        return {
          success: true,
          output: {
            agent: 'inventory-guard',
            action: 'handleSlowMoving',
            slowMovingCount: 23,
            proposals: [
              { sku: 'SKU-099', action: '捆绑促销', expectedClearance: '60 天' },
              { sku: 'SKU-105', action: '折扣清仓 30%', expectedClearance: '30 天' },
              { sku: 'SKU-112', action: '建议停售退货供应商', reason: '库龄 > 180 天' },
            ],
          },
          duration: 1500,
        };

      case 'conductInventoryAudit':
        return {
          success: true,
          output: {
            agent: 'inventory-guard',
            action: 'conductInventoryAudit',
            auditDate: new Date().toISOString().split('T')[0],
            systemQty: 15680,
            physicalQty: 15612,
            discrepancy: 68,
            discrepancyRate: '0.43%',
            status: '库存盘点完成，差异率正常范围内',
          },
          duration: 3500,
        };

      default:
        return {
          success: true,
          output: { agent: 'inventory-guard', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [inventory-guard] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'inventory-guard', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [inventory-guard] 已安全下线`);
  },
};

export default skill;

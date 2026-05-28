import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'order-processor',
  description: '订单处理官 —— 负责订单审核、物流跟踪与异常订单处理',
  soul: './Soul.md',
  collaboration: true,
  role: 'order-processor',

  capabilities: [
    'reviewOrders',
    'trackLogistics',
    'handleAbnormalOrders',
    'batchProcessOrders',
    'updateOrderStatus',
    'splitOrMergeOrders',
    'flagHighRiskOrders',
  ],

  allowedTools: [
    'order-api',
    'inventory-api',
    'data-query',
    'notification-sender',
    'agent-messenger',
    'analytics-api',
  ],

  collaborationConfig: {
    enabled: true,
    maxDepth: 3,
    allowCrossAgentMessaging: true,
    broadcastEvents: true,
  },

  async onInit(): Promise<void> {
    console.log(`  [order-processor] 已就绪 — 订单处理官上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [order-processor] 收到消息 from ${message.from}: ${message.content}`);
    return {
      success: true,
      output: { agent: 'order-processor', message: `已处理消息: ${message.content}` },
    };
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [order-processor] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'reviewOrders':
        return {
          success: true,
          output: {
            agent: 'order-processor',
            action: 'reviewOrders',
            newOrders: 186,
            reviewed: 183,
            abnormal: 3,
            abnormalDetails: [
              { orderId: 'ORD-20260304-001', issue: '支付金额异常', action: '已冻结，转 aftersales-manager' },
              { orderId: 'ORD-20260304-002', issue: '地址不完整', action: '已暂停，触发客服联系' },
              { orderId: 'ORD-20260304-003', issue: '高风险用户标记', action: '人工复审队列' },
            ],
            avgReviewTime: '4.2 分钟',
          },
          duration: 1500,
        };

      case 'trackLogistics':
        return {
          success: true,
          output: {
            agent: 'order-processor',
            action: 'trackLogistics',
            inTransit: 1248,
            delivered: 892,
            delayed: 12,
            delayedAlerts: [
              { orderId: 'ORD-20260302-156', delay: '24h', reason: '天气原因', action: '已通知用户' },
            ],
            onTimeRate: '98.9%',
          },
          duration: 1000,
        };

      case 'handleAbnormalOrders':
        return {
          success: true,
          output: {
            agent: 'order-processor',
            action: 'handleAbnormalOrders',
            processed: task.data?.count ?? 3,
            forwarded: { agent: 'aftersales-manager', count: 2 },
            resolved: 1,
            summary: '2 件已转售后处理，1 件已自动修正',
          },
          duration: 800,
        };

      case 'pollNewOrders':
        return {
          success: true,
          output: {
            agent: 'order-processor',
            action: 'pollNewOrders',
            polledAt: new Date().toISOString(),
            newOrderCount: Math.floor(Math.random() * 30) + 5,
            pendingProcessing: Math.floor(Math.random() * 5),
            systemStatus: 'healthy',
          },
          duration: 300,
        };

      case 'batchProcessOrders':
        return {
          success: true,
          output: {
            agent: 'order-processor',
            action: 'batchProcessOrders',
            totalBatch: task.data?.batchSize ?? 500,
            processed: task.data?.batchSize ?? 500,
            shipped: (task.data?.batchSize as number ?? 500) - 8,
            held: 8,
            processingTime: '12 分钟',
          },
          duration: 5000,
        };

      default:
        return {
          success: true,
          output: { agent: 'order-processor', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [order-processor] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'order-processor', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [order-processor] 已安全下线`);
  },
};

export default skill;

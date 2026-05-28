import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'aftersales-manager',
  description: '售后管理官 —— 负责退换货处理、纠纷调解与客户满意度管理',
  soul: './Soul.md',
  collaboration: true,
  role: 'aftersales-manager',

  capabilities: [
    'processRefundRequest',
    'handleReturnExchange',
    'mediateDispute',
    'trackAftersalesCase',
    'analyzeSatisfaction',
    'escalateMaliciousReturn',
    'generateAftersalesReport',
  ],

  allowedTools: [
    'order-api',
    'crm-api',
    'notification-sender',
    'agent-messenger',
    'data-query',
    'report-generator',
    'email-sender',
  ],

  collaborationConfig: {
    enabled: true,
    maxDepth: 3,
    allowCrossAgentMessaging: true,
    broadcastEvents: true,
  },

  async onInit(): Promise<void> {
    console.log(`  [aftersales-manager] 已就绪 — 售后管理官上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [aftersales-manager] 收到消息 from ${message.from}: ${message.content}`);
    return {
      success: true,
      output: { agent: 'aftersales-manager', message: `已处理消息: ${message.content}` },
    };
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [aftersales-manager] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'processRefundRequest':
        return {
          success: true,
          output: {
            agent: 'aftersales-manager',
            action: 'processRefundRequest',
            orderId: task.data?.orderId ?? 'ORD-UNKNOWN',
            refundAmount: task.data?.amount ?? 299,
            decision: 'approved',
            reason: '商品质量问题，符合退款条件',
            processingTime: '1.5 小时',
            userNotified: true,
          },
          duration: 900,
        };

      case 'handleReturnExchange':
        return {
          success: true,
          output: {
            agent: 'aftersales-manager',
            action: 'handleReturnExchange',
            type: task.data?.type ?? 'return',
            status: 'approved',
            returnLabel: '已生成退货标签并发送用户邮箱',
            expectedReturnDate: new Date(Date.now() + 7 * 24 * 3600 * 1000).toISOString().split('T')[0],
          },
          duration: 1200,
        };

      case 'mediateDispute':
        return {
          success: true,
          output: {
            agent: 'aftersales-manager',
            action: 'mediateDispute',
            disputeId: task.data?.disputeId ?? 'DSP-001',
            resolution: '协商成功',
            outcome: '退款 50% 作为补偿，用户接受',
            closedAt: new Date().toISOString(),
          },
          duration: 2000,
        };

      case 'handleAbnormalOrder':
        return {
          success: true,
          output: {
            agent: 'aftersales-manager',
            action: 'handleAbnormalOrder',
            orderId: task.data?.orderId,
            originalIssue: task.data?.error,
            handlingStatus: 'in-progress',
            assignedTo: 'manual-review',
            estimatedResolution: '24 小时内',
          },
          duration: 600,
        };

      case 'generateAftersalesReport':
        return {
          success: true,
          output: {
            agent: 'aftersales-manager',
            action: 'generateAftersalesReport',
            period: task.data?.period ?? '本周',
            totalCases: 234,
            resolved: 218,
            pending: 16,
            satisfactionRate: '94.2%',
            avgResponseTime: '1.8 小时',
            topIssues: ['物流延迟', '商品描述不符', '包装破损'],
          },
          duration: 1800,
        };

      default:
        return {
          success: true,
          output: { agent: 'aftersales-manager', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [aftersales-manager] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'aftersales-manager', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [aftersales-manager] 已安全下线`);
  },
};

export default skill;

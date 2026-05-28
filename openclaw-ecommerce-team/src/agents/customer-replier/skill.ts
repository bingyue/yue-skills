import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'customer-replier',
  description: '客户回复官 —— 负责智能客服、用户咨询解答与关系维护',
  soul: './Soul.md',
  collaboration: true,
  role: 'customer-replier',

  capabilities: [
    'replyCustomerInquiry',
    'handleComplaint',
    'sendOrderNotification',
    'manageFAQ',
    'escalateToAftersales',
    'maintainCustomerRelation',
    'generateReplyTemplate',
  ],

  allowedTools: [
    'crm-api',
    'order-api',
    'notification-sender',
    'agent-messenger',
    'email-sender',
    'data-query',
  ],

  collaborationConfig: {
    enabled: true,
    maxDepth: 3,
    allowCrossAgentMessaging: true,
    broadcastEvents: true,
  },

  async onInit(): Promise<void> {
    console.log(`  [customer-replier] 已就绪 — 客户回复官上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [customer-replier] 收到消息 from ${message.from}: ${message.content}`);
    return {
      success: true,
      output: { agent: 'customer-replier', message: `已处理消息: ${message.content}` },
    };
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [customer-replier] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'replyCustomerInquiry':
        return {
          success: true,
          output: {
            agent: 'customer-replier',
            action: 'replyCustomerInquiry',
            customerId: task.data?.customerId ?? 'USER-001',
            inquiry: task.data?.question ?? '商品发货了吗？',
            reply: '您好！您的订单已于今日上午完成打包，预计今天下午 14:00 前完成揽收，您可以通过【订单详情】页面实时追踪物流状态。如有其他问题随时联系我们！',
            channel: task.data?.channel ?? 'chat',
            responseTime: '2 分钟',
          },
          duration: 800,
        };

      case 'handleComplaint':
        return {
          success: true,
          output: {
            agent: 'customer-replier',
            action: 'handleComplaint',
            complaintType: task.data?.type ?? '物流延迟',
            approach: 'empathy + solution',
            reply: '非常抱歉给您带来了不便！我完全理解您的心情。经查询，您的包裹因天气原因导致运输延误，预计明日送达。我们将为您申请一张 20 元优惠券作为补偿，感谢您的耐心等待！',
            escalated: false,
            couponIssued: true,
          },
          duration: 1200,
        };

      case 'sendOrderNotification':
        return {
          success: true,
          output: {
            agent: 'customer-replier',
            action: 'sendOrderNotification',
            orderId: task.data?.orderId,
            notificationType: task.data?.type ?? 'shipped',
            sent: true,
            channels: ['短信', 'APP 推送'],
          },
          duration: 400,
        };

      case 'generateReplyTemplate':
        return {
          success: true,
          output: {
            agent: 'customer-replier',
            action: 'generateReplyTemplate',
            scenario: task.data?.scenario ?? '退款咨询',
            template: '您好，感谢您联系我们！关于您的退款申请，我们已经收到并正在处理中，预计 1-3 个工作日内退款到账。如有疑问请随时联系我们，祝您购物愉快！',
            language: 'zh-CN',
          },
          duration: 600,
        };

      default:
        return {
          success: true,
          output: { agent: 'customer-replier', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [customer-replier] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'customer-replier', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [customer-replier] 已安全下线`);
  },
};

export default skill;

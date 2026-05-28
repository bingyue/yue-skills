import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'review-guardian',
  description: '评价守护者 —— 负责评价监控、差评处理与店铺口碑管理',
  soul: './Soul.md',
  collaboration: true,
  role: 'review-guardian',

  capabilities: [
    'monitorReviews',
    'handleNegativeReview',
    'replyToReviews',
    'analyzeReviewTrend',
    'detectAbnormalReviews',
    'triggerAftersalesForNegative',
    'generateReputationReport',
  ],

  allowedTools: [
    'crm-api',
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
    console.log(`  [review-guardian] 已就绪 — 评价守护者上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [review-guardian] 收到消息 from ${message.from}: ${message.content}`);
    return {
      success: true,
      output: { agent: 'review-guardian', message: `已处理消息: ${message.content}` },
    };
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [review-guardian] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'monitorReviews':
        return {
          success: true,
          output: {
            agent: 'review-guardian',
            action: 'monitorReviews',
            totalNewReviews: 89,
            fivestar: 61,
            fourStar: 18,
            threeStar: 4,
            twoStarOrBelow: 6,
            averageRating: 4.6,
            negativeReviewsHandled: 6,
            shopScore: 4.82,
          },
          duration: 1000,
        };

      case 'handleNegativeReview':
        return {
          success: true,
          output: {
            agent: 'review-guardian',
            action: 'handleNegativeReview',
            reviewId: task.data?.reviewId ?? 'REV-001',
            rating: task.data?.rating ?? 2,
            issue: task.data?.issue ?? '物流太慢',
            reply: '非常感谢您的宝贵反馈！对于此次物流体验未达到您的期望，我们深感抱歉。我们已与物流服务商反馈您的情况，并持续优化配送时效。我们已为您发送一张专属优惠券，期待您下次的光临！',
            escalatedToAftersales: true,
            resolvedAt: new Date().toISOString(),
          },
          duration: 1500,
        };

      case 'replyToReviews':
        return {
          success: true,
          output: {
            agent: 'review-guardian',
            action: 'replyToReviews',
            replied: task.data?.count ?? 20,
            positiveReplies: 14,
            negativeReplies: 6,
            avgReplyLength: 85,
            allPersonalized: true,
          },
          duration: 2000,
        };

      case 'analyzeReviewTrend':
        return {
          success: true,
          output: {
            agent: 'review-guardian',
            action: 'analyzeReviewTrend',
            period: '近 30 天',
            trendDirection: '好转',
            ratingChange: '+0.08',
            topPraised: ['发货速度快', '商品质量好', '包装精美'],
            topComplaints: ['物流偶有延迟', '部分商品描述不够详细'],
            recommendActions: [
              '对物流问题主动补偿，降低差评率',
              '优化商品详情页，减少预期落差',
            ],
          },
          duration: 1800,
        };

      case 'generateReputationReport':
        return {
          success: true,
          output: {
            agent: 'review-guardian',
            action: 'generateReputationReport',
            reportDate: new Date().toISOString().split('T')[0],
            overallScore: 4.82,
            nps: 72,
            reviewCount30d: 1248,
            negativeRate: '4.8%',
            healthStatus: '良好',
          },
          duration: 1200,
        };

      default:
        return {
          success: true,
          output: { agent: 'review-guardian', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [review-guardian] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'review-guardian', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [review-guardian] 已安全下线`);
  },
};

export default skill;

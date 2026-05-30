import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'traffic-strategist',
  description: '电商流量策略官 —— 负责全域流量分析、趋势预测与活动策划',
  soul: './Soul.md',
  collaboration: true,
  role: 'traffic-strategist',

  capabilities: [
    'analyzeTraffic',
    'predictTrend',
    'designCampaign',
    'auditTrafficSources',
    'competitorAnalysis',
    'trafficForecasting',
    'channelOptimization',
  ],

  allowedTools: [
    'web-search',
    'analytics-api',
    'data-query',
    'report-generator',
    'agent-messenger',
    'scheduler',
  ],

  collaborationConfig: {
    enabled: true,
    maxDepth: 3,
    allowCrossAgentMessaging: true,
    broadcastEvents: true,
  },

  async onInit(): Promise<void> {
    console.log(`  [traffic-strategist] 已就绪 — 流量策略官上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [traffic-strategist] 收到消息 from ${message.from}: ${message.content}`);

    switch (message.type) {
      case 'analyze':
        return {
          success: true,
          output: {
            agent: 'traffic-strategist',
            action: 'analyzeTraffic',
            summary: '流量分析完成：自然流量占比 45%，付费流量 35%，社交流量 20%',
            recommendations: [
              '建议加大 SEO 内容投入，自然流量仍有 15% 提升空间',
              '社交流量转化率低，需配合 content-marketer 优化内容钩子',
            ],
          },
        };

      case 'query':
        return {
          success: true,
          output: {
            agent: 'traffic-strategist',
            action: 'queryTrafficData',
            data: { totalVisits: 125000, bounceRate: '32%', avgSessionDuration: '2m45s' },
          },
        };

      default:
        return {
          success: true,
          output: { agent: 'traffic-strategist', message: `已处理消息: ${message.content}` },
        };
    }
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [traffic-strategist] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'analyzeTraffic':
        return {
          success: true,
          output: {
            agent: 'traffic-strategist',
            action: 'analyzeTraffic',
            topChannels: ['organic-search', 'paid-search', 'social-media'],
            insight: '搜索流量本周环比下降 8%，建议紧急检查关键词排名',
          },
          duration: 1200,
        };

      case 'predictTrend':
        return {
          success: true,
          output: {
            agent: 'traffic-strategist',
            action: 'predictTrend',
            prediction: {
              nextWeek: '+12%',
              nextMonth: '+28%',
              confidence: '85%',
              driver: '即将到来的大促节点',
            },
          },
          duration: 800,
        };

      case 'designCampaign':
        return {
          success: true,
          output: {
            agent: 'traffic-strategist',
            action: 'designCampaign',
            campaignName: (task.data?.campaignName as string) ?? '春季增长活动',
            strategy: {
              channels: ['SEO', '信息流广告', '微信私域', '达人种草'],
              expectedTrafficIncrease: '35%',
              budget: task.data?.budget ?? 50000,
              duration: '14 天',
            },
          },
          duration: 2000,
        };

      case 'generateWeeklyInsight':
        return {
          success: true,
          output: {
            agent: 'traffic-strategist',
            weeklyHighlights: [
              '流量峰值出现在周三 20:00-22:00',
              '移动端占比提升至 78%，需优化移动端落地页',
              '竞品关键词 "智能家居套装" 搜索量上涨 40%',
            ],
          },
          duration: 1500,
        };

      default:
        return {
          success: true,
          output: { agent: 'traffic-strategist', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [traffic-strategist] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'traffic-strategist', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [traffic-strategist] 已安全下线`);
  },
};

export default skill;

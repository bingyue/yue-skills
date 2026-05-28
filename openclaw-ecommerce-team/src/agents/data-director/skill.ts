import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'data-director',
  description: '数据总监 —— 负责数据分析、报表生成与全团队决策数据支撑',
  soul: './Soul.md',
  collaboration: true,
  role: 'data-director',

  capabilities: [
    'generateDailyReport',
    'generateWeeklyReport',
    'generateMonthlyReport',
    'analyzeSalesFunnel',
    'detectDataAnomaly',
    'forecastSalesTarget',
    'buildDashboard',
    'queryMetrics',
  ],

  allowedTools: [
    'analytics-api',
    'data-query',
    'report-generator',
    'notification-sender',
    'agent-messenger',
    'file-writer',
    'email-sender',
  ],

  collaborationConfig: {
    enabled: true,
    maxDepth: 3,
    allowCrossAgentMessaging: true,
    broadcastEvents: true,
  },

  async onInit(): Promise<void> {
    console.log(`  [data-director] 已就绪 — 数据总监上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [data-director] 收到消息 from ${message.from}: ${message.content}`);
    return {
      success: true,
      output: { agent: 'data-director', message: `已处理消息: ${message.content}` },
    };
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [data-director] 执行任务: ${task.action}`);

    const today = new Date().toISOString().split('T')[0];

    switch (task.action) {
      case 'generateDailyReport':
        return {
          success: true,
          output: {
            agent: 'data-director',
            action: 'generateDailyReport',
            reportDate: task.data?.date ?? today,
            generatedAt: new Date().toISOString(),
            summary: {
              totalRevenue: '¥ 128,456',
              orderCount: 892,
              avgOrderValue: '¥ 143.9',
              newCustomers: 234,
              conversionRate: '3.8%',
              refundRate: '1.2%',
            },
            highlights: [
              '今日营收环比昨日增长 12.4%',
              '新客转化率略低于目标值 4.0%，建议排查落地页',
              '品类 A 销量突破历史新高',
            ],
            recommendations: [
              '流量高峰在 20:00-22:00，建议定时推送优惠活动',
              '客单价偏低，可测试满减策略提升 AOV',
            ],
            distributedTo: [
              'traffic-strategist',
              'ads-optimizer',
              'content-marketer',
              'product-architect',
              'inventory-guard',
              'order-processor',
            ],
          },
          duration: 3000,
        };

      case 'generateWeeklyReport':
        return {
          success: true,
          output: {
            agent: 'data-director',
            action: 'generateWeeklyReport',
            period: task.data?.period ?? '本周',
            totalRevenue: '¥ 856,320',
            growthRate: '+18.5% WoW',
            topProducts: ['商品A', '商品B', '商品C'],
            underPerformers: ['商品X', '商品Y'],
            channelBreakdown: {
              organic: '45%',
              paid: '35%',
              social: '20%',
            },
          },
          duration: 4000,
        };

      case 'detectDataAnomaly':
        return {
          success: true,
          output: {
            agent: 'data-director',
            action: 'detectDataAnomaly',
            scannedMetrics: 48,
            anomaliesFound: 2,
            anomalies: [
              {
                metric: '退款率',
                current: '4.8%',
                baseline: '1.5%',
                delta: '+220%',
                severity: 'high',
                affectedSKU: 'SKU-023',
              },
              {
                metric: '页面停留时间',
                current: '45s',
                baseline: '95s',
                delta: '-53%',
                severity: 'medium',
                affectedPage: '商品详情页 A',
              },
            ],
            notifiedAgents: ['aftersales-manager', 'product-architect'],
          },
          duration: 2000,
        };

      case 'forecastSalesTarget':
        return {
          success: true,
          output: {
            agent: 'data-director',
            action: 'forecastSalesTarget',
            forecastPeriod: task.data?.period ?? '下个月',
            forecastRevenue: '¥ 1,200,000',
            confidence: '87%',
            growthDrivers: ['大促节点', '新品上线', '广告预算增加'],
            risks: ['竞品降价压力', '供应链波动风险'],
          },
          duration: 2500,
        };

      case 'queryMetrics':
        return {
          success: true,
          output: {
            agent: 'data-director',
            action: 'queryMetrics',
            metrics: task.data?.metrics ?? ['GMV', 'DAU', '转化率'],
            data: {
              GMV: '¥ 128,456',
              DAU: 32800,
              '转化率': '3.8%',
            },
            asOf: new Date().toISOString(),
          },
          duration: 500,
        };

      default:
        return {
          success: true,
          output: { agent: 'data-director', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [data-director] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'data-director', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [data-director] 已安全下线`);
  },
};

export default skill;

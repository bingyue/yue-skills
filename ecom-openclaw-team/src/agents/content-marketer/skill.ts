import type { AgentSkill, AgentMessage, AgentTask, AgentData, AgentTaskResult } from '../../types/agent';

const skill: AgentSkill = {
  name: 'content-marketer',
  description: '内容营销官 —— 负责内容创作、SEO 优化与营销素材管理',
  soul: './Soul.md',
  collaboration: true,
  role: 'content-marketer',

  capabilities: [
    'createContent',
    'optimizeSEO',
    'manageMaterials',
    'planContentCalendar',
    'writeAdCopy',
    'produceLandingPage',
    'briefInfluencer',
  ],

  allowedTools: [
    'content-editor',
    'web-search',
    'analytics-api',
    'file-writer',
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
    console.log(`  [content-marketer] 已就绪 — 内容营销官上线`);
  },

  async onMessage(message: AgentMessage): Promise<AgentTaskResult> {
    console.log(`  [content-marketer] 收到消息 from ${message.from}: ${message.content}`);
    return {
      success: true,
      output: { agent: 'content-marketer', message: `已处理消息: ${message.content}` },
    };
  },

  async onTask(task: AgentTask): Promise<AgentTaskResult> {
    console.log(`  [content-marketer] 执行任务: ${task.action}`);

    switch (task.action) {
      case 'createContent':
        return {
          success: true,
          output: {
            agent: 'content-marketer',
            action: 'createContent',
            contentType: task.data?.type ?? '种草图文',
            title: task.data?.title ?? '春季新品上市，这 5 款爆品你不能错过',
            wordCount: 800,
            seoScore: 92,
            status: '草稿已完成，等待审核',
          },
          duration: 3000,
        };

      case 'optimizeSEO':
        return {
          success: true,
          output: {
            agent: 'content-marketer',
            action: 'optimizeSEO',
            keywords: task.data?.keywords ?? ['智能家居', '爆款好物', '性价比'],
            improvements: [
              '标题加入核心关键词',
              '正文关键词密度优化至 2.5%',
              '增加内链 3 条',
              '图片 alt 标签补充完整',
            ],
            estimatedRankImprovement: '+5 位',
          },
          duration: 1200,
        };

      case 'manageMaterials':
        return {
          success: true,
          output: {
            agent: 'content-marketer',
            action: 'manageMaterials',
            totalMaterials: 156,
            newAdded: task.data?.count ?? 12,
            archived: 8,
            readyForAds: 24,
          },
          duration: 600,
        };

      case 'planContentCalendar':
        return {
          success: true,
          output: {
            agent: 'content-marketer',
            action: 'planContentCalendar',
            week: task.data?.week ?? '本周',
            plan: [
              { day: '周一', type: '产品测评', platform: '小红书' },
              { day: '周三', type: '使用教程', platform: '抖音' },
              { day: '周五', type: '促销预告', platform: '微信公众号' },
              { day: '周日', type: '用户故事', platform: '全渠道' },
            ],
          },
          duration: 800,
        };

      case 'updateMaterials':
        return {
          success: true,
          output: {
            agent: 'content-marketer',
            action: 'updateMaterials',
            updated: task.data?.count ?? 8,
            newCampaignAssets: '春季增长活动素材包已生成',
            formats: ['主图 x5', '海报 x3', '短视频脚本 x2', '文案 x10'],
          },
          duration: 2500,
        };

      default:
        return {
          success: true,
          output: { agent: 'content-marketer', action: task.action, status: '已完成' },
          duration: 500,
        };
    }
  },

  async onData(data: AgentData): Promise<AgentTaskResult> {
    console.log(`  [content-marketer] 接收数据 from ${data.source}: schema=${data.schema}`);
    return {
      success: true,
      output: { agent: 'content-marketer', received: data.schema, processed: true },
    };
  },

  async onShutdown(): Promise<void> {
    console.log(`  [content-marketer] 已安全下线`);
  },
};

export default skill;

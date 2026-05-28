// ============================================================
//  OpenClaw Ecommerce Team — Agent 类型定义
// ============================================================

export type AgentName =
  | 'traffic-strategist'
  | 'ads-optimizer'
  | 'content-marketer'
  | 'product-architect'
  | 'inventory-guard'
  | 'order-processor'
  | 'aftersales-manager'
  | 'customer-replier'
  | 'review-guardian'
  | 'data-director';

export type AllowedTool =
  | 'web-search'
  | 'data-query'
  | 'report-generator'
  | 'notification-sender'
  | 'ad-platform-api'
  | 'content-editor'
  | 'inventory-api'
  | 'order-api'
  | 'crm-api'
  | 'analytics-api'
  | 'email-sender'
  | 'file-writer'
  | 'scheduler'
  | 'agent-messenger';

export interface AgentMessage {
  id?: string;
  from?: AgentName | 'system' | 'user';
  type: 'analyze' | 'generate' | 'notify' | 'query' | 'broadcast' | 'custom';
  content: string;
  metadata?: Record<string, unknown>;
  timestamp?: string;
}

export interface AgentTask {
  id?: string;
  action: string;
  data?: Record<string, unknown>;
  priority?: 'low' | 'normal' | 'high' | 'urgent';
  deadline?: string;
  requester?: AgentName | 'system' | 'user';
}

export interface AgentData {
  source: string;
  schema?: string;
  payload: Record<string, unknown>;
  receivedAt?: string;
}

export interface AgentTaskResult {
  success: boolean;
  output?: unknown;
  error?: string;
  duration?: number;
}

export interface AgentCollaborationConfig {
  enabled: boolean;
  maxDepth: number;
  allowCrossAgentMessaging?: boolean;
  broadcastEvents?: boolean;
}

export interface AgentSkill {
  name: AgentName;
  description: string;
  soul: string;
  collaboration: boolean;
  role: string;
  capabilities: string[];
  allowedTools: AllowedTool[];
  collaborationConfig?: AgentCollaborationConfig;

  onMessage?(message: AgentMessage): Promise<AgentTaskResult>;
  onTask?(task: AgentTask): Promise<AgentTaskResult>;
  onData?(data: AgentData): Promise<AgentTaskResult>;
  onInit?(): Promise<void>;
  onShutdown?(): Promise<void>;
}

export interface AgentStatus {
  name: AgentName;
  active: boolean;
  soulLoaded: boolean;
  registeredAt: string;
  lastActivity?: string;
  taskCount: number;
}

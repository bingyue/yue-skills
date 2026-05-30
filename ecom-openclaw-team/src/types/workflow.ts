// ============================================================
//  OpenClaw Ecommerce Team — Workflow 类型定义
// ============================================================

import type { AgentName, AgentTaskResult } from './agent';

export type TriggerType = 'cron' | 'polling' | 'event' | 'manual';

export interface CronTrigger {
  type: 'cron';
  expression: string;
  timezone?: string;
}

export interface PollingTrigger {
  type: 'polling';
  intervalMs: number;
  maxRetries?: number;
}

export interface EventTrigger {
  type: 'event';
  eventName: string;
  source?: string;
}

export type WorkflowTrigger = CronTrigger | PollingTrigger | EventTrigger;

export interface WorkflowStep {
  id: string;
  agent: AgentName;
  action: string;
  inputMapping?: Record<string, string>;
  outputKey?: string;
  condition?: string;
  onError?: 'stop' | 'continue' | 'retry' | { forward: AgentName; action: string };
  retryConfig?: { maxRetries: number; delayMs: number };
  timeout?: number;
}

export interface WorkflowDefinition {
  name: string;
  description: string;
  version: string;
  trigger: WorkflowTrigger;
  steps: WorkflowStep[];
  onSuccess?: { notify?: AgentName[]; action?: string };
  onFailure?: { notify?: AgentName[]; action?: string };
  enabled: boolean;
  tags?: string[];
}

export interface WorkflowRunResult {
  workflowName: string;
  runId: string;
  startTime: string;
  endTime?: string;
  status: 'running' | 'success' | 'failed' | 'partial';
  stepResults: { stepId: string; result: AgentTaskResult }[];
  error?: string;
}

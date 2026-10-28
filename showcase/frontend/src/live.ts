// Live reviews: types mirror showcase/backend/tasks.py.

export type StageStatus = 'pending' | 'active' | 'done' | 'skipped' | 'stopped' | 'failed'
export type TaskStatus = 'starting' | 'running' | 'archiving' | 'checking' | 'done' | 'failed' | 'cancelled' | 'interrupted'

export type Params = { topic: string; category: string; start: string; end: string; count: number }

export type Snapshot = {
  id: string
  params: Params
  prompt: string
  model: string
  status: TaskStatus
  error: string | null
  created: number
  elapsed: number
  stages: { key: string; label: string; status: StageStatus; started: number | null }[]
  feed: { t: number; stage: string | null; text: string; tone?: 'good' | 'warning' | 'critical' | null }[]
  subagents: { started: number; done: number }
  tokens: number
  funnel: { searched: number | null; expanded: number | null; shortlisted: number | null; included: number | null }
  papers: { id: string; title: string; authors: string[]; published: string | null; evidence: number }[]
  batches: string[][]
  evidence: { e: string; paper: string; section: string | null; para: string | null; quote: string }[]
  evidence_total: number
  gate: { event: string; cited?: number; retrieved?: number }[]
  citations: { verified: { ok: number; of: number }; in_window?: { ok: number; of: number }; in_category?: { ok: number; of: number } } | null
  has_report: boolean
}

export type Health = {
  ok: boolean
  busy: boolean
  model: string
  categories: Record<string, string>
  checks: { key: string; label: string; ok: boolean; detail: string | null }[]
}

export type TaskItem = {
  id: string
  topic: string
  category: string
  status: TaskStatus
  created: number
  elapsed: number
  verified: { ok: number; of: number } | null
}

export const ACTIVE: TaskStatus[] = ['starting', 'running', 'archiving', 'checking']

export const STATUS_TEXT: Record<TaskStatus, [string, string]> = {
  starting: ['', '准备中'],
  running: ['', '进行中'],
  archiving: ['', '保存结果'],
  checking: ['', '核查引用'],
  done: ['good', '已完成'],
  failed: ['critical', '失败'],
  cancelled: ['warning', '已取消'],
  interrupted: ['warning', '已中断'],
}

// Sending this header makes the request non-simple, so other sites cannot trigger a paid run.
export async function postLive<T>(path: string, body?: unknown): Promise<T> {
  const res = await fetch(`/api/live${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CiteGuard': 'live' },
    body: body === undefined ? undefined : JSON.stringify(body),
  })
  const data = await res.json().catch(() => ({}))
  if (!res.ok) throw new Error((data as { detail?: string }).detail ?? `请求失败（${res.status}）`)
  return data as T
}

export const clock = (s: number) => {
  const m = Math.floor(s / 60)
  const sec = Math.floor(s % 60)
  return `${m}:${sec.toString().padStart(2, '0')}`
}

export const isoDaysAgo = (years: number) => {
  const d = new Date()
  d.setFullYear(d.getFullYear() - years)
  return d.toISOString().slice(0, 10)
}

export const today = () => new Date().toISOString().slice(0, 10)

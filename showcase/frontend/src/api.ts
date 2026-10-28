// Types mirror showcase/backend/data.py.

export type Arm = {
  suite: string
  label: string
  runs: number
  clean_runs: number
  wilson95: [number, number]
  topics: number
  topics_clean_every_repeat: number
  delivered: number
  mostly_fabricated: number | null
  verified_rate: number | null
  in_window_rate: number | null
  in_category_rate: number | null
  mean_seconds: number | null
  mean_tokens: number | null
  claims: { judge: string; pairs: number; supported_rate: number | null; verified_only_supported_rate: number | null }
}

export type Overview = { arms: [Arm, Arm]; suites: number; runs: number }

export type SuiteKind = 'live' | 'holdout' | 'dev' | 'smoke' | 'archive'

export type SuiteHead = {
  name: string
  label: string
  kind: SuiteKind
  runs: number
  delivered: number
  clean_runs: number | null
  mean_seconds: number | null
  mean_tokens: number | null
  verified_rate: number | null
  coverage_precision: number | null
}

export type RunRow = {
  run: string
  topic: string
  seconds: number | null
  tokens: number | null
  token_source: string | null
  status: string
  error: string | null
  refs: number | null
  verified: number | null
  in_window: number | null
  in_category: number | null
  gate_final: string | null
  gate_rejections: number
  evidence: number
  clean: boolean | null
  coverage_hits?: number
  coverage_gold?: number
}

export type Suite = SuiteHead & { rows: RunRow[] }

export type CitationRow = {
  id: string
  resolved?: boolean
  verified?: boolean
  in_window?: boolean
  in_category?: boolean
  first_author?: boolean
  year?: boolean
  title?: boolean
}

export type GateEvent = { event: string; [key: string]: unknown }

export type Evidence = {
  e: string
  paper: string
  para?: string
  section?: string
  quote: string
  claim?: string
  source?: string
}

export type Claim = {
  section: string
  kind: string
  text: string
  ids: string[]
  judgments: { id: string; label: string; reason?: string }[]
}

export type Paper = { id: string; title: string; authors?: string[]; published?: string; primary_category?: string }

export type Run = {
  suite: string
  run: string
  topic: string
  prompt: string | null
  model: string | null
  seconds: number | null
  tokens: number | null
  token_source: string | null
  error: string | null
  report: string | null
  citations: { metrics: Record<string, unknown>; rows: CitationRow[] } | null
  gate: GateEvent[]
  claims: { judge: string | null; items: Claim[] } | null
  evidence: Evidence[]
  papers: Paper[]
}

export async function getJSON<T>(path: string): Promise<T> {
  const res = await fetch(`/api${path}`)
  if (!res.ok) throw new Error(res.status === 404 ? '没有找到这项内容' : `请求失败（${res.status}）`)
  return res.json() as Promise<T>
}

export const pct = (x: number | null | undefined, digits = 1) =>
  x == null ? '—' : `${(x * 100).toFixed(digits).replace(/\.0$/, '')}%`

export const secs = (x: number | null | undefined) => (x == null ? '—' : `${Math.round(x)} 秒`)

export const tokens = (x: number | null | undefined) =>
  x == null ? '—' : `${(x / 1e4).toFixed(x >= 1e6 ? 0 : 1)} 万`

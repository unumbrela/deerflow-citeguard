const GATE: Record<string, [string, string]> = {
  accepted: ['good', '通过'],
  rejected: ['critical', '拒收'],
  released_unverified: ['warning', '未核实发布'],
}

export function GateBadge({ event, rejections = 0 }: { event: string | null; rejections?: number }) {
  if (!event) return <span className="muted">—</span>
  const [tone, text] = GATE[event] ?? ['', event]
  return (
    <span className={`badge ${tone}`}>
      {text}
      {rejections > 0 && <span className="muted small">（拒收 {rejections} 次）</span>}
    </span>
  )
}

export function Check({ ok }: { ok: boolean | undefined }) {
  if (ok == null) return <span className="muted">—</span>
  return ok ? <span className="badge good">是</span> : <span className="badge critical">否</span>
}

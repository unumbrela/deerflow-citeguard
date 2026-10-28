import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { getJSON, tokens } from '../api'
import { ACTIVE, STATUS_TEXT, clock, postLive, type Snapshot } from '../live'

const ABOUT: Record<string, string> = {
  method: '主 Agent 读取综述方法：先检索、再筛选、分批读全文，引用必须出自本次检索。',
  search: '插件按主题、时间和类别检索 arXiv，并沿参考文献扩展候选池。日期和类别由代码过滤，不靠模型记忆。',
  screen: '模型按相关度给候选论文打分，入选的论文被分成若干批，交给子 Agent。',
  read: '子 Agent 逐篇阅读 arXiv 全文，把原文引语登记为证据。代码会核对每条引语确实出现在原文里。',
  index: '主 Agent 取回所有已登记的证据和规范引用格式，准备写作。',
  write: '主 Agent 撰写综述，每个论断后标注对应的证据编号 [E#]。',
  gate: '交付时关卡核对：每个编号都要出自本次检索，每个证据标记都要指向对应论文。不通过就拒收并说明原因。',
  check: '运行结束后，展示站点对照 arXiv 官方 API 逐条核对编号、标题、日期和类别。',
}

function useTask(id: string) {
  const [snap, setSnap] = useState<Snapshot | null>(null)
  const [fetchedAt, setFetchedAt] = useState(0)
  const [error, setError] = useState<string | null>(null)
  useEffect(() => {
    let live = true
    let timer: ReturnType<typeof setTimeout>
    const tick = async () => {
      try {
        const s = await getJSON<Snapshot>(`/live/tasks/${encodeURIComponent(id)}`)
        if (!live) return
        setFetchedAt(Date.now())
        setSnap(s)
        setError(null)
        if (ACTIVE.includes(s.status)) timer = setTimeout(tick, 1000)
      } catch (e) {
        if (!live) return
        setError((e as Error).message)
        timer = setTimeout(tick, 3000)
      }
    }
    tick()
    return () => {
      live = false
      clearTimeout(timer)
    }
  }, [id])
  return { snap, error, setSnap, fetchedAt }
}

// Smooth seconds between polls; the clock is only read inside the timer.
function useElapsed(snap: Snapshot | null, fetchedAt: number) {
  const [now, setNow] = useState(0)
  const active = snap ? ACTIVE.includes(snap.status) : false
  useEffect(() => {
    if (!active) return
    const t = setInterval(() => setNow(Date.now()), 250)
    return () => clearInterval(t)
  }, [active])
  if (!snap) return 0
  const extra = active && snap.elapsed > 0 && now > fetchedAt ? (now - fetchedAt) / 1000 : 0
  return snap.elapsed + Math.min(extra, 5)
}

export default function LiveTask() {
  const { id = '' } = useParams()
  const { snap, error, setSnap, fetchedAt } = useTask(id)
  const elapsed = useElapsed(snap, fetchedAt)
  const [cancelling, setCancelling] = useState(false)

  if (error && !snap) return <p className="error">{error}</p>
  if (!snap) return <p className="loading">加载中…</p>

  const active = ACTIVE.includes(snap.status)
  const current = snap.stages.find((s) => s.status === 'active')
  const p = snap.params
  const retry = new URLSearchParams({ ...p, count: String(p.count) }).toString()

  const cancel = async () => {
    if (!confirm('取消这个任务？已经消耗的 token 不会退回。')) return
    setCancelling(true)
    try {
      setSnap(await postLive<Snapshot>(`/tasks/${encodeURIComponent(id)}/cancel`))
    } catch (e) {
      alert((e as Error).message)
    } finally {
      setCancelling(false)
    }
  }

  return (
    <div className="live">
      <div className="crumbs">
        <Link to="/review">在线综述</Link> / {snap.id}
      </div>

      <header className="live-head">
        <div>
          <h1>{p.topic}</h1>
          <div className="live-params">
            <span className="pill">{p.category}</span>
            <span className="pill">
              {p.start} 至 {p.end}
            </span>
            <span className="pill">{p.count} 篇</span>
            <span className="pill">{snap.model}</span>
          </div>
        </div>
        <div className="live-meter">
          <div className={`live-status ${snap.status}`}>
            {active && <span className="pulse-dot" />}
            {STATUS_TEXT[snap.status][1]}
          </div>
          <div className="live-clock">{clock(elapsed)}</div>
          <div className="muted small">{snap.tokens ? `约 ${tokens(snap.tokens)} token` : ' '}</div>
          {active && (
            <button className="btn ghost-danger" onClick={cancel} disabled={cancelling}>
              {cancelling ? '取消中…' : '取消任务'}
            </button>
          )}
        </div>
      </header>

      <div className="live-grid">
        <aside className="timeline" aria-label="阶段">
          {snap.stages.map((s, i) => (
            <div key={s.key} className={`tl-step ${s.status}`}>
              <div className="tl-rail">
                <span className="tl-dot">{s.status === 'done' ? '✓' : s.status === 'failed' ? '×' : ''}</span>
                {i < snap.stages.length - 1 && <span className="tl-line" />}
              </div>
              <div className="tl-body">
                <div className="tl-label">{s.label}</div>
                <div className="tl-time">
                  {s.started != null ? clock(s.started) : s.status === 'skipped' ? '未经过' : ''}
                  {s.key === 'read' && snap.subagents.started > 0 && ` · 子 Agent ${snap.subagents.done}/${snap.subagents.started}`}
                  {s.key === 'gate' && snap.gate.length > 0 && ` · ${gateSummary(snap)}`}
                </div>
              </div>
            </div>
          ))}
        </aside>

        <div className="live-main">
          {snap.status === 'done' && <ResultCard snap={snap} />}
          {['failed', 'cancelled', 'interrupted'].includes(snap.status) && (
            <div className="card end-card">
              <h3>{STATUS_TEXT[snap.status][1]}</h3>
              <p>{snap.error ?? '任务没有完成。'}</p>
              <div className="flow">
                <Link className="btn primary" to={`/review?${retry}`}>
                  用相同设置重新开始
                </Link>
                {snap.has_report && (
                  <Link className="btn" to={`/experiments/live/${snap.id}`}>
                    查看已有结果
                  </Link>
                )}
              </div>
            </div>
          )}

          {active && (
            <div className="card now-card">
              <div className="eyebrow">{current ? '正在进行' : '准备中'}</div>
              <h3>{current?.label ?? '连接 DeerFlow'}</h3>
              <p>{current ? ABOUT[current.key] : '创建对话线程，发送任务。'}</p>
            </div>
          )}

          {snap.funnel.searched != null && <Funnel funnel={snap.funnel} />}

          {snap.papers.length > 0 && <Papers snap={snap} />}

          {snap.evidence.length > 0 && (
            <section className="card">
              <div className="card-head">
                <h3>最新登记的证据</h3>
                <span className="muted small">共 {snap.evidence_total} 条 · 引语已核对出自原文</span>
              </div>
              <div className="quotes">
                {[...snap.evidence].reverse().slice(0, 5).map((e) => (
                  <figure key={e.e} className="quote-item">
                    <blockquote>{e.quote}</blockquote>
                    <figcaption>
                      <span className="ev-chip">{e.e}</span> arXiv:{e.paper}
                      {e.section && ` · ${e.section}`}
                    </figcaption>
                  </figure>
                ))}
              </div>
            </section>
          )}

          <section className="card">
            <div className="card-head">
              <h3>过程记录</h3>
            </div>
            <ol className="feed">
              {[...snap.feed].reverse().map((f, i) => (
                <li key={`${f.t}-${i}`} className={f.tone ?? ''}>
                  <span className="feed-time">{clock(f.t)}</span>
                  <span className="feed-text">{f.text}</span>
                </li>
              ))}
            </ol>
          </section>

          <details className="prompt-box">
            <summary>发送给 Agent 的任务</summary>
            <p>{snap.prompt}</p>
          </details>
        </div>
      </div>
    </div>
  )
}

function gateSummary(snap: Snapshot) {
  const rejected = snap.gate.filter((g) => g.event === 'rejected').length
  const last = snap.gate[snap.gate.length - 1]?.event
  const verdict = last === 'accepted' ? '通过' : last === 'rejected' ? '拒收' : '未核实放行'
  if (last === 'accepted' && !rejected) return '一次通过'
  return rejected && last !== 'rejected' ? `拒收 ${rejected} 次后${verdict}` : verdict
}

function Funnel({ funnel }: { funnel: Snapshot['funnel'] }) {
  const steps = [
    ['检索', funnel.searched],
    ['引用扩展', funnel.expanded != null ? `+${funnel.expanded}` : null],
    ['初选', funnel.shortlisted],
    ['入选', funnel.included],
  ].filter(([, v]) => v != null) as [string, number | string][]
  return (
    <section className="card">
      <div className="card-head">
        <h3>选文漏斗</h3>
        <span className="muted small">日期与类别由代码过滤</span>
      </div>
      <div className="funnel">
        {steps.map(([label, value], i) => (
          <div key={label} className={`funnel-step${i === steps.length - 1 ? ' last' : ''}`}>
            <div className="funnel-value">{value}</div>
            <div className="funnel-label">{label}</div>
          </div>
        ))}
      </div>
    </section>
  )
}

function Papers({ snap }: { snap: Snapshot }) {
  const batchOf = new Map<string, number>()
  snap.batches.forEach((b, i) => b.forEach((id) => batchOf.set(id, i + 1)))
  const read = snap.papers.filter((p) => p.evidence > 0).length
  return (
    <section className="card">
      <div className="card-head">
        <h3>入选论文</h3>
        <span className="muted small">
          {read}/{snap.papers.length} 篇已有证据
          {snap.batches.length > 0 && ` · 分 ${snap.batches.length} 批阅读`}
        </span>
      </div>
      <div className="paper-grid">
        {snap.papers.map((p) => (
          <a
            key={p.id}
            className={`paper${p.evidence > 0 ? ' lit' : ''}`}
            href={`https://arxiv.org/abs/${p.id}`}
            target="_blank"
            rel="noreferrer"
          >
            <div className="paper-top">
              <span className="paper-id">{p.id}</span>
              {batchOf.has(p.id) && <span className="paper-batch">第 {batchOf.get(p.id)} 批</span>}
            </div>
            <div className="paper-title">{p.title}</div>
            <div className="paper-meta">
              {p.authors[0] ?? ''}
              {p.authors.length > 1 ? ' 等' : ''} · {p.published?.slice(0, 4)}
            </div>
            <div className="paper-ev" aria-label={`${p.evidence} 条证据`}>
              {Array.from({ length: Math.min(p.evidence, 8) }, (_, i) => (
                <span key={i} className="ev-dot" />
              ))}
              <span className="muted small">{p.evidence ? `${p.evidence} 条证据` : '等待阅读'}</span>
            </div>
          </a>
        ))}
      </div>
    </section>
  )
}

function ResultCard({ snap }: { snap: Snapshot }) {
  const v = snap.citations?.verified
  const last = snap.gate[snap.gate.length - 1]?.event
  const allTrue = v ? v.ok === v.of : null
  return (
    <div className="card result-card">
      <div className="result-mark">{allTrue && last === 'accepted' ? '✓' : '!'}</div>
      <div className="result-body">
        <h2>综述已完成</h2>
        <div className="result-stats">
          <Stat label="引用核查" value={v ? `${v.ok}/${v.of}` : '—'} note={v ? (allTrue ? '全部可在 arXiv 查到' : '有引用未通过') : '未完成'} />
          <Stat label="关卡" value={last === 'accepted' ? '通过' : last === 'rejected' ? '拒收' : last ? '未核实' : '—'} note={gateSummary(snap)} />
          <Stat label="原文证据" value={String(snap.evidence_total)} note="条引语" />
          <Stat label="用时" value={clock(snap.elapsed)} note={snap.tokens ? `约 ${tokens(snap.tokens)} token` : ''} />
        </div>
        <div className="flow">
          <Link className="btn primary" to={`/experiments/live/${snap.id}`}>
            阅读完整报告
          </Link>
          <a className="btn" href={`/api/suites/live/runs/${snap.id}/references.bib`} download>
            BibTeX
          </a>
          {snap.evidence_total > 0 && (
            <a className="btn" href={`/api/suites/live/runs/${snap.id}/evidence.csv`} download>
              证据 CSV
            </a>
          )}
          <Link className="btn" to="/review">
            开始新的综述
          </Link>
        </div>
      </div>
    </div>
  )
}

function Stat({ label, value, note }: { label: string; value: string; note?: string }) {
  return (
    <div className="result-stat">
      <div className="stat-label">{label}</div>
      <div className="result-value">{value}</div>
      {note && <div className="stat-note">{note}</div>}
    </div>
  )
}
